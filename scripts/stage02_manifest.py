"""Hash the Stage 2 research inputs, maintained code and complete outputs."""
from pathlib import Path
import hashlib,json,sys,importlib.metadata
ROOT=Path(__file__).resolve().parents[1]
paths=[]
for d in ['literature','scripts','manuscript']:
 paths.extend(p for p in (ROOT/d).glob('**/*') if p.is_file() and 'node_modules' not in p.parts and '__pycache__' not in p.parts and not p.name.endswith('.inspect.ndjson'))
paths.extend(ROOT/p for p in ['docs/PROJECT_STATE.md','docs/base_paper_audit.md','docs/novelty_audit.md','docs/literature_search_strategy.md','docs/stage_02_quality.md','docs/integrity_report.json','docs/literature_integrity_report.json','output/pdf/Constrained-Annealing-2026-DRAFT.pdf'])
manifest={'stage':2,'date':'2026-09-12','python':sys.version.split()[0],'packages':{x:importlib.metadata.version(x) for x in ['reportlab','pypdf','pdfplumber','Pillow','lxml']},'hash_algorithm':'SHA-256','files':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(set(paths))},'note':'File-byte hashes at stage completion; immutable external metadata and source-download hashes are recorded separately. No solver results.'}
(ROOT/'docs/stage_02_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8',newline='\n')
print(f'Hashed {len(paths)} stage files')
