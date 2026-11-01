"""Non-isothermal material-point verification; never a production annealing run."""
from pathlib import Path
import argparse,csv,hashlib,json,math,shutil,subprocess,tempfile,time
ROOT=Path(__file__).resolve().parents[1]
EXE=Path(r'C:\Program Files\ANSYS Inc\ANSYS Student\v261\ansys\bin\winx64\ANSYS261.exe')
HISTORY=[(0.,23.),(42.,65.),(57.,80.),(117.,80.),(132.,65.),(174.,23.),(234.,23.)]
SAMPLES=[1.,10.,20.,30.,40.,42.,45.,50.,55.,57.,60.,70.,90.,117.,120.,125.,130.,132.,140.,150.,160.,170.,174.,180.,200.,234.]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def shift_log(t):
    if not 23<=t<=85:raise ValueError('Source temperature domain exceeded')
    return 35000*(1/(t+273.15)-1/(65+273.15)) if t<65 else -17.4*(t-65)/(51.6+t-65)
def temperature(t):
    for (a,x),(b,y) in zip(HISTORY,HISTORY[1:]):
        if a<=t<=b:return x+(y-x)*(t-a)/(b-a)
    raise ValueError(t)
def parameters():return json.loads((ROOT/'material/constitutive_reference.json').read_text())
def reference(dt):
    """Independent scalar exponential integration of ds/dt+s/(a*tau)=k*de/dt.

    Reads source-converted spectrum, without importing src.constitutive or APDL.
    Midpoint coefficient freezing is checked by halving dt; not claimed exact.
    """
    p=parameters();e0=p['instantaneous_moduli_MPa']['E'];eq=p['equilibrium_modulus_MPa']
    ks=[b['shear_fraction']*e0 for b in p['prony']];tau=[b['reference_relaxation_time_s'] for b in p['prony']]
    s=[0.]*len(ks);clock=0.;last=0.;out={}
    for end in sorted(set(SAMPLES+[v[0] for v in HISTORY[1:]])):
        n=round((end-last)/dt);step=(end-last)/n
        for j in range(n):
            a=last+j*step;b=a+step;ta=temperature(a);tb=temperature(b)
            rate=10**(-shift_log((ta+tb)/2));dxi=step*rate;clock+=dxi;de=-68e-6*(tb-ta)
            for i,(k,tau_i) in enumerate(zip(ks,tau)):
                r=dxi/tau_i;decay=math.exp(-r);weight=-math.expm1(-r)/r
                s[i]=decay*s[i]+k*de*weight
        out[end]={'stress_MPa':eq*(-68e-6*(temperature(end)-23))+math.fsum(s),'reduced_time_s':clock}
        last=end
    return out
def spec(dt,spacing):
    return dict(purpose='Non-isothermal numerical verification only; not physical validation',source='Chapuis2025; DOI10.1088/1361-665X/adeee4; source-converted spectrum',history_s_C=HISTORY,sample_times_s=SAMPLES,dt_s=dt,shift_table_spacing_C=spacing,temperature_domain_C=[23,85],reference_C=23,alpha_per_K=68e-6,geometry_mm=[10,1,1],element='one SOLID185;8nodes',boundary='x=0 and10 axial restraint; y=0 UY=0; z=0 UZ=0; transverse faces free',strain_model='thermal+isotropic generalized Maxwell; matching normalized shear/bulk spectra',absolute_stress_tolerance_MPa=1e-4,relative_stress_tolerance=.002,relative_refinement_limit=.002,reference_dt_s=.001,reference_confirmation_dt_s=.0005)
