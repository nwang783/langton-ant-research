"""Discovery of ONE specified mixed twelve-corner cylinder, not a period search.
Two flat RIGHTs in RR, two RLR3 macros and one intervening VV bridge.
Full d=(-6,0); all count-forced missing corner cells, complete WHITE cap4
histories, zero ports, physical ordinals, voltage and critical sides retained.
"""
from pathlib import Path
from itertools import product
from collections import Counter,defaultdict,deque
import json,time
base=Path(__file__).parent;lib={'__file__':str(base/'explore_two_flat_pair_reader_closure.py')};exec((base/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],lib)
H=lib['H'];V=lib['V'];out=lib['out'];rot=lib['rot'];cnt=lib['cnt'];fp=lib['fp'];edge=lib['edge'];dom=lib['dom']
W=6
def canon(p):return (p[0]%W,p[1])
def build(fs):
 turns='RRLRLRLLRLRL';p=(0,0);ci='N';nodes=[];flat=iter(fs)
 for i,t in enumerate(turns):
  if i in[0,1]:h=rot(next(flat),ci,'N');role='flat'
  elif i in[3,8]:h=rot('EWE',ci);role='source'
  elif i in[5,10]:h=rot('EEE',ci);role='sink'
  elif i in[4,9]:h=rot('WEEE',ci);role='cut3'
  else:h=rot('WWEE',ci);role='V'
  co=H[(H.index(ci)+(1 if t=='R'else-1))%4];nodes.append(dict(cell=canon(p),lift=p,turn=t,ci=ci,co=co,history=h,role=role))
  p=(p[0]+V[co][0],p[1]+V[co][1]);ci=co
 assert p==(6,0)and ci=='N'
 return nodes

def prop(ds):
 q=list(ds)
 while q:
  p=q.pop()
  for dr,v in V.items():
   z=canon((p[0]+v[0],p[1]+v[1]))
   if z not in ds:continue
   opp=H[(H.index(dr)+2)%4];a={edge(h,p,dr)for h in ds[p]}
   nh=[h for h in ds[z]if edge(h,z,opp)in a]
   if not nh:return None
   if len(nh)<len(ds[z]):ds[z]=nh;q.append(z)
 return ds

