from pathlib import Path
from collections import defaultdict
import json,hashlib,sys,ctypes as C,math
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'stateful_growth_quadratic_2026-10-23'
sys.path.insert(0,str(ROOT/'sources/kehao95-core/defect_synthesis/verification/presburger_defects'))
from isl_exact import Context,Object,_bind,_P
isbounded=_bind('isl_set_is_bounded',[_P],C.c_int)
ctx=Context(max_operations=200000000)
def xy(z):return(int(z.real),int(z.imag))
def integ(w,h):
 p=0j;ev=[]
 for t in w:
  ev.append((p,h,t));h=(h+(1 if t=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
 return p,h,ev
def normalized(blocks,h):
 bs=[(w*b,0,1)if a==0 else(w,a,b)for w,a,b in blocks if a or b]
 assert bs and any(b for w,a,b in bs)
 def net(bs):
  hh=h;slope=0j;const=0j
  for w,a,b in bs:
   dp,nh,_=integ(w,hh);assert not a or nh==hh;slope+=a*dp;const+=b*dp;hh=nh
  assert hh==h;return slope,const
 d1,d0=net(bs);bundled=any(z%2 for z in xy(d1))
 if bundled:bs=[(w,2*a,b)for w,a,b in bs]+[(w,2*a,a+b)for w,a,b in bs];d1,d0=net(bs)
 A=d1/2;B=d0-A;assert all(int(v)==v for v in(A.real,A.imag,B.real,B.imag))
 families=[];slope=0j;const=0j;hh=h
 for b,(w,a,z)in enumerate(bs):
  dp,nh,ev=integ(w,hh)
  for r,(q,h0,t)in enumerate(ev):families.append(dict(block=b,phase=r,a=a,z=z,b=B+slope,c=dp,d=const+q,h=h0,t=t))
  slope+=a*dp;const+=z*dp;hh=nh
 return bs,A,B,bundled,families

def finiteK(A,fs):
 if not A:return None,None
 # A positive coordinate projection alone suffices; no author's optimized choice is used.
 axis=0 if A.real else 1;sgn=1 if xy(A)[axis]>0 else-1;ell=lambda z:sgn*xy(z)[axis];a=ell(A);low=[];up=[]
 for f in fs:
  b,c,d=map(ell,(f['b'],f['c'],f['d']));j0=(b,d);j1=(b+c*f['a'],d+c*(f['z']-1));low.append(j0 if c>=0 else j1);up.append(j1 if c>=0 else j0)
 L=min(x for x,y in low);l=min(y for x,y in low);U=max(x for x,y in up);u=max(y for x,y in up);gap=max(0,u-l)
 k=0;delta=1
 while True:
  coef=2*a*delta+L-U;val=a*delta*delta+L*delta-gap
  if coef<0 or val<=0:k=delta
  if coef>=0 and val>0 and a*(2*delta+1)+L>0:break
  delta+=1
 return k,dict(axis=axis,sign=sgn,a=a,L=L,l=l,U=U,u=u,K=k,cutoff=delta)
def union(objs):
 o=objs[0]
 for x in objs[1:]:o=o.union(x)
 return o.coalesce()
def compile_(A,fs,K):
 dm=[];left=[];letters=[];coords=[]
 for f in fs:
  b,r,a,z=f['block'],f['phase'],f['a'],f['z'];condition=f'n>=0 and b={b} and r={r} and 0<=j<{a}*n+{z}'
  dom=ctx.set('{[n,b,j,r]:'+condition+'}');dm.append(dom)
  if f['t']=='L':letters.append(dom)
  x,y=[f'{xy(f["b"])[v]}*n+{xy(f["c"])[v]}*j+{xy(f["d"])[v]}'for v in(0,1)]
  coords.append(ctx.map('{[n,b,j,r]->'+('[n,x,y]'if A else'[x,y]')+':'+condition+f' and x={x} and y={y}'+'}'))
 domain=union(dm);L=union(letters)if letters else ctx.set('{[n,b,j,r]:false}');mapping=union(coords)
 if not A:eq=mapping.apply_range(mapping.reverse())
 else:
  aa,bb=xy(A);pieces=[]
  for delta in range(-K,K+1):
   shift=ctx.map('{[m,x,y]->[n,z,w]:'+f'n=m-{delta} and z=x+{2*aa*delta}*m-{aa*delta*delta} and w=y+{2*bb*delta}*m-{bb*delta*delta}'+'}')
   pieces.append(mapping.apply_range(mapping.apply_range(shift).reverse()))
  eq=union(pieces)
 before=ctx.map('{[n,b,j,r]->[m,c,k,s]:m<n or(m=n and c<b)or(m=n and c=b and k<j)or(m=n and c=b and k=j and s<r)}');prior=eq.intersect(before).coalesce()
 # Delete pairs having an intermediate same-cell event, independently of lexmax.
 prev=prior.subtract(prior.apply_range(prior)).coalesce();assert prev.is_equal(prior.lexmax())
 LL=L;RR=domain.subtract(L)
 def diag(s):return ctx.map('{[n,b,j,r]->[n,b,j,r]}').intersect_domain(s) if False else Object(ctx,'map',_bind('isl_map_intersect_domain',[_P,_P])(ctx.map('{[n,b,j,r]->[n,b,j,r]}')._copy(),s._copy()))
 bad=diag(LL).apply_range(prev).apply_range(diag(LL)).union(diag(RR).apply_range(prev).apply_range(diag(RR))).coalesce()
 firstL=domain.subtract(prior.domain()).intersect(L).coalesce();return eq,prev,bad,firstL
std=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text());ref=json.loads((D/'quadratic_lap_validator.json').read_text());refby={r['name']:r for r in ref['records']}
programs=[('standard104_grouped',[(std['word'],1,1)],std['heading']),('infinite_prepared_axial_rail',[('LRRL',1,1)],1),('equal_L_boundary_conflict',[('LRRL',1,1),('LLLL',0,1)],1),('punctuated_prepared_rail',[('LRRL',1,1),('RRRR',0,1)],1),('affine_closed_square_conflict',[('RRRR',1,1)],0),('odd_displacement_bundling',[('RL',1,1)],0),('rotating_constant_stages',[('RL',1,0),('R',0,1),('RL',1,1),('RRR',0,1)],0)]
reports=[]
for name,blocks,h in programs:
 ctx.reset_operations();bs,A,B,bundled,fs=normalized(blocks,h);K,bound=finiteK(A,fs);eq,prev,bad,firstL=compile_(A,fs,K);bounded=isbounded(firstL.ptr);assert bounded>=0
 if name in refby:
  r=refby[name];assert xy(A)==tuple(r['A'])and xy(B)==tuple(r['B'])and bundled==r['bundled'];assert bad.is_equal(ctx.map(r['bad_relation']));assert firstL.is_equal(ctx.set(r['firstL_relation']));assert bad.is_empty()==r['alternating']and bool(bounded)==r['firstL_finite']
 lookup={(f['block'],f['phase']):f for f in fs};actual=[];p=0j;hh=h;by=defaultdict(list)
 for n in range(5):
  for b,(w,a,z)in enumerate(bs):
   for j in range(a*n+z):
    for r,t in enumerate(w):
     f=lookup[b,r];assert p==A*n*n+f['b']*n+f['c']*j+f['d']and hh==f['h'];e=(n,b,j,r);actual.append((e,p,t));by[p].append(e);hh=(hh+(1 if t=='R'else-1))%4;p+=(1j,1,-1j,-1)[hh]
 # One finite relation records ALL actual collisions at these complete five laps.
 pieces=[];previous=[];first=[];last={}
 for e,p,t in actual:
  if p in last:previous.append((e,last[p]))
  elif t=='L':first.append(e)
  last[p]=e
 for es in by.values():
  for e in es:
   for f in es:
    if K is not None:assert abs(e[0]-f[0])<=K
    pieces.append('['+','.join(map(str,e))+']->['+','.join(map(str,f))+']')
 finiteEq=ctx.map('{'+(';'.join(pieces))+'}');cut=ctx.map('{[n,b,j,r]->[m,c,k,s]:0<=n<5 and 0<=m<5}');assert eq.intersect(cut).is_equal(finiteEq)
 finiteprev=ctx.map('{'+(';'.join('['+','.join(map(str,e))+']->['+','.join(map(str,f))+']'for e,f in previous))+'}')if previous else ctx.map('{[n,b,j,r]->[m,c,k,s]:false}')
 assert prev.intersect(cut).is_equal(finiteprev)
 if name=='standard104_grouped':
  seed=sorted(xy(p)for e,p,t in actual if e in set(first));assert seed==sorted(map(tuple,std['seed']))
  finitefirst=ctx.set('{'+(';'.join('['+','.join(map(str,e))+']'for e in first))+'}');assert firstL.is_equal(finitefirst)
 reports.append(dict(name=name,A=xy(A),B=xy(B),bundled=bundled,bound=bound,alternating=bad.is_empty(),firstL_finite=bool(bounded),literal_reads=len(actual),all_five_lap_samecell_pairs=len(pieces)))
 print(name,'PASS',flush=True)
out=dict(status='PASS independent quadratic-lap collision compiler and exact previous-event finite-seed criteria',programs=reports,source_note_sha256=hashlib.sha256((D/'quadratic_lap_finite_seed_decision.md').read_bytes()).hexdigest(),author_code_sha256=hashlib.sha256((D/'quadratic_lap_validator.py').read_bytes()).hexdigest(),analytic='For positive projection ell(A), scalar quadratic separation gives a computable all-history K. Fixed delta cancels n^2 exactly; augmented-coordinate translation compiler independently agrees with every saved exact FirstL/Bad relation. Previous was computed by subtracting pairs with an intermediate same-cell event, not author lexmax, and crosschecked. Finite first-L event set iff a common finite seed exists under exact alternation. A=0 uses existing affine Presburger relations. Fixed104 successor query is decidable analytically but NOT executed here. Variable nonzero-copy-drift L phases require positive-width prior-R parallel resonance; transverse matches are only O(N), nonresonant parallel matches occupy finitely many laps, zero-drift repeated pose words cannot repeat legally twice.',scope='Supplied affine-count literal lap programs only, including genuine quadratic starts and constant rotating stages. No successful nonstandard finite-seed model, generic arbitrary-period decision, global capture proof or wider literature claim.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
