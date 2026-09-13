"""Stage 9 small reference problems; no production annealing predictions."""
import argparse,csv,hashlib,json,math,shutil,subprocess,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
EXE=Path(r"C:\Program Files\ANSYS Inc\ANSYS Student\v261\ansys\bin\winx64\ANSYS261.exe")
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def spec(kind):
    d=dict(kind=kind,units="N mm s MPa degC",length=10.,area=1.,E=2000.,nu=.3,alpha=1e-5,gap=.002,eigenstrain=-.001,absolute_tolerance=1e-7,relative_tolerance=.001,purpose="declared verification fixtures; not production PLA data")
    if kind=="visco":
        m=json.loads((ROOT/'material/constitutive_reference.json').read_text())
        d.update(E=m['instantaneous_moduli_MPa']['E'],nu=m['poisson_ratio'],prony=m['prony'],temperature_C=65.,strain=.001,ramp_s=1.,dt=.01,purpose="isothermal source-spectrum implementation test at 65 C; not physical validation")
    return d

def deck(c):
    kind=c['kind']; E=c['E']; nu=c['nu']
    lines=['/BATCH','/FILNAME,structural','/PREP7','ET,1,185',f'MP,EX,1,{E}',f'MP,PRXY,1,{nu}',f'MP,ALPX,1,{c["alpha"]}','TREF,20','N,1,0,0,0','N,2,10,0,0','N,3,10,1,0','N,4,0,1,0','N,5,0,0,1','N,6,10,0,1','N,7,10,1,1','N,8,0,1,1','E,1,2,3,4,5,6,7,8','NSEL,S,LOC,X,0','D,ALL,UX,0','NSEL,S,LOC,Y,0','D,ALL,UY,0','NSEL,S,LOC,Z,0','D,ALL,UZ,0','ALLSEL,ALL','CP,1,UX,2,3,6,7']
    if kind.startswith('eigen'):
        s=-E*c['eigenstrain']/(1-2*nu)
        lines+=['INISTATE,SET,DTYP,STRE',f'INISTATE,DEFINE,1,,,,{s},{s},{s},0,0,0']
    if kind=='visco':
        for mode in ['SHEAR','BULK']:
            lines += [f'TB,PRONY,1,,{len(c["prony"])},{mode}']
            for i,b in enumerate(c['prony']): lines += [f'TBDATA,{2*i+1},{b["shear_fraction"]:.16g},{b["reference_relaxation_time_s"]:.16g}']
    if kind=='contact':
        lines+=['N,9,10.002,0,0','D,9,ALL,0','ET,2,178','KEYOPT,2,2,4','KEYOPT,2,5,1','R,2','RMODIF,2,9,-1e-9,-1e-9','TYPE,2','REAL,2','E,2,9']
    lines+=['ALLSEL,ALL','FINISH','/SOLU','ANTYPE,STATIC','NLGEOM,OFF','OUTRES,ALL,ALL','AUTOTS,OFF','KBC,0']
    if kind.endswith('fixed'): lines+=['D,2,UX,0']
    if kind=='visco':
        stages=[(1.,.01,0.01),(11.,.01,.01),(31.,.01,.01),(32.,0.,.01),(62.,0.,.01)]
        for t,u,dt in stages: lines += [f'TIME,{t}',f'D,2,UX,{u}',f'DELTIM,{dt},{dt},{dt}','SOLVE']
    else:
        stages=[(1.,30.),(2.,80.),(3.,20.)]
        for t,temp in stages:
            lines += [f'TIME,{t}','NSUBST,10,10,10',f'BF,ALL,TEMP,{temp}','SOLVE']
        if kind=='eigen_fixed':
            lines += ['DDELE,2,UX','TIME,4','NSUBST,10,10,10','SOLVE']; stages.append((4.,20.))
    lines+=['FINISH','/POST1','*CFOPEN,values,csv']
    for st in stages:
        t=st[0]
        lines += [f'SET,,,,,{t}','ALLSEL,ALL','*GET,UXV,NODE,2,U,X','*GET,UYV,NODE,3,U,Y','*GET,UZV,NODE,6,U,Z','ETABLE,SXV,S,X','*GET,SXX,ELEM,1,ETAB,SXV','RFV=0','*GET,R1,NODE,1,RF,FX','*GET,R4,NODE,4,RF,FX','*GET,R5,NODE,5,RF,FX','*GET,R8,NODE,8,RF,FX','RFV=R1+R4+R5+R8','CFV=0','STATV=0','GAPV=0']
        if kind=='contact': lines+=['ETABLE,CFOR,SMISC,1','ETABLE,CSTAT,NMISC,1','ETABLE,CGAP,NMISC,3','*GET,CFV,ELEM,2,ETAB,CFOR','*GET,STATV,ELEM,2,ETAB,CSTAT','*GET,GAPV,ELEM,2,ETAB,CGAP']
        lines += [f'TV={t}','*VWRITE,TV,UXV,UYV,UZV,SXX,RFV,CFV,STATV,GAPV',"(9(E23.15,','))"]
    lines+=['*CFCLOS','FINISH','/EXIT,NOSAVE']
    return '\n'.join(lines)+'\n'

