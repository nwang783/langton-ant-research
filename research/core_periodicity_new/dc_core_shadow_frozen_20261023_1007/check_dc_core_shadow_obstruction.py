"""Complete all-age residual-origin shadow for protected DC sibling pairs.
No C threshold, word-depth bound, initial-root assumption, or search cap.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,hashlib
R=Path(__file__).resolve().parent;gp=R/'chronology_dcuv/literal_residual_geometry.json';J=json.loads(gp.read_text());G=J['geometry'];IDS=(0,1,4,5,6,7,8,9);K={tuple(p)for p in J['core']}
def rot(q,h):x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return(p[0]+q[0],p[1]+q[1])
def sub(p,q):return(p[0]-q[0],p[1]-q[1])
P=[tuple(q)for q in G[1]['outputs']];q=(2,1);ep=G[1]['endpoint'][:2];eh=G[1]['endpoint'][2];exitcore={add(ep,rot(z,eh))for z in K};assert q in exitcore and q not in P
# Derive every complete context independently from its raw word plus actual M11.
D=((0,1),(1,0),(0,-1),(-1,0));ctx={}
for a in IDS:
 pp=(0,0);hh=0;last={};req={}
 for c in G[a]['word']+G[a]['marker']:
  assert last.get(pp)!=c;req.setdefault(pp,c=='L');last[pp]=c;hh=(hh+(-1 if c=='L'else 1))%4;pp=add(pp,D[hh])
 assert req=={tuple(z[:2]):z[2]for z in G[a]['requirements']};ctx[a]=req
rows=[]
for a in IDS:
 for h in range(4):
  for oi,z in enumerate(G[a]['outputs']):
   p=sub(q,rot(z,h))
   if(sum(p)-h)%2:continue
   req=ctx[a];I={tuple(v)for v in G[a]['inputs']};hits=[]
   for si,w in enumerate(P):
    rel=rot(sub(w,p),-h)
    if rel in req:hits.append({'source_output_index':si,'source_cell':w,'producer_local_cell':rel,'role':'input'if rel in I else'core'if rel in K else'white'if not req[rel]else'other_black'})
   assert hits
   rows.append({'producer':a,'name':G[a]['name'],'pose':[*p,h],'output_slot_index':oi,'output_slot':z,'created_residual_cell':q,'protected_source_hits':hits})
assert len(rows)==136
covers=[]
for n in range(1,5):
 for ss in combinations(range(4),n):
  if all(set(ss)&{z['source_output_index']for z in r['protected_source_hits']}for r in rows):
   if not any(set(t)<=set(ss)for t in covers):covers.append(ss)
assert covers==[(0,2),(0,3)]
# All U-family input placements simultaneously containing the three old spares.
targets=[];S=set(P[1:])
for a in(7,8,9):
 seen=set()
 for h in range(4):
  for w in S:
   for v in G[a]['inputs']:
    p=sub(w,rot(v,h))
    if(sum(p)-h)%2:continue
    key=(*p,h)
    if key in seen:continue
    seen.add(key);I={add(p,rot(z,h))for z in G[a]['inputs']}
    if S<=I:targets.append({'packet':a,'pose':[*p,h],'inputs':sorted(I),'contains_all_four_source_output_cells':set(P)<=I,'fifth_input':sorted(I-set(P))})
assert len(targets)==3 and all(t['pose']==[3,-1,0]and t['contains_all_four_source_output_cells']and t['fifth_input']==[q]for t in targets)
O={'status':'AUTHOR_COMPLETE_ALL_AGE_PROTECTED_ORIGIN_SHADOW_PASS','scope':'All later marked boundaries in one complete recurrent-eight interval, exact old ordered residual identities. No initial-root/backlog restriction; no actual helper path asserted.','source_DC_pose':[0,0,0],'source_outputs':P,'source_exit_core':sorted(exitcore),'shadow_cell':q,'initial_shadow_cell_is_residual':False,'all_sector_output_producers':rows,'output_producer_count':len(rows),'minimal_protected_source_output_index_covers':covers,'equivalent_creation_precondition':'Before(2,1) can enter the residual ledger, either originalA=(2,0) has retired, OR BOTH originalC=(3,1) and originalD=(3,2) have retired.','all_three_spare_U_family_targets':targets,'all_age_exclusion':'No U/UC/UCC packet can consume all four old residual outputs of one DC simultaneously.','bulk_three_spare_consequence':'A U-family packet consuming all three old DC spares must have retired the old mainA strictly earlier; its input at physical cellA is a different replacement identity.','coverage_hitset_profile':{str(k):v for k,v in Counter(tuple(z['source_output_index']for z in r['protected_source_hits'])for r in rows).items()},'input_sha256':hashlib.sha256(gp.read_bytes()).hexdigest()}
(R/'chronology_dcuv/dc_core_shadow_obstruction.json').write_text(json.dumps(O,indent=2)+'\n');print({'all_sector_output_producers':len(rows),'minimal_protected_pair_covers':covers,'U_targets':targets})
