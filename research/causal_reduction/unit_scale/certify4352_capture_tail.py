"""Exact all-M/all-future tail ownership for the supplied394 capture contract.
The finite prefix's legality is a separate chronology obligation. This checker
retains the complete XOR of every initial cell and every prescribed past read,
normalizes the final head, and proves the entire infinite104 input interface.
"""
from pathlib import Path
from collections import defaultdict,Counter
from fractions import Fraction
import json,hashlib
from check_prepared1564_router_geometry import trace
P=Path(__file__).resolve().parent;J=json.loads((P/'prepared4352_capture_manifest.json').read_text());mod=78
# Normalize by adding(156M,156M); the head is fixed at(-399,-429,N).
rr=list(trace(J['tail_word'],(-399,-429),0));assert rr[-1][1:3]==((-401,-431),0)
groups=defaultdict(list)
for i,q,h,c in rr[:-1]:groups[q[0]-q[1],q[0]%2].append((104*(q[0]//2)+i,q[0]//2,c))
needed=set();rays={}
for(t,a),g in groups.items():
 g.sort();mn=min(x[1]for x in g);mx=max(x[1]for x in g);assert g[0][2]=='R'
 for n in range(mn,mx+1):
  f=next(x for x in g if x[1]>=n)
  if f[2]=='L':needed.add((a+2*n,a+2*n-t))
 for aa in range(a,78,2):rays[(t,aa)]=(a+2*mx-aa)//78
E=defaultdict(Counter);count=0

def interval(k,lo,hi):
 global count
 if k not in rays:return
 E[k][lo]^=1;E[k][(hi[0],hi[1]+1)]^=1;count+=1

def point(q,a):
 assert a[0]==a[1]and(a[0]+156)%78==0
 k=(q[0]-q[1],q[0]%78);v=((a[0]+156)//78,q[0]//78);interval(k,v,v)
for s in J['stages']:
 p=(s['start_x_N_constant'][1],s['start_y_N_constant'][1]);a=(s['start_x_N_constant'][0],s['start_y_N_constant'][0]);cc,cd=s['count_N_constant'];rows=list(trace(s['word'],p,s['heading']));d=rows[-1][1][0]-p[0]
 if(cc,cd)==(0,1):
  for _,q,h,c in rows[:-1]:point(q,a)
  continue
 assert rows[-1][1][1]-p[1]==d and d in(-78,-2,2,26)
 res=78//abs(d);assert cc%res==0 and a[0]==a[1]and(a[0]+156)%78==0
 for _,q,h,c in rows[:-1]:
  for r in range(res):
   qq=(q[0]+d*r,q[1]+d*r);k=(qq[0]-qq[1],qq[0]%78);start=((a[0]+156)//78,qq[0]//78);ls=cc//res;lc=(cd-1-r)//res;assert ls+lc>=0
   sg=1 if d>0 else-1;end=(start[0]+sg*ls,start[1]+sg*lc);interval(k,start if sg>0 else end,end if sg>0 else start)
for x,y in J['seed_families']:point((x[1],y[1]),(x[0],y[0]))
for q in needed:interval((q[0]-q[1],q[0]%78),(0,q[0]//78),(0,q[0]//78))
proof=[];tests=0
for k,end in sorted(rays.items()):
 lines=[v for v,b in E[k].items()if b]+[(0,end+1)];cuts={1}
 for i,a in enumerate(lines):
  for b in lines[:i]:
   if a[0]==b[0]:continue
   v=Fraction(b[1]-a[1],a[0]-b[0]);n=v.numerator//v.denominator
   if n>=1:cuts.add(n)
   if n+1>=1:cuts.add(n+1)
 cuts.add(max(cuts)+1);tests+=len(cuts)
 for m in sorted(cuts):
  changes=Counter()
  for(s,c),bit in E[k].items():
   if bit:changes[s*m+c]^=1
  bit=False;previous=None
  for z in sorted(changes):
   assert not(bit and previous<min(z,end+1)),('bad tail field',k,m,previous,z,end)
   bit^=bool(changes[z]);previous=z
  assert not(bit and previous<end+1),('bad tail ray',k,m,previous,end)
 proof.append([list(k),end,len(lines),sorted(cuts)])
out={'scope':__doc__,'status':'ALL-M ALL-FUTURE104 FIELD PASS','domain':'M>=1','normalized_tail_pose':[[-399,-429],0],'tail_drift':[-2,-2],'tail_read_normal_hull':[min(k[0]for k in rays),max(k[0]for k in rays)],'physical_mod2_orbits':len(groups),'split_mod78_rays':len(rays),'required_black_cells':sorted(needed),'restricted_past_interval_families':count,'integer_order_chambers':tests,'proof_digest':hashlib.sha256(json.dumps(proof,separators=(',',':')).encode()).hexdigest(),'manifest_sha256':hashlib.sha256((P/'prepared4352_capture_manifest.json').read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'prepared4352_capture_tail.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
