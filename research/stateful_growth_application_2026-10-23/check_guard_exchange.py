#!/usr/bin/env python3
"""One retained full-shuttle guard exchange on the actual W6 output.
All-parameter chronology; no cap, phase, word, seed or horizon search.
"""
from pathlib import Path
import sys,json,hashlib
ROOT=Path('/workspace/shared/langton'); HERE=Path(__file__).parent
sys.path.insert(0,str(ROOT/'stateful_growth_quadratic_2026-10-23'))
from quadratic_lap_validator import Context,D
ctx=Context(max_operations=100000000)
W6='RRLRRRRLLLLRLLLLRLRR';T='LRRL'
source=ROOT/'new_constructive_2026-10-23/two_layer_restored_bulk_shuttle.json'
J=json.loads(source.read_text());E=J['stages'][1]['word']
DOMAIN='M>=1 and r>=10 and r>=M+1'
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(a,n):return tuple(x*n for x in a)
def exp(v):return '('+'+'.join(f'{a}*{z}'for a,z in zip(v,('M','r','1')))+')'
def xor(a,b):return a.subtract(b).union(b.subtract(a)).coalesce()
def empty():return ctx.set('[M,r]->{[x,y]:false}')
stages=[(W6,(1,0,0),'writer'),(T,(0,1,0),'outbound'),(E,(0,0,1),'remote'),(T,(0,1,0),'return'),('RRRRLL',(0,0,1),'local')]
p=((0,0,0),(0,0,0));h=1;tm=(0,0,0);families=[];manifest=[]
for word,count,label in stages:
 start=p;hs=h;off=(0,0);reads=[]
 for phase,ch in enumerate(word):
  reads.append((off,h,ch));h=(h+(1 if ch=='R'else-1))%4;off=add(off,D[h])
 repeated=count!=(0,0,1)
 if repeated:assert h==hs and off!=(0,0)
 manifest.append(dict(word=word,count=count,label=label,start=start,heading=hs,time=tm,drift=off))
 for phase,(q,hh,ch) in enumerate(reads):
  v=tuple(add(start[a],(0,0,q[a]))for a in(0,1))
  if repeated:
   domain=DOMAIN+f' and exists(j:0<=j<{exp(count)} and x={exp(v[0])}+{off[0]}*j and y={exp(v[1])}+{off[1]}*j)'
   ax=0 if off[0]else 1;sc=len(word)//off[ax];assert sc*off[ax]==len(word)
   time=(tm[0]-sc*v[ax][0],tm[1]-sc*v[ax][1],sc if ax==0 else 0,sc if ax==1 else 0,tm[2]+phase-sc*v[ax][2])
  else:
   domain=DOMAIN+f' and x={exp(v[0])} and y={exp(v[1])}'
   time=(*tm[:2],0,0,tm[2]+phase)
  families.append(dict(stage=label,phase=phase,turn=ch,heading=hh,domain=ctx.set('[M,r]->{[x,y]:'+domain+'}'),time=time))
 p=tuple(add(start[a],mul(count,off[a]))for a in(0,1));tm=add(tm,mul(count,len(word)))
assert p==((-2,0,0),(0,0,0))and h==1 and tm==(20,8,52)
def prior(g,f):
 dt=tuple(g['time'][a]-f['time'][a]for a in range(5))
 eq='+'.join(f'{a}*{b}'for a,b in zip(dt,('M','r','x','y','1')))+'<0'
 return f['domain'].intersect(g['domain']).intersect(ctx.set('[M,r]->{[x,y]:'+eq+'}'))
firstL=empty();priors=[]
for i,f in enumerate(families):
 ctx.reset_operations();before=empty();ps=[]
 for j,g in enumerate(families):
  z=empty()if i==j else prior(g,f);ps.append(z);before=before.union(z)
 priors.append(ps)
 if f['turn']=='L':firstL=firstL.union(f['domain'].subtract(before))
firstL=firstL.coalesce()
# Explicit disjoint minimum seed, with g=2(r-M)>0. No black requirement
# is silently supplied after the writer begins.
seed_expected=ctx.set('[M,r]->{[x,y]:'+DOMAIN+' and ((y=-3 and -2M<=x<0) or (y=0 and (x=-2M or x=-1 or 1<=x<2r-2M)) or (y=-1 and (x=-1 or x=2r-2M or x=2r-2M+1)) or (x=0 and y=-2))}')
assert firstL.is_equal(seed_expected)
fail=[]
for i,f in enumerate(families):
 ctx.reset_operations();current=firstL.intersect(f['domain'])
 for z in priors[i]:current=xor(current,z)
 bad=f['domain'].subtract(current)if f['turn']=='L'else current
 if not bad.is_empty():fail.append(dict(stage=f['stage'],phase=f['phase'],bad=str(bad.coalesce())))
