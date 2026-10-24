from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'foreign_C5_joint_rewrite_frontier_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='ff4ea217c9fe1a66b6a7d67e2f53f9c6bcd6c15a5c2635978c0887ca12e832a7';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'C5_joint_rewrite.json').read_text());lib=S.parent/'check_old_V_second_age1_independent.py';N={'__file__':str(lib)};exec(lib.read_text().split('# Universal')[0],N);W,M,K,tr,rot,xy=[N[k]for k in('W','M','K','tr','rot','xy')];G={a:tr(W[a])for a in W};C={a:tr(W[a]+M)for a in W};I={a:{q for q,b in C[a]['req'].items()if b and q not in K}for a in W};pose=lambda p,h:[*xy(p),h];sort=lambda z:sorted(z,key=lambda p:(p.real,p.imag));ff=lambda a,q:next(([c,t]for t,(p,h,c)in enumerate(C[a]['reads'])if p==q),None)
F15={-1-1j,-1+0j,-1+1j,0j,1j,1+0j,1+1j,1+2j,2+0j,2+1j,-4+1j,-4+2j,-3+2j,-2+1j,-2-1j};old13=F15-{2+0j,2+1j};HK={-1-1j,-2-1j,-3-1j,-3-2j}
for a in'FQB':
 ek={G[a]['p']+rot(G[a]['h'])*k for k in K};oo={q for q,(c,t)in G[a]['last'].items()if c=='R'}-ek;assert F15<=oo
 if a in'QB':assert HK<=oo
# All external CORE capture is covered by actual context requirements; C's
# new exitCORE cells never supply a silent CURRENT-black absorption.
core=[]
for a in'DCVU':
 ek={G[a]['p']+rot(G[a]['h'])*k for k in K}
 for q in ek-K:
  f=ff(a,q);assert f;core.append([a,xy(q),f])
  if a=='C':assert f[0]=='R'
 for q in I[a]:
  if q not in G[a]['req']:assert q in ek
assert not I['C']and sum(map(len,(I[a]for a in'DVU')))==8

def bad(a,p,h,field):
 z=[]
 for g in sort(field):
  q=(g-p)/rot(h);f=ff(a,q)
  if q in K or f and f[0]=='R':z.append(dict(original=xy(g),local=xy(q),first=f,reason='ENTRY_CORE'if q in K else'first_WHITE'))
 return z

def losses(field,author,ep=None):
 rows=[];co=Counter();kept=[]
 for g in sort(field):
  for a in'DVU':
   for slot in sort(I[a]):
    p=g-rot(1)*slot;au=next(z for z in author if z['original']==xy(g)and z['consumer']==a and z['ENTRY']==pose(p,1));assert au['true_input']==xy(slot)and au['actual_L']['context_tick0']==ff(a,slot)[1]
    if(int(p.real+p.imag)+1)%2:why='sector'
    else:
     b=bad(a,p,1,field);assert b==au['field_conflicts']
     if b:why='held_field'
     elif ep is not None and(p.real<ep.real or p.imag>ep.imag):why='behind_actual_E_exit'
     else:why='possible_first_loss';kept.append((g,a,p))
    assert why==au['route'];co[why]+=1;rows.append([xy(g),a,pose(p,1),xy(slot),why])
 assert len(rows)==8*len(field)==len(author)
 return rows,co,kept
