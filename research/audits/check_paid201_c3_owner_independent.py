from pathlib import Path
from collections import Counter,defaultdict
from itertools import combinations
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'PAID201_A5_C3_UPPER_LIFETIME_OBSTRUCTION.md';C=D/'paid201_top_c3_owner_obstruction_certificate.json';assert sha(P)=='dc8e7b5f197773e2fd9058b0261f12159f33aa65b562a55ce17e26a1606d3951';assert sha(C)=='0315895e91fd5f342fd7fd9ff8ad9898361d2986778095b7876a1d29baec5188';J=json.loads(C.read_text())
for f,h in J['dependency_hashes'].items():assert sha(D/f)==h
ns={};exec(S.with_name('check_drift31_refined_top_gap_independent.py').read_text().split("for line in(P/'DRIFT31_REFINED_TOP_ODD_GAP_SHA256SUMS')")[0],ns);rk,canon,verify_rel,check_witness,oh=[ns[k]for k in('rk','canon','verify_rel','check_witness','o')]
F=json.loads((D/'open79_paid_chain201_certificate.json').read_text());events=F['events'];assert len(events)==201 and events[0]['position']==[2,1]and all(e['position']!=[5,2]for e in events);by=defaultdict(lambda:defaultdict(list))
for e in events:
 x,y=e['position'];assert e['normal_level']==3*y-x+11;by[e['normal_level']][(x,y)].append(e)
groups={t:sorted(v.values(),key=lambda g:-g[0]['position'][1])for t,v in by.items()}
for gg in groups.values():assert len(gg)==len({g[0]['position'][1]for g in gg})
assert {str(t):g for t,g in groups.items()if 27<=t<=34}==J['physical_fragment_order']['groups_used']
raw_count=0;word_count=0;tree_count=0

def domain(ih,I,out_h,O,bound,par,rel):
 global raw_count
 ans=[]
 for n in range(bound+1):
  if n%2!=par:continue
  ev=list(range(0,n,2));od=list(range(1,n,2));rr=len(ev);ll=len(od)
  zz=O-ll+I if oh(ih,0)==out_h else rr+I-O
  if zz%2:continue
  a=zz//2;b=I-a
  if not 0<=a<=rr or not 0<=b<=ll:continue
  for E in combinations(ev,a):
   for L in combinations(od,b):
    w=[(ih+2)%4]*n
    for k in E+L:w[k]=ih
    assert len(rk(w,ih))==I and len(rk(w,out_h,True))==O;raw_count+=1
    if all(x<len(rk(w,h1,True))and y<len(rk(w,h2))and rk(w,h2)[y]==rk(w,h1,True)[x]+1 for h1,h2,x,y,duration in rel):ans.append(w)
 return ans

def check_tree(p,rel):
 global tree_count
 tt=p['exhaustive_prefix_tree'];seen=set();complete=[];ih,I=p['incoming_heading_count'];out_h,O=p['outgoing_heading_count'];bound=p['derived_bound'];dm={x:y for h1,h2,x,y,L in rel};pm={y:x for x,y in dm.items()};assert len(pm)==len(dm)==len(rel)
 def visit(i,prefix):
  assert i not in seen;seen.add(i);z=tt[i];assert z['prefix']==prefix;n=len(prefix);arr=rk(prefix,ih);dep=rk(prefix,out_h,True);ni=len(arr);nj=len(dep);last=(nj-1)if n and oh(prefix[-1],n-1)==out_h else None;pending=dm.get(last)if last is not None else None
  assert z['incoming_count']==ni and z['outgoing_count']==nj and z['previous_departure_ordinal']==last and z['pending_arrival_ordinal']==pending
  valid=ni==I and nj==O and pending is None and n%2==p['required_parity'];assert z['complete']==valid
  if valid:complete.append(prefix)
  if n==bound:assert z.get('at_derived_bound')is True and not z['branches'];return
  assert len(z['branches'])==2 and{b['heading']for b in z['branches']}=={ih,(ih+2)%4}
  for b in z['branches']:
   h=b['heading'];arrival=h==ih;departure=oh(h,n)==out_h;ii=ni+arrival;jj=nj+departure;reason=None
   if ii>I or jj>O:reason='fixed_port_count_exceeded'
   elif pending is not None and(not arrival or ni!=pending):reason='forced_next_physical_return_arrival_missing'
   elif arrival and ni in pm and last!=pm[ni]:reason='forced_previous_physical_return_departure_missing'
   nxt=dm.get(nj)if departure else None
   if reason is None and nxt is not None and ii!=nxt:reason='wrong_arrival_ordinal_before_forced_return'
   if reason:assert b==dict(heading=h,pruned=reason)
   else:assert set(b)=={'heading','child'};visit(b['child'],prefix+[h])
 visit(0,[]);assert len(seen)==len(tt);assert sorted(complete)==sorted(p['complete_return_compatible_domain']);tree_count+=len(tt)

