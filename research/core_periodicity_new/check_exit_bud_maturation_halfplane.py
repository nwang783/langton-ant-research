"""Extract exact ≤2-postexit-C bud exclusions from SIGNED KV; no new threshold.
Then derive a3C half-plane persistence invariant from exact zero-C endpoints.
"""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;GP=R/'chronology_dcuv/literal_residual_geometry.json';CP=R/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';G=json.loads(GP.read_text())['geometry'];IDS=[0,1,4,5,6,7,8,9];mp={a:i for i,a in enumerate(IDS)};COUNT={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()}
rot=lambda q,h:((q[0],q[1]),(q[1],-q[0]),(-q[0],-q[1]),(-q[1],q[0]))[h]
rows=[];queries=[];sector_impossible=[]
for p in IDS:
 c=G[p]['name'].count('C');ex,ey,eh=G[p]['endpoint'];v=rot((1,-1),eh);o=(ex+v[0],ey+v[1]);assert list(o)in G[p]['outputs'];cnt=0
 for delta in range(3):
  n=c+delta;h=(-n)%4;assert 0<=n<=4
  for b in IDS:
   for inp in G[b]['inputs']:
    r=rot(inp,h);head=(o[0]-r[0],o[1]-r[1]);row=dict(source=p,exit_bud_output=o,postexit_C_age=delta,source_included_C_age=n,consumer=b,input=inp,consumer_pose=[*head,h])
    if(sum(head)+h)%2:sector_impossible.append(row);continue
    key=(mp[p],mp[b],*head,h,*o,n);assert key in COUNT;row['exact_counted_query']=key;queries.append(row);cnt+=1
 rows.append(dict(producer=p,C_count=c,raw_exit=[ex,ey,eh],universal_exit_bud_output=o,sector_compatible_excluded_queries=cnt))
# At3postexit Cs, any strict first consumer before B has ZERO remaining C,
# hence is D/V/U atE. Its base ends strictly right of the A-normalized x=0.
endpoints=[]
for b in(0,4,7):
 for inp in G[b]['inputs']:
  v=rot(inp,1);head=(1-v[0],-1-v[1]);step=rot(G[b]['endpoint'][:2],1);end=(head[0]+step[0],head[1]+step[1]);assert end[0]>=1
  endpoints.append(dict(consumer=b,input=inp,consumer_head=head,raw_end=end))
assert all(rot(G[b]['endpoint'][:2],1)[0]>0 for b in(0,4,7))
white=[];black=[]
for b in IDS:
 for w in G[b]['requirements']:
  # At targetB=(X,Y,E), localbud=(Y+1,1-X); X<=0 iff localv>=1.
  if w[1]>=1:
   row=dict(target=b,local_cell=w[:2],relative_B_pose=[1-w[1],w[0]-1,1],first_read=w[3])
   (black if w[2]else white).append(row)
J=dict(status='AUTHOR_SIGNED_KV_BUD_MATURATION_AND_3C_HALFPLANE_PASS',scope='No exit bud of any recurrent producer can be consumed with0,1,2 additional Cs after its producer exit; every exact tested source-includedage<=4. At3Cs after markedA immediatelyfollowingproducer, bud remainscurrent beforeevery later markedBheadingE withX<=0, NOYbound. InitialAwithoutproducer exempt. No record or protectedgoal assumption.',producer_buds=rows,all_exact_exclusion_queries=queries,sector_impossible_options=sector_impossible,zero_C_E_consumer_endpoints=endpoints,halfplane_target_white_avoidances=white,halfplane_target_black_origins=black,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,CP,Path(__file__).resolve()]})
(R/'chronology_dcuv/exit_bud_maturation_halfplane.json').write_text(json.dumps(J,indent=2)+'\n');print(dict(exact_queries=len(queries),sector_impossible=len(sector_impossible),zero_C_endpoints=len(endpoints),white_avoidances=len(white),black_origins=len(black)))
