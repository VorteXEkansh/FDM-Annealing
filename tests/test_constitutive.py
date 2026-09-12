"""Analytical/synthetic material-point tests. No simulated coupon or validation data."""
import math
import unittest
from dataclasses import replace
from src.constitutive import (Prusament, EvidenceGapError, ZERO, add, sub, scale,
    isotropic_stress, isotropic_strain, fixture_property, fixture_elastic_stress,
    annealing_strain, crystallization, production_annealing_model, fixture_thermal_strain)


class MaterialRelations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = Prusament.from_database()

    def near_tensor(self,a,b,tol=1e-10):
        for x,y in zip(a,b): self.assertAlmostEqual(x,y,delta=tol)

    def test_source_modulus_sum(self):
        self.assertEqual(len(self.m.branches),23)
        self.assertAlmostEqual(self.m.instantaneous,1691.594,places=9)

    def test_reference_shift_is_unity(self):
        self.assertEqual(self.m.shift(65),1.)

    def test_arrhenius_absolute_temperature_and_base(self):
        expected=10**(35000*(1/296.15-1/338.15))
        self.assertAlmostEqual(self.m.shift(23)/expected,1.,places=12)

    def test_wlf_published_coefficients(self):
        self.assertAlmostEqual(self.m.shift(80),10**(-17.4*15/66.6),places=14)

    def test_shift_continuity_and_direction(self):
        self.assertLess(abs(self.m.log10_shift(65-1e-7)),1e-6)
        self.assertLess(abs(self.m.log10_shift(65+1e-7)),1e-6)
        values=[self.m.shift(t) for t in (23,40,60,65,80,85)]
        self.assertTrue(all(a>b for a,b in zip(values,values[1:])))

    def test_outside_characterization_domain_rejected(self):
        for t in (20,22.99,85.01,95,110):
            with self.subTest(t=t),self.assertRaises(EvidenceGapError): self.m.shift(t)

    def test_nonfinite_input_rejected(self):
        for t in (math.nan,math.inf,-math.inf):
            with self.subTest(t=t),self.assertRaises(ValueError): self.m.shift(t)

    def test_thermal_expansion_units_and_shear(self):
        self.near_tensor(self.m.thermal_strain(80),(.003876,)*3+(0.,)*3)

    def test_thermal_cycle_reversible(self):
        self.near_tensor(add(self.m.thermal_strain(80,23),self.m.thermal_strain(23,80)),ZERO)
        self.near_tensor(self.m.thermal_strain(23),ZERO)

    def test_prony_fractions_admissible(self):
        fractions=self.m.normalized_prony()
        self.assertTrue(all(0<g<1 and tau>0 for g,tau in fractions))
        self.assertAlmostEqual(sum(g for g,_ in fractions)+self.m.equilibrium/self.m.instantaneous,1.,places=14)

    def test_relaxation_fast_and_slow_limits(self):
        self.assertAlmostEqual(self.m.relaxation_modulus(0,65),self.m.instantaneous)
        self.assertEqual(self.m.relaxation_modulus(1e6,65),self.m.equilibrium)

    def test_relaxation_monotonic_positive(self):
        values=[self.m.relaxation_modulus(t,65) for t in (0,1e-10,1e-6,.01,1,100,1e6)]
        self.assertTrue(all(a>=b>0 for a,b in zip(values,values[1:])))

    def test_warmer_equal_duration_relaxes_more(self):
        self.assertGreater(self.m.relaxation_modulus(1,23),self.m.relaxation_modulus(1,80))

    def test_shear_bulk_conversion_preserves_poisson(self):
        for t in (0,.001,10,1e6):
            g,k=self.m.shear_bulk(t,65)
            self.assertAlmostEqual(9*k*g/(3*k+g),self.m.relaxation_modulus(t,65),places=9)
            self.assertAlmostEqual((3*k-2*g)/(2*(3*k+g)),.35,places=14)

    def test_shear_only_relaxation_is_not_constant_poisson(self):
        g,k=self.m.shear_bulk(1e6,65)
        _,k_fast=self.m.shear_bulk(0,65)
        self.assertGreater(abs((3*k_fast-2*g)/(2*(3*k_fast+g))-.35),.1)

    def test_compliance_inverts_stiffness(self):
        e=(.001,-.0002,.0004,.0003,-.0001,.0002)
        self.near_tensor(isotropic_strain(isotropic_stress(e,2000,.3),2000,.3),e)

    def test_engineering_to_tensor_shear_factor(self):
        gamma=.002; young=2000; nu=.3
        s=isotropic_stress((0,0,0,gamma/2,0,0),young,nu)
        self.assertAlmostEqual(s[3],young/(2*(1+nu))*gamma)

    def test_hydrostatic_bulk_response(self):
        g,k=self.m.shear_bulk(0,65)
        self.near_tensor(isotropic_stress((.001,)*3+(0.,)*3,self.m.instantaneous,.35),(3*k*.001,)*3+(0.,)*3)

    def test_plane_stress_reduction_matches_source(self):
        ex,ey,gamma=.001,-.0003,.0004; nu=self.m.poisson
        ez=-nu/(1-nu)*(ex+ey)
        s=isotropic_stress((ex,ey,ez,gamma/2,0,0),self.m.instantaneous,nu)
        self.assertAlmostEqual(s[0],self.m.instantaneous/(1-nu**2)*(ex+nu*ey))
        self.assertAlmostEqual(s[1],self.m.instantaneous/(1-nu**2)*(ey+nu*ex))
        self.assertAlmostEqual(s[2],0,places=12)

    def test_strain_partition_closes(self):
        e=(.001,0,0,.0002,0,0)
        state=self.m.advance_reduced(self.m.step_strain_state(e),e,.1)
        elastic,delayed=self.m.strain_parts(state)
        self.near_tensor(add(elastic,delayed),e)
        self.near_tensor(isotropic_stress(elastic,self.m.instantaneous,.35),self.m.stress(state))

    def test_step_relaxation_matches_analytical_modulus(self):
        e=(.001,-.35*.001,-.35*.001,0,0,0)
        state=self.m.advance_reduced(self.m.step_strain_state(e),e,1.)
        self.assertAlmostEqual(self.m.stress(state)[0],.001*self.m.relaxation_modulus(1.,65),places=12)

    def test_single_branch_ramp_exact_integral(self):
        # Synthetic two-modulus model is an analytical fixture, not a PLA property.
        m=replace(self.m,equilibrium=2.,branches=((3.,4.),),poisson=0.)
        state=m.advance_reduced(m.zero_state(),(.01,0,0,0,0,0),2.)
        expected=2*.01+3*.01*(4/2)*(1-math.exp(-2/4))
        self.assertAlmostEqual(m.stress(state)[0],expected,places=14)

    def test_isothermal_partition_invariance(self):
        final=(.001,0,0,0,0,0)
        one=self.m.advance_reduced(self.m.zero_state(),final,.01)
        many=self.m.zero_state()
        for i in range(1,11): many=self.m.advance_reduced(many,scale(final,i/10),.001)
        self.near_tensor(self.m.stress(one),self.m.stress(many))

    def test_zero_loading_has_no_spontaneous_stress(self):
        state=self.m.advance(self.m.zero_state(),ZERO,23,23,1)
        self.near_tensor(self.m.stress(state),ZERO)

    def test_free_reversible_heating_has_no_stress(self):
        state=self.m.zero_state()
        for a,b in ((23,65),(65,80),(80,65),(65,23)):
            state=self.m.advance(state,self.m.thermal_strain(b),a,b,10)
            self.near_tensor(self.m.stress(state),ZERO)

    def test_restrained_heating_compressive_sign(self):
        state=self.m.advance(self.m.zero_state(),ZERO,23,60,10)
        self.assertTrue(all(s<0 for s in self.m.stress(state)[:3]))

    def test_reduced_time_isothermal(self):
        self.assertEqual(self.m.reduced_time(65,65,10),10)
        self.assertAlmostEqual(self.m.reduced_time(80,80,10),10/self.m.shift(80))

    def test_ramp_reduced_time_refinement_and_endpoint_error(self):
        a=self.m.reduced_time(23,85,10,256)
        b=self.m.reduced_time(23,85,10,512)
        self.assertLess(abs(a-b)/b,1e-6)
        self.assertGreater(abs(b-10/self.m.shift(85))/b,1.)

    def test_reduced_time_reversal_and_additivity(self):
        x=self.m.reduced_time(23,85,10,256)
        self.assertAlmostEqual(x,self.m.reduced_time(85,23,10,256),places=8)
        split=self.m.reduced_time(23,65,10*42/62,256)+self.m.reduced_time(65,85,10*20/62,256)
        self.assertAlmostEqual(x,split,places=8)

    def test_nonisothermal_strain_update_refinement(self):
        # Prescribed restrained ramp; discretization of a material relation only.
        def run(n):
            s=self.m.zero_state()
            for a,b in ((23,65),(65,80)):
                for i in range(n): s=self.m.advance(s,ZERO,a+(b-a)*i/n,a+(b-a)*(i+1)/n,10/n)
            return self.m.stress(s)[0]
        coarse,medium,fine,reference=(run(n) for n in (32,64,128,1024))
        self.assertLess(abs(fine-reference),abs(medium-reference))
        self.assertLess(abs(medium-reference),abs(coarse-reference))

    def test_positive_dissipation_branch_form(self):
        # For positive definite C_i and positive tau, s:C_i^-1:s/tau >= 0.
        state=self.m.step_strain_state((.001,-.0002,.0003,.0001,0,0))
        for (k,tau),s in zip(self.m.branches,state.branch_stresses):
            e=isotropic_strain(s,k,.35)
            product=sum(a*b*(1 if j<3 else 2) for j,(a,b) in enumerate(zip(s,e)))
            self.assertGreaterEqual(product/tau,0.)

    def test_small_time_step_avoids_cancellation(self):
        m=replace(self.m,equilibrium=2.,branches=((3.,4.),),poisson=0.)
        state=m.advance_reduced(m.zero_state(),(.01,0,0,0,0,0),1e-18)
        self.assertAlmostEqual(m.stress(state)[0],.05,places=14)

    def test_invalid_steps_and_tg_crossing_rejected(self):
        for dt in (0,-1):
            with self.subTest(dt=dt),self.assertRaises(ValueError): self.m.advance(self.m.zero_state(),ZERO,23,23,dt)
        with self.assertRaises(ValueError): self.m.advance(self.m.zero_state(),ZERO,23,80,1)
        with self.assertRaises(ValueError): self.m.relaxation_modulus(-1,65)
        with self.assertRaises(ValueError): self.m.reduced_time(23,80,1,3)

    def test_missing_mechanisms_fail_closed(self):
        for fn in (annealing_strain,crystallization,production_annealing_model,fixture_thermal_strain):
            with self.subTest(fn=fn.__name__),self.assertRaises(EvidenceGapError): fn()

    def test_fixture_knots_and_interpolation(self):
        self.assertEqual(fixture_property('E',20),200)
        self.assertEqual(fixture_property('k',100),16.6)
        self.assertEqual(fixture_property('ρ',200),7840)
        self.assertAlmostEqual(fixture_property('E',110),190.61)
        for sym in ('ρ','c_p','k','α','E','ν'):
            a,b=fixture_property(sym,100),fixture_property(sym,200)
            self.assertTrue(min(a,b)<=fixture_property(sym,110)<=max(a,b))

    def test_fixture_elastic_units(self):
        self.assertAlmostEqual(fixture_elastic_stress((.001,-.00029,-.00029,0,0,0),20)[0],200)

    def test_fixture_extrapolation_rejected(self):
        for t in (19,201):
            with self.subTest(t=t),self.assertRaises(EvidenceGapError): fixture_property('k',t)

    def test_invalid_material_and_tensor_rejected(self):
        with self.assertRaises(ValueError): replace(self.m,branches=((-1,1),))
        with self.assertRaises(ValueError): isotropic_stress(ZERO,1,.5)
        with self.assertRaises(ValueError): isotropic_stress((1,2,3),1,.3)


if __name__=='__main__': unittest.main()
