"""Run and compare a genuine MAPDL plane-wall transient thermal benchmark.

The benchmark constants are declared numerical fixtures. They are deliberately
separate from the project PLA database and must never be used in a production
annealing case.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "simulation/cases/thermal_verification_plane_wall.json"
MAPDL = Path(r"C:\Program Files\ANSYS Inc\ANSYS Student\v261\ansys\bin\winx64\ANSYS261.exe")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def root_bisect(bi: float, mode: int) -> float:
    """Return root of z*tan(z)=Bi on (n*pi, n*pi+pi/2)."""
    lo = mode * math.pi + (1e-14 if mode else 0.0)
    hi = mode * math.pi + math.pi / 2.0 - 1e-14
    for _ in range(120):
        mid = (lo + hi) / 2.0
        value = mid * math.tan(mid) - bi
        if value > 0.0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2.0


def center_step_modes(config: dict) -> list[tuple[float, float]]:
    material = config["verification_material"]
    thickness = config["geometry"]["thickness_z_m"]
    half = thickness / 2.0
    h = config["boundary"]["convection_coefficient_W_m2K"]
    k = material["thermal_conductivity_W_mK"]
    alpha = k / (material["density_kg_m3"] * material["specific_heat_J_kgK"])
    bi = h * half / k
    modes = []
    for n in range(config["analytical_series_terms"]):
        zeta = root_bisect(bi, n)
        coefficient = 4.0 * math.sin(zeta) / (2.0 * zeta + math.sin(2.0 * zeta))
        decay = zeta * zeta * alpha / (half * half)
        modes.append((coefficient, decay))
    return modes


def analytical_center_temperature(config: dict, time_s: float) -> float:
    """Duhamel integral of the exact plane-wall step response for linear ramps."""
    history = config["ambient_history"]
    value = config["initial_temperature_C"]
    modes = center_step_modes(config)
    for left, right in zip(history[:-1], history[1:]):
        a, b = left["time_s"], right["time_s"]
        if time_s <= a:
            continue
        q = min(time_s, b)
        slope = (right["temperature_C"] - left["temperature_C"]) / (b - a)
        if slope == 0.0:
            continue
        duration = q - a
        response_integral = duration
        for coefficient, decay in modes:
            response_integral -= coefficient * (
                math.exp(-decay * (time_s - q))
                - math.exp(-decay * (time_s - a))
            ) / decay
        value += slope * response_integral
    return value


def validate(config: dict) -> None:
    if config["case_kind"] != "thermal_verification":
        raise ValueError("only a thermal_verification case is admitted")
    if "not a physical PLA dataset" not in config["verification_material"]["evidence_status"]:
        raise ValueError("verification-only evidence label is missing")
    history = config["ambient_history"]
    if history[0]["time_s"] != 0.0 or history[0]["temperature_C"] != config["initial_temperature_C"]:
        raise ValueError("ambient and solid must share the declared initial state")
    if any(b["time_s"] <= a["time_s"] for a, b in zip(history[:-1], history[1:])):
        raise ValueError("ambient-history times must increase")
    if config["time_step_s"] <= 0 or any(t <= 0 for t in config["comparison_times_s"]):
        raise ValueError("time steps and comparison times must be positive")
    if max(config["comparison_times_s"]) > history[-1]["time_s"]:
        raise ValueError("comparison time is outside the solution history")
    required = [
        config["verification_material"]["thermal_conductivity_W_mK"],
        config["verification_material"]["specific_heat_J_kgK"],
        config["verification_material"]["density_kg_m3"],
        config["boundary"]["convection_coefficient_W_m2K"],
    ]
    if not all(v > 0 for v in required):
        raise ValueError("thermal properties and convection must be positive")


def apdl_deck(config: dict) -> str:
    g = config["geometry"]
    m = config["verification_material"]
    h = config["boundary"]["convection_coefficient_W_m2K"]
    dt = config["time_step_s"]
    times = config["comparison_times_s"]
    hist = config["ambient_history"]
    initial = config["initial_temperature_C"]
    assignments = "\n".join(f"TS({i})={t:.12g}" for i, t in enumerate(times, 1))
    load_steps = []
    for point in hist[1:]:
        load_steps.extend([
            "ASEL,S,LOC,Z,0",
            f"ASEL,A,LOC,Z,{g['thickness_z_m']:.12g}",
            f"SFA,ALL,1,CONV,{h:.12g},{point['temperature_C']:.12g}",
            "ALLSEL,ALL",
            f"TIME,{point['time_s']:.12g}",
            "KBC,0",
            f"DELTIM,{dt:.12g},{dt:.12g},{dt:.12g},ON",
            "SOLVE",
        ])
    return f"""/BATCH
