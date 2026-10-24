#!/usr/bin/env python3
"""Author positive controls, reconstructs geometry without solver imports."""
import json
from pathlib import Path
D=((0,1),(1,0),(0,-1),(-1,0));cases=[(3,1,3),(3,3,3),(3,1,3,1),(3,1,3,3),(3,3,3,1),(3,3,3,3)]
root=Path(__file__).parent;results=[]
for case in range(6):
 f=root/(f'cap4_real_patch_r2_c{case}_max1.json' if case in (2,5) else f'cap4_chains_r2_c{case}_globalmax.json')
 d=json.loads(f.read_text());assert d['status']=='SAT_LOCAL_CHAIN_ORDER_ONLY';cert=d['certificate'];cells={tuple(c['position']):c for c in cert['cells']};ps={(x,y) for x in range(-2,3) for y in range(-2,3)}
 times=[]
 for p,c in cells.items():
  h=c['headings'];ts=c['times'];assert p in ps and 1<=len(h)<=4 and len(h)==len(ts)
  assert all(x%2==1-sum(p)%2 for x in h) and all(isinstance(t,int) for t in ts) and all(a<b for a,b in zip(ts,ts[1:]));times+=ts
 assert len(times)==len(set(times));assert tuple(cells[0,0]['headings'])==cases[case]
 def events(p,h,kind):
  c=cells.get(p,{'headings':[],'times':[]})
  return [t for j,(x,t) in enumerate(zip(c['headings'],c['times'])) if (x if kind=='in' else (x+(1 if j%2==0 else -1))%4)==h]
 edges=0
 for p in ps:
  for h,(dx,dy) in enumerate(D):
   if h%2!=sum(p)%2:continue
   q=p[0]+dx,p[1]+dy
   if q not in ps:continue
   a=events(p,h,'out');b=events(q,h,'in');assert len(a)==len(b) and all(y==x+1 for x,y in zip(a,b));edges+=len(a)
 z={tuple(a['face']):a['depth'] for a in cert['shifted_height_depths']};assert len(z)==36 and z[0,0]==0 and all(isinstance(v,int) and v>=0 for v in z.values());he=0
 for x,y in z:
  for ax,ay in ((1,0),(0,1)):
   q=x+ax,y+ay
   if q not in z:continue
   u,v=((x+1,y),(x+1,y+1)) if ax else ((x,y+1),(x+1,y+1));h=D.index((v[0]-u[0],v[1]-u[1]))
   if sum(u)%2!=h%2:u,v=v,u;h=(h+2)%4
   fcount=len(events(u,h,'out')) if u in ps else len(events(v,h,'in'))
   C,L=((x,y),q) if (x+y)%2==0 else (q,(x,y));assert z[L]+1==z[C]+fcount;(he:=he+1)
 results.append(dict(case=case,source=f.name,active_cells=len(cells),events=len(times),internal_arcs=edges,height_edges=he,checked=True))
out=dict(status='ALL_SIX_RADIUS_TWO_GLOBALMAX_LOCAL_MODELS_CHECKED',scope='Open-patch complete histories with distinct chronology and global-maximum height restriction; not full orbits.',cases=results)
(root/'cap4_globalmax_local_controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
