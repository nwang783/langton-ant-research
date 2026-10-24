from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry']
def rot(p,h):x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def ctx(a,p,h):return {add(p,rot(z[:2],h)):z[2:]for z in G[a]['requirements']}
rows=[]
for a,p,h,k in[(1,(-5,1),0,4),(5,(-4,7),1,5)]:
 c=G[a]['name'].count('C');dx,dy,dh=G[a]['endpoint'];ep=add(p,rot((dx,dy),h));eh=(h+dh)%4;left=k-c;B=rot(sub((0,0),ep),-eh);bh=(-eh)%4;r=add(ep,rot((1,-1),eh));o=rot(sub(r,p),-h);assert o in set(map(tuple,G[a]['outputs']))
 assert(left,bh)in[(3,1),(4,0)]and B[0]<=0
 I9=set(map(tuple,G[9]['inputs']));C9=ctx(9,(0,0),0);assert r not in I9
 rr=dict(producer=a,pose=[*p,h],exact_full_source_age=k,producer_exit=[*ep,eh],post_exit_Cgap=left,creator_in_exit_frame=[*B,bh],old_bud=r,actual_full_source_output=o)
 if a==1:
  assert r not in C9
  checks=[]
  for helper in[4,5]:
   CI=ctx(helper,(-1,5),2);HI={add((-1,5),rot(z,2))for z in G[helper]['inputs']};assert r in CI and r not in HI
   checks.append(dict(helper=helper,context_before_and_first_read=CI[r],not_residual_input=True))
  rr.update(reason='3C_persistence_through_untouched_UCC_then_immediate_helper_noninput_context_conflict',creator_context_misses_old_bud=True,immediate_helper_checks=checks)
 else:
  assert r in C9 and C9[r][0]==False
  rr.update(reason='4C_persistence_at_creator_before_WHITE_context',creator_before_and_first_read=C9[r])
 rows.append(rr)
D=[GP,Path(__file__).resolve()]+[W/p/'manifest.json'for p in['atomic_predecessor_halfplanes_frozen_20261023_1505','U_q_source_history_frozen_20261023_2027','U1_six_mask_last_birth_frozen_20261023_2029','V1_six_mask_last_birth_frozen_20261023_2044']]
R=dict(status='AUTHOR_TWO_EXACT_SHORT_RETURNS_EXCLUDED_PENDING_AUDIT',scope='Only two specified exact-age representatives from the necessary six-mask classifications are excluded by already signed incoming-bud3/4 halfplanes. DC(-5,1,N) k4 and VC(-4,7,E) k5 fail. Their larger congruent counted-overflow tails8+ and9+ are NOT excluded or attained here. No extended path/age search.',cases=rows,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(W/'chronology_dcuv/six_mask_short_return_buds.json').write_text(json.dumps(R,indent=2)+'\n');print(json.dumps(rows,indent=2))
