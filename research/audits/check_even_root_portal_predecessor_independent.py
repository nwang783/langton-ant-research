from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib,ast
S=Path(__file__).resolve();R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files={'even_root_even_endpoint_LL_portals_have_no_incoming_b_predecessor.md':'f85ae1142b0057277d608847f200d26acd4def8c87bb07c07a0b895e5da7e893','check_even_root_portal_incoming_predecessor.py':'9360da16951d0d73a20c939736e17789139b17439a0a628c0013311d2d528184','check_even_root_portal_incoming_predecessor.json':'aa9bc25577424aa72c9f1610a92416a889be2365b7507c14ed5a15d465618d77'}
for f,h in files.items():assert sha(D/f)==h
J=json.loads((D/'check_even_root_portal_incoming_predecessor.json').read_text())
lib=S.with_name('check_terminal_LL_portal_suppliers_independent.py');ns={'__file__':str(lib)};exec(lib.read_text().split('loc=[];lc=Counter()')[0],ns)
V,out,cv,string,NS,EW,test,dom,prop,cin,cout,key=[ns[k]for k in('V','out','cv','string','NS','EW','test','dom','prop','cin','cout','key')]
lib2=S.with_name('check_terminal_LL_upper_completion_independent.py');ns2={'__file__':str(lib2)};exec(lib2.read_text().split('ct1=Counter()')[0],ns2);verify_cert=ns2['verify_cert']
shift=lambda hs:{p-1-1j:w for p,w in hs.items()};mapping={'skipped':'rank','global_max':'higher_C'}
code=lambda hs:tuple((int(p.real),int(p.imag),string(w))for p,w in sorted(hs.items(),key=lambda z:key(z[0])))
vs=[w for w in EW if w and out(w,0)==0 and len(cout(w,0))==1];assert list(map(string,vs))==J['predecessor_complete_domain']==['W','WW','WWE','WWEW']
# q's other geometrical predecessor would be its north neighbor C; C first R goes north, away.
assert out(cv('WWEE'),0)==0 and out(cv('SSN'),0)==3
local={};modes=[];lr={(r['v'],r['X'],r['H']):r for r in J['local_nonport_rows']};seen=set();heights=[];localpaths=Counter();localclocks=Counter()
for v in vs:
 ct=Counter()
 for x,h in product(NS,EW):
  hs={1:v,1+1j:cv('SSN'),2:x,2+1j:h};ans,wit=test(shift(hs));typ=mapping.get(ans,ans);ct[typ]+=1;k=tuple(map(string,(v,x,h)))
  if typ!='port':
   assert k in lr and lr[k]['result']==typ;seen.add(k);z=verify_cert(shift(hs),lr[k])
   if typ=='rank':localpaths[z]+=1
   elif typ=='clock':localclocks[z]+=1
   elif typ=='higher_C':heights.append([k,wit])
  if typ=='open':modes.append((v,x,h))
 local[string(v)]=dict(ct)
assert local==J['local_counts']and seen==set(lr)and set(tuple(map(string,z))for z in modes)==set(map(tuple,J['local_modes']))
ref={code({complex(*ast.literal_eval(p)):cv(w)for p,w in r['histories'].items()}):r for r in J['closure_rows']};seen=set();ct=Counter();profiles=Counter();paths=Counter();incidence=[];upper=[];closures=[]
for v,x,h in modes:
 fixed={1:v,1+1j:cv('SSN'),2:x,2+1j:h,1j:cv('WE'),2j:cv('SNNS'),-1+2j:cv('EEWW'),-1+1j:cv('SS'),1+2j:cv('WWEE')};pts=set(fixed)
 while True:
  add={p+z for p in pts for z in V}-pts;add={q for q in add if sum(q+z in pts for z in V)>=2}
  if not add:break
  pts|=add
 assert pts-set(fixed)=={-1+0j,0j,2+2j}
 def rec(ds):
  ds=prop(ds)
  if ds is None:return
  free=[p for p in ds if len(ds[p])>1]
  if free:
   p=min(free,key=lambda p:(len(ds[p]),key(p)))
   for z in ds[p]:rec(ds|{p:[z]})
   return
  hs={p:ws[0]for p,ws in ds.items()};k=code(hs);assert k not in seen;seen.add(k);ans,wit=test(shift(hs));typ=mapping.get(ans,ans);ct[typ]+=1;assert ref[k]['result']==typ
  z=verify_cert(shift(hs),ref[k])
  if typ=='rank':paths[z]+=1
  elif typ=='higher_C':closures.append(wit)
  elif typ=='open':
   profiles[tuple(map(string,(v,x,h)))]+=1
   # Exhaust every physical possible b predecessor of v, respecting its incoming axes/zero ports.
   candidates=[]
   for hin in set(v):
    p=1-V[hin];assert p in hs
    if out(hs[p],0)==hin:candidates.append(p)
   if string(v)in('W','WW'):
    assert set(v)=={3}and candidates==[]and string(x)in('NSSS','NNS','NNSS')and out(x,0)==1
    incidence.append(k)
   else:
    assert string(hs[-1+2j])=='EEWW'and string(hs[2j])=='SNNS'and string(hs[1+2j])=='WWEE'and string(hs[2+2j])in('SNN','SNNS');upper.append(k)
 rec({p:[fixed[p]]if p in fixed else dom(p)for p in pts})
