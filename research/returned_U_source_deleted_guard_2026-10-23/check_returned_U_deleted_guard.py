"""Seven actual U-source returned-contact residues: source-deleted(0,2) guard.
One 38-role atomic output inventory, arbitrary zero-C E runs solved exactly.
No postforeign maturation, returned simplicity, or generic prefix enumeration.
"""
from pathlib import Path
from collections import Counter
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';QP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json';CP=R/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact.json'
G=json.loads(GP.read_text())['geometry'];W=json.loads(QP.read_text())['macro_words'];C=json.loads(CP.read_text());M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};L={(0,0),(0,1),(1,0),(1,1)};VEL=((0,1),(1,0),(0,-1),(-1,0))
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def at(q,p,h):return add(p,rot(q,h))
def derive(w):
 p=(0,0);h=0;par=set();rq={};rd={}
 for t,ch in enumerate(w):
  b=(ch=='L')^(p in par);assert p not in rq or rq[p]==b;rq[p]=b;rd.setdefault(p,[]).append([t,ch]);par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEL[h])
 return rq,par,p,h,rd
q=(0,2);uq,up,_,_,urd=derive(W[3]['word']);assert urd[q][-1]==[20,'L'] and not(uq[q]^(q in up))
for gi in(7,8,9):
 rq,par,ep,dh,rd=derive(G[gi]['word']);assert rd[q][-1]==[20,'L'];assert q not in set(map(tuple,G[gi]['outputs']))and q not in{at(z,ep,dh)for z in K}
# Same-source cones: after U base, N0 heads y>=4, W1 heads H>=5.
assert q[1]<4 and q[1]-q[0]<5
AT=[]
for i in range(4):
 rq,par,ep,dh,rd=derive(W[i]['word']);ctx,_,_,_,_=derive(W[i]['word']+M);outs={z for z in rq if rq[z]^(z in par)}-{at(z,ep,dh)for z in K};assert all(z[1]>=0 and sum(z)>=0 for z in outs)
 AT.append(dict(name='DCVU'[i],endpoint=ep,turn=dh,outputs=outs,context=ctx))
# Full producer C tails are included: S C3 finishes at3; E C4 starts3 but
# finishes4 and cannot precede these E foreign entries at exact clock3.
roles=[];surv=[]
for h in(2,1):
 for a in AT:
  for slot in sorted(a['outputs']):
   p=sub(q,rot(slot,h));ep=at(a['endpoint'],p,h);hits=sorted({at(z,p,h)for z in a['context']}&L)
   if(sum(p)+h)%2:why='wrong_active_sector'
   elif hits:why='held_original_U_star_in_actual_complete_context'
   elif h==1 and a['name']=='C':why='E_C4_full_completion_after_foreign_clock3'
   else:
    assert h==1 and(a['name'],slot,p,ep)in(('V',(2,1),(-1,4),(2,3)),('U',(1,2),(-2,3),(2,3)),('U',(2,1),(-1,4),(3,4)))
    why='remaining_plain_E3_full_base_endpoint';surv.append((a['name'],slot,p,ep))
   roles.append(dict(heading=h,atom=a['name'],output_slot=slot,pose=[*p,h],endpoint=[*ep,(h+a['turn'])%4],held_star_hits=hits,reason=why))
