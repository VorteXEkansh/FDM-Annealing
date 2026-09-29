"""Stage 15 source-availability audit, restricted to actual Stage 14 outputs."""
from pathlib import Path
import csv,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    source=ROOT/'data/processed/all_cases.csv'
    with source.open(encoding='utf-8') as f: cases=list(csv.DictReader(f))
    previous=json.loads((ROOT/'docs/stage_14_manifest.json').read_text())['files']
    assert sha(source)==previous['data/processed/all_cases.csv'],'Stage 14 registry changed'
    assert not cases,'New outputs require genuine numerical postprocessing, not this empty-source audit'
    assert {p.relative_to(ROOT/'data/raw').as_posix() for p in (ROOT/'data/raw').rglob('*') if p.is_file()}=={'README.md'}
    campaign=json.loads((ROOT/'docs/stage_14_campaign_checks.json').read_text())
    assert not campaign['campaign_completed'] and campaign['launched_cases']==0
    required={
      'thermal_history':'Part and ambient temperature versus time with locations and phase definitions',
      'fixture_gap_onset':'Actual local gap and contact status versus time; pressure penetration and solver tolerances',
      'temperature_effects':'Matched cases differing in temperature within admitted material domain',
      'holding_time_effects':'Matched cases differing in attained-temperature holding time',
      'warpage_suppression':'Matched FREE and GAP released-state warpage with the same reference fit and observation time',
      'dimensional_change':'Signed directional initial and final landmark dimensions at the same observation state',
      'residual_stress':'Matched cooled and released stress fields with a fixed scalar and region definition',
      'contact_pressure':'Pressure contact-area and reaction histories under matched restraint definitions',
      'constraint_tradeoffs':'Matched dimensional warpage and stress responses from admitted case pairs'}
    out=ROOT/'data/processed/postprocessing_availability.csv'
    with out.open('w',encoding='utf-8',newline='') as f:
        w=csv.writer(f,lineterminator='\n');w.writerow(['analysis','status','required_evidence','eligible_stage14_cases','absolute_change','percentage_change','response_minimum','response_maximum','response_range','plot_path'])
        for topic,need in required.items():w.writerow([topic,'not_computable_no_stage14_solver_outputs',need,0,'','','','','',''])
    paths=['data/processed/all_cases.csv','data/processed/postprocessing_availability.csv','data/raw/README.md','docs/stage_14_campaign_checks.json','docs/postprocessing_status.md','scripts/check_postprocessing_stage.py']
    report={'stage':15,'date':'2026-09-30','passed':True,'scope':'Availability and provenance audit only; no numerical result analysis',
            'eligible_stage14_cases':0,'matched_free_gap_pairs':0,'analysis_topics':len(required),'numerical_analysis_completed':False,'plots_generated':0,
            'unexpected_trend_review':'not_possible_no_outputs','smoothing_applied':False,
            'source_hashes':{p:sha(ROOT/p) for p in paths}}
    (ROOT/'docs/stage_15_postprocessing_checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
    print('Nine requested analyses audited; no Stage 14 numerical outputs or matched pairs')
if __name__=='__main__':main()
