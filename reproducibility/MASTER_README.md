# Reproducing the master investigation

The current article is a numerical verification and fixture-feasibility study. It
is not a validated production annealing model or an official completion release.
The earlier Stage 20 package and all original solver evidence remain intact.
Read `docs/PROJECT_STATE.md` first. The checkpoint is `1608028`; the baseline
release is `d23a9ecd097072bf8165a36fa731e8e15910122f`.

## Evidence and scientific limits

`reproducibility/master_result_traceability.csv` links 274 new comparison,
calculation and reserved-observation records to source files, code and hashes.
`result_traceability.csv` retains the 384 earlier records. The master checksum
registry covers the new manuscript, inputs, outputs and methods. Each of the 13
new solver attempt directories has its own immutable manifest. Six reference
attempts are accepted; none is a production simulation. A launch failure, an
equilibrium failure, two coarse accuracy failures and three wrong-normal contact
attempts remain available. A successful run is not physical validation.

Main Table 1 and Figure 1 use `verification/master_nonisothermal*.csv`, with raw
ANSYS data in `simulation/master/nonisothermal/`. Figure 2 uses
`data/processed/master_fixture_screen.csv` and the three accepted stop exports in
`simulation/master/stop/`. Figure 3 uses `verification/programmed_road_check.csv`;
it is an independent Python calculation, not an ANSYS result. Tables S1–S12
preserve the earlier property/reference evidence; S13–S17 add the new attempts,
transient comparisons, recovery checks, stop responses and kinematic screen.

The ten main bibliography DOIs resolve to archived Crossref records. Publisher
author lists correct two incomplete metadata records in a separate file without
altering the raw records. Search coverage, full-text access limits, formulation
compatibility and observation reservations are in the master decision documents.
No publisher PDF, account secret or unnecessary binary scratch is included in
the current Git tree. Locally retained binary results can be checked against
their manifest hashes; scalar exports and input/log evidence are distributed.

## Calculation environment

ANSYS: Student 2026 R1, MAPDL 26.1, update 20260202. Its proprietary executable
and license are required only to repeat solver runs. The reference runs use one
CPU and tiny meshes, within the recorded Student license. The system inventory
is `docs/software_environment.md`; no production resource claim is inferred.

The tested authoring runtime is the Codex bundled Python and packages recorded
in `reproducibility/master_environment.json`. Main Word/PDF conversion uses
Microsoft Word, whose exact version/build is in `master_word_environment.json`,
and the Office16 MML2OMML transform. Figures were generated with the installed
Python/Matplotlib environment recorded separately in the same environment file.
`requirements.txt` provides the authoring dependencies; numerical comparison
scripts otherwise use Python's standard library, except surface SVD uses NumPy.

From the repository root, run the following with the recorded Python executable:

```text
python -m unittest discover -s tests -v
python scripts/screen_fixture_mechanism.py
python scripts/check_programmed_recovery.py
python scripts/summarize_master_nonisothermal.py --audit-reference
python scripts/plot_master.py
python scripts/build_master.py
python scripts/build_master_supplement.py
python scripts/check_master.py --preflight --write
```

The calculation scripts refresh derived files, never solver archives. The main
builder creates editable OMML equations, invokes read-only native Word export,
and copies the current full main PDF to the evolving DRAFT path. The supplementary
PDF uses ReportLab. The packaged LibreOffice renderer was attempted but its
executable was unavailable; the log is retained locally. Word is the tested
fallback. PDF metadata can vary; numerical reproduction and DOCX source content
are tested separately from byte-identical PDF exports.

Render both PDFs with Poppler and inspect every page. Update the visual review
record only after inspection, then run `python scripts/check_master.py --write`.
The check verifies archived hashes, independently recomputes response metrics,
checks citations/equations, and rejects fabricated entries in blocked result
registries. Passing it is an integrity result, not publication certification.

## Repeating a solver reference

Use a fresh empty directory and the archived `input.dat` and command in the chosen
manifest. Adapt only paths to the new machine. Keep the original attempt intact.
`scripts/run_master_nonisothermal.py --help` and
`scripts/check_mount_kinematics.py --help` expose new-attempt controls. The
non-isothermal runner guards the 23–85 °C constitutive domain, uses full Newton
iteration and records temperature-shift/time discretization. The accepted stop
cases require the explicit Z normal, KEYOPT(5)=3. Do not copy the excluded
wrong-normal decks as accepted methods.

The independent scalar reference is evaluated at 0.001 s and checked at 0.0005 s.
Accepted final ANSYS time increment is 0.025 s with 0.125 °C shift-table spacing
for this reference history only. Production mesh, time-step, thermal contact and
free/released-state extraction still require separate validation and convergence.

## Resuming the physical investigation

See `docs/master_remaining_blockers.md`. No approved production design, fitted
surrogate, uncertainty distribution, Pareto optimum or confirmation result exists.
The independent literature observations cannot supply all missing initial-state
and thermal boundary histories. Replacing missing evidence with arbitrary
coefficients would change the scientific question and is not an authorized
physical prediction. No release tag or submission-readiness declaration is made.
