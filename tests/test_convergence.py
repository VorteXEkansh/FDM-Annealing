import csv
import json
import math
import unittest
from pathlib import Path

from scripts.check_convergence_stage import delta_percent, profile_l2_excursion

ROOT = Path(__file__).resolve().parents[1]


class ConvergenceTests(unittest.TestCase):
    def test_requested_delta_definition(self):
        self.assertAlmostEqual(delta_percent(12.0, 11.0), 100.0 / 12.0)

    def test_zero_denominator_rule(self):
        self.assertEqual(delta_percent(0.0, 0.0), 0.0)
        self.assertIsNone(delta_percent(0.0, 1.0))

    def test_profile_norm(self):
        result = {"profile": {"1": [[0.0, 20.0], [1.0, 30.0]]}}
        self.assertAlmostEqual(profile_l2_excursion(result), math.sqrt(50.0))

    def test_verification_selection_does_not_claim_production_mesh(self):
        report = json.loads((ROOT / "docs/stage_10_convergence_checks.json").read_text(encoding="utf-8"))
        self.assertFalse(report["production_mesh_selected"])
        self.assertFalse(report["production_sweeps_admitted"])

    def test_final_refinement_pairs_pass(self):
        report = json.loads((ROOT / "docs/stage_10_convergence_checks.json").read_text(encoding="utf-8"))
        self.assertTrue(all(report["final_pair_checks"].values()))

    def test_required_csvs_have_solver_traceability(self):
        for name in ("mesh_convergence.csv", "timestep_convergence.csv", "contact_sensitivity.csv"):
            with (ROOT / "convergence" / name).open(encoding="utf-8", newline="") as handle:
                rows = list(csv.DictReader(handle))
            self.assertTrue(rows)
            self.assertTrue(all(row["run_path"].startswith("simulation/convergence/") for row in rows))


if __name__ == "__main__":
    unittest.main()
