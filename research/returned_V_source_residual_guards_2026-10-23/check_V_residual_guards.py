"""Remaining18 old-V returned-first-contact labels: actual ancestry guards.
Six source-deleted(1,1), ten source exit-bud endpoints, two forced A-cleanup
fresh-cohort guards. No postforeign age law or returned simplicity.
"""
from pathlib import Path
from collections import Counter
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';QP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json';CP=R/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact.json';PP=R/'returned_V_source_reduction_2026-10-23/returned_V_source_reduction.json'
G=json.loads(GP.read_text())['geometry'];W=json.loads(QP.read_text())['macro_words'];C=json.loads(CP.read_text());P=json.loads(PP.read_text());M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};VEL=((0,1),(1,0),(0,-1),(-1,0));held={(0,0),(1,0)};deleted=(1,1);exitbud=(2,2)
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def at(q,p,h):return add(p,rot(q,h))
def derive(w,stop=False):
 p=(0,0);h=0;par=set();rq={};rd={};first={}
 for t,ch in enumerate(w):
  b=(ch=='L')^(p in par)
  if p in rq and rq[p]!=b:
   if stop:return dict(conflict_tick=t,cell=p,first=first[p],required_initial=b,original_initial=rq[p])
   raise AssertionError((t,p))
  if p not in rq:rq[p]=b;first[p]=[t,ch]
  rd.setdefault(p,[]).append([t,ch]);par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEL[h])
 return rq,par,p,h,rd
Vbase=set(map(tuple,G[4]['outputs']));vr,vpar,_,_,vrd=derive(W[2]['word']);assert vrd[deleted]==[[6,'R'],[10,'L']]
for gi in(4,5,6):
 rq,par,ep,dh,rd=derive(G[gi]['word']);assert rd[deleted]==vrd[deleted]and deleted not in set(map(tuple,G[gi]['outputs']))and deleted not in{at(z,ep,dh)for z in K};assert rd[exitbud][-1]==[16,'R']
# Actual sourceV exit is(1,3,N). N0 heads y>=3, W1 heads H>=3.
assert deleted[1]<3 and deleted[1]-deleted[0]<3
AT=[]
for i in range(4):
 rq,par,ep,dh,rd=derive(W[i]['word']);ctx,_,_,_,_=derive(W[i]['word']+M);outs={z for z in rq if rq[z]^(z in par)}-{at(z,ep,dh)for z in K};assert all(z[1]>=0 and sum(z)>=0 for z in outs);AT.append(dict(name='DCVU'[i],outputs=outs,endpoint=ep,turn=dh,context=ctx))
rebirth=[];origins=[]
for h in(2,1):
 for a in AT:
  for slot in sorted(a['outputs']):
   p=sub(deleted,rot(slot,h));ep=at(a['endpoint'],p,h);hits=sorted(held&{at(z,p,h)for z in a['context']})
   if(sum(p)+h)%2:why='wrong_active_sector'
   elif hits:why='current_original_r_or_B_in_complete_context'
   elif h==1 and a['name']=='C':why='E_C4_completes_after_foreign_clock3'
   else:
    assert h==1 and(a['name'],slot,p,ep)in(('V',(2,1),(0,3),(3,2)),('U',(2,1),(0,3),(4,3)));why='plain_E3_origin';origins.append((a['name'],slot,p,ep))
   rebirth.append(dict(heading=h,atom=a['name'],output_slot=slot,pose=[*p,h],endpoint=ep,current_r_B_hits=hits,reason=why))
assert len(rebirth)==38 and len(origins)==2
for x in rebirth:
 if x['heading']==2:assert x['reason']in('wrong_active_sector','current_original_r_or_B_in_complete_context')
