"""All-age PREfirstforeign port cuts by a genuine old-U star/chord.
Only three actual allowed complete-eight predecessors; no age search.
"""
from pathlib import Path
import importlib.util,json,hashlib
from fractions import Fraction as Q
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def after(word,p=(0,0,0)):
 pos,h=p[:2],p[2]
 for c in word:h=(h+(1 if c=='R'else-1))%4;pos=add(pos,l.DIRS[h])
 return*pos,h

def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(a,p):return z(p),z(after(W[a],p))
STAR={(0,0),(0,1),(1,0),(1,1)};old=chord('U',(0,0,0));assert old==((-1,-1),(-1,7))
# Reconstruct the source restriction as literal complete pairs, preserving
# actual coalesced G8/full tails and actual following M11.
pairs=[]
for full in('D','DC','V','VC','VCC','U','UC','UCC'):
 for A in'FQB':
  tr=l.trace(''.join(W[a]for a in full+A)+l.M);pairs.append(dict(actual_full_predecessor=full,foreign=A,feasible=tr['feasible'],conflict=None if tr['feasible']else tr))
assert[(r['actual_full_predecessor'],r['foreign'])for r in pairs if r['feasible']]==[('V','F'),('V','Q'),('U','F'),('U','Q'),('U','B')]
rows=[]
for A,pA,allowed in[('Q',(-1,-3,2),('V','U')),('B',(0,-4,2),('U',))]:
 for previous in allowed:
  delta=after(W[previous],(0,0,2));pp=(pA[0]-delta[0],pA[1]-delta[1],2);assert after(W[previous],pp)==pA
  core={add(pp[:2],l.rot(q,pp[2]))for q in l.K};hit=STAR&core;ch=chord(previous,pp)
  row=dict(foreign=A,foreign_pose=pA,actual_last_complete_eight_packet=previous,predecessor_entry_pose=pp,predecessor_corrected_chord=ch,actual_predecessor_entry_core=sorted(core),SAME_original_U_star_inside_core=sorted(hit))
  assert hit
  expected=STAR if pp==(0,0,2)else {(0,1)}
  assert hit==expected
  row.update(classification='permanent_SAME_old_U_star_in_predecessor_ENTRY_core',all_listed_original_STAR_ids_CURRENT_through_predecessor_entry=True)
  if pp==(-1,1,2):
   assert(A,previous,ch)==('Q','U',((-1,3),(-1,-5)))
   assert ch[0][0]==old[0][0]and -1<ch[0][1]<7
   row.update(additional_independent_geometric_cut='strict_old_U_chord_return_and_overlap_before_foreign',old_source_parameter_at_predecessor_entry='1/2',new_parameter_at_first_repeated_point='0',full_geometric_overlap_y_interval=[-1,3],overlap_old_parameter_interval=['0','1/2'],overlap_new_parameter_interval=['0','1/2'],not_true_adjacency='Old source has entry(0,0,N); this later plainU has entry(-1,1,S), at least two Cs later by heading. Its entry is strict inside the old source chord, not its terminal.')
  rows.append(row)
assert len(rows)==3
paths=[R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',R/'audits/check_U_left_star_permanence_independent.json',R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/manifest.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py'];assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_ALL_AGE_OLD_U_PRE_FIRSTFOREIGN_Q_B_PORT_GUARD_PENDING_REVIEW',scope='A genuine creating U/UC/UCC normalized base0,N inside an uninterrupted U-entry complete-eight factor up to its FIRST complete foreign. At ANY possible age, that foreign cannot have Q(-1,-3,S) or B(0,-4,S). This is PREforeign only, no third-atom or postforeign age premise.',all24_actual_full_eight_foreign_literal_pairs=pairs,all3_allowed_genuine_predecessor_core_chord_guards=rows,conclusion='Q requires plainV(0,0,S), whose entry core contains all four SAME permanent old-U star IDs, or plainU(-1,1,S), whose entry core contains SAME original w=(0,1) (and whose chord independently overlaps the old source). B requires plainU(0,0,S), again with all four star IDs in entry core. Thus both foreign poses are causally impossible at every age before any foreign reset.',application_not_global_claim='This removes the four necessary old-U THIRD n2 residues Q(-1,-3,S) orB(0,-4,S), b1C,b2V,b3V/U(0,3,W), without applying old bud maturity to their postforeign secondV selected input. It is not a complete third-contact catalogue or universal simplicity theorem.',no_prepared_countercontrol_or_unbounded_prefix_scan=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'backward_ports.json').write_text(json.dumps(out,indent=2)+'\n');print('All-age genuine oldU guard: Q(-1,-3,S) andB(0,-4,S) fail all3 actual plainV/U predecessors by SAME star entryCORE or strict oldU chord return.')
