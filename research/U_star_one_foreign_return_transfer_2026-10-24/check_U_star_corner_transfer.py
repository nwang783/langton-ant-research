"""Same-original U-star corner transfer at SECOND ordinary RAW entry.
Future M11 is a compatibility constraint, NEVER executed before the cut.
CORE capture is ordered loss; physically unread old labels are still alive.
"""
from pathlib import Path
from fractions import Fraction
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';QP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
G=json.loads(GP.read_text())['geometry'];W=json.loads(QP.read_text())['macro_words'];M='LLLLRLRRRRL';VEL=((0,1),(1,0),(0,-1),(-1,0));ids=(0,1,4,5,6,7,8,9);mp={a:i for i,a in enumerate('DCVUFQB')}
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def at(q,p,h):return add(p,rot(q,h))
def center(p,h):return add((2*p[0],2*p[1]),rot((-1,-1),h))
def literal(word):
 p=(0,0);h=0;par=set();rq={};rd={};first={}
 for t,ch in enumerate(word):
  b=(ch=='L')^(p in par)
  if p in rq and rq[p]!=b:return dict(feasible=False,tick=t,cell=p,first_read=first[p],required_initial=b,original_initial=rq[p])
  if p not in rq:rq[p]=b;first[p]=[t,ch]
  rd.setdefault(p,[]).append([t,ch]);par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEL[h])
 return dict(feasible=True,requirements=rq,reads=rd,parity=par,endpoint=[*p,h])
def physical(word,initial):
 board=set(initial);p=(0,0);h=0;log=[]
 for t,expected in enumerate(word):
  b=p in board;turn='L'if b else'R';assert turn==expected;log.append(dict(tick=t,cell=p,black_before=b,turn=turn,heading_before=h));board.symmetric_difference_update({p});h=(h+(-1 if turn=='L'else 1))%4;p=add(p,VEL[h])
 return board,log,[*p,h]
def walk(ns):
 p=(0,0);h=0;t=0;atoms=[]
 for n in ns:
  a=literal(W[mp[n]]['word']);ep=tuple(a['endpoint'][:2]);dh=a['endpoint'][2];atoms.append(dict(atom=n,entry=[*p,h],tick=t,start=center(p,h),end=center(at(ep,p,h),(h+dh)%4)));p=at(ep,p,h);h=(h+dh)%4;t+=len(W[mp[n]]['word'])
 return atoms
# Exact rational point contacts; all checked pairs are noncollinear here.
def meet(a,b,c,d):
 u=sub(b,a);v=sub(d,c);w=sub(c,a);cross=lambda q,r:q[0]*r[1]-q[1]*r[0];den=cross(u,v)
 if den:
  s=Fraction(cross(w,v),den);t=Fraction(cross(w,u),den)
  return(s,t)if 0<=s<=1 and 0<=t<=1 else None
 # collinear overlap test via dominant coordinate, preserving point overlaps.
 if cross(w,u):return None
 k=0 if u[0]else 1
 if not u[k]:return None
 x,y=sorted((Fraction(c[k]-a[k],u[k]),Fraction(d[k]-a[k],u[k])));lo=max(0,x);hi=min(1,y)
 if lo>hi:return None
 if lo<hi:return('overlap',lo,hi)
 q=add(a,(u[0]*lo,u[1]*lo));kk=0 if v[0]else 1;t=Fraction(q[kk]-c[kk],v[kk]);return(lo,t)

from collections import Counter
from math import floor,ceil
K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};L={(0,0),(0,1),(1,0),(1,1)}
PORTS={'LEFT':{(0,0),(0,1)},'TOP':{(0,1),(1,1)},'RIGHT':{(1,0),(1,1)}}
FOURPORTS={**PORTS,'BOTTOM':{(0,0),(1,0)}}
oldU=literal(W[3]['word']);birth={q:oldU['reads'][q][-1][0]for q in L};assert birth=={(0,0):4,(0,1):19,(1,0):9,(1,1):18}
for q,t in birth.items():assert oldU['reads'][q][-1]==[t,'R']
for b in'DCVU':
 firstsix={p for p,rr in literal(W[mp[b]]['word'])['reads'].items()if any(t<6 for t,_ in rr)};assert firstsix==K

