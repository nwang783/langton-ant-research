#!/usr/bin/env python3
"""Exact first-read validator for affine-count laps with quadratic start positions.
No candidate-search loop. Errors/resource exhaustion raise, never mean impossibility.
"""
from pathlib import Path
from dataclasses import dataclass
import sys, json, ctypes as C, time, hashlib, math
ROOT=Path('/workspace/shared/langton')
sys.path.insert(0,str(ROOT/'sources/kehao95-core/defect_synthesis/verification/presburger_defects'))
from isl_exact import Context,Object,_FUN,_bind,_P,_libc

D=((0,1),(1,0),(0,-1),(-1,0))
_bind_bounded=_bind('isl_set_is_bounded',[_P],C.c_int)
_intersect_range=_bind('isl_map_intersect_range',[_P,_P])
_intersect_domain=_bind('isl_map_intersect_domain',[_P,_P])
_cb=C.CFUNCTYPE(C.c_int,_P,_P)
_foreach_point=_bind('isl_set_foreach_point',[_P,_cb,_P],C.c_int)
_point_coord=_bind('isl_point_get_coordinate_val',[_P,C.c_int,C.c_int])
_point_free=_bind('isl_point_free',[_P],None)
_val_str=_bind('isl_val_to_str',[_P]); _val_free=_bind('isl_val_free',[_P],None)

def add(u,v): return tuple(a+b for a,b in zip(u,v))
def scale(a,v): return tuple(a*b for b in v)
def dot(u,v): return sum(a*b for a,b in zip(u,v))
def lin(a,b=0,var='n'): return f'({a}*{var}+{b})'
def inter(map_,set_,side):
 fn=_intersect_domain if side=='domain' else _intersect_range
 return Object(map_.ctx,'map',fn(map_._copy(),set_._copy()))
def bounded(s):
 result=_bind_bounded(s.ptr)
 if result<0:s.ctx.fail()
 return bool(result)
def points(s,limit=100000):
 result=[];errors=[]
 @_cb
 def cb(p,user):
  try:
   row=[]
   for i in range(4):
    v=_point_coord(p,3,i)
    if not v: s.ctx.fail()
    z=_val_str(v)
    if not z:s.ctx.fail()
    try: row.append(int(C.string_at(z).decode()))
    finally:_libc.free(z);_val_free(v)
   result.append(tuple(row))
   if len(result)>limit:raise OverflowError('finite first-read set exceeds extraction limit')
   return 0
  except BaseException as e:errors.append(e);return -1
  finally:_point_free(p)
 r=_foreach_point(s.ptr,cb,None)
 if errors:raise errors[0]
 if r<0:s.ctx.fail()
 return sorted(result)

@dataclass
class Family:
 block:int; phase:int; alpha:int; beta:int; b:tuple; c:tuple; d:tuple; turn:str; heading:int
 def dom(self,n='n',b='b',j='j',r='r'):
  return f'{n}>=0 and {b}={self.block} and {r}={self.phase} and 0<={j}<{self.alpha}*{n}+{self.beta}'

