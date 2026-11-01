"""Validate and register genuine exported result tables; never synthesize rows."""
import argparse, csv, hashlib, json, math
from pathlib import Path

REQUIRED={"case_id","time_s","quantity","value","unit","location","solver_file"}

def validate_export(path, evidence_root=None):
    path=Path(path).resolve()
    evidence_root=Path(evidence_root or path.parent).resolve()
    with path.open(encoding="utf-8-sig",newline="") as f:
        reader=csv.DictReader(f); fields=set(reader.fieldnames or []); rows=list(reader)
    missing=REQUIRED-fields
    if missing: raise ValueError(f"missing columns: {sorted(missing)}")
    if not rows: raise ValueError("empty export: no result registered")
    raw={}
    for n,row in enumerate(rows,1):
        if not all(isinstance(row.get(k),str) and row[k].strip() for k in REQUIRED):
            raise ValueError(f"row {n}: blank required result field")
        t,value=float(row['time_s']),float(row['value'])
        if not math.isfinite(t) or t<0 or not math.isfinite(value):
            raise ValueError(f'row {n}: non-finite value or invalid time')
        source=(evidence_root/row['solver_file']).resolve()
        if not source.is_relative_to(evidence_root) or source==path:
            raise ValueError(f'row {n}: solver evidence must be a distinct file inside evidence root')
        if not source.is_file():raise FileNotFoundError(source)
        key=source.relative_to(evidence_root).as_posix()
        if key not in raw:
            with source.open('rb') as f:raw[key]=hashlib.file_digest(f,'sha256').hexdigest()
    return {"path":str(path),"rows":len(rows),"sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
            'evidence_root':str(evidence_root),'raw_sha256':raw,
            'scope':'Schema, finite values and source-file integrity only; not solver convergence or physical validation'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("csv_file",type=Path)
    ap.add_argument('--evidence-root',type=Path);args=ap.parse_args()
    record=validate_export(args.csv_file,args.evidence_root)
    print(json.dumps(record,indent=2))

if __name__=="__main__": main()

