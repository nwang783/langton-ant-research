"""Select a minimum additional-black corner from the fixed one-turn phase inventory.
No image/cap length increase. Each positive literal candidate is independently
checked against the exact infinite periodic-tail arithmetic checker.
"""
from pathlib import Path
import sys,json
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'computability'))
from periodic_tail_checker import State,first_mismatch
from certify_highway_wake_reflector import trace
from probe_perpendicular_highway_wake import H,shifted_seed,step
cases=json.loads((P/'single_turn_highway_corner.json').read_text())['survivors'];res=[]
for case in cases:
 a=case['in_phase'];b=case['out_phase'];cap=case['cap']
 base=shifted_seed(1,(0,0));p=(0,0);h=2
 for c in H[:a]:p,h,cc=step(base,p,h);assert c==cc
 base={(x-p[0],y-p[1])for x,y in base};ha=h
 iw=H[a:]+H[:a];ow=H[b:]+H[:b]
 rr,capP,capH=trace(iw*30,(0,0),ha);past={q for q,hh,c in rr}
 rr2,_,_=trace(cap+ow*10,capP,capH);rr+=rr2
 first={};odd=set()
 for q,hh,c in rr:
  if q not in first:first[q]=c
  odd.symmetric_difference_update({q})
 required={q for q,c in first.items()if c=='L'};white={q for q,c in first.items()if c=='R'}
 if base&white:continue
 extra=required-base;assert not extra&past
 B=base|extra;p=(0,0);h=ha
 for c in iw*30+cap:p,h,cc=step(B,p,h);assert cc==c
 assert first_mismatch(State(frozenset(B),p,h),ow) is None
 res.append(dict(**case,extra_count=len(extra),extra_relative_cap=sorted((x-capP[0],y-capP[1])for x,y in extra),base_count=len(base),input_head=ha,cap_pose=[capP,capH],tail_pose=[p,h]))
res.sort(key=lambda c:(c['extra_count'],c['in_phase'],c['out_phase']))
(P/'single_turn_corner_selected.json').write_text(json.dumps(dict(scope=__doc__,exact_finite_m30_tail_passes=len(res),cases=res),indent=2)+'\n')
print('counts',len(res));print(*res[:10],sep='\n')
