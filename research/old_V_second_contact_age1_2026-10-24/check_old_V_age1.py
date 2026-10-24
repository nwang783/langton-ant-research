"""Exact old-V true preforeign age1 slice; bounded endpoint equations,
four genuine VC-entry controls, naturally closed fixed-word predecessor trees.
No generic prefix search or postforeign maturity.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from itertools import permutations
import json,hashlib,math,importlib.util
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent;BP=R/'U_star_one_foreign_return_transfer_2026-10-24/check_U_star_corner_transfer.py';n={'__file__':str(BP)};exec(BP.read_text().split('# Exactly twelve constant local suffixes.')[0],n)
W=n['W'];mp=n['mp'];M=n['M'];K=n['K'];rot=n['rot'];at=n['at'];sub=n['sub'];add=n['add'];literal=n['literal'];center=n['center'];meet=n['meet'];cross=lambda a,b:a[0]*b[1]-a[1]*b[0]
CP=R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py';sp=importlib.util.spec_from_file_location('owner',CP);co=importlib.util.module_from_spec(sp);sp.loader.exec_module(co)
AP=R/'second_ordinary_after_first_foreign_2026-10-24/small_second_ordinary_geometry.json';angles=[x for x in json.loads(AP.read_text())['conditional217_old_source_angle_interfaces']if x['old_source']=='V'and x['actual_old_source_to_FOREIGN_C_age']==1];assert len(angles)==16
QMIN=R/'audits/dcuv_count5_replay/queries.json';MIN=json.loads(QMIN.read_text());assert len(MIN['slots'])==23
for k,s in MIN['slots'].items():
 assert s['certified_minimum_C_age']>=2 and s['unexcluded_counts_0_to_4'][:2]==[0,0]
 assert all('OPEN'not in x['reasons_0_through_4'][:2]for x in s['rows'])
# Every genuine completed V/VC output stays CURRENT to the A-entry age1.
SOURCE={}
for src in('V','VC'):
 sd=literal(''.join(W[mp[a]]['word']for a in src));ep=tuple(sd['endpoint'][:2]);eh=sd['endpoint'][2];outs={q for q,v in sd['requirements'].items()if v^(q in sd['parity'])}-{at(q,ep,eh)for q in K};assert len(outs)==(6 if src=='V' else 9)
 assert all(sd['reads'][q][-1][1]=='R'for q in outs);SOURCE[src]=(sd,outs)
# Exact SECOND-pose parallelograms. Old outgoing source owns0<=s<1;
# t0 contacts are forbidden at CUT2 by signed one-return simplicity.
a0=(-1,-1);b0=(1,5);v0=sub(b0,a0);geometries=[];boxes=[];parallel_cut2=[]
for angle in angles:
 b1=angle['first_ordinary'];b2=angle['second_ordinary'];h=angle['second_heading_relative_old_source'];assert h==(0 if b1=='C' else 1)
 rd=literal(W[mp[b2]]['word']);c=center((0,0),h);en=at(tuple(rd['endpoint'][:2]),(0,0),h);d=center(en,(h+rd['endpoint'][2])%4);vv=sub(d,c);den=cross(v0,vv);corn=[tuple(Q(a0[k]+s*v0[k]-c[k]-t*vv[k],2)for k in(0,1))for s in(0,1)for t in(0,1)];bounds=[(math.floor(min(z[k]for z in corn)),math.ceil(max(z[k]for z in corn)))for k in(0,1)]
 boxes.append(dict(first=b1,second=b2,heading=h,corners=[[str(q)for q in z]for z in corn],exhaustive_integer_bounds=bounds))
 for x in range(bounds[0][0],bounds[0][1]+1):
  for y in range(bounds[1][0],bounds[1][1]+1):
   if(x+y+h)%2:continue
   cc=add(c,(2*x,2*y));dd=add(d,(2*x,2*y));z=sub(cc,a0)
   if den:
    s=Q(cross(z,vv),den);t=Q(cross(z,v0),den)
    if not(0<=s<1 and 0<t<=1):continue
    kind='nonparallel'
   else:
    if cross(z,v0):continue
    assert b2=='V'and h==0 and vv==v0
    start=Q(z[0],v0[0]);s=Q(0);t=-start
    if 0<=start<1:parallel_cut2.append(dict(first=b1,second=b2,pose=[x,y,h],old_parameter=str(start)));continue
    if not(0<t<=1):continue
    kind='parallel_first_positive_onset'
   geometries.append(dict(first=b1,second=b2,second_pose=[x,y,h],source_s=str(s),second_t=str(t),kind=kind))
assert len(geometries)==50
# Invert exact A+b1 endpoints, retain full source role V versus VC.
counts=Counter();typed=[];survive=[]
for geo in geometries:
 b1,b2=geo['first'],geo['second'];p2=geo['second_pose'];ha=3
 for A in'FQB':
  disp=literal(W[mp[A]]['word']+W[mp[b1]]['word']);ap=sub(tuple(p2[:2]),rot(tuple(disp['endpoint'][:2]),ha));assert(ha+disp['endpoint'][2])%4==p2[2]
  full=literal(W[mp[A]]['word']+W[mp[b1]]['word']+W[mp[b2]]['word']+M)
  for src in('V','VC'):
   sd,outs=SOURCE[src];row=dict(**geo,FOREIGN=A,FOREIGN_pose=[*ap,ha],true_source_to_FOREIGN_C_age=1,source_full=src)
   if not full['feasible']:why='literal_A_FIRST_SECOND_conflict';row['conflict']=full
   elif outs&{at(q,ap,ha)for q in K}:why='genuine_SOURCE_CURRENT_in_FOREIGN_entryK'
   else:
    whites=[q for q in outs if full['requirements'].get(rot(sub(q,ap),-ha))is False]
    if whites:why='genuine_SOURCE_BLACK_vs_combined_before_WHITE';row['WHITE_source_output_obstructions']=sorted(whites)
    else:
     # Every surviving prior foreign/first chord misses source's actual
     # full V/C-tail path; no true immediate adjacency is discarded.
     pieces=[]
     for aa in n['walk'](A+b1):
      u=at(aa['start'],(2*ap[0],2*ap[1]),ha);v=at(aa['end'],(2*ap[0],2*ap[1]),ha)
      if aa['atom']in'QB':
       bend=at(add((2*aa['entry'][0],2*aa['entry'][1]),rot((-7,-3),aa['entry'][2])),(2*ap[0],2*ap[1]),ha);pieces.extend([(u,bend),(bend,v)])
      else:pieces.append((u,v))
     schords=[(aa['start'],aa['end'])for aa in n['walk'](src)]
     assert not any(meet(u,v,e,f)is not None for u,v in pieces for e,f in schords)
     why='necessary_one_C_endpoint_obligation';survive.append(row)
   row['classification']=why;counts[why]+=1;typed.append(row)
assert len(typed)==300 and len(survive)==54
assert counts==Counter({'genuine_SOURCE_BLACK_vs_combined_before_WHITE':234,'literal_A_FIRST_SECOND_conflict':12,'necessary_one_C_endpoint_obligation':54})
# Solve ALL nonnegative N/W count equations. The endpoint y bound makes
# the count domain finite; this is not a chosen packet-depth horizon.
def perms(d,v,u):return sorted({''.join(s)for s in permutations('D'*d+'V'*v+'U'*u)})
obligations=[];whole=[];positive={}
for z in survive:
 A=z['FOREIGN'];x,y,ha=z['FOREIGN_pose'];src=z['source_full'];allowed='VU'if A in'FQ'else'U';solutions=[];countsol=[]
 if src=='VC':
  drop=y-4;dx=1-x
  for vw in range(max(drop+1,0)):
   dw=drop-vw;rem=dx-dw-3*vw
   if rem<0 or rem%4:continue
   uw=rem//4
   if not any(b in allowed and k for b,k in zip('DVU',(dw,vw,uw))):continue
   words=[s for s in perms(dw,vw,uw)if s[-1]in allowed];solutions.extend(words);countsol.append(dict(N_counts=[0,0,0],W_counts=[dw,vw,uw],one_C_owner='own SOURCE VC tail',all_connectors=words))
 else:
  rem=y-4
  for dn in range(max(rem+1,0)):
   for vn in range(max(rem//3+1,0)):
    for un in range(max(rem//4+1,0)):
     if dn+vn+un==0:continue
     nw=rem-dn-3*vn-4*un
     if nw<0:continue
     for vw in range(nw+1):
      dw=nw-vw;rhs=1+dn+vn-dw-3*vw-x
      if rhs<0 or rhs%4:continue
      uw=rhs//4
      if not any(b in allowed and k for b,k in zip('DVU',(dw,vw,uw))):continue
      words=[r+'C'+s for r in perms(dn,vn,un)for s in perms(dw,vw,uw)if s[-1]in allowed];solutions.extend(words);countsol.append(dict(N_counts=[dn,vn,un],W_counts=[dw,vw,uw],one_C_owner='FIRST tail of last actual N-base DC/VC/UC, not SOURCE V',all_connectors=words))
 obligations.append(dict(source_case=z,all_nonnegative_count_solutions=countsol,all_actual_full_connectors=solutions,connector_count=len(solutions)))
 for run in solutions:
  seq=src+run+A+z['first']+z['second'];raw=''.join(W[mp[a]]['word']for a in seq);d=literal(raw+M);r=dict(source_case=z,connector=run,word=seq,feasible=d['feasible'])
  if d['feasible']:positive[seq]=(z,run,d)
  else:r['immutable_conflict']=d
  whole.append(r)
assert sum(bool(x['all_actual_full_connectors'])for x in obligations)==18 and len(whole)==26 and len(positive)==4
assert set(positive)=={'VCDUFDD','VCVUQDD','VCVUFVD','VCDUUQVD'}
# Exact complete-eight predecessor closure for each actual prepared word.
# The frontier dies naturally after one plain D; no depth cap is used.
G8=('D','DC','V','VC','VCC','U','UC','UCC');back=[];queries=0
for seq in sorted(positive):
 frontier=[('',seq)];nodes=[]
 while frontier:
  prep,word=frontier.pop(0);children=[];qq=[]
  for before in G8:
   d=literal(''.join(W[mp[a]]['word']for a in before+word)+M);queries+=1;qq.append(dict(predecessor=before,feasible=d['feasible'],conflict=d if not d['feasible']else None))
   if d['feasible']:children.append(before);frontier.append((before+prep,before+word))
  nodes.append(dict(prepended_full_prefix=prep,word=word,all8_queries=qq,exact_legal_predecessors=children))
 assert len(nodes)==2 and nodes[0]['exact_legal_predecessors']==['D']and not nodes[1]['exact_legal_predecessors']
 back.append(dict(base_word=seq,nodes=nodes,no_U_family_at_any_naturally_reached_prefix=True))
assert queries==64
# Four whole-board prepared controls: source VC is a REAL producer, but
# its entire prehistory is source-entry-only or a single D, never U-entry.
controls=[]
for seq,(z,run,d)in sorted(positive.items()):
 raw=''.join(W[mp[a]]['word']for a in seq);initial={q for q,v in d['requirements'].items()if v};board=set(initial);labels={q:'initial_'+str(q)for q in initial};p=(0,0);h=0;log=[];snap={};src='VC';srcLen=sum(len(W[mp[a]]['word'])for a in src);preLen=srcLen+sum(len(W[mp[a]]['word'])for a in run);afterA=preLen+len(W[mp[z['FOREIGN']]]['word']);cut2=afterA+len(W[mp[z['first']]]['word']);cut3=cut2+len(W[mp[z['second']]]['word']);sd,outs=SOURCE[src];birth={q:sd['reads'][q][-1][0]for q in outs};original={q:'source_VC_R_'+str(t)for q,t in birth.items()};spans=[];off=0
 # Parse the actual preforeign connector by attaching its unique C to
 # its preceding base; the positive controls here are all zero-C W runs.
 packets=['VC']+list(run)+[z['FOREIGN'],z['first'],z['second']]
 for i,packet in enumerate(packets):le=sum(len(W[mp[a]]['word'])for a in packet);spans.append((off,off+le,packet,i));off+=le
 assert off==len(raw)
 for tick,turn in enumerate(raw+M):
  if tick in(srcLen,preLen,afterA,cut2,cut3):
   kk={at(v,p,h)for v in K};snap[tick]=dict(tick0=tick,head=[*p,h],source_originals=[dict(cell=q,label=labels.get(q),SAME_original_alive=labels.get(q)==original[q],SAME_original_CURRENT=(labels.get(q)==original[q]and q not in kk),SAME_original_CORE=(labels.get(q)==original[q]and q in kk))for q in sorted(outs)])
  actual='L'if p in board else'R';assert actual==turn;old=labels.get(p)
  if actual=='L':board.remove(p);labels.pop(p)
  else:board.add(p);labels[p]=original[p]if p in original and tick==birth[p]else'new_R_'+str(tick)
  own=next(((packet,tick-lo,i)for lo,hi,packet,i in spans if lo<=tick<hi),None);owner=co.describe(own[0],own[1])if own else dict(owner='next actual word M11 prefix',owner_tick0=tick-len(raw),owner_read_number1=tick-len(raw)+1)
  if own:owner['actual_packet_index0']=own[2]
  log.append(dict(tick0=tick,cell=p,turn=turn,old_label=old,new_label=labels.get(p),physical_owner=owner));h=(h+(-1 if turn=='L' else 1))%4;p=add(p,n['VEL'][h])
 assert all(t['SAME_original_CURRENT']for t in snap[preLen]['source_originals'])
 # Old prefix+A+b1 is physically geometrically simple. The second
 # terminal returns to initial old-V start, with outgoing V ownership.
 pieces=[];rawentry=0
 for atom in n['walk'](seq):
  if atom['atom']in'QB':cut=add((2*atom['entry'][0],2*atom['entry'][1]),rot((-7,-3),atom['entry'][2]));pieces.extend([(atom['start'],cut),(cut,atom['end'])])
  else:pieces.append((atom['start'],atom['end']))
 bad=[]
 for i,(u,v)in enumerate(pieces):
  for k in range(i+2,len(pieces)):
   hit=meet(u,v,*pieces[k])
   if hit is not None:bad.append((i,k,hit))
 assert len(bad)==1 and bad[0][0]==0 and bad[0][1]==len(pieces)-1 and bad[0][2]==(Q(0),Q(1))
 controls.append(dict(word=seq,actual_packets=packets,complete_initial_BLACK_board=sorted(initial),mass=len(initial),all_other_cells_WHITE=True,all_actual_fine_reads=log,cut_snapshots=list(snap.values()),source_VC_output_births=[dict(cell=q,last_R_tick0=t)for q,t in sorted(birth.items())],original_source_outputs_all_current_at_foreign_entry=True,old_plus_foreign_plus_first_proxy_simple=True,second_FIRST_newcontact=dict(old_source='outgoing initial V base',old_source_parameter='0',second_parameter='1',point=[-1,-1]),all_nonadjacent_contacts=[dict(old_piece=i,new_piece=k,contact=[str(t)for t in hit])for i,k,hit in bad],scope='Actual finite prepared board with genuine VC producer. Not U-entry: exact complete-eight reverse closure has only D then no predecessor. No capture or periodicity claim.'))
D=[BP,CP,AP,R/'second_ordinary_after_first_foreign_2026-10-24/small_second_ordinary_geometry_manifest.json',QMIN,R/'seven_word_spatial_return_2026-10-23/first_foreign_first_returned_atom_simplicity_manifest.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='Old outgoing V-base chronological FIRST SECOND-ordinary contact, true source-entry-to-firstFOREIGN age1, excluded for U-entry complete8 history. VCC cannot complete byage1; actual source V/VC roles retained. Four genuine preparedVC controls remain as regressions but have finite reverseclosure noU.',angle_interfaces16=angles,exact16_head_parallelograms=boxes,parallel_CUT2_already_old_rejections=parallel_cut2,all50_b1_typed_SECOND_geometries=geometries,all300_fullsource_foreign_typed_states=typed,classification_counts=dict(counts),all54_unbounded_one_C_endpoint_obligations=obligations,all26_endpoint_exhaustive_whole_words=whole,all64_reverse_queries_in_four_naturally_closed_trees=back,four_genuine_VC_entry_physical_controls=controls,one_C_count_equations=dict(sourceVC='xA=1-dW-3vW-4uW; yA=4+dW+vW',sourceV='xA=1+dN+vN-dW-3vW-4uW; yA=4+dN+3vN+4uN+dW+vW; dN+vN+uN>=1',full_C_owner='SourceVC owns C1 itself. SourceV must have the actual last N-base DC/VC/UC with its FIRST C tail; no standaloneC or doubletail atage1.',allowed_last_W='V/U before F/Q, U before B; follows signed actual adjacency, forbids endingC/D',finiteness='yA-4 bounds every nonnegative count exceptuW; x-equation determinesuW exactly. No arbitrary packet cap.'),produced_age_note='All23 genuine produced-input slots have minimum>=2; only used beforeFOREIGN age1 to hold SOURCE full outputs current. No postforeign maturation.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'old_V_age1.json').write_text(json.dumps(o,indent=2)+'\n');print('OldV trueFOREIGNage1:300→54→26wholewords→4preparedVCcontrols→64-query natural reverseclosure noU. No U-entry SECOND contact in this slice.')
