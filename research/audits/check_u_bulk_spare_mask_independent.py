"""Derive U-family inputs from literal reads, then exhaust all anchor placements."""
import json,hashlib
from pathlib import Path
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
K={q for q,b in walk(mark)[2].items()if b};cases={};S={2+3j,3+1j,3+2j};A=2+0j
for a in(7,8,9):
 I={q for q,b in walk(raws[a]+mark)[2].items()if b}-K
 candidates={(q-rotation(z,h),h)for q in S for z in I for h in range(4)};hits=[]
 for p,h in candidates:
  inputs={p+rotation(z,h)for z in I}
  if S<=inputs:assert(p,h)==(3-1j,0)and A in inputs;hits.append([*xy(p),h])
 assert hits==[[3,-1,0]];cases[a]={'candidates_without_sector_filter':len(candidates),'accepted':hits}
note=ROOT/'cut_order_obstruction_2026-10-23/mass_sensitive/all_input/u_bulk_spare_mask_lemma.md'
J={'status':'PASS independent raw+marker input masks and complete anchor placements','cases':cases,'note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'scope':'A literal U-family cannot consume all three original DC spares while preserving original main A. No multistep, replacement, delayed-main or general U-archive exclusion.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(J,indent=2)+'\n');print(json.dumps(J,indent=2))
