"""Two exact full-source role extractions closing the second-C birth-clock gap."""
from pathlib import Path
import json,hashlib,collections
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry'];HP=W/'chronology_dcuv/protected_patch2.tsv';CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';HB={tuple(map(int,l.split()[:7]))for l in HP.read_text().splitlines()};COUNT={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()};keep=[0,1,4,5,6,7,8,9];mp={a:i for i,a in enumerate(keep)}
def rot(z,h):x,y=z;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
roles=[];queries=[]
for a,pre,o in[(6,5,(1,6)),(9,8,(0,7))]:
 assert list(o)in G[a]['outputs'];x,y,h=G[pre]['endpoint'];u,v=rot((2,0),h);assert(x+u,y+v)==o
 roles.append(dict(full_producer=a,second_C_entry_prefix=pre,atomic_entry=G[pre]['endpoint'],atomic_output_slot=[2,0],full_output_slot=o,full_birth_C=0,atomic_birth_C=1,atomic_age_equals_full_age_minus=1))
 for n in range(4):
  hb=(-n)%4
  for b in keep:
   for z in G[b]['inputs']:
    u,v=rot(z,hb);p=o[0]-u,o[1]-v;key=(a,b,*p,hb,*o);ck=(mp[a],mp[b],*p,hb,*o,n)
    q=dict(producer=a,output=o,consumer=b,input=z,exact_full_source_age=n,consumer_pose=[*p,hb],HB_key=key,count5_key=ck)
    if(sum(p)+hb)%2:q['reason']='SECTOR_IMPOSSIBLE'
    elif key in HB:q['reason']='SIGNED_HB_EXCLUDED'
    elif ck in COUNT:q['reason']='SIGNED_COUNT5_EXCLUDED'
    else:raise AssertionError(q)
    queries.append(q)
assert len(queries)==184;counts=collections.Counter(q['reason']for q in queries);assert counts=={'SECTOR_IMPOSSIBLE':92,'SIGNED_COUNT5_EXCLUDED':92}
O=dict(status='AUTHOR_SECOND_C_COMMON_OUTPUT_CLOCK_GUARD_PASS',scope='Full VCC(1,6)/UCC(0,7) output roles exclude every full-source age<=3, implying atomic second-C output(2,0) consumption age>=3 despite the one-C birth-clock shift. No independent atomic counted closure, search, finite fuel or capture claim.',roles=roles,queries=queries,counts=counts,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,HP,CP,W/'atomic_exit_bud_frozen_20261023_1325/manifest.json',Path(__file__).resolve()]});(W/'chronology_dcuv/second_C_common_output_clock_guard.json').write_text(json.dumps(O,indent=2)+'\n');print(dict(raw_cases=len(queries),counts=dict(counts)))
