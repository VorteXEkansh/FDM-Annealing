"""Stage 5 small-strain reference relations, NOT an ANSYS solver or material card.

Stress/moduli: MPa; time: s; temperature input: deg C; strain: dimensionless.
Symmetric tensors use (xx, yy, zz, xy, yz, xz), with TENSOR shear strains.
No production annealing call is admitted. Missing mechanisms raise errors.
"""
from dataclasses import dataclass
from pathlib import Path
import csv
import math

ROOT = Path(__file__).resolve().parents[1]
ZERO = (0.,) * 6


class EvidenceGapError(ValueError):
    """A requested physical relation has no admitted parameterization."""


def finite(value):
    value = float(value)
    if not math.isfinite(value):
        raise ValueError('Input must be finite')
    return value


def tensor(values):
    values = tuple(finite(x) for x in values)
    if len(values) != 6:
        raise ValueError('Six tensor components required')
    return values


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def scale(a, factor):
    return tuple(x*factor for x in a)


def isotropic_stress(strain, young, poisson):
    e = tensor(strain)
    young, poisson = finite(young), finite(poisson)
    if young <= 0 or not -1 < poisson < .5:
        raise ValueError('Non-positive isotropic stiffness')
    shear = young/(2*(1+poisson))
    lam = young*poisson/((1+poisson)*(1-2*poisson))
    tr = sum(e[:3])
    return tuple(2*shear*v + (lam*tr if j < 3 else 0) for j,v in enumerate(e))


def isotropic_strain(stress, young, poisson):
    s = tensor(stress)
    # Reuse stiffness validation, then apply the analytical compliance.
    isotropic_stress(ZERO, young, poisson)
    tr = sum(s[:3])
    return tuple(((1+poisson)*v-(poisson*tr if j<3 else 0))/young for j,v in enumerate(s))


@dataclass(frozen=True)
class State:
    mechanical_strain: tuple
    branch_stresses: tuple


