from pathlib import Path
from collections import Counter
import hashlib,json
S=Path(__file__).resolve();R=S.parents[1];D=R/'U_star_one_foreign_return_transfer_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();man=D/'manifest.json';assert sha(man)=='1bf342dfdca683efa34e1f6ef1c38efd46f67ce5fee586e2b190fce7dad22871';mf=json.loads(man.read_text())
for f in mf['files']:assert sha(D/f['file'])==f['sha256']
ref=json.loads((D/'U_star_corner_transfer.json').read_text())
for p,h in ref['dependencies'].items():assert sha(R/p)==h
ns={'__file__':str(S.with_name('check_foreign_kinked_barrier_turn_independent.py'))};exec(Path(ns['__file__']).read_text().split('geometries=[]')[0],ns);W,M,walk,center,xy,meet,inventory=[ns[k]for k in['W','M','walk','center','xy','meet','inventory']];V=(1j,1,-1j,-1);K={-1-1j,-1,-1j,0j,1};star={0j,1j,1+0j,1+1j};ports={'LEFT':{0j,1j},'TOP':{1j,1+1j},'RIGHT':{1+0j,1+1j}};four={**ports,'BOTTOM':{0j,1+0j}}
tr={a:walk(W[a])for a in'DCVUFQB'};cx=lambda q:complex(*q);old=(xy(center(0j,0)),xy(center(tr['U']['p'],tr['U']['h'])))
assert old==((-1,-1),(-1,7))
birth={q:max(i for i,(p,h,c)in enumerate(tr['U']['reads'])if p==q and c=='R')for q in star};assert {xy(q):t for q,t in birth.items()}=={(0,0):4,(0,1):19,(1,0):9,(1,1):18}
for b in'DCVU':assert {p for p,h,c in tr[b]['reads'][:6]}==K
local={};universe=set()
for a in'FQB':
 for b in'DCVU':
  raw=walk(W[a]+W[b]);full=walk(W[a]+W[b]+M);assert raw['feasible']and full['feasible'];local[a,b]=(raw,full)
  for q,black in full['req'].items():
   if black:
    for tag in star:
     for h in range(4):p=tag-q*(-1j)**h;universe.add((a,b,*xy(p),h))
