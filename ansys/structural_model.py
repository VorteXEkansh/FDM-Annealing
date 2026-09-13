"""Structural production boundary; verification decks are independently executable."""
from scripts.run_structural_verification import deck as verification_deck, spec as verification_spec
BLOCKERS=(
    'compatible production thermal histories',
    'identified bulk irreversible annealing-strain evolution',
    'verified non-isothermal Arrhenius/WLF adapter',
    'fixture thermal-expansion convention',
    'surface-contact discretization and friction evidence',
    'production release and observation definitions',
)
def build_production_deck():
    raise RuntimeError('Production structural model blocked: '+ '; '.join(BLOCKERS))