@dataclass(frozen=True)
class Prusament:
    equilibrium: float
    poisson: float
    alpha: float
    tg: float
    c1: float
    c2: float
    c3: float
    branches: tuple

    def __post_init__(self):
        for value in (self.equilibrium,self.poisson,self.alpha,self.tg,self.c1,self.c2,self.c3):
            finite(value)
        if self.equilibrium <= 0 or not -1 < self.poisson < .5 or self.c2 <= 0:
            raise ValueError('Invalid material constants')
        if not self.branches or any(finite(k)<=0 or finite(tau)<=0 for k,tau in self.branches):
            raise ValueError('Positive branch moduli and times required')

    @classmethod
    def from_database(cls):
        with (ROOT/'material/pla_properties.csv').open(encoding='utf-8-sig',newline='') as f:
            rows = list(csv.DictReader(f))
        def value(symbol):
            return float(next(r['value'] for r in rows if r['property_symbol']==symbol and r['source_key']=='Chapuis2025'))
        ks = {r['component']:float(r['value']) for r in rows if r['property_symbol']=='kᵢ'}
        ts = {r['component']:float(r['value']) for r in rows if r['property_symbol']=='τᵢ'}
        if ks.keys()!=ts.keys() or len(ks)!=23:
            raise ValueError('Incomplete source spectrum')
        return cls(value('E_∞'),value('ν'),value('α')*1e-6,value('T_g'),value('C₁'),value('C₂'),value('C₃'),tuple((k,ts[i]) for i,k in ks.items()))

    @property
    def instantaneous(self):
        return self.equilibrium + math.fsum(k for k,_ in self.branches)

    def temperature(self, temperature):
        t = finite(temperature)
        if not 23 <= t <= 85:
            raise EvidenceGapError('Prusament direct characterization envelope is 23–85 deg C')
        return t

    def log10_shift(self, temperature):
        t = self.temperature(temperature)
        if t < self.tg:
            return self.c3*(1/(t+273.15)-1/(self.tg+273.15))
        return -self.c1*(t-self.tg)/(self.c2+t-self.tg)

    def shift(self, temperature):
        return 10**self.log10_shift(temperature)

    def thermal_strain(self, temperature, reference=23.):
        # Constant source alpha; reference=23 deg C is an explicit test convention.
        value = self.alpha*(self.temperature(temperature)-self.temperature(reference))
        return (value,value,value,0.,0.,0.)

    def relaxation_modulus(self, elapsed, temperature):
        elapsed = finite(elapsed)
        if elapsed < 0:
            raise ValueError('Negative elapsed time')
        shift = self.shift(temperature)
        return self.equilibrium + math.fsum(k*math.exp(-elapsed/(shift*tau)) for k,tau in self.branches)

    def normalized_prony(self):
        """Identical SHEAR and BULK fractions, conditional on constant Poisson ratio."""
        return tuple((k/self.instantaneous,tau) for k,tau in self.branches)

    def shear_bulk(self, elapsed, temperature):
        young = self.relaxation_modulus(elapsed,temperature)
        return young/(2*(1+self.poisson)), young/(3*(1-2*self.poisson))

    def zero_state(self):
        return State(ZERO,tuple(ZERO for _ in self.branches))

    def step_strain_state(self, mechanical_strain):
        """Ideal instantaneous strain jump, for analytical unit tests only."""
        e = tensor(mechanical_strain)
        return State(e,tuple(isotropic_stress(e,k,self.poisson) for k,_ in self.branches))

    def stress(self, state):
        if len(state.branch_stresses)!=len(self.branches):
            raise ValueError('State and spectrum mismatch')
        s = isotropic_stress(state.mechanical_strain,self.equilibrium,self.poisson)
        for b in state.branch_stresses:
            s = add(s,tensor(b))
        return s

    def strain_parts(self, state):
        elastic = isotropic_strain(self.stress(state),self.instantaneous,self.poisson)
        # Effective macroscopic delayed strain, not the strain in any one branch.
        return elastic, sub(state.mechanical_strain,elastic)

    def advance_reduced(self, state, new_mechanical_strain, delta_xi):
        """Exact branch update for strain linear in reduced time on this segment."""
        delta_xi = finite(delta_xi)
        if delta_xi <= 0:
            raise ValueError('Positive reduced-time step required')
        new = tensor(new_mechanical_strain)
        increment = sub(new,tensor(state.mechanical_strain))
        self.stress(state)
        updated = []
        for (k,tau),old in zip(self.branches,state.branch_stresses):
            r = delta_xi/tau
            decay = math.exp(-r)
            weight = -math.expm1(-r)/r if r else 1.
            updated.append(add(scale(old,decay),scale(isotropic_stress(increment,k,self.poisson),weight)))
        return State(new,tuple(updated))

    def advance(self, state, new_total_strain, t0, t1, dt, reference=23.):
        """Midpoint frozen-temperature substep; split ramps at Tg before calling."""
        t0,t1 = self.temperature(t0),self.temperature(t1)
        dt = finite(dt)
        if dt <= 0:
            raise ValueError('Positive physical time step required')
        if min(t0,t1)<self.tg<max(t0,t1):
            raise ValueError('Split a temperature segment at Tg')
        new_mechanical = sub(tensor(new_total_strain),self.thermal_strain(t1,reference))
        return self.advance_reduced(state,new_mechanical,dt/self.shift((t0+t1)/2))

    def reduced_time(self, t0, t1, dt, panels=128):
        """Composite Simpson quadrature for a linear temperature ramp, split at Tg.

        This is a reference integration utility; it does not make the frozen-
        temperature strain update exact for general non-isothermal loading.
        """
        t0,t1 = self.temperature(t0),self.temperature(t1)
        dt = finite(dt)
        if dt < 0 or not isinstance(panels,int) or panels<2 or panels%2:
            raise ValueError('Nonnegative time and positive even panel count required')
        if dt==0: return 0.
        if t0==t1: return dt/self.shift(t0)
        if min(t0,t1)<self.tg<max(t0,t1):
            fraction=(self.tg-t0)/(t1-t0)
            return self.reduced_time(t0,self.tg,dt*fraction,panels)+self.reduced_time(self.tg,t1,dt*(1-fraction),panels)
        h=1/panels
        terms=[(1 if i in (0,panels) else 4 if i%2 else 2)/self.shift(t0+(t1-t0)*i*h) for i in range(panels+1)]
        return dt*h*math.fsum(terms)/3


def annealing_strain(*args, **kwargs):
    raise EvidenceGapError('No admitted signed bulk irreversible annealing-strain law')


def crystallization(*args, **kwargs):
    raise EvidenceGapError('No admitted grade-specific crystallization kinetics')


def production_annealing_model():
    raise EvidenceGapError('Production blocked: thermal functions, irreversible law, initial state and validation domain unresolved')


def fixture_property(symbol, temperature):
    temperature = finite(temperature)
    with (ROOT/'material/fixture_properties.csv').open(encoding='utf-8-sig',newline='') as f:
        points=sorted((float(r['temperature_C']),float(r['value'])) for r in csv.DictReader(f) if r['property_symbol']==symbol)
    if not points: raise ValueError('Unknown fixture property')
    if not points[0][0]<=temperature<=points[-1][0]:
        raise EvidenceGapError('No fixture-property extrapolation admitted')
    for t,v in points:
        if t==temperature: return v
    for (lo,a),(hi,b) in zip(points,points[1:]):
        if lo<temperature<hi:
            return a+(b-a)*(temperature-lo)/(hi-lo)


def fixture_elastic_stress(strain, temperature):
    return isotropic_stress(strain,fixture_property('E',temperature)*1000,fixture_property('ν',temperature))


def fixture_thermal_strain(*args, **kwargs):
    raise EvidenceGapError('Fixture alpha tangent-versus-mean convention and reference temperature not established')
