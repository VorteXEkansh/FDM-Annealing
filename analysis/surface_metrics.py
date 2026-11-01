"""Released-surface metrics; algorithms only, not production evidence.

Coordinates in mm. Use the same named material surface and sampling weights
for all cases. A plane is fitted by orthogonal least squares (SVD), not a
vertical regression. Dimensions use declared paired material fiducials;
axis-aligned bounding boxes are not rigid-rotation invariant.
"""
import numpy as np


def plane_warpage(points, weights=None):
    p = np.asarray(points, dtype=float)
    if p.ndim != 2 or p.shape[1] != 3 or len(p) < 3 or not np.isfinite(p).all():
        raise ValueError('At least three finite 3-D surface points required')
    w = np.ones(len(p)) if weights is None else np.asarray(weights, dtype=float)
    if w.shape != (len(p),) or not np.isfinite(w).all() or np.any(w <= 0):
        raise ValueError('Positive finite surface weights required')
    w = w / w.sum()
    center = np.sum(p * w[:, None], axis=0)
    _, s, vt = np.linalg.svd((p-center) * np.sqrt(w[:, None]), full_matrices=False)
    if s[1] <= max(s[0], 1.) * 1e-12:
        raise ValueError('Collinear or degenerate surface')
    if s[1]-s[2] <= s[0]*1e-12:
        raise ValueError('Best-fit plane normal is not uniquely identifiable')
    normal = vt[-1]
    d = (p-center) @ normal
    return dict(W_max_mm=float(np.max(np.abs(d))),
                W_RMS_mm=float(np.sqrt(np.sum(w*d*d))),
                centroid_mm=center.tolist(), normal=normal.tolist(),
                distances_mm=d.tolist(), weighting='uniform nodes' if weights is None else 'supplied positive weights')


def fiducial_change(initial_pair, final_pair):
    a,b = (np.asarray(x,dtype=float) for x in (initial_pair,final_pair))
    if a.shape != (2,3) or b.shape != (2,3) or not np.isfinite(a).all() or not np.isfinite(b).all():
        raise ValueError('Two matching finite 3-D fiducials in each state required')
    before,after = np.linalg.norm(a[1]-a[0]),np.linalg.norm(b[1]-b[0])
    if before <= 0: raise ValueError('Initial gauge must be positive')
    return dict(initial_mm=float(before), final_mm=float(after),
                change_mm=float(after-before),strain=float(after/before-1))
