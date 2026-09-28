"""Stage 11 source, split, extraction and metric checks; no solver validation claim."""
from pathlib import Path
import csv, hashlib, json, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from scripts.build_validation_dataset import extract

def main():
    checks=[]
    def check(name,ok):
        assert ok,name
        checks.append({'check':name,'status':'pass'})
    rows=list(csv.DictReader((ROOT/'validation/validation_dataset.csv').open(encoding='utf-8')))
    check('CSV reproduces source XML exactly',rows==extract())
    check('Unique observation IDs',len(rows)==len({r['observation_id'] for r in rows})==45)
    primary=[r for r in rows if r['dataset_role']=='reserved_validation']
    check('18 primary means: six conditions and three directions',len(primary)==18 and {r['temperature_C'] for r in primary}=={'63','75','86','98','109','132'} and {r['direction'] for r in primary}=={'L','W','H'})
    check('Primary selection excludes powder restraint and melting case',all(r['support']=='without_mould' and r['temperature_C']!='155' for r in primary))
    check('Secondary maxima quarantined',len([r for r in rows if r['dataset_role']=='secondary_quarantined'])==3)
    check('No fabricated predictions, errors or scatter',all(not r['prediction'] and not r['error'] and not r['reported_response_sd'] and r['validation_solved']=='false' for r in rows))
    check('All observed rows unused in calibration',all(r['calibration_used']=='false' for r in rows))
    material_manifest=json.loads((ROOT/'material/build_manifest.json').read_text(encoding='utf-8'))
    check('Reserved validation evidence excluded from material database',all('stage_11/' not in e['path'] for e in material_manifest['evidence']))
    cal=list(csv.DictReader((ROOT/'validation/calibration_register.csv').open(encoding='utf-8')))
    check('Calibration source distinct from external observations',not ({r['doi'] for r in rows}&{r['doi'] for r in cal}) and all(r['independent_validation_eligible']=='false' for r in cal))
    check('Signed primary observations preserved',next(r for r in rows if r['observation_id']=='LC22_75_without_mould_L')['value']=='-1.60' and next(r for r in rows if r['observation_id']=='LC22_63_without_mould_H')['value']=='0.00')
    check('Secondary source extrema preserved',[r['value'] for r in rows if r['dataset_role']=='secondary_quarantined']==['0.7','0.25','5.8'])
    for s in json.loads((ROOT/'validation/source_manifest.json').read_text())['sources']:
        check(s['source_key']+' source and metadata hashes',all(hashlib.sha256((ROOT/s[p]).read_bytes()).hexdigest()==s[h] for p,h in [('path','sha256'),('metadata_path','metadata_sha256')]))
        meta=json.loads((ROOT/s['metadata_path']).read_bytes())['message']
        check(s['source_key']+' DOI exact match',meta['DOI'].lower()==s['doi'].lower())
    subprocess.run([sys.executable,'-m','unittest','discover','-s','tests','-p','test_validation_metrics.py'],cwd=ROOT,check=True)
    check('Four synthetic metric tests pass',True)
    doc=(ROOT/'docs/validation_protocol.md').read_text(encoding='utf-8')
    check('Nonblind reservation and uncertainty limit explicit','not a blinded test' in doc and 'indeterminate: missing uncertainty' in doc and 'Do not calculate R²' in doc)
    paths=['validation/validation_dataset.csv','validation/source_manifest.json','validation/calibration_register.csv','docs/validation_protocol.md','scripts/build_validation_dataset.py','scripts/check_validation_stage.py','analysis/validation_metrics.py','tests/test_validation_metrics.py']
    report={'stage':11,'date':'2026-09-28','passed':True,'count':len(checks),'checks':checks,'observation_count':45,'reserved_primary_count':18,'excluded_context_count':24,'secondary_quarantined_count':3,'solver_validation_executed':False,'physical_validation_pass_claimed':False,'source_hashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
    (ROOT/'docs/stage_11_validation_checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(f'{len(checks)} validation-design checks passed; no validation solve')

if __name__=='__main__':main()