def owner(t,a,b):
 na=len(W[mp[a]]['word']);nb=len(W[mp[b]]['word'])
 if t<na:return dict(stage='FOREIGN executed RAW',symbol=a,word_tick0=t,word_read_number1=t+1,executed_at_cut=True)
 if t<na+nb:return dict(stage='FIRST ordinary executed RAW',symbol=b,word_tick0=t-na,word_read_number1=t-na+1,executed_at_cut=True)
 return dict(stage='future physical M11 stream; NOT executed at cut',symbol=None,stream_tick0=t-na-nb,stream_read_number1=t-na-nb+1,executed_at_cut=False)

def statuses(a,b,p,h,rawdata,fulldata,en,eh):
 rd=rawdata['reads'];k2={at(q,en,eh)for q in K};out=[]
 for q in sorted(L):
  z=rot(sub(q,p),-h);rr=rd.get(z,[]);future=[(t,ch)for t,ch in fulldata['reads'].get(z,[])if t>=len(W[mp[a]]['word'])+len(W[mp[b]]['word'])]
  alive=not rr;current=alive and q not in k2;core_alive=alive and q in k2
  if rr:assert rr[0][1]=='L'
  if current:assert z not in fulldata['requirements'] and not future
  if core_alive:
   assert future and future[0][1]=='L';ft=owner(future[0][0],a,b);assert ft['stream_tick0']<=5
  replacement=None
  if rr and rr[-1][1]=='R':replacement=dict(last_R=owner(rr[-1][0],a,b),is_original=False,physical_state='CORE'if q in k2 else'residual')
  out.append(dict(cell=q,original_genuine_source_birth=dict(source='same actual creating U-base instance',U_RAW_tick0=birth[q],U_RAW_read_number1=birth[q]+1,turn='R'),executed_RAW_reads=[dict(combined_tick0=t,turn=ch,owner=owner(t,a,b))for t,ch in rr],original_physically_alive_at_cut=alive,original_ordered_CURRENT_at_cut=current,original_alive_but_CORE_at_cut=core_alive,original_physical_retirement=owner(rr[0][0],a,b)if rr else None,replacement_BLACK_at_cut=replacement,physical_color_at_cut='BLACK'if not rr or rr[-1][1]=='R'else'WHITE',future_M11_reads_NOT_executed=[dict(combined_tick0=t,turn=ch,owner=owner(t,a,b))for t,ch in future]))
 return out

# Exactly twelve constant local suffixes. M11 is constraints at later times,
# while rawdata stops strictly BEFORE the SECOND atom's first RAW read.
local={};universe=set()
for a in'FQB':
 for b in'DCVU':
  raw=W[mp[a]]['word']+W[mp[b]]['word'];full=literal(raw+M);r=literal(raw);assert full['feasible']and r['feasible']
  local[a,b]=(raw,r,full)
  for slot,black in full['requirements'].items():
   if black:
    for tag in L:
     for h in range(4):
      p=sub(tag,rot(slot,h));universe.add((a,b,*p,h))