def check(hs,nodes):
 succ={};eq={};ev=[(p,r)for p,h in hs.items()for r in range(len(h))]
 for p,h in hs.items():
  for dr in H:
   v=V[dr];raw=p[0]+v[0],p[1]+v[1];q=canon(raw);k=(raw[0]-q[0])//(-W) # raw=q+k*d
   sr=[r for r in range(len(h))if out(h,r)==dr]
   if q in hs:
    tr=[r for r,a in enumerate(hs[q])if a==dr]
    if len(sr)!=len(tr):return'PORT',None
    succ.update({(p,a):((q,b),k)for a,b in zip(sr,tr)})
  for dr in ('EW'if sum(p)%2==0 else'NS'):eq[p,dr]=cnt(h,dr,'out')
  for dr in ('NS'if sum(p)%2==0 else'EW'):
   v=V[dr];q=canon((p[0]-v[0],p[1]-v[1]));f=cnt(h,dr,'in')
   if(q,dr)in eq and eq[q,dr]!=f:return'PORT',None
   eq[q,dr]=f
 # Any already closed event component must be the whole actual quotient orbit.
 done=set();cycles=[]
 for a in ev:
  cur=a;vis={};path=[];k=0
  while cur in succ and cur not in vis and cur not in done:
   vis[cur]=(len(path),k);path.append(cur);cur,v=succ[cur];k+=v
  if cur in vis:
   j,k0=vis[cur];cyc=path[j:];w=k-k0
   if len(cyc)!=len(ev)or w!=1:return'CLOSED_EVENT_COMPONENT',dict(length=len(cyc),winding=w,all_events=len(ev),route=cyc)
   cycles.append((cyc,w))
  done.update(path)
 # Every literal return to one physical cell must hit its next complete rank.
 for a in ev:
  cur=a;k=0;seen=set()
  while cur in succ and(cur,k)not in seen:
   seen.add((cur,k));cur,v=succ[cur];k+=v
   if cur[0]==a[0]and k==0:
    if cur[1]!=a[1]+1:return'RANK_RETURN',dict(start=a,target=cur,steps=len(seen))
    break
   # An open path uses each class at most once before any nonzero cycle;
   # all cycles were already rejected unless the entire front candidate.
   if len(seen)>len(ev)*2:break
 # Critical LEFT excursions cannot encounter any RIGHT incoming gamma event.
 right=set();roots=[]
 for n in nodes:
  p=tuple(n['cell']);h=n['history']
  if n['role']=='cut3':roots.append(p);right.add((p,0))
  elif n['turn']=='R':right.add((p,0))
  else:right.update((p,r)for r in range(3))
 for a in roots:
  cur=(a,1);k=0;seen=set()
  while cur in succ and(cur,k)not in seen:
   seen.add((cur,k));cur,v=succ[cur];k+=v
   if cur==(a,2)and k==0:break
   if cur in right or cur[0]in roots and cur[1]in[1,2]:return'CRITICAL_SIDE',dict(root=a,target=cur,voltage=k,steps=len(seen))
   if len(seen)>2*len(ev):break
 # Periodic dual stream, including every zero port, global C maximum and H(L).
 adj=defaultdict(list)
 for(p,dr),f in eq.items():
  c,l=fp(p,dr);c=canon(c);l=canon(l);adj[l].append((c,f));adj[c].append((l,-f))
 val={(0,-1):0};q=deque(val)
 while q:
  u=q.popleft()
  for v,w in adj[u]:
   if v in val:
    if val[v]!=val[u]+w:return'CURL',None
   else:val[v]=val[u]+w;q.append(v)
 if any(a>0 for p,a in val.items()if sum(p)%2):return'C_MAX',None
 if any(a>-1 for p,a in val.items()if sum(p)%2==0):return'H_MAX',None
 return'OPEN',dict(stream={str(p):z for p,z in val.items()},open_out=[(p,r,out(h,r))for p,h in hs.items()for r in range(len(h))if(p,r)not in succ],closed_full=bool(cycles))

summary=Counter();rows=[];t=time.time()
for fs in product(['NNSS','NSSN'],repeat=2):
 nodes=build(fs);fixed={tuple(n['cell']):n['history']for n in nodes};pts=set(fixed)
 while True:
  cand={canon((p[0]+v[0],p[1]+v[1]))for p in pts for v in V.values()}-pts
  add={q for q in cand if sum(canon((q[0]+v[0],q[1]+v[1]))in pts for v in V.values())>=2}
  if not add:break
  pts|=add
 ds=prop({p:([fixed[p]]if p in fixed else dom(p))for p in sorted(pts)})
 counts=Counter();good=[];witness={}
 def rec(ds):
  if all(len(v)==1 for v in ds.values()):
   hs={p:v[0]for p,v in ds.items()};a,ob=check(hs,nodes);counts[a]+=1
   if a=='OPEN':good.append(dict(histories={str(p):h for p,h in hs.items()},**ob))
   elif a not in witness:witness[a]=ob
   return
  p=min((p for p in ds if len(ds[p])>1),key=lambda p:len(ds[p]))
  for h in ds[p]:
   nd=prop(ds|{p:[h]})
   if nd is not None:rec(nd)
 if ds is not None:rec(ds)
 else:counts['PORT_AT_START']+=1
 summary.update(counts);rows.append(dict(flat_words=fs,nodes=nodes,closure_cells=sorted(pts),counts=dict(counts),first_witness=witness,open=good));print(fs,len(pts),dict(counts),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,summary=dict(summary),rows=rows),indent=2)+'\n');print('DONE',time.time()-t,dict(summary))
