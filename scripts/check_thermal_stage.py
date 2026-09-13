"""Stage 8 transient-thermal solver and analytical-verification integrity."""
from __future__ import annotations

import csv
import hashlib
import json
import math
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ansys.thermal_model import load_case, production_blockers
from scripts.run_thermal_verification import CONFIG, analytical_center_temperature, parse_solver_csv

RUN = ROOT / "simulation/verification/stage08_attempt_05"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    checks = []

    def check(name: str, condition: bool) -> None:
        assert condition, name
        checks.append({"check": name, "status": "pass"})

    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    manifest = json.loads((RUN / "manifest.json").read_text(encoding="utf-8"))
    output = (RUN / "mapdl.out").read_text(errors="replace")
    check("Accepted MAPDL execution returned zero", manifest["accepted"] and manifest["status"] == "accepted" and manifest["returncode"] == 0)
    check("Exact MAPDL build and Student product recorded", all(token in output for token in ["RELEASE= 2026 R1", "BUILD= 26.1", "UP20260202", "Academic Student"]))
    check("MAPDL emitted no error messages", "NUMBER OF ERROR   MESSAGES ENCOUNTERED=          0" in output and "*** ERROR ***" not in output)
    check("One explained result-set boundary warning", "NUMBER OF WARNING MESSAGES ENCOUNTERED=          1" in output and "load data are not consistent" in output)
    check("Verification case is explicitly not PLA", "not a physical PLA dataset" in config["verification_material"]["evidence_status"])
    check("Complete ramp-hold-cooling schedule", [p["phase"] for p in config["ambient_history"]] == ["initial ambient", "linear heating ramp", "hot hold", "linear cooling ramp", "ambient recovery"])
    material = config["verification_material"]
    bi = config["boundary"]["convection_coefficient_W_m2K"] * config["geometry"]["thickness_z_m"] / 2 / material["thermal_conductivity_W_mK"]
    check("Biot number reproduced", math.isclose(bi, 0.05, rel_tol=0, abs_tol=1e-15) and math.isclose(manifest["benchmark_Biot_number"], bi))
    check("Accepted input code and output hashes match", all(digest(CONFIG if name == "simulation/cases/thermal_verification_plane_wall.json" else ROOT / name if "/" in name else RUN / name) == value for name, value in manifest["sha256"].items()))
    solver = parse_solver_csv(RUN / "solver_center_temperature.csv")
    with (ROOT / "verification/thermal_verification.csv").open(encoding="utf-8", newline="") as handle:
        published = list(csv.DictReader(handle))
    check("Nine exact comparison times exported", len(solver) == len(published) == 9 and [r["solver_time_s"] for r in solver] == config["comparison_times_s"])
    for raw, row in zip(solver, published):
        reference = analytical_center_temperature(config, raw["solver_time_s"])
        check(f"Analytical temperature reproduced at {raw['solver_time_s']:.0f} s", math.isclose(float(row["analytical_temperature_C"]), reference, rel_tol=0, abs_tol=5e-10))
        check(f"ANSYS temperature preserved at {raw['solver_time_s']:.0f} s", math.isclose(float(row["ansys_temperature_C"]), raw["ansys_center_temperature_C"], rel_tol=0, abs_tol=5e-10))
    max_abs = max(float(r["absolute_error_C"]) for r in published)
    max_rel_exc = max(float(r["relative_excursion_error_percent"]) for r in published)
    check("Absolute acceptance threshold passed", max_abs == 0.0051807 and max_abs <= config["predeclared_acceptance"]["maximum_absolute_error_C"])
    check("Excursion-relative acceptance threshold passed", max_rel_exc == 0.157660518 and max_rel_exc <= config["predeclared_acceptance"]["maximum_excursion_relative_error_percent"])
    counts = [float(v.strip()) for v in (RUN / "mesh_counts.csv").read_text().splitlines()[1].split(",")]
    check("Mapped mesh count preserved", counts == [1025.0, 640.0, 850.0])
    for attempt, expected in [(1, "postprocessing_failed"), (2, "comparison_failed"), (3, "comparison_failed"), (4, "solver_failed")]:
        m = json.loads((ROOT / f"simulation/verification/stage08_attempt_{attempt:02d}/manifest.json").read_text())
        check(f"Failed attempt {attempt:02d} remains traceable", not m.get("accepted", False) and expected in m["status"])
    production = load_case()
    blockers = production_blockers(production)
    check("Production thermal model remains fail closed", len(blockers) >= 8 and all(key in blockers for key in ["material.thermal_conductivity_table", "material.specific_heat_table", "boundaries.convection", "boundaries.thermal_contact", "boundaries.radiation.relevance_decision"]))
    suite = unittest.defaultTestLoader.discover(str(ROOT / "tests"), pattern="test_thermal*.py")
    result = unittest.TextTestRunner(stream=sys.stderr, verbosity=1).run(suite)
    check("Ten thermal unit tests pass", result.wasSuccessful() and result.testsRun == 10)
    report = {
        "stage": 8,
        "date": "2026-09-13",
        "passed": True,
        "checks": checks,
        "count": len(checks),
        "accepted_run": "simulation/verification/stage08_attempt_05",
        "maximum_absolute_error_C": max_abs,
        "maximum_relative_error_percent_K": max(float(r["relative_error_percent_K"]) for r in published),
        "maximum_excursion_relative_error_percent": max_rel_exc,
        "scope": "Genuine MAPDL plane-wall transient thermal code verification and fail-closed production thermal contract; no PLA coupon prediction or physical validation.",
    }
    (ROOT / "docs/stage_08_thermal_checks.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"{len(checks)} thermal checks passed")


if __name__ == "__main__":
    main()
