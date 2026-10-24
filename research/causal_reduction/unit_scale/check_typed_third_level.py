"""Deterministic certificate: no locally legal two-active-phase composite
can be applied to any typed primitive transport image. This author checker
shares palette/trace code; an independent implementation is still required.
"""
import json,pathlib,hashlib,struct,time,collections
from analyze_typed_phase_pairs import inventories,expand,conflict,typed
BASE=pathlib.Path(__file__).parent
st=time.monotonic();dom=inventories();inv=json.load(open(BASE/'analyze_typed_phase_pairs.inventory.json'))
cs=[tuple(z['composite']) for z in inv];assert cs==sorted(set(cs)) and len(cs)==29840
for h in range(4):
 for c in range(2):
  for w in dom[c][1:]:
   counts=collections.Counter(typed(w,h));assert [counts[s] for s in range(8)]==[1+(s==2*h+c) for s in range(8)]
raw=bytearray();latest=0;hist=collections.Counter()
for C in cs:
 for s in range(8):
  for w in dom[s%2][1:]:
   v=expand(w,s//2,C);t=conflict(v,s//2)
   assert t is not None,(C,s,w)
   raw.extend(struct.pack('<H',t));latest=max(latest,t);hist[t]+=1
p=pathlib.Path(__file__);p.with_suffix('.conflicts.u16').write_bytes(raw)
ans=dict(status='COMPLETE',scope='all locally legal two-active-phase composites on all48 typed primitives',controllers=len(cs),cases=len(raw)//2,latest_conflict=latest,ordering='composite tuples lexicographic; state0..7; primitive inventory order after identity; each first conflict is unsigned16 little endian',palettes=dom,conflict_histogram=dict(sorted(hist.items())),records_sha256=hashlib.sha256(raw).hexdigest(),inventory_sha256=hashlib.sha256((BASE/'analyze_typed_phase_pairs.inventory.json').read_bytes()).hexdigest(),seconds=time.monotonic()-st)
p.with_suffix('.json').write_text(json.dumps(ans,indent=2)+'\n');print(json.dumps(ans),flush=True)
