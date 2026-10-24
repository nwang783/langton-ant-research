from pathlib import Path
from itertools import product
import json,hashlib
B=Path('/workspace/shared/langton');F=B/'core_periodicity_new/genealogy_coordinate_slack_frozen_20261023_0804';M=json.loads((F/'manifest.json').read_text())
for name,digest in M.items():assert hashlib.sha256((F/name).read_bytes()).hexdigest()==digest
G=json.loads((B/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text());ages={(a,complex(x,y)):v for a,x,y,v in json.loads((B/'core_periodicity_new/chronology_dcuv/counted_input_age_rules_complete.json').read_text())};chosen={0:1j,1:1j,4:1+2j,5:1+2j,6:3j,7:3j,8:3j,9:3j};phi=(0,5,6,3);checked=0;zero=[];cases=[]
# Literal output sets are independently reconstructed as in KP, not trusted as table output.
core={complex(x,y)for x,y in G['core']}
for a,q in chosen.items():
 g=G['geometry'][a];z=0j;h=1j;toggle=set();need={};snap=None
 for t,c in enumerate(g['word']+g['marker']):
  v=(c=='L')^(z in toggle);assert z not in need or need[z]==v;need[z]=v;toggle.symmetric_difference_update([z]);h*=(-1j if c=='R' else 1j);z+=h
  if t+1==len(g['word']):snap=z,h,toggle.copy()
 black={p for p,v in need.items()if v};end,head,flipped=snap;out=(black^flipped)-{end+p*(head/1j)for p in core}
 for hp,hc in product(range(4),repeat=2):
  age=ages[a,q];n=next(n for n in range(age,age+4)if(hp-hc-n)%4==0)
  for v in out:
   delta=(v-q)*((-1j)**hc)
   for frame in range(4):
    dy=int((delta*((-1j)**frame)).imag);margin=4*(n-dy)+phi[(hp+frame)%4]-phi[(hc+frame)%4]-3*(a!=9);assert margin>=0;checked+=1
   dy=int(delta.imag);cases.append((hp,hc,a,n-dy,(int(v.real),int(v.imag)),n,dy))
   if n==dy:zero.append([hp,hc,a,[int(v.real),int(v.imag)],n,dy])
expected=[[2,3,1,[3,1],3,3],[2,3,1,[3,2],3,3],[3,0,5,[2,5],3,3],[0,0,9,[-1,7],4,4],[0,0,9,[0,7],4,4]]
assert sorted(zero)==sorted(expected)
cycle=[]
for hp,hc,a in [(0,1,4),(1,2,4),(2,3,1),(3,0,5)]:cycle.append(min((c for c in cases if c[:3]==(hp,hc,a)),key=lambda c:c[3]))
assert sum(c[3]for c in cycle)==3 and len(cycle)==4
# Only source upper (0,7) is sector-compatible with a following equal-heading chosen input.
recurrent=[]
for out in(-1+7j,7j):
 shift=out-3j
 if int(shift.real+shift.imag)%2==0:recurrent.append([int(shift.real),int(shift.imag),0])
assert recurrent==[[0,4,0]]
res=dict(status='PASS independent literal inequality and corrected recurrent-sector scope',fundamental_facet_cases=checked,potential=list(phi),zero_slack_born_output_cases=sorted(zero),abstract_optimality_cycle=cycle,recurrent_actual_sector_compatible_pose=recurrent,correction='Frozen note incorrectly lists(-1,4,0) as surviving. It is wrong-sector and cannot recur; output(-1,7) may only terminate a tight chain.',scope='Auxiliary ancestry coordinate slack bound in complete recurrent-eight factors; abstract4/3 optimality is not physical realizability, and no capture follows.')
Path(__file__).with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
