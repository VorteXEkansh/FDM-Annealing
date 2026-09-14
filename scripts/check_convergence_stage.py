"""Recompute Stage 10 convergence tables, verify provenance, and draw plots."""
from __future__ import annotations

import csv
import hashlib
import json
import math
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.run_convergence_study import numeric_rows

RUN_ROOT = ROOT / "simulation/convergence"
OUT = ROOT / "convergence"
FIG = ROOT / "figures"

STRUCTURAL_MESH = [
    ("coarse", "stage10_structural_mesh_coarse_a03"),
    ("medium", "stage10_structural_mesh_medium_a01"),
    ("fine", "stage10_structural_mesh_fine_a01"),
    ("extra_fine", "stage10_structural_mesh_extra_fine_a01"),
    ("ultra_fine", "stage10_structural_mesh_ultra_fine_a01"),
]
THERMAL_MESH = [
    ("coarse", "stage10_thermal_mesh_coarse_a01"),
    ("medium", "stage10_thermal_mesh_medium_a01"),
    ("fine", "stage10_thermal_mesh_fine_a01"),
    ("extra_fine", "stage10_thermal_mesh_extra_fine_a01"),
]
CONTACT_MESH = [
    ("coarse", "stage10_contact_mesh_lagrange_coarse_a03"),
    ("medium", "stage10_contact_mesh_lagrange_medium_a03"),
    ("fine", "stage10_contact_mesh_lagrange_fine_a03"),
    ("extra_fine", "stage10_contact_mesh_lagrange_extra_fine_a03"),
]
STRUCTURAL_TIME = [
    ("coarse", "stage10_structural_time_coarse_a01"),
    ("medium", "stage10_structural_time_medium_a01"),
    ("fine", "stage10_structural_mesh_fine_a01"),
    ("extra_fine", "stage10_structural_time_extra_fine_a01"),
]
THERMAL_TIME = [
    ("coarse", "stage10_thermal_time_coarse_a01"),
    ("medium", "stage10_thermal_time_medium_a01"),
    ("fine", "stage10_thermal_mesh_extra_fine_a01"),
    ("extra_fine", "stage10_thermal_time_extra_fine_a01"),
]
CONTACT_SENSITIVITY = [
    ("penalty_fkn_0p1", "stage10_contact_penalty_fkn_0p1_a03"),
    ("penalty_fkn_1", "stage10_contact_penalty_fkn_1_a03"),
    ("penalty_fkn_10", "stage10_contact_penalty_fkn_10_a03"),
    ("augmented_fkn_0p1", "stage10_contact_augmented_fkn_0p1_a03"),
    ("augmented_fkn_1", "stage10_contact_mesh_fine_a03"),
    ("augmented_fkn_10", "stage10_contact_augmented_fkn_10_a03"),
    ("normal_lagrange", "stage10_contact_normal_lagrange_a03"),
    ("augmented_mu_0p1", "stage10_contact_augmented_mu_0p1_a03"),
    ("augmented_mu_0p3", "stage10_contact_augmented_mu_0p3_a03"),
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_run(name: str) -> dict:
    run = RUN_ROOT / name
    manifest = json.loads((run / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["accepted"] and manifest["returncode"] == 0, name
    for filename, expected in manifest["files"].items():
        assert digest(run / filename) == expected, (name, filename)
    text = (run / "mapdl.out").read_text(errors="replace")
    assert "*** ERROR ***" not in text and "BUILD= 26.1" in text and "UP20260202" in text, name
    return {
        "name": name,
        "path": run,
        "case": json.loads((run / "case.json").read_text(encoding="utf-8")),
        "result": json.loads((run / "result.json").read_text(encoding="utf-8")),
        "mapdl": text,
    }


def delta_percent(current: float, previous: float) -> float | None:
    if current == 0.0:
        return 0.0 if previous == 0.0 else None
    return abs(current - previous) / abs(current) * 100.0


def profile_values(result: dict) -> list[float]:
    return [temperature for time in sorted(result["profile"], key=float) for _, temperature in result["profile"][time]]


def profile_l2_excursion(result: dict) -> float:
    values = profile_values(result)
    return math.sqrt(sum((value - 20.0) ** 2 for value in values) / len(values))


def profile_rmse(first: dict, second: dict) -> float:
    a, b = profile_values(first), profile_values(second)
    if len(a) != len(b):
        raise ValueError("profile grids differ")
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)) / len(a))


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def mesh_table(design: dict) -> tuple[list[dict], dict[str, list[dict]]]:
    groups: dict[str, list[dict]] = {}
    specifications = [
        ("structural", STRUCTURAL_MESH, [
            ("W_max", "w_max_mm", "mm", design["acceptance"]["mesh_global_response_limit_percent"]),
            ("residual_displacement", "residual_displacement_mm", "mm", design["acceptance"]["mesh_global_response_limit_percent"]),
            ("residual_stress_p95", "residual_stress_p95_MPa", "MPa", design["acceptance"]["mesh_local_stress_or_peak_pressure_limit_percent"]),
        ]),
        ("thermal", THERMAL_MESH, [
            ("thermal_lag_at_300_s", "thermal_lag_C", "degC", design["acceptance"]["mesh_global_response_limit_percent"]),
            ("temperature_gradient_at_300_s", "temperature_gradient_C_per_m", "degC/m", design["acceptance"]["mesh_global_response_limit_percent"]),
        ]),
        ("contact_normal_lagrange", CONTACT_MESH, [
            ("mean_contact_pressure", "mean_contact_pressure_MPa", "MPa", design["acceptance"]["mesh_global_response_limit_percent"]),
            ("maximum_contact_pressure", "max_contact_pressure_MPa", "MPa", design["acceptance"]["mesh_local_stress_or_peak_pressure_limit_percent"]),
            ("maximum_penetration", "max_penetration_mm", "mm", design["acceptance"]["mesh_global_response_limit_percent"]),
            ("normal_reaction", "normal_reaction_N_per_mm", "N/mm", design["acceptance"]["mesh_global_response_limit_percent"]),
        ]),
    ]
    rows: list[dict] = []
    for model, sequence, metrics in specifications:
        runs = [(level, load_run(name)) for level, name in sequence]
        groups[model] = []
        previous_values: dict[str, float] = {}
        for ordinal, (level, run) in enumerate(runs, 1):
            case, result = run["case"], run["result"]
            if model == "structural":
                solid_elements = case["nx"] * case["nz"]
                nodes = (case["nx"] + 1) * (case["nz"] + 1)
            elif model == "thermal":
                solid_elements = case["nz"]
                nodes = 4 * (case["nz"] + 1)
            else:
                solid_elements = case["nx"] * case["ny"]
                nodes = (case["nx"] + 1) * (case["ny"] + 1)
            for label, key, unit, limit in metrics:
                value = float(result[key])
                previous = previous_values.get(key)
                change = None if previous is None else abs(value - previous)
                delta = None if previous is None else delta_percent(value, previous)
                passed = "" if previous is None else (delta is not None and delta <= limit)
                row = {
                    "model": model,
                    "level": level,
                    "ordinal": ordinal,
                    "solid_elements": solid_elements,
                    "nodes": nodes,
                    "quantity": label,
                    "value": f"{value:.12g}",
                    "unit": unit,
                    "previous_level": "" if ordinal == 1 else runs[ordinal - 2][0],
                    "absolute_change": "" if change is None else f"{change:.12g}",
                    "delta_percent": "" if delta is None else f"{delta:.9g}",
                    "limit_percent": f"{limit:.9g}",
                    "passed": passed,
                    "run_path": str(run["path"].relative_to(ROOT)).replace("\\", "/"),
                    "evidence": "A: genuine MAPDL solver output; derived metric recomputed from raw extraction",
                }
                rows.append(row)
                groups[model].append(row)
                previous_values[key] = value
    return rows, groups


