from pathlib import Path
from collections import defaultdict,Counter
from itertools import product
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'Q_B_hook_next_foreign_low_clock_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json'
assert sha(MF)=='3300959a542d5e8c97fe278a32a282174d6a43a37fec72a40cd5402dc25f741c';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'low_clock_hook_transfer.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy=[ns[k]for k in ('W','M','K','tr','rot','xy')]
HOOK={-1-1j,-2-1j,-3-1j,-3-2j};NE={-1-1j,-1+0j,-1+1j,0j,1j,1+0j,1+1j,1+2j,2+0j,2+1j};field=HOOK|NE

def first(a):
 ans={}
 for t,(q,h,c) in enumerate(tr(W[a]+M)['reads']):ans.setdefault(q,(c,t))
 return ans
frames={a:tr(W[a])for a in'QB'}
for a,z in frames.items():
 assert z['h']==2 and HOOK<={q for q,(c,t)in z['last'].items()if c=='R' and(q-z['p'])/rot(2)not in K}
 row=next(r for r in J['all2_source_hook_frames']if r['source']==a);assert row['EXIT']==[*xy(z['p']),2]
 assert row['all4_own_hook_R_births']==[dict(cell=xy(q),R_tick0=z['last'][q][1])for q in sorted(HOOK,key=lambda p:(p.real,p.imag))]
kept={};summary={}
for clock,h,title in [(0,2,'all57_C0_true_hook_loss_pose_field_checks'),(1,1,'all56_C1_true_hook_loss_pose_field_checks')]:
 goals=defaultdict(list)
 for a in'FQB':
  for g in HOOK:
   for slot,(c,t)in first(a).items():
    if c!='L' or slot in K:continue
    p=g-rot(h)*slot
    if (int(p.real+p.imag)+h)%2:continue
    goals[a,p].append((g,slot,t))
 assert len(goals)==len(J[title]);keep=[];counts=Counter()
 for(a,p),ww in goals.items():
  row=next(r for r in J[title]if r['next_foreign']==a and r['entry']==[*xy(p),h]);assert row['C_count']==clock
  assert set(ww)=={(complex(*v['source_hook']),complex(*v['true_input']),v['physical_first_L']['context_tick0'])for v in row['input_witnesses']}
  bad=[]
  for g in sorted(field,key=lambda p:(p.real,p.imag)):
   loc=(g-p)/rot(h);f=first(a).get(loc)
   if loc in K or(f and f[0]=='R'):bad.append(dict(SAME_CURRENT=xy(g),local=xy(loc),role='ENTRY_CORE'if loc in K else'initial_WHITE',first=list(f)if f else None))
  typ='CURRENT_FIELD_CORE_WHITE'if bad else'endpoint_route';assert row['classification']==typ
  if bad:assert bad==row['conflicts']
  else:keep.append((a,p))
  counts[typ]+=1
 kept[clock]=keep;summary[clock]=dict(counts)
assert summary=={0:{'CURRENT_FIELD_CORE_WHITE':51,'endpoint_route':6},1:{'CURRENT_FIELD_CORE_WHITE':41,'endpoint_route':15}}
assert {p.imag for a,p in kept[0]}=={0,2}
for source,z in frames.items():
 assert z['p'].imag<=-4
 for a,p in kept[0]:assert p.imag>z['p'].imag
assert all(tr(W[a],0j,2)['p'].imag<0 for a in'DVU')
# Exact endpoint semigroups. S and E counts come from the real vertical
# budget; the only zero-y direction U_E is solved exactly by the x equation.
def arrangements(d,v,u):
 if d+v+u==0:return ['']
 ans=[]
 for a,cnt in [('D',d),('V',v),('U',u)]:
  if cnt:
   ns=(d-(a=='D'),v-(a=='V'),u-(a=='U'));ans.extend(a+w for w in arrangements(*ns))
 return ans
sols=[];words={};budgets=[]
for source,z in frames.items():
 ex=z['p']
 for a,p in kept[1]:
  budget=int(ex.imag-1-p.imag);num=0;assert budget<=2
  if budget>=0:
   for ds,vs,us,de,ve in product(range(budget+1),repeat=5):
    if ds+3*vs+4*us+de+ve!=budget:continue
    x=int(p.real-ex.real)+ds+vs-de-3*ve
    if x<0 or x%4:continue
    ue=x//4;num+=1;sols.append(dict(source=source,next_foreign=a,target=[*xy(p),1],S_counts=[ds,vs,us],E_counts=[de,ve,ue]))
    for b in arrangements(ds,vs,us):
     for e in arrangements(de,ve,ue):
      sec=b+'C'+e;word=source+sec+a;pose=tr(''.join(W[c]for c in word[:-1]));assert(pose['p'],pose['h'])==(p,1);words[word]=sec
  row=next(r for r in J['all30_typed_C1_endpoint_count_solutions']if r['source']==source and r['next_foreign']==a and r['target']==[*xy(p),1]);assert row['exact_vertical_budget']==budget and row['nonnegative_count_tuple_count']==num;budgets.append(budget)
