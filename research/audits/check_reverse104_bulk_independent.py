"""Independent complex-coordinate complete orbit histories and every shift class."""
from pathlib import Path
from collections import defaultdict
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'causal_reduction/unit_scale';H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];J=json.loads((D/'shifted_reverse104_bulk.json').read_text())
def profile(word,p,h,sign):
 hist=defaultdict(list)
 for t,c in enumerate(word):
  x,y=int(p.real),int(p.imag);e=x%2;q=(x-e)//2
  hist[x-y,e].append((t+sign*104*q,c))
  h*=(-1j if c=='R'else 1j);p+=h
 for v in hist.values():
  v.sort();assert len({t for t,c in v})==len(v)
  assert all(a[1]!=b[1]for a,b in zip(v,v[1:]))
 return hist,p,h
forward,ep,eh=profile(H,0j,1,-1);assert(ep,eh)==(2+2j,1)
assert all(v[0][1]=='R'for v in forward.values())
wake={k for k,v in forward.items()if len(v)%2}
rev=H[::-1].translate(str.maketrans('RL','LR'))
back,ep,eh=profile(rev,-1+0j,-1,1);assert(ep,eh)==(-3-2j,-1)
black={k for k,v in back.items()if v[0][1]=='L'};white=set(back)-black
assert wake==black and len(wake)==12 and len(white)==10 and len(forward)==22
assert sorted(wake)==list(map(tuple,J['wake_black_classes']))
assert sorted(white)==list(map(tuple,J['reverse_white_classes']))
assert min(z for z,e in wake)==-7 and max(z for z,e in wake)==3
assert len({e for z,e in wake if z==-6})==1
# All potentially overlapping transverse shifts are EXACT differences of z's.
lo=min(a-c for a,b in wake for c,d in black);hi=max(a-c for a,b in wake for c,d in black);assert(lo,hi)==(-10,10)
rows=[];allmatch=[]
for e in range(2):
 for dz in range(lo,hi+1):
  translated=lambda k:(k[0]+dz,(k[1]+e)%2)
  missing=sum(translated(k)not in wake for k in black);polluted=sum(translated(k)in wake for k in white)
  if missing==0:allmatch.append((e,dz,polluted))
  if dz%2:rows.append({'translation':[e,e-dz],'missing':missing,'polluted':polluted,'total':missing+polluted})
assert allmatch==[(0,0,0)]
assert rows==J['same_sector_overlap_classes']
assert min(q['missing']for q in rows)==7 and min(q['total']for q in rows)==10
# Initial pose sectors differ; only odd tx+ty restores them, equivalently odd dz.
assert (0+0+1)%2 != (-1+0+3)%2
out={'status':'PASS exact forward/reverse bulk profiles and all translated interfaces','candidate_sha256':hashlib.sha256((D/'shifted_reverse104_bulk.json').read_bytes()).hexdigest(),'forward_classes':22,'black_classes':12,'white_classes':10,'matching_shift_classes_mod_2_2':allmatch,'sector_repair_minimum_missing_black':7,'sector_repair_minimum_total_changed':10,'scope':'Translated exact reverse104 bulk only, with bounded endpoint repairs. Not arbitrary return words, a reusable wake, or an infinite-seed ant claim.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
