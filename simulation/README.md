# Simulation records

`cases/` holds explicit parameter records. `runs/<case_id>/` holds solver logs
and a hash manifest. Case inputs never receive silent defaults for temperature,
hold time, fixture gap, or material identity. Failed runs remain in place.

The production template is intentionally non-executable. Stage 6 has no model,
mesh, numerical field result, or simulation campaign.

