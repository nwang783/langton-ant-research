"""The paired-rewrite L28 hole is unread by the next FOREIGN RAW, but
an actual following complete C restores it as a new external output.
"""
from pathlib import Path
from collections import Counter
import json,hashlib
# Function-only reuse: no frozen checker or output is executed/written.
source=Path('/workspace/shared/langton/two_foreign_three_C_rewrite_controls_2026-10-24/check_three_C_controls.py').read_text()
exec(source.split("PREFIX=")[0])
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
NE={(-1,-1),(-1,0),(-1,1),(0,0),(0,1),(1,0),(1,1),(1,2),(2,0),(2,1)}
old9=(NE|{(-2,-1)})-{(2,0),(2,1)};gate=(3,-1,0);exit_gate=(3,3,0);hole=(0,2)
new9={add(gate[:2],tuple(q))for q in lit.literal_geometry(W['U'])['outputs']};field=old9|new9
assert len(field)==18 and max(q[1]for q in field)==2

def Wcounts(dx,dy):
 if dx<0 or dy<0:return[]
 out=[]
 for d in range(dy+1):
  v=dy-d;r=dx-d-3*v
  if r>=0 and r%4==0:out.append((d,v,r//4))
 return out

def future_counts(p):
 dx,dy=p[0]-3,p[1]-3;out=[]
 if p[2]==0:
  if dx<0 or dy<0:return[]
  for d in range(dx+1):
   v=dx-d;r=dy-d-3*v
   if r>=0 and r%4==0:out.append(dict(N=(d,v,r//4),W=None))
  return out
 assert p[2]==3
 dy-=1
 if dy<0:return[]
 for d in range(dy+1):
  for v in range((dy-d)//3+1):
   for u in range((dy-d-3*v)//4+1):
    wy=dy-d-3*v-4*u;wx=d+v-dx
    for wc in Wcounts(wx,wy):out.append(dict(N=(d,v,u),W=wc))
 return out

rows=[]
for heading in(0,3):
 for actor in'FQB':
  rt=lit.trace(W[actor]);ct=lit.trace(W[actor]+lit.M)
  for slot,(turn,tick)in rt['first'].items():
   if turn!='R':continue
   p=(*sub(hole,lit.rot(slot,heading)),heading)
   row=dict(actor=actor,ENTRY=p,hole_local_cell=slot,first_R=owner.describe(actor,tick),RAW_last_read=rt['last'][slot])
   if(sum(p[:2])+heading)%2:route='sector'
   else:
    counts=future_counts(p);row['all_nonnegative_endpoint_count_tuples']=counts
    if not counts:route='post_gate_endpoint_impossible'
    else:
     bad=[]
     for held in sorted(field):
      q=lit.rot(sub(held,p[:2]),(-heading)%4);f=ct['first'].get(q)
      if q in lit.K or f and f[0]=='R':bad.append(dict(SAME_CURRENT=held,local=q,reason='ENTRY_CORE'if q in lit.K else'first_WHITE',first=f))
     assert bad
     row['conflicts']=bad;route='held_18_field'
   row['route']=route;rows.append(row)
assert len(rows)==106
assert Counter(r['route']for r in rows)=={'sector':53,'post_gate_endpoint_impossible':32,'held_18_field':21}
R_support=[]
for a in'DCVU':
 p=(0,0,0);rr=[]
 for t,c in enumerate(W[a]):
  if c=='R':
   assert p[1]>=0 and p[0]>=-1
   rr.append(dict(own_tick0=t,local_cell=p[:2]))
  p=after(c,p)
 R_support.append(dict(atom=a,all_actual_R_cells=rr))

PREFIX='UQCDDVCVUUC';STAR={(0,0),(0,1),(1,0),(1,1)};HOOK={(-1,-1),(-2,-1),(-3,-1),(-3,-2)}
controls=[];next_ports=[]
for rail,mass,reads in [('DDVV',58,395),('DDDDU',61,407)]:
 base=PREFIX+rail+'Q';packet=base+'C';raw=''.join(W[a]for a in packet);tr=lit.trace(raw+lit.M);assert tr['feasible']
 seed={q for q,(c,t)in tr['first'].items()if c=='L'};assert len(seed)==mass and len(raw)+11==reads
 before=lit.trace(''.join(W[a]for a in base)+lit.M)
 assert {q for q,(c,t)in before['first'].items()if c=='L'}==seed
 B={q:('initial',q)for q in seed};p=(0,0,0);tick=0;cuts=[];pieces=[]
 h=(0,6);k=(-1,6);r=(-4,7);history={h:[],k:[],r:[]};selected={}
 next_index=len(base)-1;next_start=sum(len(W[a])for a in base[:-1]);next_exit=next_start+len(W['Q'])
 for index,a in enumerate(packet):
  entry=p
  if index==0:
   t=lit.trace(W['U']);selected.update({q:t['last'][q][1]for q in STAR})
  if index==1:
   t=lit.trace(W['Q']);selected.update({add(p[:2],q):tick+t['last'][q][1]for q in HOOK})
  for own,c in enumerate(W[a]):
   q=p[:2];assert(q in B)==(c=='L')
   if q in history:history[q].append(dict(global_tick0=tick,atom_index0=index,atom=a,actual_read=owner.describe(a,own),turn=c,previous_identity=B.get(q)))
   if c=='L':del B[q]
   else:B[q]=tick
   p=after(c,p);tick+=1
  if a in'FQB':
   mid=after(W['F'],entry);pieces.append(dict(atom_index0=index,atom=a,piece='actual_F56_prefix',start=z(entry),end=z(mid)))
   if a!='F':pieces.append(dict(atom_index0=index,atom=a,piece='actual_tail',start=z(mid),end=z(p)))
  else:pieces.append(dict(atom_index0=index,atom=a,piece='ordinary',start=z(entry),end=z(p)))
  K={add(p[:2],lit.rot(q,p[2]))for q in lit.K}
  if index in(1,9,next_index,next_index+1):
   cuts.append(dict(after_atom_index0=index,atom=a,cut_tick0=tick,head=p,hole_h_physically_BLACK=h in B,hole_h_present_R_identity=B.get(h),hole_h_current=h in B and h not in K,side_hole_r_physically_BLACK=r in B,side_hole_r_present_R_identity=B.get(r),selected_old_Ustar_Qhook_SAME_CURRENT=[dict(cell=q,birth=bid,SAME_CURRENT=B.get(q)==bid and q not in K)for q,bid in sorted(selected.items())]))
  if index==next_index:
   assert h not in B and k not in B and B.get(r)==next_start+54
  if index==next_index+1:
   assert B.get(h)==next_exit+7 and h not in K
   assert B.get(k)==next_exit+8 and k not in K
 assert all(B.get(q)==bid for q,bid in selected.items())
 assert [x for x in history[h]if 56<x['global_tick0']<next_exit+7]==[]
 assert [x for x in history[k]if 57<x['global_tick0']<next_exit+8]==[]
 assert [x for x in history[r]if 63<x['global_tick0']<next_start+54]==[]
 assert history[h][-1]['global_tick0']==next_exit+7 and history[h][-1]['actual_read']['owner_tick0']==7
 assert history[r][-1]['global_tick0']==next_start+54
 for marker_tick,c in enumerate(lit.M):
  q=p[:2];assert(q in B)==(c=='L')
  if c=='L':del B[q]
  else:B[q]=tick
  p=after(c,p);tick+=1
 pairs=[]
 for i,a in enumerate(pieces):
  for j in range(i+1,len(pieces)):
   b=pieces[j];hit=meet(a['start'],a['end'],b['start'],b['end'])
   if j==i+1:assert hit==dict(old_s='1',new_lo='0',new_hi='0')
   else:assert hit is None
   pairs.append(dict(earlier_piece=i,later_piece=j,intersection=hit,legal_adjacent_point=j==i+1))
 # Actual C owns the earlier foreign's M11 and really completes, on the
 # SAME full board. A partial D10 inside that M is not a marked D packet.
 for a in'DCVUFQB':
  t=lit.trace(''.join(W[b]for b in base+a)+lit.M)
  row=dict(base=base,next_atom=a,feasible=t['feasible'])
  if a=='C':assert t['feasible']
  else:
   assert not t['feasible'];row['immutable_conflict']=t
   row['actual_owner']=owner.describe(a,t['conflict_read']-next_exit)
  next_ports.append(row)
 controls.append(dict(packet=packet,compact_packet='UQCDDVCVUUC '+rail+' Q C',complete_seed=sorted(seed),seed_mass=len(seed),all_actual_reads=tick,old_source_Q_ENTRY=(0,4,0),paired_U_ENTRY=(3,3,0),next_Q_ENTRY_SOURCE_frame=(-5,8,3),source_hole_h_world=h,source_hole_h_old_last_L_global_tick0=56,source_second_hole_k_world=k,source_second_hole_k_old_last_L_global_tick0=57,side_hole_r_world=r,side_hole_r_old_last_L_global_tick0=63,next_Q_start_global_tick0=next_start,next_Q_RAW_EXIT_global_tick0=next_exit,side_hole_r_new_Q_R54_global_tick0=next_start+54,hole_h_new_actual_C_R7_global_tick0=next_exit+7,hole_k_new_actual_C_R8_global_tick0=next_exit+8,source_hole_read_histories=[dict(cell=q,all_actual_reads=history[q])for q in(h,k,r)],all_relevant_actual_cut_states=cuts,same_seed_base_plus_M_and_complete_following_C=True,complete_next_C_not_fictitious_D_inside_M=True,all_repaired_proxy_pieces=pieces,all_closed_proxy_pair_checks=pairs,finite_OPEN_proxy_simple_through_following_C_RAW=True))
assert len(next_ports)==14 and sum(r['feasible']for r in next_ports)==2
D=['two_foreign_three_C_rewrite_controls_2026-10-24/manifest.json','audits/check_two_foreign_three_C_controls_independent.json','two_foreign_three_C_rewrite_controls_2026-10-24/check_three_C_controls.py','foreign_three_C_NE_reserve_2026-10-24/manifest.json','audits/check_foreign_three_C_NE_reserve_independent.json','foreign_two_C_pair_hole_transfer_2026-10-24/manifest.json','audits/check_foreign_two_C_pair_hole_independent.json','Q_B_hook_three_C_foreign_transfer_2026-10-24/manifest.json','audits/check_QB_three_C_hook_transfer_independent.json','word_stabilization/check_foreign_return_interfaces.py','literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
result=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Any actual source F/Q/B ENTRY0N whose actual N2 paired U(3,-1,N) has completed, then remaining ordinary RAW words through total at most3Cs, then one next complete F/Q/B RAW plus real following M11. The old source L28 hole(0,2) is physically WHITE throughout and entirely UNREAD by that next FOREIGN RAW. NO claim through its future M11. Two actual genuine U-entry controls complete a following C on the same full boards and restore the hole as a NEW CURRENT C output.',
 post_gate_FIELD18_CURRENT=sorted(field),all106_next_FOREIGN_first_R_hole_alignments=rows,all_actual_ordinary_R_supports=R_support,
 hole_before_foreign='Signed158 gives hWHITE after the actual N2 paired rewrite. Later N heads y>=3 and all R offsets have y>=0. C3 has the same N bound. W heads y>=4 and physical R offsets have y>=-1. Thus no remaining ordinary physical R can reach h_y2; actual histories cannot execute L on a WHITE h either. It remains physically WHITE before the next foreign.',
 no_foreign_READ_proof='Any first RAW read of h by the next FOREIGN must be R, since it is WHITE before that RAW. Every possible R-first slot is enumerated, including temporary R-then-L and all CORE writes. Active-sector and exact N or N/C/W endpoint equations plus the genuine18 CURRENT field exclude all106 roles:53sector+32endpoint+21field. A first L is impossible on WHITE. Therefore the next FOREIGN RAW never reads h at all. This proof stops at the actual RAW exit, before any of the next real word executes.',
 all2_genuine_complete_restoration_controls=controls,all14_prescribed_actual_next_G7_ports=next_ports,
 restoration_mechanism='The source L35 side hole is restored by next Q ownR54. The source L28 hole is NOT read by that Q RAW; its real following C ownR7 restores it. The same C ownR8 also restores the adjacent source L29 hole as a genuine CURRENT common output. The actual C completes with its own real M11 on the SAME initial58/61-cell boards, and h is a genuine CURRENT external C output at its RAW exit. Calling the first11 reads an unowned marker or a completed D would erase this ownership distinction. All three repaired cells carry new identities, not resurrected source identities.',
 not_claimed=['No WHITE permanence through actual following M11; the complete following C controls explicitly refute it.','No protected old Ustar/Qhook erosion in these controls; selected originals survive.','No SOURCEF two-tag persistence through the next FOREIGN.','No iteration through further foreigners, arbitrary-tail simplicity, bounded field, language coverage or capture.'],dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in D})
(HERE/'paired_hole_restore.json').write_text(json.dumps(result,indent=2)+'\n')
print('Paired hWHITE: NEXTFORE RAW misses h,106=53sector+32endpoint+21field. Genuine58/61 boards restore sourceL35 at nextQ R54, then sourceL28/L29 at actual followingC R7/R8 externalCURRENT. Same seeds;14 nextports onlyC; direct proxies simple.')
