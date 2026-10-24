"""Finite actual C-projection/WHITE-parent first-entry forest of signedF49.
Distinguishes internal R0 color production from BLACK-root face ancestry.
"""
from pathlib import Path
import json
p=Path(__file__).with_name('check_prepared_F49_portal_external_entry.json');j=json.loads(p.read_text());V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
def c_right(p,h):
 x,y=p;return {'E':(x,y-1),'W':(x-1,y),'N':(x,y),'S':(x-1,y-1)}[h]
p,h=j['start'];p=tuple(p);cur=c_right((p[0]-V[h][0],p[1]-V[h][1]),h);first={cur:dict(time=-1,type='initial')};root={cur:cur};R0={};vis={};owners={};C_states=[cur]
for e in j['trace']:
 p=tuple(e['cell']);rank=vis.get(p,0);vis[p]=rank+1
 if rank==0 and e['turn']=='R':R0[p]=cur
 if rank==1 and p in R0:owners[p]=R0[p]
 nxt=c_right(p,e['next_incoming'])
 if e['turn']=='R':assert nxt==cur
 if nxt not in first:
  assert e['turn']=='L'
  if p in R0:
   assert rank==1;par=R0[p];rt=root[par];tag='WHITE'
  else:assert rank==0;par=None;rt=nxt;tag='BLACK'
  first[nxt]=dict(time=e['t'],cell=p,rank=rank,type=tag,parent=par,basin=rt);root[nxt]=rt
 cur=nxt;C_states.append(cur)
F,H,G=(0,-1),(0,1),(1,0)
assert first[F]['type']=='BLACK'and first[F]['time']==0
assert first[H]['type']=='BLACK'and first[H]['time']==21
assert first[G]['type']=='WHITE'and first[G]['time']==26 and first[G]['parent']==F
assert owners[(1,0)]==F and owners[(1,1)]==H and root[F]!=root[H]
assert [i for i,f in enumerate(C_states)if f==G]==[27]
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,all_first_entries={str(f):d for f,d in first.items()},R0_owner_faces={str(p):f for p,f in owners.items()},leaf_G=G,first_entry_parent=F,exit_color_producer_face=H,distinct_BLACK_basins=True,internal_color_production_times={'A':[2,26],'B':[23,27]},warning='Finite factor forest only. Not a full-quotient one-basin example, a first-entry-cycle/root count or an auxiliary-incidence merger theorem.'),indent=2)+'\n');print('PASS internalA/B R0 color production, distinctBLACKbasinsF/H, WHITE leafG parentF')
