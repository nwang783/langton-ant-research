"""Existing signed cap-five query extraction for two fixed prefix-bud roles.
No new counted closure, larger age threshold, or path search.
"""
from pathlib import Path
import json,hashlib,collections
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry'];HP=W/'chronology_dcuv/protected_patch2.tsv';CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';HB={tuple(map(int,l.split()[:7]))for l in HP.read_text().splitlines()};COUNT={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()};keep=[0,1,4,5,6,7,8,9];mp={a:i for i,a in enumerate(keep)}
def rot(z,h):x,y=z;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
queries=[];prefixes=[]
for a,pre,o in[(6,5,(2,5)),(9,8,(1,6))]:
 assert G[a]['word'].startswith(G[pre]['word'])and G[a]['word'][len(G[pre]['word']):].startswith(G[pre]['marker'])
 assert list(o)in G[a]['outputs'];x,y,dh=G[pre]['endpoint'];u,v=rot((1,-1),dh);assert(x+u,y+v)==o
 prefixes.append(dict(full_packet=a,prefix_packet=pre,full_output_slot=o,prefix_endpoint=G[pre]['endpoint'],source_C=2,prefix_cut_C=1,relative_bud_at_prefix_cut=[1,-1]))
 for age in range(5):
  h=(-age)%4
  for b in keep:
   for z in G[b]['inputs']:
    u,v=rot(z,h);p=o[0]-u,o[1]-v;key=(a,b,*p,h,*o);ck=(mp[a],mp[b],*p,h,*o,age)
    r=dict(producer=a,output=o,consumer=b,input=z,exact_age=age,consumer_pose=[*p,h],HB_key=key,count5_key=ck)
    if(sum(p)+h)%2:r['reason']='SECTOR_IMPOSSIBLE'
    elif key in HB:r['reason']='SIGNED_HB_EXCLUDED'
    elif ck in COUNT:r['reason']='SIGNED_COUNT5_EXCLUDED'
    else:raise AssertionError(r)
    queries.append(r)
ports=[]
for x,y,bit,*_ in G[7]['requirements']:
 p=(x-1,y-1)
 if(sum(p)+3)%2==0:ports.append(dict(internal_W_cut=p,prefix_bud=[x,y],goal_required_black=bool(bit),goal_role='INPUT'if[x,y]in G[7]['inputs']else'CORE'if(x,y)in{(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}else'WHITE'))
assert len(queries)==230 and len(ports)==11
assert{tuple(z['internal_W_cut'])for z in ports}=={(-2,-1),(-2,1),(-2,3),(-1,-2),(-1,0),(-1,2),(0,-1),(0,1),(0,3),(1,0),(1,4)}
counts=collections.Counter(z['reason']for z in queries);O=dict(status='AUTHOR_INTERNAL_C_PREFIX_BUD_GUARD_PASS',scope='Two full-producer output roles have no possible consumer through exactCage4 under already signed clauses. Their internal one-C prefix cuts therefore have an11-port U-goal avoidance at cutclockgoal−3. No extension of a retained-eight theorem to standaloneC, no q4/U1 exclusion or finite budget.',prefixes=prefixes,queries=queries,query_counts=counts,internal_W_cut_U_goal_ports=ports,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,HP,CP,Path(__file__).resolve()]});(W/'chronology_dcuv/internal_C_prefix_bud_guard.json').write_text(json.dumps(O,indent=2)+'\n');print(dict(raw_cases=len(queries),query_counts=dict(counts),ports=len(ports)))
