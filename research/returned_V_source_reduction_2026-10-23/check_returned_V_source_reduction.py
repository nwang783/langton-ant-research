"""94/112 existing V-source returned first-contact labels excluded.
Actual last-R old cohorts and common-bud endpoint ancestry;18 remain necessary.
No generic prefix enumeration, returned simplicity, or postforeign age law.
"""
from pathlib import Path
from collections import Counter
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';QP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json';CP=R/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact.json'
G=json.loads(GP.read_text())['geometry'];W=json.loads(QP.read_text())['macro_words'];C=json.loads(CP.read_text());M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};VEL=((0,1),(1,0),(0,-1),(-1,0));S=set(map(tuple,G[4]['outputs']));r=(0,0);B=(1,0);bud=(2,0)
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def at(q,p,h):return add(p,rot(q,h))
def derive(w,stop_on_conflict=False):
 p=(0,0);h=0;par=set();rq={};rd={};first={}
 for t,ch in enumerate(w):
  b=(ch=='L')^(p in par)
  if p in rq and rq[p]!=b:
   if stop_on_conflict:return dict(conflict_tick=t,cell=p,previous_first_read=first[p],required_initial=b,required_initial_at_first=rq[p],last_pose=[*p,h],read_log=rd)
   raise AssertionError((t,p))
  if p not in rq:rq[p]=b;first[p]=[t,ch]
  rd.setdefault(p,[]).append([t,ch]);par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEL[h])
 return rq,par,p,h,rd
# Genuine last-R source identities survive their actual source C tails.
vr,_,_,_,vrd=derive(W[2]['word']);source=[]
for gi in(4,5,6):
 qr,_,_,_,qrd=derive(G[gi]['word']);assert S<=set(map(tuple,G[gi]['outputs']))
 for z in S:assert qrd[z]==vrd[z]and qrd[z][-1][1]=='R'
 source.append(dict(full_source=G[gi]['name'],base_outputs=[dict(cell=z,last_source_R=vrd[z][-1])for z in sorted(S)]))
# Exact direct signed queries: ALL produced residual input slots have minimum>=2.
J=json.loads((R/'audits/dcuv_count5_replay/queries.json').read_text());assert J['status'].startswith('PASS');assert all(v['certified_minimum_C_age']>=2 for v in J['slots'].values())
# Raw C followed by U is intrinsically impossible, separately preserving actual ownership.
cu=derive(W[1]['word']+W[3]['word'],True);assert cu['conflict_tick']==29 and cu['cell']==(-1,0)and cu['previous_first_read']==[1,'L']
# Eight allowed common-bud clearer input roles, followed by all arbitrary E runs
# to the two foreign targets whose actual before requirement is WHITE.
common=[]
for j,target in((4,(2,-3)),(5,(4,-3))):
 aq,_,_,_,ard=derive(W[j]['word']+M);local=rot(sub(bud,target),-1);assert aq[local]is False and ard[local][0][1]=='R'and ard[local][0][0]<len(W[j]['word'])
 for gi in(0,4,7):
  for slot in map(tuple,G[gi]['inputs']):
   p=sub(bud,rot(slot,1));ep=at(tuple(G[gi]['endpoint'][:2]),p,1);dx=target[0]-ep[0];down=ep[1]-target[1];sol=[]
   for v in range(max(down+1,0)):
    d=down-v;rem=dx-d-3*v
    if rem<0 or rem%4:continue
    u=rem//4;last=[a for a,c in(('D',d),('V',v),('U',u))if c and a in('V','U')];sol.append(dict(d=d,v=v,u=u,allowed_last=last))
   assert ep!=target and all(not s['allowed_last']for s in sol)
   common.append(dict(foreign='DCVUFQB'[j],foreign_entry=[*target,1],old_bud=bud,foreign_bud_local=local,first_before_WHITE_read=ard[local][0],C_age=3,clearer=G[gi]['name'],input_slot=slot,clearer_entry=[*p,1],clearer_endpoint=ep,all_zero_C_E_continuation_counts=sol))
assert len(common)==16
rows=[];early=[];residual=[]
for ix,row in enumerate(C['old_source_contact_cases']):
 if row['source_atom']!='V':continue
 n=row['source_to_foreign_C_age'];assert 0<=n<=4;j='DCVUFQB'.index(row['foreign']);i='DCVU'.index(row['returned_atom']);p=tuple(row['foreign_pose'][:2]);h=row['foreign_pose'][2]
 br,_,_,_,brd=derive(W[j]['word']+W[i]['word']+M);white={at(z,p,h)for z,b in br.items()if not b};guard=None;read=None;bounds=None
 if n<=1:
  hit=S&white
  if hit:why='young_all_six_V_base_identities_current_before_combined_WHITE';guard=sorted(hit)[0]
  elif n==0:
   assert row['foreign']in('Q','B');assert(p,h)in(((3,5),0),((2,6),0));dx=p[0]-1;dy=p[1]-3;sol=[]
   for d in range(dx+1):
    v=dx-d;rem=dy-d-3*v
    if rem<0 or rem%4:continue
    u=rem//4;last=[a for a,c in(('D',d),('V',v),('U',u))if c and(a in('V','U')if row['foreign']=='Q'else a=='U')];sol.append(dict(d=d,v=v,u=u,allowed_last=last))
   assert all(not s['allowed_last']for s in sol);why='clock0_N_run_has_no_actual_allowed_last_foreign_predecessor';bounds=dict(all_N_run_counts=sol)
  else:
   assert h==3 and p[1]<=4
   if p[1]<4:why='one_C_N_to_W_head_minimum_y4_exceeds_foreign_y';bounds=dict(minimum_y=4)
   else:
    # y4 forces the only C to be sourceVC's own C1 and ALL W bases to be U.
    numer=1-p[0]
    if numer<0 or numer%4:why='clock1_y4_W_U_only_run_wrong_x_residue';bounds=dict(W_start=[1,4,3],required_four_U_displacement=numer)
    else:
     u=numer//4;assert u>=1;why='clock1_forces_actual_VC_then_U_and_raw_C_U_is_literal_conflict';bounds=dict(source_full='VC',forced_first_W='U',number_W_U=u,C_U_conflict={k:v for k,v in cu.items()if k!='read_log'})
   early.append(dict(catalogue_case=ix,foreign=row['foreign'],foreign_pose=row['foreign_pose'],proof=why,exact_interface=bounds))
 elif r in white:why='genuine_V_r_first_retirement5_vs_combined_before_WHITE';guard=r
 elif n<=3 and B in white:why='genuine_V_B_first_retirement4_vs_combined_before_WHITE';guard=B
 elif n==3 and(row['foreign'],p)in(('F',(2,-3)),('Q',(4,-3))):why='genuine_common_bud3_E_clearer_endpoint_guard';guard=bud
 else:why='necessary_geometry_not_asserted_attained';residual.append(ix)
 if guard is not None:
  local=rot(sub(guard,p),-h);read=brd[local][0]
 rows.append(dict(catalogue_case=ix,foreign=row['foreign'],foreign_pose=row['foreign_pose'],returned_atom=row['returned_atom'],returned_pose=row['returned_pose'],source_to_foreign_C_clock=n,contact=row['contact'],classification=why,chosen_same_source_guard=guard,actual_combined_first_read=read,exact_head_interface=bounds))
