from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json,importlib.util
R=Path('/workspace/shared/langton');H=Path('/workspace/shared/langton/old_D_third_young_endpoint_2026-10-24')
s=importlib.util.spec_from_file_location('l',R/'word_stabilization/check_foreign_return_interfaces.py');l=importlib.util.module_from_spec(s);s.loader.exec_module(l);s=importlib.util.spec_from_file_location('o',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');o=importlib.util.module_from_spec(s);s.loader.exec_module(o);W=o.WORDS
J=json.load(open(R/'third_ordinary_local_interface_2026-10-24/third_local_interface.json'))
C=json.load(open(R/'second_old_C_age3_2026-10-24/C_age3_source_reserve.json'))

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for t in w:h=(h+(1 if t=='R'else-1))%4;q=add(q,l.DIRS[h])
 return *q,h

def raw(t):return ''.join(W[a]for a in t)
def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(a,p):return z(p),z(after(W[a],p))
def hit(a,b,c,d):
 u,v,zz=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if den:
  s,t=Q(det(zz,v),den),Q(det(zz,u),den)
  return(s,t)if 0<=s<=1 and 0<=t<=1 else None
 if det(zz,u):return None
 k=0 if u[0] else 1;lo,hi=sorted((Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k])))
 return('parallel',max(0,lo),min(1,hi))if max(0,lo)<=min(1,hi)else None

angles=[r for r in J['all831_conditional_preFOREIGN_old_source_angle_interfaces']if r['old_source']=='D'];rows=[];geos=[]
a,b=chord('D',(0,0,0));u=sub(b,a)
for ai,angle in enumerate(angles):
 n=angle['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age'];N=angle['total_ordinary_C_before_third'];b1,b2,b3=(angle[k]for k in['first','second','third']);hh=angle['third_heading_relative_old'];c,d=chord(b3,(0,0,hh));v=sub(d,c);den=det(u,v)
 corners=[tuple(Q(a[k]+ss*u[k]-c[k]-tt*v[k],2)for k in(0,1))for ss in(0,1)for tt in(0,1)];bounds=[(min(p[k]for p in corners).__floor__(),max(p[k]for p in corners).__ceil__())for k in(0,1)]
 for x in range(bounds[0][0],bounds[0][1]+1):
  for y in range(bounds[1][0],bounds[1][1]+1):
   if(x+y-N)%2:continue
   zz=sub(add(c,(2*x,2*y)),a)
   if den:
    ss,tt=Q(det(zz,v),den),Q(det(zz,u),den)
    if not(0<=ss<1 and 0<tt<=1):continue
   else:
    if det(zz,u):continue
    k=0 if u[0] else 1;q,mul=Q(zz[k],u[k]),Q(v[k],u[k]);assert mul>0
    if q>=0:continue
    ss,tt=Q(0),-q/mul
    if not(0<tt<=1):continue
   p3=(x,y,hh);geos.append((ai,p3,ss,tt))
   for A in'FQB':
    ha=angle['true_FOREIGN_heading_relative_old'];delta=after(raw(A+b1+b2),(0,0,ha));pa=(x-delta[0],y-delta[1],ha);fcut=after(W['F'],pa);ep=after(W[A],pa);verts=[z(pa),z(fcut)]
    if A!='F':verts.append(z(ep))
    for bb in[b1,b2]:ep=after(W[bb],ep);verts.append(z(ep))
    assert ep==p3
    T=A+b1+b2+b3;tr=l.trace(raw(T)+l.M);early=any(hit(a,b,c0,d0)for c0,d0 in zip(verts,verts[1:]));base='earlier_contact'if early else('local_immutable'if not tr['feasible']else'live')
    cases=[('DC',None)]+[('D',nextfull)for nextfull in('D','DC','V','VC','VCC','U','UC','UCC')]
    for full,nextfull in cases:
     facts={(2,0)};why=base;cuts=[]
     if n<=2:facts.add((1,-1))
     if full=='DC':
      if n<1:why='full_source_uncompleted'
      facts.update([(2,3),(3,1),(3,2)])
     else:
      if nextfull.count('C')>n:why='actual_next_full_uncompleted'
      if nextfull[0]=='D':facts.add((3,1))
      elif nextfull[0]=='V':facts.update([(1,1),(2,1),(3,2)])
      else:facts.update([(1,1),(1,2),(2,1),(2,2)])
     if why=='live':
      if full=='D'and nextfull[0]=='U':
       Actx=l.trace(W[A]+l.M)['first']
       if any(l.rot(sub(g,pa[:2]),-pa[2]) in Actx for g in[(1,1),(1,2),(2,1),(2,2)]):why='young_nextU_FOREIGN_star_effect'
      if why=='live':
       for g in facts:
        local=l.rot(sub(g,pa[:2]),-pa[2]);fr=tr['first'].get(local)
        if local in l.K or(fr and fr[0]=='R'):cuts.append(g)
       why='CURRENT_cut'if cuts else'NECESSARY'
     rows.append(dict(source=full,nextfull=nextfull,n=n,b1=b1,b2=b2,b3=b3,A=A,pa=pa,p3=p3,why=why,cuts=cuts))