rows=[];survivors=[];foreign_miss_states=[];counts=Counter();local_counts=Counter();losssets=Counter();original_loss_counts=Counter();bottom_removed=[]
for a,b,x,y,h in sorted(universe):
 p=(x,y);raw,r,full=local[a,b];T=len(raw);ae=literal(W[mp[a]]['word'])['endpoint'];fp=at(tuple(ae[:2]),p,h);fh=(h+ae[2])%4;en=at(tuple(r['endpoint'][:2]),p,h);eh=(h+r['endpoint'][2])%4
 if(sum(p)+h)%2:why='wrong_active_sector'
 elif L&{at(q,p,h)for q in K}:why='old_CURRENT_star_inside_FOREIGN_entryK'
 elif any(full['requirements'].get(rot(sub(q,p),-h))is False for q in L):why='old_BLACK_original_requires_before_WHITE'
 else:
  ss=statuses(a,b,p,h,r,full,en,eh);keep={tuple(z['cell'])for z in ss if z['original_ordered_CURRENT_at_cut']};lost=L-keep
  assert lost and len(lost)<=2 and any(q<=keep for q in FOURPORTS.values())
  local_counts[tuple(sorted(lost))]+=1
  cut=add((2*x,2*y),rot((-7,-3),h));fpieces=[(center(p,h),cut)]+([(cut,center(fp,fh))]if a!='F'else[])
  rpiece=(center(fp,fh),center(en,eh))
  fcontact=[(i,meet((-1,-1),(-1,7),u,v))for i,(u,v)in enumerate(fpieces)if meet((-1,-1),(-1,7),u,v)is not None]
  rcontact=meet((-1,-1),(-1,7),*rpiece)
  # A star-hit/capture case cannot be the true immediate U->FOREIGN join;
  # its fixed local footprints miss every original star cell.
  assert (p,h)!=((0,4),0)
  if fcontact:why='actual_foreign_proxy_meets_old_U_chord_nonadjacently'
  elif rcontact is not None:why='actual_first_return_chord_meets_old_U_chord_nonadjacently'
  else:
   why='necessary_only_three_corner_transfer_state';ports=[name for name,q in PORTS.items()if q<=keep];assert ports
   losssets[tuple(sorted(lost))]+=1;original_loss_counts[sum(bool(z['executed_RAW_reads'])for z in ss),sum(z['original_alive_but_CORE_at_cut']for z in ss)]+=1
   data=dict(foreign=a,first_returned_raw_atom=b,foreign_entry_in_creator_U_frame=[x,y,h],physical_cut=dict(SECOND_atom_entry_tick0=T,last_executed_tick0=T-1,FOREIGN_RAW_length=len(W[mp[a]]['word']),FIRST_return_RAW_length=len(W[mp[b]]['word']),future_M11_ticks_NOT_executed=[T,T+10]),FOREIGN_exit_next_entry=[*fp,fh],SECOND_atom_entry=[*en,eh],SECOND_entryK=sorted({at(q,en,eh)for q in K}),same_original_star_statuses=ss,same_original_CURRENT_cells=sorted(keep),available_corner_ports=ports,chosen_corner_port=ports[0],necessary_only=True,genuine_creating_U_ancestry_attained=False)
   foreign_ctx=literal(W[mp[a]]['word']+M)['requirements']
   foreign_miss=all(rot(sub(q,p),-h)not in foreign_ctx for q in L)
   data['FOREIGN_complete_context_MISSES_original_star']=foreign_miss
   if foreign_miss:
    assert all(z['original_physically_alive_at_cut']for z in ss)
    assert PORTS['LEFT']<=keep and len(lost)<=1 and lost<={(1,0),(1,1)}
    foreign_miss_states.append(dict(foreign=a,first_return=b,pose=[x,y,h],alive_CORE_originals=sorted(lost),all4_originals_physically_unread=True,fixed_SAME_current_LEFT_pair=sorted(PORTS['LEFT'])))
   survivors.append(data)
  if lost=={(0,1),(1,1)}:
   assert why!='necessary_only_three_corner_transfer_state';bottom_removed.append(dict(foreign=a,first_return=b,pose=[x,y,h],only_four_port_survivor='BOTTOM',rejection=why))
 counts[why]+=1;rows.append(dict(foreign=a,first_return=b,pose=[x,y,h],reason=why))
assert len(universe)==2396 and len(survivors)==262 and sum(local_counts.values())==324 and len(bottom_removed)==15
assert original_loss_counts==Counter({(1,0):205,(2,0):39,(0,1):18})
assert len(foreign_miss_states)==18
# Literal atomic I/O gives the SECOND step capacity, including marker-only K
# capture. A current outside-entryK BLACK can only be an I or a complete MISS.
second=[];edgechecks=[]
def edge(q):
 x,y=q;return((2*x-1,2*y-1),(2*x+1,2*y+1))if(x+y)%2==0 else((2*x-1,2*y+1),(2*x+1,2*y-1))
