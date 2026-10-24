"""Dependency-only all-tail old-U / first-contact-C guard.
Same genuine LEFT, true preforeign funding clock, no postforeign maturation.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,importlib.util
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('ownership',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def after(word,p=(0,0,0)):
 pos,h=p[:2],p[2]
 for c in word:h=(h+(1 if c=='R'else-1))%4;pos=add(pos,l.DIRS[h])
 return*pos,h

def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(atom,p):return z(p),z(after(W[atom],p))
AP=R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json';angles=json.loads(AP.read_text())['all44_exact_source_target_C_window_rows'];angle=next(a for a in angles if a['source_class']=='preFOREIGN_ordinary'and a['source_atom']=='U'and a['contact_atom']=='C');assert angle['allowed_C_counts_before_contact_ENTRY']==[1,2,3,4]
a,b=chord('U',(0,0,0));u=sub(b,a);boxes=[];cases=[];LEFT={(0,0),(0,1)}
for K in angle['allowed_C_counts_before_contact_ENTRY']:
 h=(2-K)%4;c,d=chord('C',(0,0,h));v=sub(d,c);den=det(u,v);assert den
 corners=[tuple(Q(a[k]+s*u[k]-c[k]-t*v[k],2)for k in(0,1))for s in(0,1)for t in(0,1)];bounds=[(min(q[k]for q in corners).__floor__(),max(q[k]for q in corners).__ceil__())for k in(0,1)];boxes.append(dict(total_actual_C_before_contact_ENTRY=K,heading=h,rational_corners=[[[q.numerator,q.denominator]for q in p]for p in corners],integer_bounds=bounds))
 for x in range(bounds[0][0],bounds[0][1]+1):
  for y in range(bounds[1][0],bounds[1][1]+1):
   if(x+y-K)%2:continue
   q=sub(add(c,(2*x,2*y)),a);s,t=Q(det(q,v),den),Q(det(q,u),den)
   if not(0<=s<1 and 0<t<=1):continue
   tr=l.trace(W['C']+l.M);facts=[];cuts=[]
   for cell in sorted(LEFT):
    local=l.rot(sub(cell,(x,y)),-h);first=tr['first'].get(local);fact=dict(SAME_original_LEFT_cell=cell,contact_C_local=local,in_actual_entry_K=local in l.K,first_physical_read=None if first is None else o.describe('C',first[1]));facts.append(fact)
    if local in l.K:cuts.append(dict(**fact,contradiction='SAME original CURRENT identity is outside actual contact entry core'))
    elif first and first[0]=='R':
     assert first[1]<len(W['C']);cuts.append(dict(**fact,contradiction='SAME original BLACK conflicts with own RAW first-R before-WHITE'))
   assert cuts
   cases.append(dict(total_actual_C_before_contact_ENTRY=K,contact_C_pose=(x,y,h),old_outgoing_s=str(s),new_positive_t=str(t),all_SAME_LEFT_facts=facts,actual_contradictions=cuts))
assert len(boxes)==4 and len(cases)==8
assert {(c['total_actual_C_before_contact_ENTRY'],tuple(c['contact_C_pose']))for c in cases}=={(1,(-1,0,1)),(1,(-1,2,1)),(2,(-1,-1,0)),(2,(-1,1,0)),(3,(0,-1,3)),(3,(0,1,3)),(4,(0,0,2)),(4,(0,2,2))}
assert all(c['old_outgoing_s']in('0','1/2')and c['new_positive_t']=='1'for c in cases)
paths=[AP,R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json',R/'U_LEFT_contact_or_persistence_2026-10-24/manifest.json',R/'audits/check_LEFT_contact_or_persistence_independent.json',R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',R/'audits/check_U_left_star_permanence_independent.json',R/'foreign_U_raw_ages34_2026-10-23/manifest.json',R/'audits/check_foreign_U_raw_ages34_independent.json',R/'foreign_U_star_age2_2026-10-23/manifest.json',R/'foreign_U_marker_clocks_2026-10-23/manifest.json',R/'audits/check_foreign_U_age2_and_marker_independent.json',R/'second_ordinary_after_first_foreign_2026-10-24/old_U_second_C_left_pair_guard_manifest.json',R/'audits/check_old_U_second_C_left_guard_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
assert all(p.exists()for p in paths),[str(p)for p in paths if not p.exists()]
out=dict(status='AUTHOR_ARBITRARY_ORDINARY_TAIL_OLD_U_FIRST_CONTACT_C_EXCLUSION_PENDING_REVIEW',scope='Any finite ordinary RAW tail D/C/V/U following FIRST foreign of an actual U-entry complete-eight prefix, with actual markers and no second foreign. If the expanded proxy has a global FIRST positive new contact owned by a preFOREIGN genuine U-base outgoing chord, its contact atom cannot be C. No full-tail simplicity or other-source exclusion claimed.',exact_signed_arbitrary_tail_angle_row=angle,funding_clock='K counts all actual Cs from source-U ENTRY to contact-C ENTRY, excluding contact C. True preFOREIGN age n is a nonnegative subcount n<=K<=4, never K interpreted as preforeign age.',preFOREIGN_guard='Original four-star current by1918. Signed ages0..2,RAW3/4,marker clocks prohibit any firstFOREIGN RAW retirement or marker/core capture at n<=4; before-WHITE or entry-core contact already contradicts that actual state. Thus complete foreign context MISSES all4 originals.',LEFT_entry_guard='Stop at ENTRY of the global first-contact atom. The earlier expanded prefix is simple by first-contact choice. Signed arbitrary-tail contact-or-LEFT persistence bf1018 therefore gives SAME original LEFT CURRENT/outside actual entry K; no postforeign maturation or fixed-atom transfer is used.',all4_exact_contact_parallelograms=boxes,all8_outgoing_owned_contact_C_poses_and_actual_LEFT_contradictions=cases,conclusion='A RAW C at ANY ordinary-tail index cannot make the global FIRST proxy contact with an outgoing old genuine U-base source chord after exactly one first foreign. Every possible old-U/C geometry conflicts with SAME LEFT at entry or an actual own-RAW first-R. This includes THIRD C but is not a third-step or arbitrary-tail simplicity theorem.',no_old_full_source_or_new_postforeign_maturity_reset=True,no_original_RIGHT_or_q_or_shadow_persistence_after_foreign_assumed=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'C_first_contact.json').write_text(json.dumps(out,indent=2)+'\n');print('All-tail oldU/C first-contact: signed K1..4, true preFOREIGN n<=K, original foreign-star MISS then SAME LEFT entry;8 exact C poses all impossible.')
