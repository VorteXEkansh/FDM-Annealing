"""Check balanced source initialization and independent single-arm creep solution."""
from dataclasses import replace
import math
import unittest

from src.constitutive import EvidenceGapError, Prusament
from src.programmed_recovery import initialize, free_step, total_strain


class ProgrammedRoadTests(unittest.TestCase):
    def setUp(self):
        self.m = Prusament.from_database()

    def test_internal_energy_can_exist_without_net_traction(self):
        state = initialize(self.m, 0.056175)
        self.assertGreater(state.equilibrium_stress, 0)
        self.assertTrue(all(h<0 for h in state.branch_stresses))
        self.assertAlmostEqual(state.stress, 0, places=14)
        self.assertEqual(state.mechanical_strain,0)

    def test_single_arm_independent_solution(self):
        # Under zero traction: d(e+p)/dξ = -E∞(e+p)/[(E∞+E1)τ1].
        m = replace(self.m, equilibrium=2., branches=((8.,1.),))
        p = 0.01
        solution = p*(math.exp(-2*3/(2+8))-1)
        errors = []
        for n in (2,8,32,128):
            state=initialize(m,p)
            for _ in range(n):
                state=free_step(m,state,65.,65.,3./n)
            self.assertAlmostEqual(state.stress,0,places=14)
            errors.append(abs(state.mechanical_strain-solution))
        self.assertTrue(all(a>b*10 for a,b in zip(errors,errors[1:])),errors)
        self.assertLess(errors[-1],5e-8)

    def test_free_asymptote_and_reversible_branch(self):
        p = 0.056175
        state = free_step(self.m,initialize(self.m,p),75.,75.,1e8)
        self.assertAlmostEqual(state.mechanical_strain,-p,places=8)
        passive=initialize(self.m,0.)
        hot=free_step(self.m,passive,23.,75.,30.)
        cold=free_step(self.m,hot,75.,23.,10.)
        self.assertGreater(total_strain(self.m, hot,75,23),0)
        self.assertEqual(total_strain(self.m,cold,23,23),0)

    def test_temperature_guard_applies_even_to_prescribed_histories(self):
        with self.assertRaises(EvidenceGapError):
            free_step(self.m,initialize(self.m,0.0),22.,75.,30.)
