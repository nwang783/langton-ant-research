"""Exact all-n complete finite fields for the nonstandard prepared108 rewriter.
Independent complex-coordinate trace and finite orbit-boundary argument.
Not a finite-support infinite trajectory or a standard-wake consumer.
"""
from pathlib import Path
import json,collections,hashlib
P=Path(__file__).resolve().parent
z=json.loads((P/'reverse108_prepared_control.json').read_text());w=z['word'];assert len(w)==108
q=6j;h=-1+0j;orbits=collections.defaultdict(list)
for t,c in enumerate(w):
 x,y=int(q.real),int(q.imag);a=(x-y,x%2);l=-(x//2)
 orbits[a].append((l,t,c))
 h*=(-1j if c=='R'else 1j);q+=h
assert q==-2+4j and h==-1

def history(L,n,k):
 return sorted([(t-108*l,c,l,t)for l,t,c in L if 0<=k-l<n])
def bits(hist):
 assert hist
 assert all(a[1]!=b[1]for a,b in zip(hist,hist[1:])),hist
 return[int(hist[0][1]=='L'),int(hist[-1][1]=='R'),1,len(hist)%2]
maxwidth=0;tables=[];coef=[0]*4;intercept=[0]*4
for a,L in sorted(orbits.items()):
 lo=min(l for l,t,c in L);hi=max(l for l,t,c in L);W=hi-lo;maxwidth=max(maxwidth,W)
 n=W+1;stable=bits(sorted((t-108*l,c,l,t)for l,t,c in L));left=[];right=[]
 for k in range(lo,hi):left.append((k,bits(history(L,n,k))))
 for s in range(lo,hi):right.append((s,bits(history(L,n,n+s))))
 for j in range(4):coef[j]+=stable[j];intercept[j]+=sum(b[j]for k,b in left+right)-W*stable[j]
 tables.append(dict(orbit=a,representative=[a[1],a[1]-a[0]],events=sorted(L),min_offset=lo,max_offset=hi,width=W,stable_bits=stable,left_boundary_bits=left,right_boundary_bits=right))
assert coef==[11,3,23,12] and intercept==[13,13,19,20]
controls=[]
for n in range(1,maxwidth+2):
 total=[0]*4
 for a,L in orbits.items():
  lo=min(l for l,t,c in L);hi=max(l for l,t,c in L)
  for k in range(lo,hi+n):
   r=history(L,n,k)
   if r:
    b=bits(r)
    for j in range(4):total[j]+=b[j]
 assert total==[coef[j]*n+intercept[j]for j in range(4)]
 controls.append(dict(n=n,counts=total))
out=dict(scope=__doc__,word=w,period=108,start=[0,6,'W'],displacement=[-2,-2],field_order=['input_black','output_black','read_support','complete_XOR'],counts_affine=dict(slope=coef,intercept=intercept),valid_for='all integers n>=1',maximum_orbit_width=maxwidth,small_n_complete_controls=controls,orbit_tables=tables,field_formula='For orbit representative a and cell a+k*(-2,-2), retain event(l,t,c) iff 0<=k-l<n; sort by t-108*l. Input black iff first c=L, output black iff last c=R, XOR iff event count odd.',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'reverse108_prepared_family.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in('orbit_tables','word')})
