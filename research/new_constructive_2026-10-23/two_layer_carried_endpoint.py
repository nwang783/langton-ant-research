#!/usr/bin/env python3
"""One two-layer changed-endpoint excursion, exact all-parameter chronology.
The word was selected from the ONE stored r=k=10 orbit, not a seed scan.
All initial and returned cells are retained. This is not a renewal claim.
"""
from pathlib import Path
import sys,json,time,hashlib
P=Path('/workspace/shared/langton'); O=Path(__file__).parent
sys.path.insert(0,str(P/'computability/unit_inductive_certificates'))
from presburger_read_set_solver import Context
from isl_exact import Object,_FUN
ctx=Context(max_operations=100000000);D=((0,1),(1,0),(0,-1),(-1,0));DOMAIN='r>=10 and k>=10'
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(a,n):return tuple(x*n for x in a)
def neg(a):return mul(a,-1)
def rot(p,n):
 x,y=p
 for _ in range(n):x,y=y,neg(x)
 return x,y
def exp(v):return '('+'+'.join(f'{a}*{z}'for a,z in zip(v,('r','k','1')))+')'
def xor(a,b):return a.subtract(b).union(b.subtract(a)).coalesce()
def input_frame(shift):
 # Literal four-side minimum frame, with k replaced by k+shift, then y+shift.
 v=((2,1,shift),(0,-1,-shift-1));p=((0,0,0),(0,0,0));I=ctx.set('[r,k]->{[x,y]:false}')
 # Vectors below have coefficients r,k,s,1.
 base=[(((0,0,1,0),(0,0,0,0)),'0<=s<2r'),(((2,0,1,0),(0,0,-1,-1)),f'0<=s<k+{shift}')]
 for j in range(4):
  for off,bound in base:
   q=rot(off,j);q=tuple(plus(q[a],(p[a][0],p[a][1],0,p[a][2]))for a in(0,1));q=(q[0],plus(q[1],(0,0,0,shift)))
   ee=lambda z:'('+'+'.join(f'{a}*{b}'for a,b in zip(z,('r','k','s','1')))+')'
   I=I.union(ctx.set('[r,k]->{[x,y]:'+DOMAIN+' and exists(s:'+bound+f' and x={ee(q[0])} and y={ee(q[1])}' +')}'))
  vv=rot(v,j);p=tuple(plus(p[a],vv[a])for a in(0,1))
 return I.coalesce()
