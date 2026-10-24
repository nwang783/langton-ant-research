from pathlib import Path
from itertools import product,combinations
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();files={'RR3_stock_gates_cannot_immediately_feed_the_even_LL_portal.md':'b0f027c8e5fb65f2adcf4346e5078e92146b51708f2b0715546257fcb92a03e6','check_RR3_stock_to_even_LL_portal.py':'a6ec54f5','check_RR3_stock_to_even_LL_portal.json':'8024c146','global_max_one_to_two_crossing_launch_has_an_odd_witness.md':'69be3b518aa313a38ef6a2e4ab4fc981e290118fe6c49dc559de5bc25c3c77fd','RR3_to_even_portal_runs_require_a_singleton_RIGHT.md':'3ad98724dcfbcf68c00ad6defcfcb4f43a9c69f93ab82c77285f7d2b7d55a3c8'}
for f,h in files.items():assert sha(D/f).startswith(h)
H='NESW';V=(1j,1,-1j,-1);xy=lambda p:[int(p.real),int(p.imag)];out=lambda w,r:H[(H.index(w[r])+(1 if r%2==0 else-1))%4]
J=json.loads((D/'check_RR3_stock_to_even_LL_portal.json').read_text());rows={(z['portal_Y'],z['incoming_LEFT_q'],z['C'],z['upstream_LEFT_z'],z['shared_reader_D']):z for z in J['rows']};stats=Counter();paths=[]
profiles=[('EWW','EEW','SSN','NNS'),('EWW','EEWE','SSNS','NNSN'),('EWWE','EEW','SSNN','NNS')]
for Y,q,C,z in profiles:
 for n in range(5):
  for bits in product('EW',repeat=n):
   dw=''.join(bits);hs={1+1j:'SN',1j:Y,0j:'NNSS',1+0j:'EE',1+2j:q,2j:C,2+2j:'SSNS',2+3j:'EWWW',1+3j:z,3j:dw};row=rows[Y,q,C,z,dw];su={};bad=[]
   for p,w in hs.items():
    for hh,dd in zip(H,V):
     if p+dd not in hs:continue
     aa=[r for r in range(len(w))if out(w,r)==hh];bb=[r for r,v in enumerate(hs[p+dd])if v==hh]
     if len(aa)!=len(bb):bad.append(dict(source=xy(p),direction=hh,source_ranks=aa,target=xy(p+dd),target_ranks=bb))
     else:su.update({(p,a):(p+dd,b)for a,b in zip(aa,bb)})
   if bad:assert row['result']=='port'and row['certificate']in bad;stats['port']+=1;continue
   assert row['result']=='rank';path=[(complex(*p),r)for p,r in row['certificate']['path']];assert all(su[a]==b for a,b in zip(path,path[1:]))and path[-1][0]==path[0][0]and path[-1][1]!=path[0][1]+1
   assert all(p!=path[0][0]for p,r in path[1:-1]);stats['rank']+=1;paths.append(dict(Y=Y,q=q,C=C,z=z,D=dw,path=[[xy(p),r]for p,r in path],length=len(path)-1))
assert len(rows)==93 and stats=={'port':79,'rank':14}and Counter(p['length']for p in paths)=={16:13,4:1}
for Y,q,C,z in profiles:
 ws={r['D']for r in paths if r['Y']==Y and r['q']==q};assert ws==({'EWW','WWE','EEWW','EWWE','WEEW','WWEE'}if q=='EEW'else{'EWWW','WWEW'})
# No absent portal cells used: derive the four uncapped C count cases from first SS and GLOBAL M.
counts={};triples=[]
for Y,q in product(['EWW','EWWE'],['EEW','EEWE']):
 k=sum(out(Y,r)=='N'for r in range(len(Y)));l=q.count('E');sol=[]
 for a in range(k+1):
  for eps in(0,1):
   b=k-a;t=l-a;c=k+l-3*a+eps
   if min(b,t)<0 or c<1 or c>a:continue
   n=a+b+c+t;assert n==2*(a+c)-eps
   for rn in combinations(range(0,n,2),a):
    for ln in combinations(range(1,n,2),b):
     nn=set(rn)|set(ln);word=''.join('N'if i in nn else'S'for i in range(n))
     if not word.startswith('SS'):continue
     assert word.count('N')==k and sum(out(word,r)=='E'for r in range(n))==l;sol.append((a,c,eps,word));triples.append((Y,q,word))
 counts[f'{k},{l}']=sol
