"""Independent rotated local table and actual full-white-cycle controls.
The all-front disjointness proof is the essential-circle side-switch argument,
not extrapolation from these controls.
"""
from pathlib import Path
from collections import defaultdict, Counter
from itertools import product,combinations
import json,hashlib
R=Path(__file__).resolve().parents[1];W=(R/'word_stabilization/standard_word.txt').read_text().strip()
def cross(a,b):return int((a.conjugate()*b).imag)
local=[]
for incoming in (1j,1,-1j,-1):
 for at,bt in product('RL',repeat=2):
  ao=incoming*(-1j if at=='R'else 1j);bo=-1j*incoming
  bi=incoming if bt=='R'else-incoming
  shared_in=bi==incoming;shared_out=ao==bo
  assert (shared_in,shared_out)==({'RR':(True,True),'RL':(False,True),'LR':(True,False),'LL':(False,False)}[at+bt])
  if at+bt=='RL':
   # Endpoint rays relative to the common outgoing tangent: A right, B left.
   assert cross(bo,-incoming)<0 and cross(bo,-bi)>0
  if at+bt=='LR':
   assert cross(incoming,ao)>0 and cross(incoming,bo)<0
  if at+bt=='LL':
   assert ao==-bo and bi==-incoming
  local.append(dict(first_in=[int(incoming.real),int(incoming.imag)],turns=at+bt,shared=[shared_in,shared_out]))
def cycles(edge):
 out=[];seen=set()
 for start in edge:
  if start in seen:continue
  pos=start;path=[];where={}
  while pos not in seen and pos not in where:
   where[pos]=len(path);path.append(pos);pos=edge[pos][0]
  if pos in where:out.append(path[where[pos]:])
  seen.update(path)
 return out
records=[]
for copies in (1,2,3):
 for sign in (1,-1):
  a=2*copies;d=complex(a,sign*a);P=104*copies;q=-1+0j if sign==1 else 0j;h=1j if sign==1 else 1
  def canon(z):
   k=int(z.real)//a;return z-k*d,k
  hist=defaultdict(list)
  for t,c in enumerate(W*copies):
   z,k=canon(q);hist[z].append((t-k*P,h,c));h*=(-1j if c=='R'else 1j);q+=h
  hist={z:sorted(es)for z,es in hist.items()};first={z:es[0]for z,es in hist.items()}
  flow=Counter((z,hh*(-1j if c=='R'else 1j))for z,es in hist.items()for t,hh,c in es)
  arrival={};departure={}
  for z,(t,hh,c) in first.items():
   assert c=='R'
   u,k=canon(z-hh);arrival[z]=(u,k,hh)
   assert any(tt+k*P==t-1 and ih*(-1j if tr=='R'else 1j)==hh for tt,ih,tr in hist[u])
   v,k=canon(z-1j*hh);departure[z]=(v,k,-1j*hh)
  AC=cycles(arrival);BC=cycles(departure);AE=[];BE=[];vertices=[]
  for cyc in AC:
   assert sum(arrival[z][1]for z in cyc)==-1
   es={(arrival[z][0],arrival[z][2])for z in cyc};assert len(es)==len(cyc);AE.append(es)
  for cyc in BC:
   assert sum(departure[z][1]for z in cyc)==-1
   es={(z,departure[z][2])for z in cyc};assert len(es)==len(cyc);BE.append(es)
  assert len(AC)==len(BC)==2
  common_vertices=0
  for ca,ea in zip(AC,AE):
   for cb,eb in zip(BC,BE):
    assert ea.isdisjoint(eb)
    for z in set(ca)&set(cb):
     common_vertices+=1;ih=first[z][1]
     ao=next(dr for p,dr in ea if p==z);bo=departure[z][2]
     bz=next(p for p in cb if departure[p][0]==z);bi=departure[bz][2]
     assert ao==1j*ih and bo==-1j*ih and bi==-ih
  checked=0
  for amask in range(1<<len(AE)):
   for bmask in range(1<<len(BE)):
    residual=flow.copy();na=nb=removed=0
    for i,es in enumerate(AE):
     if amask>>i&1:
      na+=1;removed+=len(es)
      for e in es:residual[e]-=1
    for i,es in enumerate(BE):
     if bmask>>i&1:
      nb+=1;removed+=len(es)
      for e in es:residual[e]-=1
    assert min(residual.values())>=0
    disp=sum((dr*n for (z,dr),n in residual.items()),0j)
    assert disp==(1-na+nb)*d
    assert sum(n for (z,dr),n in residual.items()if dr.real)==sum(n for (z,dr),n in residual.items()if dr.imag)
    assert P>=removed+2*a*abs(1-na+nb)
    checked+=1
  records.append(dict(period=P,drift=[a,sign*a],arrival_lengths=list(map(len,AC)),departure_lengths=list(map(len,BC)),shared_edges=0,shared_LL_vertices=common_vertices,subset_flow_checks=checked))
note=R/'periodic_classification_new/dual_first_backbone_edge_separation.md'
out=dict(status='PASS independent local rotation table and complete-flow subset controls',note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),local_cases=local,actual_controls=records,scope='Analytic essential-circle side-change proof supplies universal edge separation; controls are not that proof. No changed monitor or exclusion.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
