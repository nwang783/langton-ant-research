#!/usr/bin/env python3
"""All-n exact first-read chronology for Q U^n Q V^4 U^n Q."""
from pathlib import Path
from collections import defaultdict
import json,hashlib
R=Path(__file__).resolve().parents[1]
FILE=R/'continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json'
D=json.loads(FILE.read_text());assert all(D[k]['word'] and set(D[k]['word'])<={'R','L'} for k in 'QUV');assert [len(D[k]['word']) for k in 'QUV']==[64,28,18];DIR=((0,1),(1,0),(0,-1),(-1,0))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def ev(a,n):return a[0]*n+a[1]
def walk(word,h):
 p=(0,0);out=[]
 for j,c in enumerate(word):
  out.append((p,c,j));h=(h+(1 if c=='R' else -1))%4;d=DIR[h];p=p[0]+d[0],p[1]+d[1]
 return out,p,h
segments=[(D['Q']['word'],False),(D['U']['word'],True),(D['Q']['word'],False),(D['V']['word']*4,False),(D['U']['word'],True),(D['Q']['word'],False)]
families=defaultdict(list);p=((0,0),(0,0));h=0
for s,(word,repeated) in enumerate(segments):
 reads,drift,eh=walk(word,h)
 if repeated:assert eh==h and drift[0]==0 and abs(drift[1])==4
 for (x,y),c,j in reads:
  xp=add(p[0],(0,x));yp=add(p[1],(0,y));assert xp[0]==0 and yp[0]%4==0
  residue=yp[1]%4;base=(yp[0]//4,(yp[1]-residue)//4)
  step=drift[1]//4 if repeated else 0
  if step==1:lo=base;hi=add(base,(1,0))
  elif step==-1:lo=add(base,(-1,1));hi=add(base,(0,1))
  else:lo=base;hi=add(base,(0,1))
  families[(xp[1],residue)].append(dict(segment=s,phase=j,c=c,base=base,step=step,lo=lo,hi=hi))
 p=tuple(add(a,(v,0) if repeated else (0,v)) for a,v in zip(p,drift));h=eh
assert p==((0,0),(0,8)) and h==2
# Choose an exact integer above every crossing of distinct affine endpoints.
N0=3
for fs in families.values():
 edges={tuple(f[k]) for f in fs for k in ('lo','hi')}
 for a in edges:
  for b in edges:
   da,db=sub(a,b)
   if da:N0=max(N0,(-db)//da+1)
rows=[];fuel=(0,0)
for key,fs in sorted(families.items()):
 edges=sorted({tuple(f[k]) for f in fs for k in ('lo','hi')},key=lambda a:ev(a,N0))
 for left,right in zip(edges,edges[1:]):
  dif=sub(right,left);assert dif[0]>=0 and ev(dif,N0)>0
  active=[f for f in fs if ev(f['lo'],N0)<=ev(left,N0)<ev(f['hi'],N0)]
  if not active:continue
  def index(f):return f['step']*(ev(left,N0)-ev(f['base'],N0)) if f['step'] else 0
  active.sort(key=lambda f:(f['segment'],index(f),f['phase']))
  for a,b in zip(active,active[1:]):
   if a['segment']==b['segment']:
    assert a['step']==b['step']
    # At a shared point, relative repetition indices are parameter-independent.
    d=sub(a['base'],b['base']);assert d[0]==0
    gap=a['step']*d[1]
    assert gap>0 or gap==0 and a['phase']<b['phase']
  letters=''.join(f['c'] for f in active)
  assert all(a!=b for a,b in zip(letters,letters[1:])),(key,left,right,letters)
  if letters[0]=='L':fuel=add(fuel,dif)
  rows.append(dict(column=key[0],residue=key[1],lower=left,upper_exclusive=right,letters=letters,events=[(f['segment'],f['phase']) for f in active]))
assert fuel==(10,57),fuel
# Every exceptional endpoint-order value below N0 is independently literal.
def literal(n):
 word=D['Q']['word']+D['U']['word']*n+D['Q']['word']+D['V']['word']*4+D['U']['word']*n+D['Q']['word']
 last={};seed=set();p=(0,0);h=0
 for t,c in enumerate(word):
  if p in last:
   if last[p][1]==c:return dict(feasible=False,conflict=(last[p],(t,c),p))
  elif c=='L':seed.add(p)
  last[p]=(t,c);h=(h+(1 if c=='R' else -1))%4;d=DIR[h];p=p[0]+d[0],p[1]+d[1]
 assert p==(0,8) and h==2 and len(seed)==10*n+57
 return dict(feasible=True,fuel=len(seed),time=len(word))
small={n:literal(n) for n in range(max(N0,4))}
assert all(small[n]['feasible']==(n>=3) for n in small)
result=dict(status='PASS',family='Q U^n Q V^4 U^n Q',feasible_exactly='integer n>=3',affine_endpoint_order_threshold=N0,minimal_seed_mass='10n+57',time='56n+264',end_pose=[0,8,2],source_sha256=hashlib.sha256(FILE.read_bytes()).hexdigest(),small_cases=small,slab_count=len(rows),slabs=rows)
(R/'audits/quqv4uq_family_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='slabs'},indent=2))
