"""Synthetic arithmetic tests only; never published as experimental validation."""
import unittest
from analysis.validation_metrics import compare, bounded_interpretation

class ValidationMetricsTests(unittest.TestCase):
    def test_signed_and_aggregated(self):
        r=compare([-1,3],[-2,1])
        self.assertEqual(r['signed_error'],[1,2])
        self.assertEqual(r['relative_error_percent'],[50,200])
        self.assertEqual(r['MAE'],1.5)
        self.assertAlmostEqual(r['RMSE'],2.5**0.5)
    def test_zero_does_not_become_zero_error(self):
        r=compare([1,0],[0,0])
        self.assertEqual(r['relative_error_percent'],[None,None])
        self.assertEqual(r['absolute_error'],[1,0])
    def test_bad_inputs(self):
        for p,o in [([],[]),([1],[]),([float('nan')],[1]),([1],[float('inf')])]:
            with self.assertRaises(ValueError): compare(p,o)
    def test_bounds_are_not_assumed(self):
        self.assertEqual(bounded_interpretation(.1), 'indeterminate_missing_uncertainty')
        self.assertEqual(bounded_interpretation(.2,.1,.1),'compatible_with_declared_bounds')
        self.assertEqual(bounded_interpretation(.3,.1,.1),'discrepancy_exceeds_declared_bounds')
        with self.assertRaises(ValueError): bounded_interpretation(.1,-1,.1)

if __name__=='__main__': unittest.main()