counts=Counter(x['classification']for x in rows);assert len(rows)==112 and len(residual)==18
assert counts['young_all_six_V_base_identities_current_before_combined_WHITE']==39
assert sum(v for k,v in counts.items()if k.startswith(('clock0_','one_C_','clock1_')))==11
assert counts['genuine_V_r_first_retirement5_vs_combined_before_WHITE']==26
assert counts['genuine_V_B_first_retirement4_vs_combined_before_WHITE']==14
assert counts['genuine_common_bud3_E_clearer_endpoint_guard']==4
assert residual==[167,168,169,173,174,175,211,212,213,214,215,216,217,218,219,220,221,222]
# Individually prescribed causal controls, not generic or bounded prefix search.
# This first connector is actually legal up to foreign entry; the foreign then
# demands WHITE at the same old V bud. It is NOT claimed to have a U-entry lift.
mp={a:i for i,a in enumerate('DCVUFQB')};prescribed=[]
for ns in('VCDCVVCDUF','VCDCDUCVUBD','UCCVCDCVVCDUF'):
 word=''.join(W[mp[a]]['word']for a in ns);out=derive(word,True);assert isinstance(out,dict)
 offset=0;owner=None
 for a in ns:
  nn=len(W[mp[a]]['word'])
  if offset<=out['conflict_tick']<offset+nn:owner=dict(atom=a,RAW_phase=out['conflict_tick']-offset);break
  offset+=nn
 if ns=='VCDCVVCDUF':
  assert out['conflict_tick']==188 and out['cell']==bud and owner==dict(atom='F',RAW_phase=41)
  rq0,par0,head0,heading0,_=derive(word[:188]);board={z for z,b in rq0.items()if b};physical=set(board);head=(0,0);heading=0
  for t,expected in enumerate(word[:188]):
   actual='L'if head in physical else'R';assert actual==expected
   physical.symmetric_difference_update({head});heading=(heading+(-1 if actual=='L'else 1))%4;head=add(head,VEL[heading])
  assert head==bud and head in physical and word[188]=='R'
  out['actual_finite_board_before_execution']=sorted(board);out['actual_prefix_length']=188;out['physical_turn_at_divergence']='L';out['expected_F_turn_at_divergence']='R';assert len(board)==27
 if ns=='VCDCDUCVUBD':assert out['conflict_tick']==97 and out['cell']==(-1,0)and owner==dict(atom='C',RAW_phase=1)
 if ns=='UCCVCDCVVCDUF':assert out['conflict_tick']==102 and out['cell']==(-1,1)and owner==dict(atom='C',RAW_phase=1)
 prescribed.append(dict(word=ns,actual_literal_conflict={k:v for k,v in out.items()if k!='read_log'},owner=owner,scope='one prescribed finite connector; no complete foreign or U-entry lift asserted'))
D=[GP,QP,CP,R/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact_manifest.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'audits/dcuv_count5_replay/queries.json',R/'core_periodicity_new/V_parallel_reproductive_supply_frozen_20261023_2036/manifest.json',R/'core_periodicity_new/V_C_same_heading_exclusion_frozen_20261023_2043/manifest.json',R/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='94 of112 signed existing V-source first-returned-contact labels excluded. Actual fresh last-R V-base cohort current at preforeign ages0/1, r current through4, B current through3, plus separate common-bud clearer endpoint guard for F/Q only.18 clock3 necessary geometries remain, no attainment. B may consume the common bud in RAW and is explicitly not removed by that guard. No postforeign age law, returned simplicity, generic prefix enumeration or global capture.',source_last_R_and_actual_C_tail_preservation=source,all112_V_source_rows=rows,classification_counts=dict(counts),eleven_exact_early_head_interfaces=early,sixteen_common_bud_clearer_endpoint_obligations=common,residual_catalogue_cases=residual,individually_prescribed_actual_connector_replays=prescribed,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'returned_V_source_reduction.json').write_text(json.dumps(o,indent=2)+'\n');print('V-source reduction94/112,18 necessary clock3 residues:',dict(counts))