def embed(w,gg):
 ends={0};rows=[]
 for g in gg:
  start=[j for j in range(len(w)-len(g)+1)if all(w[j+k]==e['incoming_heading']and(j+k)%2==int(e['turn']=='L')for k,e in enumerate(g))];new={j+len(g)for j in start if any(z<=j for z in ends)}
  rows.append(dict(complete_physical_fragment=g,all_matching_start_ranks=start,reachable_previous_end_ranks=sorted(ends),reachable_new_end_ranks=sorted(new)));ends=new
 return bool(ends),rows
states=[{34:[0],35:[],36:[],37:[]}];counts={};total=Counter();boundmax=0
for round in J['rounds']:
 t=round['level'];assert len(states)==round['input_parent_count'];assert{canon(H)for H in states}=={canon({int(k):v for k,v in p['complete_upper_before'].items()})for p in round['parents']};nxt=[];co=Counter()
 for p in round['parents']:
  H={int(k):v for k,v in p['complete_upper_before'].items()};ih,I,out_h,O=(2,len(rk(H[t+3],2,True)),3,H[t+1].count(3))if t%2==0 else(1,len(rk(H[t+1],1,True)),0,H[t+3].count(0));bound=2*(I+O)+1;par=int(t in J['full_odd_inventory']);boundmax=max(boundmax,bound);assert p['incoming_heading_count']==[ih,I]and p['outgoing_heading_count']==[out_h,O]and p['derived_bound']==bound and p['required_parity']==par
  rel=verify_rel(H,t,p['actual_first_return_paths']);dd=domain(ih,I,out_h,O,bound,par,rel);assert sorted(dd)==sorted(p['complete_return_compatible_domain']);assert len(dd)==len({tuple(w)for w in dd});check_tree(p,rel);word_count+=len(dd)
  assert len(p['all_outcomes'])==len(dd)and{tuple(w)for w in dd}=={tuple(q['word'])for q in p['all_outcomes']}
  for oc in p['all_outcomes']:
   w=oc['word'];HH=H|{t:w};kind=oc['outcome'];co[kind]+=1
   if kind in('open','no_complete_fragment_embedding'):
    check_witness(HH,dict(outcome='open'));ok,rows=embed(w,groups.get(t,[]));assert rows==oc['complete_fragment_embedding'];assert ok==(kind=='open')
    if ok:nxt.append(HH)
   else:check_witness(HH,oc)
 counts[t]=dict(co);assert dict(co)==round['counts'];total.update(co);states=nxt
assert not states and raw_count==213073 and word_count==187 and tree_count==2038 and dict(total)==J['total_outcome_counts']and boundmax==29
out=dict(status='PASS exact supplied201 exclusion for full a5,c3 odd inventory at all periods',proof=sha(P),certificate=sha(C),script=sha(S),independent_raw_port_compatible_words=raw_count,return_compatible_words=word_count,serialized_prefix_nodes_checked=tree_count,counts=counts,greatest_derived_bound=boundmax,analytic_review=['Complete WHITE full drift(3,1), exact full odd inventory{0,1,2,6,7,19,32,34}, yields ENTIRE read maximum34 singletonN by the signed full-footprint extreme lemma. Above34 is unread; all lower<=26 remains UNKNOWN.','The observed201 factor starts2,1 and never reads5,2, so translation period P>200 without any upper cap. Canonical event clock is observed t-yP. Distinct physical fragments in one full-drift class have different integer y and are strictly ordered by decreasing y, since all observed times lie0..200. Each fragment lists all reads of that physical cell within the actual window, so no missing ranks can be inserted inside it. Gaps before/after/between distinct fragments are unrestricted.','Independent R/L position-subset inversion enumerates213073 complete port-compatible words over28 upper parents, using the count-derived n<=2(I+J)+1, not a multiplicity cutoff. Exact physical return paths reduce this domain to187, equal to the serialized2038-node trees. Every binary branch, pruning reason, pending ordinal, complete leaf and derived-bound termination was also checked.','Every skipped-rank physical path and positive clock cycle independently reconstructed with full drift lifts. For graph-open words, every fragment start rank and exact gap-allowing reachable-end DP is independently reproduced. T27 leaves50 skips,24 positive cycles and11 empty DPs, no unresolved branch.','Earlier prepared BLACK input is not by itself forbidden. Contradiction is failure of complete WHITE histories to own all actual lifted read fragments. Only this supplied201 factor under exact a5,c3 inventory is excluded. The finite factor, every other a5 factor, larger-a embeddings, remaining controller classification and global attraction are not closed.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