def references(c,t):
    E,nu,L=c['E'],c['nu'],c['length']; kind=c['kind']; temp={1.:30.,2.:80.,3.:20.,4.:20.}
    if kind=='visco':
        # Exact convolution for 1 s linear strain ramps, with a held strain between ramps.
        stress=0.
        for a,b,slope in [(0.,1.,.001),(31.,32.,-.001)]:
            q=min(t,b)
            if q<=a: continue
            eq=E*(1-sum(x['shear_fraction'] for x in c['prony']))
            stress+=eq*slope*(q-a)
            for x in c['prony']:
                tau=x['reference_relaxation_time_s']
                stress+=E*x['shear_fraction']*slope*tau*(math.exp(-(t-q)/tau)-math.exp(-(t-a)/tau))
        strain=.001 if t<=31 else 0.
        return dict(ux_mm=L*strain,uy_mm=-nu*strain,uz_mm=-nu*strain,stress_x_MPa=stress,reaction_x_N=-stress)
    e=c['alpha']*(temp[t]-20)+(c['eigenstrain'] if kind.startswith('eigen') else 0)
    fixed=kind.endswith('fixed') and t!=4
    u=0. if fixed else L*e
    if kind=='contact': u=min(L*e,c['gap'])
    sx=E*(u/L-e)
    lateral=e-nu*sx/E
    r=dict(ux_mm=u,uy_mm=lateral,uz_mm=lateral,stress_x_MPa=sx,reaction_x_N=-sx)
    if kind=='contact': r.update(contact_force_N=sx,contact_closed=int(L*e>c['gap']),gap_mm=max(c['gap']-u,0))
    return r

def parse(path):
    out=[]
    for row in csv.reader(path.open()):
        try: vals=[float(x) for x in row if x.strip()]
        except ValueError: continue
        if len(vals)==9: out.append(vals)
    return out

def compare(c,raw):
    rows=[]; names=['ux_mm','uy_mm','uz_mm','stress_x_MPa','reaction_x_N','contact_force_N','contact_closed','gap_mm']
    for vals in raw:
        ref=references(c,vals[0])
        for i,k in enumerate(names,1):
            if k not in ref: continue
            actual=(int(vals[i]>=2) if k=='contact_closed' else vals[i]); expected=ref[k]; err=abs(actual-expected)
            tol=c['absolute_tolerance']+c['relative_tolerance']*abs(expected)
            rows.append(dict(case=c['kind'],time_s=vals[0],quantity=k,ansys=actual,reference=expected,absolute_error=err,relative_error_percent=(100*err/abs(expected) if expected else ''),tolerance=tol,passed=err<=tol,raw_contact_status=(vals[7] if k=='contact_closed' else ''),evidence='A: MAPDL; B: analytical calculation'))
    if len(raw)!=(5 if c['kind']=='visco' else 4 if c['kind']=='eigen_fixed' else 3): raise ValueError('incomplete solver extraction')
    return rows

def write_csv(path,rows):
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--kind',choices=['free','fixed','eigen_free','eigen_fixed','visco','contact'],required=True); ap.add_argument('--attempt',required=True); args=ap.parse_args()
    c=spec(args.kind); run=ROOT/'simulation/verification'/('stage09_'+args.kind+'_'+args.attempt)
    run.mkdir(exist_ok=False); scratch=Path(tempfile.gettempdir())/'FDM-Annealing'/run.name; scratch.mkdir(exist_ok=False)
    (run/'input.dat').write_text(deck(c),encoding='ascii'); (run/'case.json').write_text(json.dumps(c,indent=2)); shutil.copyfile(__file__,run/'script_snapshot.py')
    shutil.copyfile(run/'input.dat',scratch/'input.dat')
    cmd=[str(EXE),'-b','-i',str(scratch/'input.dat'),'-o',str(scratch/'mapdl.out'),'-j','structural','-np','1']
    result=subprocess.run(cmd,cwd=scratch,capture_output=True)
    (run/'stdout.log').write_bytes(result.stdout); (run/'stderr.log').write_bytes(result.stderr)
    for p in scratch.iterdir():
        if p.is_file() and p.name!='input.dat': shutil.copyfile(p,run/p.name)
    accepted=False; error=''; rows=[]
    try:
        assert result.returncode==0,'solver return code'
        assert '*** ERROR ***' not in (run/'mapdl.out').read_text(errors='replace'),'MAPDL error'
        rows=compare(c,parse(run/'values.csv')); write_csv(run/'comparison.csv',rows); accepted=all(x['passed'] for x in rows)
    except Exception as exc: error=str(exc)
    manifest=dict(accepted=accepted,error=error,returncode=result.returncode,command=cmd,files={p.name:digest(p) for p in run.iterdir() if p.is_file()})
    (run/'manifest.json').write_text(json.dumps(manifest,indent=2))
    print(run.name,'accepted=',accepted,'error=',error)
    for x in rows:
        if not x['passed']: print(x)
    if not accepted: raise SystemExit(2)
if __name__=='__main__': main()
