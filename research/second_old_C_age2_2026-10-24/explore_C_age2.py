from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from itertools import permutations
import importlib.util,json
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('lit',R/'word_stabilization/check_foreign_return_interfaces.py');l=importlib.util.module_from_spec(sp);sp.loader.exec_module(l)
sp=importlib.util.spec_from_file_location('own',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');o=importlib.util.module_from_spec(sp);sp.loader.exec_module(o);W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def raw(t):return ''.join(W[a] for a in t)
def after(w,p=(0,0,0)):
 x,y,h=p
 for c in w:
  h=(h+(1 if c=='R'else-1))%4;dx,dy=l.DIRS[h];x+=dx;y+=dy
 return x,y,h

def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(a,p):return z(p),z(after(W[a],p))
def hit(a,b,c,d):
 u,v,zz=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if den:
  s,t=Q(det(zz,v),den),Q(det(zz,u),den)
  return(s,t)if 0<=s<=1 and 0<=t<=1 else None
 if det(zz,u):return None
 k=0 if u[0] else 1
 lo,hi=sorted((Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k])))
 return ('collinear',max(0,lo),min(1,hi))if max(0,lo)<=min(1,hi)else None

def perms(d,v,u):
 if not d+v+u:yield '';return
 if d:
  for q in perms(d-1,v,u):yield'D'+q
 if v:
  for q in perms(d,v-1,u):yield'V'+q
 if u:
  for q in perms(d,v,u-1):yield'U'+q

a,b=chord('C',(0,0,0));u=sub(b,a);geos=[];boxes=[];types=[];counts=[];words={};maxsize=0
for b1 in'DCVU':
 N=2+int(b1=='C');h=(2-N)%4
 for b2 in'DCVU':
  if b1=='C'and b2=='U':continue
  c,d=chord(b2,(0,0,h));v=sub(d,c);den=det(u,v)
  corners=[tuple(Q(a[k]+s*u[k]-c[k]-t*v[k],2)for k in(0,1))for s in(0,1)for t in(0,1)]
  bounds=[(min(q[k]for q in corners).__floor__(),max(q[k]for q in corners).__ceil__())for k in(0,1)]
  boxes.append((b1,b2,bounds))
  for x in range(bounds[0][0],bounds[0][1]+1):
   for y in range(bounds[1][0],bounds[1][1]+1):
    if(x+y-N)%2:continue
    zz=sub(add(c,(2*x,2*y)),a)
    if den:
     s,t=Q(det(zz,v),den),Q(det(zz,u),den)
     if not(0<=s<1 and 0<t<=1):continue
    else:
     if det(zz,u):continue
     k=0 if u[0] else 1
     q,mul=Q(zz[k],u[k]),Q(v[k],u[k]);assert mul>0
     if q>=0:continue
     s,t=Q(0),-q/mul
     if not(0<t<=1):continue
    p2=(x,y,h);geos.append((b1,b2,p2,s,t))
    for A in'FQB':
     dp=after(W[A]+W[b1],(0,0,2));pa=(x-dp[0],y-dp[1],2)
     if pa[0]>-1:continue
     # Actual signed foreign+b1 prefix must have no earlier source contact.
     pfx=after(W['F'],pa);end=after(W[A],pa);verts=[z(pa),z(pfx)]
     if A!='F':verts.append(z(end))
     if any(hit(a,b,c0,d0)for c0,d0 in zip(verts,verts[1:])):continue
     if hit(a,b,*chord(b1,end)):continue
     tr=l.trace(W[A]+W[b1]+W[b2]+l.M)
     if not tr['feasible']:continue
     types.append((A,b1,b2,pa,p2))
     L=-1-pa[0]
     for dw in range(L+1):
      for vw in range((L-dw)//3+1):
       for uw in range((L-dw-3*vw)//4+1):
        xres=L-dw-3*vw-4*uw
        for ds in range(xres+1):
         vs=xres-ds
         yres=1+dw+vw-ds-3*vs-pa[1]
         if yres<0 or yres%4:continue
         us=yres//4
         if ds+vs+us==0:continue
         counts.append((A,b1,b2,pa,dw,vw,uw,ds,vs,us));maxsize=max(maxsize,dw+vw+uw+ds+vs+us)
         for X in perms(dw,vw,uw):
          for Y in perms(ds,vs,us):
           if Y[-1]not in('VU'if A in'FQ'else'U'):continue
           T='C'+X+'C'+Y+A+b1+b2
           assert after(raw(T[:-3]))==pa
           if T in words:continue
           old=l.trace(raw(T[:-3]));tr=l.trace(raw(T)+l.M)
           cls='positive'if tr['feasible']else('old_conflict'if not old['feasible']else'whole_conflict')
           words[T]=dict(classification=cls,trace=tr,X=X,Y=Y,foreign_pose=pa,second_pose=p2)
print('boxes',len(boxes),'geos',len(geos),'local/sourceclear types',len(types),'count tuples',len(counts),'max rail atoms',maxsize)
print('words',len(words),Counter(q['classification']for q in words.values()))
positives=[T for T,q in words.items() if q['classification']=='positive']
print('positive full creator-prefix types', Counter(P for T in positives for P in ('D','V','U','VC','UC') if l.trace(raw(P+T)+l.M)['feasible']))
for T in positives:
 for P in ('D','V','U','VC','UC'):
  if l.trace(raw(P+T)+l.M)['feasible']:print('FULL_POSITIVE',P,T)
# Only compact first-turn traces are exported here; complete actual boards follow separately.
for q in words.values():
 if q['trace']['feasible']:
  q['trace']={'feasible':True,'pose':q['trace']['pose']}
(H/'exploration.json').write_text(json.dumps(dict(boxes=boxes,geos=[(b1,b2,p2,[s.numerator,s.denominator],[t.numerator,t.denominator])for b1,b2,p2,s,t in geos],types=types,counts=counts,words=words),indent=2)+'\n')