for b in'DCVU':
 q=literal(W[mp[b]]['word']+M);inputs={c for c,v in q['requirements'].items()if v}-K;ep=literal(W[mp[b]]['word'])['endpoint'];s=(-1,-1);t=center(tuple(ep[:2]),ep[2]);contact=[]
 for x in range(floor((min(s[0],t[0])-1)/2),ceil((max(s[0],t[0])+1)/2)+1):
  for y in range(floor((min(s[1],t[1])-1)/2),ceil((max(s[1],t[1])+1)/2)+1):
   a,c=edge((x,y))
   if meet(s,t,a,c)is not None:assert(x,y)in q['requirements'];contact.append([x,y])
 adj=[]
 for x in sorted(inputs):
  for y in sorted(inputs):
   if x<y and sum(abs(x[i]-y[i])for i in(0,1))==1:adj.append([x,y])
 if b=='C':assert inputs==set();keep_min=2
 elif b=='D':assert inputs=={(0,1)};keep_min=1
 elif b=='V':assert inputs=={(0,3),(1,2)}and not adj;keep_min=1
 else:assert adj==[[(-1,1),(-1,2)],[(-1,2),(0,2)],[(0,2),(0,3)]];keep_min=0
 second.append(dict(SECOND_actual_atom=b,true_atomic_inputs_including_future_marker_only=sorted(inputs),minimum_SAME_original_corner_IDs_CURRENT_after_SECOND=keep_min,only_possible_two_ID_U_loss_roles=adj if b=='U'else[],no_maturity_used=True,barrier_through_SECOND='each guaranteed surviving member is a complete-context MISS, so its edge avoids the whole chord; which member is not fixed for D/V'))
 edgechecks.append(dict(atom=b,exact_ordinary_proxy_contacted_edge_cells=contact,all_are_in_own_RAW_plus_actual_next_M11_context=True))
# Prepared physical controls: NOT genuine creating-U ancestry. Initial labels
# are explicit I(cell), not fabricated R-born U labels. Physical cut is saved
# BEFORE replaying SECOND, and future M11 reads are separated in the output.
prepared=[]
for name,ns,p,h,port in(('two_physical_erasures','BCC',(-2,-1),1,'RIGHT'),('alive_CORE_capture','BDC',(-2,-6),2,'LEFT'),('local_four_port_countercontrol','BCC',(-1,3),2,'BOTTOM')):
 raw=''.join(W[mp[a]]['word']for a in ns);full=literal(raw+M);assert full['feasible'];assert all(full['requirements'].get(rot(sub(q,p),-h))is not False for q in L)
 initial={at(q,p,h)for q,v in full['requirements'].items()if v}|L;board=set(initial);labels={q:('initial_old_L_'+str(q)if q in L else'initial_other_'+str(q))for q in board};original={q:labels[q]for q in L};pos=p;hd=h;T=len(W[mp[ns[0]]]['word'])+len(W[mp[ns[1]]]['word']);cutdata=None;after_second=None;logs=[]
 spans=[];off=0
 for i,a in enumerate(ns):spans.append((off,off+len(W[mp[a]]['word']),i,a));off+=len(W[mp[a]]['word'])
 for tick,ch in enumerate(raw+M):
  if tick in(T,len(raw)):
   Kcut={at(q,pos,hd)for q in K};data=dict(tick0=tick,head=[*pos,hd],K=sorted(Kcut),star=[dict(cell=q,color='BLACK'if q in board else'WHITE',physical_label=labels.get(q),same_original_physically_alive=labels.get(q)==original[q],same_original_CURRENT=(labels.get(q)==original[q]and q not in Kcut),same_original_CORE=(labels.get(q)==original[q]and q in Kcut))for q in sorted(L)])
   if tick==T:cutdata=data
   else:after_second=data
  turn='L'if pos in board else'R';assert turn==ch
  own=next((dict(stage=('FOREIGN','FIRSTordinary','SECONDordinary')[i],symbol=a,word_tick0=tick-lo,word_read_number1=tick-lo+1)for lo,hi,i,a in spans if lo<=tick<hi),dict(stage='future_next_M11_after_SECOND',stream_tick0=tick-len(raw),executed_after_cut=True))
  old=labels.get(pos)
  if turn=='L':board.remove(pos);labels.pop(pos)
  else:board.add(pos);labels[pos]='new_R_'+str(tick)
  logs.append(dict(tick0=tick,read_number1=tick+1,cell=pos,turn=turn,old_physical_label=old,new_physical_label=labels.get(pos),owner=own,already_executed_at_SECOND_entry=tick<T));hd=(hd+(-1 if turn=='L'else 1))%4;pos=add(pos,VEL[hd])
 assert cutdata is not None and after_second is not None
 if name=='two_physical_erasures':assert sum(z['same_original_physically_alive']for z in cutdata['star'])==2
 if name=='alive_CORE_capture':
  assert all(z['same_original_physically_alive']for z in cutdata['star'])and sum(z['same_original_CORE']for z in cutdata['star'])==1
  assert next(z for z in cutdata['star']if z['same_original_CORE'])['cell']==(1,0)
 if port!='BOTTOM':assert all(next(z for z in after_second['star']if tuple(z['cell'])==q)['same_original_CURRENT']for q in PORTS[port])
 else:assert not any(all(next(z for z in cutdata['star']if tuple(z['cell'])==q)['same_original_CURRENT']for q in pair)for pair in PORTS.values())
 prepared.append(dict(name=name,actual_word=ns,actual_next_marker_after_SECOND=M,initial_head=[*p,h],complete_initial_BLACK_board=sorted(initial),initial_mass=len(initial),initial_star_labels_are_prepared_NOT_U_born=True,genuine_creating_U_ancestry_certified=False,SECOND_entry_cut=cutdata,after_SECOND_RAW_cut=after_second,claimed_survivor_port=port,all_actual_fine_reads=logs,scope='Actual prepared finite-board LR replay only. The BOTTOM control violates old-U-chord simplicity and is outside the three-port theorem.'))
