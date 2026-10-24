"""Literal prepared F106/F107 controls for one exact odd-root portal reader patch.
Full finite fields and every raw read are retained. The named core is WHITE,
but guide stock is prepared. No full future, GLOBAL-M complete front, essential
b-circle, archive closure, recurrence or autonomous controller is supplied.
"""
from pathlib import Path
from collections import defaultdict,Counter
import json
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
WORD='RRRRLRRRRLRLRRLRLRLRRLRLRLRRLRRRRLLLLRLRRRRLRRLLRRLRLRLRRLRLRLRRLRLLLLRRRRLRLRLRRLLLLRRLRRRRLLLLRLRLLLLRRR'
SEED={(-3,2),(-2,0),(-2,1),(-1,-1),(-1,4),(-1,5),(-1,6),(0,-2),(0,7),(1,-2),(1,8),(2,-1),(2,8),(3,0),(3,1),(3,7),(4,-1),(4,3),(4,5),(4,6)}
CORE={(-1,0):'',(-1,1):'SS',(-1,2):'EEWW',(-1,3):'NN',(0,0):'',(0,1):'WE',(0,2):'SNN',(0,3):'E',(1,0):'W',(1,1):'SSNS',(1,2):'WWEW',(1,3):'N',(2,0):'SSN',(2,1):'EEE',(2,2):'SSSN',(2,3):'WWEW'}
def replay(word,seed,start,name):
 p,h=start;black=set(seed);trace=[];hist=defaultdict(list);edges=Counter()
 for t,a in enumerate(word):
  assert a==('L' if p in black else 'R'),(name,t,p,h,a)
  before=sorted(black);co=H[(H.index(h)+(1 if a=='R' else -1))%4]
  nxt=p[0]+V[co][0],p[1]+V[co][1];black.symmetric_difference_update({p})
  event=dict(t=t,cell=p,incoming=h,turn=a,black_before=before,black_after=sorted(black),next_cell=nxt,next_incoming=co)
  trace.append(event);hist[p].append(event);edges[p,nxt]+=1;p,h=nxt,co
 assert (p,h)==((3,0),'E') and len(hist)==63 and max(map(len,hist.values()))==4
 for q,expected in CORE.items():
  assert q not in seed
  assert ''.join(e['incoming'] for e in hist[q])==expected
  assert ''.join(e['turn'] for e in hist[q])==''.join('R' if r%2==0 else 'L' for r in range(len(expected)))
 assert len(black)==34 and p not in black
 path=[(2,0),(1,0),(1,1),(0,1),(0,2),(-1,2),(-1,1),(-2,1)]
 assert [edges[a,b] for a,b in zip(path,path[1:])]==[1,1,1,2,2,2,1]
 firstR={q:next((e for e in es if e['turn']=='R'),None) for q,es in hist.items()}
 # First R OBSERVED IN THIS FACTOR may land at later target ranks. The
 # lower old guide supplies X.R2, not X.R0. No whole-history first R at
 # that prepared guide is identified.
 assert firstR[(2,-1)]['next_cell']==(2,0)
 assert firstR[(2,-1)]['t']+1==hist[(2,0)][2]['t']
 assert firstR[(2,0)]['next_cell']==(1,0) and firstR[(1,0)]['next_cell']==(1,1)
 assert firstR[(1,0)]['t']+1==hist[(1,1)][2]['t']
 targets={str(q):dict(history=expected,times=[e['t'] for e in hist[q]],initial_WHITE=True,final_BLACK=q in black) for q,expected in CORE.items()}
 return dict(name=name,word=word,start=start,end=[p,h],initial_black=sorted(seed),final_black=sorted(black),initial_mass=len(seed),final_mass=len(black),R=word.count('R'),L=word.count('L'),physical_cells=len(hist),factor_max_reads=max(map(len,hist.values())),targets=targets,selected_physical_path=path,selected_edge_uses=[edges[a,b] for a,b in zip(path,path[1:])],all_cell_histories={str(q):dict(history=''.join(e['incoming'] for e in es),turns=''.join(e['turn'] for e in es),times=[e['t'] for e in es],initial_BLACK=q in seed) for q,es in sorted(hist.items())},trace=trace)
a=replay(WORD,SEED,((2,3),'W'),'F106')
b=replay('L'+WORD,SEED|{(3,3)},((3,3),'N'),'F107')
assert len(WORD)==106 and(a['initial_mass'],a['R'],a['L'])==(20,60,46)
assert (b['initial_mass'],b['R'],b['L'])==(21,60,47)
assert a['final_black']==b['final_black'] and len(a['all_cell_histories']['(3, 3)']['times'])==3 and len(b['all_cell_histories']['(3, 3)']['times'])==4
for q,h in CORE.items():
 if h:
  for obj in [a,b]:
   t=obj['targets'][str(q)]['times'][0]
   if obj is b:assert t>0 and tuple(obj['trace'][t-1]['next_cell'])==q
obj=dict(scope=__doc__,controls=[a,b],warning='All histories are factor-only. Twenty/twenty-one prepared BLACK cells are retained. The lower guide (2,-1) starts BLACK/L in the factor before its later first R. No whole-history WHITE conversion, GLOBAL-M contour, complete essential circle, full displacement/heading field equality or reusable output-funding mechanism is certified.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n')
print('PASS preparedF106/F107: full fields20/21->34;63cells,max4;16 WHITE target histories/two unused; odd-root mixed path; factor-observed R-to-later-rank guide retained')
