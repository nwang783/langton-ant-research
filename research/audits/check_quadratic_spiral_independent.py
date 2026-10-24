"""Literal no-import control for the analytically checked all-n spiral."""
import json,hashlib
from pathlib import Path
from collections import Counter
ROOT=Path('/workspace/shared/langton');D=[1j,1,-1j,-1]
W=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
assert hashlib.sha256(W.encode()).hexdigest()=='9772fa0cced75fab3a1d336c6a1326e0e4be8f4e471a3807e0778fccc94c1f04'
standard={(W+W)[i:i+10] for i in range(104)};assert len(standard)==84
assert all(('RLLR'*4)[i:i+10] not in standard for i in range(4))
P={1-1j,1,-1+1j,1j,-3,-3+1j,-2-1j,-1-1j,-2+1j}
out=[]
for n in [1,2,3,4,7,12,25,64,128]:
 w=''.join('RLLR'*j+'L'+'RLLR'*j+'RLL'+'RLLR'*j+'L'+'RLLR'*j+'L' for j in range(n,0,-1))
 first={};last={};vis=Counter();p=0j;h=1j
 for c in w:
  assert last.get(p)!=c;first.setdefault(p,c);last[p]=c;vis[p]+=1
  h*=(-1j if c=='R' else 1j);p+=h
 assert p==-n+1j*n and h==1j
 seed={q for q,c in first.items() if c=='L'}
 assert len(seed)==11*n+2 and len(w)==8*n*n+14*n and max(vis.values())<=2
 final={q for q,c in last.items() if c=='R'}
 relative=set(P)
 for j in range(2,n+1):
  A={complex(j,-j),complex(j,j-1),complex(j-1,j),complex(-j-2,1-j),complex(-j-2,j),complex(-j-1,-j),complex(j-2,-j)}
  assert len(A)==7 and not(A&relative);relative|=A
 assert final=={z+p for z in relative} and len(final)==7*n+2
 board=set(seed);p2=0j;h2=1j
 for c in w:
  assert c==('L' if p2 in board else 'R')
  board.symmetric_difference_update({p2});h2*=(-1j if c=='R' else 1j);p2+=h2
 assert board==final and p2==p and h2==h
 K=sum(w[t-10:t] not in standard and w[t-9:t+1] not in standard for t in range(10,len(w)))
 assert K>=8*max(n-2,0)**2
 out.append(dict(n=n,entry_mass=len(seed),length=len(w),final_mass=len(final),max_reads=max(vis.values()),internal_K=K))
result=dict(status='PASS independent literal feasibility, minimal seed, complete final profile and internal K count',cases=out,analytic_scope='all-n proof is the separate exact rail/corner overlap argument; finite checks are controls')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
