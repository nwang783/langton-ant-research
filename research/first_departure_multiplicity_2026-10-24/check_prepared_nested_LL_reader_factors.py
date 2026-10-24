"""Literal finite prepared controls for the nested reader words only.
These omit every earlier/future complete-WHITE supplier obligation and are
NOT complete reader inventories, fronts, regenerative factors or controllers.
"""
from pathlib import Path
import json
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
start=(2,-1);heading='E'
cases=[('eight','LLRRRRLL',{(2,-1),(2,0),(1,-1)}),('twelve','LLRRLLLLRRLL',{(2,-1),(2,0),(2,1),(2,2),(1,2),(1,-1)})]
rows=[]
for name,word,seed in cases:
 black=set(seed);p=start;h=heading;tr=[];reads={}
 for t,w in enumerate(word):
  actual='L'if p in black else'R';assert actual==w
  tr.append(dict(t=t,cell=p,incoming=h,turn=actual,black_before=sorted(black)))
  reads[p]=reads.get(p,0)+1
  if p in black:black.remove(p)
  else:black.add(p)
  h=H[(H.index(h)+(1 if actual=='R'else-1))%4];p=p[0]+V[h][0],p[1]+V[h][1]
 assert(p,h)==(start,heading)and start not in black
 assert (len(seed),len(black))==((3,3)if name=='eight'else(6,2))
 rows.append(dict(name=name,word=word,initial_black=sorted(seed),final_black=sorted(black),start=[start,heading],end=[p,h],mass=[len(seed),len(black)],trace=tr,max_factor_cell_reads=max(reads.values()),returned_root_white=True))
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,cases=rows,warning='Root is WHITE on return; neither word can immediately repeat. No full-WHITE earlier R0 histories or open future L3 field is supplied.'),indent=2)+'\n');print('PASS prepared8 mass3->3 and prepared12 mass6->2; full pose, rootWHITE, no repetition')
