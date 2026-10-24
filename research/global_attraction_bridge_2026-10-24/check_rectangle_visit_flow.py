"""Directed visit-flow inequality on actual complete confined ant intervals."""
from pathlib import Path
from collections import Counter
from math import comb
import json,hashlib,time
P=Path(__file__).parent
DIR=[(0,1),(1,0),(0,-1),(-1,0)]

def tables(W,H):
 A={};K={}
 for i in range(W):
  for j in range(H):
   K[i,j]=2**(i+j)*comb(i+j,i)
   A[i,j]=1+2*A.get((i-1,j),0)+2*A.get((i,j-1),0)
 S=sum(A.values())
 assert S==sum((W-i)*(H-j)*k for (i,j),k in K.items())
 return A,K,S

def verify(M,s,e,box):
 x0,x1,y0,y1=box;W=x1-x0+1;H=y1-y0+1
 for (x,y),m in M.items():
  assert m<=2*(M[x-1,y]+M[x,y-1])+1+2*((x,y)==s)+((x,y)==e),(M,s,e,(x,y),m)
 return True

def exact_bound(M,s,e,box):
 x0,x1,y0,y1=box;W=x1-x0+1;H=y1-y0+1
 row=[0]*H;S=0;targets={(x1-s[0],y1-s[1]),(x1-e[0],y1-e[1]),(W-1,H-1)};vals={}
 def kernel(i,j):return 2**(i+j)*comb(i+j,i) if i>=0 and j>=0 else 0
 for i in range(W):
  for j in range(H):
   row[j]=1+2*row[j]+(2*row[j-1] if j else 0);S+=row[j]
   if (i,j)in targets:vals[i,j]=row[j]
   q=(i+x0,j+y0)
   if q in M:assert M[q]<=row[j]+2*kernel(q[0]-s[0],q[1]-s[1])+kernel(q[0]-e[0],q[1]-e[1])
 bound=S+2*vals[x1-s[0],y1-s[1]]+vals[x1-e[0],y1-e[1]]
 assert sum(M.values())<=bound
 assert bound<=S+3*vals[W-1,H-1]<=(W*H+3)*(4**(W+H-1)-1)//3
 return bound

def complete_small(W,H):
 cells=[(x,y)for x in range(W)for y in range(H)];box=(0,W-1,0,H-1);prefixes=0;max_exit=0;digest=hashlib.sha256();cases=0
 for mask in range(1<<len(cells)):
  B0={q for i,q in enumerate(cells)if mask>>i&1}
  for s in cells:
   for hd in range(4):
    B=set(B0);p=s;h=hd;M=Counter([p]);steps=0
    while 0<=p[0]<W and 0<=p[1]<H:
     verify(M,s,p,box);exact_bound(M,s,p,box);prefixes+=1
     ch='L'if p in B else'R';B.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p=(p[0]+DIR[h][0],p[1]+DIR[h][1]);steps+=1
     if 0<=p[0]<W and 0<=p[1]<H:M[p]+=1
     assert steps<1000
    max_exit=max(max_exit,steps);cases+=1;digest.update(f'{mask},{s},{hd},{steps};'.encode())
 return dict(width=W,height=H,complete_states=cases,confined_prefixes=prefixes,max_exit_updates=max_exit,results_sha256=digest.hexdigest())

small=[]
for W,H in[(1,6),(2,4),(3,3)]:
 small.append(complete_small(W,H));print(small[-1],flush=True)
R=json.loads((P/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());J=json.loads((P/'DROUGHT_BOUNDARY_PINNING_CHECKED.json').read_text());controls=[]
for n in[100,137]:
 qm=(202,201);qt=(2*n+230,2*n+229)
 B={tuple(q)for q in R['canonical_source']}|{(qm[0]+2*a,qm[1]+2*a)for a in[0,1,6,8]}|{(qt[0]+2*a,qt[1]+2*a)for a in[0,1,3,5,6]}
 assert len(B)==22
 original=sorted(B);p=(0,0);h=1;end=80270+208*n;start=32433+104*n;M=Counter([p]);MD=Counter();headbox=[0,0,0,0];records=0;ds=None
 for t in range(end):
  if t==start:ds=p;MD[p]+=1
  old=p in B;B.symmetric_difference_update({p});h=(h+(-1 if old else 1))%4;p=(p[0]+DIR[h][0],p[1]+DIR[h][1]);M[p]+=1
  if t>=start:MD[p]+=1
  before=tuple(headbox);headbox=[min(headbox[0],p[0]),max(headbox[1],p[0]),min(headbox[2],p[1]),max(headbox[3],p[1])];records+=tuple(headbox)!=before
 c=next(c for c in J['controls']if c['n']==n)
 assert B=={tuple(q)for q,i in c['whole_end_black']}and[p,h]==[tuple(c['pose_end'][0]),c['pose_end'][1]]
 verify(M,(0,0),p,headbox);b=exact_bound(M,(0,0),p,headbox)
 dbox=[min(x for x,y in MD),max(x for x,y in MD),min(y for x,y in MD),max(y for x,y in MD)]
 verify(MD,ds,p,dbox);db=exact_bound(MD,ds,p,dbox)
 W=headbox[1]-headbox[0]+1;H=headbox[3]-headbox[2]+1;assert W+H==records+2
 assert end+1<=(((records+2)**2//4+3)*(4**(records+1)-1))//3
 controls.append(dict(n=n,seed=original,updates=end,head_box=headbox,head_records=records,whole_field_sha256=hashlib.sha256(json.dumps(sorted(B)).encode()).hexdigest(),max_site_head_cuts=max(M.values()),exact_whole_bound_decimal=str(b),drought_start=start,drought_duration=end-start,drought_head_box=dbox,exact_drought_bound_decimal=str(db),local_counter_sha256=hashlib.sha256(json.dumps(sorted(M.items())).encode()).hexdigest()))
 print('MT',n,'reads',end,'records',records,'max count',max(M.values()),flush=True)
files=['DROUGHT_BOUNDARY_PINNING_MANIFEST.json','DROUGHT_BOUNDARY_ORIENTATION_ADDENDUM.json','../audits/check_drought_boundary_pinning_independent.json','RECURSIVE_PHASE13_PACKET_MANIFEST.json','SOUTHWEST_ARCHIVE_IMPORT_MANIFEST.json','../audits/check_southwest_archive_import_independent.json','MT_COMPLETED_DROUGHT_INVENTORY_MANIFEST.json','../audits/check_MT_completed_drought_inventory_independent.json','../first_principles_new/recurrent_boundary_current.md']
for f in files:assert(P/f).exists(),f
out=dict(status='AUTHOR exact directed visit-flow hierarchy; independent audit pending',small_exhaustions=small,full_controls=controls,dependencies={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in files},scope='Universal finite-interval perimeter-exponential confinement and logarithmic head-record lower bound; no pristine fast-clock occurrence or capture claim')
(P/'RECTANGLE_VISIT_FLOW_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
