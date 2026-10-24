"""Exact local ordinal proof and full-strip event separator for RRLL b cycles.
Complete WHITE cap four. No period, drift, width, support or length scan.
A b edge is the FIRST R departure, not necessarily a target's first read.
"""
from pathlib import Path
from itertools import product
import json
H='NESW'; V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
def out(h,r): return H[(H.index(h[r])+(1 if r%2==0 else -1))%4]
def ranks(h,dr,kind): return [r for r in range(len(h)) if (h[r] if kind=='in' else out(h,r))==dr]
def alphabet(first,cycle_in,cycle_out,left=False):
 ans=[]
 axis='NS' if first in 'NS' else 'EW'
 for n in range(1,5):
  for tail in product(axis,repeat=n-1):
   h=first+''.join(tail)
   if left and (n<3 or h[2]!=cycle_in): continue
   if len(ranks(h,cycle_in,'in'))==len(ranks(h,cycle_out,'out'))==2: ans.append(h)
 return ans
A={
 'Z':alphabet('N','S','E',True),
 'A':alphabet('E','E','S'),
 'B':alphabet('S','S','W'),
 'Y':alphabet('E','W','S',True)}
assert A=={'Z':['NSS','NNSS','NSSN'],'A':['EEWW','EWWE'],'B':['SNNS','SSNN'],'Y':['EWW','EEWW','EWWE']},A
# First ordinal around the physical C square F_k, not around the b cycle:
# Z_k -> A_k -> B_(k-1) -> Y_(k-1) -> Z_k.
F_dirs=[('Z','A','E'),('A','B','S'),('B','Y','W'),('Y','Z','N')]
def loop_terms(hs,edges,ordinal):
 incoming={}; outgoing={}
 for u,v,dr in edges:
  sr=ranks(hs[u],dr,'out');tr=ranks(hs[v],dr,'in')
  if len(sr)!=len(tr) or len(sr)<=ordinal: return None
  outgoing[u]=sr[ordinal];incoming[v]=tr[ordinal]
 return {u:(incoming[u],outgoing[u]) for u in hs}
F_rows=[]
for z,a,b,y in product(A['Z'],A['A'],A['B'],A['Y']):
 hs=dict(Z=z,A=a,B=b,Y=y);terms=loop_terms(hs,F_dirs,0)
 if terms is None: continue
 nonzero={u:rr for u,rr in terms.items() if rr[0]!=rr[1]}
 assert nonzero==({'Y':(2,1)} if y=='EEWW' else {'Y':(1,2)}),(hs,terms)
 # The loop's exact clock sum is 4 + sum(Tout-Tin) = 0.
 if y!='EEWW': verdict='positive four-step clock cycle'
 elif z=='NSSN':
  # Y outgoing N at ranks1,2 feeds Z incoming N at ranks0,3.
  assert ranks(y,'N','out')==[1,2] and ranks(z,'N','in')==[0,3]
  verdict='T3(Z)-T0(Z)=Delta12(Y)=4, but at least12'
 else:
  assert z=='NNSS';verdict='necessary survivor: Delta12(Y)=4 and T1(Z)-T0(Z)=4'
 F_rows.append(dict(histories=hs,first_ordinal_pairs=terms,verdict=verdict))
F_surv=[r for r in F_rows if r['verdict'].startswith('necessary survivor')]
assert len(F_rows)==20 and len(F_surv)==4
# Second ordinal around the physical L square Q_k:
# Z_k -> A_k -> B_k -> Y_k -> Z_k.
Q_dirs=[('Z','A','E'),('A','B','N'),('B','Y','W'),('Y','Z','S')]
Q_rows=[]
for a,b in product(A['A'],A['B']):
 hs=dict(Z='NNSS',A=a,B=b,Y='EEWW');terms=loop_terms(hs,Q_dirs,1);assert terms
 nz={u:rr for u,rr in terms.items() if rr[0]!=rr[1]}
 expected={}
 if a=='EEWW':expected['A']=(1,2)
 if b=='SNNS':expected['B']=(2,1)
 assert nz==expected,(hs,terms)
 if b!='SNNS':verdict='positive four-step clock cycle'
 elif a=='EEWW':
  assert ranks(a,'N','out')==ranks(b,'N','in')==[1,2]
  verdict='Delta12(B)=4+Delta12(A), but ordinal edges give equality'
 else:verdict='unique necessary survivor: Delta12(B)=4 and Delta23(A)=4'
 Q_rows.append(dict(histories=hs,second_ordinal_pairs=terms,verdict=verdict))
