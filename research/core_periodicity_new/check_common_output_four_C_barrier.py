"""A fresh source-entry output yields unconditional exact4C nonreturn.
No factor-first exception, no new counted relation, complete8 scope only.
"""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;GP=R/'chronology_dcuv/literal_residual_geometry.json';AP=R/'chronology_dcuv/counted_input_age_rules_complete.json';G=json.loads(GP.read_text())['geometry'];mins={(a,x,y):v for a,x,y,v in json.loads(AP.read_text())};IDS=[0,1,4,5,6,7,8,9];K=set(map(tuple,json.loads(GP.read_text())['core']));q=(2,0);D=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
source_rows=[];target_rows=[]
for a in IDS:
 c=G[a]['name'].count('C');assert list(q)in G[a]['outputs']and list(q)not in G[a]['inputs']and q not in K
 req=[w for w in G[a]['requirements']if tuple(w[:2])==q];assert req==[[2,0,False,8]]
 assert len(G[a]['word'])%2==c%2 and G[a]['endpoint'][2]==(-c)%4
 source_rows.append(dict(source=a,C_count=c,output=q,source_before_white_requirement=req[0],fresh_output_birth_clock=0))
 target_rows.append(dict(target=a,marked_before_white_requirement=req[0]))
assert all(v>=2 for v in mins.values())
age2=[]
for a in IDS:
 for inp in G[a]['inputs']:
  if mins[a,*inp]>2:continue
  h=2;r=rot(inp,h);p=(q[0]-r[0],q[1]-r[1]);assert(a,inp)==(4,[0,3])or(a,inp)==(5,[0,3]);assert(sum(p)+h)%2==1
  age2.append(dict(consumer=a,input=inp,required_pose=[*p,h],wrong_sector=(sum(p)+h)%2))
assert len(age2)==2
endpoints=[]
for h in(0,1):
 for b in(0,4,7):
  step=rot(G[b]['endpoint'][:2],h)
  for inp in G[b]['inputs']:
   ri=rot(inp,h);p=(q[0]-ri[0],q[1]-ri[1]);e=(p[0]+step[0],p[1]+step[1]);assert e[0]>=2
   endpoints.append(dict(age=4 if h==0 else 3,heading=h,consumer_base=b,input=inp,base_start=p,base_end=e,remaining_C_to4=0 if h==0 else 1,minimum_four_C_final_x=e[0]+(0 if h==0 else 1)))
assert all(rot(G[b]['endpoint'][:2],h)[0]>=0 for b in(0,4,7)for h in(0,1))
C=G[1]['word'][len(G[0]['word']):];p=(0,0);h=1
for ch in C:h=(h+(-1 if ch=='L'else 1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
assert(p,h)==((1,0),0)
J=dict(status='AUTHOR_COMMON_SOURCE_OUTPUT_3C_4C_BARRIER_AND_UNCONDITIONAL_4C_NONRETURN_PASS',scope='Any complete8 source atA0,N, includingfactorFIRST. Fresh source-output(2,0) survives before3C targetBheadingE withX<=1 and4C targetBheadingN withX<=1. Thus exactmarkedpose repeat at4C impossible evenfactorfirst. No atomicinternal-cut extension or higherCnonreturn claimed.',sources=source_rows,all_target_marker_whites=target_rows,all_age2_eligible_consumers_wrong_sector=age2,all16_after_consumer_endpoints=endpoints,sector_invariant='x+y+h mod2=0 after normalizing sourceA to0,N; each packet has length parity equal C parity',remaining_E_to_N_C_displacement=[1,0,0],dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,AP,Path(__file__).resolve()]})
(R/'chronology_dcuv/common_output_four_C_barrier.json').write_text(json.dumps(J,indent=2)+'\n');print(dict(common_fresh_outputs=len(source_rows),common_target_whites=len(target_rows),age2_sector_cases=len(age2),endpoints=len(endpoints),four_C_min_x=min(r['minimum_four_C_final_x']for r in endpoints)))
