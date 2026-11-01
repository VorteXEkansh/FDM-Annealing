"""Audit immutable verification runs and regenerate derived tables; no solver call."""
import argparse,csv,json,math,hashlib
from pathlib import Path
from run_master_nonisothermal import ROOT,SAMPLES,reference,temperature,writecsv

def rows(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--audit-reference',action='store_true');a=ap.parse_args()
    runs=ROOT/'simulation/master/nonisothermal';byrun={};details=[];stats=[];paired=[]
    ref=reference(.0005) if a.audit_reference else None
    for run in sorted(runs.iterdir()):
        if not run.is_dir():continue
        manifest=json.loads((run/'manifest.json').read_text());case=json.loads((run/'case.json').read_text())
        for name,h in manifest['files'].items():
            if name=='noniso.rst' and not (run/name).is_file():continue # optional local solver binary
            assert hashlib.sha256((run/name).read_bytes()).hexdigest()==h,(run.name,name)
        if not (run/'comparison.csv').exists():continue
        rr=rows(run/'comparison.csv');byrun[run.name]=rr
        assert [float(r['time_s']) for r in rr]==SAMPLES
        raw=[[float(v) for v in row if v.strip()] for row in csv.reader((run/'values.csv').open())]
        for data,r in zip(raw,rr):
            t,T,stress,uy,reaction=data;r0=float(r['reference_stress_MPa']);assert abs(t-float(r['time_s']))<1e-7 and stress==float(r['ansys_stress_MPa'])
            assert abs(stress-r0)==float(r['absolute_error_MPa']);assert math.isclose(abs(stress-r0)<=float(r['tolerance_MPa']),r['passed']=='True')
            if ref:assert abs(ref[round(t,8)]['stress_MPa']-r0)<1e-10
            details.append(dict(attempt=run.name,dt_s=case['dt_s'],table_spacing_C=case['shift_table_spacing_C'],run_accepted=manifest['accepted'],raw_export=(run/'values.csv').relative_to(ROOT).as_posix(),**r))
        stats.append(dict(attempt=run.name,dt_s=case['dt_s'],table_spacing_C=case['shift_table_spacing_C'],passed_samples=sum(r['passed']=='True' for r in rr),total_samples=len(rr),run_accepted=manifest['accepted'],max_abs_error_MPa=max(float(r['absolute_error_MPa']) for r in rr),max_relative_error_pct=max(float(r['relative_error_percent']) for r in rr),rms_error_MPa=math.sqrt(math.fsum(float(r['absolute_error_MPa'])**2 for r in rr)/len(rr)),max_reference_check_change_MPa=max(float(r['reference_refinement_change_MPa']) for r in rr),max_reaction_imbalance_N=max(abs(float(r['ansys_stress_MPa'])+float(r['ansys_reaction_N'])) for r in rr)))
    out=ROOT/'verification';writecsv(out/'master_nonisothermal.csv',details);writecsv(out/'master_nonisothermal_summary.csv',stats)
    for ia,first in enumerate(stats):
        for second in stats[ia+1:]:
            if (first['table_spacing_C']==second['table_spacing_C'])==(first['dt_s']==second['dt_s']):continue
            coarse,fine=sorted((first,second),key=lambda v:(v['dt_s'],v['table_spacing_C']),reverse=True)
            x=byrun[coarse['attempt']];y=byrun[fine['attempt']];d=[abs(float(u['ansys_stress_MPa'])-float(v['ansys_stress_MPa'])) for u,v in zip(x,y)]
            passed=[e<=.0001+.002*abs(float(v['ansys_stress_MPa'])) for e,v in zip(d,y)]
            paired.append(dict(axis='timestep' if first['dt_s']!=second['dt_s'] else 'shift_table_spacing',coarse=coarse['attempt'],fine=fine['attempt'],max_difference_MPa=max(d),max_relative_difference_percent=max(100*e/abs(float(v['ansys_stress_MPa'])) for e,v in zip(d,y)),passed_samples=sum(passed),sample_count=len(d),all_pass=all(passed)))
    if paired:writecsv(out/'master_nonisothermal_refinement.csv',paired)
    print(stats);print(paired)
if __name__=='__main__':main()
