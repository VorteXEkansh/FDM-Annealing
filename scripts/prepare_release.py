"""Create Stage 20 traceability from existing evidence; never execute a solver."""
from pathlib import Path
import csv, hashlib, json, re, subprocess
ROOT=Path(__file__).resolve().parents[1]
def sha(p):
    if (ROOT/p).is_file():
        return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
    for register in ['external_evidence.csv', 'external_scratch.csv']:
        for record in rows('reproducibility/'+register):
            if record['path']==p:
                return record['sha256']  # Registered provenance, not fresh byte verification.
    raise FileNotFoundError(p)
def rows(p):
    with (ROOT/p).open(encoding='utf-8-sig') as f:return list(csv.DictReader(f))
def write(p,data,fields=None):
    dest=ROOT/p;dest.parent.mkdir(parents=True,exist_ok=True)
    with dest.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields or list(data[0]),lineterminator='\n');w.writeheader();w.writerows(data)
def main():
    trace=[]
    def add(claim,loc,data,row,value,unit,run,raw,category='A genuine solver output / B calculation'):
        paths=[f'{run}/{x}' for x in raw if (ROOT/run/x).exists()] if run else raw
        trace.append(dict(claim_id=f'Q{len(trace)+1:04d}',claim=claim,manuscript_location=loc,processed_data=data,record=row,value=value,unit=unit,evidence_category=category,raw_export=';'.join(paths),raw_sha256=';'.join(sha(p) for p in paths),ansys_case=f'{run}/case.json' if run else '',ansys_input=f'{run}/input.dat' if run else '',input_sha256=sha(f'{run}/input.dat') if run else '',processed_sha256=sha(data)))
    for p in ['verification/thermal_verification.csv','verification/structural_verification.csv','verification/contact_verification.csv']:
        for i,r in enumerate(rows(p),1):
            thermal='thermal_' in p
            add('Center temperature and analytical error' if thermal else r['case']+' '+r['quantity']+' versus analytical reference','Abstract; §4.1; Conclusions; Tables 1, S5–S6',p,i,r.get('ansys',r.get('ansys_temperature_C')), '°C' if thermal else r['quantity'],r.get('run_path','simulation/verification/stage08_attempt_05'),['solver_center_temperature.csv'] if thermal else ['values.csv'])
    for i,r in enumerate(rows('convergence/stage_19_audited_refinement.csv'),1):
        add(r['quantity']+'; refinement '+r['interpretation'],'Abstract; §§4.2–4.3; Figures 2–3; Tables 2–3; Conclusions','convergence/stage_19_audited_refinement.csv',i,r['value'],r['unit'],r['run_path'],['top_nodes.csv','element_stress.csv','temperature_profile.csv','contact_values.csv','reaction.csv'])
    for i,r in enumerate(rows('convergence/contact_sensitivity.csv'),1):
        for k in ['mean_contact_pressure_MPa','maximum_contact_pressure_MPa','maximum_penetration_mm','normal_reaction_N_per_mm']:
            add(r['case']+' '+k,'§4.14; Figure 4; Table S7','convergence/contact_sensitivity.csv',i,r[k],k,r['run_path'],['contact_values.csv','reaction.csv'])
    for p in ['material/pla_properties.csv','material/fixture_properties.csv']:
        for i,r in enumerate(rows(p),1):
            source=next(s for s in rows('material/property_sources.csv') if s['source_key']==r['source_key'])
            add(r['property_symbol']+'; '+r['source_locator'],'§3.3; Tables S2–S3; supplementary property register',p,i,r['value'],r['unit'],'',[source['local_evidence']],'C verified publication; formulation/use restrictions retained')
    for i,r in enumerate(rows('validation/validation_dataset.csv'),1):
        # Whole observation retained; no prediction exists.
        add('Published observation only; '+r['observation_id']+'; '+r['source_locator'],'§3.13; §4.4; Table S4','validation/validation_dataset.csv',i,r['value'],r['unit'], '',[r['source_path']],'C published observation; not a validation prediction')
    previous=None
    for i,r in enumerate(rows('convergence/timestep_convergence.csv'),1):
        if r['model']=='thermal' and r['quantity']=='thermal_lag_at_300_s':
            if previous:
                add('Pairwise thermal profile RMSE; '+r['level']+' versus '+previous['level'],
                    'Figure 3; Table 3; Conclusion 6 (finest pair)',
                    'convergence/timestep_convergence.csv',i,r['profile_RMSE_C_vs_previous'],'°C',
                    r['run_path'],['temperature_profile.csv'])
                trace[-1]['raw_export']+=';'+previous['run_path']+'/temperature_profile.csv'
                trace[-1]['raw_sha256']+=';'+sha(previous['run_path']+'/temperature_profile.csv')
            previous=r
    write('reproducibility/result_traceability.csv',trace)
    figs=[]
    for num,name,dataset in [(1,'geometry','geometry/geometry_definition.json'),(2,'mesh_convergence','convergence/mesh_convergence.csv'),(3,'timestep_convergence','convergence/timestep_convergence.csv'),(4,'contact_sensitivity','convergence/contact_sensitivity.csv')]:
        path='figures/release/geometry.png' if num==1 else f'figures/publication_stage19/{name}.png'
        cases=sorted({r['ansys_case'] for r in trace if (f'Figure {num}' in r['manuscript_location'] or (num in [2,3] and 'Figures 2–3' in r['manuscript_location'])) and r['ansys_case']})
        figs.append(dict(figure=f'Figure {num}',source_script='scripts/build_manuscript.py; scripts/build_release.py' if num==1 else 'scripts/build_review_figures.py',source_dataset=dataset,ansys_case=';'.join(cases),output_file=path,interpretation='Design schematic; not a solver result' if num==1 else 'Verification benchmarks only; no AI-generated imagery'))
    write('reproducibility/figure_manifest.csv',figs)
    source=(ROOT/'manuscript/current.md').read_text(encoding='utf-8');tables=[];counts={'TABLE:':0,'SUPPTABLE:':0}
    mapping=['verification/structural_verification.csv;verification/contact_verification.csv','convergence/stage_19_audited_refinement.csv','convergence/stage_19_audited_refinement.csv','literature/literature_matrix.json','material/pla_properties.csv','material/fixture_properties.csv','validation/validation_dataset.csv','verification/thermal_verification.csv','verification/structural_verification.csv','convergence/contact_sensitivity.csv']
    for line in source.splitlines():
        for token in counts:
            if line.startswith(token):
                counts[token]+=1;label=('S' if token=='SUPPTABLE:' else '')+str(counts[token])
                tables.append(dict(table='Table '+label,caption=line[len(token):].strip(),source_dataset=mapping[len(tables)],source_script='scripts/build_manuscript.py; scripts/build_release.py',output_file='manuscript/current.md',ansys_cases='See reproducibility/result_traceability.csv',type='Publication summary with explicit limits'))
    extra=['verification/structural_verification.csv','verification/contact_verification.csv','convergence/stage_19_audited_refinement.csv','material/pla_properties.csv','convergence/mesh_convergence.csv;convergence/timestep_convergence.csv;convergence/contact_sensitivity.csv']
    captions=[s[10:].strip() for s in (ROOT/'supplementary/current.md').read_text(encoding='utf-8').splitlines() if s.startswith('SUPPTABLE:')][7:]
    for n,(caption,data) in enumerate(zip(captions,extra),8):tables.append(dict(table=f'Table S{n}',caption=caption,source_dataset=data,source_script='scripts/build_release.py',output_file='supplementary/current.md',ansys_cases='See reproducibility/result_traceability.csv',type='Complete detailed evidence table'))
    write('reproducibility/table_manifest.csv',tables)
    tracked=subprocess.check_output(['git','ls-files'],cwd=ROOT,text=True).splitlines()
    excluded=[]
    for p in tracked:
        if p.startswith('literature/evidence/') and p.endswith('.pdf'):
            matches=[s for s in rows('material/property_sources.csv') if s['local_evidence']==p]
            excluded.append(dict(path=p,sha256=sha(p),source_url=matches[0]['source_url'] if matches else 'See literature/references.bib and acquisition_manifest.json',reason='Third-party PDF excluded from release tree; local evidence unchanged; prior Git history not rewritten'))
    if excluded:write('reproducibility/external_evidence.csv',excluded)
    inventory=[dict(path=p,size_bytes=(ROOT/p).stat().st_size,sha256=sha(p)) for p in tracked if (ROOT/p).is_file() and (ROOT/p).stat().st_size>10_000_000]
    write('reproducibility/large_file_inventory.csv',inventory,['path','size_bytes','sha256'])
    print(f'{len(trace)} traceability rows, {len(figs)} figures, {len(tables)} summary tables; {len(inventory)} tracked files above 10 MB')
if __name__=='__main__':main()