assert len(roles)==38 and len(surv)==3
assert all(x['reason']in('wrong_active_sector','held_original_U_star_in_actual_complete_context')for x in roles if x['heading']==2)
ids=(297,298,351,352,362,363,364);cases=[];endpoints=[]
for ix in ids:
 row=C['old_source_contact_cases'][ix];assert row['source_atom']=='U'and row['source_to_foreign_C_age']==3
 j='DCVUFQB'.index(row['foreign']);i='DCVU'.index(row['returned_atom']);ap=tuple(row['foreign_pose'][:2]);ah=row['foreign_pose'][2];pp=tuple(row['returned_pose'][:2]);ph=row['returned_pose'][2];assert ah==1 and ph==3
 ar,_,aep,adh,ard=derive(W[j]['word']+M);rawa,_,rawaep,rawadh,raward=derive(W[j]['word']);_,_,rawpep,rawpdh,_=derive(W[i]['word'])
 assert at(rawaep,ap,ah)==pp and(ah+rawadh)%4==ph
 foreignctx={at(z,ap,ah)for z in ar};pr,_,_,_,_=derive(W[i]['word']+M);returnctx={at(z,pp,ph)for z in pr};assert not L&foreignctx and not L&returnctx
 br,_,_,_,brd=derive(W[j]['word']+W[i]['word']+M);local=rot(sub(q,ap),-ah);assert br[local]is True and local not in K
 first=brd[local][0];assert first[1]=='L';marker_only=q in foreignctx and local not in rawa
 if marker_only:assert row['foreign']in('Q','B')and first[0]==len(W[j]['word'])+1
 else:assert q not in foreignctx and row['returned_atom']=='U'and first[0]==len(W[j]['word'])+13
 cases.append(dict(catalogue_case=ix,foreign=row['foreign'],foreign_pose=row['foreign_pose'],foreign_C_clock=3,returned_atom=row['returned_atom'],returned_pose=row['returned_pose'],source_deleted_guard=q,guard_combined_local=local,guard_first_physical_read=first,guard_ownership='foreign_marker_only_input; returned RAW phase1'if marker_only else'returned_U_lower_q_RAW13',both_contexts_miss_original_star=True))
 allowed=('V','U')if row['foreign']in('F','Q')else('U',)
 for name,slot,p,ep in surv:
  dx=ap[0]-ep[0];down=ep[1]-ap[1];solutions=[]
  for v in range(max(down+1,0)):
   d=down-v;rem=dx-d-3*v
   if rem<0 or rem%4:continue
   u=rem//4;last=[n for n,c in(('D',d),('V',v),('U',u))if c and n in allowed];solutions.append(dict(d=d,v=v,u=u,allowed_last=last))
  # If no intervening base at all, the origin itself would have to be allowed;
  # no such zero-displacement case occurs in these seven target positions.
  assert ep!=ap and all(not s['allowed_last']for s in solutions)
  endpoints.append(dict(catalogue_case=ix,origin=name,origin_pose=[*p,1],origin_output_slot=slot,origin_endpoint=ep,foreign_entry=ap,all_arbitrary_zero_C_E_run_counts=solutions,reason='no_count_solution_with_actual_allowed_last_full_packet'))
assert len(cases)==7 and len(endpoints)==21
# The seven are exactly all existing U-source rows whose foreign and returned
# atomic complete contexts both miss original L; enumerate no new geometry.
miss=[]
for ix,row in enumerate(C['old_source_contact_cases']):
 if row['source_atom']!='U':continue
 j='DCVUFQB'.index(row['foreign']);i='DCVU'.index(row['returned_atom']);ap=tuple(row['foreign_pose'][:2]);ah=row['foreign_pose'][2];pp=tuple(row['returned_pose'][:2]);ph=row['returned_pose'][2]
 ar,_,_,_,_=derive(W[j]['word']+M);pr,_,_,_,_=derive(W[i]['word']+M)
 if not L&{at(z,ap,ah)for z in ar}and not L&{at(z,pp,ph)for z in pr}:miss.append(ix)
assert tuple(miss)==ids
D=[GP,QP,CP,R/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact_manifest.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='Seven exact U-source first-returned-atom contact configurations at foreign clock3 are impossible after genuine U/UC/UCC plus uninterrupted complete-eight. Actual foreign+returned before-mask requires source-deleted(0,2) black outside foreign entry core. Its genuine preforeign rebirth has no N0/W1/S2 origin and only3 E3 origins, all killed by exact endpoint/allowed-last equations. This exclusion does not need chronological first-contact itself, returned simplicity, postforeign identity-age laws or any attained control.',source_U_guard_reads=urd[q],all38_atomic_rebirth_roles=roles,three_plain_E3_origin_ports=[dict(atom=n,output=o,pose=[*p,1],endpoint=e)for n,o,p,e in surv],seven_existing_U_source_contact_rows=cases,twenty_one_unbounded_E_endpoint_obligations=endpoints,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'returned_U_deleted_guard.json').write_text(json.dumps(o,indent=2)+'\n');print('All7 U-source both-context-star-miss residues excluded by genuine deleted(0,2):38 atomic roles,3 E3 origins,21 exact unbounded endpoint/last-packet equations.')
