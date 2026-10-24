"""Exact full-context geometry for transition-complete C-cut garbage collection.

Unlike input-only294, this tests all literal context cells, including WHITE
requirements, against already-actual producer/current entry centers. No next
candidate's validity is assumed and no trajectory search is performed.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
import json,hashlib
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
GP=ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry'];IDS=(0,1,4,5,6,7,8,9)
DIR=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):
 x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def ori(a,b,c):return(b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def on(a,b,c):return ori(a,b,c)==0 and all(min(a[k],b[k])<=c[k]<=max(a[k],b[k])for k in(0,1))
def touch(a,b,c,d):
 p,q,r,s=ori(a,b,c),ori(a,b,d),ori(c,d,a),ori(c,d,b)
 return p*q<0 and r*s<0 or p==0 and on(a,b,c)or q==0 and on(a,b,d)or r==0 and on(c,d,a)or s==0 and on(c,d,b)
STEPS=sorted({rot(v,h)for v in((1,1),(1,3),(0,4))for h in range(4)})
def sites(d):
 out=[]
 for x in range(min(0,d[0])-4,max(0,d[0])+5):
  for y in range(min(0,d[1])-4,max(0,d[1])+5):
   if(x+y)%2:continue
   vv=[v for v in STEPS if touch((0,0),d,(x,y),add((x,y),v))]
   if vv:out.append(dict(entry=(x,y),vectors=vv))
 return out
# Independently derive ALL complete-context first-read cells and their BEFORE
# entry colors from each raw packet + following actual marker.
contexts={}
for a in IDS:
 p=(0,0);h=0;odd=set();need={};first={}
 for tick,ch in enumerate(G[a]['word']+G[a]['marker']):
  before=(ch=='L')^(p in odd)
  assert p not in need or need[p]==before
  need[p]=before;first.setdefault(p,tick)
  if p in odd:odd.remove(p)
  else:odd.add(p)
  h=(h+(-1 if ch=='L'else 1))%4;p=add(p,DIR[h])
 assert {(x,y):(bool(b),tau)for x,y,b,tau in G[a]['requirements']}=={q:(b,first[q])for q,b in need.items()}
 contexts[a]=need
assert sum(map(len,contexts.values()))==186
assert sum(len(G[a]['outputs'])for a in IDS)==68
C={};rows=[];counts=Counter()
for a in IDS:
 for output in G[a]['outputs']:
  for b in IDS:
   for slot,color in contexts[b].items():
    for h in range(4):
     counts['raw_alignments']+=1;p=sub(output,rot(slot,h))
     if(sum(p)+h)%2:counts['wrong_sector']+=1;continue
     counts['sector_alignments']+=1;r=rot((-1,-1),h);d=(p[0]+(r[0]+1)//2,p[1]+(r[1]+1)//2)
     assert sum(d)%2==0
     if d not in C:C[d]=sites(d)
     M=len(C[d]);g=0 if d==(0,0)else 4*M+11;residue=(-h)%4;bound=0 if d==(0,0)else g-(g-residue)%4
     rows.append(dict(source=a,output=output,candidate=b,context_slot=slot,before_color=color,current_relative_heading=h,current_head=p,center_delta=d,candidate_sites=M,geometric_bound=g,C_residue=residue,rounded_bound=bound,coincident_centers=d==(0,0)))
assert counts==Counter(raw_alignments=50592,wrong_sector=25296,sector_alignments=25296)
assert len(C)==157 and max(map(len,C.values()))==80
assert max(z['geometric_bound']for z in rows)==331 and max(z['rounded_bound']for z in rows)==330
mx=[z for z in rows if z['rounded_bound']==330];assert len(mx)==8
assert all(not z['before_color']and z['center_delta']==(0,14)and z['current_relative_heading']==2 and z['current_head']==(-1,13)and z['candidate_sites']==80 for z in mx)
cc=(F(-1,2),F(-1,2));offsets=[]
for a in IDS:
 for slot in contexts[a]:
  for h in range(4):
   dd=sub(rot(sub(cc,slot),h),cc);offsets.append(dict(packet=a,slot=slot,heading=h,offset=tuple(map(str,dd)),radius=max(map(abs,dd))))
assert max(z['radius']for z in offsets)==8
for z in offsets:z['radius']=int(z['radius'])
# Arithmetic of the finite but growing331-layer frontier.
for j in range(331,1000):
 assert sum(2*a+10 for a in range(j-330,j+1))==331*(2*j-320)
OUT=dict(status='AUTHOR_TRANSITION_COMPLETE_FULL_CONTEXT_GEOMETRY',scope='Exact next-complete-packet contexts on an actual simple U-entry retained prefix; stop at first language exit, not arbitrary later ant dynamics or bounded global state.',complete_context_cell_count=186,output_slot_count=68,counts=dict(counts),distinct_deltas=len(C),max_candidate_sites=80,max_geometric_bound=331,max_heading_rounded_context_C_age=330,entry_context_center_offset_maximum=8,entry_context_expiration='20R+271',maximizers=mx,all_roles=rows,all_candidate_sites=[dict(delta=d,sites=C[d])for d in sorted(C)],all_entry_context_offsets=offsets,dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in(GP,ROOT/'causal_archive_spatial_lifetime_2026-10-23/manifest.json')},checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(HERE/'full_context_horizon_controls.json').write_text(json.dumps(OUT,indent=2)+'\n')
print(json.dumps({k:OUT[k]for k in('status','scope','complete_context_cell_count','counts','distinct_deltas','max_candidate_sites','max_geometric_bound','max_heading_rounded_context_C_age','entry_context_center_offset_maximum','entry_context_expiration')},indent=2))
