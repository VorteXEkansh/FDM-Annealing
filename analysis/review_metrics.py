"""Independent Stage 19 extraction review; archived solver data are read-only.

These metrics describe numerical benchmarks, not production PLA predictions.
"""
import csv
import math


def relative_change(fine, coarse):
    """Undefined at every zero denominator, including a zero-to-zero pair."""
    if not all(math.isfinite(x) for x in (fine, coarse)):
        raise ValueError('Finite values required')
    return None if fine == 0 else 100 * abs(fine-coarse) / abs(fine)


def numeric_csv(path):
    with path.open() as f:
        return [[float(v) for v in row if v.strip()] for row in csv.reader(f) if row]


def extract(run, model):
    """Recompute measurands without importing the original extraction routines."""
    if model == 'structural':
        nodes = numeric_csv(run/'top_nodes.csv')
        points = [(v[1]+v[3], v[2]+v[4]) for v in nodes]
        n = len(points)
        xm, ym = (math.fsum(p[j] for p in points)/n for j in (0, 1))
        slope = math.fsum((x-xm)*(y-ym) for x,y in points)/math.fsum((x-xm)**2 for x,y in points)
        errors = [abs(y-ym-slope*(x-xm)) for x,y in points]
        stresses = sorted(abs(v[3]) for v in numeric_csv(run/'element_stress.csv') if 6 <= v[1] <= 54)
        pos = .95*(len(stresses)-1)
        lo, hi = math.floor(pos), math.ceil(pos)
        return {'W_max':max(errors), 'residual_displacement':max(math.hypot(v[3],v[4]) for v in nodes),
                'residual_stress_p95':stresses[lo]+(pos-lo)*(stresses[hi]-stresses[lo])}
    if model == 'thermal':
        rows = numeric_csv(run/'temperature_profile.csv')
        profile = sorted((z,t) for time,z,t in rows if time == 300)
        center = min(profile,key=lambda pair:abs(pair[0]-.005))[1]
        return {'thermal_lag_at_300_s':80-center,
                'temperature_gradient_at_300_s':abs((profile[0][1]+profile[-1][1])/2-center)/.005,
                'temperature_profile_L2_excursion':math.sqrt(math.fsum((v[2]-20)**2 for v in rows)/len(rows))}
    if model == 'contact_normal_lagrange' or model == 'contact':
        rows = numeric_csv(run/'contact_values.csv')
        pressures = [max(0,v[2]) for v in rows]
        # Accepted archived cases report either zero or uniformly signed penetration.
        signs = {math.copysign(1,v[3]) for v in rows if v[3]}
        if len(signs)>1:
            raise ValueError('Mixed penetration signs require element-level review')
        return {'mean_contact_pressure':math.fsum(pressures)/len(rows),
                'maximum_contact_pressure':max(pressures),
                'maximum_penetration':max(abs(v[3]) for v in rows),
                'normal_reaction':numeric_csv(run/'reaction.csv')[0][0]}
    raise ValueError('Unknown benchmark')
