"""Validate Stage 7 geometry, calculate derived dimensions, and write an APDL deck."""
from __future__ import annotations
import argparse, csv, hashlib, json, subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DEF=ROOT/'geometry/geometry_definition.json'
OUTDIR=ROOT/'simulation/geometry/stage07_plate_gap'
MAPDL=Path(r'C:\Program Files\ANSYS Inc\ANSYS Student\v261\ansys\bin\winx64\ANSYS261.exe')

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def validate(d):
    s=d['specimen']; f=d['fixture']; c=d['clearance_design']
    dims=[s['length_mm'],s['width_mm'],s['thickness_mm'],f['plate_length_mm'],f['plate_width_mm'],f['plate_thickness_mm']]
    if not all(v>0 for v in dims): raise ValueError('all dimensions must be positive')
    m=f['planar_margin_each_side_mm']
    if f['plate_length_mm'] != s['length_mm']+2*m or f['plate_width_mm'] != s['width_mm']+2*m:
        raise ValueError('plate dimensions and planar margins are inconsistent')
    if len(c['levels_gamma']) != len(c['levels_total_gap_mm']): raise ValueError('gap arrays differ in length')
    for gamma,gap in zip(c['levels_gamma'],c['levels_total_gap_mm']):
        if abs(gamma-gap/s['thickness_mm'])>1e-12: raise ValueError('gamma and gap are inconsistent')
    if c['geometry_build_level_gamma'] not in c['levels_gamma']: raise ValueError('build level absent')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--execute',action='store_true'); args=ap.parse_args()
    d=json.loads(DEF.read_text()); validate(d); s=d['specimen']; f=d['fixture']; c=d['clearance_design']
    OUTDIR.mkdir(parents=True,exist_ok=True)
    rows=[]
    for gamma,gap in zip(c['levels_gamma'],c['levels_total_gap_mm']):
        rows.append({'gamma':f'{gamma:.4f}','total_gap_mm':f'{gap:.3f}','half_gap_mm':f'{gap/2:.3f}','plate_separation_mm':f"{s['thickness_mm']+gap:.3f}",'assembly_height_mm':f"{2*f['plate_thickness_mm']+s['thickness_mm']+gap:.3f}",'status':'declared screening geometry'})
    with (OUTDIR/'gap_design.csv').open('w',newline='',encoding='utf-8') as fp:
        w=csv.DictWriter(fp,fieldnames=rows[0]); w.writeheader(); w.writerows(rows)
    gap=c['levels_total_gap_mm'][c['levels_gamma'].index(c['geometry_build_level_gamma'])]
    deck=f'''/BATCH\n/PREP7\n! Stage 7 geometry only. Units: mm. No mesh, material, load, or solve.\nLSP={s['length_mm']:.9f}\nWSP={s['width_mm']:.9f}\nHSP={s['thickness_mm']:.9f}\nLPL={f['plate_length_mm']:.9f}\nWPL={f['plate_width_mm']:.9f}\nTPL={f['plate_thickness_mm']:.9f}\nGAP={gap:.9f}\nXM=(LPL-LSP)/2\nYM=(WPL-WSP)/2\nBLOCK,0,LPL,0,WPL,-TPL-GAP/2,-GAP/2\nVSEL,S,VOLU,,1\nCM,LOWER_PLATE,VOLU\nALLSEL,ALL\nBLOCK,XM,XM+LSP,YM,YM+WSP,0,HSP\nVSEL,S,VOLU,,2\nCM,SPECIMEN,VOLU\nALLSEL,ALL\nBLOCK,0,LPL,0,WPL,HSP+GAP/2,HSP+GAP/2+TPL\nVSEL,S,VOLU,,3\nCM,UPPER_PLATE,VOLU\nALLSEL,ALL\nCM,FIXTURE_PLATES,VOLU\n*GET,NVOL,VOLU,0,COUNT\n/COM,STAGE7_EXPECTED_VOLUMES=3\n/COM,STAGE7_TOTAL_GAP_MM={gap:.9f}\n/COM,STAGE7_GAMMA={c['geometry_build_level_gamma']:.9f}\nVSUM\nSAVE,stage07_plate_gap,db\n/EXIT,NOSAVE\n'''
    inp=OUTDIR/'geometry.dat'; inp.write_text(deck,encoding='ascii',newline='\n')
    command=None; rc=None
    if args.execute:
        command=[str(MAPDL),'-b','-i',str(inp),'-o',str(OUTDIR/'mapdl_geometry.out'),'-j','stage07_geometry','-np','1']
        rc=subprocess.run(command,cwd=OUTDIR,check=False).returncode
    derived={'specimen_volume_mm3':s['length_mm']*s['width_mm']*s['thickness_mm'],'nominal_contact_area_each_face_mm2':s['length_mm']*s['width_mm'],'length_to_thickness':s['length_mm']/s['thickness_mm'],'width_to_thickness':s['width_mm']/s['thickness_mm'],'length_to_width':s['length_mm']/s['width_mm'],'fixture_plate_volume_each_mm3':f['plate_length_mm']*f['plate_width_mm']*f['plate_thickness_mm']}
    manifest={'created_utc':datetime.now(timezone.utc).isoformat(),'execution':{'executed':args.execute,'returncode':rc,'command':command},'source_sha256':sha(DEF),'input_sha256':sha(inp),'gap_table_sha256':sha(OUTDIR/'gap_design.csv'),'derived_calculations':derived}
    for name in ['mapdl_geometry.out','stage07_plate_gap.db','stage07_geometry.err','stage07_geometry.log']:
        p=OUTDIR/name
        if p.exists(): manifest.setdefault('output_sha256',{})[name]=sha(p)
    (OUTDIR/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(manifest,indent=2))
    if args.execute and rc: raise SystemExit(rc)

if __name__=='__main__': main()
