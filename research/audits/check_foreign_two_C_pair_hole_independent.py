from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'foreign_two_C_pair_hole_transfer_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();M=D/'manifest.json';assert sha(M)=='158e512e826f161f1db153930ef5163dfce5b9d464d7e3dcef3c82de76408d20';mf=json.loads(M.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'pair_hole_transfer.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,Mk,K,tr,rot,xy=[ns[k]for k in('W','M','K','tr','rot','xy')];NE={-1-1j,-1,-1+1j,0j,1j,1,1+1j,1+2j,2,2+1j};hole=2j;gate=3-1j;target=3+3j;G={a:tr(W[a])for a in'DCVUFQB'}
def context(a):
 z=tr(W[a]+Mk);first={}
 for t,(q,h,c)in enumerate(z['reads']):first.setdefault(q,(c,t))
 return z,first
CTX={a:context(a)for a in'DCVUFQB'}
def held_conflicts(a,p):
 first=CTX[a][1];out=[]
 for g in sorted(NE,key=lambda p:(p.real,p.imag)):
  q=g-p;f=first.get(q)
  if q in K or(f and f[0]=='R'):out.append(dict(original=xy(g),local=xy(q),role='ENTRY_CORE'if q in K else'initial_WHITE',first=list(f)if f else None))
 return out
for a in'FQB':
 z=G[a];ek={z['p']+rot(z['h'])*q for q in K};O={q for q,(c,t)in z['last'].items()if c=='R'and q not in ek};assert NE<=O and z['last'][hole]==('L',28)
 rc=next(r for r in J['all3_source_fields']if r['source_foreign']==a);assert rc['actual_EXIT']==[*xy(z['p']),z['h']]and rc['all10_output_lastR']==[dict(cell=xy(g),own_R_tick0=z['last'][g][1])for g in sorted(NE,key=lambda p:(p.real,p.imag))]
I={a:{q for q,(c,t)in CTX[a][1].items()if c=='L'and q not in K}for a in'DVU'};loss=[];cnt=Counter()
for g in NE:
 for a in'DVU':
  for q in I[a]:
   p=g-q;bad=held_conflicts(a,p);why='sector'if int(p.real+p.imag)%2 else('held_NE_CORE_WHITE'if bad else'sole_U_pair_breaker');r=next(v for v in J['all80_N2_NE_first_loss_roles']if v['original']==xy(g)and v['consumer']==a and v['true_input']==xy(q));assert r['entry']==[*xy(p),0]and r['classification']==why
   if why=='held_NE_CORE_WHITE':assert r['conflicts']==bad
   if why=='sole_U_pair_breaker':loss.append((g,a,p))
   cnt[why]+=1
assert cnt=={'sector':40,'held_NE_CORE_WHITE':38,'sole_U_pair_breaker':2}and set(loss)=={(g,'U',gate)for g in(2,2+1j)}
assert G['U']['p']+gate==target
for g in NE-{2,2+1j}:assert g-gate not in CTX['U'][1]
assert G['U']['last'][-1+1j]==('L',14)and G['U']['last'][-1+2j]==('R',21)and hole-gate not in CTX['U'][1]
z=G['U'];ek={z['p']+q for q in K};UO={q for q,(c,t)in z['last'].items()if c=='R'and q not in ek};new={gate+q for q in UO};assert len(new)==9 and max(q.imag for q in new)==2 and sorted(map(xy,new))==J['post_breaker_STATE']['new_U_all9_CURRENT'];assert all(g-target not in K for g in new|(NE-{2,2+1j}))
for a in'DCVU':
 rr=[q for q,h,c in G[a]['reads']if c=='R'];assert min(q.real for q in rr)>=-1 and min(q.imag for q in rr)>=0
 if a!='C':assert min(q.imag for q in I[a])>=1 and G[a]['p'].imag>0
rep=[];rcnt=Counter()
for a in'DVU':
 for q,(c,t)in G[a]['last'].items():
  if c!='R':continue
  p=hole-q;ep=p+G[a]['p'];bad=held_conflicts(a,p);why='sector'if int(p.real+p.imag)%2 else('held_NE_CORE_WHITE'if bad else'three_common_R8_funders');r=next(v for v in J['all28_CORE_inclusive_hole_last_R_roles']if v['producer']==a and v['RAW_last_R_slot']==xy(q));assert r['entry']==[*xy(p),0]and r['RAW_EXIT']==[*xy(ep),0]and r['R_own_tick0']==t and r['classification']==why
  if why=='held_NE_CORE_WHITE':assert r['conflicts']==bad
  if why=='three_common_R8_funders':rep.append((a,p,ep,t))
  rcnt[why]+=1