/FILNAME,stage08_thermal
/TITLE,Stage 8 analytical plane-wall thermal verification only
/PREP7
ET,1,70
MP,KXX,1,{m['thermal_conductivity_W_mK']:.12g}
MP,KYY,1,{m['thermal_conductivity_W_mK']:.12g}
MP,KZZ,1,{m['thermal_conductivity_W_mK']:.12g}
MP,C,1,{m['specific_heat_J_kgK']:.12g}
MP,DENS,1,{m['density_kg_m3']:.12g}
BLOCK,0,{g['length_x_m']:.12g},0,{g['width_y_m']:.12g},0,{g['thickness_z_m']:.12g}
MSHAPE,0,3D
MSHKEY,1
ESIZE,{g['element_size_m']:.12g}
VMESH,ALL
ALLSEL,ALL
FINISH
/SOLU
ANTYPE,TRANS
TRNOPT,FULL
AUTOTS,OFF
*DIM,TS,ARRAY,{len(times)}
{assignments}
OUTRES,ERASE
OUTRES,NSOL,%TS%
TUNIF,{initial:.12g}
ASEL,S,LOC,Z,0
ASEL,A,LOC,Z,{g['thickness_z_m']:.12g}
SFA,ALL,1,CONV,{h:.12g},{initial:.12g}
ALLSEL,ALL
TIME,1e-6
KBC,1
NSUBST,1,1,1
SOLVE
{chr(10).join(load_steps)}
FINISH
/POST1
ALLSEL,ALL
NSEL,S,LOC,X,{g['length_x_m']/2:.12g}
NSEL,R,LOC,Y,{g['width_y_m']/2:.12g}
NSEL,R,LOC,Z,{g['thickness_z_m']/2:.12g}
*GET,CNODE,NODE,0,NUM,MIN
ALLSEL,ALL
*CFOPEN,solver_center_temperature,csv
*VWRITE,'requested_time_s,solver_time_s,ansys_center_temperature_C'
(A65)
*DO,II,1,{len(times)}
TREQ=TS(II)
SET,,,,,TREQ
*GET,TNOW,ACTIVE,0,SET,TIME
*GET,TC,NODE,CNODE,TEMP
*VWRITE,TREQ,TNOW,TC
(F16.6,',',F16.6,',',E24.16)
*ENDDO
*CFCLOS
ALLSEL,ALL
*GET,NN,NODE,0,COUNT
*GET,NE,ELEM,0,COUNT
*CFOPEN,mesh_counts,csv
*VWRITE,'nodes,elements,center_node'
(A30)
*VWRITE,NN,NE,CNODE
(F16.0,',',F16.0,',',F16.0)
*CFCLOS
FINISH
/EXIT,NOSAVE
"""


def parse_solver_csv(path: Path) -> list[dict[str, float]]:
    # MAPDL character literals are limited to eight characters in *VWRITE;
    # parse the fixed three-column numeric records and assign explicit names.
    with path.open(encoding="utf-8-sig", newline="") as handle:
        records = list(csv.reader(handle, skipinitialspace=True))
    parsed = []
    for record in records:
        if len(record) != 3:
            continue
        try:
            requested, solver, temperature = (float(value.strip()) for value in record)
        except ValueError:
            continue
        parsed.append({
            "requested_time_s": requested,
            "solver_time_s": solver,
            "ansys_center_temperature_C": temperature,
        })
    if not parsed:
        raise ValueError(f"no three-column numerical records in {path}")
    return parsed


def compare(config: dict, solver_rows: list[dict[str, float]]) -> list[dict[str, str]]:
    output = []
    initial = config["initial_temperature_C"]
    for row in solver_rows:
        time_s = row["solver_time_s"]
        ansys = row["ansys_center_temperature_C"]
        reference = analytical_center_temperature(config, time_s)
        error = abs(ansys - reference)
        rel_kelvin = 100.0 * error / (reference + 273.15)
        excursion = abs(reference - initial)
        rel_excursion = 100.0 * error / excursion if excursion > 1e-12 else 0.0
        output.append({
            "case_id": config["case_id"],
            "location": "slab center",
            "requested_time_s": f"{row['requested_time_s']:.6f}",
            "solver_time_s": f"{time_s:.6f}",
            "ansys_temperature_C": f"{ansys:.9f}",
            "analytical_temperature_C": f"{reference:.9f}",
            "absolute_error_C": f"{error:.9f}",
            "relative_error_percent_K": f"{rel_kelvin:.9f}",
            "relative_excursion_error_percent": f"{rel_excursion:.9f}",
            "ansys_evidence_class": "A: genuine MAPDL solver output",
            "reference_evidence_class": "B: reproducible analytical calculation",
        })
    return output


def write_comparison(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--publish", action="store_true")
    args = parser.parse_args()
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    validate(config)
    run_dir = ROOT / "simulation/verification" / args.run_id
    if run_dir.exists():
        raise FileExistsError(f"immutable run directory already exists: {run_dir}")
    run_dir.mkdir(parents=True)
    input_path = run_dir / "input.dat"
    input_path.write_text(apdl_deck(config), encoding="ascii", newline="\n")
    shutil.copyfile(CONFIG, run_dir / "case.json")
    command = None
    returncode = None
    if args.execute:
        if not MAPDL.exists():
            raise FileNotFoundError(MAPDL)
        command = [str(MAPDL), "-b", "-i", str(input_path), "-o", str(run_dir / "mapdl.out"), "-j", "stage08_thermal", "-np", "1"]
        with (run_dir / "runner_stdout.log").open("wb") as stdout, (run_dir / "runner_stderr.log").open("wb") as stderr:
            completed = subprocess.run(command, cwd=run_dir, stdout=stdout, stderr=stderr, check=False)
        returncode = completed.returncode
        if returncode != 0:
            status = "solver_failed"
        elif not (run_dir / "solver_center_temperature.csv").exists():
            status = "extraction_missing"
        elif "*** ERROR ***" in (run_dir / "mapdl.out").read_text(errors="replace"):
            status = "mapdl_error_reported"
        else:
            status = "solver_complete"
    else:
        status = "deck_only"

    rows = []
    accepted = False
    if status == "solver_complete":
        solver_rows = parse_solver_csv(run_dir / "solver_center_temperature.csv")
        rows = compare(config, solver_rows)
        write_comparison(run_dir / "comparison.csv", rows)
        max_abs = max(float(r["absolute_error_C"]) for r in rows)
        max_excursion = max(float(r["relative_excursion_error_percent"]) for r in rows)
        acceptance = config["predeclared_acceptance"]
        accepted = max_abs <= acceptance["maximum_absolute_error_C"] and max_excursion <= acceptance["maximum_excursion_relative_error_percent"]
        status = "accepted" if accepted else "comparison_failed_acceptance"
        if args.publish:
            if not accepted:
                raise RuntimeError("verification did not meet predeclared acceptance thresholds")
            target = ROOT / "verification/thermal_verification.csv"
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(run_dir / "comparison.csv", target)

    material = config["verification_material"]
    half = config["geometry"]["thickness_z_m"] / 2.0
    bi = config["boundary"]["convection_coefficient_W_m2K"] * half / material["thermal_conductivity_W_mK"]
    manifest = {
        "run_id": args.run_id,
        "case_id": config["case_id"],
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "accepted": accepted,
        "solver": "Ansys Mechanical APDL Student 2026 R1",
        "returncode": returncode,
        "command": command,
        "benchmark_Biot_number": bi,
        "evidence_boundary": config["purpose"],
        "sha256": {
            "simulation/cases/thermal_verification_plane_wall.json": sha256(CONFIG),
            "scripts/run_thermal_verification.py": sha256(Path(__file__)),
            **{p.name: sha256(p) for p in sorted(run_dir.iterdir()) if p.is_file() and p.name != "manifest.json"},
        },
    }
    (run_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(manifest, indent=2))
    if args.execute and status != "accepted":
        raise SystemExit(2)


if __name__ == "__main__":
    main()
