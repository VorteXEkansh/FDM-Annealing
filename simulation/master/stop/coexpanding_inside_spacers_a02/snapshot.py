"""Small-strain 3-D stop benchmark. Writes a fresh attempt, never production data."""
import argparse,csv,hashlib,json,os,re,shutil,subprocess,sys,tempfile,time
from pathlib import Path
from screen_fixture_mechanism import ROOT,separation_change,Prusament

layouts=['fixed_inside_spacing','coexpanding_inside_spacers','fixed_outer_faces']
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(layout,gap,attempt):
    assert re.fullmatch('[A-Za-z0-9_-]+',attempt) and gap>0 and layout in layouts
    f=ROOT/'simulation/master/stop'/attempt; f.mkdir(parents=True,exist_ok=False)
    mat=Prusament.from_database();geo=json.loads((ROOT/'geometry/geometry_definition.json').read_text());s=geo['specimen'];H=s['thickness_mm'];P=geo['fixture']['plate_thickness_mm'];L=s['length_mm'];W=s['width_mm'];A=L*W
    # Half thickness; full area; lateral normal constraints at x=0 and y=0 fix rigid motions.
    steel=json.loads((ROOT/'material/master_fixture_source.json').read_text())['value_per_K']
    temperatures=[30,45,60,70,75,80,75,70,60,45,30,23]
    case=dict(layout=layout,gap_mm=gap,temperature_C=temperatures,reference_C=23,units='N, mm, MPa',thermal_input='prescribed uniform temperature; load index is not physical time',
        material='Constant equilibrium modulus k0, no recovery: limiting elastic verification only',young_MPa=mat.equilibrium,poisson=mat.poisson,alpha_pla_per_K=mat.alpha,alpha_steel_per_K=steel,
        selection='For g=0.02 mm compare three different mount idealisations. No fitted values. Free thermal expansion before contact is the analytical comparator.',
        tolerance='absolute gap error <= 1e-7 mm; absolute force error <= 1e-4 N; correct status at all sampled loads')
    (f/'case.json').write_text(json.dumps(case,indent=2)+'\n');shutil.copyfile(__file__,f/'snapshot.py')
    lines=['/BATCH','/FILNAME,stop','/PREP7','ET,1,185',f'MP,EX,1,{mat.equilibrium}',f'MP,PRXY,1,{mat.poisson}',f'MP,ALPX,1,{mat.alpha}','TREF,23']
    for i,(x,y,z) in enumerate([(0,0,0),(L,0,0),(L,W,0),(0,W,0),(0,0,H/2),(L,0,H/2),(L,W,H/2),(0,W,H/2)],1):lines.append(f'N,{i},{x},{y},{z}')
    lines+=['E,1,2,3,4,5,6,7,8','NSEL,S,LOC,X,0','D,ALL,UX,0','NSEL,S,LOC,Y,0','D,ALL,UY,0','NSEL,S,LOC,Z,0','D,ALL,UZ,0','ALLSEL,ALL','CP,1,UZ,5,6,7,8',f'N,9,0,0,{(H+gap)/2}','D,9,ALL,0','ET,2,178','KEYOPT,2,2,4','KEYOPT,2,5,3','R,2','RMODIF,2,9,-1e-9,-1e-9','TYPE,2','REAL,2','E,5,9','FINISH','/SOLU','ANTYPE,STATIC','NLGEOM,OFF','AUTOTS,OFF','OUTRES,ALL,LAST','KBC,0']
    ref=[]
    for i,T in enumerate(temperatures,1):
        opening=separation_change(layout,H,gap,P,steel*(T-23)/(1+steel*(23-20)))
        trial=gap+opening-H*mat.alpha*(T-23)
        ref.append((max(0,trial)/2,max(0,-trial/H)*mat.equilibrium*A))
        lines += [f'TIME,{i}',f'D,9,UZ,{opening/2:.15g}',f'BF,ALL,TEMP,{T}','NSUBST,10,10,10','SOLVE']
    lines+=['FINISH','/POST1','*CFOPEN,raw,csv']
    for i in range(1,len(ref)+1):
        lines += [f'SET,{i},LAST','ETABLE,CF,SMISC,1','ETABLE,CS,NMISC,1','ETABLE,CG,NMISC,3','*GET,FF,ELEM,2,ETAB,CF','*GET,SS,ELEM,2,ETAB,CS','*GET,GG,ELEM,2,ETAB,CG','*GET,UU,NODE,5,U,Z','*GET,RR,NODE,9,RF,FZ',f'II={i}','*VWRITE,II,GG,FF,SS,UU,RR',"(6(E23.15,','))"]
    lines+=['*CFCLOS','FINISH','/EXIT,NOSAVE'];(f/'input.dat').write_text('\n'.join(lines)+'\n',encoding='ascii')
    work=Path(tempfile.mkdtemp(prefix='fdm_stop_'));shutil.copyfile(f/'input.dat',work/'input.dat');exe=os.environ.get('MAPDL_EXE',r'C:\Program Files\ANSYS Inc\ANSYS Student\v261\ansys\bin\winx64\ANSYS261.exe')
    command=[exe,'-b','-i',str(work/'input.dat'),'-o',str(work/'mapdl.out'),'-j','stop','-np','1'];t=time.monotonic(); err=None; code=None; ok=False
    try:
        p=subprocess.run(command,cwd=work,capture_output=True,timeout=240);code=p.returncode
        for name,buf in [('stdout.log',p.stdout),('stderr.log',p.stderr)]: (f/name).write_bytes(buf)
        for name in ['raw.csv','mapdl.out','stop.err']:
            if (work/name).exists():shutil.copyfile(work/name,f/name)
        assert code==0 and '*** ERROR ***' not in (f/'mapdl.out').read_text(errors='replace'),'Solver failed; see raw output'
        records=[]
        for row in csv.reader((f/'raw.csv').open()):
            i,g,force,status,uz,rf=[float(x) for x in row if x.strip()];i=int(i);rg,rF=ref[i-1];gf=-g;F=-force
            records.append(dict(step=i,T_C=temperatures[i-1],gap_mm=gf,ref_gap_mm=rg,compressive_force_N=F,ref_force_N=rF,status=round(status),top_UZ_mm=uz,stop_RFZ_N=rf,
                passed=abs(gf-rg)<1e-7 and abs(F-rF)<1e-4 and abs(abs(rf)-rF)<1e-4 and (round(status)>=2)==(rF>0)))
        assert [r['step'] for r in records]==list(range(1,len(ref)+1))
        with (f/'comparison.csv').open('w',newline='') as stream:
            w=csv.DictWriter(stream,fieldnames=list(records[0]),lineterminator='\n');w.writeheader();w.writerows(records)
        ok=all(r['passed'] for r in records)
    except Exception as e:err=repr(e)
    finally:
        (f/'manifest.json').write_text(json.dumps(dict(accepted=ok,error=err,returncode=code,command=command,runtime_s=time.monotonic()-t,files={p.name:digest(p) for p in f.iterdir() if p.is_file()}),indent=2)+'\n')
    print(attempt,ok,err);return ok
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--layout',choices=layouts,required=True);p.add_argument('--gap',type=float,default=.02);p.add_argument('--attempt',required=True);a=p.parse_args();sys.exit(0 if run(a.layout,a.gap,a.attempt) else 2)