def timestep_table(design: dict) -> tuple[list[dict], dict[str, list[dict]]]:
    rows: list[dict] = []
    groups: dict[str, list[dict]] = {}
    specs = [
        ("structural", STRUCTURAL_TIME, [
            ("W_max", "w_max_mm", "mm", design["acceptance"]["time_global_response_limit_percent"]),
            ("residual_displacement", "residual_displacement_mm", "mm", design["acceptance"]["time_global_response_limit_percent"]),
            ("residual_stress_p95", "residual_stress_p95_MPa", "MPa", design["acceptance"]["time_local_stress_limit_percent"]),
        ]),
        ("thermal", THERMAL_TIME, [
            ("thermal_lag_at_300_s", "thermal_lag_C", "degC", design["acceptance"]["time_global_response_limit_percent"]),
            ("temperature_gradient_at_300_s", "temperature_gradient_C_per_m", "degC/m", design["acceptance"]["time_global_response_limit_percent"]),
            ("temperature_profile_L2_excursion", "profile_l2", "degC", design["acceptance"]["time_global_response_limit_percent"]),
        ]),
    ]
    for model, sequence, metrics in specs:
        runs = [(level, load_run(name)) for level, name in sequence]
        groups[model] = []
        previous_values: dict[str, float] = {}
        previous_result = None
        for ordinal, (level, run) in enumerate(runs, 1):
            case, result = run["case"], run["result"]
            extended = dict(result)
            if model == "thermal":
                extended["profile_l2"] = profile_l2_excursion(result)
            for label, key, unit, limit in metrics:
                value = float(extended[key])
                previous = previous_values.get(key)
                delta = None if previous is None else delta_percent(value, previous)
                row = {
                    "model": model,
                    "level": level,
                    "ordinal": ordinal,
                    "thermal_dt_s": case.get("dt_s", ""),
                    "structural_ramp_dt_s": case.get("ramp_dt_s", ""),
                    "structural_hold_dt_s": case.get("hold_dt_s", ""),
                    "quantity": label,
                    "value": f"{value:.12g}",
                    "unit": unit,
                    "previous_level": "" if ordinal == 1 else runs[ordinal - 2][0],
                    "absolute_change": "" if previous is None else f"{abs(value - previous):.12g}",
                    "delta_percent": "" if delta is None else f"{delta:.9g}",
                    "profile_RMSE_C_vs_previous": (
                        f"{profile_rmse(result, previous_result):.12g}"
                        if model == "thermal" and previous_result is not None else ""
                    ),
                    "limit_percent": f"{limit:.9g}",
                    "passed": "" if delta is None else (delta <= limit),
                    "run_path": str(run["path"].relative_to(ROOT)).replace("\\", "/"),
                    "evidence": "A: genuine MAPDL solver output; derived metric recomputed from raw extraction",
                }
                rows.append(row)
                groups[model].append(row)
                previous_values[key] = value
            previous_result = result
    return rows, groups


