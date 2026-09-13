import unittest
from scripts.run_structural_verification import spec,references,deck
class StructuralReferences(unittest.TestCase):
    def test_free_cycle(self):
        self.assertAlmostEqual(references(spec('free'),2)['ux_mm'],.006)
        self.assertEqual(references(spec('free'),3)['stress_x_MPa'],0)
    def test_restrained_equilibrium(self):
        r=references(spec('fixed'),2)
        self.assertAlmostEqual(r['stress_x_MPa'],-1.2)
        self.assertAlmostEqual(r['reaction_x_N'],1.2)
    def test_eigenstrain_survives_cooling_and_release(self):
        self.assertAlmostEqual(references(spec('eigen_free'),3)['ux_mm'],-.01)
        self.assertAlmostEqual(references(spec('eigen_fixed'),3)['stress_x_MPa'],2)
        self.assertAlmostEqual(references(spec('eigen_fixed'),4)['ux_mm'],-.01)
    def test_contact_complementarity(self):
        for t in [1,2,3]:
            r=references(spec('contact'),t)
            self.assertGreaterEqual(r['gap_mm'],0)
            self.assertLessEqual(r['contact_force_N'],0)
            self.assertAlmostEqual(r['gap_mm']*r['contact_force_N'],0)
    def test_exact_single_branch_ramp(self):
        import math
        c=spec('visco'); c['E']=1000; c['prony']=[{'shear_fraction':.6,'reference_relaxation_time_s':10}]
        self.assertAlmostEqual(references(c,1)['stress_x_MPa'],.4+6*(1-math.exp(-.1)))
    def test_full_spectrum_and_reference_temperature(self):
        c=spec('visco'); d=deck(c)
        self.assertEqual(len(c['prony']),23)
        self.assertIn('TB,PRONY,1,,23,SHEAR',d)
        self.assertIn('TB,PRONY,1,,23,BULK',d)
        self.assertIn('TREF,65',d)
        self.assertIn('BF,ALL,TEMP,65',d)
