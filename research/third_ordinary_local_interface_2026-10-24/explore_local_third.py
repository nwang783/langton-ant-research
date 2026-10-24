from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import importlib.util,json
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('l',R/'word_stabilization/check_foreign_return_interfaces.py');l=importlib.util.module_from_spec(s);s.loader.exec_module(l);s=importlib.util.spec_from_file_location('o',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');o=importlib.util.module_from_spec(s);s.loader.exec_module(o);W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def raw(t):return ''.join(W[a]for a in t)
def after(word,pose=(0,0,0)):
 p,h=pose[:2],pose[2]
 for c in word:h=(h+(1 if c=='R'else-1))%4;p=add(p,l.DIRS[h])
 return *p,h

def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def hit(a,b,c,d):
 u,v,zz=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if den:
  s,t=Q(det(zz,v),den),Q(det(zz,u),den)
  return dict(old_s=s,new_t=t,kind='point')if 0<=s<=1 and 0<=t<=1 else None
 if det(zz,u):return None
 k=0 if v[0]else 1
 lo,hi=sorted((Q(a[k]-c[k],v[k]),Q(b[k]-c[k],v[k])))
 lo,hi=max(0,lo),min(1,hi)
 if lo>hi:return None
 pt=tuple(Q(c[k])+lo*v[k]for k in(0,1));j=0 if u[0]else 1;s=Q(pt[j]-a[j],u[j])
 return dict(old_s=s,new_t=Q(lo),new_t_upper=Q(hi),kind='collinear')

rows=[];contacts=[];positive=[]
for A in'FQB':
 for b1 in'DCVU':
  for b2 in'DCVU':
   for b3 in'DCVU':
    T=A+b1+b2+b3;fcut=after(W['F']);end=after(W[A]);verts=[z((0,0,0)),z(fcut)];labels=['F56prefix']
    if A!='F':verts.append(z(end));labels.append(A+'tail')
    p=end
    for ix,b in enumerate([b1,b2,b3]):p=after(W[b],p);verts.append(z(p));labels.append('b'+str(ix+1)+':'+b)
    segs=list(zip(verts,verts[1:]));new=segs[-1];local=[]
    for i,old in enumerate(segs[:-1]):
     h=hit(*old,*new)
     if h and h['new_t']>0:local.append((h['new_t'],i,h))
    record=dict(tokens=T)
    if local:
     t,i,h=min(local,key=lambda x:x[0]);owner=i+1 if h['old_s']==1 else i
     assert owner<len(segs)-2 # b2 cannot be a nonadjacent old owner
     tr=l.trace(raw(T)+l.M);fpred={P:l.trace(raw(P+T)+l.M)['feasible'] for P in('VU'if A in'FQ'else'U')}
     record.update(first_local_owner=labels[owner],first_new_t=[t.numerator,t.denominator],literal_feasible=tr['feasible'],forced_last_old_base_predecessors=fpred)
     if not tr['feasible']:record['conflict']=tr
     contacts.append(record)
     if tr['feasible']:positive.append(record)
    rows.append(record)
print('all',len(rows),'contacts',len(contacts),Counter(q['first_local_owner']for q in contacts),'full positives',len(positive))
for q in contacts:print(q)
(H/'exploration.json').write_text(json.dumps(dict(rows=rows,contacts=contacts,positive=positive),indent=2)+'\n')