assert rcnt=={'sector':14,'held_NE_CORE_WHITE':11,'three_common_R8_funders':3}and set(rep)=={('D',-2+2j,-1+3j,8),('V',-2+2j,-1+5j,8),('U',-2+2j,-2+6j,8)}
for a,p,e,t in rep:assert p!=gate and e.imag>gate.imag and(e.imag>target.imag or(e.imag==target.imag and e!=target))
for a in'FQB':assert CTX[a][1][hole-target]==('L',42)
assert len(J['all9_portable_next_FOREIGN_3_3_gate_exclusions'])==9
# Rebuild two DISTINCT minimal full initial fields and physical identities, with all actual core cuts.
seq='UFCDDVCDUU';raw=''.join(W[a]for a in seq);prefix=tr(raw+Mk);ready=tr(raw+W['Q'][:42]);assert not prefix['bad']and not ready['bad']and len(raw)==218 and(prefix['reads'][218][:2])==(3+7j,0)
seeds=[{q for q,v in z['req'].items()if v}for z in(prefix,ready)];assert list(map(len,seeds))==[35,45]and seeds[0]<seeds[1]and all(q not in prefix['req']for q in seeds[1]-seeds[0]);assert sorted(map(xy,seeds[1]-seeds[0]))==J['unread_extension'];old={q+4j:28+G['F']['last'][q][1]for q in NE};controls=[]
for seed,row in zip(seeds,J['all2_actual_genuine_U_entry_fields']):
 assert sorted(map(xy,seed))==row['complete_seed'];B={q:['initial',xy(q)]for q in seed};p=0j;h=0;tick=0;deaths={};cutrows=[]
 for i,a in enumerate(seq):
  for c in W[a]:
   assert(p in B)==(c=='L')
   if c=='R':B[p]=tick
   else:
    bid=B.pop(p)
    if isinstance(bid,int):deaths[bid]=tick
   h=(h+(1 if c=='R'else-1))%4;p+=rot(h)*1j;tick+=1
  if i>=1:
   core={p+rot(h)*q for q in K};states=[dict(cell=xy(q),source_FOREIGN_R_birth=bid,SAME_physically_BLACK=B.get(q)==bid,CURRENT=B.get(q)==bid and q not in core,actual_present_R_identity=B.get(q))for q,bid in sorted(old.items(),key=lambda z:(z[0].real,z[0].imag))];cutrows.append(dict(after_atom_index0=i,atom=a,RAW_cut_tick0=tick,actual_head=[*xy(p),h],all10_original_source_FOREIGN_ID_states=states))
 assert cutrows==row['all_actual_marked_NE_ID_cut_states'];assert deaths[35]==203 and deaths[36]==204 and B.get(2+5j)==211 and 2+4j not in B and 6j not in B and all(B.get(q)==bid for q,bid in old.items()if q not in{2+4j,2+5j});assert all(B[3+3j+q]==190+G['U']['last'][q][1]for q in UO)
 destroyed=[]
 for i,c in enumerate(W['Q']):
  if(p in B)!=(c=='L'):break
  if c=='L':
   if p in old and B[p]==old[p]:destroyed.append(i)
   del B[p]
  else:B[p]=tick
  h=(h+(1 if c=='R'else-1))%4;p+=rot(h)*1j;tick+=1
 assert i==(12 if len(seed)==35 else 42)and row['first_unmatched_Q_request']['candidate_Q_own_tick0']==i and row['first_unmatched_Q_request']['cell']==xy(p)and not destroyed;assert i!=42 or p==6j;controls.append(dict(seed=len(seed),RAW=218,first_Q_failure=i,old_pair_deaths=[203,204],new_q_birth=211))
O={'status':'PASS portable coupled two-C NE-pair transfer and source-L28 hole target guard ONLY','manifest':sha(M),'script':sha(S),'first_loss_counts':dict(cnt),'last_R_counts':dict(rcnt),'controls':controls,'analytic_review':['The signed entryframe sourceNE10 frontier throughS0/E1 is used without any U orsimplehistory hypothesis. All80 actualN trueinput roles retain simultaneousBLACK inputs and markerCORE absorption, giving exactlyone U3,-1 firstloss atom, selectedtwice byits two originalinputs. Other38 reject only actualheldCORE/beforeWHITE conflicts.','Complete pairbreakerRAW deletesold2,0 andold2,1; R21at2,1 isNEW, notidentityrestoration. EightSAMEsurvivors andnineactualnewUoutputs areoutsideexitCORE athead3,3 andbelowrow3. Subsequent N inputs occuratY>=4; exact CORE interface andstrictlyincreasingheads preserveall17, without extendingthroughanotherFOREIGN.','AllphysicalR footprints ofD/C/V/U, notjustO, giveSmaxx<=-2/Emaxy<=-2, so sourceL28 hole0,2 staysWHITE beforeN2. A laterBLACK atacompletedcut haslastRAW R, includingCOREwrites; the28 exactroles beforefirstloss leaveonlythree commonR8funders. Noneis thepairbreaker. Their exity>=3 cannot reach pairbreakerheady-1 or target3,3 (Dsameywrongx,othershigher); afterpairbreakerallR y>=3 missholey2. This coversbothbefore/afterfirstloss branches withouta globalWHITE permanenceclaim.','Allnine source/targetFOREIGN pairs atrelative3,3 firstdemandholeBLACK atownL42, withnopriorreadthere, sofail. Otherposes andlaterC remainopen.','Two actualcomplete initialfields35/45 are separatelyreconstructed; ten extraBLACKs are genuinelyunreadthroughprefixplusM. Bothattain oldpairphysicaldeaths203/204,newq211 andall eightoldsurvivorsCURRENT. Fixed35firstfails attemptedQ12,distinct45 follows42readsthenfailsQ42 atworld0,6. NeithercompletesthesecondQ, and no physicaltermination or fullfieldfinite-state quotient isclaimed.']};S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
