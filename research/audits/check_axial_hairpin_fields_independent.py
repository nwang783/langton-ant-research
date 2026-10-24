from pathlib import Path
from collections import defaultdict
import json
ROOT=Path('/workspace/shared/langton');U='RRLRRRRL';V='LLRLLRLL'
def walk(w,h=1j):
 z=0j;hist=defaultdict(str)
 for c in w:hist[z]+=c;h*= -1j if c=='R'else 1j;z+=h
 return z,h,hist
assert walk(U)[:2]==(2,1j) and walk(V,1)[:2]==(-2,1)
controls=[]
for r in [1,2,3,4,5,16,31,64,257]:
 z,h,H=walk(U*r+'R'+V*r);assert (z,h)==(1,1)
 expected={}
 def add(xs,y,w):
  for x in xs:assert complex(x,y)not in expected;expected[complex(x,y)]=w
 add(range(1,2*r+1),-2,'R');add(range(1,2*r,2),-1,'LR');add(range(2,2*r+1,2),-1,'RL')
 add([0],0,'RL');add([1],0,'R');add(range(2,2*r),0,'RL');add([2*r],0,'R');add([2*r+1],0,'L')
 add([0],1,'L');add([1],1,'R');add(range(2,2*r,2),1,'LR');add(range(3,2*r,2),1,'RL');add([2*r],1,'R');add([2*r+1],1,'L')
 add(range(1,2*r+1),2,'L');assert dict(H)==expected
 I={p for p,w in H.items()if w[0]=='L'};O={p for p,w in H.items()if w[-1]=='R'}
 assert (len(I),len(O),len(I^O),len(H))==(4*r+2,4*r+3,4*r+7,10*r+4)
 board=set(I);p=0j;hh=1j
 for c in U*r+'R'+V*r:
  assert(p in board)==(c=='L')
  if p in board:board.remove(p)
  else:board.add(p)
  hh*= -1j if c=='R'else 1j;p+=hh
 assert board==O
 controls.append({'r':r,'input':len(I),'output':len(O),'xor':len(I^O),'read_support':len(H)})
res={'status':'PASS independent complete row histories and literal fields; analytic affine-slot proof reviewed','controls':controls,'phase_obstruction':'Half-turn swaps the alternating rail parities, so matching on the identical strip needs odd horizontal translation and hence the wrong x+y+h sector. Only that direct same-strip inverse interface is excluded.','scope':'Prepared local all-r component, not a finite-seed root or renewal.'}
(ROOT/'audits/axial_hairpin_fields_independent.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res))