class Program:
 def __init__(self,blocks,heading=0,name='unnamed'):
  # blocks [(literal word,alpha,beta)]; counts alpha*n+beta are nonnegative.
  self.name=name;self.heading=heading;self.blocks=[]
  for word,a,b in blocks:
   assert word and set(word)<=set('LR') and a>=0 and b>=0
   if a==0:
    if b:self.blocks.append((word*b,0,1))
   else:
    assert (word.count('R')-word.count('L'))%4==0, 'variable-count word must restore heading'
    self.blocks.append((word,a,b))
  assert self.blocks and any(b for w,a,b in self.blocks),'each lap must be nonempty'
  d1,d0,h=self._net(self.blocks)
  assert h==heading,'the complete lap must restore its actual heading'
  self.bundled=False
  if any(v%2 for v in d1):
   self.blocks=[(w,2*a,b)for w,a,b in self.blocks]+[(w,2*a,a+b)for w,a,b in self.blocks]
   self.bundled=True;d1,d0,h=self._net(self.blocks)
  self.A=tuple(v//2 for v in d1)
  self.B=tuple(d0[i]-self.A[i]for i in (0,1))
  assert all(2*self.A[i]==d1[i]for i in (0,1))
  self.families=[];pos1=(0,0);pos0=(0,0);h=heading
  for b,(word,alpha,beta)in enumerate(self.blocks):
   p=(0,0);local=[];hh=h
   for r,t in enumerate(word):
    local.append((p,hh,t));hh=(hh+(1 if t=='R'else-1))%4;p=add(p,D[hh])
   assert alpha==0 or hh==h
   for r,(q,hh0,t)in enumerate(local):
    self.families.append(Family(b,r,alpha,beta,add(self.B,pos1),p,add(pos0,q),t,hh0))
   pos1=add(pos1,scale(alpha,p));pos0=add(pos0,scale(beta,p));h=hh
  assert pos1==d1 and pos0==d0 and h==heading
  self._by={(f.block,f.phase):f for f in self.families}
  self.bound=self.collision_bound()
 def _net(self,blocks):
  h=self.heading;p1=(0,0);p0=(0,0)
  for w,a,b in blocks:
   p=(0,0);hh=h
   for t in w:hh=(hh+(1 if t=='R'else-1))%4;p=add(p,D[hh])
   assert not a or hh==h
   p1=add(p1,scale(a,p));p0=add(p0,scale(b,p));h=hh
  return p1,p0,h
 def pose(self,e):
  n,b,j,r=e;f=self._by[b,r]
  return tuple(self.A[i]*n*n+f.b[i]*n+f.c[i]*j+f.d[i]for i in(0,1)),f.heading
 def literal(self,N):
  p=(0,0);h=self.heading;out=[]
  for n in range(N):
   for b,(word,a,c)in enumerate(self.blocks):
    for j in range(a*n+c):
     for r,t in enumerate(word):
      e=(n,b,j,r);assert self.pose(e)==(p,h)
      out.append((e,p,h,t));h=(h+(1 if t=='R'else-1))%4;p=add(p,D[h])
  return out
 def collision_bound(self):
  if self.A==(0,0):return dict(kind='affine',K=None)
  candidates=[]
  ells=[]
  for i in (0,1):
   if self.A[i]:ells.append(tuple((1 if self.A[i]>0 else-1)if i==j else 0 for j in(0,1)))
  g=math.gcd(abs(self.A[0]),abs(self.A[1]));ells.append(tuple(v//g for v in self.A))
  for ell in set(ells):
   a=dot(ell,self.A);lows=[];ups=[]
   for f in self.families:
    b,c,d=dot(ell,f.b),dot(ell,f.c),dot(ell,f.d)
    endpoints=[(b,d),(b+c*f.alpha,d+c*(f.beta-1))]
    # The affine endpoint gives the exact min/max whenever this block is nonempty.
    lows.append(endpoints[0]if c>=0 else endpoints[1]);ups.append(endpoints[1]if c>=0 else endpoints[0])
   L=min(x for x,y in lows);l=min(y for x,y in lows)
   U=max(x for x,y in ups);u=max(y for x,y in ups);gap=max(0,u-l)
   delta=1;K=0
   while True:
    coeff=2*a*delta+L-U;constant=a*delta*delta+L*delta-gap
    if coeff<0 or constant<=0:K=delta
    if coeff>=0 and constant>0 and a*(2*delta+1)+L>0:break
    delta+=1
   candidates.append(dict(ell=ell,a=a,L=L,l=l,U=U,u=u,gap=gap,K=K,first_permanent_exclusion=delta))
  best=min(candidates,key=lambda z:z['K'])
  return dict(kind='quadratic',K=best['K'],best=best,candidates=candidates)
 def compile(self,ctx):
  empty=ctx.set('{[n,b,j,r]:false}');domain=empty;left=None;L=empty
  for f in self.families:
   dom=f.dom();s=ctx.set('{[n,b,j,r]:'+dom+'}')
   domain=domain.union(s)
   if f.turn=='L':L=L.union(s)
   X=f'{f.b[0]}*n+{f.c[0]}*j+{f.d[0]}'
   Y=f'{f.b[1]}*n+{f.c[1]}*j+{f.d[1]}'
   target='[n,X,Y]'if self.A!=(0,0)else'[X,Y]'
   q=ctx.map('{[n,b,j,r]->'+target+':'+dom+f' and X={X} and Y={Y}'+'}')
   left=q if left is None else left.union(q)
  left=left.coalesce();domain=domain.coalesce();L=L.coalesce()
  if self.A==(0,0):eq=left.apply_range(left.reverse()).coalesce()
  else:
   eq=None
   for delta in range(-self.bound['K'],self.bound['K']+1):
    right=None
    for f in self.families:
     X=f'{2*self.A[0]*delta+f.b[0]}*m+{f.c[0]}*k+{f.d[0]-self.A[0]*delta*delta}'
     Y=f'{2*self.A[1]*delta+f.b[1]}*m+{f.c[1]}*k+{f.d[1]-self.A[1]*delta*delta}'
     q=ctx.map('{[m,c,k,s]->[n,X,Y]:'+f.dom('m','c','k','s')+f' and n=m-{delta} and X={X} and Y={Y}'+'}')
     right=q if right is None else right.union(q)
    chunk=left.apply_range(right.coalesce().reverse())
    eq=chunk if eq is None else eq.union(chunk)
   eq=eq.coalesce()
  before=ctx.map('{[n,b,j,r]->[m,c,k,s]:m<n or(m=n and c<b)or(m=n and c=b and k<j)or(m=n and c=b and k=j and s<r)}')
  prior=eq.intersect(before).coalesce();previous=prior.lexmax().coalesce()
  R=domain.subtract(L).coalesce()
  bad=inter(inter(previous,L,'domain'),L,'range').union(inter(inter(previous,R,'domain'),R,'range')).coalesce()
  first=domain.subtract(prior.domain()).coalesce();firstL=first.intersect(L).coalesce()
  return dict(domain=domain,L=L,equality=eq,previous=previous,bad=bad,firstL=firstL)

def run_controls():
 t0=time.monotonic();ctx=Context(max_operations=200000000);out=[]
 std=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())
 programs=[Program([(std['word'],1,1)],std['heading'],'standard104_grouped'),
   Program([('LRRL',1,1)],1,'infinite_prepared_axial_rail'),
   Program([('LRRL',1,1),('LLLL',0,1)],1,'equal_L_boundary_conflict'),
   Program([('LRRL',1,1),('RRRR',0,1)],1,'punctuated_prepared_rail'),
   Program([('RRRR',1,1)],0,'affine_closed_square_conflict')]
 for P in programs:
  ctx.reset_operations();compiled=P.compile(ctx)
  valid_alt=compiled['bad'].is_empty();finite=bounded(compiled['firstL'])
  first_events=points(compiled['firstL'])if finite else None
  seed=sorted({P.pose(e)[0]for e in first_events})if finite else None
  print(P.name,'EXACT alt',valid_alt,'finite',finite,'K',P.bound['K'],flush=True)
  literal=P.literal(4);reads={};pair_checks=0;literal_bad=[];literal_first=[]
  for e,p,h,t in literal:
   if p in reads:
    prev,pt=reads[p]
    if pt==t:literal_bad.append((e,prev))
   elif t=='L':literal_first.append(e)
   reads[p]=(e,t)
  # Exact relation evaluated against every observed cell's full pair inventory,
  # plus all nearby-time noncolliding event pairs in the finite control window.
  bycell={}
  for e,p,h,t in literal:bycell.setdefault(p,[]).append(e)
  collision_checks=0
  for es in bycell.values():
   for e in es:
    for f in es:
     if P.bound['K']is not None:assert abs(e[0]-f[0])<=P.bound['K']
     ctx.reset_operations()
     point=ctx.map('{[n,b,j,r]->[m,c,k,s]:'+ ' and '.join(f'{v}={a}'for v,a in zip(('n','b','j','r','m','c','k','s'),e+f))+'}')
     assert not compiled['equality'].intersect(point).is_empty();collision_checks+=1
  for index,(e,p,h,t)in enumerate(literal):
   for index2 in range(max(0,index-3),min(len(literal),index+4)):
    f,q,hh,tt=literal[index2]
    ctx.reset_operations()
    point=ctx.map('{[n,b,j,r]->[m,c,k,s]:'+ ' and '.join(f'{v}={a}'for v,a in zip(('n','b','j','r','m','c','k','s'),e+f))+'}')
    assert (not compiled['equality'].intersect(point).is_empty())==(p==q);pair_checks+=1
  record=dict(name=P.name,A=P.A,B=P.B,bundled=P.bundled,collision_bound=P.bound,
    alternating=valid_alt,firstL_finite=finite,firstL_relation=str(compiled['firstL']),
    bad_relation=str(compiled['bad']),minimal_seed=seed,firstL_events=first_events,
    control_laps=4,control_reads=len(literal),literal_colliding_pair_checks=collision_checks,
    literal_nearby_pair_checks=pair_checks)
  if P.name=='standard104_grouped':
   assert valid_alt and finite and seed==sorted(map(tuple,std['seed']))
  elif P.name=='infinite_prepared_axial_rail':assert valid_alt and not finite
  elif P.name=='equal_L_boundary_conflict':assert not valid_alt
  elif P.name=='affine_closed_square_conflict':assert not valid_alt
  out.append(record);print(P.name,'alt',valid_alt,'finite',finite,'K',P.bound['K'],flush=True)
 result=dict(status='EXACT ALL-LAP CHRONOLOGY AND FINITE-SUPPLY CONTROLS',records=out,
   libisl_version=ctx.version,seconds=time.monotonic()-t0,
   source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
   standard_sha256=hashlib.sha256((ROOT/'recovered_bundle/ant_global/root/standard.json').read_bytes()).hexdigest(),
   scope='No growing nonstandard finite-seed model. Complete inverse criterion uses all same-cell reads; retired garbage stays on board. Literal checks control compiler conventions, not the all-lap proof.')
 Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items()if k!='records'},indent=2))
if __name__=='__main__':run_controls()