assert not fail,fail
# Full initial and returned field of this minimal-prepared legal finite episode.
change=empty()
for f in families:change=xor(change,f['domain'])
returned=xor(firstL,change)
q=ctx.set('[M,r]->{[x=-2M-1,y=0]:'+DOMAIN+'}')
a=ctx.set('[M,r]->{[x=-2M,y=1]:'+DOMAIN+'}')
entry=ctx.set('[M,r]->{[x=-2M,y=0]:'+DOMAIN+'}')
# Full field immediately after writer, before shuttle.
afterW=firstL
for f in families:
 if f['stage']=='writer':afterW=xor(afterW,f['domain'])
pre_expected=ctx.set('[M,r]->{[x,y]:'+DOMAIN+' and ((y=0 and -2M-1<=x<2r-2M) or (y=-1 and (x=-2M-1 or x=2r-2M or x=2r-2M+1)) or (x=-2M and y=-2))}')
assert afterW.is_equal(pre_expected)
assert afterW.intersect(q).is_equal(q)and afterW.intersect(a).is_empty()and afterW.intersect(entry).is_equal(entry)
assert returned.intersect(q).is_empty()and returned.intersect(a).is_equal(a)and returned.intersect(entry).is_equal(entry)
shuttle_change=xor(afterW,returned)
# Signed complete 18-cell change with origin translated from (0,2) to (-2M,0).
left={(0,1),(0,2),(-1,2),(-1,0)}
right={(-1,-1),(0,-1),(1,-1),(2,-1),(3,0),(3,1),(0,1),(1,1),(-1,2),(0,2),(1,2),(2,2),(0,3),(1,3)}
clauses=[f'(x=-2M+{x} and y={y})'for x,y in left]+[f'(x=-2M+2r+{x} and y={y})'for x,y in right]
expected=ctx.set('[M,r]->{[x,y]:'+DOMAIN+' and ('+' or '.join(clauses)+')}')
assert shuttle_change.is_equal(expected)
# Actual finite copied-board control at the already selected M50,r51 values.
def control(M=50,r=51):
 word=W6*M+T*r+E+T*r+'RRRRLL';pos=(0,0);hh=1;hist={};seed=set();addresses=[]
 for i,ch in enumerate(word):
  if pos in hist:assert hist[pos][0]!=ch,(i,pos,ch,hist[pos])
  elif ch=='L':seed.add(pos)
  hist[pos]=(ch,i);addresses.append((pos,hh,ch))
  hh=(hh+(1 if ch=='R'else-1))%4;pos=add(pos,D[hh])
 B=set(seed);pos=(0,0);hh=1
 for i,ch in enumerate(word):
  assert ('L'if pos in B else'R')==ch
  if pos in B:B.remove(pos)
  else:B.add(pos)
  hh=(hh+(1 if ch=='R'else-1))%4;pos=add(pos,D[hh])
 assert len(word)==1460 and len(seed)==107 and len(B)==119 and pos==(-100,0)and hh==1
 assert (-101,0)not in B and(-100,1)in B and(-100,0)in B
 return dict(M=M,r=r,reads=len(word),seed_mass=len(seed),final_mass=len(B),head=pos,heading=hh,seed=sorted(seed),returned=sorted(B),word=word)
control_data=control()
report=dict(status='EXACT ALL-PARAMETER PHYSICAL GUARD EXCHANGE, NOT A CAP REPAIR',domain=DOMAIN,
 word='W6^M T^r E46 T^r RRRRLL',endpoint=[[-2,0,0],[0,0,0]],heading=h,duration=tm,
 families=len(families),failures=fail,minimal_seed_mass='2r+5',returned_mass='2r+17',minimal_seed_relation=str(firstL),complete_before_shuttle_relation=str(afterW),complete_returned_relation=str(returned),
 complete_shuttle_change_relation=str(shuttle_change),stages=manifest,
 local_exchange=dict(before='entry p black, a=p+(0,1) white, q=p+(-1,0) black',after='entry p black, a black, q white',
 source_guard='last W6 phase19 R',clearing_guard='final local phase5 L',blocking_gate='local phase3 R followed by first outbound-T phase1 R, with three intervening off-cell reads'),
 arbitrary_remote_cap_scope='Any actual prefix reaching the fixed local RRRRLL entry (-1,1,W), relative to the E return port, has the same final six-read geometry; after that local cap, a is black and q white. Every immediately following T or F fails at T phase1, regardless of the preceding remote cap, arm lengths, retained board or supply.',
 source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),retained_shuttle_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
 scope=__doc__)
(HERE/'guard_exchange.json').write_text(json.dumps(report,indent=2)+'\n')
(HERE/'guard_exchange_M50_r51.json').write_text(json.dumps(control_data,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items()if k not in('stages','minimal_seed_relation','complete_returned_relation','complete_shuttle_change_relation')},indent=2))
print('FIRSTL',firstL)
print('RETURNED',returned)
