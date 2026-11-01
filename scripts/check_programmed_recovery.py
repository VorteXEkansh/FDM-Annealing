"""Recompute conditional free-road recovery; no file is an ANSYS result."""
import csv
import hashlib
import json
from pathlib import Path
import sys
from dataclasses import replace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from src.constitutive import Prusament
from src.programmed_recovery import initialize,free_step,total_strain


def main():
    config=json.loads((ROOT/'material/programmed_road.json').read_text(encoding='utf-8'))
    m=replace(Prusament.from_database(),equilibrium=config['equilibrium_MPa'])
    rows=[]
    for pieces in (8,32,128,512):
        state=initialize(m,config['active_axial_prestrain'])
        for phase,a,b,dt in config['prescribed_numerical_history']:
            for j in range(pieces):
                state=free_step(m,state,a+(b-a)*j/pieces,a+(b-a)*(j+1)/pieces,dt/pieces)
            rows.append([pieces,phase,b,format(state.mechanical_strain,'.14g'),
                         format(total_strain(m,state,b,23),'.14g'),format(state.stress,'.6g')])
    out=ROOT/'verification/programmed_road_check.csv'
    with out.open('w',encoding='utf-8',newline='') as f:
        writer=csv.writer(f,lineterminator='\n')
        writer.writerow(['substeps_per_phase','phase','prescribed_temperature_C','axial_mechanical_strain',
                         'axial_total_strain','net_axial_stress_MPa'])
        writer.writerows(rows)
    files=['material/programmed_road.json','material/pla_properties.csv','src/constitutive.py',
           'src/programmed_recovery.py','scripts/check_programmed_recovery.py',
           'tests/test_programmed_recovery.py','verification/programmed_road_check.csv',
           'validation/master_spring_targets.csv','literature/evidence/stage_04/Chapuis2025_UMAT_SMPViscoShells.f']
    sha=lambda name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
    (ROOT/'reproducibility/programmed_road_manifest.json').write_text(
        json.dumps({'scope':'Class B, 1D road calculation. No ANSYS run or validated coupon prediction.',
                    'sha256':{f:sha(f) for f in files}},indent=2)+'\n',encoding='utf-8',newline='\n')
    print('Wrote',len(rows),'phase endpoints, finest resolution:',rows[-1])


if __name__=='__main__':
    main()
