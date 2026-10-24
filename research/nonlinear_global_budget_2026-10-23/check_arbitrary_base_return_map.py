#!/usr/bin/env python3
"""Whole-field literal controls for the analytic arbitrary-base return map."""
import contextlib,io,json,runpy
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
 g=runpy.run_path(str(Path(__file__).with_name('compute_exceptional_layer.py')))
run,step,shift=g['run'],g['step'],g['shift']
base,entry,eh,d=g['base'],g['entry'],g['eh'],g['d']
R,r,rh,W,V=g['R'],g['r'],g['rh'],g['W'],g['V']
L=W^shift(V,d);head=g['head'];a=52262
# A capturing base with three old, genuinely active-on-return bits.
DX={tuple(r[j]+k*d[j]for j in range(2))for k in[5,8,20]}
assert not base&DX
S=g['S'];Q=[];p=r;h=rh;bb=set(R)
for _ in range(104):Q.append(p);p,h=step(bb,p,h)
A=set();p=entry;h=eh;bb=base|{tuple(head[j]+11*d[j]for j in range(2))}
for _ in range(a):A.add(p);p,h=step(bb,p,h)
assert p==r and h==rh and bb==R

def ray_index(q,s):
 ks=[]
 for v,w in zip((q[0]-s[0],q[1]-s[1]),d):
  if w==0:
   if v:return None
  else:
   if v%w:return None
   ks.append(v//w)
 return ks[0]if ks and len(set(ks))==1 else None
# DX misses all future incoming reads, so base|DX is already certified H forever.
assert all((k:=ray_index(q,s))is None or k<0 for q in DX for s in S)
forbidden=[k for q in DX for s in A|set(Q)if(k:=ray_index(q,s))is not None and k>=0]
K=1+max(forbidden,default=-1)
WX=set()
for i in range(K):WX^=shift(W,d,i)
AX=DX^shift(R,d,K)^WX
controls=[];suffixes=set()
for n in[0,1,2,5,20]:
 obs=tuple(head[j]+(11+K+n)*d[j]for j in range(2))
 initial=base|DX|{obs};p=entry;h=eh;bb=set(initial);turns=''
 elapsed=a+104*K+208*n
 for t in range(elapsed):
  ch='L'if p in bb else'R';turns=(turns+ch)[-10:];p,h=step(bb,p,h)
 layers=set()
 for i in range(n):layers^=shift(L,d,K+i)
 predicted=AX^layers
 assert bb==predicted and p==tuple(r[j]+K*d[j]for j in range(2))and h==rh
 if n>=1:suffixes.add(turns)
 controls.append({'n':n,'initial_mass':len(initial),'elapsed':elapsed,'return_mass':len(bb),'preceding_ten':turns})
assert len(suffixes)==1
out={'status':'PASS','K':K,'base_mass':len(base|DX),'base_is_standard_from_time_zero':True,
     'retained_old_archive_bits':sorted(DX),'fixed_return_pose':[list(p),h],
     'fixed_AX_mass':len(AX),'complete_field_controls':controls,
     'scope':'Finite continuous-cursor whole-board controls for the analytic all-n return map, not a post-section capture claim.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
