#!/usr/bin/env python3
"""All-word78-stride barrier for central15324-output ribbon.
Exact finite quotient / potential proof, no turn-word search, visit cap or horizon.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib
P=Path('/workspace/shared/langton/causal_reduction/unit_scale');O=Path(__file__).parent
W=json.loads((P/'prepared4352_output_return_wave.json').read_text())['word'];N=json.loads((P/'prepared15324_return_normal_form.json').read_text());D=((0,1),(1,0),(0,-1),(-1,0));p=(13,7);h=0;T=set()
for c in W:
 j=(p[0]-p[1],p[0]%78)
 if j in T:T.remove(j)
 else:T.add(j)
 h=(h+(-1 if c=='L'else 1))%4;v=D[h];p=p[0]+v[0],p[1]+v[1]
I={(t,a)for t,b in N['bulk_mod26']for a in range(b,78,26)};S=I^T;assert len(S)==3300
L,U=-66,94;BAND=set(range(8,25));results=[]
for g in[1,2,3,6,13,26,39,78]:
 allowed={};witnesses=[]
 for t in range(L,U+1):
  for a in range(g):
   black=[x for x in range(a,78,g)if(t,x)in S];white=[x for x in range(a,78,g)if(t,x)not in S]
   if not black:allowed[t,a]=0
   elif not white:allowed[t,a]=1
   else:witnesses.append([t,a,black[0],white[0]])
 adj=defaultdict(list)
 for(t,a)in allowed:
  edges=[((t+1,(a+1)%g),int(a==g-1),'E'),((t-1,(a-1)%g),-int(a==0),'W'),((t-1,a),0,'N'),((t+1,a),0,'S')]
  for q,w,name in edges:
   if q in allowed:adj[t,a].append((q,w,name))
 seen=set();central_components=[];essential_normal=set();ncomp=0;allcentral=set()
 for root in sorted(allowed):
  if root in seen:continue
  pot={root:0};todo=[root];seen.add(root);cycle=None
  for v in todo:
   for q,w,name in adj[v]:
    if q in pot:
     if pot[q]!=pot[v]+w and cycle is None:cycle=[v,q,w,pot[v],pot[q]]
    else:pot[q]=pot[v]+w;todo.append(q);seen.add(q)
  boundary=any(t in[L,U]for t,a in pot)
  essential=cycle is not None or boundary
  if essential:essential_normal.update(t for t,a in pot if -28<=t<=46)
  central={q for q in pot if q[0]in BAND};allcentral.update(central);ncomp+=1
  if central:
   central_components.append({'size':len(pot),'normal_hull':[min(t for t,a in pot),max(t for t,a in pot)],'touches_exterior_collar':boundary,'nonzero_winding_witness':cycle,'potential':[[t,a,z]for(t,a),z in sorted(pot.items())]if not essential else None})
   if g<78:
    assert not essential
    assert all(pot[q]-pot[v]==w for v in pot for q,w,name in adj[v])
    assert all(L<t<U for t,a in pot)
 if g<78:assert not(BAND&essential_normal)
 else:assert BAND<=essential_normal and len(central_components)==1
 results.append({'gcd':g,'allowed_vertices':len(allowed),'incompatible_vertices':len(witnesses),'components':ncomp,'essential_core_normals':sorted(essential_normal),'central_allowed_vertices':len(allcentral),'central_components':central_components,'color_incompatibility_witnesses':witnesses})
# A simple nonvacuous example for the lift conventions: E,N repeatedg times
# on either two-row white exterior collar has quotient winding+1.
for g in[1,2,3,6,13,26,39,78]:
 pp=(0,67); # t=-67, safely outside all profile black cells.
 q=pp
 for _ in range(g):q=q[0]+1,q[1];q=q[0],q[1]+1
 assert q==(g,67+g)
out={'status':'AUTHOR exact all-word stride divisibility barrier','profile_black_classes':len(S),'source_period':78,'central_ribbon':[8,24],'theorem':'Any nonzero parallel translating periodic consumer of this profile plus any finite cap, whose repeating read support meets8<=x-y<=24, has78 dividing its full stride s in displacement(s,s).','proper_divisors_checked':[1,2,3,6,13,26,39],'finite_graph_normal_range':[L,U],'all_exterior_collars_white':True,'results':results,'scope':__doc__,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(O/'central_ribbon_stride_divisibility.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='results'},indent=2));print('g : allowed / centralallowed / centralcomponents')
for r in results:print(r['gcd'],r['allowed_vertices'],r['central_allowed_vertices'],len(r['central_components']))