D=[GP,QP,R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',R/'core_periodicity_new/current_residual_barrier_frozen_20261023_1822/manifest.json',R/'foreign_U_raw_ages34_2026-10-23/manifest.json',R/'seven_word_spatial_return_2026-10-23/first_foreign_first_returned_atom_simplicity_manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='At physical SECOND ordinary RAW entry after FIRST foreign F/Q/B plus one immediate ordinary RAW, each genuine old U4-star retains SAME original CURRENT corner pair fromLEFT/TOP/RIGHT, under signed old+foreign+firstreturn simplicity. Current means BLACK outside canonical entryK; future M11 is not executed. Local weaker four-port >=2 law needs only compatible colors/sector/core, not old-U chord simplicity. Necessary-only alignments are not genuine erosion histories.',physical_cut_convention=dict(time='after FOREIGN RAW and FIRSTordinary RAW, BEFORE SECOND RAW read0',CURRENT='same original R-born label BLACK outside SECOND entryK',CORE='physically alive original BLACK inside K; ordered current loss at cut but physical death NOT yet occurred',future_M11='compatibility only, at cut+0..10 NOT executed; if SECOND is D, the11thsymbol may be following-word read0',no_fictitious_K_at_internal_foreign_F_prefix=True),source_U_original_R_births=[dict(cell=q,U_RAW_tick0=t,U_RAW_read_number1=t+1)for q,t in sorted(birth.items())],three_current_corner_ports={k:sorted(v)for k,v in PORTS.items()},all2396_aligned_loss_or_capture_rows=rows,classification_counts=dict(counts),weaker_local324_loss_sets=[dict(lost_cells=k,count=v)for k,v in local_counts.items()],all15_BOTTOM_only_states_rejected_by_simple_U_chord=bottom_removed,all262_necessary_three_corner_states=survivors,old_loss_counts_at_physical_cut=[dict(physically_erased=n,alive_but_CORE=c,count=v)for(n,c),v in original_loss_counts.items()],FOREIGN_context_MISS_specialization=dict(all18_nontrivial_states=foreign_miss_states,zero_loss_default='all4current',fixed_current_port='LEFT',physical_originals='all4alive at exact cut',only_possible_ordered_CORE_loss='one right-column original, not yet physically deleted'),low_preFOREIGN_age_corollary=dict(hypothesis='genuine old U/UC/UCC sourceENTRY-to-firstFOREIGN C age at most4',used_signed_bound='9fdbb997 firstFOREIGN original-star RAW retirement or marker-only absorption needs at least5',conclusion='FOREIGN context misses oldstar; same original LEFT pair current at SECONDentry, all4 physicallyalive',not_used='No postFOREIGN age; returnedC does NOT change the old source age at the FOREIGN funding cut'),SECOND_step_literal_current_transfer=second,ordinary_atom_current_edge_footprint_checks=edgechecks,three_actual_prepared_controls=prepared,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'U_star_corner_transfer.json').write_text(json.dumps(o,indent=2)+'\n');print('Three SAME-original current corner ports at exact SECOND entry:2396/262; core-only18 separated; SECOND C2,D/V1,Uadjacent3; three prepared controls.')