assert sorted(triples)==sorted((Y,q,C)for Y,q,C,z in profiles)
# First-port source/root chronology depends on optional source R2 neither at Y nor C.
for B in['SN','SNN']:
 assert[ r for r,h in enumerate(B)if h=='S']==[0]and[ r for r in range(len(B))if out(B,r)=='W'][0]==0
 for Y in['EWW','EWWE']:
  assert Y.index('W')==1 and next(r for r in range(len(Y))if out(Y,r)=='N')==2
# Cross-type/rotation witness recovery and exact two-LEFT mixed-run contradiction.
recover=[]
for r in range(4):
 rot=(-1j)**r
 for shift in[0j,13-7j,-9+4j]:
  B=(1+1j)*rot+shift;y=1j*rot+shift;q=(1+2j)*rot+shift
  assert y+rot==B and q-1j*rot==B
  yword=''.join(H[(H.index(c)+r)%4]for c in'EWW');qword=''.join(H[(H.index(c)+r)%4]for c in'EEW');assert(H.index(yword[1])-H.index(yword[0]))%4==2 and qword[1]==qword[0];recover.append((r,xy(shift)))
for q in['EEW','EEWE']:
 for t in['SSN','SSNS']:
  p='WWEW';assert out(q,0)=='S'and out(t,0)=='W'and out(p,0)=='N';assert p.count('E')==1 and all(out('SN',r)!='E'for r in range(2))
# Bind already signed scopes, not the author discovery imports.
deps={f:sha(R/'audits'/f)for f in['check_even_portal_entry_odd_independent.json','check_one_use_capped_flow3_independent.json','check_one_use_input_flow3_v2_independent.json','check_cap_free_endpoint_domains_independent.json']}
O=dict(status='PASS exact immediate RR3-to-even-portal obstruction; separate cap-free GLOBAL-M one-to-two launch injection; dependent singleton-link reservation',files={f:sha(D/f)for f in files},dependencies=deps,script=sha(S),all93_summary=stats,all14_actual_physical_paths=paths,four_complete_uncapped_count_cases=counts,rotation_recovery_controls=recover,analytic_review=[
'For the exact immediate join, signed even-portal entry gives all three complete(Y,q,C) rows. The preceding one-use-cappedRR3 gate has exactly matched outerLEFT3/3 or4/4 histories and the displayed SSNS/EWWW RIGHTs. They fix nine physical cells; the sole corner D has every empty/length1..4 completeEW history retained. All93 products are rebuilt,79 exact completeport mismatches and14 literal actual next-rank failures, without clock/height/side/age filtering. Every displayed successor step is fixed by physical same-direction ordinal matching. A full-drift identification cannot change the same physical start/end rank contradiction.',
'The localized one-to-two theorem needs only consecutive sourceB=SN/SNN and rootY=EWW/EWWE plus its independently supplied GLOBAL-M sectors. q firstE arrival/R0 supplies B uniqueS and Y firstW/L1. Hence C firstEout=Y1-3 while CfirstNin=Y2+1; completeWHITE forces CstartsSS. A RIGHT q would require C firstR departE, but it departsW, so qLEFT at arbitrary multiplicity. No Z/A or outgoing sink is used.',
'Y equalC sectors identify q firstR SW and C oppositeSE withM. Only this independent maximum activates the signed cap-free outputone endpoint bound q=E/EE/EEW/EEWE. LEFT removes E/EE. Exact four(k,l) integercases with CstartsSS and R_S-R_N<=0 give precisely SSN/SSNS/SSNN and no evenY/evenq. This is a derived finite domain, not an exteriorcap or universal firstRmax rule.',
'Odd rootY and odd predecessorq are rotation-distinguished by opposite versus same R0/L1 headings. Each recovers unique launchB physically and full-drift equivariantly. The reservation is the SAME injection as the earlier portal result, not an additional count; optional sourceSNN is not separately charged.',
'For a maximal flow1 run from a one-use-cappedRR3 sink to an exact evenSN/EE portal, zero internalvertices would put a RIGHT sink at q, already forbidden. If there is no internalRIGHT singleton, noLLL on the embedded essential b-circle leaves1or2LEFTs. One is the just-excluded immediatejoin. Two force qEEW/EEWE,tSSN/SSNS,pWWEW at the displayed distinct physical lifts; p requiresEin1 from portalB SN, whose Eout0 is a literal contradiction. Thus an internalRIGHTsingleton exists. Different maximalrun classes on one actual b-circle are disjoint, reserving distinct one-read outputs, distinct by complete multiplicity from the existing three-read evenportal witness. Only these specifically disjoint capacities add; no originalfuel or transferlengthbound follows.',
'No standalone gate, preparedF48/F49 factor, longer singleton-bearing connector, uncapped D mixedjoin, all-cap crossing classification, controller or global capture is excluded.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(stats,counts);print(sha(S.with_suffix('.json')))
