"""Sound finite-patch test of one surviving C-output transfer.
Source DC at origin,N, target D at (2,2),N consumes q=(2,3).
The target must have actual M11 right context. Intermediate packets cannot read q.
Any witness is abstract only; an exhausted no-hit closure would be a certificate.
"""
import json,sys,collections
from pathlib import Path
R=int(sys.argv[1]);CAP=int(sys.argv[2]);q=2+3j;source=1;target=0;sp=0j;sh=0;tp=2+2j;th=0
M=json.load(open('seven_sub_dcv_port_quotient.json'))['macro_words'];F={tuple(map(int,l.split()[:5]))for l in open('seven_sub_dcv_star4_kernel.tsv')};D=(1j,1,-1j,-1)
def tr(w):
 p=0j;h=0;first={};last={};odd=set()
 for c in w:
  first.setdefault(p,c=='L');assert last.get(p)!=c;last[p]=c;odd.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=D[h]
 return p,h,first,odd
G=[]
for a in M:
 e,h,_,odd=tr(a['word']);req=tr(a['word']+a['end_marker'])[2];G.append((e,h,req,odd))
P=[complex(x,y)for x in range(2-R,3+R)for y in range(3-R,4+R)];ix={p:i for i,p in enumerate(P)}
heads=set()
for a,(e,dh,req,odd)in enumerate(G):
 for h in range(4):
  z=(-1j)**h
  for c in req:
   for p in P:
    v=p-z*c
    if (int(v.real+v.imag)+h)%2==0:heads.add((v,h))
heads=sorted(heads,key=lambda z:(z[0].real,z[0].imag,z[1]));si={v:i for i,v in enumerate(heads)};OUT=len(heads);T={};reentry=set()
def fk(a,b,p,h):return (a,b,int(p.real),int(p.imag),h)in F
for sid,(p,h)in enumerate(heads):
 z=(-1j)**h
 for a,(e,dh,req,odd)in enumerate(G):
  dest=(p+z*e,(h+dh)%4);to=si.get(dest,OUT);known=val=flip=0
  for c,v in req.items():
   j=ix.get(p+z*c)
   if j is not None:known|=1<<j;val|=int(v)<<j
  for c in odd:
   j=ix.get(p+z*c)
   if j is not None:flip^=1<<j
  isgoal=(a==target and p==tp and h==th)
  qq=(q-p)/z
  allowed=qq not in req and not fk(source,a,p,h) and not fk(a,target,(tp-p)/z,(-h)%4)
  T[sid,a]=(to,known,val,flip,allowed,isgoal)
  # Incoming predecessor of this head under a.
  hh=(h-dh)%4;pp=p-(-1j)**hh*e
  if (pp,hh)not in si:reentry.add(sid)
e,dh,req,odd=G[source];known=val=0
for c,v in req.items():
 j=ix.get(c)
 if j is not None:known|=1<<j;val|=int(v^(c in odd))<<j
start=(si.get((e,dh),OUT),known,val);Q=collections.deque([start]);prev={start:None};goal=None
while Q:
 st=Q.popleft();sid,k,v=st
 if len(prev)>CAP:break
 if sid==OUT:succ=[((j,k,v),'OUT')for j in reentry]
 else:
  succ=[]
  for a in range(len(G)):
   to,kk,vv,ff,allowed,isgoal=T[sid,a]
   if not(allowed or isgoal)or ((v^vv)&k&kk):continue
   nk=k|kk;nv=((v&k)|(vv&~k))^ff
   if isgoal:goal=(st,a);break
   succ.append(((to,nk,nv),a))
 if goal:break
 for ns,label in succ:
  if ns not in prev:prev[ns]=(st,label);Q.append(ns)
out={'radius':R,'heads':len(heads),'states':len(prev),'pending':len(Q),'goal':bool(goal),'status':'abstract_witness'if goal else'cap'if Q else'exhausted_no_hit'}
if goal:
 st,a=goal;path=[(st,a)]
 while prev[st]is not None:
  old,b=prev[st];path.append((old,b));st=old
 path.reverse();out['witness']=[{'pose':None if s[0]==OUT else[int(heads[s[0]][0].real),int(heads[s[0]][0].imag),heads[s[0]][1]],'macro':b if b=='OUT'else M[b]['name']}for s,b in path]
Path('dcv_surviving_upper_r%d.json'%R).write_text(json.dumps(out,indent=2));print(json.dumps(out))