def contact_table() -> list[dict]:
    loaded = [(case_id, load_run(name)) for case_id, name in CONTACT_SENSITIVITY]
    baseline = next(run for case_id, run in loaded if case_id == "augmented_fkn_1")["result"]
    rows = []
    expected_algorithms = {
        "penalty": "Penalty method",
        "augmented_lagrange": "Augmented Lagrange method",
        "normal_lagrange": "Lagrange multiplier method",
    }
    for case_id, run in loaded:
        case, result, text = run["case"], run["result"], run["mapdl"]
        algorithm = case["algorithm"]
        assert expected_algorithms[algorithm] in text, case_id
        if algorithm != "normal_lagrange":
            match = re.search(r"Contact stiffness factor FKN\s+([0-9.E+\-]+)", text)
            assert match and math.isclose(float(match.group(1)), float(case["FKN_factor"]), rel_tol=1e-6), case_id
        raw = numeric_rows(run["path"] / "contact_values.csv", 6)
        pressure_closed_fraction = sum(row[2] > 1e-12 for row in raw) / len(raw)
        pressure = float(result["mean_contact_pressure_MPa"])
        peak = float(result["max_contact_pressure_MPa"])
        penetration = float(result["max_penetration_mm"])
        requirements = (
            int(result["solver_return_code"]) == 0
            and int(result["mapdl_error_count"]) == 0
            and pressure_closed_fraction == 1.0
            and pressure >= 0.0
            and peak >= pressure
            and math.isfinite(penetration)
            and int(result["converged_message_count"]) > 0
        )
        def versus(key: str) -> str:
            change = delta_percent(float(result[key]), float(baseline[key]))
            return "" if change is None else f"{change:.9g}"
        rows.append({
            "case": case_id,
            "algorithm": algorithm,
            "FKN_factor": case["FKN_factor"],
            "friction_coefficient": case["friction_coefficient"],
            "mean_contact_pressure_MPa": f"{pressure:.12g}",
            "mean_pressure_change_vs_augmented_FKN1_percent": versus("mean_contact_pressure_MPa"),
            "maximum_contact_pressure_MPa": f"{peak:.12g}",
            "peak_pressure_change_vs_augmented_FKN1_percent": versus("max_contact_pressure_MPa"),
            "maximum_penetration_mm": f"{penetration:.12g}",
            "penetration_change_vs_augmented_FKN1_percent": versus("max_penetration_mm"),
            "normal_reaction_N_per_mm": f"{float(result['normal_reaction_N_per_mm']):.12g}",
            "pressure_closed_fraction": f"{pressure_closed_fraction:.9g}",
            "maximum_friction_stress_MPa": f"{float(result['max_friction_stress_MPa']):.12g}",
            "converged_message_count": result["converged_message_count"],
            "warning_count": result["mapdl_warning_count"],
            "contact_requirements_passed": requirements,
            "run_path": str(run["path"].relative_to(ROOT)).replace("\\", "/"),
            "evidence": "A: genuine MAPDL solver output",
        })
    return rows


