"""Kinematic contact feasibility, not an ANSYS or calibrated PLA prediction."""
import csv,hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from src.constitutive import Prusament

def separation_change(layout,h,g,plate,steel_strain):
    if layout=='fixed_inside_spacing':return 0.
    if layout=='coexpanding_inside_spacers':return (h+g)*steel_strain
    if layout=='fixed_outer_faces':return -2*plate*steel_strain
    raise ValueError(layout)

def main():
    geometry=json.loads((ROOT/'geometry/geometry_definition.json').read_text())
    alpha=Prusament.from_database().alpha
    h=geometry['specimen']['thickness_mm'];p=geometry['fixture']['plate_thickness_mm']
    # 16e-6/K: Outokumpu Core304/4301 Table7 mean20-100C.
    # Constant-mean extension within that interval is a screening assumption.
    steel_alpha=json.loads((ROOT/'material/master_fixture_source.json').read_text())['value_per_K']
    rows=[]
    for T in [60.,65.,70.,75.,80.,85.]:
        for layout in ['fixed_inside_spacing','coexpanding_inside_spacers','fixed_outer_faces']:
            for g in geometry['clearance_design']['levels_total_gap_mm']:
                epss=steel_alpha*(T-23.)/(1+steel_alpha*(23.-20.))
                opening=separation_change(layout,h,g,p,epss)
                growth=h*alpha*(T-23.)
                critical=(g+opening-growth)/h
                rows.append(dict(temperature_C=T,gap_mm=g,layout=layout,
                    free_thermal_thickness_growth_mm=growth,inside_spacing_change_mm=opening,
                    zero_recovery_trial_clearance_mm=g+opening-growth,
                    critical_signed_thickness_recovery_strain=critical,
                    interpretation='Contact requires free thickness recovery strain >= critical; flat centered uniform-temperature kinematic screen only'))
    dest=ROOT/'data/processed/master_fixture_screen.csv'
    with dest.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
    inputs=['scripts/screen_fixture_mechanism.py','src/constitutive.py','material/pla_properties.csv','geometry/geometry_definition.json','material/master_fixture_source.json']
    manifest=dict(scope='B reproducible kinematic calculation, not solver output or validated material prediction',files={n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in inputs+[str(dest.relative_to(ROOT)).replace('\\','/')]})
    (ROOT/'reproducibility/master_fixture_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print(len(rows),'kinematic scenarios; no physical recovery value assumed')

if __name__=='__main__':main()
