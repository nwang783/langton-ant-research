from pathlib import Path
from itertools import product
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'K1_pipeline_detours_2026-10-23'
def out(hs):return[(h+(1 if r%2==0 else-1))%4 for r,h in enumerate(hs)]
def selected(h):return[[h,h,(h+2)%4]+tail for tail in([], [h],[(h+2)%4])]
def histories(axis,kind):
 for n in range(1,5):
  for hs in product((axis,(axis+2)%4),repeat=n):
   rs=hs[::2]
   if kind=='strict'and any(h!=axis for h in rs):continue
   if kind=='flat'and(sorted(rs)!=sorted((axis,(axis+2)%4))):continue
   yield list(hs)
def feasible(hs,phase,edges,ineq):
 # Work in raw integer times, then enforce exact same-cell residue via n variables.
 nodes=[(v,r)for v,x in hs.items()for r in range(len(x))];cons=[]
 def lower(a,b,k):cons.append((a,b,(k+phase[a[0]]-phase[b[0]]+3)//4))
 for v,x in hs.items():
  for j in range(len(x)-1):lower((v,j),(v,j+1),4)
 for a,b,direction in edges:
  left=[(a,r)for r,h in enumerate(out(hs[a]))if h==direction];right=[(b,r)for r,h in enumerate(hs[b])if h==direction]
  if len(left)!=len(right):return False
  for x,y in zip(left,right):lower(x,y,1);lower(y,x,-1)
 for x,y,k in ineq:lower(x,y,k)
 # Floyd-Warshall max-plus: a strictly positive diagonal is infeasible.
 n=len(nodes);idx={x:i for i,x in enumerate(nodes)};neg=-10**9;F=[[0 if i==j else neg for j in range(n)]for i in range(n)]
 for a,b,k in cons:F[idx[a]][idx[b]]=max(F[idx[a]][idx[b]],k)
 for k in range(n):
  for i in range(n):
   if F[i][k]==neg:continue
   for j in range(n):
    if F[k][j]!=neg:F[i][j]=max(F[i][j],F[i][k]+F[k][j])
 return all(F[i][i]<=0 for i in range(n))
right=[]
for a,z,y,b in product(selected(0),histories(3,'strict'),histories(0,'strict'),selected(1)):
 hs=dict(A=a,Z=z,Y=y,B=b)
 if feasible(hs,dict(A=0,Z=1,Y=2,B=3),[('A','Z',3),('Z','Y',0),('Y','B',1),('B','A',2)],[(('A',2),('B',1),1)]):right.append(hs)
A=json.loads((D/'right_turn_local_ports.json').read_text());assert len(right)==len(A['rows'])==6
key=lambda h:tuple((v,tuple(h[v]))for v in sorted(h))
assert set(map(key,right))=={key(r['headings'])for r in A['rows']}
branch=[];port_candidates=set()
for a,z,b in product(selected(0),histories(3,'flat'),selected(0)):
 hs=dict(A=a,Z=z,B=b);edges=[('A','Z',3),('Z','B',0)]
 if sum(h==3 for h in z)>=2 and sum(h==0 for h in out(z))>=2:port_candidates.add(tuple(z))
 if feasible(hs,dict(A=0,Z=1,B=2),edges,[(('A',1),('B',0),1),(('B',0),('A',2),1),(('A',2),('B',1),1)]):branch.append(hs)
assert port_candidates=={(3,3,1,1),(3,1,1,3),(1,3,3,1),(1,1,3,3)}
J=json.loads((D/'straight_flat_branch_local_ports.json').read_text());assert len(branch)==len(J['rows'])==4 and set(map(key,branch))=={key(r['headings'])for r in J['rows']}
assert all(z['Z']==[3,3,1,1]and all(len(z[v])==3 or z[v][3]==2 for v in('A','B'))for z in branch)
# Equal-max q's two opposite R headings allow at most one E departure strictly before first S arrival.
qcontrols=[]
for hs in histories(0,'flat'):
 firstS=hs.index(2);count=sum(h==1 for h in out(hs)[:firstS]);assert count<=1;qcontrols.append((hs,count))
result=dict(status='PASS independent complete local ordinal/clock tables and flat-q prefix bound',right_turn_rows=right,straight_flat_branch_rows=branch,q_prefix_controls=qcontrols,source_sha256={f:hashlib.sha256((D/f).read_bytes()).hexdigest()for f in['strict_left_K1_right_turn_table.md','K1_branches_force_bends.md']},scope='Complete white cap4 K1 first-L curves only. Strict-left right-turn six rows are necessary local overapproximations, not exterior realizations. A straight equal-M left branch forces the next face to bend; together with signed five-strict-face obstruction, every six-face window bends. No bend cost, general K1 exclusion, or global capture.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(result['status'],len(right),len(branch))