def plot_tables(mesh_rows: list[dict], time_rows: list[dict], contact_rows: list[dict]) -> None:
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 9, "axes.titlesize": 10, "axes.labelsize": 9, "figure.dpi": 140})
    FIG.mkdir(parents=True, exist_ok=True)
    colors = {"structural": "#24576b", "thermal": "#cc6b32", "contact_normal_lagrange": "#4c7a52"}
    panels = [
        ("structural", "W_max", r"$W_{\max}$ (mm)"),
        ("structural", "residual_displacement", "Residual displacement (mm)"),
        ("structural", "residual_stress_p95", r"Residual $\sigma_{\mathrm{res},95}$ (MPa)"),
        ("thermal", "temperature_gradient_at_300_s", "Temperature gradient (°C m⁻¹)"),
        ("contact_normal_lagrange", "mean_contact_pressure", "Mean contact pressure (MPa)"),
        ("contact_normal_lagrange", "maximum_contact_pressure", "Peak contact pressure (MPa)"),
    ]
    fig, axes = plt.subplots(2, 3, figsize=(10.2, 6.2), constrained_layout=True)
    for ax, (model, quantity, ylabel) in zip(axes.flat, panels):
        subset = [row for row in mesh_rows if row["model"] == model and row["quantity"] == quantity]
        x = [int(row["solid_elements"]) for row in subset]
        y = [float(row["value"]) for row in subset]
        ax.plot(x, y, "o-", color=colors[model], linewidth=1.7, markersize=4)
        ax.set_xscale("log")
        ax.set_xlabel("Solid elements")
        ax.set_ylabel(ylabel)
        ax.grid(True, alpha=0.25)
        ax.set_title({"structural": "Two-layer Prony benchmark", "thermal": "Plane-wall benchmark", "contact_normal_lagrange": "Normal-Lagrange contact"}[model])
    fig.suptitle("Stage 10 mesh refinement: genuine MAPDL verification responses", fontsize=12, fontweight="bold")
    fig.savefig(FIG / "mesh_convergence.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    panels = [
        ("thermal", "thermal_lag_at_300_s", "Thermal lag (°C)", "thermal_dt_s"),
        ("thermal", "temperature_profile_L2_excursion", "Profile L2 excursion (°C)", "thermal_dt_s"),
        ("structural", "W_max", r"$W_{\max}$ (mm)", "structural_ramp_dt_s"),
        ("structural", "residual_stress_p95", r"Residual $\sigma_{\mathrm{res},95}$ (MPa)", "structural_ramp_dt_s"),
    ]
    fig, axes = plt.subplots(2, 2, figsize=(8.4, 6.2), constrained_layout=True)
    for ax, (model, quantity, ylabel, step_key) in zip(axes.flat, panels):
        subset = [row for row in time_rows if row["model"] == model and row["quantity"] == quantity]
        x = [float(row[step_key]) for row in subset]
        y = [float(row["value"]) for row in subset]
        ax.plot(x, y, "o-", color=colors[model], linewidth=1.7, markersize=4)
        ax.set_xscale("log")
        ax.invert_xaxis()
        ax.set_xlabel("Time increment (s)")
        ax.set_ylabel(ylabel)
        ax.grid(True, alpha=0.25)
    fig.suptitle("Stage 10 time-step refinement: genuine MAPDL verification responses", fontsize=12, fontweight="bold")
    fig.savefig(FIG / "timestep_convergence.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.6), constrained_layout=True)
    for algorithm, marker in (("penalty", "o"), ("augmented_lagrange", "s")):
        subset = [row for row in contact_rows if row["algorithm"] == algorithm and float(row["friction_coefficient"]) == 0.0]
        subset.sort(key=lambda row: float(row["FKN_factor"]))
        axes[0].plot([float(row["FKN_factor"]) for row in subset], [float(row["maximum_penetration_mm"]) for row in subset], marker + "-", label=algorithm.replace("_", " "))
    axes[0].set_xscale("log"); axes[0].set_yscale("log")
    axes[0].set_xlabel(r"$F_{\mathrm{KN}}$ factor"); axes[0].set_ylabel("Maximum penetration (mm)")
    axes[0].grid(True, which="both", alpha=0.25); axes[0].legend(frameon=False)
    friction = [row for row in contact_rows if row["algorithm"] == "augmented_lagrange" and float(row["FKN_factor"]) == 1.0]
    friction.sort(key=lambda row: float(row["friction_coefficient"]))
    mu = [float(row["friction_coefficient"]) for row in friction]
    axes[1].plot(mu, [float(row["mean_contact_pressure_MPa"]) for row in friction], "o-", label="mean pressure")
    axes[1].plot(mu, [float(row["maximum_contact_pressure_MPa"]) for row in friction], "s-", label="peak pressure")
    axes[1].set_xlabel("Friction coefficient, μ"); axes[1].set_ylabel("Contact pressure (MPa)")
    axes[1].grid(True, alpha=0.25); axes[1].legend(frameon=False)
    fig.suptitle("Stage 10 contact-control sensitivity: 40-element interface", fontsize=12, fontweight="bold")
    fig.savefig(FIG / "contact_sensitivity.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    design = json.loads((ROOT / "simulation/cases/stage10_convergence_design.json").read_text(encoding="utf-8"))
    mesh_rows, mesh_groups = mesh_table(design)
    time_rows, time_groups = timestep_table(design)
    contact_rows = contact_table()
    write_csv(OUT / "mesh_convergence.csv", mesh_rows)
    write_csv(OUT / "timestep_convergence.csv", time_rows)
    write_csv(OUT / "contact_sensitivity.csv", contact_rows)
    plot_tables(mesh_rows, time_rows, contact_rows)

    def final_pair_pass(rows: list[dict], level: str) -> bool:
        selected = [row for row in rows if row["level"] == level]
        return bool(selected) and all(str(row["passed"]).lower() == "true" for row in selected)

    all_selected_runs = {name for _, name in STRUCTURAL_MESH + THERMAL_MESH + CONTACT_MESH + STRUCTURAL_TIME + THERMAL_TIME + CONTACT_SENSITIVITY}
    all_runs = sorted(path.name for path in RUN_ROOT.glob("stage10_*") if path.is_dir())
    report = {
        "stage": 10,
        "date": "2026-09-14",
        "passed": True,
        "raw_run_directory_count": len(all_runs),
        "selected_run_count": len(all_selected_runs),
        "excluded_or_rejected_run_count": len(set(all_runs) - all_selected_runs),
        "mesh_rows": len(mesh_rows),
        "timestep_rows": len(time_rows),
        "contact_sensitivity_rows": len(contact_rows),
        "verification_discretization": {
            "structural": "90 x 12 elements confirmed by 120 x 16; verification benchmark only",
            "thermal": "32 through-thickness elements confirmed by 64; verification benchmark only",
            "contact": "40 contact elements on a 40 x 16 solid grid confirmed by 60 on 60 x 24; normal Lagrange; verification benchmark only",
            "thermal_time_step": "0.25 s confirmed by 0.125 s",
            "structural_time_steps": "0.01 s ramps and 0.1 s holds confirmed by 0.005 s and 0.05 s",
        },
        "final_pair_checks": {
            "structural_mesh_extra_to_ultra": final_pair_pass(mesh_groups["structural"], "ultra_fine"),
            "thermal_mesh_fine_to_extra": final_pair_pass(mesh_groups["thermal"], "extra_fine"),
            "contact_mesh_fine_to_extra": final_pair_pass(mesh_groups["contact_normal_lagrange"], "extra_fine"),
            "structural_time_fine_to_extra": final_pair_pass(time_groups["structural"], "extra_fine"),
            "thermal_time_fine_to_extra": final_pair_pass(time_groups["thermal"], "extra_fine"),
        },
        "production_mesh_selected": False,
        "production_sweeps_admitted": False,
        "reason": "Production material, irreversible strain, thermal boundary/contact and three-dimensional contact definitions remain evidence-gated; verification convergence cannot qualify an unbuilt production model.",
        "source_hashes": {
            path: digest(ROOT / path) for path in [
                "scripts/run_convergence_study.py",
                "scripts/check_convergence_stage.py",
                "simulation/cases/stage10_convergence_design.json",
                "simulation/cases/stage10_convergence_design_revision_03.json",
                "simulation/cases/stage10_convergence_design_revision_04.json",
                "simulation/cases/stage10_convergence_design_revision_05.json",
                "simulation/cases/stage10_convergence_design_revision_06.json",
                "simulation/cases/stage10_convergence_design_revision_07.json",
            ]
        },
    }
    assert all(report["final_pair_checks"].values())
    (ROOT / "docs/stage_10_convergence_checks.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
    suite = unittest.defaultTestLoader.discover(str(ROOT / "tests"), pattern="test_convergence.py")
    result = unittest.TextTestRunner().run(suite)
    assert result.wasSuccessful()
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
