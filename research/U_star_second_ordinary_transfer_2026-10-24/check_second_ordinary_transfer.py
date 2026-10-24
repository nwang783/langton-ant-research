"""Exactly TWO ordinary RAW atoms after one foreign: no tail iteration."""
from pathlib import Path
import hashlib,json
from collections import Counter
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
BP=R/'U_star_one_foreign_return_transfer_2026-10-24';P=BP/'check_U_star_corner_transfer.py';BJ=BP/'U_star_corner_transfer.json';BM=BP/'manifest.json'
# Import only definitions; never rerun or edit the frozen parent artifact.
ns={'__file__':str(P)};exec(P.read_text().split('# Exactly twelve constant local suffixes.')[0],ns)
W=ns['W'];mp=ns['mp'];literal=ns['literal'];M=ns['M'];at=ns['at'];rot=ns['rot'];sub=ns['sub'];K=ns['K'];L=ns['L'];PORTS=ns['FOURPORTS'];meet=ns['meet'];center=ns['center'];add=ns['add'];VEL=ns['VEL']
j=json.loads(BJ.read_text());assert len(j['all262_necessary_three_corner_states'])==262
rows=[];counts=Counter();by_atom=Counter();loss=Counter();bottom=[];universe=set();local={}
base_states={(z['foreign'],z['first_returned_raw_atom'],*z['foreign_entry_in_creator_U_frame']):z for z in j['all262_necessary_three_corner_states']}
# Include ALL newly touched CUT2-four-current poses, not just the 262
# previously nontrivial transfer states. Exactly 48 fixed local footprints.
for a in 'FQB':
 for b1 in 'DCVU':
  for b2 in 'DCVU':
   raw=''.join(W[mp[z]]['word']for z in(a,b1,b2));rd=literal(raw);full=literal(raw+M);local[a,b1,b2]=raw,rd,full
   if not full['feasible']:continue
   for slot,v in full['requirements'].items():
    if v:
     for tag in L:
      for h in range(4):universe.add((a,b1,b2,*sub(tag,rot(slot,h)),h))
for a,b1,b2,x,y,h in sorted(universe):
 p=(x,y);raw,rd,full=local[a,b1,b2];row=dict(foreign=a,first_ordinary=b1,SECOND_ordinary=b2,foreign_pose=[x,y,h],necessary_only=True,genuine_U_ancestry_certified=False)
 if (x+y+h)%2:why='wrong_active_sector'
 elif L&{at(q,p,h)for q in K}:why='original_CURRENT_inside_FOREIGN_entryK'
 elif any(full['requirements'].get(rot(sub(q,p),-h))is False for q in L):why='original_BLACK_vs_combined_before_WHITE'
 else:
  # Nontrivial aligned states cannot be true U->A adjacency. That one
  # literal pose misses all four original tags through this two-atom cut.
  assert (p,h)!=((0,4),0)
  pieces=[]
  for atom in ns['walk'](a+b1):
   z0=at(atom['start'],(2*x,2*y),h);z1=at(atom['end'],(2*x,2*y),h)
   if atom['atom']in'QB':
    zc=at(add((2*atom['entry'][0],2*atom['entry'][1]),rot((-7,-3),atom['entry'][2])),(2*x,2*y),h);pieces.extend([(z0,zc),(zc,z1)])
   else:pieces.append((z0,z1))
  contacts=[meet((-1,-1),(-1,7),u,v)for u,v in pieces]
  if any(z is not None for z in contacts):why='old_U_chord_contact_through_FIRST_return'
  else:
   cut2=literal(''.join(W[mp[z]]['word']for z in(a,b1)));end2=at(tuple(cut2['endpoint'][:2]),p,h);h2=(h+cut2['endpoint'][2])%4;k2={at(q,end2,h2)for q in K};keep2={q for q in L if rot(sub(q,p),-h)not in cut2['reads']and q not in k2}
   if len(keep2)<4:
    base=base_states[a,b1,x,y,h];assert keep2=={tuple(q)for q in base['same_original_CURRENT_cells']}
   else:base=None
   end=at(tuple(rd['endpoint'][:2]),p,h);eh=(h+rd['endpoint'][2])%4;k3={at(q,end,eh)for q in K};keep={q for q in L if rot(sub(q,p),-h)not in rd['reads']and q not in k3};alive={q for q in L if rot(sub(q,p),-h)not in rd['reads']};ports=[name for name,pair in PORTS.items()if pair<=keep]
   assert len(keep)>=2 and ports
   assert all(rot(sub(q,p),-h)not in full['requirements']for q in keep)
   why='compatible_necessary_four_corner_state';row.update(inherited_CUT2_current_originals=sorted(keep2),CUT2_was_all4_current=(base is None),THIRD_atom_entry=[*end,eh],physical_cut_tick0=len(raw),last_executed_tick0=len(raw)-1,future_M11_NOT_executed=[len(raw),len(raw)+10],same_original_CURRENT_cells=sorted(keep),same_original_physically_alive_cells=sorted(alive),same_original_alive_CORE_cells=sorted(alive-keep),four_corner_ports=ports)
   loss[b2,len(keep),len(alive),len(keep2)]+=1;by_atom[b2,tuple(ports)]+=1
   if ports==['BOTTOM']:bottom.append(row)
 row['reason']=why;counts[why]+=1;rows.append(row)