counts=Counter();beforegeometry=0;loss=Counter();bottom=0;missrows=0;keeps={};statusrefs={(q['foreign'],q['first_returned_raw_atom'],*q['foreign_entry_in_creator_U_frame']):q for q in ref['all262_necessary_three_corner_states']};reasons={(q['foreign'],q['first_return'],*q['pose']):q['reason']for q in ref['all2396_aligned_loss_or_capture_rows']}
for a,b,x,y,h in sorted(universe):
 p=complex(x,y);rot=(-1j)**h;raw,full=local[a,b];end=p+rot*raw['p'];eh=(h+raw['h'])%4;k2={end+q*(-1j)**eh for q in K};k0={p+rot*q for q in K};fp=p+rot*tr[a]['p'];fh=(h+tr[a]['h'])%4
 if(x+y+h)%2:why='wrong_active_sector'
 elif star&k0:why='old_CURRENT_star_inside_FOREIGN_entryK'
 elif any(full['req'].get((q-p)/rot)is False for q in star):why='old_BLACK_original_requires_before_WHITE'
 else:
  reads={q:[(i,c)for i,(r,hh,c)in enumerate(raw['reads'])if p+rot*r==q]for q in star};alive={q for q in star if not reads[q]};core=alive&k2;keep=alive-k2;lost=star-keep;beforegeometry+=1
  assert lost and len(lost)<=2 and any(pair<=keep for pair in four.values())
  for q in star:
   if reads[q]:assert reads[q][0][1]=='L'
   elif q in core:
    future=[(i,c)for i,(r,hh,c)in enumerate(full['reads'])if p+rot*r==q];assert future and future[0][0]>=len(raw['reads'])and future[0][0]-len(raw['reads'])<6 and future[0][1]=='L'
   else:assert(q-p)/rot not in full['req']
  fc=[(xy(center(p,h)),xy(center(p+rot*tr['F']['p'],(h+tr['F']['h'])%4)))]
  if a!='F':fc.append((fc[-1][1],xy(center(fp,fh))))
  rc=(xy(center(fp,fh)),xy(center(end,eh)));assert(p,h)!=(4j,0)
  if any(meet(*old,*z)is not None for z in fc):why='actual_foreign_proxy_meets_old_U_chord_nonadjacently'
  elif meet(*old,*rc)is not None:why='actual_first_return_chord_meets_old_U_chord_nonadjacently'
  else:
   why='necessary_only_three_corner_transfer_state';assert any(pair<=keep for pair in ports.values());rr=statusrefs[a,b,x,y,h];assert keep=={cx(q)for q in rr['same_original_CURRENT_cells']};assert k2=={cx(q)for q in rr['SECOND_entryK']};assert len(raw['reads'])==rr['physical_cut']['SECOND_atom_entry_tick0'];loss[len(star-alive),len(core)]+=1;keeps[a,b,x,y,h]=keep
   for st in rr['same_original_star_statuses']:
    q=cx(st['cell']);assert st['original_physically_alive_at_cut']==(q in alive)and st['original_ordered_CURRENT_at_cut']==(q in keep)and st['original_alive_but_CORE_at_cut']==(q in core)
    assert [(z['combined_tick0'],z['turn'])for z in st['executed_RAW_reads']]==reads[q]
   foreignctx=walk(W[a]+M)['req'];is_miss=all((q-p)/rot not in foreignctx for q in star);assert is_miss==rr['FOREIGN_complete_context_MISSES_original_star']
   if is_miss:missrows+=1;assert alive==star and ports['LEFT']<=keep and core<={1+0j,1+1j}and len(core)<=1
  if lost=={1j,1+1j}:bottom+=1;assert why!='necessary_only_three_corner_transfer_state'
 counts[why]+=1;assert why==reasons[a,b,x,y,h]
assert len(universe)==2396 and beforegeometry==324 and len(keeps)==262 and bottom==15 and missrows==18 and counts==ref['classification_counts'];assert loss=={(1,0):205,(2,0):39,(0,1):18}
# Continuation literal input capacity and exact edge-contact containment.
continuation={}
for b in'DCVU':
 full=walk(W[b]+M);inputs={q for q,c in full['req'].items()if c}-K;adj=[(x,y)for x in inputs for y in inputs if xy(x)<xy(y)and abs((x-y).real)+abs((x-y).imag)==1];contacts=inventory((-1,-1),xy(center(tr[b]['p'],tr[b]['h'])));assert set(contacts)<={xy(q)for q in full['req']}
 if b=='C':assert inputs==set()
 if b=='D':assert inputs=={1j}
 if b=='V':assert inputs=={3j,1+2j}and not adj
 if b=='U':assert {tuple(sorted(map(xy,p)))for p in adj}=={((-1,1),(-1,2)),((-1,2),(0,2)),((0,2),(0,3))}
 continuation[b]={'inputs':sorted(map(xy,inputs)),'adjacent_pairs':sorted([sorted(map(xy,p))for p in adj]),'edge_contacts':sorted(contacts)}
