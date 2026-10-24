"""Exact consumer-cover law at the U-family's middle white cell.

All 92 finite input alignments are exhausted, with no C-age threshold,
word-length cutoff, center-simplicity premise, or guessed spatial box.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import hashlib,json
ROOT=Path(__file__).resolve().parent
GP=ROOT/'chronology_dcuv/literal_residual_geometry.json'
IP=ROOT/'chronology_dcuv/u_middle_input_origin_order.json'
MP=ROOT/'u_middle_origin_frozen_20261023_1013/manifest.json'
D=json.loads(GP.read_text());G=D['geometry'];K=set(map(tuple,D['core']))
IDS=(0,1,4,5,6,7,8,9)
INPUTS=((-1,1),(-1,2),(-1,4),(0,2),(0,3))
NAMES={(-1,1):'a',(-1,2):'q',(-1,4):'b',(0,2):'c',(0,3):'d'}
Z=(-1,3)
STEPS=((0,1),(1,0),(0,-1),(-1,0))
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def rot(p,h):
 x,y=p;return ((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def context(a):return {tuple(z[:2])for z in G[a]['requirements']}
# Independently regenerate every literal before-context, input/output set,
# endpoint and common U white requirement from raw plus its actual marker.
literal=[]
for a in IDS:
 raw=G[a]['word'];marker=G[a]['marker'];seen={};colors={};p=(0,0);h=0;raw_parity=set()
 raw_end=None
 for tick,t in enumerate(raw+marker):
  want=t=='L'
  if p not in colors:seen[p]=want;colors[p]=want
  assert colors[p]==want
  colors[p]=not want
  if tick<len(raw):raw_parity.symmetric_difference_update({p})
  h=(h+(-1 if want else 1))%4;p=add(p,STEPS[h])
  if tick+1==len(raw):raw_end=(*p,h)
 assert raw_end==tuple(G[a]['endpoint'])
 assert seen=={tuple(z[:2]):z[2]for z in G[a]['requirements']}
 assert {q for q,c in seen.items()if c}-K==set(map(tuple,G[a]['inputs']))
 black={q for q,c in seen.items()if c};black.symmetric_difference_update(raw_parity)
 exitK={add(raw_end[:2],rot(q,raw_end[2]))for q in K}
 assert exitK<=black and black-exitK==set(map(tuple,G[a]['outputs']))
 assert(sum(raw_end[:2])+raw_end[2])%2==0
 literal.append({'packet':a,'name':G[a]['name'],'context_cells':len(seen),'inputs':G[a]['inputs'],'outputs':G[a]['outputs'],'endpoint':raw_end})
for t in (7,8,9):
 assert set(map(tuple,G[t]['inputs']))==set(INPUTS)
 assert dict((tuple(z[:2]),z[2])for z in G[t]['requirements'])[Z] is False

alignments=[];counts=Counter()
for a in IDS:
 for inp in G[a]['inputs']:
  for h in range(4):
   p=sub(Z,rot(inp,h));sector=(sum(p)+h)%2
   hits=set(INPUTS)&{add(p,rot(z,h))for z in context(a)}
   counts['raw']+=1
   if sector:counts['wrong_sector']+=1
   else:counts['correct_sector']+=1;assert hits
   alignments.append({'packet':a,'name':G[a]['name'],'input':inp,'head':(*p,h),'wrong_sector':bool(sector),'protected_context_hits':sorted(hits)})
assert counts==Counter(raw=92,wrong_sector=46,correct_sector=46)
sector_hits=[set(map(tuple,r['protected_context_hits']))for r in alignments if not r['wrong_sector']]
minimal=[];subsets=[]
for n in range(6):
 for ps in combinations(INPUTS,n):
  P=set(ps);witness=next((j for j,H in enumerate(sector_hits)if not H&P),None)
  cover=witness is None
  subsets.append({'protected_inputs':ps,'covers_every_sector_compatible_consumer':cover,'avoiding_consumer_index_in_sector_rows':witness})
  if cover and not any(set(Q)<=P for Q in minimal):minimal.append(ps)
expected=[((-1,1),(-1,4)),((-1,1),(0,3)),((-1,2),(-1,4)),((-1,2),(0,3))]
assert minimal==expected
for pair in expected:
 assert all(set(pair)&H for H in sector_hits)

# Reconstruct the complete 24-row FOUR-cohort inventory from output/input
# point alignments, then compare with the already signed inventory.
templates={}
for a in IDS:
 O=set(map(tuple,G[a]['outputs']))
 for h in range(4):
  for o in O:
   for inp in INPUTS:
    p=sub(o,rot(inp,h))
    if(sum(p)+h)%2:continue
    P=O&{add(p,rot(i,h))for i in INPUTS}
    assert len(P)<5
    if len(P)!=4:continue
    key=(a,*p,h)
    localP={rot(sub(q,p),-h)for q in P};shadow=add(p,rot(Z,h))
    covers=[pair for pair in expected if set(pair)<=localP]
    blocked=shadow in O and bool(covers)
    templates[key]={'source_packet':a,'source_name':G[a]['name'],'consumer_pose':(*p,h),'matched_source_outputs':sorted(P),'target_offsets':sorted(localP),'shadow_in_source_outputs':shadow in O,'shadow_cell':shadow,'blocking_pairs':covers if shadow in O else [],'new_retirement_exclusion':blocked}
assert len(templates)==24
old=json.loads(IP.read_text())['four_cohort_templates']
assert set(templates)=={(t['source_packet'],*t['consumer_pose'])for t in old}
rows=[]
for j,t in enumerate(old):
 r=templates[(t['source_packet'],*t['consumer_pose'])].copy()
 assert set(r['matched_source_outputs'])==set(map(tuple,t['matched_source_outputs']))
 r['signed_inventory_row']=j;r['previous_outcome']=t['outcome'];rows.append(r)
blocked=[r for r in rows if r['new_retirement_exclusion']]
assert len(blocked)==12
assert all(r['previous_outcome']=='not_excluded_by_this_static_test'for r in blocked)
assert Counter((r['source_name'],tuple(r['consumer_pose']))for r in blocked)==Counter((name,pose)for name in ('U','UC','UCC')for pose in ((2,-2,0),(-1,0,1),(0,4,2),(4,1,3)))
summary={'raw_alignments':92,'wrong_sector':46,'correct_sector_cover_checks':46,'minimal_blocking_pairs':4,'all_input_subsets_checked':32,'four_cohort_templates':24,'new_all_age_four_cohort_exclusions':12,'old_all_age_exclusions':7,'old_strictly_older_fifth_rows':2,'remaining_static_survivors':3}
result={'status':'AUTHOR_EXACT_CONSUMER_SHADOW_RETIREMENT_COVER','scope':'Complete recurrent-eight factors, any board, age or center path. Ordered residual identities, not literal black-lifetime tokens. No U count, component merger, record closure or capture theorem.','target':{'white_shadow':Z,'inputs':INPUTS,'labels':{str(k):v for k,v in NAMES.items()}},'literal_reconstruction':literal,'summary':summary,'minimal_blocking_pairs':expected,'all_consumer_alignments':alignments,'all_subset_cover_checks':subsets,'four_cohort_templates':rows,'dependencies':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in (GP,IP,MP,Path(__file__).resolve())}}
(ROOT/'chronology_dcuv/U_white_shadow_retirement.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(summary,indent=2))
