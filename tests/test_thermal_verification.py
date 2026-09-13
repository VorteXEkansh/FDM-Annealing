import json
import math
import unittest
from pathlib import Path

from scripts.run_thermal_verification import (
    CONFIG,
    analytical_center_temperature,
    center_step_modes,
    root_bisect,
    validate,
)


class ThermalVerificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = json.loads(CONFIG.read_text(encoding="utf-8"))

    def test_config_is_admitted_verification_fixture(self):
        validate(self.config)

    def test_plane_wall_roots_satisfy_characteristic_equation(self):
        bi = 0.05
        for mode in range(8):
            root = root_bisect(bi, mode)
            self.assertAlmostEqual(root * math.tan(root), bi, places=11)

    def test_modal_coefficients_reconstruct_initial_center_ratio(self):
        coefficients = [coefficient for coefficient, _ in center_step_modes(self.config)]
        # The finite 200-mode truncation leaves a bounded 1.3e-7 remainder.
        self.assertLess(abs(sum(coefficients) - 1.0), 2.0e-7)

    def test_initial_temperature(self):
        self.assertAlmostEqual(analytical_center_temperature(self.config, 0.0), 20.0, places=12)

    def test_history_heats_then_cools_without_overshoot(self):
        values = [analytical_center_temperature(self.config, t) for t in self.config["comparison_times_s"]]
        self.assertTrue(all(20.0 <= value <= 80.0 for value in values))
        self.assertGreater(values[4], values[1])
        self.assertLess(values[-1], values[4])


if __name__ == "__main__":
    unittest.main()
