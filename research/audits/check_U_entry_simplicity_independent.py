"""Independent complete contact universe plus hash-bound signed-module assembly."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib,math
P=Path(__file__).resolve();ROOT=P.parents[1];R=ROOT/'core_periodicity_new';B=R/'U_entry_simplicity_frozen_20261023_1616';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
A=json.loads((B/'02_U_entry_center_simplicity.json').read_text());depaudits={'horizon':'check_center_contact','proper_catalogue':'check_atomic_crossing_contexts','proper_VU':'check_VU_crossing_retirement','two':'check_two_C_first_contact','three_nonproper':'check_three_C_center_touch','atomic_left_pose':'check_atomic_three_C_pose_boundary','four':'check_four_C_contact','four_boundary':'check_atomic_predecessor_halfplanes','C_W5':'check_C_first_W_contact','D_W5_gate':'check_D_first_W5_gate','D_W5_helpers':'check_D_W5_helper_history','five_nonproper':'check_five_C_center_touch','five_boundary':'check_five_C_endpoint_boundary','six':'check_six_C_contact','six_successor_geometry':'check_six_C_successor','six_successor_cohort':'check_six_C_successor_cohort','read_cap':'check_simple_center_read_cap'}
depdata={};bindings=[]
for name,row in A['dependency_manifest_hashes'].items():
 dp=R/row['path'];sha=hashlib.sha256(dp.read_bytes()).hexdigest();assert sha==row['sha256'];own=P.with_name(depaudits[name]+'_independent.json');txt=own.read_text();assert sha in txt and json.loads(txt)['status'].startswith('PASS')
 dm=json.loads(dp.read_text())
 for f in dm['files']:assert hashlib.sha256((dp.parent/f['frozen']).read_bytes()).hexdigest()==f['sha256']
 depdata[name]=json.loads(next(dp.parent.glob('02_*json')).read_text());bindings.append(dict(module=name,manifest_sha256=sha,independent_evidence=own.name))
# Reconstruct each atomic corrected-center vector directly from its literal raw word.
g=json.loads((R/'chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];words={a:g[i]['word']for a,i in [('D',0),('V',4),('U',7)]};words['C']=g[1]['word'][len(words['D']):];rot=lambda z,h:z*((-1j)**(h%4));c=-1-1j;dirs=(1j,1,-1j,-1);steps={}
for a,w in words.items():
 p=0j;h=0
 for ch in w:h=(h+(1 if ch=='R'else-1))%4;p+=dirs[h]
 steps[a]=(2*p+rot(c,h)-c)/2
assert steps=={'D':1+1j,'V':1+3j,'U':4j,'C':1+1j}
def det(a,b):return int(a.real*b.imag-a.imag*b.real)
def xy(p):return int(p.real),int(p.imag)
rank={'U':0,'V':1,'D':2,'C':2};universe=set()
for n in range(2,7):
 h=(-n)%4
 for a,u0 in steps.items():
  for b,v0 in steps.items():
   if n==2 and rank[a]<=rank[b]or n==6 and rank[a]>=rank[b]:continue
   u=2*u0;v=2*rot(v0,h);box=[c-rot(c,h)+s*u-t*v for s in(0,1)for t in(0,1)]
   for x in range(math.ceil(min(z.real for z in box)/2),math.floor(max(z.real for z in box)/2)+1):
    for y in range(math.ceil(min(z.imag for z in box)/2),math.floor(max(z.imag for z in box)/2)+1):
     if(x+y+h)%2:continue
     w=2*complex(x,y)+rot(c,h)-c;den=det(u,v)
     if den:s=F(det(w,v),den);t=F(det(w,u),den)
     else:
      if det(w,u):continue
      # All parallel possibilities have equal heading and forward direction.
      assert n==4 and u.real*v.real+u.imag*v.imag>0
      axis=(lambda z:int(z.real))if v.real else(lambda z:int(z.imag))
      t=F(-axis(w),axis(v));s=F(0)
     if 0<=s<1 and 0<t<=1:universe.add((n,a,b,x,y,h,s,t))
assert Counter(x[0]for x in universe)=={2:8,3:45,4:23,5:45,6:8}
# Compare six disjoint previously independently reconstructed geometry catalogues.
def frac(x):return F(*x)if isinstance(x,list)else F(x)
def key(n,a,b,p,s,t):return(n,a,b,*p,frac(s),frac(t))
cat=[]
for r in depdata['two']['all_eight_canonical_two_C_contact_geometries']:cat.append(key(2,r['earlier_atom'],r['later_atom'],r['later_pose'],r['earlier_chord_parameter'],r['later_chord_parameter']))
for r in depdata['proper_catalogue']['crossings']:cat.append(key(3 if r['later_pose'][2]==1 else 5,r['first_atom'],r['later_atom'],r['later_pose'],r['first_parameter'],r['later_parameter']))
for r in depdata['three_nonproper']['all_24_canonical_nonproper_geometries']:cat.append(key(3,r['earlier_atom'],r['later_atom'],r['later_pose'],r['earlier_parameter'],r['later_parameter']))
for r in depdata['four']['all_23_canonical_geometries']:cat.append(key(4,r['earlier_atom'],r['later_atom'],r['later_pose'],r['earlier_parameter'],r['later_parameter']))
for r in depdata['five_nonproper']['all_24_geometries']:cat.append(key(5,r['a'],r['b'],[*r['p'],r['h']],r['s'],r['t']))
for r in depdata['six']['geometries']:cat.append(key(6,r['first_atom'],r['later_atom'],r['later_pose'],r['earlier_parameter'],r['later_parameter']))
assert len(cat)==len(set(cat))==129 and set(cat)==universe
allowed={(3,'D','V',-1,0,1):[0,1],(3,'C','V',-1,0,1):[1],(3,'V','D',-1,0,1):[0,4,5,6],(4,'D','C',-1,-1,0):[0,1],(5,'D','C',0,-1,3):[0,1]}
rows={key(r['entry_C_gap'],r['earlier_atom'],r['later_atom'],r['later_pose'],r['earlier_parameter'],r['later_parameter']):r for r in A['all129_canonical_first_contact_cases']};assert set(rows)==universe
for k,r in rows.items():
 expected=allowed.get(k[:6],[]);assert r['surviving_allowed_first_full_packet_ids']==expected and not set(expected)&{7,8,9}
 if expected:assert r['surviving_source_entry_C_clock']==0
 n,a,b,x,y,h,s,t=k;proper=0<s<1 and 0<t<1
 if n in(2,6):assert not expected
 if proper and a in('V','U'):assert not expected
 if n==5 and proper:assert not expected
 if n==3 and proper and a in('D','C'):assert expected and(x,y,h)==(-1,0,1)and b=='V'
assert sum(bool(r['surviving_allowed_first_full_packet_ids'])for r in rows.values())==5
cap=json.loads(P.with_name('check_simple_center_read_cap_independent.json').read_text());assert cap['raw_read_cap']==104 and cap['terminal_marker_extra']==2
out=dict(status='PASS independent complete129-case U-family-entry center-simplicity assembly',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),geometry_counts=dict(Counter(x[0]for x in universe)),proper_counts=dict(Counter(n for n,a,b,x,y,h,s,t in universe if 0<s<1 and 0<t<1)),signed_dependency_bindings=bindings,boundary_rows=[dict(geometry=list(k),possible_first_packet_ids=v)for k,v in allowed.items()],U_first_packet_ids=[7,8,9],raw_physical_read_cap=104,with_terminal_marker_cap=106,scope='Any actual complete recurrent-eight factor beginning U/UC/UCC has an injective corrected-center path; every cell is read at most104 raw times,106 with its actual final marker. Infinite such factors leave every fixed finite cell set. Not microscopic self-avoidance, beta0, finite C, renewal, standard capture or a global arbitrary-ant statement.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='signed_dependency_bindings'})
