"""Add the five signed delayed-height max registers to exact height Petri edges.
The backward solver stores their minimum demands, not an expanded control product.
"""
from pathlib import Path
import json,sys,hashlib
src,out=map(Path,sys.argv[1:3]);J=json.loads(src.read_text());S=json.loads(Path(J['source_file']).read_text());acts={(a[0],a[1]):a for a in S['actions']};F=J['initial_bound'];rules=Path('chronology_dcuv/counted_input_age_rules_complete.json');target=S['target']
def extra(p,a):
 h,q=J['poses'][J['positions'][p][0]];v=acts[h,a];c=v[2]
 # A low-bin source was chosen below all input/output F crossings.
 if q is None:return [c,0,0,0,0,0,0]
 mi=[max(0,q+x-F)if x>-900 else 0 for x in v[7:]]
 return [c,max(0,q+v[5]-F)]+mi
E=[e+extra(e[0],e[2]) for e in J['transitions']];goals=[]
for p,r in J['goal_requirements']:
 qs=extra(p,target)[2:]
 for i in range(3,-1,-1):qs[i]=max(qs[i],qs[i+1])
 goals.append([p,r+qs])
N={k:v for k,v in J.items()if k not in ['transitions','goal_requirements']};N.update(format='record_height_petri_delays_v1',base_model_file=str(src.resolve()),base_model_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),rules_file=str(rules.resolve()),rules_sha256=hashlib.sha256(rules.read_bytes()).hexdigest(),Q_offset=F,Q_max_offset=J['height_cap']-F,goal_requirements=goals,transitions=E,scope='Exact high-height counts plus five monotone signed-age height envelopes, each stored as an offset from F. Initial counters and envelope offsets are all zero. Backward requirements use the ordered Q0>=...>=Q4 domain.')
out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f'{len(J["places"])} {len(J["positions"])} {len(E)} {len(J["initial_controls"])} {len(goals)} {N["Q_max_offset"]}\n');f.write(' '.join(map(str,J['initial_controls']))+'\n')
 for p,r in goals:f.write(' '.join(map(str,[p]+r))+'\n')
 for p,q,a,i,o,c,H,*mi in E:f.write(' '.join(map(str,[p,q,a]+i+o+[c,H]+mi))+'\n')
print({'count_places':len(J['places']),'Q_requirements':5,'edges':len(E)})
