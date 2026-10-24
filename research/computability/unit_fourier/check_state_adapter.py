import random,json,pathlib
from state_refinement_transfer import *
p=pathlib.Path(__file__).parent;inv=json.loads((p.parent.parent/'causal_reduction/unit_scale/probe_charge_preserving_nine.json').read_text())
rng=random.Random(231026);cases=[];checks=letters=0
for c in range(24):
 images=[rng.choice((["R"]+inv['R_images']) if s%2==0 else (["L"]+inv['L_images'])) for s in range(8)]
 images[0]=rng.choice([w for w in inv['R_images'] if w[0]=='R'])
 info=validate_state_images(images,0)
 assert info['root_period']==1
 for q,u,v in((2,1,1),(3,1,2),(4,2,1)):
  _,d,mats,z=cyclotomic_matrices(images,0,q,u,v)
  for r in range(4):
   occ,pp,h,n=literal_state_occupation(images,0,r)
   assert z[:d]==eval_occupation(occ,q,u,v);assert pp==(1,0) and h==1
   checks+=1;letters+=n;z=mv(mats[r%len(mats)],z)
 tests=[character_test(images,0,3,u,v) for u,v in ((1,0),(0,1))]
 cases.append(dict(images=images,mod3_unbounded=any(not t['bounded'] for t in tests)))
# Explicit two-cycle root control: first R image begins L, and first L begins R.
images=[inv['R_images'][-1] if s%2==0 else inv['L_images'][0] for s in range(8)]
info=validate_state_images(images,0);assert info['root_period']==2 and info['group_period']==2
ans=character_test(images,0,3,1,2);assert all(c['phase']==0 for c in ans['certificates'])
out=dict(independent_heading_assignments=len(cases),literal_checks=checks,literal_letters=letters,
 cases=cases,root_cycle_control=dict(images=images,information=info,test=ans))
(p/'check_state_adapter.json').write_text(json.dumps(out,indent=2)+'\n');print(checks,letters,sum(c['mod3_unbounded'] for c in cases))
