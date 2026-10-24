"""Genuine U ancestry guards for one foreign then one complete-eight star consumer.
72 fixed interface rows only; no prefix enumeration or postforeign permanence.
"""
from pathlib import Path
from collections import Counter
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';QP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json';PP=R/'foreign_U_port_interfaces_2026-10-23/foreign_U_ports.json'
G=json.loads(GP.read_text())['geometry'];W=json.loads(QP.read_text())['macro_words'];PORTS=json.loads(PP.read_text())['postreturn']['gates'];M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};L={(0,0),(0,1),(1,0),(1,1)};E={(2,0),(2,1)};VEL=((0,1),(1,0),(0,-1),(-1,0));INDEX={g['name']:i for i,g in enumerate(G)}
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def at(q,p,h):return add(p,rot(q,h))
def derive(w):
 p=(0,0);h=0;par=set();req={};reads={}
 for t,ch in enumerate(w):
  b=(ch=='L')^(p in par);assert p not in req or req[p]==b,(t,p);req[p]=b;reads.setdefault(p,[]).append((t,ch));par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEL[h])
 return req,par,p,h,reads
assert len(PORTS)==24
rows=[]
for port in PORTS:
 i=INDEX[port['packet']];rp=tuple(port['pose'][:2]);rh=port['pose'][2];pw=G[i]['word']
 for j in(4,5,6):
  aw=W[j]['word'];ah=(rh-2)%4;_,_,ep,dh,_=derive(aw);assert dh==2;ap=sub(rp,rot(ep,ah));acore={at(q,ap,ah)for q in K};ar,_,_,_,ard=derive(aw+M)
  assert not L&{at(q,ap,ah)for q in ar}, 'All four original identities survive foreign COMPLETE context and remain outside its exit core'
  rq,_,_,_,rd=derive(aw+pw+M)
  star_reads=[]
  for q in sorted(L):
   z=rot(sub(q,ap),-ah)
   if z not in rd:continue
   t,ch=rd[z][0];assert ch=='L'and t>=len(aw)+11
   star_reads.append(dict(cell=q,first_combined_read=[t,ch],phase_in_returned_packet=t-len(aw),physical_owner='returned packet RAW'if t<len(aw)+len(pw)else'following word RAW phase1; returned packet exit-core absorption',original_tag_unread_through_foreign_complete_context=True))
  assert len(star_reads)==1
  # Force only ACTUAL earlier renewal producers from original current-identity
  # absence. Each fresh star is checked at foreign ENTRY, never assumed current
  # after the foreign begins. The combined before-requirement already accounts
  # for every foreign toggle and marker/core ownership change.
  trace=[];blocked=False;last_j=0
  for k in range(4):
   hp=(3*k,-k);ls={at(q,hp,0)for q in L};es={at(q,hp,0)for q in E}
   def witnesses(T):
    out=[]
    for q in sorted(T):
     z=rot(sub(q,ap),-ah)
     if q in acore:out.append(dict(cell=q,reason='genuine current identity in foreign entry core'))
     elif rq.get(z)is False:out.append(dict(cell=q,reason='combined actual before-requirement WHITE',first_combined_read=rd[z][0],reader='foreign RAW'if rd[z][0][0]<len(aw)else'returned RAW'if rd[z][0][0]<len(aw)+len(pw)else'following marker'))
    return out
   star_bad=witnesses(ls);east_absence=witnesses(es)
   trace.append(dict(actual_U_producer_index=k,pose=[*hp,0],source_C_entry_clock=4*k,fresh_star=sorted(ls),star_conflicts=star_bad,east_absence_forcing_witnesses=east_absence))
   last_j=k
   if star_bad:blocked=True;break
   if not east_absence:break
   assert k<3, 'Finite target footprint is exhausted by the third guardian'
  nres=(-ah)%4
  if blocked:classification='universal_genuine_ancestry_guard_obstruction';bound=None
  elif last_j==0 and rh==1:
   assert ap[1]<=4 and nres==1
   # At exact one C every reachable W cut from U base exit has y>=5.
   classification='necessary_foreign_clock_at_least5';bound=5
  elif last_j==0 and rh==2:
   assert nres==0
   classification='necessary_foreign_clock_at_least4';bound=4
  elif last_j==1 and port['packet']in('V','VC'):
   assert j==4 and sub(ap,(3,-1))==(3,-2)and ah==1
   # It is exactly the actual guardian's marker-only F mechanism, whose signed
   # relative clock lower bound7 adds to its real global entry clock4.
   z=rot(sub((4,0),ap),-ah);assert z==(-3,-2)and ard[z][0]==(57,'L')
   classification='necessary_foreign_clock_at_least11_with_actual_first_renewal';bound=11
  else:
   assert last_j==1 and port['packet']in('U','UC')and nres==3
   classification='necessary_foreign_clock_at_least7_with_actual_first_renewal';bound=7
  rows.append(dict(foreign='DCVUFQB'[j],foreign_pose=[*ap,ah],returned_packet=port['packet'],returned_entry_pose=port['pose'],foreign_C_age_residue=nres,original_star_first_read=star_reads[0],genuine_renewal_guard_trace=trace,classification=classification,necessary_foreign_C_age_at_least=bound))