# Exact complete endpoint families for the remaining true ages zero and one.
def perms(d,v,u):
 if not d+v+u:yield '';return
 for a,n in [('D',d),('V',v),('U',u)]:
  if n:
   for t in perms(d-(a=='D'),v-(a=='V'),u-(a=='U')):yield a+t
physical={n:{}for n in (0,1)}
for r in rows:
 if r['why']=='NECESSARY'and r['n']in physical:
  k=(r['A'],tuple(r['pa']),r['b1'],r['b2'],r['b3'],tuple(r['p3']));physical[r['n']][k]=r
lookup={(r['n'],r['A'],tuple(r['pa']),r['b1'],r['b2'],r['b3'],r['source'],r['nextfull']):r['why']for r in rows}
def simulate(T):
 fine=raw(T)+l.M;tr=l.trace(fine);assert tr['feasible']
 seed={q for q,(a,t)in tr['first'].items()if a=='L'};black=set(seed);p=(0,0);h=0
 for tick,a in enumerate(fine):
  assert(p in black)==(a=='L'),(T,tick,p,a)
  if a=='L':black.remove(p)
  else:black.add(p)
  h=(h+(1 if a=='R'else-1))%4;p=add(p,l.DIRS[h])
 return dict(seed=sorted(seed),seed_mass=len(seed),actual_reads=len(fine),actual_exit=(*p,h),exit_mass=len(black))
