"""Full-field literal replay of prepared F84/F85 LL-drop controls.
Only the explicit word/seed are used; no symbolic interface solver is imported.
Not complete WHITE fronts, translating boards, or regenerative controllers.
"""
from pathlib import Path
from collections import defaultdict,Counter
import json
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
W='RRRRLRRRRLRRLRRLRRLLLLRRLRRLRLRLRRLRLRRLRLRRRRLRLRRLRLRLRLRRLRLRLRRLRLLLLRRRRLRLRRLL'
SEED=[(-1,-3),(-1,-2),(-1,1),(-1,2),(0,-4),(0,-1),(0,3),(1,-4),(1,-1),(1,4),(2,-3),(2,5),(3,-2),(3,0),(3,1),(3,5),(4,4),(5,0),(5,2),(5,3)]
TARGET={(1,0):'WWEW',(1,1):'SSN',(2,0):'SNNN',(2,1):'EE'}
def replay(name,word,seed,start):
 black=set(seed);p,head=start;hist=defaultdict(list);trace=[];edges=[]
 for t,want in enumerate(word):
  tr='L'if p in black else'R';assert tr==want,(name,t,p,head,tr,want)
  before=sorted(black);black.symmetric_difference_update({p});nh=H[(H.index(head)+(1 if tr=='R'else-1))%4];v=V[nh];q=p[0]+v[0],p[1]+v[1]
  hist[p].append(dict(t=t,incoming=head,turn=tr));trace.append(dict(t=t,cell=p,incoming=head,turn=tr,black_before=before,black_after=sorted(black),next_cell=q,next_incoming=nh));edges.append((p,q));p,head=q,nh
 assert (p,head)==((1,-1),'S')and max(map(len,hist.values()))==4
 assert all(q not in seed for q in TARGET)
 for q,h in TARGET.items():assert ''.join(z['incoming']for z in hist[q])==h and ''.join(z['turn']for z in hist[q])==''.join('R'if r%2==0 else'L'for r in range(len(h)))
 # Exact physical one-use boundary arc through the LL bit drop.
 for e in [((0,0),(1,0)),((1,0),(1,1)),((1,1),(0,1))]:assert edges.count(e)==1
 assert (1,-1)in black # immediate R-start repetition is illegal.
 return dict(name=name,word=word,initial_black=sorted(seed),start=start,end=[p,head],final_black=sorted(black),mass=[len(seed),len(black)],turns=dict(Counter(word)),factor_max_reads=4,physical_cells_read=len(hist),trace=trace,histories={str(q):z for q,z in sorted(hist.items())},target_histories={str(q):hist[q]for q in TARGET},selected_one_use_edges=[[[0,0],[1,0]],[[1,0],[1,1]],[[1,1],[0,1]]],all_target_R0s_physically_supplied=name=='F85',warning='Prepared finite factor only; complete full-drift histories, GLOBAL-M terrain, essential b-circle and board-period equality are NOT supplied.')
a=replay('F84',W,set(SEED),((1,1),'S'));c=replay('F85','L'+W,set(SEED)|{(1,2)},((1,2),'W'))
assert a['mass']==[20,36]and c['mass']==[21,36]and a['final_black']==c['final_black']
assert len(W)==84 and len(c['word'])==85 and a['turns']=={'R':50,'L':34}and c['turns']=={'L':35,'R':50}
for q in TARGET:
 assert [z['t']for z in c['target_histories'][str(q)]]==[z['t']+1for z in a['target_histories'][str(q)]]
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,controls=[a,c],warning='The discovery builder had lazily installed untouched future seed cells in its early diagnostic boards. This certificate instead replays every read from the COMPLETE explicit initial seed, and is the only submitted full-field replay.'),indent=2)+'\n')
print('PASS F84/F85 full fields,20/21 BLACK seeds->36,13 target WHITE reads,all physical multiplicities<=4; no immediate repeat')
