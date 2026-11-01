"""Uniaxial, traction-free specialization of Chapuis et al. (2025), eqs. 3–8.

This is a material-point calculation for an intentionally programmed road.
It is not a fitted bulk annealing eigenstrain, coupon solver or experiment.
Stress in MPa; strains relative to the initial printed configuration.
"""
from dataclasses import dataclass
import math

from src.constitutive import Prusament, finite


@dataclass(frozen=True)
class RoadState:
    mechanical_strain: float
    equilibrium_stress: float
    branch_stresses: tuple[float, ...]

    @property
    def stress(self):
        return math.fsum((self.equilibrium_stress, *self.branch_stresses))


def initialize(material: Prusament, prestrain: float) -> RoadState:
    """Program tensile prestrain without a net initial traction (source eqs. 7–8)."""
    h = material.equilibrium * finite(prestrain)
    modulus_sum = math.fsum(k for k, _ in material.branches)
    return RoadState(0.0, h, tuple(-h*k/modulus_sum for k, _ in material.branches))


def free_step(material: Prusament, state: RoadState, t0: float, t1: float, dt: float) -> RoadState:
    """Enforce zero end traction, taking strain linear in reduced time per step.

    Integrate inverse shift over the specified linear temperature ramp. For a
    stress-free point, reversible expansion adds to recovered strain without
    driving the internal stresses. Return mechanical strain only.
    """
    if finite(dt) <= 0 or len(state.branch_stresses) != len(material.branches):
        raise ValueError('Positive time step and matching spectrum required')
    xi = material.reduced_time(t0, t1, dt)
    previous = []
    tangents = []
    for (k,tau),h in zip(material.branches,state.branch_stresses):
        r = xi/tau
        previous.append(math.exp(-r)*h)
        tangents.append(k*(-math.expm1(-r)/r if r else 1.0))
    de = -math.fsum([state.equilibrium_stress, *previous])/math.fsum([material.equilibrium, *tangents])
    return RoadState(state.mechanical_strain + de, state.equilibrium_stress + material.equilibrium*de,
                     tuple(h+b*de for h,b in zip(previous,tangents)))


def total_strain(material: Prusament, state: RoadState, temperature: float, reference: float):
    return state.mechanical_strain + material.thermal_strain(temperature, reference)[0]
