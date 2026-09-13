"""Fail-closed MAPDL case runner with immutable input/output manifests."""
from __future__ import annotations
import argparse, hashlib, json, subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAPDL = Path(r"C:\Program Files\ANSYS Inc\ANSYS Student\v261\ansys\bin\winx64\ANSYS261.exe")

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load_case(path: Path) -> dict:
    data=json.loads(path.read_text(encoding="utf-8"))
    required={"case_id","case_kind","parameters","admission"}
    missing=required-data.keys()
    if missing: raise ValueError(f"missing keys: {sorted(missing)}")
    if data["case_kind"] == "production":
        p=data["parameters"]
        for key in ("temperature_C","hold_time_s","fixture_gap_mm","material_id"):
            if key not in p: raise ValueError(f"production case lacks {key}")
        failed=[k for k,v in data["admission"].items() if v is not True]
        if failed: raise RuntimeError(f"production execution blocked by: {', '.join(failed)}")
    elif data["case_kind"] != "environment_smoke":
        raise ValueError("case_kind must be production or environment_smoke")
    return data

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("case",type=Path)
    ap.add_argument("--execute",action="store_true")
    args=ap.parse_args()
    case_path=args.case.resolve(); case=load_case(case_path)
    run_dir=ROOT/"simulation"/"runs"/case["case_id"]
    run_dir.mkdir(parents=True,exist_ok=True)
    input_file=ROOT/"ansys"/"apdl"/"environment_smoke.dat" if case["case_kind"]=="environment_smoke" else None
    command=None; returncode=None
    if args.execute:
        if not MAPDL.exists(): raise FileNotFoundError(MAPDL)
        if input_file is None: raise RuntimeError("production APDL deck is not implemented or admitted")
        command=[str(MAPDL),"-b","-i",str(input_file),"-o",str(run_dir/"mapdl.out"),"-j",case["case_id"],"-np","1"]
        completed=subprocess.run(command,cwd=run_dir,check=False)
        returncode=completed.returncode
    manifest={
      "case_id":case["case_id"],"case_kind":case["case_kind"],
      "created_utc":datetime.now(timezone.utc).isoformat(),"executed":args.execute,
      "returncode":returncode,"command":command,
      "input_sha256":sha256(case_path),
      "apdl_sha256":sha256(input_file) if input_file else None,
      "outputs":{p.name:sha256(p) for p in sorted(run_dir.iterdir()) if p.is_file()}
    }
    (run_dir/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(manifest,indent=2))
    if args.execute and returncode: raise SystemExit(returncode)

if __name__=="__main__": main()

