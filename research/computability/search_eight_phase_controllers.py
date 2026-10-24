"""NOT RUN: this pure-root class is already covered by the causal worker's
independently RUP-certified 512-turn k8 exclusion. Retained only as unused
prototype; it does not treat eventual affine or coupled-curve relations.

Discovery-only literal synthesis for p(8n)=(2+2i)p(n).
A rule depends on coarse R/L, coarse absolute heading and fine entry heading.
Unassigned rules branch once, then must be reused. No finite-support claim
from a surviving horizon; fuel counts distinct first-L cells exactly.
"""
import itertools,json,time,sys,pathlib,collections
D=((0,1),(1,0),(0,-1),(-1,0))
HERE=pathlib.Path(__file__).resolve().parent

def mul(p): return (2*p[0]-2*p[1],2*p[0]+2*p[1])
def inventory():
 by=collections.defaultdict(list)
 for H in (0,2):
  for ww in itertools.product('RL',repeat=8):
   w=''.join(ww);x=y=0;h=H;last={};good=True
   for ch in w:
    if last.get((x,y))==ch:good=False;break
    last[(x,y)]=ch;h=(h+(1 if ch=='R' else -1))%4;dx,dy=D[h];x+=dx;y+=dy
   if good:by[H,x,y].append(w)
 return by
BY=inventory()

def search(root,fuelcap,nodecap=200000,depthcap=1000):
 letters=[];poses=[(0,0,0)];last={};rules={};nodes=conflicts=fuelfails=maxdepth=0;stop=None;best=None;fuel=0
 def dfs(n):
  nonlocal nodes,conflicts,fuelfails,maxdepth,stop,best,fuel
  nodes+=1
  if n>maxdepth:
   maxdepth=n;best=dict(word=''.join(letters),fuel=fuel,rules=[dict(key=k,word=v) for k,v in rules.items()])
  if nodes>=nodecap:stop='NODE_CAP';return
  if n>=depthcap:stop='HORIZON_ONLY';return
  c=root if n==0 else letters[n];hc=poses[n][2];hf=poses[-1][2];assert hf in (0,2)
  dx,dy=mul(D[(hc+(1 if c=='R' else -1))%4]);key=(c,hc,hf);fresh=key not in rules
  for w in BY.get((hf,dx,dy),[]) if fresh else [rules[key]]:
   if n==0 and w[0]!=root:continue
   if fresh:rules[key]=w
   l0=len(letters);p0=len(poses);f0=fuel;undo=[];okay=True
   for ch in w:
    x,y,h=poses[-1];p=x,y;old=last.get(p)
    if old==ch:conflicts+=1;okay=False;break
    if old is None and ch=='L':
     fuel+=1
     if fuelcap is not None and fuel>fuelcap:fuelfails+=1;okay=False;break
    undo.append((p,old));last[p]=ch;letters.append(ch);h=(h+(1 if ch=='R' else -1))%4;dx,dy=D[h];poses.append((x+dx,y+dy,h))
   if okay:
    assert poses[-1][:2]==mul(poses[n+1][:2]);dfs(n+1)
   for p,old in reversed(undo):
    if old is None:del last[p]
    else:last[p]=old
   del letters[l0:];del poses[p0:];fuel=f0
   if fresh:del rules[key]
   if stop:return
 dfs(0)
 return dict(root=root,fuelcap=fuelcap,status=stop or 'EXHAUSTED',nodes=nodes,conflicts=conflicts,fuel_failures=fuelfails,max_macros=maxdepth,best=best)
if __name__=='__main__':
 sys.setrecursionlimit(10000);start=time.time();results=[]
 budgets=[int(x) if x!='none' else None for x in sys.argv[1:]] or [None]
 for cap in budgets:
  for root in 'RL':
   r=search(root,cap);results.append(r);print({k:v for k,v in r.items() if k!='best'},flush=True)
   (HERE/'eight_phase_controllers.json').write_text(json.dumps(dict(results=results,seconds=time.time()-start,inventory_size=sum(map(len,BY.values()))),indent=2))
