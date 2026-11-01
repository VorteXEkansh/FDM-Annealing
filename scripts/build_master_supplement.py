"""Retain prior supplementary tables and add complete new compact evidence."""
from pathlib import Path
import csv,json,re
import build_manuscript as pdf
import build_release as legacy
from scientific_format import number
ROOT=Path(__file__).resolve().parents[1]
def read(p):return list(csv.DictReader((ROOT/p).open(encoding='utf-8-sig')))
def fmt(x):
    try:return number(x,7)
    except ValueError:return str(x)
def table(title,heads,records):
    return '\n\nSUPPTABLE: '+title+'\n'+' | '.join(heads)+'\n'+'\n'.join(' | '.join(fmt(v) for v in row) for row in records)+'\n'
def main():
    base=(ROOT/'manuscript/current.md').read_text(encoding='utf-8')
    text=legacy.supplemental(base)
    text=text.replace('Verification-only release · 1 October 2026','Numerical verification and feasibility supplement · 1 November 2026')
    text=text.replace('Reference numbers refer to the accompanying main article.','Tables S1–S12 retain the earlier reference evidence. Their numeric citations use the legacy reference key in Section M4 below, not the shorter main article bibliography. Sections M1–M3 document the new investigation. Statements about production incompleteness remain applicable; non-isothermal reference verification has now been added.')
    start=text.index('### S7. Reproduction and interpretation')
    text=text[:start]+'''### S7. Historical reproduction record

Tables S1–S12 retain the earlier accepted calculations and material inventory. Their historical build environment, hashes and quality checks remain in the Stage 20 records. Those records describe the earlier package; the current master build, checks and environment are specified in Section M3 and reproducibility/MASTER_README.md. Every archived attempt remains immutable. Neither reference-case convergence nor the current export quality establishes physical validation.
'''
    # Repair two indistinguishable labels without changing any archived CSV value.
    lines=text.splitlines();inS10=False;source=iter(read('convergence/stage_19_audited_refinement.csv'))
    for i,line in enumerate(lines):
        if line.startswith('SUPPTABLE: All audited mesh'):inS10=True;continue
        if inS10 and line.startswith('###'):inS10=False
        if inS10 and line.startswith(('Mesh |','Time |')):
            r=next(source);parts=line.split(' | ');name=r['run_path'].split('stage10_')[1]
            parts[1]=name.replace('structural','S').replace('thermal','T').replace('contact','C').replace('_',' ');lines[i]=' | '.join(parts)
    text='\n'.join(lines)+'\n'
    text+='''\n<!-- PAGE -->
### M1. New calculations and numerical verification

The source material-point check is deliberately uniaxial and print-conditioned. Its 23–75 °C history is prescribed and differs from the original spring experiment. The spring involved two PLA formulations; the reserved spring means and newer Prusament dog-bone observations are not calibration inputs and have no prediction column populated. The current main paper and repository decision documents explain why no physical validation accuracy is claimed.

The non-isothermal ANSYS test uses a source-derived 23-arm spectrum, full Newton iteration and a temperature-shift table. The original 0.0001 MPa + 0.002|reference stress| gate is retained. Coarse solver and accuracy failures are listed below. The reference discretization is independently halved. All accepted/rejected input, command, source snapshot, log and scalar export hashes are retained in each attempt directory. Binary result files remain local optional evidence; their manifests distinguish their absence from a changed scalar export.
'''
    records=[]
    for group in ['nonisothermal','stop']:
        for p in sorted((ROOT/'simulation/master'/group).iterdir()):
            if not p.is_dir():continue
            m=json.loads((p/'manifest.json').read_text());c=json.loads((p/'case.json').read_text())
            records.append([p.name.replace('_',' '),'Accepted' if m.get('accepted') else 'Excluded',str(m.get('error') or ('Numerical checks passed' if m.get('accepted') else 'Accuracy or wrong-normal check failed'))])
    text+=table('Every new solver attempt and disposition',['Attempt','Disposition','Reason'],records)
    r=[r for r in read('verification/master_nonisothermal.csv') if r['attempt']=='table_confirm_a01']
    text+=table('Final non-isothermal sample comparisons; stresses in MPa',['Time (s)','T (°C)','ANSYS σ','Reference σ','Absolute error'],[[v[k] for k in ['time_s','temperature_C','ansys_stress_MPa','reference_stress_MPa','absolute_error_MPa']] for v in r])
    r=read('verification/programmed_road_check.csv')
    text+=table('Programmed-road refinement; dimensionless mechanical and total strains',['Substeps','Phase','Mechanical strain','Total strain','Net stress (MPa)'],[[v[k] for k in ['substeps_per_phase','phase','axial_mechanical_strain','axial_total_strain','net_axial_stress_MPa']] for v in r])
    text+='\nThe following stop cases use half-thickness symmetry, rigid plane motion, a constant equilibrium spring, prescribed uniform temperature and no nonthermal recovery. Force is the full 600 mm² face resultant. Reported gap is the one-sided node-to-stop separation; total clearance is twice that value. These are benchmarks and not pressure distributions.\n'
    r=[]
    for key,label in [('fixed_inside_spacing','Inner fixed'),('coexpanding_inside_spacers','Inner spacers'),('fixed_outer_faces','Outer fixed')]:
        for v in read(f'simulation/master/stop/{key}_a02/comparison.csv'):r.append([label,v['step'],v['T_C'],v['gap_mm'],v['compressive_force_N'],v['status']])
    text+=table('Three-dimensional stop outputs; state 1 open, state 2 closed',['Mount','Load','T (°C)','Gap (mm)','Force (N)','State'],r)
    text+='\n### M2. Complete deterministic clearance screen\n\nThe critical signed free thickness strain comes from geometry and thermal expansion; it is not an observed or fitted recovery strain. I = fixed inner spacing; S = coexpanding inner spacers; O = fixed outer faces. All calculations use h₀ = 4 mm and plate thickness 5 mm. The mean steel expansion is treated as constant within the manufacturer interval and rebased to 23 °C. No parameter probability or contact-pressure prediction is introduced.\n'
    labels={'fixed_inside_spacing':'I','coexpanding_inside_spacers':'S','fixed_outer_faces':'O'}
    text+=table('All 90 kinematic scenarios',['T (°C)','g₀ (mm)','Mount','ΔH (mm)','e critical (%)'],[[v['temperature_C'],v['gap_mm'],labels[v['layout']],v['inside_spacing_change_mm'],100*float(v['critical_signed_thickness_recovery_strain'])] for v in read('data/processed/master_fixture_screen.csv')])
    text+='''\n### M3. Reproduction, unresolved results and data separation

Run the Python unit suite and scripts/screen_fixture_mechanism.py, scripts/check_programmed_recovery.py, scripts/summarize_master_nonisothermal.py --audit-reference, and scripts/check_master.py from the repository root. The first two perform numerical calculations; the third recomputes comparison summaries from immutable exports. No ANSYS license is needed for these checks. scripts/plot_master.py draws the figures; scripts/build_master.py and scripts/build_master_supplement.py regenerate the documents from their maintained sources. The exact tested dependency versions and font/Office requirements are documented in reproducibility/MASTER_README.md. The main PDF is a native Word export of the editable manuscript; this supplement is typeset separately.

To repeat a solver case, use compatible Ansys Student 2026 R1/MAPDL26.1 with a valid license and a new empty working directory; run its archived input.dat with the recorded command adapted to the new path. Never reuse an archived attempt directory. The master runners accept a new attempt identifier and preserve accepted and failed evidence. They do not assemble a validated production coupon. One SOLID185 plus one CONTA178 in the stop test is far below the documented Student node limit but is not a converged production surface mesh.

No production design is approved. All production, sensitivity, uncertainty, surrogate, optimization and confirmation registries remain empty. These absences are not zero errors, zero warpage, an empty feasible set or a failed physical validation score. Source-specific reserved observations are in validation/master_spring_targets.csv and validation/master_suder_targets.csv; their original cohorts and limitations are retained. Earlier Ultimaker means remain in the legacy register. No dataset is both fitted and independently validated here.

The code-generated figures contain no AI-generated result imagery. Raw scalar evidence, equation/source links and all final artifacts are hashed. The prior full numerical tables are retained above; the duplicate thermal case-label ambiguity in S10 is corrected by keeping mesh/time in the names. The following legacy bibliography permits independent interpretation of all prior numeric citations. New citations in the main article use its own bibliography.

### M4. Legacy reference key for Tables S1–S12
'''
    text+=base.split('### References',1)[1].split('### Supplementary information',1)[0].replace('<!-- PAGE -->','')
    text='\n'.join(s.rstrip() for s in text.splitlines()).rstrip()+'\n'
    (ROOT/'supplementary/master.md').write_text(text,encoding='utf-8',newline='\n')
    pdf.footer=legacy.footer;pdf.CAPTION_MIN_SPACE=110;pdf.ST['tablecaption'].keepWithNext=False
    pdf.TABLE_WIDTHS={'Table S10':[42,102,106,95,51,91]}
    pdf.OUT=ROOT/'output/master/Constrained-Annealing-2026-Supplementary.pdf';pdf.build(text)
if __name__=='__main__':main()
