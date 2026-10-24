"""Eight independent heading/turn images; bounded CHECKPOINT charge fuel API.
State order N-R,N-L,E-R,E-L,S-R,S-L,W-R,W-L. Words use base incoming N.
"""
import math
from fourier_transfer import *
from positive_moments import negative_divergence

def validate_state_images(images,a,root=0):
 assert len(images)==8 and root in range(8)
 for state,w in enumerate(images):
  assert w and set(w)<=set('RL')
  sign=1 if state%2==0 else -1
  _,p,h=image_data(w)
  assert h==sign%4 and p==rotate((sign,0),a)
  # Per-image signed charge need not equal the parent sign.
 F=[2*(s//2)+(0 if w[0]=='R' else 1) for s,w in enumerate(images)]
 seq=[];s=root
 while s not in seq:seq.append(s);s=F[s]
 assert s==root,'selected root is not on a first-state cycle'
 period=len(seq)
 # Nonerasing: this cycle grows iff some cycle image has length>1.
 assert any(len(images[s])>1 for s in seq),'selected root does not generate an infinite limit'
 unit_period=next(r for r in range(1,5) if a*r%4==0)
 return dict(root_period=period,unit_period=unit_period,group_period=math.lcm(period,unit_period),root_cycle=seq)

def cyclotomic_matrices(images,a,q,u,v,root=0):
 info=validate_state_images(images,a,root);d,powers=cyclotomic_ring(q);D=8*d;mats=[]
 for phase in range(info['group_period']):
  M=[[0]*D for _ in range(D)]
  for state,w in enumerate(images):
   h=state//2
   for p,hj,sj in image_data(w)[0]:
    p=rotate(p,a*phase-h);child=2*((h+hj)%4)+sj;e=(u*p[0]+v*p[1])%q
    for b in range(d):
     for c,z in enumerate(powers[(e+b)%q]):M[state*d+c][child*d+b]+=z
  mats.append(M)
 initial=[0]*D
 for s in range(8):initial[s*d]=1 if s%2==0 else -1
 return info,d,mats,initial

def positive_matrices(images,a,x,y,root=0):
 info=validate_state_images(images,a,root);x=Q(x);y=Q(y);assert x>0 and y>0;mats=[]
 for phase in range(info['group_period']):
  M=[[Q(0)]*8 for _ in range(8)]
  for s,w in enumerate(images):
   h=s//2
   for p,hj,sj in image_data(w)[0]:
    px,py=rotate(p,a*phase-h)
    M[s][2*((h+hj)%4)+sj]+=x**px*y**py
  mats.append(M)
 return info,mats,[Q(1),Q(-1)]*4

def character_test(images,a,q,u,v,root=0):
 info,d,mats,z=cyclotomic_matrices(images,a,q,u,v,root);D=len(z)
 phases=range(0,len(mats),info['root_period']);seq={(ph,b):[] for ph in phases for b in range(d)}
 for r in range(3*D+3):
  cur=z
  for ph,M in enumerate(mats):
   if ph in phases:
    for b in range(d):seq[ph,b].append(cur[root*d+b])
   cur=mv(M,cur)
  z=cur
 cert=[]
 for (ph,b),values in seq.items():
  c=recurrence_certificate(values,D);c.update(phase=ph,basis=b);cert.append(c)
 return dict(**info,modulus=q,character=[u,v],root=root,bounded=all(c['bounded'] for c in cert),certificates=cert)

def positive_test(images,a,x,y,root=0):
 info,mats,z=positive_matrices(images,a,x,y,root);D=8
 phases=range(0,len(mats),info['root_period']);seq={ph:[] for ph in phases}
 for r in range(6*D+7):
  cur=z
  for ph,M in enumerate(mats):
   if ph in phases:seq[ph].append(cur[root])
   cur=mv(M,cur)
  z=cur
 cert=[]
 for ph,values in seq.items():
  for parity in range(2):
   c=negative_divergence(values[parity::2],D);c.update(phase=ph,block_parity=parity);cert.append(c)
 return dict(**info,x=str(x),y=str(y),root=root,negative_divergence=any(c['certified'] for c in cert),certificates=cert)

def refined_states(images,state,depth):
 word=[state]
 for _ in range(depth):
  nxt=[]
  for s in word:
   h=s//2
   for _,hj,sj in image_data(images[s])[0]:nxt.append(2*((h+hj)%4)+sj)
  word=nxt
 return word

def literal_state_occupation(images,root,depth):
 states=refined_states(images,root,depth);p=(0,0);h=root//2;occ={}
 for s in states:
  assert s//2==h
  sign=1 if s%2==0 else -1;occ[p]=occ.get(p,0)+sign
  h=(h+sign)%4;p=(p[0]+DIR[h][0],p[1]+DIR[h][1])
 return {p:c for p,c in occ.items() if c},p,h,len(states)


def checkpoint_charge_certificate(images,a=0,root=0):
 return character_test(images,a,1,0,0,root)

def bounded_fuel_character(images,a,q,u,v,root=0):
 charge=checkpoint_charge_certificate(images,a,root)
 if not charge['bounded']:
  return dict(status='NO BOUNDED-CHECKPOINT-CHARGE CERTIFICATE',charge=charge)
 output=character_test(images,a,q,u,v,root)
 return dict(status='FINITE-SUPPORT OBSTRUCTION' if not output['bounded'] else 'PASSED NECESSARY TEST',charge=charge,output=output)