assert len(rows)==9912
assert counts==Counter({'wrong_active_sector':4884,'original_CURRENT_inside_FOREIGN_entryK':1080,'original_BLACK_vs_combined_before_WHITE':2628,'old_U_chord_contact_through_FIRST_return':227,'compatible_necessary_four_corner_state':1093})
assert len(bottom)==12
compatible=[z for z in rows if z['reason']=='compatible_necessary_four_corner_state'];new=[z for z in compatible if z['CUT2_was_all4_current']];assert len(new)==119
# A single prepared boundary test: F,D,U gives BOTTOM only after SECOND RAW.
# It satisfies the local first-return/old-U chord disjointness, but initial
# labels are NOT a creating-U genealogy and no preforeign path is supplied.
a,b1,b2='FDU';p=(4,-3);h=1;raw=''.join(W[mp[z]]['word']for z in(a,b1,b2));full=literal(raw+M);assert full['feasible']
initial={at(q,p,h)for q,v in full['requirements'].items()if v}|L
board=set(initial);labels={q:('initial_L_'+str(q)if q in L else'initial_other_'+str(q))for q in board};orig={q:labels[q]for q in L};pos=p;hd=h;log=[];cuts={};off=0;spans=[]
for z in(a,b1,b2):spans.append((off,off+len(W[mp[z]]['word']),z));off+=len(W[mp[z]]['word'])
T2=len(W[mp[a]]['word'])+len(W[mp[b1]]['word']);T3=len(raw)
for tick,ch in enumerate(raw+M):
 if tick in(T2,T3):
  kk={at(q,pos,hd)for q in K};cuts[tick]=dict(tick0=tick,head=[*pos,hd],original_statuses=[dict(cell=q,physical_label=labels.get(q),same_original_physically_alive=labels.get(q)==orig[q],same_original_CURRENT=(labels.get(q)==orig[q]and q not in kk),same_original_CORE=(labels.get(q)==orig[q]and q in kk))for q in sorted(L)])
 turn='L'if pos in board else'R';assert turn==ch;old=labels.get(pos)
 if turn=='L':board.remove(pos);labels.pop(pos)
 else:board.add(pos);labels[pos]='new_R_tick'+str(tick)
 own=next((dict(symbol=z,word_tick0=tick-lo,word_read_number1=tick-lo+1)for lo,hi,z in spans if lo<=tick<hi),dict(symbol='future_M11_after_SECOND',stream_tick0=tick-T3,stream_read_number1=tick-T3+1))
 log.append(dict(tick0=tick,cell=pos,turn=turn,old_label=old,new_label=labels.get(pos),owner=own,executed_at_THIRD_entry=tick<T3));hd=(hd+(-1 if turn=='L'else 1))%4;pos=add(pos,VEL[hd])
keep={tuple(z['cell'])for z in cuts[T3]['original_statuses']if z['same_original_CURRENT']};assert keep==PORTS['BOTTOM']
# The actual SECOND U strictly contacts the hypothetical old-U chord. This
# is not excluded by the signed first-return simplicity theorem.
atoms=ns['walk']('FDU');pieces=[]
for atom in atoms:
 s=at(atom['start'],(2*p[0],2*p[1]),h);t=at(atom['end'],(2*p[0],2*p[1]),h);pieces.append(dict(atom=atom['atom'],start=s,end=t,old_U_chord_contact=meet((-1,-1),(-1,7),s,t)))