assert len([r for r in Q_rows if r['verdict'].startswith('unique')])==1
forced={'Z':'NNSS','A':'EWWE','B':'SNNS','Y':'EEWW'}
# Symbolic physical cell coordinates and all ranks' event-side labels.
def pos(role,k):return {'Z':(0,2*k),'A':(1,2*k),'B':(1,2*k+1),'Y':(0,2*k+1)}[role]
def decode(p):
 x,y=p;k=y//2
 if x==0:return ('Z' if y%2==0 else 'Y',k)
 if x==1:return ('A' if y%2==0 else 'B',k)
 return None
def label(role,r):return ('WEST' if r<3 else 'EAST') if role in 'ZY' else ('WEST' if r==0 else 'EAST')
all_internal=[];all_open_in=[];all_open_out=[]
for role,h in forced.items():
 p=pos(role,0)
 for dr in H:
  q=(p[0]+V[dr][0],p[1]+V[dr][1]);dec=decode(q)
  sr=ranks(h,dr,'out')
  if dec:
   v,k=dec;tr=ranks(forced[v],dr,'in');assert len(sr)==len(tr)
   for ordinal,(r,s) in enumerate(zip(sr,tr),1):
    assert label(role,r)==label(v,s)
    all_internal.append(dict(source=[role,0,r],target=[v,k,s],heading=dr,ordinal=ordinal,side=label(role,r)))
  else:
   for ordinal,r in enumerate(sr,1):
    side='WEST' if q[0]<0 else 'EAST';assert label(role,r)==side
    all_open_out.append(dict(source=[role,0,r],target=q,heading=dr,ordinal=ordinal,side=side))
  src=(p[0]-V[dr][0],p[1]-V[dr][1]);dec=decode(src)
  if not dec:
   for ordinal,r in enumerate(ranks(h,dr,'in'),1):
    side='WEST' if src[0]<0 else 'EAST';assert label(role,r)==side
    all_open_in.append(dict(source=src,target=[role,0,r],heading=dr,ordinal=ordinal,side=side))
assert len(all_internal)==12 and len(all_open_in)==len(all_open_out)==4
# Trace every exterior ingress until the next exterior egress.
succ={(tuple(e['source'])):e for e in all_internal}
channels=[]
for e in all_open_in:
 role,k,r=e['target'];cur=(role,k,r);route=[];side=e['side']
 for step in range(1,20):
  u,j,s=cur;route.append([u,j,s]);p=pos(u,j);dr=out(forced[u],s)
  q=(p[0]+V[dr][0],p[1]+V[dr][1]);dec=decode(q)
  if dec is None:
   assert ('WEST' if q[0]<0 else 'EAST')==side
   channels.append(dict(ingress=e,route=route,external_egress=q,egress_heading=dr,steps=len(route)+1,side=side));break
  v,l=dec;oo=ranks(forced[u],dr,'out').index(s);tr=ranks(forced[v],dr,'in');cur=(v,l,tr[oo])
 else:raise AssertionError('unexpected closed internal chain')
assert sorted(c['steps']for c in channels)==[3,3,7,7]
obj=dict(scope=__doc__,complete_constant_flow2_alphabets=A,F_first_ordinal_rows=F_rows,Q_second_ordinal_rows=Q_rows,forced_histories=forced,event_side_labels={u:[label(u,r)for r in range(4)]for u in forced},all_internal_symbolic_ordinal_edges=all_internal,all_external_ingresses=all_open_in,all_external_egresses=all_open_out,complete_actual_channels=channels,conclusion='A closed RRLL constant-flow2 b circle would exhaust the full two-column strip. Every actual event successor preserves WEST/EAST, including every exterior port. The full drift is vertical and preserves the labels, contradicting one actual P-event cycle. Finite segments can bypass the endpoints; general one-use remains open.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n')
print('PASS: 20 F rows -> 4; 4 Q rows -> 1; 12 internal ordinal edges and 8 exterior ports; channels3,3,7,7')
