"""Literal prepared102-read BLACK-helper connector, not a complete front.
Explicit17-cell input, actual ant replay and complete WITHIN-FACTOR histories.
"""
from pathlib import Path
from collections import Counter
import json
H='NESW';D=[(0,1),(1,0),(0,-1),(-1,0)]
WORD='RRRRLRRRRLRRRRLLLLRLLLLRLRRRRLLLLRLLLLRLRRLLRRRRLLRRLLLLRRLLRLLLLRLRRLLLLRRLRRRRLLLLRLLRLLRRLRLLRLLRLL'
SEED=[(-3,0),(-3,1),(-2,-1),(-2,2),(-2,3),(-2,4),(-1,-2),(-1,5),(0,-2),(0,5),(1,3),(1,4),(2,3),(2,4),(3,-1),(3,4),(4,3)]
KNOWN={(1,0):'NNSN',(0,0):'WWEW',(0,1):'NSSS',(1,1):'EEWE',(0,-1):'SSSN',(-1,-1):'WWWE',(-1,0):'NNSN',(-2,0):'WWWE',(-2,1):'NNNS',(-1,1):'EEWE',(-1,2):'NNNS',(0,2):'EWEE',(1,2):'NNNS',(2,2):'EEEW',(2,1):'SSNS',(-2,2):'W'}
assert len(WORD)==102 and len(SEED)==17 and len(set(SEED))==17
seed=set(SEED);B=set(seed);p=(1,0);k=0;hist={};trace=[]
for t,w in enumerate(WORD):
 c='L'if p in B else'R';assert c==w,(t,p,c,w)
 o=(k+(1 if c=='R'else -1))%4;z=dict(time=t,cell=p,incoming=H[k],turn=c,outgoing=H[o]);trace.append(z);hist.setdefault(p,[]).append(z)
 if p in B:B.remove(p)
 else:B.add(p)
 dx,dy=D[o];p=(p[0]+dx,p[1]+dy);k=o
assert(p,H[k])==((0,3),'N') and len(B)==9
assert max(map(len,hist.values()))==4
for q,h in KNOWN.items():
 assert ''.join(z['incoming']for z in hist[q])==h
 assert ''.join(z['turn']for z in hist[q])==('L'if q==(-2,2)else'RLRL')
 assert(q in seed)==(q==(-2,2))
faces=dict(D=(0,0),J=(-1,-1),P0=(-2,0),I=(-1,1),G=(1,1));births={};bounds={}
for n,(x,y)in faces.items():
 ports=[((x+1,y),'W'),((x,y),'N'),((x,y+1),'E'),((x+1,y+1),'S')]
 reads=[z for z in trace if(z['cell'],z['outgoing'])in ports];births[n]=min(z['time']for z in reads);bounds[n]=[dict(cell=q,direction=o,first=min(z['time']for z in trace if z['cell']==q and z['outgoing']==o))for q,o in ports]
assert births==dict(D=4,J=9,P0=24,I=39,G=43)
route=[((-1,1),2),((-1,2),1),((-2,2),0),((-2,1),3),((-1,1),3)];rt=[hist[q][rank]['time']for q,rank in route];assert rt==[51,52,53,54,55]
out=dict(scope=__doc__,word=WORD,prepared_black=SEED,initial_pose=dict(cell=[1,0],incoming='N'),end_pose=dict(cell=p,incoming=H[k]),length=102,initial_black_count=17,final_black_count=9,read_turn_counts=dict(Counter(WORD)),visited_cells=len(hist),maximum_reads=max(map(len,hist.values())),visit_spectrum=dict(Counter(map(len,hist.values()))),known_headings={str(q):h for q,h in KNOWN.items()},known_read_times={str(q):[z['time']for z in hist[q]]for q in KNOWN},first_boundary_times=births,boundary_first_departures=bounds,exact_helper_route_times=rt,trace=trace,complete_finite_headings={str(q):''.join(z['incoming']for z in h)for q,h in hist.items()},complete_finite_turns={str(q):''.join(z['turn']for z in h)for q,h in hist.items()},final_black=sorted(B))
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2)+'\n');print('PASS literal102 reads,17->9 prepared mass, cap4, fifteen WHITE RLRL cells and one BLACK singleton helper')
