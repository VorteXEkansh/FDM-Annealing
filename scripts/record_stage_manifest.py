"""Record input, code and output byte hashes without implying numerical evidence."""
from pathlib import Path
import argparse,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser()
ap.add_argument('--stage',type=int,required=True)
args=ap.parse_args()
paths=['docs/PROJECT_STATE.md','docs/novelty_audit.md','docs/research_scope.md','docs/manuscript_restructure_map.md','docs/integrity_report.json',f'docs/stage_{args.stage:02d}_quality.md',f'docs/stage_{args.stage:02d}_literature_integrity.json','literature/literature_matrix.json','literature/literature_matrix.xlsx','literature/references.bib','manuscript/current.md','manuscript/research_scope.md','scripts/build_manuscript.py','scripts/check_integrity.py','scripts/check_literature.py','scripts/verify_delivery.py','scripts/record_stage_manifest.py','output/pdf/Constrained-Annealing-2026-DRAFT.pdf']
if args.stage >= 4:
    paths += ['docs/material_property_audit.md',f'docs/stage_{args.stage:02d}_material_integrity.json','material/pla_properties.csv','material/property_sources.csv','material/uncertainty_ranges.csv','material/fixture_properties.csv','material/build_manifest.json','scripts/build_material_database.py','scripts/check_materials.py']
scope = 'Material-property source audit and manuscript update; no solver execution or simulation findings.' if args.stage >= 4 else 'Document scope finalization; no solver execution or new quantitative findings.'
data={'stage':args.stage,'date':'2026-09-12','algorithm':'SHA-256','files':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},'scope':scope}
(ROOT/f'docs/stage_{args.stage:02d}_manifest.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
print(f'Recorded {len(paths)} input/code/output hashes')
