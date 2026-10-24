from pathlib import Path
from itertools import product
from collections import Counter
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'PAID201_A5_C5_UPPER_LIFETIME_OBSTRUCTION.md';C=D/'paid201_top_c5_owner_obstruction_certificate.json';assert sha(P)=='09c11d3cfc428b7a1b951085d0fed05db344d73e4a7f747a9c13afbd038f3351';assert sha(C)=='96922c82036dbdc569a5ca7933303a8c94eac6fd36c545e6eb1dfa4af0261f3b';J=json.loads(C.read_text())
for f,h in J['dependency_hashes'].items():assert sha(D/f)==h
ns={};code=S.with_name('check_drift31_refined_top_gap_independent.py').read_text();exec(code.split("for line in(P/'DRIFT31_REFINED_TOP_ODD_GAP_SHA256SUMS')")[0],ns);rk,canon,verify_rel,check_witness=[ns[k]for k in('rk','canon','verify_rel','check_witness')]
records=J['records'];used=set();states=[{34:[0],35:[],36:[],37:[]}];counts={};bounds=[]
for t in range(33,28,-1):
 nxt=[];co=Counter()
 for H in states:
  idx=[i for i,r in enumerate(records)if r['level']==t and canon({int(k):w for k,w in r['complete_upper_before'].items()})==canon(H)];assert len(idx)==1;i=idx[0];assert i not in used;used.add(i);r=records[i]
  ih,I,oh,O=(2,len(rk(H[t+3],2,True)),3,H[t+1].count(3))if t%2==0 else(1,len(rk(H[t+1],1,True)),0,H[t+3].count(0));bound=2*(I+O)+1;par=int(t in{31,32,34});assert r['incoming_heading_count']==[ih,I]and r['outgoing_heading_count']==[oh,O]and r['derived_bound']==bound and r['required_parity']==par;bounds.append(bound)
  rel=verify_rel(H,t,r['actual_first_return_paths']);dd=[]
  for n in range(bound+1):
   if n%2!=par:continue
   for hs in product((t%2,t%2+2),repeat=n):
    if len(rk(hs,ih))==I and len(rk(hs,oh,True))==O:dd.append(hs)
  assert len(dd)==len(set(dd))and set(dd)==set(map(tuple,r['complete_domain']));assert len(r['outcomes'])==len(dd)and{tuple(o['word'])for o in r['outcomes']}==set(dd)
  for o in r['outcomes']:
   w=o['word'];kind=o['outcome'];co[kind]+=1
   if kind=='first_return_rank':
    z=o['witness'];p=r['actual_first_return_paths'][z['path_index']];sr=rk(w,p['outgoing_heading'],True)[p['outgoing_ordinal']];dst=rk(w,p['incoming_heading'])[p['incoming_ordinal']];assert dst!=sr+1 and z['source_rank']==sr and z['target_rank']==dst and z['required_target_rank']==sr+1
   else:
    assert all(rk(w,h2)[b]==rk(w,h1,True)[a]+1 for h1,h2,a,b,L in rel);HH=H|{t:w};check_witness(HH,o)
    if kind=='open':nxt.append(HH)
 counts[str(t)]=dict(co);states=nxt
assert len(used)==len(records)and counts==J['counts']and len(states)==8
upper=[]
for H in states:
 w=H[29];block=[j for j in range(len(w)-3)if j%2==1 and w[j:j+4]==[3,3,3,1]];assert not block or block==[1];assert all(not[k for k in range(j)if k%2]for j in block);upper.append(dict(T30=''.join('NESW'[h]for h in H[30]),T31=''.join('NESW'[h]for h in H[31]),T29=''.join('NESW'[h]for h in w),block=block))
assert sum(bool(x['block'])for x in upper)==2
# The signed literal201 factor supplies actual complete physical fragments, not guessed BLACK inputs.
F=json.loads((D/'open79_paid_chain201_certificate.json').read_text());events=F['events'];q=-3+5j;p=q+3+1j
for pt,expected in[(p,[(87,3,'L')]),(q,[(93,3,'L'),(105,3,'R'),(109,3,'L'),(117,1,'R')])]:assert [(e['time'],e['incoming_heading'],e['turn'])for e in events if complex(*e['position'])==pt]==expected
assert[o['owner_R_time']for o in F['all_L_lifetime_owners']if o['time']in(87,93)]==['initial BLACK','initial BLACK'];assert int(3*q.imag-q.real+11)==29
out=dict(status='PASS exact supplied201 exclusion at full a=c=5 odd inventory; uniform stated-top-parity rank lemma',proof=sha(P),certificate=sha(C),script=sha(S),complete_counts=counts,derived_bounds=bounds,eight_open_interfaces=upper,analytic_review=['In a complete WHITE full(3,1) front with the vertical-even sector, the maximum of the ENTIRE actual read footprint is even singletonN, hence equals the highest full odd level34 for the exact supplied inventory. Only levels35..37 are setempty; all omitted lowerlevels<=28 remain UNKNOWN. This is not a black-field or cropped-wake extremum.','For even newlevel exact upper SinI/WoutJ gives floor(n/2)=I+J-2a. For odd E-inI/NoutJ gives ceil(n/2)=I+J-2b. Therefore n<=2(I+J)+1 is complete and derived. Independent binary-word enumeration reproduces every complete parity-constrained domain, including empty when permitted, without using the author subset generator.','All upper same-PHYSICAL-cell return paths and full voltages were independently reconstructed. Every121 explicit return rejection, five skipped-rank paths and four positive clock cycles atT29 was verified, along with all earlier57 T30 cases. Eight necessary OPEN upper interfaces remain; no exterior completion is claimed.','The W/L,W/R,W/L,E/R physical block can occur only at complete rank1 in EWWWEWWE. Thus there is no earlier L rank of ANY heading. The factor provides q+d W/L at87 and consecutive q block93/105/109/117. Full translation implies an actual q W/L at87-P<93 for every positive P, contradicting complete-rank firstness. Prepared BLACK is not rejected by itself; its observed full-drift owner is the constraint.','The general rank lemma depends only on the stated six top parities odd/even/odd/odd/even/even and complete-read maximum. Its application excludes only the given201 factor with FULL odd inventory{0,1,2,6,7,31,32,34}. It does not exclude all c=a fronts, a5c3, largerparameters, arbitrary controllers or global attraction, and does not retract the genuine finite factor.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
