"""Literal connected prepared48 control realizing the even one-use LL
portal. Full finite field retained. NOT a complete WHITE front, global
max-stream b-circle, immediately repeated word or autonomous controller.
"""
from pathlib import Path
from collections import defaultdict,Counter
import json
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
WORD='RRRRLRRRRLRRLRRLRLRRLRRLLLLRRLRLLRLLRRLLRLLRLRLL'
SEED={(-3,3),(-3,4),(-2,0),(-2,1),(-2,5),(-1,2),(-1,5),(0,2),(0,5),(1,5),(2,3),(2,4)}
TARGET={(0,0):'NNSS',(1,0):'EE',(1,1):'SN',(0,1):'EWWE'}
p=(0,0);h='N';black=set(SEED);trace=[];hist=defaultdict(list);edges=Counter()
for t,w in enumerate(WORD):
 a='L'if p in black else'R';assert a==w
 before=sorted(black);oldp=p;oldh=h
 if p in black:black.remove(p)
 else:black.add(p)
 h=H[(H.index(h)+(1 if a=='R'else-1))%4];p=p[0]+V[h][0],p[1]+V[h][1];edges[oldp,p]+=1
 e=dict(t=t,cell=oldp,incoming=oldh,turn=a,black_before=before,black_after=sorted(black),next_cell=p,next_incoming=h)
 trace.append(e);hist[oldp].append(e)
assert len(WORD)==48 and(p,h)==((0,2),'N')and len(SEED)==12 and len(black)==16
assert max(map(len,hist.values()))==4 and len(hist)==34
for q,word in TARGET.items():
 assert q not in SEED and ''.join(e['incoming']for e in hist[q])==word
 assert ''.join(e['turn']for e in hist[q])==('RLRL'if len(word)==4 else'RL')and q not in black
assert edges[(1,2),(1,1)]==1 and edges[(1,0),(1,-1)]==1
assert [edges[e]for e in[((1,1),(0,1)),((0,1),(0,0)),((0,0),(1,0))]]==[2,2,2]
assert [(trace[t]['cell'],trace[t]['turn'])for t in range(23,28)]==[((0,1),'L'),((0,0),'L'),((1,0),'L'),((1,1),'L'),((0,1),'R')]
assert p in black # nextR would be illegal, so exact word cannot immediately repeat.
obj=dict(scope=__doc__,word=WORD,initial_black=sorted(SEED),start=[(0,0),'N'],end=[p,h],initial_mass=len(SEED),final_mass=len(black),final_black=sorted(black),physical_cells=len(hist),factor_max_cell_reads=4,targets={str(q):dict(incoming=''.join(e['incoming']for e in hist[q]),turns=''.join(e['turn']for e in hist[q]),times=[e['t']for e in hist[q]],initial_WHITE=q not in SEED,final_WHITE=q not in black)for q in TARGET},one_use_boundary_edges=[dict(source=s,target=t,count=edges[s,t])for s,t in[((1,2),(1,1)),((1,0),(1,-1))]],actual_four_L_times=[23,24,25,26,27],all_cell_histories={str(q):dict(incoming=''.join(e['incoming']for e in es),turns=''.join(e['turn']for e in es),times=[e['t']for e in es])for q,es in sorted(hist.items())},trace=trace,warning='Factor-only histories. Twelve prepared BLACK cells are mandatory. Later target visits after time48 are unclassified. No full-drift field equality/global max-stream/front or repeatability is asserted; endpoint is BLACK so immediate nextR fails.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS preparedF48: fullfield12->16,34cells,max4,12WHITEportalreads,oneuseedges,BLACKendpoint')
