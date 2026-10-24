"""Fixed 17-place geometric trap limitation for three surviving U cohorts.

Pure finite diagnostic: no actual word search or extended spatial box.
The absence of an initial marked trap is UNKNOWN, not a reachability result.
"""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent
G=json.load(open(R/'chronology_dcuv/literal_residual_geometry.json'))['geometry'];IDS=(0,1,4,5,6,7,8,9)
F={(-1,1),(-1,2),(-1,4),(0,2),(0,3)}
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def rot(p,h):
 x,y=p;return ((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def contact(x,y):
 p,q=x;z,w=y;d=sub(q,p);e=sub(w,z);r=sub(z,p);D=det(d,e)
 if D:
  s,t=det(r,e),det(r,d)
  if D<0:D,s,t=-D,-s,-t
  return 0<=s<=D and 0<=t<=D
 return det(r,d)==0 and all(max(min(p[k],q[k]),min(z[k],w[k]))<=min(max(p[k],q[k]),max(z[k],w[k]))for k in (0,1))
def record(a,p,h):
 ar=[];pp=p;hh=h;base=0 if a in(0,1)else 4 if a in(4,5,6)else 7
 for at in [base]+['C']*G[a]['name'].count('C'):
  s=add((2*pp[0],2*pp[1]),rot((-1,-1),hh));v=(0,1)if at=='C'else G[at]['endpoint'][:2]
  pp=add(pp,rot(v,hh));hh=(hh-(at=='C'))%4;ar.append((s,add((2*pp[0],2*pp[1]),rot((-1,-1),hh))))
 return dict(packet=a,name=G[a]['name'],pose=(*p,h),arcs=ar,exit=(*pp,hh),outputs={add(p,rot(z,h))for z in G[a]['outputs']},context={add(p,rot(z[:2],h))for z in G[a]['requirements']})
def compatible(A,B):
 for i,x in enumerate(A['arcs']):
  for j,y in enumerate(B['arcs']):
   if not contact(x,y):continue
   if not(i==len(A['arcs'])-1 and j==0 and A['exit']==B['pose']and x[1]==y[0]):return False
   if det(sub(x[1],x[0]),sub(y[1],y[0]))==0 and not all(max(min(x[0][k],x[1][k]),min(y[0][k],y[1][k]))==min(max(x[0][k],x[1][k]),max(y[0][k],y[1][k]))==x[1][k]for k in(0,1)):return False
 return True
goal=record(7,(0,0),0);domain=goal['context']-F;assert len(domain)==17
results=[]
for a in(7,8,9):
 A=record(a,(-1,1),0);P=A['outputs']&F;assert P=={(-1,1),(-1,2),(0,2),(0,3)}
 consumers={}
 for w in domain:
  L=[]
  for b in IDS:
   for inp in G[b]['inputs']:
    for h in range(4):
     p=sub(w,rot(inp,h))
     if(sum(p)+h)%2:continue
     B=record(b,p,h)
     if B['context']&P or not compatible(A,B)or not compatible(B,goal):continue
     L.append(B)
  consumers[w]=L
 T=set(domain);rounds=[];witnesses=[]
 while True:
  bad={w:next((B for B in consumers[w]if not(B['outputs']&T)),None)for w in T};bad={w:B for w,B in bad.items()if B is not None}
  rounds.append(sorted(T))
  if not bad:break
  for w,B in sorted(bad.items()):witnesses.append(dict(cell=w,round=len(rounds)-1,consumer_packet=B['packet'],consumer_pose=B['pose'],outputs=sorted(B['outputs'])))
  T-=set(bad)
 assert list(map(len,rounds))==[17,5,2]and T=={(-1,3),(0,0)}and not(A['outputs']&T)
 results.append(dict(source=a,source_name=G[a]['name'],source_pose=A['pose'],protected_source_cohort=sorted(P),mandatory_spares=sorted(A['outputs']&domain),allowed_consuming_alignments=sum(map(len,consumers.values())),trap_rounds=rounds,final_trap=sorted(T),source_output_trap_intersection=sorted(A['outputs']&T),deletion_witnesses=witnesses))
O=dict(status='UNKNOWN_THREE_COHORT_GEOMETRIC_TRAP_ANSATZ_DOES_NOT_EXCLUDE',scope='Only the fixed 17-place goal-absence trap, protected source four and source/goal own-chord avoidance. Adjacent matching full-pose endpoints are exempt. No global word, age assignment, reachability or no-trap theorem.',cases=results,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in(R/'chronology_dcuv/literal_residual_geometry.json',Path(__file__).resolve())})
(R/'chronology_dcuv/U_three_cohort_geometric_traps_diagnostic.json').write_text(json.dumps(O,indent=2)+'\n')
print(json.dumps([{'source':r['source_name'],'allowed':r['allowed_consuming_alignments'],'trap_rounds':list(map(len,r['trap_rounds'])),'initial_trap_intersection':r['source_output_trap_intersection']}for r in results]))