def deck(c):
    p=parameters();E=p['instantaneous_moduli_MPa']['E'];nu=p['poisson_ratio']
    lines=['/BATCH','/FILNAME,noniso','/PREP7','ET,1,185',f'MP,EX,1,{E}',f'MP,PRXY,1,{nu}','MP,ALPX,1,68e-6','TREF,23','TOFFST,273.15']
    for mode in ['SHEAR','BULK']:
        lines+=[f'TB,PRONY,1,,23,{mode}']
        for i,b in enumerate(p['prony']):lines+=[f'TBDATA,{2*i+1},{b["shear_fraction"]:.16g},{b["reference_relaxation_time_s"]:.16g}']
    lines+=['TB,SHIFT,1,,,PLIN']
    n=round(62/c['shift_table_spacing_C'])
    for i in range(n+1):
        t=23+62*i/n;lines+=[f'TBPT,,{t+273.15:.12g},{-shift_log(t):.16g}']
    lines+=['N,1,0,0,0','N,2,10,0,0','N,3,10,1,0','N,4,0,1,0','N,5,0,0,1','N,6,10,0,1','N,7,10,1,1','N,8,0,1,1','E,1,2,3,4,5,6,7,8','D,ALL,UX,0','NSEL,S,LOC,Y,0','D,ALL,UY,0','NSEL,S,LOC,Z,0','D,ALL,UZ,0','ALLSEL,ALL','BF,ALL,TEMP,23','FINISH','/SOLU','ANTYPE,STATIC','NROPT,FULL','NLGEOM,OFF','AUTOTS,OFF','KBC,0','OUTRES,ALL,LAST']
    # Every reported time is a load-step endpoint; no interpolation of solver outputs.
    for t in sorted(set(SAMPLES+[v[0] for v in HISTORY[1:]])):
        dt=c['dt_s'];lines += [f'TIME,{t}',f'BF,ALL,TEMP,{temperature(t):.14g}',f'DELTIM,{dt},{dt},{dt}','SOLVE']
    lines+=['FINISH','/POST1','*CFOPEN,values,csv']
    for t in SAMPLES:
        lines += [f'SET,,,,,{t}','ETABLE,SXV,S,X','*GET,SXX,ELEM,1,ETAB,SXV','*GET,UYV,NODE,3,U,Y','*GET,R1,NODE,1,RF,FX','*GET,R4,NODE,4,RF,FX','*GET,R5,NODE,5,RF,FX','*GET,R8,NODE,8,RF,FX','RFV=R1+R4+R5+R8','*GET,TV,ACTIVE,0,SET,TIME','ETABLE,EPTHERM,EPTH,X','*GET,EPX,ELEM,1,ETAB,EPTHERM','TEMPV=23+EPX/68e-6','*VWRITE,TV,TEMPV,SXX,UYV,RFV',"(5(E23.15,','))"]
    return '\n'.join(lines+['*CFCLOS','FINISH','/EXIT,NOSAVE'])+'\n'
def writecsv(p,rows):
    with p.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys(),lineterminator='\n');w.writeheader();w.writerows(rows)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--dt',type=float,required=True);ap.add_argument('--spacing',type=float,default=.25);ap.add_argument('--attempt',required=True);args=ap.parse_args()
    c=spec(args.dt,args.spacing);run=ROOT/'simulation/master/nonisothermal'/args.attempt;run.mkdir(parents=True,exist_ok=False)
    (run/'case.json').write_text(json.dumps(c,indent=2)+'\n');(run/'input.dat').write_text(deck(c),encoding='ascii');shutil.copyfile(__file__,run/'script_snapshot.py')
    scratch=Path(tempfile.gettempdir())/'FDM-Annealing'/('noniso_'+args.attempt);scratch.mkdir(parents=True,exist_ok=False);shutil.copyfile(run/'input.dat',scratch/'input.dat')
    cmd=[str(EXE),'-b','-i',str(scratch/'input.dat'),'-o',str(scratch/'mapdl.out'),'-j','noniso','-smp','-np','1']
    start=time.monotonic();result=subprocess.run(cmd,cwd=scratch,capture_output=True);elapsed=time.monotonic()-start
    (run/'stdout.log').write_bytes(result.stdout);(run/'stderr.log').write_bytes(result.stderr)
    for p in scratch.iterdir():
        if p.is_file() and p.name in {'mapdl.out','noniso.err','values.csv','noniso.rst'}:shutil.copyfile(p,run/p.name)
    accepted=False;error='';rows=[]
    try:
        assert result.returncode==0,'Solver returned nonzero'
        assert '*** ERROR ***' not in (run/'mapdl.out').read_text(errors='replace'),'MAPDL error'
        ref=reference(c['reference_dt_s']);confirm=reference(c['reference_confirmation_dt_s'])
        for row in csv.reader((run/'values.csv').open()):
            a=[float(v) for v in row if v.strip()];t,T,s,uy,R=a;t=round(t,8);r=confirm[t]['stress_MPa'];err=abs(s-r);tol=c['absolute_stress_tolerance_MPa']+c['relative_stress_tolerance']*abs(r)
            rows.append(dict(time_s=t,temperature_C=T,ansys_stress_MPa=s,reference_stress_MPa=r,absolute_error_MPa=err,relative_error_percent=100*err/abs(r) if r else '',tolerance_MPa=tol,passed=err<=tol,reference_refinement_change_MPa=abs(ref[t]['stress_MPa']-r),reduced_time_s=confirm[t]['reduced_time_s'],ansys_transverse_displacement_mm=uy,ansys_reaction_N=R))
        assert len(rows)==len(SAMPLES),'Incomplete extraction'
        writecsv(run/'comparison.csv',rows);accepted=all(r['passed'] and abs(r['temperature_C']-temperature(r['time_s']))<1e-4 and abs(r['ansys_reaction_N']+r['ansys_stress_MPa'])<1e-5 for r in rows)
    except Exception as exc:error=str(exc)
    manifest=dict(accepted=accepted,error=error,returncode=result.returncode,runtime_s=elapsed,command=cmd,material_sha256=sha(ROOT/'material/constitutive_reference.json'),files={p.name:sha(p) for p in run.iterdir() if p.is_file()})
    (run/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(run.name,'accepted',accepted,'error',error,'runtime',elapsed)
    for r in rows:
        if not r['passed']:print(r)
    if not accepted:raise SystemExit(2)
if __name__=='__main__':main()