cases=[];futures={}
for kind,f0,gate in[('F',old13,-3-2j),('QB',old13|HK,-4-3j)]:
 au=next(z for z in J['all568_pre_post_joint_loss_rows']if z['source_kind']==kind);assert list(map(xy,sort(f0)))==au['pre_field']and au['gate']==pose(gate,1);rows,co,left=losses(f0,au['all_pre_E5_first_loss_rows']);assert dict(co)==au['pre_counts'];assert all(a=='U'and p==gate for g,a,p in left)
 spent={g for g,a,p in left};assert spent==({-2-1j,-1-1j}if kind=='F'else{-3-2j});ep=gate+rot(1)*G['U']['p'];assert au['actual_U_RAW_EXIT']==pose(ep,1)
 survive=f0-spent;localUO={q for q,(c,t)in G['U']['last'].items()if c=='R'and(q-G['U']['p'])/rot(G['U']['h'])not in K};assert len(localUO)==9;new={gate+rot(1)*q for q in localUO};assert not new&survive
 for g in survive:assert(g-gate)/rot(1)not in G['U']['last']and(g-ep)/rot(1)not in K
 f1=survive|new;assert len(f1)==(20 if kind=='F' else 23)and list(map(xy,sort(f1)))==au['post_field'];r2,c2,k2=losses(f1,au['all_post_E5_first_loss_rows'],ep);assert not k2 and dict(c2)==au['post_counts']
 for a in'DVU':z=rot(1)*G[a]['p'];assert z.real>0 and z.imag<=0
 deaths={}
 for g in spent:
  q=(g-gate)/rot(1);f=ff('U',q);assert f[0]=='L'and f[1]<28;deaths[tuple(xy(g))]=f[1]
 assert deaths=={tuple(z['original']):z['own_physical_L']['context_tick0']for z in au['physically_spent_old_identities']}
 births={tuple(xy(g)):G['U']['last'][(g-gate)/rot(1)][1]for g in new};assert births=={tuple(z['cell']):z['own_final_RAW_R']['context_tick0']for z in au['all9_genuine_new_R_births']}
 ctrl=au['prepared_local_rewrite'];seed={gate+rot(1)*q for q,b in C['U']['req'].items()if b}|f0;assert list(map(xy,sort(seed)))==ctrl['complete_seed']and len(seed)==ctrl['mass'];B={g:['prepared_initial',xy(g)]for g in seed};p=gate;h=1;boards=[]
 for t,c in enumerate(W['U']+M):
  rr=ctrl['all39_reads'][t];assert rr['tick0']==t and rr['cell']==xy(p)and rr['turn']==c and rr['prior_identity']==B.get(p);assert(p in B)==(c=='L')
  if c=='L':del B[p]
  else:B[p]=['new_R',t]
  h=(h+(1 if c=='R'else-1))%4;p+=rot(h)*1j;boards.append(dict(cut=t+1,pose=pose(p,h),complete_BLACK=list(map(xy,sort(B)))))
  if t+1 in[28,39]:
   cut=next(z for z in ctrl['actual_cuts']if z['actual_read_count']==t+1);assert cut['pose']==pose(p,h)and cut['complete_BLACK']==list(map(xy,sort(B)))
   for g in survive:assert B[g]==['prepared_initial',xy(g)]and(g-p)/rot(h)not in K
   for g in new:assert B[g]==['new_R',births[tuple(xy(g))]]and(g-p)/rot(h)not in K
 cases.append(dict(kind=kind,pre_counts=dict(co),post_counts=dict(c2),pre_rows=rows,post_rows=r2,gate=pose(gate,1),exit=pose(ep,1),deaths=[[*g,t]for g,t in deaths.items()],new_births=[[*g,t]for g,t in births.items()],complete_prepared_seed=list(map(xy,sort(seed))),all39_complete_boards=boards));futures[kind]=(f1,ep)
assert sum(len(z['pre_rows'])+len(z['post_rows'])for z in cases)==568
# Earliest BLACK-at-completed-RAW-cut origins, including CORE writes. An
# origin with first localL requires an earlier BLACK cut and is not a first repair.
hrows=[];hkeep=[]
for hole in[-2+0j,-4-2j]:
 for h in[2,1,0,3]:
  for a in'DCVU':
   for slot,(c,t)in G[a]['last'].items():
    if c!='R':continue
    p=hole-rot(h)*slot;ep=p+rot(h)*G[a]['p'];eh=(h+G[a]['h'])%4;ar=next(z for z in J['all288_QB_pre_rewrite_hole_last_R_rows']if z['hole']==xy(hole)and z['heading']==h and z['producer']==a and z['ENTRY']==pose(p,h));first=ff(a,slot);assert ar['final_R']['context_tick0']==t and ar['first_turn']==first[0]and ar['first_read']['context_tick0']==first[1]and ar['RAW_EXIT']==pose(ep,eh)and ar['hole_in_EXIT_CORE']==((hole-ep)/rot(eh)in K)
    if(int(p.real+p.imag)+h)%2:why='sector'
    else:
     b=bad(a,p,h,old13|HK);assert b==ar['pre_rewrite_field_conflicts'];why='held_field'if b else'possible_funder'
    assert why==ar['route'];hrows.append([xy(hole),a,pose(p,h),pose(ep,eh),t,first,why])
    if why=='possible_funder':hkeep.append(hrows[-1])
assert len(hrows)==288 and len(hkeep)==5 and all(z[0]==[-4,-2]for z in hkeep)
firstrepair=[z for z in hkeep if z[5][0]=='R'];assert len(firstrepair)==1 and firstrepair[0][1:5]==['C',[-6,-2,0],[-6,-1,3],8]
assert all(z[2][2]==3 and z[5]==['L',5]and z[4]==9 for z in hkeep if z not in firstrepair)
for a in'QB':assert G[a]['last'][-2+0j]==('L',48)
assert G['Q']['last'][-4-2j]==('L',56)and G['B']['last'][-4-2j]==('R',64)
# Every physical first L of a current old hook, including entryCORE and actualM.
f1,ep=futures['QB'];goals={};spent={-3-2j}
for a in'FQB':
 for slot,b in C[a]['req'].items():
  if not b:continue
  for g in HK:
   p=g-rot(1)*slot
   if(int(p.real+p.imag)+1)%2:continue
   goals.setdefault((a,p),[]).append((g,slot,ff(a,slot)[1]))
