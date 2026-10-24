"""Complete finite producer inventory and signed clauses, not a path search."""
from pathlib import Path
import hashlib,json
W=Path(__file__).resolve().parent
GP=W/'chronology_dcuv/literal_residual_geometry.json'
CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv'
RP=W/'chronology_dcuv/delayed_height_probe/u1_residue_cegar/root_out.json'
G=json.loads(GP.read_text())['geometry'];IDS=(0,1,4,5,6,7,8,9)
mp={a:i for i,a in enumerate(IDS)}
COUNT={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()}
R=json.loads(RP.read_text());T={(a,h):v for a,h,v in R['created_peaks']}
a=(-1,1);q=(-1,2);UPPER={(-1,4),(0,2),(0,3)}
def rot(p,h):
 x,y=p
 return ((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def query(b,h,o,consumer,cell,age):
 dh=(-h)%4;v=rot(cell,dh)
 key=(mp[b],mp[consumer],o[0]-v[0],o[1]-v[1],dh,*o,age)
 return dict(tuple=key,excluded=key in COUNT)
def producers(cell,h,protected,age,consumer):
 out=[]
 for b in IDS:
  for oi,o in enumerate(G[b]['outputs']):
   z=rot(o,h);head=(cell[0]-z[0],cell[1]-z[1])
   if(sum(head)+h)%2:continue
   ctx={(head[0]+rot((x,y),h)[0],head[1]+rot((x,y),h)[1])
        for x,y,*_ in G[b]['requirements']}
   if ctx&protected:continue
   outputs=[(head[0]+rot(t,h)[0],head[1]+rot(t,h)[1])for t in G[b]['outputs']]
   out.append(dict(packet=b,head=[*head,h],output_slot=oi,output_cell=cell,
                   other_lower_is_output=a in outputs,
                   a_output_slot=outputs.index(a)if a in outputs else None,
                   counted=query(b,h,o,consumer,cell,age)))
 return out
cases=[]
for consumer in (7,8,9):
 distinct=[]
 for age,h in ((3,3),(4,0)):
  rows=producers(a,h,UPPER|{q},age,consumer)
  assert len(rows)==(11 if age==3 else 2)
  assert all(r['counted']['excluded']for r in rows)
  distinct.append(dict(a_age=age,a_heading=h,producer_placements=rows))
 Q=producers(q,0,UPPER,4,consumer)
 assert len(Q)==15
 remaining=[]
 for r in Q:
  if r['counted']['excluded']:continue
  assert r['other_lower_is_output']
  b=r['packet'];o=G[b]['outputs'][r['a_output_slot']]
  r['a_counted']=query(b,0,o,consumer,a,4)
  assert not r['a_counted']['excluded']
  remaining.append(r)
 assert len(remaining)=={7:8,8:6,9:0}[consumer]
 cases.append(dict(consumer=consumer,distinct_birth_options=distinct,
                   q_geometry_placements=Q,same_birth_survivors=remaining))
u1=[]
for r in cases[0]['same_birth_survivors']:
 b=r['packet'];x,y,h=r['head'];assert h==0
 score=2*(y-x)+T[b,1]
 u1.append(dict(packet=b,head=r['head'],created_peak=score,
                excluded_by_strict_record=score>=30))
assert [(r['packet'],r['head'])for r in u1 if r['excluded_by_strict_record']]==[(7,[-3,1,0]),(9,[-3,1,0])]
O=dict(status='AUTHOR_U_AGE4_PAIR_SAME_PRODUCER_PASS',
       scope='Complete recurrent-eight factor. Produced lower q of age4; JO/KV/LN and existing signed exact counted clauses only. Surviving templates not claimed attainable.',
       cases=cases,U1_strict_record_filter=u1,
       dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in [GP,CP,RP,Path(__file__).resolve()]})
P=W/'chronology_dcuv/u_age_four_pair_cohort.json'
P.write_text(json.dumps(O,indent=2)+'\n')
print({'same_birth_survivors':{r['consumer']:len(r['same_birth_survivors'])for r in cases},
       'U1_survivors':sum(not r['excluded_by_strict_record']for r in u1)})