assert seen==set(ref)and dict(ct)==J['closure_counts']==dict(rank=358,higher_C=6,open=30)
assert len(incidence)==12 and len(upper)==18
assert {str(k):n for k,n in profiles.items()}==J['open_profiles']
# Both transfers of maximum height use actual balanced opposite R counts, not arbitrary first-R maxima.
for w,aa,bb in [('SSN',2,0),('WWEE',3,1)]:
 c=cv(w);assert sum(c[i]==aa for i in range(0,len(c),2))==sum(c[i]==bb for i in range(0,len(c),2))
upper_report=S.with_name('check_terminal_LL_upper_completion_independent.json');assert sha(upper_report)=='b80c7a3800f7547cc23e31d20ba62e1554fefbbd902e564a7169d93aa75a5b07'
report=dict(status='PASS scoped complete-WHITE GLOBAL-M cap4 exclusion of exact even-root two-read-endpoint LL portal',bindings=files,first_square=local,complete_predecessors=list(map(string,vs)),local_rank_lengths=dict(localpaths),local_clock_weights=dict(localclocks),local_higher_C=heights,closure=dict(ct),closure_rank_lengths=dict(paths),closure_higher_C=closures,open_profiles={str(k):n for k,n in profiles.items()},no_b_predecessor_networks=len(incidence),signed_upper_completion_networks=len(upper),signed_upper_report=sha(upper_report),analytic_review=[
'The supplied prior entry-incidence theorem forces q=SSN and C=WWEE in this rotated exact even portal. A b-predecessor of q could geometrically use either its S or N arrival, but C north of q first-departs N away. Thus actual cyclic predecessor is south v, first-departing N; q has exactly one N input. Every complete WHITE cap4 v is W,WW,WWE,WWEW, with no presumed LEFT/RIGHT or incoming multiplicity.',
'The selected maximum is the physical C face bottom-left F=(1,0), so independent test translates ALL cells by(-1,-1) to its canonical anchor(0,-1). Opposite face(0,-1) in the original frame is NEVER assumed maximal for W/WW. q SSN has balanced R_S/R_N and transports the known portal maximum to F.',
'Independent full products4*31*31 produce exactly28 modes and independently verify every stored local wrong-rank/positive-clock witness. Count propagation uses both directed edges and all zero ports. Three geometric two-neighbor corner additions are derived, not chosen by radius.',
'All394 complete closure histories independently reconstructed and matched by full physical words.358 literal same-physical-cell next-rank failures,6 GLOBAL-M contradictions and30 open local networks. No period, lifetime, critical K or fuel condition is used.',
'Every W/WW survivor has only W arrivals at v; its only possible physical b predecessor is east X. Every X first R is N and departs E away from v, so there is no b predecessor. Translated full-drift aliases preserve the same local departure and cannot supply the missing physical edge.',
'Every other survivor contains the exact four histories of signed65df upper-side completion. Balanced C WWEE transports the known portal M sector to the upper Q sector; independently signed b80c upper-reader cover eliminates all18. No assumption about v side, age, or owner is needed.',
'The conclusion is only this specified even-root/two-read-endpoint portal in complete WHITE cap4 GLOBAL-M essential b-circle scope, at any incoming mixed-link length and any critical index. Odd-root EWW, changed endpoint roles, nonmaximum/higher-cap curves and prepared finite F48/F49/F84/F85 remain outside. Weaker local networks remain valid without full completion. No whole-front/classification/fuel theorem follows.'
])
S.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print(report['status']);print(sha(S.with_suffix('.json')));print(ct,profiles)
