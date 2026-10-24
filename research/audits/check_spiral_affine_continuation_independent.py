"""Independent affine-incidence arrangement and complete representative replays."""
import json,hashlib,time
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm,floor
ROOT=Path('/workspace/shared/langton');P=ROOT/'causal_reduction/spiral_endpoint';words=json.loads((P/'family_words.json').read_text())
canonical=json.loads((ROOT/'computability/singleton_first_block_input.json').read_text())['word'];assert hashlib.sha256(canonical.encode()).hexdigest()=='9772fa0cced75fab3a1d336c6a1326e0e4be8f4e471a3807e0778fccc94c1f04'
assert len(words['H'])==104 and words['H'] in canonical+canonical
vectors=((0,1),(1,0),(0,-1),(-1,0))
sequence=[('RL',(1,0))]+[(words[k],c)for k,c in [('P',(0,1)),('V',(1,-9)),('C',(0,1)),('W',(1,0)),('D',(0,1)),('H',None)]]
assert [len(w)for w,c in sequence]==[2,1540,10,22,10,1549,104]
A=(0,0);B=(0,0);h=0;reads=[];starts=[]
for block,(word,count) in enumerate(sequence):
 starts.append((A,B,h));x=y=0;oldh=h;local=[]
 for phase,turn in enumerate(word):
  local.append((x,y));h=(h+(1 if turn=='R'else -1))%4;dx,dy=vectors[h];x+=dx;y+=dy
 drift=(x,y);repeat=count!=(0,1)
 if repeat:assert h==oldh
 for phase,(x,y) in enumerate(local):reads.append((A,(B[0]+x,B[1]+y),drift if repeat else (0,0),count,block,phase))
 if count is not None:
  A=tuple(A[z]+count[0]*drift[z]for z in (0,1));B=tuple(B[z]+count[1]*drift[z]for z in (0,1))
assert starts[-1]==((-1,1),(-13,6),3) and drift==(-2,-2)
cap={(1,-1),(1,0),(-1,1),(0,1),(-3,0),(-3,1),(-2,-1),(-1,-1),(-2,1)}
arms=[((1,-1),(0,0)),((1,1),(0,-1)),((1,1),(-1,0)),((-1,-1),(-2,1)),((-1,1),(-2,0)),((-1,-1),(-1,0)),((1,-1),(-2,0))]
seed=[((0,0),q,(0,0),(0,1),-1,0)for q in cap]
seed += [((0,0),(2*v[0]+b[0],2*v[1]+b[1]),v,(1,-1),-1,0)for v,b in arms]
# Only geometry is deduplicated; every physical update remains in the replay.
def geometries(fs):return sorted(set(f[:-1]for f in fs),key=str)
target=geometries(reads);source=geometries(seed+reads);atoms=set();modulus=1

def atom(coeff):
 den=lcm(*(x.denominator if isinstance(x,F)else 1 for x in coeff));v=tuple(int(x*den)for x in coeff);g=gcd(*v)
 if not g:return
 v=tuple(x//g for x in v)
 if next(x for x in v if x)<0:v=tuple(-x for x in v)
 atoms.add(v)
def minus(a,b):return tuple(x-y for x,y in zip(a,b))
for ta,tb,tv,tc,tk in target:
 if tv!=(0,0):
  atom((0,1,0))
  if tc is not None:atom((-tc[0],1,-tc[1]))
 for sa,sb,sv,sc,sk in source:
  if sk>tk:continue
  delta=[(ta[z]-sa[z],tv[z],tb[z]-sb[z])for z in (0,1)]
  if sv==(0,0):
   for c in delta:atom(c)
  else:
   assert sv[0];modulus=lcm(modulus,abs(sv[0]));index=tuple(F(x,sv[0])for x in delta[0]);atom(index)
   if sc is not None:atom(minus(index,(sc[0],0,sc[1])))
   atom(minus(delta[1],tuple(sv[1]*x for x in index)))
   if sk==tk and tv!=(0,0):atom(minus(index,(0,1,0)))
lines={(F(-a,b),F(-c,b))for a,b,c in atoms if b};threshold=11
for a,b,c in atoms:
 if not b and a:threshold=max(threshold,floor(F(-c,a))+1)
for a,b in lines:
 for c,d in lines:
  if a>c:threshold=max(threshold,floor((2*modulus-b+d)/(a-c))+1)
period=lcm(modulus,*(modulus*a.denominator for a,b in lines))
assert all((a-c)*threshold+b-d>2*modulus for a,b in lines for c,d in lines if a>c)
assert (len(target),len(source),len(atoms),len(lines),threshold,modulus,period)==(743,759,212,153,46,2,4)
cases=[]
for n in range(11,threshold+period):
 tail=max(1,max(floor(a*n+b)for a,b in lines)+2*modulus+3);board=set(cap)
 for j in range(2,n+1):board.update((j*v[0]+b[0],j*v[1]+b[1])for v,b in arms)
 assert len(board)==7*n+2
 x=y=h=0;time=0
 for k,(word,count) in enumerate(sequence):
  c=tail if count is None else count[0]*n+count[1]
  for j in range(c):
   for phase,turn in enumerate(word):
    A,B,oldh=starts[k];fs=[f for f in reads if f[4]==k] if phase==0 and j==0 else fs
    aa,bb,v,cc,kk,pp=fs[phase];assert (x,y)==(aa[0]*n+bb[0]+v[0]*j,aa[1]*n+bb[1]+v[1]*j)
    assert ((x,y)in board)==(turn=='L'),(n,time,x,y,turn)
    board.symmetric_difference_update({(x,y)});h=(h+(1 if turn=='R'else -1))%4;dx,dy=vectors[h];x+=dx;y+=dy;time+=1
 assert (x,y,h)==(-n-13-2*tail,n+6-2*tail,3)
 assert time==22*n+3021+104*tail
 cases.append({'n':n,'tail_periods':tail,'updates':time})
author=json.loads((P/'affine_family_certificate.json').read_text());assert cases==author['cases']
result={'status':'PASS independent all-parameter affine arrangement and literal continuation','scope':'Every n>=11, including every future standard period; not arbitrary seeds','target_families':len(target),'source_families':len(source),'atoms':len(atoms),'lines':len(lines),'stable_threshold':threshold,'modulus':modulus,'period':period,'literal_reads':sum(c['updates']for c in cases),'cases':cases,'words_sha256':hashlib.sha256((P/'family_words.json').read_bytes()).hexdigest(),'capture_after_spiral':'22*n+3021','capture_from_initial_seed':'8*n*n+36*n+3021'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
