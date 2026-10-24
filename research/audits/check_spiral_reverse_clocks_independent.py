"""No-import exact controls for the analytic seven-arm reverse obstruction."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib,json
D=((0,1),(1,0),(0,-1),(-1,0))
cap={(1,-1),(1,0),(-1,1),(0,1),(-3,0),(-3,1),(-2,-1),(-1,-1),(-2,1)}
def chi(p): return 1 if sum(p)%2==0 else -1
def clocks(B,p,h):
 s=chi(p)*((-1)**h)
 e=sum(D[h])
 return tuple(-s*sum((chi(q)*Q(3)**(t*sum(q)) for q in B),Q(0))+(Q(1,2) if t*e==1 else Q(-3,2))*Q(3)**(t*sum(p)) for t in (1,-1))
step=[]
for h in range(4):
 for black in (0,1):
  B={(0,0)} if black else set(); before=clocks(B,(0,0),h)
  hp=(h+(-1 if black else 1))%4; p=D[hp]
  B.symmetric_difference_update({(0,0)}); after=clocks(B,p,hp)
  gains=tuple(b-a for a,b in zip(before,after)); assert min(gains)>=0
  step.append({'heading':h,'black':black,'gains':list(map(str,gains))})
cases=[]
for n in (1,2,3,5,10,20,50,100):
 B=set(cap)
 for j in range(2,n+1):
  arm={(j,-j),(j,j-1),(j-1,j),(-j-2,1-j),(-j-2,j),(-j-1,-j),(j-2,-j)}
  assert len(arm)==7 and not (arm&B)
  gains=tuple(-sum((chi(q)*Q(3)**(t*sum(q)) for q in arm),Q(0)) for t in (1,-1))
  assert gains==(Q(2,3)*(Q(9)**j+Q(9)**(-j))-Q(11,9),6*(Q(9)**j+Q(9)**(-j))-19)
  B.update(arm)
 A,C=clocks(B,(0,0),0)
 assert len(B)==7*n+2
 assert A==Q(253,54)+sum((Q(2,3)*(Q(9)**j+Q(9)**(-j))-Q(11,9) for j in range(2,n+1)),Q(0))
 assert C==9*A-8*n+2 and A>=Q(1,2)*9**n and C>=4*9**n
 for h in range(4):
  p=(0,0);q=(-D[h][0],-D[h][1]);hp=(h+2)%4
  assert clocks(B,q,hp)==tuple(-v for v in clocks(B,p,h))
 for tx,ty in ((0,1),(3,4),(-n-4,n-1),(-101,42)):
  assert (tx+ty)%2==1
  Y={(tx-x,ty-y) for x,y in B};s=tx+ty
  assert clocks(Y,(tx,ty+1),0)==(-Q(3)**s*C,-Q(3)**(-s)*A)
 cases.append({'n':n,'A':str(A),'C':str(C)})
root=Path(__file__).resolve().parents[1]
note=root/'core_periodicity_new/spiral_reverse_interface_obstruction.md'
result={'status':'PASS','scope':'Exact local identities and finite arithmetic controls supplement the all-n analytic proof; no distributed-repair impossibility is claimed.','note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'literal_step_gains':step,'cases':cases}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: 8 step cases, all displayed arm identities, 32 reversals and 32 sector-compatible half-turns')
