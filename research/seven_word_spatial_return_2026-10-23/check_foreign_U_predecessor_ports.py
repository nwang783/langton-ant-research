"""Eight immediate-predecessor obligations for two U-normalized atomic cuts.
No path enumeration or assumption of a post-foreign simple center path.
"""
from pathlib import Path
from fractions import Fraction as Q
import hashlib,json
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
G=json.loads((R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry']
V=((0,1),(1,0),(0,-1),(-1,0));K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};L={(0,0),(0,1),(1,0),(1,1)}
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def endpoint(w):
 p=(0,0);h=0
 for ch in w:
  h=(h+(-1 if ch=='L'else 1))%4;p=add(p,V[h])
 return p,h
W={'D':G[0]['word'],'C':G[1]['word'][len(G[0]['word']):],'V':G[4]['word'],'U':G[7]['word']}
def center(p,h):return add((2*p[0],2*p[1]),rot((-1,-1),h))
rows=[]
for target in((1,3),(2,4)):
 for a,w in W.items():
  ep,dh=endpoint(w);h=(-dh)%4;p=sub(target,rot(ep,h));c=center(p,h)
  core={add(p,rot(q,h))for q in K};held=sorted(core&L)
  ga={'D':0,'V':4,'U':7}.get(a);white={add(p,rot(q[:2],h))for q in G[ga]['requirements']if not q[2]} if ga is not None else set();white_hits=sorted(white&L)
  repeat= c[0]==-1 and -1<=c[1]<=7
  reason='repeats_old_U_chord' if repeat else 'old_star_in_entry_core' if held else 'old_star_before_white' if white_hits else 'predecessor_cut_already_excluded' if target==(2,4)and a=='D' else 'only_unexcluded_role'
  rows.append(dict(target_pose=(*target,0),predecessor_atom=a,predecessor_pose=(*p,h),predecessor_center=c,old_star_entry_core_hits=held,old_star_before_white_hits=white_hits,reason=reason))
assert [r['reason'] for r in rows[:4]]==['repeats_old_U_chord','repeats_old_U_chord','repeats_old_U_chord','old_star_before_white']
assert [r['reason'] for r in rows[4:]]==['predecessor_cut_already_excluded','only_unexcluded_role','old_star_in_entry_core','old_star_in_entry_core']
assert rows[5]['predecessor_pose']==(1,4,1)
D=[R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json',R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/manifest.json',R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',H/'foreign_first_contact_manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_AUDIT',scope='Immediate predecessors inside the retained-eight interval following a genuine U creator; no post-foreign simplicity or permanence. Atomic C may be internal, while D/V/U base entries are actual full boundaries.',rows=rows,excluded_cut=(1,3,0),forced_C_predecessor_cut=(2,4,0),forced_predecessor=(1,4,1),dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'foreign_U_predecessor_ports.json').write_text(json.dumps(o,indent=2)+'\n')
print('Eight literal predecessor roles; cut (1,3,N) excluded, cut (2,4,N) requires immediate C.')