# Exact arbitrary E-run equations, with the actual last-fullpacket ownership.
def endpoint_obligation(ep,target,foreign):
 dx=target[0]-ep[0];down=ep[1]-target[1];sol=[];allowed=('V','U')if foreign in('F','Q')else('U',)
 for v in range(max(down+1,0)):
  d=down-v;rem=dx-d-3*v
  if rem<0 or rem%4:continue
  u=rem//4;last=[a for a,c in(('D',d),('V',v),('U',u))if c and a in allowed];sol.append(dict(d=d,v=v,u=u,allowed_last=last))
 assert ep!=target and all(not z['allowed_last']for z in sol)
 return sol
sixes={167,168,169,211,212,213};tens={173,174,175,214,215,216,217,218,219,220};twos={221,222};assert sixes|tens|twos==set(P['residual_catalogue_cases'])
rows=[];del_end=[];bud_end=[];helpers=[]
for ix in P['residual_catalogue_cases']:
 row=C['old_source_contact_cases'][ix];assert row['source_atom']=='V'and row['source_to_foreign_C_age']==3;j='DCVUFQB'.index(row['foreign']);i='DCVU'.index(row['returned_atom']);ap=tuple(row['foreign_pose'][:2]);ah=row['foreign_pose'][2];assert ah==1
 ar,_,_,_,ard=derive(W[j]['word']+M);br,_,_,_,brd=derive(W[j]['word']+W[i]['word']+M)
 if ix in sixes:
  local=rot(sub(deleted,ap),-ah);assert br[local]is True and local not in K;assert ar[local]is True
  why='source_deleted_11_has_no_possible_preforeign_rebirth';guard=deleted;read=brd[local][0]
  for name,slot,p,ep in origins:
   sol=endpoint_obligation(ep,ap,row['foreign']);del_end.append(dict(case=ix,origin=name,output_slot=slot,origin_entry=[*p,1],endpoint=ep,foreign=row['foreign'],foreign_entry=ap,all_zero_C_E_continuation_counts=sol))
 elif ix in tens:
  local=rot(sub(exitbud,ap),-ah);assert br[local]is False and local not in K;why='genuine_V_exit_bud_first_clearer_at3_cannot_reach_foreign';guard=exitbud;read=brd[local][0]
  for gi in(0,4,7):
   for slot in map(tuple,G[gi]['inputs']):
    p=sub(exitbud,rot(slot,1));ep=at(tuple(G[gi]['endpoint'][:2]),p,1);sol=endpoint_obligation(ep,ap,row['foreign']);bud_end.append(dict(case=ix,clearer=G[gi]['name'],input_slot=slot,clearer_entry=[*p,1],clearer_endpoint=ep,foreign=row['foreign'],foreign_entry=ap,all_zero_C_E_continuation_counts=sol))
 else:
  assert ix in twos and row['returned_atom']=='U';A=(0,1);localA=rot(sub(A,ap),-ah);assert br[localA]is False;why='original_A_clock2_cleanup_forces_fresh_age1_helper_output_before_WHITE';guard=A;read=brd[localA][0]
  # Signed all-age A first-retirement law forces H=V/VC(0,4,S), clock2.
  hp=(0,4);hh=2;HS={at(z,hp,hh)for z in Vbase};whites={at(z,ap,ah)for z,b in br.items()if not b};hits=sorted(HS&whites);assert hits==[(-2,3),(-2,4),(-1,4),(0,3)]
  newA=(0,3);assert at((0,1),hp,hh)==newA;newlocal=rot(sub(newA,ap),-ah);assert br[newlocal]is False
  for hgi in(4,5):
   _,_,_,_,hrd=derive(G[hgi]['word']);assert hrd[(0,1)][-1]==[11,'R'];assert Vbase<=set(map(tuple,G[hgi]['outputs']))
  helpers.append(dict(case=ix,old_original_A=A,forced_cleanup_families=['V','VC'],forced_cleanup_pose=[0,4,2],actual_full_source_C_clock=2,foreign_C_clock=3,fresh_helper_six_output_cells=sorted(HS),before_WHITE_fresh_helper_cells=hits,chosen_helper_new_A=newA,last_actual_H_R=[11,'R'],combined_before_WHITE_first_read=brd[newlocal][0],correct_universal_produced_input_minimum=2,helper_output_age_at_foreign_entry=1))
 rows.append(dict(case=ix,foreign=row['foreign'],foreign_pose=row['foreign_pose'],returned_atom=row['returned_atom'],returned_pose=row['returned_pose'],actual_old_source_C_clock=0,foreign_C_clock=3,exclusion=why,source_guard=guard,actual_combined_first_read=read))
