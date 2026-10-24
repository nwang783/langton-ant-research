"""Atomic-exit bud lifetime from literal C geometry and existing cap5 clauses.
No new closure generation, path search, or increased count threshold.
"""
from pathlib import Path
import json,hashlib,collections
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';J=json.loads(GP.read_text());G=J['geometry'];K=set(map(tuple,J['core']));HP=W/'chronology_dcuv/protected_patch2.tsv';CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';HB={tuple(map(int,l.split()[:7]))for l in HP.read_text().splitlines()};COUNT={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()};keep=[0,1,4,5,6,7,8,9];mp={a:i for i,a in enumerate(keep)}
def rot(z,h):x,y=z;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
C=G[1]['word'][len(G[0]['word']):];marker=G[0]['marker'];assert C.startswith(marker)
# Standalone C's complete entry requirements are exactly core-black, all else white.
p=(0,0);h=0;need={};par=set();raw_end=None
for i,ch in enumerate(C+marker):
 bit=ch=='L';r=bit^(p in par);assert p not in need or need[p]==r;need[p]=r
 if p in par:par.remove(p)
 else:par.add(p)
 h=(h+(-1 if bit else 1))%4;u,v=rot((0,1),h);p=p[0]+u,p[1]+v
 if i+1==len(C):raw_end=(p,h,set(par))
assert{p for p,r in need.items()if r}==K
p,h,rawodd=raw_end;B=K^rawodd;newcore={(p[0]+rot(z,h)[0],p[1]+rot(z,h)[1])for z in K};assert newcore<=B;C_outputs=B-newcore
assert(p,h)==((0,1),3)and len(C_outputs)==3 and(1,2)in C_outputs
u,v=rot((1,-1),h);assert(p[0]+u,p[1]+v)==(1,2)
roles=[];queries=[]
for a in keep:
 cc=G[a]['name'].count('C');base=0 if a in[0,1]else 4 if a in[4,5,6]else 7;assert G[a]['word']==G[base]['word']+C*cc and G[a]['inputs']==G[base]['inputs']
 p=tuple(G[base]['endpoint'][:2]);h=0
 for j in range(cc+1):
  u,v=rot((1,-1),h);o=p[0]+u,p[1]+v;assert list(o)in G[a]['outputs'];roles.append(dict(full_producer=a,atomic_prefix_C=j,atomic_exit=[*p,h],bud_full_output_slot=o))
  for n in range(j,j+3):
   hb=(-n)%4
   for b in keep:
    for z in G[b]['inputs']:
     u,v=rot(z,hb);q=o[0]-u,o[1]-v;key=(a,b,*q,hb,*o);ck=(mp[a],mp[b],*q,hb,*o,n)
     r=dict(producer=a,prefix_C=j,output=o,consumer=b,input=z,source_included_age=n,post_atomic_exit_C=n-j,consumer_pose=[*q,hb],HB_key=key,count5_key=ck)
     if n<cc:r['reason']='CONSUMER_PRECEDES_FULL_PRODUCER_EXIT'
     elif(sum(q)+hb)%2:r['reason']='SECTOR_IMPOSSIBLE'
     elif key in HB:r['reason']='SIGNED_HB_EXCLUDED'
     elif ck in COUNT:r['reason']='SIGNED_COUNT5_EXCLUDED'
     else:raise AssertionError(r)
     queries.append(r)
  u,v=rot((0,1),h);p=p[0]+u,p[1]+v;h=(h-1)%4
assert len(roles)==15 and len(queries)==1035
counts=collections.Counter(q['reason']for q in queries);O=dict(status='AUTHOR_ATOMIC_EXIT_BUD_THREE_C_MATURATION_PASS',scope='Every D/V/U/C atomic exit in a complete retained-eight factor installs a residual bud at exithead+rot_heading(1,-1); it cannot be consumed through two further C turns. Literal C consumes no residuals. Rollingtwo-C atomic exit-bud cells are pairwise distinct. No global fuel, packing or capture theorem.',C_word=C,C_marker=marker,C_endpoint=[*raw_end[0],raw_end[1]],C_entry_requirements=[[*p,bool(r)]for p,r in sorted(need.items())],C_residual_inputs=[],C_residual_outputs=sorted(C_outputs),roles=roles,queries=queries,query_counts=counts,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,HP,CP,Path(__file__).resolve()]});(W/'chronology_dcuv/atomic_exit_bud_maturation.json').write_text(json.dumps(O,indent=2)+'\n');print(dict(roles=len(roles),raw_cases=len(queries),counts=dict(counts),C_outputs=sorted(C_outputs)))
