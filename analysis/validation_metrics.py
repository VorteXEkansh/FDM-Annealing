"""Predeclared comparison metrics; this module contains no fitted parameters."""
import math

def compare(predicted, observed):
    predicted, observed = list(predicted), list(observed)
    if not observed or len(predicted) != len(observed):
        raise ValueError('Nonempty matched observations required')
    if not all(math.isfinite(x) for x in predicted + observed):
        raise ValueError('Finite observations required')
    signed = [p-o for p,o in zip(predicted,observed)]
    absolute = [abs(e) for e in signed]
    return {'signed_error':signed, 'absolute_error':absolute,
            'relative_error_percent':[100*a/abs(o) if o != 0 else None for a,o in zip(absolute,observed)],
            'MAE':sum(absolute)/len(absolute),
            'RMSE':math.sqrt(sum(e*e for e in signed)/len(signed))}

def bounded_interpretation(absolute_error, numerical_bound=None, measurement_bound=None):
    """Deterministic compatibility screen, not a confidence interval or validation pass."""
    vals=[absolute_error]+[x for x in (numerical_bound,measurement_bound) if x is not None]
    if any(not math.isfinite(x) or x < 0 for x in vals):
        raise ValueError('Bounds and absolute error must be finite and nonnegative')
    if numerical_bound is None or measurement_bound is None:
        return 'indeterminate_missing_uncertainty'
    return ('compatible_with_declared_bounds' if absolute_error <= numerical_bound+measurement_bound
            else 'discrepancy_exceeds_declared_bounds')
