"""Finite literal controls for the separately analytic all-input nesting theorem."""
from pathlib import Path
from random import Random
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];rng=Random(590138)
def cross(a,b):return int((a.conjugate()*b).imag)
def on_segment(p,a,b):return cross(b-a,p-a)==0 and (p.real-a.real)*(p.real-b.real)+(p.imag-a.imag)*(p.imag-b.imag)<=0
def contains(poly,p):
 if any(on_segment(p,a,b)for a,b in zip(poly,poly[1:]+poly[:1])):return True
 wn=0
 for a,b in zip(poly,poly[1:]+poly[:1]):
  if a.imag<=p.imag<b.imag and cross(b-a,p-a)>0:wn+=1
  if b.imag<=p.imag<a.imag and cross(b-a,p-a)<0:wn-=1
 return wn!=0
counts=[];total=0;maxcycles=0
for test in range(180):
 seed={complex(x,y)for x in range(-4,5)for y in range(-4,5)if rng.randrange(8)==0}if test else set()
 board=set(seed);q=0j;h=1j;first={};edge={};read=[]
 for t in range(1800):
  read.append(q)
  if q not in first:first[q]=(t,h)
  right=q not in board
  h*=(-1j if right else 1j);to=q+h
  if first[q][0]==t and q not in seed and to not in seed:edge[q]=to
  board.symmetric_difference_update({q});q=to
 edge={a:b for a,b in edge.items()if b in first};seen=set();cycles=[]
 for start in edge:
  if start in seen:continue
  v=start;walk=[];ix={}
  while v in edge and v not in seen and v not in ix:
   ix[v]=len(walk);walk.append(v);v=edge[v]
  if v in ix:
   cyc=walk[ix[v]:];assert len(cyc)>=4 and len(set(cyc))==len(cyc)
   area=sum(cross(a,b)for a,b in zip(cyc,cyc[1:]+cyc[:1]));assert area<0 and contains(cyc,0j)
   Q=0;left=0
   for i,v in enumerate(cyc):
    u=cyc[i-1];incoming=v-u;outgoing=edge[v]-v;T,I=first[v]
    gap=first[u][0]+1-T;assert gap>=0 and gap%4==0
    if outgoing==1j*incoming:left+=1;assert gap>=4
    else:
     assert outgoing==-1j*incoming
     if v!=0j:assert gap==0
    Q+=gap//4
   assert len(cyc)==4*Q and len(cyc)-2*left==4
   cycles.append(cyc)
  seen.update(walk)
 for i,A in enumerate(cycles):
  for B in cycles[i+1:]:
   assert set(A).isdisjoint(B)
   assert all(contains(A,z)for z in B)or all(contains(B,z)for z in A)
 total+=len(cycles);maxcycles=max(maxcycles,len(cycles));counts.append(len(cycles))
note=ROOT/'periodic_classification_new/one_sided_white_departure_nested_cycles.md'
out=dict(status='PASS independent literal one-sided cycle controls',note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),initial_boards=180,literal_updates=180*1800,finite_cycles_checked=total,maximum_cycles_in_control=maxcycles,scope='The all-input theorem is proved analytically via corrected head exception and finite-interior first-time minimum. Finite controls do not establish the universal theorem or bound nesting.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
