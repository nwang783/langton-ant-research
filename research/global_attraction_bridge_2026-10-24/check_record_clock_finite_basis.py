"""Finite clopen-basis decision and exact outward-period certificate regressions.
The unbounded total F(H) search is proved, NOT launched here.
"""
from pathlib import Path
from itertools import product
import hashlib,json
from check_return_permanent_output_debt import DXY
P=Path(__file__).parent

def geom(p,h,w):
 Q=[]
 for c in w:
  Q.append(p);h=(h+(1 if c=='R'else-1))%4;p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
 return Q,p,h

def certificate(B,p,h,prefix,w,a,M):
 assert w and all(c in'RL'for c in prefix+w)
 dot=lambda q:q[0]*a[0]+q[1]*a[1]
 assert all(dot(q)<=M for q in B)
 C=set(B);Preads=[]
 for c in prefix:
  Preads.append(p);assert(p in C)==(c=='L');C.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
 Q,end,eh=geom(p,h,w);d=(end[0]-p[0],end[1]-p[1]);assert eh==h and d!=(0,0) and dot(d)>0
 axis=0 if d[0] else 1
 def multiple(v):
  if v[axis]%d[axis]:return None
  k=v[axis]//d[axis]
  return k if v==(k*d[0],k*d[1])else None
 tests=0
 for i,q in enumerate(Q):
  flips=[];hits=[];critical={0}
  for j,z in enumerate(Q):
   m=multiple((z[0]-q[0],z[1]-q[1]))
   if m is not None and(m>0 or(m==0 and j<i)):flips.append(m);critical.add(m)
  for z in C:
   k=multiple((z[0]-q[0],z[1]-q[1]))
   if k is not None and k>=0:hits.append(k);critical|={k,k+1}
  for k in critical:
   assert(sum(m<=k for m in flips)+sum(j==k for j in hits))%2==(w[i]=='L');tests+=1
 F={q for q in Preads if dot(q)<=M}
 for q in Q:
  last=(M-dot(q))//dot(d)
  for k in range(max(0,last+1)):F.add((q[0]+k*d[0],q[1]+k*d[1]))
 return dict(period=len(w),drift=d,side=a,offset=M,guard=[[q,int(q in B)]for q in sorted(F)],parity_tests=tests)

def finite_cover(H,T,guards):
 # Domain: head0,N; N bound0; E,S,W in N union infinity; all y>=0 WHITE.
 # Each guard is a clopen cylinder with finite side equalities and cell colors.
 cap=max([T]+[m for g in guards for a,m in g['bounds'].items()]+[abs(c)for g in guards for q,b in g['bits']for c in q]);bound_trials=0;trajectory_leaves=0;outside=None
 norms=lambda p:(p[1],p[0],-p[1],-p[0])
 def forced(q,bounds):return q[1]>=0 or any(v>m for v,m in zip(norms(q),bounds)if m is not None)
 def avoid(gs,assign,bounds):
  left=[]
  for g in gs:
   if any(bounds[int(a)]!=m for a,m in g['bounds'].items()):continue
   rem=[];bad=False
   for q,b in g['bits']:
    q=tuple(q);v=0 if forced(q,bounds)else assign.get(q)
    if v is not None and v!=b:bad=True;break
    if v is None:rem.append((q,b))
   if bad:continue
   if not rem:return None
   left.append(dict(bounds={},bits=rem))
  if not left:return assign
  q=left[0]['bits'][0][0]
  for b in(0,1):
   out=avoid(left,dict(assign,**{})|{q:b},bounds)
   if out is not None:return out
  return None
 for e,s,w in product(list(range(cap+1))+[None],repeat=3):
  bounds=(0,e,s,w);bound_trials+=1
  def dfs(t,p,h,ext,last,assign,odd):
   nonlocal trajectory_leaves
   v=norms(p);new=list(ext);event=False
   if t:
    for a in range(4):
     if new[a] is not None and v[a]>new[a]:assert v[a]==new[a]+1;new[a]=v[a];event=True
    if event:last=t
    if t-last>=H:return None
   if t==T:
    trajectory_leaves+=1;z=avoid(guards,assign,bounds)
    return None if z is None else dict(bounds=bounds,initial_black=sorted(q for q,b in z.items()if b),head=p,heading=h)
   v0=0 if forced(p,bounds)else assign.get(p)
   for b in(0,1)if v0 is None else(v0,):
    aa=assign|{p:b};color=b^(p in odd);hh=(h+(-1 if color else 1))%4;qq=(p[0]+DXY[hh][0],p[1]+DXY[hh][1]);out=dfs(t+1,qq,hh,new,last,aa,odd^{p})
    if out is not None:return out
   return None
  out=dfs(0,(0,0),0,bounds,0,{},set())
  if out is not None:return dict(covered=False,witness=out,bound_trials=bound_trials,trajectory_leaves=trajectory_leaves,offset_cutoff=cap)
 return dict(covered=True,bound_trials=bound_trials,trajectory_leaves=trajectory_leaves,offset_cutoff=cap)

j=json.loads((P/'OUTWARD_RECORD_GUARDS_CHECKED.json').read_text());positive=[]
for r in j['normal_catalog'][0]['records']:
 # Rotate E to N; the whole upper half-plane is WHITE.
 rotate=lambda q:(-q[1],q[0]);B={rotate(q)for q in r['required_black']};c=certificate(B,(0,0),0,'',r['cycle_word'],(0,1),0)
 assert c['drift']==(2,2) and B<=set(tuple(q)for q,b in c['guard'])
 # Generalized hull has only the north side finite, so these are true N records.
 Q,_,_=geom((0,0),0,r['cycle_word']*6);maxy=0;last=0;gaps=[]
 for t,q in enumerate(Q):
  if q[1]>maxy:gaps.append(t-last);last=t;maxy=q[1]
 assert max(gaps)<=104
 c.update(source_phase=r['phase'],six_period_record_gaps=gaps);positive.append(c)
empty=finite_cover(1,3,[]);assert empty['covered'] and empty['trajectory_leaves']==0
nonempty=finite_cover(1,2,[]);assert not nonempty['covered']
# Test the generic finite Boolean cover step, not a claimed capture certificate.
covered=finite_cover(1,2,[dict(bounds={1:0,2:0},bits=[])]);assert covered['covered']
# Altering a required initial black in a true periodic certificate must reject.
negative=[]
for c,r in zip(positive,j['normal_catalog'][0]['records']):
 B={(-q[1],q[0])for q in r['required_black']};q=min(B)
 rejected=False
 try:certificate(B-{q},(0,0),0,'',r['cycle_word'],(0,1),0)
 except AssertionError:rejected=True
 assert rejected;negative.append(dict(source_phase=r['phase'],removed=q,rejected=True))
files=['JOINT_RECORD_DROUGHT_MANIFEST.json','../audits/check_joint_record_drought_independent.json','OUTWARD_RECORD_GUARDS_MANIFEST.json','../audits/check_fresh_and_outward_record_guards_independent.json']
for f in files:assert(P/f).exists(),f
out=dict(status='AUTHOR finite basis and outward-certificate regressions; uniform theorem is analytic; audit pending',source_hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in files},H1_F3_vacuous_test=empty,H1_T2_nonempty=nonempty,generic_Boolean_cover_test=covered,outward_periodic_certificates=positive,mutated_certificate_rejections=negative,unbounded_cover_search='NOT EXECUTED; totality proved in accompanying theorem, no numerical F(H) for H>=2')
(P/'RECORD_CLOCK_FINITE_BASIS_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n');print('F(1)=3 vacuous; positive H104 certificates',len(positive),'finite cover tests complete')
