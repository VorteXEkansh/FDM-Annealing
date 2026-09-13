"""Fail-closed admission checks for the production transient thermal model.

This module defines the data contract needed to emit a production MAPDL deck.
It intentionally emits no deck while physical thermal inputs are unresolved.
The executed analytical benchmark lives in scripts/run_thermal_verification.py.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCTION_TEMPLATE = ROOT / "simulation/cases/thermal_production_template.json"
PHASES = (
    "initial_ambient",
    "heating",
    "approach_to_target",
    "holding",
    "cooling",
    "final_observation",
)


class ThermalEvidenceGap(RuntimeError):
    """Raised when a production thermal deck would require an invented input."""


def load_case(path: Path = PRODUCTION_TEMPLATE) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def production_blockers(case: dict) -> list[str]:
    blockers = []
    if case.get("case_kind") != "transient_thermal_production":
        blockers.append("case_kind")
    cycle = case.get("cycle", {})
    blockers.extend(f"cycle.{phase}" for phase in PHASES if phase not in cycle)
    material = case.get("material", {})
    for field in ("density_table", "thermal_conductivity_table", "specific_heat_table"):
        if not material.get(field):
            blockers.append(f"material.{field}")
    if case.get("target_temperature_C") is None:
        blockers.append("target_temperature_C")
    if case.get("hold_duration_s") is None:
        blockers.append("hold_duration_s")
    boundaries = case.get("boundaries", {})
    convection = boundaries.get("convection", {})
    if convection.get("coefficient_W_m2K") is None or not convection.get("source_or_design_basis"):
        blockers.append("boundaries.convection")
    radiation = boundaries.get("radiation", {})
    if radiation.get("enabled") is None:
        blockers.append("boundaries.radiation.relevance_decision")
    contact = boundaries.get("thermal_contact", {})
    if case.get("condition") in (None, "GAP", "FREE_or_GAP") and contact.get("conductance_W_m2K") is None:
        blockers.append("boundaries.thermal_contact")
    for gate, admitted in case.get("admission", {}).items():
        if admitted is not True:
            blockers.append(f"admission.{gate}")
    return sorted(set(blockers))


def require_production_ready(case: dict) -> None:
    blockers = production_blockers(case)
    if blockers:
        raise ThermalEvidenceGap("production transient thermal execution blocked by: " + ", ".join(blockers))


def build_production_deck(case: dict) -> str:
    require_production_ready(case)
    raise NotImplementedError("deck emission is unavailable until an admitted case exists")
