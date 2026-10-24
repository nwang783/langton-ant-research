"""Exact obstruction to canonical backward REANCHORING, not a no-map theorem.
No new prefix enumeration. Uses the fourteen signed necessary parent interfaces.
"""
from pathlib import Path
import json,hashlib,importlib.util
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
JP=R/'returned_D_last_C_parent_reduction_2026-10-24/D_last_C_parent_reduction.json';QP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json';GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';CP=R/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact.json'
J=json.loads(JP.read_text());W=json.loads(QP.read_text())['macro_words'];G=json.loads(GP.read_text())['geometry'];CAT=json.loads(CP.read_text());M='LLLLRLRRRRL';VEL=((0,1),(1,0),(0,-1),(-1,0))
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def ctr(p,h):return add((2*p[0],2*p[1]),rot((-1,-1),h))
def pose_in(q,p,h):return [*rot(sub(tuple(q[:2]),p),-h),(q[2]-h)%4]
def center_in(q,p,h):return rot(sub(q,(2*p[0],2*p[1])),-h)
def endpoint(w):
 p=(0,0);h=0
 for z in w:h=(h+(-1 if z=='L'else 1))%4;p=add(p,VEL[h])
 return p,h
parents=[];previous=[]
for f in J['fourteen_remaining_genuine_DC_VC_interfaces']:
 ix=f['catalogue_id'];r=CAT['old_source_contact_cases'][ix];p=tuple(f['packet_entry'][:2]);h=f['packet_entry'][2];assert h==1
 fp=pose_in(r['foreign_pose'],p,h);rp=pose_in(r['returned_pose'],p,h);q=(-1,-1)if ix==15 else(0,0);qnew=center_in(q,p,h)
 assert fp[2]==0 and rp[2]==2
 parents.append(dict(catalogue_id=ix,parent_full_packet=f['last_positive_C_full_packet'],short_actual_N_run=f['actual_pre_D_zero_C_word'],parent_entry_in_selectedD_frame=f['packet_entry'],rebased_foreign_pose=fp,rebased_returned_pose=rp,source_to_foreign_C_age=4,rebased_contact_point=qnew,actual_contact_owner='later selected D, not earlier D/V parent base',parent_base_to_contact_owner_atomic_index=2+len(f['actual_pre_D_zero_C_word']),same_three_F_normalized_foreign_heading=False,obstruction='all three target templates require foreign headingE1; parent-normalized foreign heading isN0; C distance grows3to4'))
 run=f['actual_pre_D_zero_C_word']
 if not run:continue
 a=run[-1];pp=(-1,-1)if a=='D'else(-1,-3);hh=0;newF=pose_in(r['foreign_pose'],pp,hh);newR=pose_in(r['returned_pose'],pp,hh);qc=center_in(q,pp,hh)
 near=(ix==15 and a=='D');assert near==(newF==[3,-4,1]and newR==[1,0,3]and r['returned_atom']=='C')
 if a=='D':
  assert newF==([3,-4,1]if ix==15 else[4,-3,1]);assert qc==((1,1)if ix==15 else(2,2))
  owner='outgoing later D at older D END'if ix==15 else'strict midpoint of later D, beyond older D END'
 else:assert ix==15 and newF==[3,-2,1]and newR==[1,2,3]and qc==(1,5);owner='outgoing later D at older V END'
 previous.append(dict(catalogue_id=ix,parent_full_packet=f['last_positive_C_full_packet'],short_actual_N_run=run,strictly_earlier_plain_packet=a,earlier_entry=pp,rebased_foreign_pose=newF,rebased_returned_pose=newR,rebased_contact_point=qc,actual_contact_owner=owner,source_to_foreign_C_age=3,foreign_normal_before=sum(r['foreign_pose'][:2]),foreign_normal_after=sum(newF[:2]),normal_increase=2 if a=='D'else 4,head_pose_near_match_to_C75=near,actual_earlier_full_packet_is_DC=False,earlier_packet_has_no_C1=True))
assert len(parents)==14 and len(previous)==12
# The tempting D15+D -> C75 geometry is NOT an actual DC packet.
actual=W[0]['word']*2+M;hyp=W[0]['word']+W[1]['word']+M
first=next(i for i,(a,b)in enumerate(zip(actual,hyp))if a!=b);assert first==21 and(actual[first],hyp[first])==('L','R')
epDD,hDD=endpoint(W[0]['word']*2);epDC,hDC=endpoint(W[0]['word']+W[1]['word']);assert(epDD,hDD)==((2,2),0)and(epDC,hDC)==((1,2),3)
assert ctr(epDD,hDD)==ctr(epDC,hDC)==(3,3)
OP=R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py';spec=importlib.util.spec_from_file_location('own',OP);own=importlib.util.module_from_spec(spec);spec.loader.exec_module(own)
contrast=dict(actual_two_plain_D_RAW_length=20,hypothetical_DC_RAW_length=25,first_physical_disagreement_tick0=first,actual_owner=own.describe('DD',first),hypothetical_owner=own.describe('DC',first),actual_end_head=[*epDD,hDD],hypothetical_end_head=[*epDC,hDC],coincident_END_corrected_center=[3,3],actual_C_increments=0,hypothetical_C_increments=1,warning='Equal corrected centers do not identify physical head/heading, fine time, packet word, C clock or birth/core ownership.')
D=[JP,QP,GP,CP,OP,R/'returned_D_last_C_parent_reduction_2026-10-24/manifest.json',R/'returned_D_forced_core_ports_2026-10-24/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_EXACT_REANCHORING_OBSTRUCTION_PENDING_REVIEW',scope='Assesses canonical exact backward reanchoring of the fourteen necessary D-parent interfaces. No well-founded same-three-F recurrence is obtained. Does NOT rule out a more elaborate future history-preserving map, and does not eliminate or attain any necessary interface.',all14_last_positive_C_parent_rebasings=parents,all12_nonempty_short_run_immediate_predecessor_rebasings=previous,tempting_D15_to_C75_literal_countercheck=contrast,exact_data_that_changes_or_grows=['Crossing the positive-C parent increases true source-to-foreign C distance3to4 and rotates normalized foreign headingEtoN.','Stepping backward through one N-oriented plainD keeps age3 but increases foreign normal x+y by2; a plainV increases it by4.','The strict older creator does not own the first contact: the actual later D remains owner, at older-END or a later midpoint. Source-to-owner atomic offset increases.','A hypothetical DD-to-DC replacement changes physical read21, fine length20to25, head/heading, C count and core/identity ownership despite coincident corrected END centers.','No uniform bound or monotone cancellation of older boundary labels is supplied; full genuine port/core history must be retained.'],dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'backward_interface.json').write_text(json.dumps(o,indent=2)+'\n');print('14 positive-C rebasings,12 immediate N-predecessor rebasings; exact DD/DC mismatch21 and preserved later contact ownership.')
