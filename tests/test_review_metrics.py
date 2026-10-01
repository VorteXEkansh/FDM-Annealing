import unittest
from analysis.review_metrics import relative_change


class ReviewMetricsTests(unittest.TestCase):
    def test_both_zero_remains_undefined(self):
        self.assertIsNone(relative_change(0.,0.))

    def test_nonzero_over_zero_remains_undefined(self):
        self.assertIsNone(relative_change(0.,2.))

    def test_signed_denominator_uses_magnitude(self):
        self.assertAlmostEqual(relative_change(-4.,-3.),25.)

    def test_nonfinite_rejected(self):
        with self.assertRaises(ValueError): relative_change(float('nan'),1.)
