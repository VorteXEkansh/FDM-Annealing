"""Execute immutable Stage 10 MAPDL convergence cases sequentially.

The models are numerical verification configurations. They do not replace the
missing production Prusament thermal and irreversible-strain evidence.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DESIGN = ROOT / "simulation/cases/stage10_convergence_design.json"
MAPDL = Path(r"C:\Program Files\ANSYS Inc\ANSYS Student\v261\ansys\bin\winx64\ANSYS261.exe")
RUN_ROOT = ROOT / "simulation/convergence"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prony_lines(material_id: int = 1, time_factor: float = 1.0) -> tuple[float, float, list[str]]:
    model = json.loads((ROOT / "material/constitutive_reference.json").read_text(encoding="utf-8"))
    lines: list[str] = []
    for mode in ("SHEAR", "BULK"):
        lines.append(f"TB,PRONY,{material_id},,{len(model['prony'])},{mode}")
        for index, branch in enumerate(model["prony"]):
            lines.append(
                f"TBDATA,{2 * index + 1},{branch['shear_fraction']:.16g},"
                f"{branch['reference_relaxation_time_s'] * time_factor:.16g}"
            )
    return model["instantaneous_moduli_MPa"]["E"], model["poisson_ratio"], lines


def structural_deck(nx: int, nz: int, ramp_dt: float, hold_dt: float) -> str:
    length, height, total_force = 60.0, 4.0, -0.001
    modulus, poisson, prony_lower = prony_lines(1, 1.0)
    _, _, prony_upper = prony_lines(2, 10.0)
    lines = [
        "/BATCH", "/FILNAME,stage10_structural", "/TITLE,Stage 10 isothermal discretization verification",
        "/PREP7", "ET,1,182", "KEYOPT,1,3,3", "R,1,1", "TYPE,1", "REAL,1", "MAT,1",
        f"MP,EX,1,{modulus:.16g}", f"MP,PRXY,1,{poisson:.16g}", *prony_lower,
        f"MP,EX,2,{modulus:.16g}", f"MP,PRXY,2,{poisson:.16g}", *prony_upper,
    ]
    node = lambda ix, iz: iz * (nx + 1) + ix + 1
    for iz in range(nz + 1):
        for ix in range(nx + 1):
            lines.append(f"N,{node(ix, iz)},{length * ix / nx:.16g},{height * iz / nz:.16g},0")
    for iz in range(nz):
        lines.append(f"MAT,{1 if iz < nz / 2 else 2}")
        for ix in range(nx):
            lines.append(f"E,{node(ix, iz)},{node(ix + 1, iz)},{node(ix + 1, iz + 1)},{node(ix, iz + 1)}")
    for iz in range(nz + 1):
        lines.extend([f"D,{node(0, iz)},UX,0", f"D,{node(0, iz)},UY,0"])
    lines.extend([
        "FINISH", "/SOLU", "ANTYPE,STATIC", "NLGEOM,OFF", "AUTOTS,OFF", "KBC,0",
        "OUTRES,ERASE", "OUTRES,ALL,LAST", "TREF,65", "BF,ALL,TEMP,65",
    ])
    traction = total_force / height
    for iz in range(nz + 1):
        weight = (height / nz) * (0.5 if iz in (0, nz) else 1.0)
        lines.append(f"F,{node(nx, iz)},FY,{traction * weight:.16g}")
    lines.extend([
        "TIME,1", f"DELTIM,{ramp_dt:.16g},{ramp_dt:.16g},{ramp_dt:.16g}", "SOLVE",
        "TIME,31", f"DELTIM,{hold_dt:.16g},{hold_dt:.16g},{hold_dt:.16g}", "SOLVE",
    ])
    for iz in range(nz + 1):
        lines.append(f"FDELE,{node(nx, iz)},FY")
    lines.extend([
        "TIME,32", f"DELTIM,{ramp_dt:.16g},{ramp_dt:.16g},{ramp_dt:.16g}", "SOLVE",
        "TIME,62", f"DELTIM,{hold_dt:.16g},{hold_dt:.16g},{hold_dt:.16g}", "SOLVE",
        "FINISH", "/POST1", "SET,,,,,62", "ETABLE,SEQV,S,EQV",
        "*CFOPEN,top_nodes,csv",
    ])
    for ix in range(nx + 1):
        nid = node(ix, nz)
        lines.extend([
            f"NIDV={nid}", f"*GET,XV,NODE,{nid},LOC,X", f"*GET,YV,NODE,{nid},LOC,Y",
            f"*GET,UXV,NODE,{nid},U,X", f"*GET,UYV,NODE,{nid},U,Y",
            "*VWRITE,NIDV,XV,YV,UXV,UYV", "(5(E24.16,','))",
        ])
    lines.extend(["*CFCLOS", "*CFOPEN,element_stress,csv"])
    for eid in range(1, nx * nz + 1):
        lines.extend([
            f"EIDV={eid}", f"*GET,XV,ELEM,{eid},CENT,X", f"*GET,YV,ELEM,{eid},CENT,Y",
            f"*GET,SV,ELEM,{eid},ETAB,SEQV", "*VWRITE,EIDV,XV,YV,SV", "(4(E24.16,','))",
        ])
    lines.extend(["*CFCLOS", "FINISH", "/EXIT,NOSAVE"])
    return "\n".join(lines) + "\n"


def thermal_deck(nz: int, dt: float) -> str:
    length = 0.010
    times = [300.0, 900.0, 1200.0, 1800.0]
    history = [(300.0, 80.0), (900.0, 80.0), (1200.0, 20.0), (1800.0, 20.0)]
    lines = [
        "/BATCH", "/FILNAME,stage10_thermal", "/TITLE,Stage 10 plane-wall discretization verification",
        "/PREP7", "ET,1,70", "MP,KXX,1,0.5", "MP,KYY,1,0.5", "MP,KZZ,1,0.5",
        "MP,C,1,1000", "MP,DENS,1,1000", "TYPE,1", "MAT,1",
    ]
    for iz in range(nz + 1):
        z = length * iz / nz
        base = 4 * iz
        lines.extend([
            f"N,{base + 1},0,0,{z:.16g}", f"N,{base + 2},0.001,0,{z:.16g}",
            f"N,{base + 3},0.001,0.001,{z:.16g}", f"N,{base + 4},0,0.001,{z:.16g}",
        ])
    for iz in range(nz):
        low, high = 4 * iz, 4 * (iz + 1)
        lines.append(f"E,{low + 1},{low + 2},{low + 3},{low + 4},{high + 1},{high + 2},{high + 3},{high + 4}")
    lines.extend([
        "FINISH", "/SOLU", "ANTYPE,TRANS", "TRNOPT,FULL", "AUTOTS,OFF", "KBC,0",
        "OUTRES,ERASE", "*DIM,TS,ARRAY,4", "TS(1)=300", "TS(2)=900", "TS(3)=1200", "TS(4)=1800",
        "OUTRES,NSOL,%TS%", "TUNIF,20",
    ])
    bottom, top = (1, 4), (4 * nz + 1, 4 * (nz + 1))
    def convection(temp: float) -> list[str]:
        return [
            f"NSEL,S,NODE,,{bottom[0]},{bottom[1]}", f"SF,ALL,CONV,5,{temp:.16g}",
            f"NSEL,S,NODE,,{top[0]},{top[1]}", f"SF,ALL,CONV,5,{temp:.16g}", "ALLSEL,ALL",
        ]
    lines.extend(convection(20.0))
    lines.extend(["TIME,1e-6", "KBC,1", "NSUBST,1,1,1", "SOLVE", "KBC,0"])
    for time_s, ambient in history:
        lines.extend(convection(ambient))
        lines.extend([f"TIME,{time_s:.16g}", f"DELTIM,{dt:.16g},{dt:.16g},{dt:.16g},ON", "SOLVE"])
    lines.extend(["FINISH", "/POST1", "*CFOPEN,temperature_profile,csv"])
    for time_s in times:
        lines.append(f"SET,,,,,{time_s:.16g}")
        for iz in range(nz + 1):
            nid = 4 * iz + 1
            lines.extend([
                f"TV={time_s:.16g}", f"ZV={length * iz / nz:.16g}", f"*GET,TEMPV,NODE,{nid},TEMP",
                "*VWRITE,TV,ZV,TEMPV", "(3(E24.16,','))",
            ])
    lines.extend(["*CFCLOS", "FINISH", "/EXIT,NOSAVE"])
    return "\n".join(lines) + "\n"


def contact_deck(nx: int, ny: int, algorithm: str, fkn: float, friction: float) -> str:
    width, height, gap = 10.0, 4.0, 0.020
    key = {"augmented_lagrange": 0, "penalty": 1, "normal_lagrange": 4}[algorithm]
    lines = [
        "/BATCH", "/FILNAME,stage10_contact", "/TITLE,Stage 10 contact-control verification",
        "/PREP7", "ET,1,182", "KEYOPT,1,3,2", "ET,2,169", "ET,3,172",
        f"KEYOPT,3,2,{key}", "KEYOPT,3,4,0", "KEYOPT,3,10,1",
        "R,1,1", f"R,3,0,0,{fkn:.16g},0.1,0,2", "MP,EX,1,2000", "MP,PRXY,1,0.3",
        "MP,ALPX,1,0.0001", f"MP,MU,1,{friction:.16g}", "TYPE,1", "REAL,1", "MAT,1",
    ]
    node = lambda ix, iy: iy * (nx + 1) + ix + 1
    for iy in range(ny + 1):
        for ix in range(nx + 1):
            lines.append(f"N,{node(ix, iy)},{width * ix / nx:.16g},{height * iy / ny:.16g},0")
    for iy in range(ny):
        for ix in range(nx):
            lines.append(f"E,{node(ix, iy)},{node(ix + 1, iy)},{node(ix + 1, iy + 1)},{node(ix, iy + 1)}")
    for ix in range(nx + 1):
        lines.append(f"D,{node(ix, 0)},UY,0")
    lines.append(f"D,{node(0, 0)},UX,0")
    target_a, target_b = 900001, 900002
    lines.extend([
        f"N,{target_a},0,{height + gap:.16g},0", f"N,{target_b},{width:.16g},{height + gap:.16g},0",
        f"D,{target_a},ALL,0", f"D,{target_b},ALL,0", "TYPE,2", "REAL,3", "MAT,1",
        f"E,{target_a},{target_b}", "TYPE,3", "REAL,3", "MAT,1",
    ])
    first_contact = nx * ny + 2
    for ix in range(nx):
        lines.append(f"E,{node(ix + 1, ny)},{node(ix, ny)}")
    lines.extend([
        "ALLSEL,ALL", "FINISH", "/SOLU", "ANTYPE,STATIC", "NLGEOM,ON", "AUTOTS,ON", "KBC,0",
        "NROPT,FULL", "OUTRES,ALL,LAST", "TREF,20",
        f"NSEL,S,NODE,,1,{(nx + 1) * (ny + 1)}", "BF,ALL,TEMP,120", "ALLSEL,ALL",
        "TIME,1", "NSUBST,20,200,5", "SOLVE", "FINISH", "/POST1", "SET,LAST",
        "ETABLE,CPRES,CONT,PRES", "ETABLE,PENE,CONT,PENE", "ETABLE,CSTAT,CONT,STAT",
        "ETABLE,CSFRIC,CONT,SFRIC", "*CFOPEN,contact_values,csv",
    ])
    for offset in range(nx):
        eid = first_contact + offset
        xmid = width * (offset + 0.5) / nx
        lines.extend([
            f"EIDV={eid}", f"XV={xmid:.16g}", f"*GET,PV,ELEM,{eid},ETAB,CPRES",
            f"*GET,PENV,ELEM,{eid},ETAB,PENE", f"*GET,STATV,ELEM,{eid},ETAB,CSTAT",
            f"*GET,FRICV,ELEM,{eid},ETAB,CSFRIC", "*VWRITE,EIDV,XV,PV,PENV,STATV,FRICV",
            "(6(E24.16,','))",
        ])
    lines.extend(["*CFCLOS", "*CFOPEN,reaction,csv", "RFY=0"])
    for ix in range(nx + 1):
        lines.extend([f"*GET,RV,NODE,{node(ix, 0)},RF,FY", "RFY=RFY+RV"])
    lines.extend(["*VWRITE,RFY", "(E24.16)", "*CFCLOS", "FINISH", "/EXIT,NOSAVE"])
    return "\n".join(lines) + "\n"


def numeric_rows(path: Path, columns: int) -> list[list[float]]:
    rows: list[list[float]] = []
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.reader(handle, skipinitialspace=True):
            if len(row) < columns:
                continue
            try:
                rows.append([float(value.strip()) for value in row[:columns]])
            except ValueError:
                continue
    if not rows:
        raise ValueError(f"no {columns}-column numeric records in {path}")
    return rows


def percentile(values: list[float], fraction: float) -> float:
    ordered = sorted(values)
    position = fraction * (len(ordered) - 1)
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    return ordered[lower] * (upper - position) + ordered[upper] * (position - lower)


def parse_structural(run: Path) -> dict:
    nodes = numeric_rows(run / "top_nodes.csv", 5)
    stress = numeric_rows(run / "element_stress.csv", 4)
    deformed = [(row[1] + row[3], row[2] + row[4]) for row in nodes]
    xbar = sum(x for x, _ in deformed) / len(deformed)
    ybar = sum(y for _, y in deformed) / len(deformed)
    denominator = sum((x - xbar) ** 2 for x, _ in deformed)
    slope = sum((x - xbar) * (y - ybar) for x, y in deformed) / denominator
    intercept = ybar - slope * xbar
    warpage = max(abs(y - (intercept + slope * x)) for x, y in deformed)
    displacement = max(math.hypot(row[3], row[4]) for row in nodes)
    interior = [abs(row[3]) for row in stress if 6.0 <= row[1] <= 54.0]
    if not interior:
        raise ValueError("no interior stress records")
    return {
        "w_max_mm": warpage,
        "residual_displacement_mm": displacement,
        "residual_stress_p95_MPa": percentile(interior, 0.95),
        "top_node_count": len(nodes),
        "element_count": len(stress),
    }


def parse_thermal(run: Path) -> dict:
    rows = numeric_rows(run / "temperature_profile.csv", 3)
    grouped: dict[float, list[tuple[float, float]]] = {}
    for time_s, z, temperature in rows:
        grouped.setdefault(time_s, []).append((z, temperature))
    for values in grouped.values():
        values.sort()
    profile = grouped[300.0]
    center = min(profile, key=lambda item: abs(item[0] - 0.005))[1]
    surface = 0.5 * (profile[0][1] + profile[-1][1])
    return {
        "thermal_lag_C": 80.0 - center,
        "temperature_gradient_C_per_m": abs(surface - center) / 0.005,
        "center_temperature_C": center,
        "profile": {f"{time_s:.0f}": values for time_s, values in sorted(grouped.items())},
        "through_thickness_divisions": len(profile) - 1,
    }


def parse_contact(run: Path, width: float = 10.0) -> dict:
    rows = numeric_rows(run / "contact_values.csv", 6)
    reaction = numeric_rows(run / "reaction.csv", 1)[0][0]
    pressure = [max(0.0, row[2]) for row in rows]
    penetration = [abs(min(0.0, row[3])) for row in rows]
    if max(penetration, default=0.0) == 0.0:
        penetration = [abs(row[3]) for row in rows]
    closed = [row[4] >= 2.0 for row in rows]
    friction = [abs(row[5]) for row in rows]
    return {
        "mean_contact_pressure_MPa": sum(pressure) / len(pressure),
        "max_contact_pressure_MPa": max(pressure),
        "max_penetration_mm": max(penetration),
        "normal_reaction_N_per_mm": reaction,
        "closed_fraction": sum(closed) / len(closed),
        "max_friction_stress_MPa": max(friction),
        "contact_element_count": len(rows),
        "contact_width_mm": width,
        "raw_pressure_min_MPa": min(row[2] for row in rows),
        "raw_pressure_max_MPa": max(row[2] for row in rows),
        "raw_penetration_min_mm": min(row[3] for row in rows),
        "raw_penetration_max_mm": max(row[3] for row in rows),
        "raw_status_min": min(row[4] for row in rows),
        "raw_status_max": max(row[4] for row in rows),
    }


def execute(case_id: str, attempt: int, case: dict, deck: str, parser) -> dict:
    run = RUN_ROOT / f"stage10_{case_id}_a{attempt:02d}"
    run.mkdir(parents=True, exist_ok=False)
    (run / "input.dat").write_text(deck, encoding="ascii", newline="\n")
    case = dict(case)
    case.update({
        "case_id": case_id,
        "attempt": attempt,
        "design_sha256": digest(DESIGN),
        "structural_revision_sha256": (
            digest(ROOT / "simulation/cases/stage10_convergence_design_revision_03.json")
            if case["family"].startswith("structural") else None
        ),
        "supplemental_revision_sha256": (
            digest(ROOT / "simulation/cases/stage10_convergence_design_revision_04.json")
            if case_id == "structural_mesh_ultra_fine" else None
        ),
        "contact_mapping_revision_sha256": (
            digest(ROOT / "simulation/cases/stage10_convergence_design_revision_05.json")
            if case["family"].startswith("contact") else None
        ),
        "contact_control_revision_sha256": (
            digest(ROOT / "simulation/cases/stage10_convergence_design_revision_07.json")
            if case["family"].startswith("contact") else None
        ),
        "contact_mesh_revision_sha256": (
            digest(ROOT / "simulation/cases/stage10_convergence_design_revision_06.json")
            if case["family"] == "contact_mesh_lagrange" else None
        ),
        "evidence_status": "genuine MAPDL numerical verification; not a production PLA annealing result",
    })
    (run / "case.json").write_text(json.dumps(case, indent=2) + "\n", encoding="utf-8", newline="\n")
    shutil.copyfile(__file__, run / "script_snapshot.py")
    with tempfile.TemporaryDirectory(prefix=f"FDM_stage10_{case_id}_") as temp_name:
        scratch = Path(temp_name)
        shutil.copyfile(run / "input.dat", scratch / "input.dat")
        command = [str(MAPDL), "-b", "-i", str(scratch / "input.dat"), "-o", str(scratch / "mapdl.out"), "-j", "stage10", "-np", "1"]
        completed = subprocess.run(command, cwd=scratch, capture_output=True)
        (run / "stdout.log").write_bytes(completed.stdout)
        (run / "stderr.log").write_bytes(completed.stderr)
        for path in scratch.iterdir():
            if path.is_file() and path.name != "input.dat":
                shutil.copyfile(path, run / path.name)
    mapdl_text = (run / "mapdl.out").read_text(errors="replace") if (run / "mapdl.out").exists() else ""
    accepted = False
    error = ""
    result: dict = {}
    try:
        if completed.returncode != 0:
            raise RuntimeError(f"solver return code {completed.returncode}")
        if "*** ERROR ***" in mapdl_text:
            raise RuntimeError("MAPDL error in output")
        if "BUILD= 26.1" not in mapdl_text or "UP20260202" not in mapdl_text:
            raise RuntimeError("unexpected MAPDL version")
        result = parser(run)
        result.update({
            "mapdl_warning_count": mapdl_text.count("*** WARNING ***"),
            "mapdl_error_count": mapdl_text.count("*** ERROR ***"),
            "converged_message_count": mapdl_text.upper().count("CONVERGED"),
            "solver_return_code": completed.returncode,
        })
        (run / "result.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
        accepted = True
    except Exception as exc:
        error = f"{type(exc).__name__}: {exc}"
    files = {path.name: digest(path) for path in sorted(run.iterdir()) if path.is_file() and path.name != "manifest.json"}
    manifest = {
        "accepted": accepted,
        "error": error,
        "returncode": completed.returncode,
        "command": command,
        "files": files,
    }
    (run / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"{run.name}: accepted={accepted}; {error or result}")
    return manifest


def cases(design: dict) -> list[tuple[str, dict, str, object]]:
    output: list[tuple[str, dict, str, object]] = []
    level_factor = design["mesh_levels"]
    for level, factor in level_factor.items():
        nx, nz = 15 * factor, 2 * factor
        case = {"family": "structural_mesh", "design_revision": 3, "level": level, "nx": nx, "nz": nz, "ramp_dt_s": 0.01, "hold_dt_s": 0.1}
        output.append((f"structural_mesh_{level}", case, structural_deck(nx, nz, 0.01, 0.1), parse_structural))
    case = {"family": "structural_mesh", "design_revision": 3, "level": "ultra_fine", "nx": 120, "nz": 16, "ramp_dt_s": 0.01, "hold_dt_s": 0.1}
    output.append(("structural_mesh_ultra_fine", case, structural_deck(120, 16, 0.01, 0.1), parse_structural))
    for level, nz in design["thermal_mesh"]["through_thickness_divisions"].items():
        case = {"family": "thermal_mesh", "level": level, "nz": nz, "dt_s": 0.25}
        output.append((f"thermal_mesh_{level}", case, thermal_deck(nz, 0.25), parse_thermal))
    for level, divisions in design["contact_mesh"]["divisions"].items():
        nx, ny = divisions
        case = {"family": "contact_mesh", "level": level, "nx": nx, "ny": ny, "algorithm": "augmented_lagrange", "FKN_factor": 1.0, "friction_coefficient": 0.0}
        output.append((f"contact_mesh_{level}", case, contact_deck(nx, ny, "augmented_lagrange", 1.0, 0.0), parse_contact))
        lagrange_case = {"family": "contact_mesh_lagrange", "design_revision": 6, "level": level, "nx": nx, "ny": ny, "algorithm": "normal_lagrange", "FKN_factor": 1.0, "friction_coefficient": 0.0}
        output.append((f"contact_mesh_lagrange_{level}", lagrange_case, contact_deck(nx, ny, "normal_lagrange", 1.0, 0.0), parse_contact))
    for level, values in design["time_step_strategies"].items():
        if level != "fine":
            case = {"family": "structural_time", "design_revision": 3, "level": level, "nx": 60, "nz": 8, "ramp_dt_s": values["structural_ramp_dt_s"], "hold_dt_s": values["structural_hold_dt_s"]}
            output.append((f"structural_time_{level}", case, structural_deck(60, 8, values["structural_ramp_dt_s"], values["structural_hold_dt_s"]), parse_structural))
        if level not in ("fine",):
            dt = values["thermal_dt_s"]
            case = {"family": "thermal_time", "level": level, "nz": 64, "dt_s": dt}
            output.append((f"thermal_time_{level}", case, thermal_deck(64, dt), parse_thermal))
    for sensitivity in design["contact_sensitivity_cases"]:
        if sensitivity["id"] == "augmented_fkn_1":
            continue
        case = {"family": "contact_sensitivity", "nx": 40, "ny": 16, **sensitivity}
        output.append((
            f"contact_{sensitivity['id']}", case,
            contact_deck(40, 16, sensitivity["algorithm"], sensitivity["FKN_factor"], sensitivity["friction_coefficient"]),
            parse_contact,
        ))
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--attempt", type=int, default=1)
    parser.add_argument("--case", help="execute only the exact generated case id")
    parser.add_argument("--family", help="execute only one case family")
    args = parser.parse_args()
    design = json.loads(DESIGN.read_text(encoding="utf-8"))
    selected = []
    for case_id, case, deck, result_parser in cases(design):
        if args.case and case_id != args.case:
            continue
        if args.family and case["family"] != args.family:
            continue
        selected.append((case_id, case, deck, result_parser))
    if not selected:
        raise SystemExit("no matching case")
    failed = []
    for case_id, case, deck, result_parser in selected:
        if not execute(case_id, args.attempt, case, deck, result_parser)["accepted"]:
            failed.append(case_id)
    if failed:
        raise SystemExit("failed cases: " + ", ".join(failed))


if __name__ == "__main__":
    main()