normalize=lambda r:(r['source'],r['next_foreign'],tuple(r['target']),tuple(r['S_counts']),tuple(r['E_counts']))
assert sorted(map(normalize,sols))==sorted(map(normalize,J['all_C1_nonnegative_tuples']))
assert len(words)==12 and {(s[0],sec)for s,sec in words.items()}=={('B','C'),('B','DC'),('Q','CD'),('Q','DCD')}
fail=[]
for word,sec in sorted(words.items()):
 zz=tr(''.join(W[a]for a in word)+M);assert zz['bad'];t,old,q,c=zz['bad'];row=next(r for r in J['all12_C1_whole_word_immutable_conflicts']if r['word']==word);ar=row['immutable_conflict'];assert(ar['conflict_read'],ar['previous_read'],ar['turn'])==(t,old,c)
 for tick,key in [(old,'previous_owner'),(t,'conflicting_owner')]:
  off=0
  for j,a in enumerate(word):
   if tick<off+len(W[a]):assert row[key]==dict(atom_index0=j,atom=a,own_tick0=tick-off,own_read_number1=tick-off+1,turn=W[a][tick-off]);break
   off+=len(W[a])
  else:assert row[key]['next_tick0']==tick-off and row[key]['turn']==M[tick-off]
 fail.append(dict(word=word,first=t,previous=old,cell=xy(q),turn=c))
positives=[]
for row in J['all3_legal_raw_C_FOREIGN_scope_controls']:
 word=row['word'];literal=''.join(W[a]for a in word)+M;zz=tr(literal);assert not zz['bad'];seed={q for q,b in zz['req'].items()if b};assert sorted(map(xy,seed))==row['complete_seed'] and len(seed)==row['seed_mass'];board=set(seed)
 for q,h,c in zz['reads']:
  assert(q in board)==(c=='L');board.symmetric_difference_update({q})
 positives.append(dict(word=word,seed=len(seed),final=len(board),reads=len(literal)))
O=dict(status='PASS one next-FOREIGN Q/B SAME hook transfer at0/1/2 ordinary Cs only',manifest=sha(MF),script=sha(S),pose_counts=summary,C1_actual_vertical_budgets=sorted(set(budgets)),C1_complete_count_solutions=len(sols),C1_whole_word_conflicts=fail,standalone_C_FOREIGN_controls=positives,exact_C2_dependency_audit=sha(R/'audits/check_QB_two_C_hook_transfer_independent.json'),analytic_review=[
'Actual Q/B source frames and four last-R births are retained. Signed ordinary hook maturity supplies CURRENT only before the nextFOREIGN, and signed NE frontier supplies all ten NE tags through S0/E1. The shared R46 is counted once. Complete true-input interfaces include marker-only exitCORE capture; simultaneous true inputs are kept, not preemptively treated as color conflicts.',
'At C0 the exact57 true-input poses split51 held-field CORE/WHITE failures and6 heads of y0or2. Source S exits have y-4/-5 and all zero-C S bases lower y. Thus all six are impossible even with empty ordinary rail, without a depth bound.',
'At C1 the exact56 poses split41 field failures and15 endpoint labels. S rail displacement(-dS-vS,-dS-3vS-4uS), actual C displacement(0,-1), and E rail(dE+3vE+4uE,-dE-vE) yield the stated two equations. Actual vertical budgets<=2 bound all nonzero-y counts; zero-y uE is then exactly fixed by x divisibility. All nonnegative tuples and every rail ordering, including empty rails, are independently generated.',
'Only B(C),B(DC),Q(CD),Q(DCD) reach the remaining poses. All twelve complete source/section/nextFOREIGN+actualM words have immutable repeated-read witnesses with independently reconstructed RAW/marker owners. Separately allCF/CQ/CB+M prepared full boards are legal and retained. No universal C-to-FOREIGN ban or discarded wrap convention is used.',
'The lower-clock proofs join only the separately signed exactC2 theorem63c1fb62/bbf58b09, with disjoint ACTUAL ordinary C counts. Excluding all possible firstCURRENT-loss inputs leaves the SAME hooks BLACK outside the next RAWexit CORE and safe through its supplied marker. It does not execute another foreign or prove further-source transfer, resource decrease, arbitrary-tail simplicity, language entry or capture.'
]);S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
