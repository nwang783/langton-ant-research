#!/usr/bin/env python3
"""Finite component search on an explicitly INFINITE wake, not finite-seed HC."""
import json,time,hashlib
from pathlib import Path
OUT=Path(__file__).resolve().parent
H=json.loads(Path('/workspace/shared/langton/recovered_bundle/ant_global/root/standard.json').read_text())['word']
D=((0,1),(1,0),(0,-1),(-1,0))
BLACK={(-3,0),(-3,1),(-2,1),(-1,0),(0,0),(1,1),(2,0),(3,0),(5,1),(6,1),(7,0),(7,1)}
PHASES={H[a:]+H[:a] for a in range(104)}
MAXTIME=100000

def base(p):return (p[0]-p[1],p[0]%2) in BLACK

def certify(E,p,h,w):
 q=[];pp=p;hh=h
 for a in w:
  q.append(pp);hh=(hh+(-1 if a=='L' else 1))%4
  dx,dy=D[hh];pp=(pp[0]+dx,pp[1]+dy)
 if hh!=h:return False
 d=(pp[0]-p[0],pp[1]-p[1])
 if d==(0,0):return False
 dx,dy=d
 def multiple(v):
  if dx:
   if v[0]%dx:return None
   k=v[0]//dx
   return k if v[1]==k*dy else None
  if v[0] or v[1]%dy:return None
  return v[1]//dy
 def key(v):
  return (dx*v[1]-dy*v[0],v[0]%abs(dx)) if dx else (v[0],v[1]%abs(dy))
 ix={}
 for b in E:ix.setdefault(key(b),[]).append(b)
 for i,qi in enumerate(q):
  changes={};zero=0;cuts={0}
  def toggle(k):changes[k]=not changes.get(k,False);cuts.add(k)
  for j,qj in enumerate(q):
   k=multiple((qj[0]-qi[0],qj[1]-qi[1]))
   if k is not None:
    if k>0:toggle(k)
    elif k==0 and j<i:zero^=1
  for b in ix.get(key(qi),[]):
   k=multiple((b[0]-qi[0],b[1]-qi[1]))
   assert k is not None
   if k>=0:toggle(k);toggle(k+1)
  dt=dx-dy
  if dt:
   for t,a in BLACK:
    dd=t-(qi[0]-qi[1])
    if dd%dt==0:
     k=dd//dt
     if k>=0:cuts.update((k,k+1))
  cuts=sorted(cuts);parity=bool(zero)
  expected=w[i]=='L'
  for z,k in enumerate(cuts):
   parity^=changes.get(k,False)
   checks=[k]
   end=cuts[z+1] if z+1<len(cuts) else None
   if not dt and dx%2 and (end is None or k+1<end):checks.append(k+1)
   for s in checks:
    color=parity^base((qi[0]+s*dx,qi[1]+s*dy))
    if color!=expected:return False
 return True

def candidate(s):
 n=len(s)
 if n>=208 and s[-104:] in PHASES and s[-208:-104]==s[-104:]:return s[-104:]
 s=s[-2048:];n=len(s)
 pi=[0]*n
 for i in range(1,n):
  j=pi[i-1]
  while j and s[i]!=s[j]:j=pi[j-1]
  if s[i]==s[j]:j+=1
  pi[i]=j
 p=n-pi[-1]
 if p<=512 and n>=3*p:return s[-p:]
 return None

def run(cap,h):
 E=set(cap);p=(0,0);letters=[];checks=0
 for t in range(1,MAXTIME+1):
  c=base(p)^(p in E);a='L' if c else 'R';letters.append(a)
  h=(h+(-1 if c else 1))%4
  if p in E:E.remove(p)
  else:E.add(p)
  dx,dy=D[h];p=(p[0]+dx,p[1]+dy)
  if t>=512 and t%512==0:
   w=candidate(''.join(letters[-2048:]))
   if w is not None:
    checks+=1
    if certify(E,p,h,w):
     standard=len(w)%104==0 and any(w==(v*(len(w)//104)) for v in PHASES)
     r={'status':'STANDARD' if standard else 'NONSTANDARD','time':t,'period':len(w),'checks':checks,'cap':sorted(cap),'pose':[p,h],'xor_mass':len(E)}
     if not standard:
      r.update({'word':w,'xor':sorted(E)})
     return r
 return {'status':'UNKNOWN','time':MAXTIME,'checks':checks,'cap':sorted(cap),'xor_mass':len(E)}

# Positive controls: the known bare wake must give certified standard outcomes.
t0=time.time();results=[]
for h in (1,3):
 rr=run(set(),h);assert rr['status']=='STANDARD';rr['initial_heading']=h;results.append(rr)
for h in (1,3):
 for x in range(-6,7):
  for y in range(-6,7):
   rr=run({(x,y)},h);rr['initial_heading']=h;results.append(rr)
   if rr['status']=='NONSTANDARD':
    (OUT/'standard_wake_nonstandard_component.json').write_text(json.dumps(rr,indent=2)+'\n')
    print('ACCEPTED NONSTANDARD',json.dumps({k:v for k,v in rr.items() if k not in ('xor','word')}),flush=True)
   if len(results)%25==0:print('PROGRESS',len(results),'unknown',sum(r['status']=='UNKNOWN' for r in results),'seconds',round(time.time()-t0,2),flush=True)
summary={'status':'FINITE SCOPED SEARCH','domain':'Both same-sector headings E,W at origin; exactly one initial XOR flip in[-6,6]^2 plus bare controls on the INFINITE bilateral standard wake.','horizon':MAXTIME,'inputs':len(results),'accepted_standard':sum(r['status']=='STANDARD' for r in results),'accepted_nonstandard':sum(r['status']=='NONSTANDARD' for r in results),'unknown':sum(r['status']=='UNKNOWN' for r in results),'seconds':time.time()-t0,'maximum_standard_certificate_time':max((r['time'] for r in results if r['status']=='STANDARD'),default=None),'scope_warning':'No arbitrary finite-cap theorem, finite-seed launch, or global budget follows. UNKNOWN is not exclusion.','results':results}
(OUT/'standard_wake_small_caps_search.json').write_text(json.dumps(summary,indent=2)+'\n')
print('SUMMARY',json.dumps({k:v for k,v in summary.items() if k!='results'}),flush=True)
