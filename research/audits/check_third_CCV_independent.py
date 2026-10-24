from pathlib import Path
from fractions import Fraction
import json,hashlib,itertools
R=Path('/workspace/shared/langton');P=R/'third_atom_CCV_adversarial_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=P/'manifest.json';assert sha(mf)=='b0e212783f240e2e9b36855863100aaed577e37f236827e0578f08db8b83c44a';MNF=json.loads(mf.read_text())
for f,h in MNF['files'].items():assert sha(P/f)==h
for f,h in MNF['dependencies'].items():assert sha(R/f)==h
p=R/'audits/check_old_V_second_age1_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('# Universal')[0],ns)
W,M,K,tr,pieces,meet,xy,V=[ns[k]for k in ['W','M','K','tr','pieces','meet','xy','V']];J=json.loads((P/'CCV_targets.json').read_text());out=[]
def full_replay(word,seed,cut):
 B=set(seed);p=0j;h=0;state=None
 for i,ch in enumerate(word):
  actual='L'if p in B else'R';assert actual==ch
  if p in B:B.remove(p)
  else:B.add(p)
  h=(h+(1 if actual=='R'else-1))%4;p+=V[h]
  if i+1==cut:state=(p,h,B.copy())
 return p,h,B,state
for a in'FQB':
 toks=a+'CCV';seg=pieces(toks);geo=next(q for q in J['exact_all_pairwise_proxy_geometries']if q['foreign']==a)
 assert [xy(seg[0][0])]+[xy(s[1])for s in seg]==geo['actual_doubled_vertices']
 non=[]
 for i,j in itertools.combinations(range(len(seg)),2):
  hit=meet(*seg[i],*seg[j])
  if j==i+1:assert hit==(1,0)
  elif hit is not None:non.append((i,j,hit))
 if a=='F':assert non==[(0,3,(Fraction(3,4),Fraction(3,4)))]and seg[0][0]+Fraction(3,4)*(seg[0][1]-seg[0][0])==-5.5-2.5j
 else:assert non==[]
 word=''.join(W[t]for t in toks)+M;T=tr(word);row=next(q for q in J['exact_literal_complete_and_partial_controls']if q['tokens']==list(toks));rawlen=len(word)-len(M)
 if a=='B':
  assert T['bad']is None;seed={q for q,b in T['req'].items()if b};assert len(seed)==24 and K<=seed and sorted(map(xy,seed))==row['complete_initial_BLACK']
  p,h,B,state=full_replay(word,seed,rawlen);z=row['actual_complete_physical_control'];assert len(word)==133 and [*xy(p),h]==z['exit_pose']==[-1,-2,3]and len(B)==z['mass']==39 and sorted(map(xy,B))==z['complete_BLACK'];pp,hh,BB=state
  assert [*xy(pp),hh]==z['RAW_cut']['pose']==[-1,-3,0]and len(BB)==40 and sorted(map(xy,BB))==z['RAW_cut']['complete_BLACK']
  out.append((a,'actual complete positive',24,133))
 else:
  fail,prev,q,ch=T['bad'];assert (fail,prev,q,ch)==((101,45,-1+0j,'R')if a=='F'else(118,46,-1-1j,'R'))
  pref=tr(word[:fail]);seed={q for q,b in pref['req'].items()if b};assert sorted(map(xy,seed))==row['complete_initial_BLACK_for_exact_feasible_prefix']
  pp,hh,BB,state=full_replay(word[:fail],seed,rawlen);assert pp==q and q in BB and sorted(map(xy,BB))==row['actual_feasible_prefix']['complete_BLACK']and [*xy(pp),hh]==row['actual_feasible_prefix']['exit_pose']
  assert row['third_RAW_completed_before_failure']==(fail>=rawlen)
  own=row['failing_actual_owner'];assert(own['canonical']['context_tick0'],own['canonical']['owner_read_number1'])==(15,16)if a=='F'else(own['next_word_tick0'],own['next_word_read_number1'])==(6,7)
  out.append((a,'immutable conflict',fail,prev,xy(q)))
tokens='UBCCV';word=''.join(W[t]for t in tokens)+M;T=tr(word);assert T['bad']==(145,1,-1+0j,'L');reads=[(i,ch)for i,(p,h,ch)in enumerate(T['reads'])if p==-1];assert reads[:2]==[(1,'L'),(145,'L')]
assert 145-sum(len(W[t])for t in'UBCC')==13
report={'status':'PASS exact prescribed A,C,C,V targets and complete prepared B control; no genuine oldG8 FIRST-B lift','manifest_sha256':sha(mf),'script_sha256':sha(Path(__file__)),'controls':out,'forced_UBCCV_deleted_cell_reads':reads,'analytic_scope':['F intended third V crosses real foreign prefix at3/4 but literal word fails before V completes, so intended chord is not actual.','Q completes RAW but fails final actual M tick6/read7; cannot be promoted to an actual recognized third ordinary context.','B complete24-black133-read prepared control has simple local proxy and full fields preserved. Signed completeG8/FIRST-B adjacency forces immediate PLAIN U, not arbitrary raw predecessor. The fixed UBCCV suffix has consecutive L requests at source U1 and thirdV13 with no read/rebirth between; no earlier field or longer prefix can repair it.','No general third-RAW simplicity, attained third-contact counterexample, arbitrary ancestry search or capture follows.']}
p=R/'audits/third_CCV_independent.json';p.write_text(json.dumps(report,indent=2)+'\n');print(sha(p));print(report['status'])
