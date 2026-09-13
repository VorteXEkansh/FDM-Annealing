import unittest

from ansys.thermal_model import PHASES, ThermalEvidenceGap, load_case, production_blockers, require_production_ready


class ProductionThermalModelTests(unittest.TestCase):
    def setUp(self):
        self.case = load_case()

    def test_complete_cycle_schema_is_present(self):
        self.assertEqual(tuple(self.case["cycle"]), PHASES)

    def test_geometry_gate_is_true(self):
        self.assertTrue(self.case["admission"]["geometry_verified"])

    def test_missing_same_grade_properties_are_blockers(self):
        blockers = production_blockers(self.case)
        self.assertIn("material.thermal_conductivity_table", blockers)
        self.assertIn("material.specific_heat_table", blockers)

    def test_contact_and_radiation_decisions_are_blockers(self):
        blockers = production_blockers(self.case)
        self.assertIn("boundaries.thermal_contact", blockers)
        self.assertIn("boundaries.radiation.relevance_decision", blockers)

    def test_production_execution_fails_closed(self):
        with self.assertRaises(ThermalEvidenceGap):
            require_production_ready(self.case)


if __name__ == "__main__":
    unittest.main()
