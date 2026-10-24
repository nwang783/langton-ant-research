from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json,importlib.util
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
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

angles=[r for r in J['all831_conditional_preFOREIGN_old_source_angle_interfaces']if r['old_source']=='C'];rows=[];geos=[];boxes=[]
a,b=chord('C',(0,0,0));u=sub(b,a)
for ai,angle in enumerate(angles):
 n=angle['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age'];N=angle['total_ordinary_C_before_third'];b1,b2,b3=(angle[k]for k in['first','second','third']);hh=angle['third_heading_relative_old'];c,d=chord(b3,(0,0,hh));v=sub(d,c);den=det(u,v)
 corners=[tuple(Q(a[k]+ss*u[k]-c[k]-tt*v[k],2)for k in(0,1))for ss in(0,1)for tt in(0,1)];bounds=[(min(p[k]for p in corners).__floor__(),max(p[k]for p in corners).__ceil__())for k in(0,1)];boxes.append((ai,bounds))
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
    tr=l.trace(raw(A+b1+b2+b3)+l.M)
    early=any(hit(a,b,c0,d0)for c0,d0 in zip(verts,verts[1:]));base='earlier_contact'if early else('local_immutable'if not tr['feasible']else'live')
    for role in C['all7_genuine_C_roles_and18_same_identity_source_reserves']:
     why=base;cuts=[];tau=role['actual_full_ENTRY_clock'];complete=role['actual_full_completion_clock']
     if n<complete:why='source_uncompleted'
     elif why=='live':
      for f in role['selected_reserves']:
       g=tuple(f['normalized_selected_C_cell']);q=l.rot(sub(g,pa[:2]),-pa[2]);fr=tr['first'].get(q)
       if q in l.K or(fr and fr[0]=='R'):cuts.append(g)
      why='signed_current_cut'if cuts else'NECESSARY'
     rows.append(dict(role=(role['actual_full'],role['selected_C_index1']),n=n,b1=b1,b2=b2,b3=b3,A=A,pa=pa,p3=p3,why=why,cuts=cuts))
print('angles',len(angles),'poses',len(geos),'typedroles',len(rows));print(Counter(r['why']for r in rows));print('Remaining',Counter((r['role'],r['n'])for r in rows if r['why']=='NECESSARY'));print('unique rem physical',len(set((r['n'],r['b1'],r['b2'],r['b3'],r['A'],r['pa'],r['p3'])for r in rows if r['why']=='NECESSARY')))
(H/'exploration.json').write_text(json.dumps(dict(rows=rows),indent=2)+'\n')