assert len(rows)==72
assert Counter(r['classification']for r in rows)=={'universal_genuine_ancestry_guard_obstruction':37,'necessary_foreign_clock_at_least5':9,'necessary_foreign_clock_at_least4':18,'necessary_foreign_clock_at_least11_with_actual_first_renewal':2,'necessary_foreign_clock_at_least7_with_actual_first_renewal':6}
assert Counter(len(r['genuine_renewal_guard_trace'])-1 for r in rows if r['classification']=='universal_genuine_ancestry_guard_obstruction')=={1:33,2:2,3:2}
# Validate the exact zero-C exclusion for the eighteen N-foreign/S-return rows.
# N transport is monotone, so the head equations have finitely many nonnegative
# count solutions. Pair adjacency restricts the last complete-eight base.
zero_rows=[]
for r in rows:
 if r['classification']!='necessary_foreign_clock_at_least4':continue
 x,y,ah=r['foreign_pose'];assert ah==0
 allowed_last={'V','U'}if r['foreign']in('F','Q')else{'U'}
 solutions=[]
 for d in range(x+1):
  v=x-d
  rem=y-4-d-3*v
  if rem<0 or rem%4:continue
  u=rem//4
  last=[a for a,count in(('D',d),('V',v),('U',u))if count and a in allowed_last]
  if last:solutions.append(dict(d=d,v=v,u=u,allowed_last=last))
 if solutions:
  assert r['returned_packet']in('U','UC')
  if r['foreign']=='Q':assert solutions==[dict(d=2,v=1,u=0,allowed_last=['V'])];names='UDDVQ';failphase=1
  else:assert r['foreign']=='B'and solutions==[dict(d=2,v=0,u=1,allowed_last=['U'])];names='UDDUB';failphase=1
  # Each count solution plus forced last base fixes the entire old factor.
  word=''.join(W['DCVUFQB'.index(a)]['word']for a in names)+G[INDEX[r['returned_packet']]]['word']+M
  p=(0,0);h=0;par=set();rq={};origin={};bad=None;oldlen=sum(len(W['DCVUFQB'.index(a)]['word'])for a in names)
  for t,ch in enumerate(word):
   need=(ch=='L')^(p in par)
   if p in rq and rq[p]!=need:bad=dict(global_tick=t,returned_RAW_phase=t-oldlen,cell=p,first_read=origin[p]);break
   rq[p]=need;origin.setdefault(p,[t,ch]);par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEL[h])
  assert bad and bad['returned_RAW_phase']==1 and bad['cell']==(0,5)and bad['first_read']==[39,'L']
 else:names=None;bad=None
 zero_rows.append(dict(foreign=r['foreign'],foreign_pose=r['foreign_pose'],returned_packet=r['returned_packet'],N_count_solutions_surviving_actual_last_base=solutions,only_possible_zero_C_word=names,immutable_conflict=bad))
assert len(zero_rows)==18 and sum(bool(r['N_count_solutions_surviving_actual_last_base'])for r in zero_rows)==4
D=[GP,QP,PP,R/'foreign_U_port_interfaces_2026-10-23/manifest.json',R/'core_periodicity_new/causal_cycle_renewal_20261023_1841/manifest.json',R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',R/'core_periodicity_new/U_renewal_exact_clock_frozen_20261023_1902/manifest.json',R/'foreign_U_marker_clocks_2026-10-23/manifest.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='First original-U-star residual effect in exactly one complete-eight packet immediately after one actual foreign, whose COMPLETE context misses all four original tags. Genuine preforeign U/UC/UCC ancestry, actual changed core, foreign+packet before-context and successor-owned marker reads retained. 37 of72 local suffixes universally obstructed;35 necessary residues receive lower clocks5/4/7/11. A foreign marker-only absorption is explicitly outside this case and remains separately classified. No physical attainment, postforeign permanence, returned-path simplicity or language termination.',rows=rows,zero_C_N_head_and_actual_word_exclusions=zero_rows,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'one_foreign_return_U_star.json').write_text(json.dumps(o,indent=2)+'\n');print('72 actual suffixes:37 genuine ancestry obstructions;35 necessary residues with clocks>=5(9),>=4(18),>=7(6),>=11(2). No attainment.')