co=Counter();grows=[]
for(a,p),ws in goals.items():
 remaining=[z for z in ws if z[0]not in spent];ar=next(z for z in J['all71_post_rewrite_next_FOREIGN_old_hook_first_L_rows']if z['actor']==a and z['ENTRY']==pose(p,1));assert {(tuple(xy(g)),tuple(xy(q)),t)for g,q,t in remaining}=={(tuple(z['original']),tuple(z['local']),z['actual_first_L']['context_tick0'])for z in ar['candidate_old_first_L']}
 if not remaining:why='old_candidate_already_physically_spent'
 elif p.real<ep.real or p.imag>ep.imag:why='behind_actual_E_rewrite_exit'
 else:why='post_field';b=bad(a,p,1,f1);assert b and b==ar['post_field_conflicts']
 assert why==ar['route'];co[why]+=1;grows.append([a,pose(p,1),[[xy(g),xy(q),t]for g,q,t in remaining],why])
assert len(goals)==71 and co=={'old_candidate_already_physically_spent':3,'behind_actual_E_rewrite_exit':54,'post_field':14}
O=dict(status='PASS exact ordinary E5 one-rewrite retained-field interface, Q-only repair precondition and conditional nextFOREIGN physical-MISS',manifest=sha(MF),script=sha(S),dependencies=mf['dependencies'],all568_loss_rows_and_prepared_fields=cases,CORE_capture_checks=core,all288_hole_final_R_origins=hrows,five_possible_hole_funders=hkeep,all71_next_FOREIGN_first_L_poses=grows,recipient_counts=dict(co),analytic_review=[
'The signed ordinaryC4 reserve supplies old13 and, forQ/B, the two extra hook originals at every completed S4 cut, independently of whether the oldN2 pair was spent. The next actualC is input-free; all external newEXITcore cells have firstWHITE requirements, so no silent CURRENT absorption is omitted. No old9 paired outputs or whole-field equality is assumed.',
'Joint earliestCURRENTloss in the E5 DVU rail uses all8 true input/marker roles per held tag. Independent568 before/after rows reproduce onlyU(-3,-2,E) forF orU(-4,-3,E) forQ/B. A TRUE simultaneous input is permitted. These are necessary local interfaces, not actual source-history reachability claims.',
'At the F gate oldF46/F47 physically die atU13/U14; at theQ/B gate lowerhook(-3,-2) physicallydiesU14. Every other selected oldID is RAW-MISS and outside exitCORE. Nine actual U lastR outputs, including recycled identities, are individually tracked and disjoint from old survivors. Renewed20/23 fields have only two remaining nonconflicting E roles each, both behind the actual exit, so no further completed E loss occurs at any rail length.',
'Two complete prepared21/24-cell boards replay all39 real U+M reads and every fullboard. The retained old/new identities are CURRENT at both RAW28 and suppliedM39 cuts. These controls do not claim an earlierFOREIGN, sourceU ancestry, minimality or a completed continuing G7 factor.',
'For the intact pre-rewriteQBfield, every possible finalRAW R to each selectedhole is reconstructed in allfour headings, COREincluded. L48(-2,0) has no compatible origin. Q-onlyL56(-4,-2) has preciselyone firstrepair candidate C atN ENTRY(-6,-2),R8,EXIT(-6,-1,W), hence the actualthirdC completion. Four apparentW funders firstneedtheholeBLACK atL5 and cannotbeitsfirst completedrepair. The premise is intact retainedfield at priorcuts, not arbitrary physicalWHITE permanence through partialwords.',
'B actually writes(-4,-2)atR64, so theQhole conclusion is explicitlynot transferredtoB. Earlierhistory or unstated oldU outputages are neverused. TheC3 restoration gate remainsopen, notexcluded.',
'After theQB rewrite, the loweroriginal isalreadydead andthreeothers remainCURRENT duringordinaryE5. All71 candidate nextFOREIGN+realM firstL poses split3spent/54behindexit/14renewedfieldconflicts. Thus a COMPLETE markednextFOREIGN cannot physicallyfirst-delete oneofthose remainingoriginals. A failedpartialword maydeletebeforelaterfailure; noCURRENT-afterFOREIGN or E6 iteration is asserted.',
'The pre-rewrite nextFOREIGN branch remainsopen, asdoes fullC5hooktransfer orsourcehistoryattainment. ForF bothprotectedoriginalsarealreadyspentbytheordinarygate. No rebornBLACK is identifiedwithitsoldtag, andno simplicity,globalfirstcontact,railcap,captureorrenewalbudget follows.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print([(z['kind'],z['pre_counts'],z['post_counts'])for z in cases]);print(sha(S.with_suffix('.json')))
