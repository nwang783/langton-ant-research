"""Exact literal role/clock controls for the analytic C-lifetime theorem.

No actual word search, enlarged age table, or reachability cap is run.
The topology is proved explicitly in the companion note.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import hashlib,json
R=Path(__file__).resolve().parent
GP=R/'chronology_dcuv/literal_residual_geometry.json'
TP=R/'atomic_center_turning_frozen_20261023_1400/manifest.json'
SP=R/'U_entry_simplicity_frozen_20261023_1616/manifest.json'
G=json.loads(GP.read_text())['geometry'];IDS=(0,1,4,5,6,7,8,9)
def rot(p,h):
 x,y=p;return ((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
# Atom steps and C shifts are reconstructed from full literal endpoints.
D,V,U=(tuple(G[a]['endpoint'])for a in (0,4,7))
assert (D,V,U)==((1,1,0),(1,3,0),(0,4,0))
c_head=sub(G[1]['endpoint'][:2],G[0]['endpoint'][:2]);assert c_head==(0,1)
C=add(c_head,sub(rot((Q(-1,2),Q(-1,2)),3),(Q(-1,2),Q(-1,2))))
assert C==(1,1)
steps={'D':D[:2],'V':V[:2],'U':U[:2],'C':C}
assert max(abs(x)for v in steps.values()for x in v)==4
assert sum(len(G[a]['outputs'])for a in IDS)==68
assert sum(len(G[a]['inputs'])for a in IDS)==23
for a in IDS:assert(sum(G[a]['endpoint'][:2])+G[a]['endpoint'][2])%2==0
rows=[];counts=Counter();maxN=0;maxrows=[]
for a in IDS:
 for o in G[a]['outputs']:
  for b in IDS:
   for i in G[b]['inputs']:
    for h in range(4):
     counts['raw_alignments']+=1;p=sub(o,rot(i,h))
     if(sum(p)+h)%2:counts['wrong_sector']+=1;continue
     A=(Q(-1,2),Q(-1,2));B=add(p,rot(A,h));delta=sub(B,A)
     assert all(x.denominator==1 for x in delta)
     dx,dy=map(lambda x:abs(int(x)),delta);N=(dx+11)*(dy+11)
     # Every C decreases heading index once. Their entry-clock difference
     # is the full source-included age; only its congruence is recorded here.
     row={'source':a,'source_name':G[a]['name'],'output':o,'source_C_tails':G[a]['name'].count('C'),'target':b,'target_name':G[b]['name'],'input':i,'relative_heading':h,'consumer_head':p,'center_delta':tuple(map(int,delta)),'rectangle_sites':N,'age_upper_bound':8*N+11,'necessary_age_residue_mod4':(-h)%4}
     rows.append(row);counts['sector_compatible_alignments']+=1
     if N>maxN:maxN=N;maxrows=[row]
     elif N==maxN:maxrows.append(row)
assert counts==Counter(raw_alignments=6256,wrong_sector=3128,sector_compatible_alignments=3128)
assert maxN==289 and 8*maxN+11==2323
assert any(r['source']==9 and r['output']==[-2,6]and r['target']==7 and r['input']==[-1,4]and r['relative_heading']==1 and r['consumer_head']==(-6,5)and r['center_delta']==(-6,6)for r in maxrows)
# The integer rounding in the turning argument is exact, not floating point.
for k in range(100):
 assert (4*k+Q(23,2)).numerator//(4*k+Q(23,2)).denominator==4*k+11
# The half-integer rectangle expanded by five has the stated site count.
for dx in range(12):
 for dy in range(12):
  assert len(range(-5,dx+6))*len(range(-5,dy+6))==(dx+11)*(dy+11)
O={'status':'AUTHOR_ANALYTIC_C_LIFETIME_BOUND_WITH_EXACT_ROLE_CONTROLS','scope':'Simple corrected-center actual complete-eight factors; sources and consumers both inside the factor. Untouched entry identities exempt. No U, C or archive-count upper bound.','geometric_bound':'n <= 8*(|dx|+11)*(|dy|+11)+11','global_produced_input_age_upper_bound':2323,'role_counts':dict(counts),'maximum_rectangle_sites':maxN,'maximizers':maxrows,'all_sector_compatible_role_alignments':rows,'dependencies':{str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in (GP,TP,SP,Path(__file__).resolve())}}
(R/'chronology_dcuv/simple_center_C_lifetime_bound.json').write_text(json.dumps(O,indent=2)+'\n')
print(json.dumps({k:v for k,v in O.items()if k not in('all_sector_compatible_role_alignments','maximizers','dependencies')},indent=2))
