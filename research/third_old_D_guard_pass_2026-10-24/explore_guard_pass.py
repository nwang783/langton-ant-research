from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json,importlib.util
R=Path('/workspace/shared/langton');H=Path('/workspace/shared/langton/third_old_D_guard_pass_2026-10-24')
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
    for sourcecase in ['DC']+list(('D','DC','V','VC','VCC','U','UC','UCC')):
     # First value uses actual sourceDC; other values use sourceD's actual NEXT full producer.
     pass
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
      else:facts.update([(1,1),(1,2),(2,1),(2,2),(3,1),(3,2),(2,4)])
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
print('angles',len(angles),'poses',len(geos),'typedrows',len(rows),Counter(r['why']for r in rows));print('REMAIN',Counter((r['source'],r['nextfull'],r['n'])for r in rows if r['why']=='NECESSARY'));print('unique physical',len(set((r['n'],r['b1'],r['b2'],r['b3'],r['A'],r['pa'],r['p3'])for r in rows if r['why']=='NECESSARY')))
(H/'exploration.json').write_text(json.dumps(dict(rows=rows),indent=2)+'\n')
