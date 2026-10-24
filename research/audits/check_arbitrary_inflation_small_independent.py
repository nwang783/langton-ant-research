"""Independent complete image inventories, exhausted prefix trees and ownership."""
from itertools import product
from collections import deque
from pathlib import Path
import json,time
ROOT=Path('/workspace/shared/langton');SRC=ROOT/'causal_reduction/morphic_candidates';start=time.time()
def advance(w,p=0j,h=1j,old=None):
 seen={} if old is None else old.copy();ps=[];reads=[]
 for c in w:
  reads.append((p,c))
  if seen.get(p)==c:return None
  seen[p]=c;h*=(-1j if c=='R' else 1j);p+=h;ps.append((p,h))
 return p,h,seen,ps,reads
def inventory(k):
 R={};L={}
 for cs in product('RL',repeat=k):
  w=''.join(cs);x=advance(w)
  if x is None:continue
  p,h=x[:2]
  if h==1:R.setdefault(p,[]).append(w)
  if h==-1:L.setdefault(-p,[]).append(w)
 return {a:{'R':R[a],'L':L[a]} for a in R.keys()&L.keys() if int(a.real)**2+int(a.imag)**2>1}
def exhausted(k,a,opts,source):
 queue=deque([('',[(0j,1j)],{})]);nodes=0;depth=0;failures=0
 while queue:
  word,poses,seen=queue.popleft();n=len(word)//k;nodes+=1;depth=max(depth,n)
  assert nodes<=source['nodes'],'declared exhausted tree did not close'
  ws=([w for c in 'RL' for w in opts[c] if w[0]==c] if n==0 else opts[word[n]])
  for w in ws:
   x=advance(w,*poses[-1],seen)
   if x is None:failures+=1;continue
   p,h,newseen,newposes,_=x;pp=poses+newposes
   assert (p,h)==(a*pp[n+1][0],pp[n+1][1])
   queue.append((word+w,pp,newseen))
 assert (nodes,depth)==(source['nodes'],source['maxdepth'])
 assert failures==source['counts'].get('alternation_conflict',0)
 return {'nodes':nodes,'depth':depth,'conflicts':failures}
def owner_rows(a,opts):
 aa,bb=int(a.real),int(a.imag);norm=aa*aa+bb*bb;positions=[]
 for w in opts['R']+opts['L']:
  for p,c in advance(w)[4]:
   for h in range(4):positions.append((p*((-1j)**h),h))
 out=[]
 for w in opts['R']:
  first={}
  for p,c in advance(w)[4]:first.setdefault(p,c)
  cells=[]
  for p,c in first.items():
   if c!='L':continue
   owners=set()
   for q,h in positions:
    delta=p-q;dx,dy=int(delta.real),int(delta.imag);nx=aa*dx+bb*dy;ny=aa*dy-bb*dx
    if nx%norm or ny%norm:continue
    x,y=nx//norm,ny//norm
    if (x+y+h)%2==0:owners.add((x,y))
   assert (0,0) in owners
   cells.append({'cell':[int(p.real),int(p.imag)],'owners':sorted(owners),'private':owners=={(0,0)},'forward':all(y>=0 for x,y in owners)})
  out.append({'word':w,'cells':cells,'private':any(c['private'] for c in cells),'forward':any(c['forward'] for c in cells)})
 return out
reports=[];remaining=[]
for k in [7,9]:
 inv=inventory(k);source=json.loads((SRC/f'free_inflations_k{k}.json').read_text());sources={complex(*r['scale']):r for r in source['results']};assert set(inv)==set(sources)
 for a,opts in sorted(inv.items(),key=lambda kv:(kv[0].real,kv[0].imag)):
  s=sources[a];assert {c:sorted(opts[c]) for c in 'RL'}=={c:sorted(s['images'][c]) for c in 'RL'}
  r={'k':k,'a':[int(a.real),int(a.imag)],'R':opts['R'],'L':opts['L']}
  if s['status']=='NONINCREASING_SCALE_MASS':
   assert max(w.count('R')-w.count('L') for w in opts['R'])<=1
   assert max(w.count('R')-w.count('L') for w in opts['L'])<=-1
   r['exclusion']='mass'
  elif s['status']=='EXHAUSTED':r.update(exclusion='finite tree',tree=exhausted(k,a,opts,s))
  else:
   rows=owner_rows(a,opts);r['ownership']=rows
   private=all(z['private'] for z in rows);forward=all(z['forward'] for z in rows)
   r['exclusion']='private fuel' if private else 'record fuel' if forward else None
   if r['exclusion'] is None:remaining.append([k,r['a']])
  reports.append(r)
assert remaining==[[9,[3,0]]]
report={'status':'passed','scope':'All pure position-and-heading arbitrary-choice inflation scales k7 and k9; k9,a3 remains unresolved. Capped source branches were never treated as exclusions.','rows':reports,'unresolved':remaining,'seconds':time.time()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
