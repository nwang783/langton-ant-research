from pathlib import Path
from collections import defaultdict
import json,hashlib
P=Path(__file__).resolve();ROOT=P.parent.parent;R=ROOT/'nonlinear_global_budget_2026-10-23';dirs=(1j,1,-1j,-1)
def xy(z):return(int(z.real),int(z.imag))
def shift(A,d):return{z+d for z in A}
def run(A,p,h,n,reads=False):
 A=set(A);history=[];turns=[]
 for _ in range(n):
  history.append(p);c='L'if p in A else'R';turns.append(c);A.symmetric_difference_update({p});h=(h+(-1 if c=='L'else 1))%4;p+=dirs[h]
 return A,p,h,history,''.join(turns)
entry_board,p,h,_,_=run(set(),0j,0,9977);_,q,hh,S,H=run(entry_board,p,h,104);d=q-p;assert d==-2-2j and hh==h
base=entry_board&set(S);base1,_,_,_,_=run(base,p,h,104);W=base1^shift(base,d);head=p-2-8j
stable,r,rh,A,anchor_word=run(base|{head+11*d},p,h,52262);after,rr,hh,Q,reverse_word=run(stable,r,rh,104)
assert rr-r==-d and hh==rh and reverse_word==H and H.count('R')-H.count('L')==12
V=after^shift(stable,-d);Lraw=W^shift(V,d);L=shift(Lraw,4*d)
groups=defaultdict(set)
for z in L:
 x,y=xy(z);a=x%2;t=x-y;k=(a-x)//2;groups[t,a].add(k)
odd=set();cap=set();profile=[]
for(t,a),ks in sorted(groups.items()):
 k0=min(ks);isodd=len(ks)%2
 if isodd:odd.add(complex(a-2*k0,a-t-2*k0))
 remainder=ks^({k0}if isodd else set());parity=False
 if remainder:
  for k in range(min(remainder),max(remainder)):
   parity^=k in remainder
   if parity:cap.add(complex(a-2*k,a-t-2*k))
 profile.append(dict(t=t,x_parity=a,L_cells=len(ks),odd=isodd,min_k=min(ks),max_k=max(ks)))
assert L==odd^cap^shift(cap,d) and(len(W),len(V),len(L),len(odd),len(cap))==(12,2436,2438,24,2189)
author=json.loads((R/'compute_exceptional_layer.json').read_text())
for name,data in [('W',W),('V',V),('L',L),('P',odd),('C',cap)]:assert sorted(map(xy,data))==list(map(tuple,author[name]))
assert profile==author['profiles']
for n in(0,1,2,5,17,80):
 layers=set();strings=set()
 for i in range(n):layers^=shift(L,i*d);strings^=shift(odd,i*d)
 assert len(strings)==24*n and layers==strings^cap^shift(cap,n*d)
# A separate full-field arbitrary-base control with three retained old archive bits.
DX={r+k*d for k in(5,8,20)}
def index(a,b):
 z=(a-b)/d
 return int(z.real)if z.imag==0 and z.real.is_integer()else None
assert all((i:=index(a,s))is None or i<0 for a in DX for s in S)
forbidden=[i for a in DX for s in set(A)|set(Q)if(i:=index(a,s))is not None and i>=0]
K=1+max(forbidden,default=-1);AX=DX^shift(stable,K*d)
for i in range(K):AX^=shift(W,i*d)
assert K==22 and len(AX)==2483
controls=[]
for n in(0,1,2,5,20):
 initial=base|DX|{head+(11+K+n)*d};elapsed=52262+104*K+208*n
 actual,pos,heading,_,word=run(initial,p,h,elapsed);predicted=AX.copy()
 for i in range(n):predicted^=shift(Lraw,(K+i)*d)
 assert actual==predicted and(pos,heading)==(r+K*d,rh)and len(actual)==len(AX)+24*n
 assert word==H*(K+n)+anchor_word+reverse_word*n
 controls.append(dict(n=n,initial_mass=len(initial),elapsed=elapsed,return_mass=len(actual),preceding_ten=word[-10:]))
other=json.loads((R/'check_arbitrary_base_return_map.json').read_text());assert controls==other['complete_field_controls']
out=dict(status='PASS independent complete exceptional masks, orbit coboundary and physical return controls',source_sha256=hashlib.sha256((R/'exceptional_arbitrary_base_return_map.md').read_bytes()).hexdigest(),W_mass=len(W),V_mass=len(V),L_mass=len(L),nonzero_drift_orbits=len(odd),finite_cap_mass=len(cap),orbit_profile=profile,safe_section_K=K,controls=controls,scope='All-n normal form uses retained pristine whole-stream/wake guards plus finite arbitrary-base ray separation, independently reviewed analytically. Full reverse passive field retained;24 persistent strings are not bounded-endcap coboundary. Physical mass grows24n while variable clean standard flights contribute no bulk defects. No post-section capture, fixed-mass defect divergence, arbitrary renewal or original-fuel descent.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in('orbit_profile','controls')})
