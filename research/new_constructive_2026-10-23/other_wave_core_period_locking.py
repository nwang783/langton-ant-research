#!/usr/bin/env python3
"""Companion all-word period-locking applications to complete1564/4352 outputs.
Uses the general gcd-compatible allowed-graph lemma; no consumer word search.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib
P=Path('/workspace/shared/langton/causal_reduction/unit_scale');O=Path(__file__).parent
A=json.loads((P/'prepared1564_actual_output_consumers.json').read_text())['backgrounds'];N=json.loads((P/'prepared15324_return_normal_form.json').read_text());sources=[('actual1564_seven_writer692',14,{tuple(q)for q in A['seven_writer_output']['black_mod14']},(-40,8)),('actual1564_with_endpoint776',14,{tuple(q)for q in A['seven_writer_output_plus_endpoint_lane']['black_mod14']},(-40,8)),('actual4352_five_writer964',26,{tuple(q)for q in N['bulk_mod26']},(15,20))];results=[]
for name,n,S,band in sources:
 L=min(t for t,a in S)-2;U=max(t for t,a in S)+2;BAND=set(range(band[0],band[1]+1));ds=[g for g in range(1,n+1)if n%g==0];rr=[]
 for g in ds:
  allowed={};mixed=[]
  for t in range(L,U+1):
   for a in range(g):
    B=[x for x in range(a,n,g)if(t,x)in S];W=[x for x in range(a,n,g)if(t,x)not in S]
    if not B:allowed[t,a]=0
    elif not W:allowed[t,a]=1
    else:mixed.append([t,a,B[0],W[0]])
  adj=defaultdict(list)
  for t,a in allowed:
   for q,w in[((t+1,(a+1)%g),int(a==g-1)),((t-1,(a-1)%g),-int(a==0)),((t-1,a),0),((t+1,a),0)]:
    if q in allowed:adj[t,a].append((q,w))
  seen=set();cc=[];ncc=0;corevertices=0
  for root in sorted(allowed):
   if root in seen:continue
   pot={root:0};todo=[root];seen.add(root);cycle=False
   for v in todo:
    for q,w in adj[v]:
     if q in pot:cycle|=pot[q]!=pot[v]+w
     else:pot[q]=pot[v]+w;todo.append(q);seen.add(q)
   central=[q for q in pot if q[0]in BAND];ncc+=1
   if central:
    boundary=any(t in[L,U]for t,a in pot);corevertices+=len(central)
    if g<n:
     assert not cycle and not boundary
     assert all(pot[q]-pot[v]==w for v in pot for q,w in adj[v])
    else:assert cycle
    cc.append({'size':len(pot),'normal_hull':[min(t for t,a in pot),max(t for t,a in pot)],'touches_collar':boundary,'has_nonzero_winding':cycle,'potential':[[t,a,v]for(t,a),v in sorted(pot.items())]if g<n else None})
  rr.append({'g':g,'allowed_vertices':len(allowed),'central_vertices':corevertices,'central_components':cc,'mixed_witnesses':mixed})
 results.append({'name':name,'period':n,'black_classes':len(S),'locked_ribbon':band,'graph_collar':[L,U],'divisors':rr})
 print(name,'black',len(S),'locked',band,'properg',[(r['g'],r['central_vertices'],len(r['central_components']))for r in rr if r['g']<n])
out={'status':'AUTHOR exact companion all-word period locks PASS','scope':__doc__,'results':results,'positive_transfer_control':{'source':'4352output964','known_consumer':'15324','full_stride':78,'source_period_divides_consumer_stride':78%26==0},'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()};(O/'other_wave_core_period_locking.json').write_text(json.dumps(out,indent=2)+'\n')
