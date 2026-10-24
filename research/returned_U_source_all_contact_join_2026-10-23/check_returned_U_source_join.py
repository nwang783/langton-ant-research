"""Dependency-minimal join of all148 returned first-contact rows with old U.
Actual color/core cuts plus signed early star effects, D/V clock bounds,
original east-return bounds, and seven source-deleted(0,2) guards.
"""
from pathlib import Path
from collections import Counter
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';QP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json';CP=R/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact.json';OP=R/'one_foreign_return_U_star_2026-10-23/one_foreign_return_U_star.json';XP=R/'returned_U_source_deleted_guard_2026-10-23/returned_U_deleted_guard.json'
G=json.loads(GP.read_text())['geometry'];W=json.loads(QP.read_text())['macro_words'];C=json.loads(CP.read_text());O=json.loads(OP.read_text());X=json.loads(XP.read_text());M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};L={(0,0),(0,1),(1,0),(1,1)};VEL=((0,1),(1,0),(0,-1),(-1,0))
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
old={(r['foreign'],tuple(r['foreign_pose']),r['returned_packet'],tuple(r['returned_entry_pose'])):r for r in O['rows']}
seven={r['catalogue_case']for r in X['seven_existing_U_source_contact_rows']};assert seven=={297,298,351,352,362,363,364}
rows=[]
for ix,r in enumerate(C['old_source_contact_cases']):
 if r['source_atom']!='U':continue
 n=r['source_to_foreign_C_age'];assert 0<=n<=4
 j='DCVUFQB'.index(r['foreign']);i='DCVU'.index(r['returned_atom']);ap=tuple(r['foreign_pose'][:2]);ah=r['foreign_pose'][2];pp=tuple(r['returned_pose'][:2]);ph=r['returned_pose'][2]
 ar,_,_,_,ard=derive(W[j]['word']+M);_,_,aep,adh,_=derive(W[j]['word']);pr,_,_,_,prd=derive(W[i]['word']+M)
 assert at(aep,ap,ah)==pp and(ah+adh)%4==ph
 actx={at(z,ap,ah)for z in ar};pctx={at(z,pp,ph)for z in pr};Ahit=L&actx;Phit=L&pctx;Kentry={at(z,ap,ah)for z in K};Kexit={at(z,pp,ph)for z in K};assert Kexit<=actx
 guard=None;read=None;bound=None;prior=None
 if Ahit:
  core=L&Kentry;white=L&{at(z,ap,ah)for z,b in ar.items()if not b}
  if core:why='foreign_entry_core_overlaps_current_original_star';guard=sorted(core)[0]
  elif white:why='foreign_before_WHITE_conflicts_current_original_star';guard=sorted(white)[0]
  else:
   why='first_foreign_original_star_effect_requires_at_least5';guard=sorted(Ahit)[0];bound=5;local=rot(sub(guard,ap),-ah);assert ar[local]is True and local not in K;read=ard[local][0];assert read[1]=='L'and n<5
 elif not Phit:
  assert ix in seven;why='genuine_source_deleted_02_guard';guard=(0,2)
 elif r['returned_atom']=='C':
  assert not L&Kexit;whitehits=[]
  for guard0 in sorted(Phit):
   local=rot(sub(guard0,pp),-ph);assert local not in K and pr[local]is False;whitehits.append((prd[local][0][0],guard0,local))
  phase,guard,local=min(whitehits);assert phase<15 and prd[local][0][1]=='R';read=prd[local][0];why='actual_returned_C_RAW_before_WHITE_conflicts_unread_old_star'
 else:
  # Complete before-mask is pulled to foreign entry. Since foreign misses L,
  # a before-WHITE star identity is already an immediate initial-color clash.
  br,_,_,_,brd=derive(W[j]['word']+W[i]['word']+M);white=L&{at(z,ap,ah)for z,b in br.items()if not b}
  if white:why='combined_foreign_return_before_WHITE_conflicts_current_star';guard=sorted(white)[0];local=rot(sub(guard,ap),-ah);read=brd[local][0]
  else:
   key=(r['foreign'],tuple(r['foreign_pose']),r['returned_atom'],tuple(r['returned_pose']));assert key in old;prior=old[key];guard=tuple(prior['original_star_first_read']['tag'])if isinstance(prior.get('original_star_first_read'),dict)and'tag'in prior['original_star_first_read']else None
   if n==1:assert prior['classification']=='necessary_foreign_clock_at_least5';why='signed_east_return_clock_at_least5_but_catalogue_clock1';bound=5
   else:
    assert n==4 and r['returned_atom']in('D','V');assert pp==((0,2)if r['returned_atom']=='D'else(0,4))and ph==2
    why='signed_D_or_V_south_return_clock_at_least8_but_catalogue_clock4';bound=8
 rows.append(dict(catalogue_case=ix,foreign=r['foreign'],foreign_pose=r['foreign_pose'],returned_atom=r['returned_atom'],returned_pose=r['returned_pose'],source_to_foreign_C_clock=n,contact=r['contact'],foreign_star_context_hits=sorted(Ahit),returned_star_context_hits=sorted(Phit),exclusion=why,chosen_guard=guard,actual_first_read=read,required_foreign_clock_at_least=bound))
counts=Counter(r['exclusion']for r in rows);assert len(rows)==148
assert counts=={'foreign_entry_core_overlaps_current_original_star':2,'foreign_before_WHITE_conflicts_current_original_star':58,'first_foreign_original_star_effect_requires_at_least5':6,'genuine_source_deleted_02_guard':7,'actual_returned_C_RAW_before_WHITE_conflicts_unread_old_star':6,'combined_foreign_return_before_WHITE_conflicts_current_star':54,'signed_east_return_clock_at_least5_but_catalogue_clock1':9,'signed_D_or_V_south_return_clock_at_least8_but_catalogue_clock4':6}
D=[GP,QP,CP,OP,XP,R/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact_manifest.json',R/'seven_word_spatial_return_2026-10-23/first_foreign_all_source_join_manifest.json',R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',R/'foreign_U_raw_ages34_2026-10-23/manifest.json',R/'foreign_U_star_age2_2026-10-23/manifest.json',R/'foreign_U_marker_clocks_2026-10-23/manifest.json',R/'one_foreign_return_U_star_2026-10-23/manifest.json',R/'one_foreign_return_U_star_2026-10-23/erratum_manifest.json',R/'one_foreign_return_U_star_2026-10-23/ownership_erratum_manifest.json',R/'one_foreign_return_D_clock_2026-10-23/manifest.json',R/'one_foreign_return_V_clock_2026-10-23/manifest.json',R/'returned_U_source_deleted_guard_2026-10-23/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='For an actual U-entry complete-eight interval and first foreign, the FIRST returned ordinary atom cannot have its chronological first new old-proxy contact on an outgoing old U-base chord. All148 existing U-source geometric cases have exact actual core/color or signed ancestry contradictions. No global returned simplicity or second foreign statement. No rejected51018788 or repaired163676a0 U-clock dependency is needed.',count=148,classification_counts=dict(counts),all148_U_source_rows=rows,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'returned_U_source_join.json').write_text(json.dumps(o,indent=2)+'\n');print('All148 old U-source first-returned-contact rows excluded:',dict(counts))
