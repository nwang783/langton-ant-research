"""Exact producer covers and all-source 4/5-input-cohort inventory.
No time, age, length, spatial or seed-size cutoff is involved.
"""
from pathlib import Path
from collections import Counter
import json,hashlib
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';J=json.loads(GP.read_text());G=J['geometry'];K=set(map(tuple,J['core']));IDS=(0,1,4,5,6,7,8,9)
I=list(map(tuple,G[7]['inputs']));assert all(G[a]['inputs']==G[7]['inputs']for a in(8,9))
q=(-1,2);P=[p for p in I if p!=q];a=(-1,1);c=(0,2);d=(0,3)
def rot(p,h):x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,z):return(p[0]+z[0],p[1]+z[1])
def producers(q,protected):
 out=[]
 for b in IDS:
  for h in range(4):
   for oi,o in enumerate(G[b]['outputs']):
    z=rot(o,h);head=(q[0]-z[0],q[1]-z[1])
    if(sum(head)+h)%2:continue
    ctx={add(head,rot((x,y),h))for x,y,*_ in G[b]['requirements']}
    hits=sorted(set(protected)&ctx)
    out.append(dict(packet=b,head=[*head,h],output_index=oi,context_hits=hits))
 assert len(out)==136
 return out
CAN=producers(q,P);assert all(r['context_hits']for r in CAN)
# Every minimal protected subset covering all producers. There are only16 subsets.
cover=[]
for mask in range(1,1<<len(P)):
 Z={p for i,p in enumerate(P)if mask>>i&1}
 if all(Z&set(map(tuple,r['context_hits']))for r in CAN):cover.append(mask)
minimal=[m for m in cover if not any(n!=m and n&m==n for n in cover)]
coverpoints=[sorted(P[i]for i in range(len(P))if m>>i&1)for m in minimal]
assert {tuple(z)for z in coverpoints}=={tuple(sorted((a,c))),tuple(sorted((a,d)))}
records=[];maximum=0
for source in IDS:
 O=set(map(tuple,G[source]['outputs']));odd=set(map(tuple,G[source]['raw_odd']));post={(x,y):bool(black)^((x,y)in odd)for x,y,black,*_ in G[source]['requirements']}
 dx,dy,dh0=G[source]['endpoint'];postcore={add((dx,dy),rot(p,dh0))for p in K}
 for dh in range(4):
  poses=sorted({(x-rot(z,dh)[0],y-rot(z,dh)[1])for x,y in O for z in I})
  for pose in poses:
   if(sum(pose)-dh)%2:continue
   T={add(pose,rot(z,dh))for z in I};cohort=T&O;maximum=max(maximum,len(cohort))
   if len(cohort)<4:continue
   assert len(cohort)==4;missing=next(iter(T-cohort));origin='unseen_possible_older_residual'if missing not in post else'post_core_nonresidual'if post[missing]else'known_white'
   if post.get(missing,False):assert missing in postcore
   candidates=producers(missing,cohort);safe=[r for r in candidates if not r['context_hits']]
   outcome='excluded_all_ages'if not safe and missing in post else'older_identity_required'if not safe else'not_excluded_by_this_static_test'
   records.append(dict(source_packet=source,source_name=G[source]['name'],consumer_packets=[7,8,9],consumer_pose=[*pose,dh],matched_source_outputs=sorted(cohort),missing_input=missing,missing_target_offset=next(z for z in I if add(pose,rot(z,dh))==missing),postsource_origin=origin,outcome=outcome,producer_placements=candidates,surviving_producer_count=len(safe)))
assert maximum==4 and len(records)==24
C=Counter(r['outcome']for r in records);assert C==dict(excluded_all_ages=7,older_identity_required=2,not_excluded_by_this_static_test=15)
for r in records:
 if r['outcome']!='not_excluded_by_this_static_test':assert tuple(r['missing_target_offset'])==q
OUT=dict(status='AUTHOR_EXACT_LITERAL_COVER_AND_COHORT_PASS',scope='Factor-relative residual identity birth order in complete recurrent-eight words. Entry identities are virtual-old; no global prior-history ownership assertion. No capture, rank bound or fresh-root claim.',input_shape=I,middle_input=q,protected_other_inputs=P,canonical_producers=CAN,minimal_producer_cover_sets=coverpoints,maximum_same_producer_U_inputs=maximum,four_cohort_templates=records,summary=dict(canonical_producer_count=len(CAN),four_cohort_templates=len(records),outcomes=dict(C),consumer_tail_multiplicity=3),dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,Path(__file__).resolve()]})
T=W/'chronology_dcuv/u_middle_input_origin_order.json';T.write_text(json.dumps(OUT,indent=2)+'\n');print(json.dumps(OUT['summary'],indent=2));print('minimal_covers',coverpoints);print(T)