assert pieces[0]['old_U_chord_contact']is None and pieces[1]['old_U_chord_contact']is None and pieces[2]['old_U_chord_contact']==(__import__('fractions').Fraction(1,2),__import__('fractions').Fraction(1,2))
def conv(z):
 if isinstance(z,__import__('fractions').Fraction):return str(z)
 raise TypeError(type(z))
control=dict(word='F,D,U plus actual next M11',initial_head=[*p,h],complete_initial_BLACK_board=sorted(initial),mass=len(initial),all_unlisted_cells_WHITE=True,initial_original_labels_are_prepared_NOT_creating_U_R_births=True,preforeign_U_entry_history_certified=False,CUT2=cuts[T2],CUT3=cuts[T3],all_actual_fine_reads=log,hypothetical_old_U_chord_geometry=pieces,missing_ancestry='No actual creating-U packet or intervening complete-eight prefix is supplied. The labels are initial prepared labels. The SECOND chord crosses the hypothetical old-U chord; signed simplicity covers only through FIRST ordinary RAW, not this second chord.')
# Longer, structurally chosen continuation of the FDU BOTTOM boundary.
# UCC turns W->S->E; V then reaches D(-1,0,E), whose true input is old(0,0).
# The next completed D supplies the actual tick1/read2 physical deletion.
CP=R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py'
import importlib.util
spec=importlib.util.spec_from_file_location('canonical_owner',CP);co=importlib.util.module_from_spec(spec);spec.loader.exec_module(co)
packets=('F','D','UCC','V','D','D');seq=''.join(packets);longraw=''.join(W[mp[z]]['word']for z in seq);ld=literal(longraw+M);assert ld['feasible']
longinitial={at(q,p,h)for q,v in ld['requirements'].items()if v}|L
assert len(longinitial)==29 and all(ld['requirements'].get(rot(sub(q,p),-h))is not False for q in L)
board=set(longinitial);labels={q:('initial_L_'+str(q)if q in L else'initial_other_'+str(q))for q in board};orig={q:labels[q]for q in L};pos=p;hd=h;llog=[];lcut={};bound={0};spans=[];off=0
for i,packet in enumerate(packets):
 le=sum(len(W[mp[z]]['word'])for z in packet);spans.append((off,off+le,packet,i));off+=le;bound.add(off)
bound|={T2,T3}
for tick,ch in enumerate(longraw+M):
 if tick in bound:
  kk={at(q,pos,hd)for q in K};lcut[tick]=dict(tick0=tick,head=[*pos,hd],old_star=[dict(cell=q,label=labels.get(q),original_physically_alive=labels.get(q)==orig[q],original_CURRENT=(labels.get(q)==orig[q]and q not in kk),original_CORE=(labels.get(q)==orig[q]and q in kk))for q in sorted(L)])
 turn='L'if pos in board else'R';assert turn==ch;old=labels.get(pos)
 if turn=='L':board.remove(pos);labels.pop(pos)
 else:board.add(pos);labels[pos]='new_R_tick'+str(tick)
 packetowner=next(((packet,tick-lo,i)for lo,hi,packet,i in spans if lo<=tick<hi),None)
 owner=co.describe(packetowner[0],packetowner[1])if packetowner else dict(owner='next actual word M11 prefix, not an extra marker word',owner_tick0=tick-len(longraw),owner_read_number1=tick-len(longraw)+1)
 if packetowner:owner['actual_packet_index0']=packetowner[2]
 llog.append(dict(tick0=tick,read_number1=tick+1,cell=pos,turn=turn,old_label=old,new_label=labels.get(pos),physical_owner=owner));hd=(hd+(-1 if turn=='L'else 1))%4;pos=add(pos,VEL[hd])