records={};count_records=[]
for n,pp in physical.items():
 for k,r in pp.items():
  x,y,h=r['pa'];tuples=[]
  if n==0:
   assert h==0
   X,Y=x-1,y-1
   for v in range(max(0,X+1)):
    d=X-v;z=Y-d-3*v
    if z>=0 and not z%4 and d+v+z//4:tuples.append((0,0,0,d,v,z//4))
  else:
   assert h==3;Y=y-2
   for dn in range(max(0,Y+1)):
    for vn in range((Y-dn)//3+1):
     for un in range((Y-dn-3*vn)//4+1):
      ww=Y-dn-3*vn-4*un
      for dw in range(ww+1):
       vw=ww-dw;z=1+dn+vn-dw-3*vw-x
       if z>=0 and not z%4 and dw+vw+z//4:tuples.append((dn,vn,un,dw,vw,z//4))
  for dn,vn,un,dw,vw,uw in tuples:
   count_records.append(dict(n=n,foreign=r['A'],foreign_pose=r['pa'],returns=[r['b1'],r['b2'],r['b3']],counts=[dn,vn,un,dw,vw,uw]))
   if n==0:
    railpairs=(('',Y)for Y in perms(dw,vw,uw))
   else:railpairs=((X,Y)for X in perms(dn,vn,un)for Y in perms(dw,vw,uw))
   for X,Y in railpairs:
    if Y[-1]not in('VU'if r['A']in'FQ'else'U'):continue
    if n==0:source,nextfull='D',Y[0]
    elif not X:source,nextfull='DC',None
    else:source,nextfull='D',X[0]+('C'if len(X)==1 else'')
    assert lookup[(n,r['A'],tuple(r['pa']),r['b1'],r['b2'],r['b3'],source,nextfull)]=='NECESSARY'
    T='D'+X+('C'if n else'')+Y+r['A']+r['b1']+r['b2']+r['b3']
    if T in records:continue
    assert after(raw('D'+X+('C'if n else'')+Y))==tuple(r['pa'])
    tr=l.trace(raw(T)+l.M)
    rec=dict(n=n,source=source,nextfull=nextfull,foreign=r['A'],foreign_pose=r['pa'],returns=[r['b1'],r['b2'],r['b3']],X=X,Y=Y,feasible=tr['feasible'])
    if tr['feasible']:rec['physical_control']=simulate(T)
    else:rec['immutable_conflict']=tr
    records[T]=rec
def actual_owner(T,tick):
 offset=0
 for j,a in enumerate(T):
  if tick<offset+len(W[a]):return dict(kind='actual_RAW',atom=a,atom_index0=j,owner_tick0=tick-offset,owner_read1=tick-offset+1)
  offset+=len(W[a])
 return dict(kind='actual_following_word_M11_prefix',owner_tick0=tick-offset,owner_read1=tick-offset+1)
for T,rec in records.items():
 if not rec['feasible']:
  f=rec['immutable_conflict'];rec['first_failure_owner']=actual_owner(T,f['conflict_read']);rec['previous_request_owner']=actual_owner(T,f['previous_read'])
positive=[T for T,r in records.items()if r['feasible']];reverse=[];seen=set(positive);todo=list(positive)
while todo:
 T=todo.pop()
 for P in('D','DC','V','VC','VCC','U','UC','UCC'):
  tr=l.trace(raw(P+T)+l.M);ok=tr['feasible']
  reverse.append(dict(target=T,predecessor=P,feasible=ok,physical_control=simulate(P+T)if ok else None,immutable_conflict=tr if not ok else None))
  if ok and P+T not in seen:seen.add(P+T);todo.append(P+T)
for r in reverse:
 if not r['feasible']:
  T=r['predecessor']+r['target'];f=r['immutable_conflict'];r['first_failure_owner']=actual_owner(T,f['conflict_read']);r['previous_request_owner']=actual_owner(T,f['previous_read'])
assert len(records)==3757 and Counter(r['n']for r in records.values())=={0:684,1:3073}
assert Counter(r['n']for r in records.values()if r['feasible'])=={0:2,1:324}
assert len(seen)==652 and len(reverse)==5216
assert all(r['predecessor']=='D'for r in reverse if r['feasible'])
assert len([r for r in reverse if r['feasible']])==326
assert not any(r['why']=='NECESSARY'and r['n']==2 for r in rows)
result=dict(scope='Outgoing old-D FIRST THIRD contact; true preFIRSTforeign ages0,1,2 only; actual U-entry G8 prefix and actual terminalM11. Prepared positives have no eligible U-entry before selectedD, although later internalU entries exist.',angles=len(angles),outgoing_heads=len(geos),typed_rows=rows,initial_partition=dict(Counter(r['why']for r in rows)),endpoint_count_records=count_records,whole_words=records,complete_reverse_relation=reverse,reverse_closed_nodes=sorted(seen),final='young old-D ages0/1/2 excluded as eligible outgoing sources of global first THIRD contact')
(H/'D_third_young_endpoint.json').write_text(json.dumps(result,indent=2)+'\n')
print(dict(angles=len(angles),heads=len(geos),typed=len(rows),initial_partition=result['initial_partition'],count_tuples=len(count_records),words=len(records),positive=len(positive),reverse_nodes=len(seen),reverse_queries=len(reverse),final=result['final']))
