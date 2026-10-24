from pathlib import Path
from collections import Counter,defaultdict
from itertools import product,permutations
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];D=R/'old_V_young_FOREIGN_ports_total3_transfer_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='adc4680d961fbbaeb31e5d4a404e47e7aeb548014b9f01e4a229a5a0f15d6cb8';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
J=json.loads((D/'young_ports.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
lib=S.with_name('check_old_V_age2_coupled_independent.py');ns={'__file__':str(lib)};exec(lib.read_text().split('fore_ref={')[0],ns);W,M,K,tr,rot,center,xy,meet,pieces,G,C,I,ex,cut,geo,RES,endpoint,names=[ns[k]for k in('W','M','K','tr','rot','center','xy','meet','pieces','G','C','I','ex','cut','geo','RES','endpoint','names')]
assert G['V']['p']==1+3j and G['V']['h']==0
# Zero-C N rail: enumerate by exact available height; no arbitrary word cap.
def onlyN(p):
 dx=int(p.real-1);dy=int(p.imag-3)
 if min(dx,dy)<0:return []
 ans=[]
 for nd in range(dy+1):
  for nv in range(dy//3+1):
   rem=dy-nd-3*nv
   if rem>=0 and rem%4==0 and nd+nv==dx:ans.append((nd,nv,rem//4))
 return sorted(ans)
rr={(z['true_source_V_ENTRY_to_FOREIGN_ENTRY_age'],tuple(z['SAME_original_V_tag']),z['FOREIGN'],tuple(z['true_input'])):z for z in J['all376_actual_young_FOREIGN_source_tag_TRUEinput_roles']};rows=[];mc=Counter();wc={0:defaultdict(set),1:defaultdict(set)}
for n,tag,A in product((0,1),sorted(RES,key=lambda q:(q.real,q.imag)),'FQB'):
 hd=(-n)%4
 for slot in sorted(I[A],key=lambda q:(q.real,q.imag)):
  p=tag-rot(hd)*slot;ar=rr[n,tuple(xy(tag)),A,tuple(xy(slot))];assert ar['ENTRY']==[*xy(p),hd]
  if(int(p.real+p.imag)+hd)%2:models=[];why='sector'
  else:models=onlyN(p)if n==0 else endpoint(1+3j,p);why='all_endpoint_forced_whole_RAW_words_conflict'if models else'no_nonnegative_endpoint_count_solution'
  keys=names[:3]if n==0 else names;assert models==sorted(tuple(z[k]for k in keys)for z in ar['all_exact_count_models'])and why==ar['route'];mc[n]+=len(models)
  for counts in models:
   nw=set(permutations('D'*counts[0]+'V'*counts[1]+'U'*counts[2]));ww={()}if n==0 else set(permutations('D'*counts[3]+'V'*counts[4]+'U'*counts[5]))
   for a,b in product(nw,ww):
    ts=('V',)+a+(()if n==0 else('C',))+b+(A,);body=tr(''.join(W[x]for x in ts[:-1]));assert(body['p'],body['h'])==(p,hd);wc[n][ts].add((tuple(xy(tag)),tuple(xy(p)),tuple(xy(slot)),counts))
  rows.append((n,xy(tag),A,xy(slot),[*xy(p),hd],why,models))
assert len(rows)==376 and mc=={0:2,1:37}and[len(wc[n])for n in(0,1)]==[2,25]
wr={(z['true_FOREIGN_age'],tuple(z['actual_entire_source_V_to_FOREIGN_RAW_word'])):z for z in J['all27_endpoint_exhaustive_whole_words_and_literal_failures']};fail=[]
for n in(0,1):
 for ts,backs in wc[n].items():
  word=''.join(W[x]for x in ts)+M;z=tr(word);assert z['bad'];t,prev,p,c=z['bad'];ar=wr[n,ts];au=ar['actual_immutable_literal_conflict'];assert au==dict(feasible=False,conflict_read=t,previous_read=prev,cell=xy(p),turn=c)
  keys=names[:3]if n==0 else names;abr={(tuple(z['source_tag']),tuple(z['actual_FOREIGN_ENTRY'][:2]),tuple(z['true_input']),tuple(z['exact_model'][k]for k in keys))for z in ar['all_endpoint_model_backreferences']};assert abr==backs
  assert z['reads'][t][0]==z['reads'][prev][0]and z['reads'][t][2]==z['reads'][prev][2]and all(x[0]!=p for x in z['reads'][prev+1:t]);fail.append((n,''.join(ts),t,prev,xy(p),c))
assert len(fail)==len(wr)==27 and set(''.join(ts)for ts in wc[0])=={'VDDB','VDDDB'}
# ALL four headings are really tested, unlike the older age2 structural restriction.
jr={(tuple(z['first_lost_tag']),z['consumer'],tuple(z['ENTRY']),tuple(z['true_input'])):z for z in J['all128_full_four_heading_first_CURRENT_loss_roles']};co=Counter();kept=[];full=[]
for tag,A,h in product(sorted(RES,key=lambda q:(q.real,q.imag)),'DVU',range(4)):
 for slot in sorted(I[A],key=lambda q:(q.real,q.imag)):
  p=tag-rot(h)*slot;e,eh=ex(A,p,h);ar=jr[tuple(xy(tag)),A,(*xy(p),h),tuple(xy(slot))];assert ar['RAW_EXIT']==[*xy(e),eh]
  if(int(p.real+p.imag)+h)%2:why='sector'
  elif any(cut(A,p,h,q)for q in RES-{tag}):why='other_SOURCE_reserve_ENTRYCORE_or_actual_firstWHITE'
  elif meet(*pieces('V')[0],center(p,h),center(e,eh))is not None:why='earlier_GLOBAL_contact_not_actual_source_adjacency_since_FOREIGN_intervenes'
  else:why='same8_firstloss_ports_as_independently_signed_age2_coupled_proof';kept.append((xy(tag),A,[*xy(p),h],[*xy(e),eh]))
  assert ar['route']==why;co[why]+=1;full.append((xy(tag),A,[*xy(p),h],xy(slot),why))
assert len(full)==128 and len(kept)==8 and all(z[2][2]in(0,3)for z in kept)
old=json.loads((R/'old_V_all_tail_foreign_age2_coupled_ports_2026-10-24/V_n2.json').read_text());oldset={(tuple(z['first_lost_SOURCE_reserve_tag']),z['consumer'],tuple(z['ENTRY']))for z in old['all8_only_ordinary_firstloss_ports']};assert oldset=={(tuple(q),a,tuple(p))for q,a,p,e in kept}
assert J['all20_signed_postloss_obligations_copied_without_foreign_age_assumption']==old['all20_exact_post_firstloss_future_obligations']
ind=json.loads((R/'audits/check_old_V_age2_coupled_independent.json').read_text());assert ind['status'].startswith('PASS')and len(ind['all20_future_obligations'])==20
for z in J['all15_target_geometries_for_oldV_n0_n1_TOTAL3_corollary']:
 assert(z['actor'],*z['ENTRY'])in{(a,x,y,h)for a,x,y,h,s,t,typ in geo}and z['TOTAL_C']==3 and z['true_FOREIGN_age_corollaries']==[0,1]
# Source completion compatibility and SAME base births are independently retained.
source=[]
for n in(0,1):
 for src in('V','VC','VCC'):
  if src.count('C')>n:continue
  z=tr(''.join(W[a]for a in src));ek={z['p']+rot(z['h'])*k for k in K}
  for q in RES:assert z['last'][q]==G['V']['last'][q]and q not in ek
  source.append((n,src))
assert source==[(0,'V'),(1,'V'),(1,'VC')]
report=dict(status='PASS endpoint-exhaustive young V TRUE-input ports and qualified TOTAL3 all-heading coupled transfer',manifest=sha(MF),dependencies=J['dependencies'],all376_exact_ports=rows,exact_count_models=dict(mc),all27_same_physical_consecutive_turn_failures=fail,new_full128_counts=dict(co),all128_headings=full,eight_retained_port_keys_and_exits=kept,actual_eligible_source_completions=source,signed_age_independent_future_report=sha(R/'audits/check_old_V_age2_coupled_independent.json'),analytic_review=[
'The source-only port lemma begins at genuine RAWV(0,0,N), actual exit(1,3,N), with exactly0/1 ordinaryCs. Every true FOREIGN input, including marker capture, is placed at all four coordinates. Exact N and N/C/W semigroups use fixed endpoint height to bound positive-y terms and solve W-U from x, with no word-depth cap. All orderings of every finite multiset are retained.',
'Independent376 roles yield2+37 count models and exactly2+25 distinct whole words. Every word has a separately reconstructed earliest same-PHYSICAL-cell consecutive equal-turn conflict. This is a no-TRUE-input statement, not automatic SAME-currentness; no generic C-to-FOREIGN ban is used.',
'For genuine oldV true age0/1 only actual V / V-or-VC source completions are eligible. SourceVCC is not completed early. Signed preforeign r5/B4/Cbud-through3 and physical internalRAW lift provide original CURRENT before the foreign. Then no true input plus impossible ENTRYCORE/firstWHITE upgrades to COMPLETE context-MISS; a reading foreign is never presumed harmless.',
'ALL128 four-heading ordinary earliest-current-loss roles are rebuilt without age2 S/E deletion.64sector, held-field and actual earlier oldV contact cuts leave exactly the same8 N/W ports. Simultaneous true inputs remain permitted. One real intervening foreign means a source terminal repeat is nonadjacent.',
'After one foreign, headingsS/E/N/W correspond to TOTAL ordinary clocks0/1/2/3; thus retained N/W ports still have total2/3 independently of true foreign age. Their signed20 future obligations begin at the FIRSTLOSS RAWexit. Only remaining totalC, actual heldC context-MISS and real C R11/CU/y endpoint constraints are used, so the premise lift is genuinely age-independent.',
'An ordinary C has no external inputs; its3 external capture sites firstWHITE and2 alreadyENTRYCORE sites remain distinct. Target CURRENT is stopped at ENTRY, not through-contact permanence. Conditional transfer plus independently supplied funding closes only oldV TOTAL3 trueages0/1, no n>=3 pair-clock lift, arbitrary-tail simplicity, all-clock source reserve or furtherforeign iteration.'
])
S.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print(report['status']);print(sha(S.with_suffix('.json')));print(mc,co)