I0=input_frame(0);I1=input_frame(1);I2=input_frame(2)
assert I0.intersect(I2).is_empty() and I1.intersect(I2).is_empty()
initial=I1.union(I2).coalesce() # Exactly after the already-signed first frame.
w=(O/'two_layer_gap_frame_r10_k10.word.txt').read_text()[244:828]
A=w[:20];B=w[200:210];C=w[424:488];Z=w[559:584]
assert len(A)==20 and len(B)==10 and len(C)==64 and len(Z)==25
stages=[(A,(1,0,0),'A'),(B,(0,0,1),'B')]
for j in range(3):stages += [('RL',(0,1,2),f'S{j}:diagonal'),('RRLL',(1,0,-1),f'S{j}:straight'),('RRLRL',(0,0,1),f'S{j}:corner')]
stages += [('RL',(0,1,-1),'last_diagonal'),('R',(0,0,1),'last_corner'),(C,(0,0,1),'C'),('LRRL',(1,0,-1),'east_transfer'),('LLL',(0,0,1),'turn'),('RRLL',(1,0,-2),'west_transfer'),(Z,(0,0,1),'Z')]
assert ''.join(word*(10*a+10*b+c)for word,(a,b,c),label in stages)==w
F=[];p=((0,0,0),(0,0,0));tm=(0,0,0);h=1;delta_mass=(0,0,0);manifest=[]
for word,count,label in stages:
 start=p;hs=h;local=(0,0);rr=[]
 for slot,ch in enumerate(word):
  rr.append((local,ch));h=(h+(1 if ch=='R'else-1))%4;dv=D[h];local=local[0]+dv[0],local[1]+dv[1]
 repeated=count!=(0,0,1)
 if repeated:assert h==hs and local!=(0,0)
 manifest.append(dict(label=label,word=word,count=count,start=start,heading=hs,time=tm,drift=local))
 for slot,(off,ch) in enumerate(rr):
  v=tuple(plus(start[a],(0,0,off[a]))for a in(0,1))
  if repeated:
   bound=f'0<=i<{exp(count)}';dom=DOMAIN+' and exists(i:'+bound+f' and x={exp(v[0])}+{local[0]}*i and y={exp(v[1])}+{local[1]}*i)'
   axis=0 if local[0]else 1;assert len(word)%local[axis]==0;scale=len(word)//local[axis]
   tf=(tm[0]-scale*v[axis][0],tm[1]-scale*v[axis][1],scale if axis==0 else 0,scale if axis==1 else 0,tm[2]+slot-scale*v[axis][2])
  else:dom=DOMAIN+f' and x={exp(v[0])} and y={exp(v[1])}';tf=(tm[0],tm[1],0,0,tm[2]+slot)
  F.append(dict(stage=label,slot=slot,turn=ch,domain=ctx.set('[r,k]->{[x,y]:'+dom+'}'),time=tf))
 p=tuple(plus(start[a],mul(count,local[a]))for a in(0,1));tm=plus(tm,mul(count,len(word)));delta_mass=plus(delta_mass,mul(count,word.count('R')-word.count('L')))
assert p==((0,0,0),(0,0,2)) and h==1 and tm==(40,8,104)
startclock=time.monotonic();fail=[];pairs=0;nonempty=0
for i,f in enumerate(F):
 ctx.reset_operations();current=initial.intersect(f['domain'])
 for j,g in enumerate(F):
  # Each repeated read family has nonzero drift, so self copies never overlap.
  if i==j:continue
  pairs+=1;z=f['domain'].intersect(g['domain'])
  if z.is_empty():continue
  dt=tuple(g['time'][a]-f['time'][a]for a in range(5));ineq='+'.join(f'{a}*{b}'for a,b in zip(dt,('r','k','x','y','1')))+'<0'
  prior=z.intersect(ctx.set('[r,k]->{[x,y]:'+ineq+'}'))
  if not prior.is_empty():current=xor(current,prior);nonempty+=1
 bad=f['domain'].subtract(current)if f['turn']=='L'else current
 if not bad.is_empty():fail.append(dict(family=i,stage=f['stage'],slot=f['slot'],bad=str(bad.coalesce())));break
 if i%50==0:print('checked',i,'of',len(F),flush=True)
returned=initial
if not fail:
 for f in F:returned=xor(returned,f['domain'])
 returned=returned.coalesce()
report=dict(status='AUTHOR EXACT ALL-r,k CHANGED-ENDPOINT EXCURSION'if not fail else'FAILED',domain=DOMAIN,initial_before_first_frame='I(r,k) UNION [I(r,k+2)+(0,2)]',initial_mass='16r+8k+8',initial_after_first_frame='[I(r,k+1)+(0,1)] UNION [I(r,k+2)+(0,2)]',start_pose=[[0,0],1],continuation_time_coefficients=tm,full_time_coefficients=[56,16,108],endpoint=[[0,2],1],continuation_mass_delta_coefficients=delta_mass,returned_mass_coefficients=plus((16,8,12),delta_mass),families=len(F),ordered_pairs=pairs,nonempty_prior_relations=nonempty,failures=fail,stages=manifest,initial_relation=str(initial),returned_relation=str(returned)if not fail else None,seconds=time.monotonic()-startclock,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope=__doc__)
(O/'two_layer_carried_endpoint.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items()if k not in('stages','initial_relation','returned_relation')},indent=2))
