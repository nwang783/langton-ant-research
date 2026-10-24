"""Independent literal tile proof and complete-field controls for every-r hairpin."""
from pathlib import Path
from collections import defaultdict
import json,hashlib
ROOT=Path('/workspace/shared/langton');U='LRLLLLRRRRLRRL';V='RLRRLL';q=-1+3j
expected={(-2,0):'L',(-2,1):'LR',(-2,2):'R',(-1,0):'RLR',(-1,1):'LRL',(-1,2):'L',(0,0):'LRL',(0,1):'RL',(0,2):'L',(0,3):'R',(1,1):'R',(1,2):'R'}
def walk(w,z=0j,h=1j):
 reads=[]
 for c in w:
  reads.append((z,c));h*= -1j if c=='R' else 1j;z+=h
 return z,h,reads
zu,hu,ur=walk(U);zv,hv,vr=walk(V,q+1,1)
assert (zu,hu)==(q,1j) and (zv,hv)==(1,1)
tile=defaultdict(str)
for z,c in ur+vr:tile[(int(z.real),int(z.imag))]+=c
assert dict(tile)==expected
assert len({3*x+y for x,y in tile})==12 and 3*q.real+q.imag==0
assert all(all(a!=b for a,b in zip(w,w[1:]))for w in tile.values())
# General proof: U copy i has all its read points i*q+ur; V copy k has
# all points (r-k-1)*q+vr. The distinct linear functional classes imply
# no cross-tile overlaps; the sole extra central read at r*q is outside
# the class-zero tile index range. Thus this table proves every r.
I={complex(x,y)for(x,y),w in tile.items()if w[0]=='L'};O={complex(x,y)for(x,y),w in tile.items()if w[-1]=='R'}
assert len(I)==len(O)==6 and len(I&O)==1
checks=[]
for r in [1,2,3,4,7,16,31,64,257]:
 initial={z+i*q for z in I for i in range(r)};wanted={z+i*q for z in O for i in range(r)}|{r*q}
 board=set(initial);z=0j;h=1j;history=defaultdict(str)
 for c in U*r+'R'+V*r:
  assert (z in board)==(c=='L');history[z]+=c
  if z in board:board.remove(z)
  else:board.add(z)
  h*= -1j if c=='R'else 1j;z+=h
 assert z==1 and h==1 and board==wanted
 assert len(initial)==6*r and len(board)==6*r+1 and len(history)==12*r+1 and len(initial^board)==10*r+1
 assert history[r*q]=='R'
 for i in range(r):
  for (x,y),w in tile.items():assert history[complex(x,y)+i*q]==w
 checks.append({'r':r,'reads':20*r+1,'input':len(initial),'output':len(board),'visited':len(history),'xor':len(initial^board)})
 for c in 'RRR':
  assert z not in board;board.add(z);h*= -1j;z+=h
 assert z==0 and h==1j and len(board)==6*r+4 and len(initial^board)==10*r+4
 checks[-1]['closed_pose_extension']={'reads':20*r+4,'output':len(board),'xor':len(initial^board)}
note=ROOT/'causal_reduction/unit_scale/decorated_oblique_hairpin.md'
out={'status':'PASS independent exact tile identity proving all r, plus complete-field controls','tile':[{ 'cell':list(z),'history':w,'invariant':3*z[0]+z[1]}for z,w in sorted(tile.items())],'controls':checks,'note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'scope':'All W_r=U^r R V^r internally legal, exact minimum6r input. Not nested root prefixes or a finite-fuel construction.'}
(ROOT/'audits/check_oblique_hairpin_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
