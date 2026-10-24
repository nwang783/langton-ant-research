"""Portable old-U arm W-run contact-or-persistence, THIRD W application.
Exact roles/current physical identity only, no age theorem after foreign.
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
from itertools import product
from collections import Counter
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry'];IDS=(0,1,4,5,6,7,8,9);compact={a:i for i,a in enumerate(IDS)};CP=R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';COUNT={tuple(map(int,line.split()[:8]))for line in CP.read_text().splitlines()};arm=(1,2)
source_roles=[];young=[]
for src in(7,8,9):
 tr=l.trace(G[src]['word']);assert tr['last'][arm]==('R',17)and list(arm)in G[src]['outputs']
 source_roles.append(dict(actual_creating_full=G[src]['name'],genuine_original_arm_cell=arm,R_birth_tick0=17,R_birth_read_number1=18,source_full_ENTRY_clock=0,actual_full_completion_clock=G[src]['name'].count('C'),own_C_tails_preserve_same_arm=True))
 for n in range(4):
  h=(-n)%4
  for con in IDS:
   for i,q in enumerate(G[con]['inputs']):
    p=sub(arm,l.rot(tuple(q),h));key=(compact[src],compact[con],*p,h,*arm,n);why='sector'if(sum(p)+h)%2 else'signed_COUNT5'if key in COUNT else'UNEXCLUDED';assert why!='UNEXCLUDED'
    young.append(dict(actual_full_source=G[src]['name'],consumer=G[con]['name'],input_slot0=i,consumer_pose=(*p,h),true_full_source_ENTRY_C_age=n,key=key,reason=why))
assert len(young)==276 and Counter(r['reason']for r in young)=={'sector':138,'signed_COUNT5':138}
# First current loss through an actual plain W D/V/U. C is not a zero-C
# atom; standalone actual C preserves every old current residual literally.
a,b=chord('U',(0,0,0));Wports=[];Nports=[]
for con in(0,4,7):
 for i,q in enumerate(G[con]['inputs']):
  p=sub(arm,l.rot(tuple(q),3));end=after(W[G[con]['name']],(*p,3));row=dict(consumer=G[con]['name'],input_slot0=i,input_cell=q,consumer_pose=(*p,3),actual_RAW_exit=end,actual_first_input_read=o.describe(G[con]['name'],l.trace(W[G[con]['name']]+l.M)['first'][tuple(q)][1]))
  if(sum(p)+3)%2:row['classification']='wrong_active_sector'
  else:
   assert con==7 and p in((2,3),(3,2));ch=chord('U',(*p,3));assert ch[0][1]==ch[1][1];yy=ch[0][1];s=Q(yy-a[1],b[1]-a[1]);t=Q(a[0]-ch[0][0],ch[1][0]-ch[0][0]);assert 0<s<1 and 0<t<=1
   row.update(classification='loss_atom_contacts_genuine_old_U_chord',actual_RAW_chord=ch,old_source_s=str(s),new_t=str(t),contact_point=(-1,yy))
  Wports.append(row)
  pN=sub(arm,tuple(q));endN=after(W[G[con]['name']],(*pN,0));assert endN[0]>=1 and endN[:2]!=(0,2)
  Nports.append(dict(consumer=G[con]['name'],input_slot0=i,input_cell=q,consumer_pose=(*pN,0),actual_RAW_exit=endN,actual_first_input_read=o.describe(G[con]['name'],l.trace(W[G[con]['name']]+l.M)['first'][tuple(q)][1]),required_pre_C_EXIT=(0,2,0),exact_mismatch=True))
assert len(Wports)==8 and sum(r['classification']=='wrong_active_sector'for r in Wports)==6 and len(Nports)==8
Cgeo=l.literal_geometry(W['C']);assert Cgeo['inputs']==[]
# Third targetV/U0,3W lies outside oldU before contact, but entryK
# contains arm. All true preA ages arise from n+#C(b1,b2)=3.
rows=[]
for b3 in'VU':
 target=(0,3,3);K={add(target[:2],l.rot(q,3))for q in l.K};assert arm in K
 for b1,b2 in product('DCVU',repeat=2):
  n=3-int(b1=='C')-int(b2=='C');assert n in(1,2,3)
  for A in'FQB':
   hA=(-n)%4;de=after(W[A]+W[b1]+W[b2],(0,0,hA));pa=(-de[0],3-de[1],hA);tr=l.trace(W[A]+l.M);loc=l.rot(sub(arm,pa[:2]),-hA);first=tr['first'].get(loc);row=dict(foreign=A,first=b1,second=b2,third=b3,third_pose=target,true_preFOREIGN_age=n,total_C_before_third_ENTRY=3,foreign_pose=pa,original_arm_foreign_local=loc,actual_FOREIGN_complete_first_arm_read=first)
   if first:
    assert first[0]=='R'and loc not in l.K;row.update(classification='initial_SAME_arm_BLACK_conflicts_with_FOREIGN_context_first_R',actual_first_read_owner=o.describe(A,first[1]),physical_read_not_claimed_FOREIGN_owned_RAW=True,actual_b1_physical_read=o.describe(b1,first[1]-len(W[A])))
   else:
    row['FOREIGN_complete_context_MISSES_original_arm']=True
    if n==3:row.update(classification='both_prior_atoms_W_zero_C_contact_or_arm_persistence',before_target_arm_CURRENT=True)
    elif n==1:
     assert b1==b2=='C';row.update(classification='both_actual_C_atoms_preserve_old_CURRENT_arm',before_target_arm_CURRENT=True)
    elif b1=='C':row.update(classification='actual_C_preserves_then_W_zero_C_contact_or_arm_persistence',before_target_arm_CURRENT=True)
    else:
     assert b2=='C';endA=after(W[A],pa);end1=after(W[b1],endA);assert end1==(0,2,0)
     row.update(classification='only_N_base_has_wrong_arm_loss_EXIT_then_C_preserves',actual_b1_EXIT=end1,all8_possible_N_input_exit_mismatches=Nports,before_target_arm_CURRENT=True)
    row['final_contradiction']='SAME original arm remains CURRENT outside active core, but arm lies in actual THIRD entryK.'
   rows.append(row)
assert len(rows)==96
assert sum(r['classification']=='initial_SAME_arm_BLACK_conflicts_with_FOREIGN_context_first_R'for r in rows)==12
assert sum(r.get('FOREIGN_complete_context_MISSES_original_arm',False)for r in rows)==84
paths=[GP,CP,R/'audits/dcuv_count5_replay/queries.json',R/'core_periodicity_new/atomic_exit_bud_frozen_20261023_1325/manifest.json',R/'audits/check_atomic_exit_bud_independent.json',R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json',R/'first_foreign_two_ordinary_simplicity_2026-10-24/manifest.json',R/'audits/two_RAW_simplicity_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py'];assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_OLD_U_ARM_W_CONTACT_OR_PERSISTENCE_AND_THIRD_W_GUARD_PENDING_REVIEW',portable_lemma_scope='A SAME genuine original U-base arm t=(1,2) is CURRENT at the start of any actual finite zero-C W-heading D/V/U RAW run. Its first CURRENT loss in that run forces a contact with the genuine old creating-U chord by completion of that loss atom. No foreign or age premise is required for this finite-role lemma, and no persistence through a contact atom is claimed.',all8_plain_W_first_loss_input_roles=Wports,no_other_star_column_or_LEFT_persistence_assumed_in_W_lemma=True,preFOREIGN_current_guard=dict(all3_actual_source_roles=source_roles,all276_exact_age0_through3_input_queries=young,query_counts=dict(Counter(r['reason']for r in young)),conclusion='At a stipulated completed old8 to FIRSTforeign boundary of true source-entry age<=3, SAME arm is CURRENT. Creator full must actually complete; own C tails literally preserve arm before full completion.'),actual_C_zero_old_input_geometry=Cgeo,all8_N_plain_arm_input_RAW_exit_obligations=Nports,third_application_scope='Only global FIRST contact by THIRD ordinary target V/U(0,3,W) owned by genuine preFOREIGN oldU0N, totalC beforethird3, true preA n1/2/3. No old-U other pose or full third simplicity.',all96_exact_inverse_FOREIGN_two_prior_RAW_interfaces=rows,conclusion='All96 interfaces fail. Twelve first-R completeFOREIGN marker requirements conflict with the original BLACK arm. The other84 complete foreign contexts MISS it; actual C atoms preserve it, W zeroC atoms cannot first lose it before an earlier oldU contact, and the sole possible N atom before a C has an impossible required EXIT0,2N versus every arm-input exitx>=1. SAME arm is therefore CURRENT at THIRD entry, but is inside its actual entryK. No postforeign age used.',no_foreign_read_misownership_or_current_CORE_physical_death_identification=True,no_generic_prefix_scan_or_postFOREIGN_maturation=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'arm_W_guard.json').write_text(json.dumps(out,indent=2)+'\n');print('PortableW arm loss:8 roles=6sector+2oldU contacts;276 genuine young-arm queries;96 thirdW inverse cases=12 firstR contradictions+84 SAME-arm persistence/core contradictions.')
