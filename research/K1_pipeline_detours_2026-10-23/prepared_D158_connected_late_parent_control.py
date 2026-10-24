"""Replay one literal prepared connected cap-four late-parent control.
Finite factor only. All sixteen designated cells start WHITE and are read four times.
The 37 prepared black exterior cells are explicit fuel, not renewable WHITE input.
"""
from pathlib import Path
from collections import defaultdict,Counter
import ast,json,hashlib
src=Path(__file__).with_name('prepared_D4_finish_fixed_prefix.json');r=json.loads(src.read_text());H='NESW';V=((0,1),(1,0),(0,-1),(-1,0));word=r['word'];seed={tuple(p)for p in r['prepared_black']};black=set(seed);p=(1,0);h=0;hh=defaultdict(str);events=defaultdict(list);turns=defaultdict(str);trace=[]
for t,w in enumerate(word):
 actual='L'if p in black else'R'
 assert actual==w,(t,p,w,actual)
 trace.append(dict(time=t,cell=p,incoming=H[h],turn=w));hh[p]+=H[h];turns[p]+=w;events[p].append(t)
 if p in black:black.remove(p)
 else:black.add(p)
 h=(h+(1 if w=='R'else-1))%4;dx,dy=V[h];p=p[0]+dx,p[1]+dy
known={ast.literal_eval(k):v for k,v in r['inventory'].items()}
assert seed.isdisjoint(known)
assert len(word)==158 and len(seed)==37
assert all(hh[q]==want and turns[q]=='RLRL'for q,want in known.items())
assert max(map(len,hh.values()))==4
faces=dict(D=(0,0),J=(-1,-1),P0=(-2,0),I=(-1,1),G=(1,1))
births={};boundary={}
for name,(x,y)in faces.items():
 bd=[((x+1,y),'W'),((x,y),'N'),((x,y+1),'E'),((x+1,y+1),'S')]
 out=[]
 for q,o in bd:
  e=[a for a in trace if tuple(a['cell'])==q and H[(H.index(a['incoming'])+(1 if a['turn']=='R'else-1))%4]==o]
  assert e
  out.append(dict(cell=q,direction=o,first=e[0]['time']))
 boundary[name]=out;births[name]=min(a['first']for a in out)
assert births==dict(D=4,J=9,P0=24,I=39,G=43)
ans=dict(scope=__doc__,initial_pose=dict(cell=(1,0),incoming='N'),end_pose=dict(cell=p,incoming=H[h]),length=len(word),prepared_black=sorted(seed),initial_black_count=len(seed),final_black_count=len(black),read_turn_counts=dict(Counter(word)),visited_cells=len(hh),maximum_reads=4,visit_spectrum=dict(Counter(map(len,hh.values()))),known_headings={str(q):s for q,s in known.items()},known_read_times={str(q):events[q]for q in known},face_lower_left=faces,first_boundary_times=births,boundary_first_departures=boundary,word=word,trace=trace,complete_finite_headings={str(q):s for q,s in hh.items()},complete_finite_turns={str(q):s for q,s in turns.items()},final_black=sorted(black))
pth=Path(__file__).with_suffix('.json');pth.write_text(json.dumps(ans,indent=2)+'\n')
print(json.dumps({k:v for k,v in ans.items()if k not in['prepared_black','known_headings','known_read_times','boundary_first_departures','word','trace','complete_finite_headings','complete_finite_turns','final_black']},indent=2))
print('certificate_sha256',hashlib.sha256(pth.read_bytes()).hexdigest())