assert len(rows)==18 and len(del_end)==12 and len(bud_end)==80 and len(helpers)==2
# The eighty endpoint rows repeat some target poses for different returned atoms;
# preserve every catalogue annotation rather than deduplicate ownership silently.
J=json.loads((R/'audits/dcuv_count5_replay/queries.json').read_text());assert all(v['certified_minimum_C_age']>=2 for v in J['slots'].values())
# Prescribed genuine-prefix attempts before claiming universal ancestry guards.
mp={a:i for i,a in enumerate('DCVUFQB')};attempts=[]
for ns in('VCDCDUCDUFV','VCCVCDVUQU'):
 word=''.join(W[mp[a]]['word']for a in ns);bad=derive(word,True);assert isinstance(bad,dict)
 offset=0
 for a in ns:
  n=len(W[mp[a]]['word'])
  if offset<=bad['conflict_tick']<offset+n:owner=[a,bad['conflict_tick']-offset];break
  offset+=n
 if ns=='VCDCDUCDUFV':assert bad['conflict_tick']==97 and bad['cell']==(-1,0)and owner==['C',1]
 else:
  assert bad['conflict_tick']==198 and bad['cell']==(3,3)and owner==['Q',61]
  rq,par,head,heading,_=derive(word[:198]);initial={z for z,b in rq.items()if b};board=set(initial);head=(0,0);heading=0
  for expected in word[:198]:
   actual='L'if head in board else'R';assert actual==expected;board.symmetric_difference_update({head});heading=(heading+(-1 if actual=='L'else 1))%4;head=add(head,VEL[heading])
  assert head==(3,3)and head in board and word[198]=='R';bad['actual_198_prefix_initial_black_board']=sorted(initial);bad['actual_turn_at_failure']='L';bad['desired_turn_at_failure']='R'
 attempts.append(dict(prescribed_word=ns,actual_conflict=bad,owner=owner,scope='specific finite genuine-prefix attempt, not a complete foreign/returned or U-entry control'))
D=[GP,QP,CP,PP,R/'returned_V_source_reduction_2026-10-23/manifest.json',R/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact_manifest.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'core_periodicity_new/V_parallel_reproductive_supply_frozen_20261023_2036/manifest.json',R/'core_periodicity_new/V_C_same_heading_exclusion_frozen_20261023_2043/manifest.json',R/'core_periodicity_new/atomic_exit_bud_frozen_20261023_1325/manifest.json',R/'audits/dcuv_count5_replay/queries.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='All18 necessary V-source first-returned-contact labels left by signedb1bd1068 have actual preforeign ancestry contradictions:6 source-deleted(1,1) rebirth guards,10 genuine exit-bud endpoint guards,2 forced oldA cleanup/young fresh helper cohorts. Combined with signed94 reduction this excludes all112 V-source first-contact labels. No first-foreign law is carried through foreign; no returned simplicity, later-contact or second-foreign claim.',all18_residual_rows=rows,all38_deleted_guard_atomic_rebirth_roles=rebirth,twelve_deleted_guard_endpoint_obligations=del_end,eighty_exit_bud_endpoint_obligations=bud_end,two_genuine_A_cleanup_fresh_cohort_guards=helpers,individually_prescribed_actual_attempts=attempts,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'V_residual_guards.json').write_text(json.dumps(o,indent=2)+'\n');print('All18 V residues:6 deleted(1,1),10 genuine exitbud(2,2) endpoints,2 actual A-cleanup fresh young output conflicts.')
