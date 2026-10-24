"""Discovery: exact adjacent two-flat gates, complete count-derived corner closure.
No imposed period, drift or radius. Every added cell is the corner completing two
known neighboring ports; all 0..4 WHITE histories are retained until constraints.
OPEN outputs are necessary local networks, not physical board factors/fronts.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json,time
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
base=Path(__file__).parent
lib={};exec((base/'flat_flow2_symbolic_row_with_odd_left.py').read_text().split('rows=[];n=0')[0],lib)
check=lib['check'];out=lib['out'];cnt=lib['cnt'];fp=lib['fp']
def rot(h,ci,base='E'):
 return ''.join(H[(H.index(a)+H.index(ci)-H.index(base))%4] for a in h)
def dom(p):
 ax='NS' if sum(p)%2==0 else 'EW'
 return ['']+[''.join(a) for n in range(1,5) for a in product(ax,repeat=n)]
def edge(h,p,dr):
 if (dr in'EW')==(sum(p)%2==0):return cnt(h,dr,'out')
 return cnt(h,H[(H.index(dr)+2)%4],'in')
def mk(tmpl,bs,fs,ms,ss):
 # B is incoming N all-N sink; source rotated from EWE/EWEW.
 turns={'RR':'RLRRLR','RLR':'RLRLRLR','RLLR':'RLRLLRLR'}[tmpl]
 p=(-1,-1);ci='N';nodes=[];flat=iter(fs);mid=iter(ms)
 for i,tr in enumerate(turns):
  if i==0:h='N'*bs;role='sink'
  elif i==len(turns)-1:h=rot('EWE' if ss==3 else 'EWEW',ci);role='source'
  elif tr=='R':h=rot(next(flat),ci,'N');role='flat'
  elif i in[1,len(turns)-2]:h=rot('WWEE',ci);role='Vcap'
  else:h=rot(next(mid),ci);role='middle'
  co=H[(H.index(ci)+(1 if tr=='R' else -1))%4]
  assert h[0]==(ci if tr=='R' else H[(H.index(ci)+2)%4])
  nodes.append(dict(cell=p,turn=tr,history=h,role=role,ci=ci,co=co))
  p=p[0]+V[co][0],p[1]+V[co][1];ci=co
 return nodes

def propagate(ds):
 queue=list(ds)
 while queue:
  p=queue.pop();ap=ds[p]
  for dr,v in V.items():
   q=(p[0]+v[0],p[1]+v[1])
   if q not in ds:continue
   opp=H[(H.index(dr)+2)%4]
   vals={edge(h,p,dr) for h in ap}
   nq=[h for h in ds[q] if edge(h,q,opp)in vals]
   if not nq:return None
   if len(nq)<len(ds[q]):ds[q]=nq;queue.append(q)
 return ds

def sidecheck(hs,nodes):
 """Only exact known contiguous successor constraints, not reader-free sides."""
 succ={};right=set();roots=[]
 for no in nodes:
  p=tuple(no['cell']);h=no['history']
  if no['turn']=='R':right.add((p,0))
  elif no['role']=='middle' and len(h)>=3 and h[0]!=h[1]:
   # normalized WEE/WEEW: first opposite, then selected E twice.
   roots.append(p);right.add((p,0));
   if len(h)==4:right.add((p,3))
  else:right.update((p,r)for r in range(min(3,len(h))))
 for p,h in hs.items():
  for dr,v in V.items():
   q=p[0]+v[0],p[1]+v[1]
   if q not in hs:continue
   sr=[r for r in range(len(h))if out(h,r)==dr];tr=[r for r,a in enumerate(hs[q])if a==dr]
   if len(sr)!=len(tr):return 'port'
   succ.update({(p,a):(q,b)for a,b in zip(sr,tr)})
 for p in roots:
  cur=(p,1);seen={cur}
  while cur in succ:
   cur=succ[cur]
   if cur==(p,2):break
   if cur in right or any(cur==(q,1)for q in roots):return'critical_SIDE'
   if cur in seen:return'critical_CYCLE'
   seen.add(cur)
 return None

stats=Counter();answers=[];start=time.time()
for tmpl in ['RR','RLR','RLLR']:
 for bs,ss in product([3,4],repeat=2):
  for fs in product(['NNSS','NSSN'],repeat=2):
   for ms in ([()] if tmpl=='RR'else [('WEE',),('WEEW',),('WWEE',)] if tmpl=='RLR' else product(['WEE','WEEW','WWEE'],repeat=2)):
    nodes=mk(tmpl,bs,fs,ms,ss);fixed={tuple(n['cell']):n['history']for n in nodes};pts=set(fixed)
    while True:
     cand={ (p[0]+v[0],p[1]+v[1])for p in pts for v in V.values() }-pts
     add={q for q in cand if sum((q[0]+v[0],q[1]+v[1])in pts for v in V.values())>=2}
     if not add:break
     pts|=add
    ds=propagate({p:([fixed[p]]if p in fixed else dom(p))for p in sorted(pts)})
    stats['primary']+=1
    if ds is None:stats['primary_PORT']+=1;continue
    loc=Counter();good=[]
    def rec(ds):
     if all(len(a)==1 for a in ds.values()):
      hs={p:a[0]for p,a in ds.items()};a=check(hs)
      if a=='open':a=sidecheck(hs,nodes)or'open'
      loc[a]+=1
      if a=='open':good.append({f'{p[0]},{p[1]}':h for p,h in hs.items()})
      return
     p=min((p for p in ds if len(ds[p])>1),key=lambda p:len(ds[p]))
     for h in ds[p]:
      nd=propagate(ds|{p:[h]})
      if nd is not None:rec(nd)
    rec(ds);stats.update(loc)
    answers.append(dict(template=tmpl,sink=bs,source=ss,flat_words=fs,middle_words=ms,known_nodes=nodes,closure_cells=sorted(pts),counts=dict(loc),open=good))
    if good:print('OPEN',tmpl,bs,ss,fs,ms,len(good),'cells',len(pts),flush=True)
obj=dict(scope=__doc__,summary=dict(stats),primary_rows=answers,warning='Discovery only: finite local necessary controls; not assigned global event phases, complete reader exterior, board factor or front. Full quotient aliases and exact two-flat motif exhaustion need separate proof.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n')
print('DONE',dict(stats),'seconds',time.time()-start)
