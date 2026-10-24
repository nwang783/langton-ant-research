"""Literal prepared prefix for one fixed all-four D4 late-parent inventory.
Not a complete front or full completion of every local four-read history.
"""
from pathlib import Path
import json,ast
H='NESW';D=((0,1),(1,0),(0,-1),(-1,0))
row=json.loads(Path(__file__).with_name('canonical_duplicator_local_parent_return.json').read_text())['rows'][0]
hh={ast.literal_eval(k):v for k,v in row['headings'].items()}
seed={(-1,-2),(0,-2),(-2,-1),(-3,1),(-3,0),(-2,3),(-3,3),(-3,2),(-1,3),(-1,4),(-2,5),(-3,5),(-4,4),(-5,3),(-5,2),(-4,1)}
black=set(seed);seen={};p=(1,0);h=0;trace=[];failure=None
for step in range(300):
 if p==(2,3)and seen.get((2,2),0)==2:break
 r=seen.get(p,0)
 if p in hh and(r>=len(hh[p])or hh[p][r]!=H[h]):failure=dict(time=step,p=p,h=H[h],rank=r);break
 turn='L'if p in black else'R';trace.append(dict(time=step,p=p,incoming=H[h],turn=turn,known=p in hh,rank=r))
 if p in black:black.remove(p)
 else:black.add(p)
 seen[p]=r+1;h=(h+(1 if turn=='R'else-1))%4;dx,dy=D[h];p=(p[0]+dx,p[1]+dy)
else:failure='time_guard'
ans=dict(scope=__doc__,inventory=row['headings'],prepared_black=sorted(seed),end_pose=[p,H[h]],raw_length=len(trace),known_reads=sum(v for p,v in seen.items()if p in hh),known_ranks={str(p):seen.get(p,0)for p in hh},failure=failure,word=''.join(x['turn']for x in trace),trace=trace,current_black=sorted(black),all_seen={str(p):n for p,n in seen.items()})
Path(__file__).with_suffix('.json').write_text(json.dumps(ans,indent=2)+'\n')
print(json.dumps({k:v for k,v in ans.items()if k not in ['inventory','trace','word','current_black','all_seen']},indent=2))
