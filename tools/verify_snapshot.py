#!/usr/bin/env python3
"""Verify exported evidence bytes, not mathematical correctness."""
import argparse,hashlib,json,sys
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--bulk-root',type=Path);args=ap.parse_args()
root=Path(__file__).resolve().parents[1];checked=0;missing=[];bad=[];archived=0;transformed=0
for line in (root/'manifests/artifacts.jsonl').read_text().splitlines():
 row=json.loads(line)
 if row['disposition']=='bulk_archive':
  archived+=1
  if args.bulk_root is None:continue
  p=args.bulk_root/row['path']
 else:p=root/'research'/row['path']
 if not p.is_file():missing.append(row['path']);continue
 h=hashlib.sha256()
 with p.open('rb')as f:
  while b:=f.read(1024*1024):h.update(b)
 if p.stat().st_size!=row['bytes']or h.hexdigest()!=row['sha256']:bad.append(row['path'])
 checked+=1
 if row.get('source_sha256'):transformed+=1
print(json.dumps(dict(checked=checked,bulk_artifacts=archived,bulk_checked=args.bulk_root is not None,privacy_transformed_artifacts_checked=transformed,integrity_basis="Export SHA-256; original source hashes are provenance, not substituted proof verification",missing=missing,mismatched=bad),indent=2))
sys.exit(bool(missing or bad))