assert {tuple(z['cell'])for z in lcut[94]['old_star']if z['original_CURRENT']}==PORTS['BOTTOM']
assert {tuple(z['cell'])for z in lcut[152]['old_star']if z['original_CURRENT']}=={(1,0)}
assert next(z for z in lcut[152]['old_star']if z['cell']==(0,0))['original_CORE']
assert llog[153]['cell']==(0,0)and llog[153]['turn']=='L'and llog[153]['old_label']==orig[0,0]
assert llog[153]['physical_owner']['owner_tick0']==1 and llog[153]['physical_owner']['owner_read_number1']==2
assert {tuple(z['cell'])for z in lcut[162]['old_star']if z['original_physically_alive']}=={(1,0)}
longcontrol=dict(actual_complete_packets=packets,actual_next_M11=M,initial_head=[*p,h],complete_initial_BLACK_board=sorted(longinitial),mass=len(longinitial),all_other_cells_WHITE=True,all_fine_reads=llog,physical_boundary_snapshots=list(lcut.values()),original_losses=[dict(cell=q,first_actual_L_tick0=next((z['tick0']for z in llog if z['old_label']==orig[q]and z['turn']=='L'),None))for q in sorted(L)],identity_convention='Four initial prepared labels, NOT genuine source-U R births. Replacements have new_R_tick labels.',exact_loss='BOTTOM pair current at tick94. At tick152 original(0,0) is physically alive CORE, only(1,0) CURRENT; physical deletion is next actual D tick1/read2 at153. At162 only original(1,0) survives physically/current.',missing_ancestry='No creating-U packet or old complete-eight prefix is supplied. Its second U chord already crosses the hypothetical old-U chord at strict midpoints. This is not a counterexample under global no-contact/genuine-U-history premises.',refutes='Iterating the corner/current-color abstraction alone as an unconditional two-original invariant through ordinary tails.',structural_connector='From second-U exit(-3,2,W), own CC ends(-4,1,E); V reaches(-1,0,E), D reaches(0,-1,E), and next D read2 consumes the preceding D input old(0,0).')
local48=[dict(foreign=k[0],first=k[1],second=k[2],literal_RAW_plus_M11_feasible=v[2]['feasible'],conflict=v[2]if not v[2]['feasible']else None)for k,v in sorted(local.items())]
out=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='At actual THIRD ordinary RAW entry after exactly one FIRST foreign and TWO ordinary RAW atoms, every genuine earlier U-star retains at least two SAME original CURRENT IDs forming one of FOUR adjacent corners. This finite two-step statement is NOT a closed arbitrary-tail invariant.',physical_cut='after FOREIGN RAW + FIRST RAW + SECOND RAW, before THIRD RAW read0; future M11 compatibility has not been executed',all48_fixed_local_suffix_feasibilities=local48,all9912_aligned_states=rows,classification=dict(counts),all119_newly_touched_CUT2_all4_current_states=new,CURRENT_and_physical_alive_counts=[dict(second=k[0],current=k[1],physically_alive=k[2],CUT2_current=k[3],count=v)for k,v in sorted(loss.items())],all12_BOTTOM_only_necessary_states=bottom,prepared_BOTTOM_boundary_control=control,actual_29_cell_prepared_tail_erosion_control=longcontrol,continuation_state_requirements=dict(original_tags='Each of four source-R IDs must have its alive/retired and CURRENT/CORE status, plus current fine birth if replaced.',relative_pose='Actual head and heading relative to original star, not just corner name.',ordinary_ownership='Current full-word/atomic tail index and actual boundary/next-marker obligations.',outside_return_interface='Any future extension must specify actual entry core and every first-read requirement on previously constrained cells. On newly read cells retain the chosen initial color, and update physical color/parity at each read. This constrained-cell archive grows with visited footprint; no uniform finite bound is proved.',geometric_interface='Barrier use needs the claimed original member to MISS the actual continuation context; second-contact simplicity has NOT been assumed. The prepared erosion control already has the hypothetical old-U contact; it does not settle a no-contact erosion implication.',not_closed='Corner name alone omits pose, colors, rewritten core ports and unbounded outside read constraints. No tail iteration is licensed.'),dependencies={str(z.relative_to(R)):hashlib.sha256(z.read_bytes()).hexdigest()for z in(P,BJ,BM,CP,Path(__file__).resolve())})
(H/'second_ordinary_transfer.json').write_text(json.dumps(out,indent=2,default=conv)+'\n')
print('9912 aligned states / 1093 compatible,119 newly touched defaults; adjacent original pair at THIRD entry. Actual29-cell tail later leaves1 original; no arbitrary-tail closure.')
