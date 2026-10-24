#!/usr/bin/env python3
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
raw=json.loads((R/'continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json').read_text())
M=json.loads((R/'word_stabilization/cfree_kernel_current_marks.json').read_text())
D=((0,1),(1,0),(0,-1),(-1,0));F={};E={};phase={}
for a in 'UVQB':
 x=y=h=0;f=set();ph={}
 for i,c in enumerate(raw[a]['word']):
  f.add((x,y));ph.setdefault((x,y),[]).append([i,c]);h=(h+(1 if c=='R' else -1))%4;dx,dy=D[h];x+=dx;y+=dy
 F[a]=f;E[a]=(x,y,h);phase[a]=ph
 assert {(-1,0),(0,1),(1,2)}<=f
 assert tuple([1,2] if a=='V' else [-1,0]) in map(tuple,M[a])
def rot(q,h):
 x,y=q
 for _ in range(h%4):x,y=y,-x
 return x,y
def cen(p,h):
 a,b=rot((-1,1),h);return 2*p[0]+a,2*p[1]+b
def tr(q,p,h):
 x,y=rot(q,h);return x+p[0],y+p[1]
rows=[]
for a in'UVQB':
 assert cen((0,0),0)!=cen(E[a][:2],E[a][2])
 h=(2-E[a][2])%4;dx,dy=rot(E[a][:2],h);p=(-1-dx,1-dy)
 mark={tr(q,p,h):q for q in M[a]}
 targets=[(-1,2)]+([(0,3)] if a in'UB' else [(1,4)] if a=='Q' else [])
 assert all(t in mark for t in targets)
 rows.append({'predecessor':a,'entry':[*p,h],'witnesses':[{'physical':t,'local':mark[t],'read_phases':phase[a][tuple(mark[t])]} for t in targets]})
 # Two-block V+a geometry, literally compose endpoints.
 ex,ey,eh=E[a];end=(E['V'][0]+ex,E['V'][1]+ey)
 assert cen(end,eh)!=cen((0,0),0)
for a in'QB':assert(-2,-1)in F[a]
for a in'UVQB':
 assert (0,-1) in F[a]
 terminal=tr((0,-1),E[a][:2],E[a][2])
 assert terminal in set(map(tuple,M[a]))
for a in'UQB':assert(-1,2)in F[a]
assert(-1,2)in F['U'];assert E['V']==(1,3,0)
assert cen((0,0),0)==cen((-1,1),2)
assert cen((1,3),0)==cen((0,4),2)
out={'status':'All literal ingredients for minimum-span descent verified independently','macro_word_hash':hashlib.sha256(''.join(raw[a]['word'] for a in'UVQB').encode()).hexdigest(),'rows':rows,'endpoints':E,'scope':'Macro starts plus terminal boundary in feasible C-free words; terminal-star relation and endpoint descent checked; relies on audited29-site freshness'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
