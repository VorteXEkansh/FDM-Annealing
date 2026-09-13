"""Validate and register genuine exported result tables; never synthesize rows."""
import argparse, csv, hashlib, json
from pathlib import Path

REQUIRED={"case_id","time_s","quantity","value","unit","location","solver_file"}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("csv_file",type=Path); args=ap.parse_args()
    path=args.csv_file.resolve()
    with path.open(encoding="utf-8-sig",newline="") as f:
        reader=csv.DictReader(f); fields=set(reader.fieldnames or []); rows=list(reader)
    missing=REQUIRED-fields
    if missing: raise SystemExit(f"missing columns: {sorted(missing)}")
    if not rows: raise SystemExit("empty export: no result registered")
    if any(not all(row[k].strip() for k in REQUIRED) for row in rows):
        raise SystemExit("blank required result field")
    record={"path":str(path),"rows":len(rows),"sha256":hashlib.sha256(path.read_bytes()).hexdigest()}
    print(json.dumps(record,indent=2))

if __name__=="__main__": main()