controls=[]
for r in ref['three_actual_prepared_controls']:
 B={cx(q)for q in r['complete_initial_BLACK_board']};orig=set(star);p=cx(r['initial_head'][:2]);h=r['initial_head'][2];w=''.join(W[b]for b in r['actual_word'])+M;cut=r['SECOND_entry_cut']['tick0'];secondcut=r['after_SECOND_RAW_cut']['tick0'];snaps={}
 for t,ch in enumerate(w):
  if t in(cut,secondcut):
   kc={p+q*(-1j)**h for q in K};snaps[t]=(set(orig),orig-kc)
   rr=r['SECOND_entry_cut']if t==cut else r['after_SECOND_RAW_cut'];assert [*xy(p),h]==rr['head']
   for q in rr['star']:
    z=cx(q['cell']);assert q['same_original_physically_alive']==(z in orig)and q['same_original_CURRENT']==(z in orig-kc)and q['same_original_CORE']==(z in orig&kc)
  assert(ch=='L')==(p in B);log=r['all_actual_fine_reads'][t];assert xy(p)==tuple(log['cell'])and ch==log['turn']and log['already_executed_at_SECOND_entry']==(t<cut)
  if ch=='L':B.remove(p);orig.discard(p)
  else:B.add(p)
  h=(h+(1 if ch=='R'else-1))%4;p+=V[h]
 if r['name']=='alive_CORE_capture':assert snaps[cut][0]==star and len(snaps[cut][1])==3 and r['all_actual_fine_reads'][85]['cell']==[1,0]
 controls.append({'name':r['name'],'initial_mass':r['initial_mass'],'reads':len(w),'cut':cut,'alive_at_cut':len(snaps[cut][0]),'current_at_cut':sorted(map(xy,snaps[cut][1]))})
out={'status':'PASS same-original three-corner transfer at exact SECOND entry, necessary states only','author_manifest':sha(man),'aligned_states':len(universe),'filters':dict(counts),'weaker_four_corner_states':beforegeometry,'BOTTOM_only_rejections':bottom,'loss_distribution':[(*k,v)for k,v in loss.items()],'foreign_MISS_core_only_states':missrows,'literal_second_capacity':continuation,'prepared_physical_controls':controls,'analytic_review':[
'Loss or CORE capture of an initially current original requires a TRUE initial-color context cell. All four headings and four star identities against all12 exact suffix masks exhaust every such alignment with no geometry cutoff. If no alignment exists allfour remain unread outsideK. BeforeWHITE contradictions and entryK exclusions use actual original BLACK state, not labels reconstructed from final color.',
'Only A RAW+b1 RAW reads determine physical survival at CUT2. FutureM11 is compatibility, not executed. All current originals are whole-context MISS; the18 CORE captures have their firstL still future within the firstsix reads. An original unread throughb1 cannot have entered foreign-exitK, since every ordinary atom physically visits allK in its firstsix RAW reads. No internalF56 core is invented.',
'The324 color/sector/core-compatible states have at mosttwo losses and a four-corner pair. Exact repairedforeign pieces and firstreturned chord against oldU remove62 states, including all15 BOTTOM-only cases. True sourceU-to-foreign adjacency at0,4N is not among star-hit alignments and is never falsely excluded. Signed proxy simplicity applies through exactlyb1.',
'Foreign fullcontextMISS specializes to18 core-only nontrivial states, preserving allfour physical originals and fixedCURRENTLEFT pair. The age<=4 corollary invokes signed firstFOREIGN star-effect>=5 only beforeforeign, with its original source-entryclock; no returnedC age advance or postforeign maturation is used.',
'At secondentry the retained adjacent pair is outsideK. Genuine input or whole-contextMISS exhausts a valid old BLACK cell. C has noinputs; D one; V two diagonalinputs cannot take bothadjacent; U has exactlythree adjacent input-pair escapes. Marker-only inputs can be orderedCORE losses before physicaldeath. GuaranteedMISS member is outsidefutureK and its edge avoidswholeordinarychord by fresh exact footprint containment.',
'Three complete prepared boards were replayed with original-label deletion only, including84-cut BDC where allfour remain physicallyalive and(1,0) dies only at85. These initial labels are NOT claimed genuine U births/attained ancestry. BOTTOM control violates the geometric premise. No lateriteration, surviving-pair attachment forRIGHT, or permanentstar claim is inferred.' ]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
