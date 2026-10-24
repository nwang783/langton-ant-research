"""THIRD ordinary E-facing old-U contact: exact zero/one-C endpoints.
No generic prefix scan or postforeign maturation.
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
from itertools import product,permutations
from collections import Counter
AP=R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json';angle_rows=json.loads(AP.read_text())['all44_exact_source_target_C_window_rows'];angle_proof=[]
for target in'DCVU':
 a=next(a for a in angle_rows if a['source_class']=='preFOREIGN_ordinary'and a['source_atom']=='U'and a['contact_atom']==target);allowed=[K for K in a['allowed_C_counts_before_contact_ENTRY']if(2-K)%4==1];assert allowed==[1];angle_proof.append(dict(signed_row=a,E_heading_forces_total_C_before_third_ENTRY=allowed))
a,b=chord('U',(0,0,0));u=sub(b,a);LEFT={(0,0),(0,1)};geom=[];keeps=[]
for target in'DCVU':
 c,d=chord(target,(0,0,1));v=sub(d,c);den=det(u,v);assert den
 corners=[tuple(Q(a[k]+s*u[k]-c[k]-t*v[k],2)for k in(0,1))for s in(0,1)for t in(0,1)];bounds=[(min(q[k]for q in corners).__floor__(),max(q[k]for q in corners).__ceil__())for k in(0,1)];tr=l.trace(W[target]+l.M)
 for x in range(bounds[0][0],bounds[0][1]+1):
  for y in range(bounds[1][0],bounds[1][1]+1):
   if(x+y-1)%2:continue
   q=sub(add(c,(2*x,2*y)),a);s,t=Q(det(q,v),den),Q(det(q,u),den)
   if not(0<=s<1 and 0<t<=1):continue
   cuts=[]
   for cell in sorted(LEFT):
    loc=l.rot(sub(cell,(x,y)),-1);first=tr['first'].get(loc)
    if loc in l.K or first and first[0]=='R':cuts.append(dict(SAME_LEFT=cell,third_local=loc,actual_entry_core=loc in l.K,actual_first_read=None if first is None else o.describe(target,first[1])))
   row=dict(third=target,third_pose=(x,y,1),old_s=str(s),third_t=str(t),SAME_LEFT_contradictions=cuts);geom.append(row)
   if not cuts:keeps.append(row)
assert len(geom)==18 and len(keeps)==4
assert {(r['third'],r['third_pose'])for r in keeps}=={('D',(-1,0,1)),('V',(-3,0,1)),('U',(-4,-1,1)),('U',(-2,-1,1))}
def raw(tokens):return ''.join(W[a]for a in tokens)
def actual_owner(tokens,tick):
 t=0
 for i,a in enumerate(tokens):
  if tick<t+len(W[a]):return dict(actual_atom_index0=i,actual_atom=a,canonical=o.describe(a,tick-t))
  t+=len(W[a])
 return dict(actual_atom='next actual word',tick0=tick-t,read_number1=tick-t+1,turn=l.M[tick-t])
# Actual grammar prerequisites for the one-C W phase.
cu=l.trace(W['C']+W['U']+l.M);assert not cu['feasible']
CP=R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json'
source_role_clocks=[]
for n in(0,1):
 for full in('U','UC','UCC'):
  c=full.count('C');source_role_clocks.append(dict(true_preFOREIGN_age=n,actual_creating_full=full,source_full_entry_clock=0,actual_full_completion_clock=c,chronologically_possible=c<=n,creator_plain_U_oneC_requires_new_N_base_before_C=(n==1 and full=='U')))
rows0=[];rows1=[];words0=[];words1=[]
for r in keeps:
 b3=r['third'];p3=r['third_pose']
 for b1,b2 in product('DCVU',repeat=2):
  post=int(b1=='C')+int(b2=='C');n=1-post
  if n not in(0,1):continue
  for A in'FQB':
   hA=(-n)%4;delta=after(raw(A+b1+b2),(0,0,hA));pa=(p3[0]-delta[0],p3[1]-delta[1],hA);base=dict(first=b1,second=b2,third=b3,third_pose=p3,foreign=A,foreign_pose=pa,true_preFOREIGN_age=n,total_C_before_third=1)
   if n==0:
    models=[];x,y=pa[:2]
    if x>=0 and y>=4:
     for v in range(x+1):
      d=x-v;rest=y-4-d-3*v
      if rest<0 or rest%4:continue
      uc=rest//4
      seqs=[]
      for seq in sorted(set(permutations('D'*d+'V'*v+'U'*uc))):
       if seq and not(seq[-1]=='U'or(seq[-1]=='V'and A!='B')):continue
       T='U'+''.join(seq)+A+b1+b2+b3;tr=l.trace(raw(T)+l.M);assert not tr['feasible']
       rec=dict(**base,creator_actual_full='U',exact_N_zero_run=''.join(seq),counts=dict(D=d,V=v,U=uc),whole_actual_word=T,conflict=tr,conflict_owner=actual_owner(T,tr['conflict_read']),previous_owner=actual_owner(T,tr['previous_read']));words0.append(rec);seqs.append(T)
      models.append(dict(D=d,V=v,U=uc,all_actual_last_V_U_ordered_words=seqs))
    rows0.append(dict(**base,all_exact_N_count_models=models,endpoint_equations='xA=d+v; yA=4+d+3v+4u; actual last old baseV/U required; empty run keeps creatingU as actual predecessor'))
   else:
    # Exact source types: UCC cannot complete; plainU has yA>=7.
    # UC starts its W run at(0,5,W). C->FOREIGN forbidden; C->U
    # impossible. Thus first W baseD/V contributes y1; all others
    # must U if yA==6. Endpoint x then fixes every possible U count.
    assert pa[1]<=6
    models=[]
    if pa[1]==6 and A in'FQ'and b1 in'DV'and b2 in'DV':
     assert b3 in'DV'
     for first,x0 in(('D',-1),('V',-3)):
      diff=x0-pa[0]
      if diff<0 or diff%4:continue
      uc=diff//4
      if first=='D'and uc==0:continue
      T='UC'+first+'U'*uc+A+b1+b2+b3;tr=l.trace(raw(T)+l.M);assert not tr['feasible'];models.append(dict(actual_first_W_base=first,W_U_count=uc,whole_actual_word=T))
      words1.append(dict(**base,creator_actual_full='UC',actual_first_W_base=first,W_U_count=uc,whole_actual_word=T,conflict=tr,conflict_owner=actual_owner(T,tr['conflict_read']),previous_owner=actual_owner(T,tr['previous_read'])))
    rows1.append(dict(**base,plain_creator_U='minimum yA7 by nonempty N ownerbase beforeC plus nonempty W firstD/V afterC, excluded',creator_UCC='fullcompletion2>FOREIGN1',creator_UC_exact_height_x_models=models))
assert len(rows0)==72 and len(rows1)==108 and len(words0)==13 and len(words1)==16
assert all(not r['conflict']['feasible']for r in words0+words1)
paths=[AP,R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json',R/'U_LEFT_contact_or_persistence_2026-10-24/manifest.json',R/'audits/check_LEFT_contact_or_persistence_independent.json',R/'foreign_U_raw_ages34_2026-10-23/manifest.json',R/'audits/check_foreign_U_raw_ages34_independent.json',R/'foreign_U_star_age2_2026-10-23/manifest.json',R/'foreign_U_marker_clocks_2026-10-23/manifest.json',R/'audits/check_foreign_U_age2_and_marker_independent.json',CP,R/'third_ordinary_local_interface_2026-10-24/manifest.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py'];assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_OLD_U_THIRD_E_ENDPOINT_GUARD_PENDING_INDEPENDENT_AUDIT',scope='Global FIRST contact by THIRD ordinary RAW, target heading E relative to an outgoing old creating U-base chord, after U-entry complete8 and its FIRST foreign. No other heading/old source or full third simplicity. Actual M11 retained.',all4_signed_angle_rows_and_forced_K1=angle_proof,all18_exact_E_contact_geometries=geom,exact4_SAME_LEFT_compatible_geometries=keeps,SAME_LEFT_premise='K1 implies true preA n<=1; young-star bounds force entire A STAR-MISS. Earlier proxy is simple by global-first-contact choice, so bf1018 gives SAME LEFT current at third entry. No old8 maturity after A.',all6_actual_creator_full_completion_cases=source_role_clocks,all72_zero_preFOREIGN_C_endpoint_cases=rows0,all13_zero_C_endpoint_exhaustive_whole_words_fail=words0,all108_one_preFOREIGN_C_endpoint_cases=rows1,all16_one_C_endpoint_exhaustive_whole_words_fail=words1,one_C_unbounded_run_proof='N/W y increments D1,V3,U4 and W D/V1,U0. Source plainU must install firstC through later N fullbase, adding>=1; a nonempty W run begins D/V because C->U is literal-impossible and C-ending complete8->A impossible. Thus yA>=7. Actual creatorUC exits to W(0,5); yA<=6 forces exactly one initial W D/V then only U atoms. The exact x fixes every U count, no depth cap.',raw_C_U_immutable_conflict=cu,conclusion='All old-U-source THIRD E-heading first contacts are excluded. The only endpoint-realizable histories in the required K1 window are13 zero-C words or16 one-C words; all have immutable physical literal conflicts. No genuine positive contact was found or assumed.',no_unbounded_rail_length_truncation_or_postFOREIGN_age_law=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'third_E_endpoints.json').write_text(json.dumps(out,indent=2)+'\n');print('OldU THIRD E:18 geometries->4 SAME LEFT poses;K1 forces n0/1;72+108 endpoint cases yield13+16 exact wholewords, all literal failures.')
