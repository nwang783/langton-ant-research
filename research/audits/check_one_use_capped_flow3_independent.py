from pathlib import Path
from itertools import combinations,product
from collections import Counter
import ast,json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'one_use_capped_flow3_segments_are_RR_stock_gates.md';JF=D/'check_one_use_capped_flow3_gates.json';assert sha(P)=='fb98672870c12633db3d483200ea0b73a89d357b3bb616204a7c6f3a3770e6f5'and sha(JF).startswith('4b6f34a1')and sha(D/'check_one_use_capped_flow3_gates.py').startswith('189244da');J=json.loads(JF.read_text());assert sha(D/'mixed_RR_boundary_closure_and_required_flat_RIGHT_exits.md').startswith('f008184d')
ns={'__file__':str(S.with_name('check_global_max_flow2_staircase_independent.py'))};exec(Path(ns['__file__']).read_text().split('rows=[];stats=Counter()')[0],ns);cv,V,out,test=[ns[k]for k in('cv','V','out','test')];xy=lambda p:[int(p.real),int(p.imag)]
def network(hs):
 su={};pre={};events={(p,r)for p,w in hs.items()for r in range(len(w))}
 for p,w in hs.items():
  for h,v in enumerate(V):
   if p+v not in hs:continue
   a=[r for r in range(len(w))if out(w,r)==h];b=[r for r,hh in enumerate(hs[p+v])if hh==h];assert len(a)==len(b)
   for r,s in zip(a,b):su[p,r]=(p+v,s);pre[p+v,s]=(p,r)
 return events,su,pre

def calendar(row):
 hs={complex(*ast.literal_eval(p)):cv(w)for p,w in row['histories'].items()};assert test(hs)[0]=='open';ev,su,pre=network(hs);tt={(complex(*ast.literal_eval(k)[0]),ast.literal_eval(k)[1]):t for k,t in row['distinct_mod4_calendar'].items()};assert set(tt)==ev and len(set(tt.values()))==len(ev)==row['events'];cs=[];used=set()
 for e in sorted(ev-set(pre),key=lambda e:(e[0].real,e[0].imag,e[1])):
  path=[];f=e
  while True:
   assert f not in used;used.add(f);path.append(f)
   if f not in su:break
   f=su[f]
  cs.append(path)
 assert used==ev and [[[xy(p),r]for p,r in c]for c in cs]==row['components'];order=row['component_order'];assert sorted(order)==list(range(len(cs)))and all(tt[cs[a][-1]]<tt[cs[b][0]]for a,b in zip(order,order[1:]))
 for e,f in su.items():assert tt[f]==tt[e]+1
 for p,w in hs.items():
  x,y=map(int,(p.real,p.imag));ph=2*(x%2)if(x+y)%2==0 else 3-2*(x%2)
  for r in range(len(w)):
   assert tt[p,r]%4==ph
   if r:assert tt[p,r]-tt[p,r-1]>=4
 assert row['odd_classes']==sum(len(w)%2 for w in hs.values());return hs,su,tt
rr=[]
for row in J['RR_two_complete_controls']:
 hs,su,tt=calendar(row);path=[(complex(*p),r)for p,r in row['actual_RRRR']];assert all(su[a]==b for a,b in zip(path,path[1:]))and ''.join('RL'[r%2]for p,r in path[:-1])=='RRRR'and path[-1]==(0j,1)and tt[path[-1]]-tt[path[0]]==4;assert su[-1j,1]==(0j,0)
 if len(hs[0j])==4:assert su[-1j,3]==(0j,3)
 rr.append(dict(events=len(tt),components=len(row['components']),odd=row['odd_classes']))
# Every pair of cap-free flow1 LEFT endpoint words is tested, not just the two positives.
for z,y in product(['NNS','NNSN'],['EEW','EEWE']):
 hs={0j:cv(z),1+0j:cv('EWWW'),1-1j:cv('SSNS'),-1j:cv(y)};assert(test(hs)[0]=='open')==(len(z)==len(y))
base={1+1j:cv('SNNN'),1j:cv('EWWW'),0j:cv('SSNS')};domain={};stats=Counter();shield=[]
for a in range(1,4):
 for eps in(0,1):
  n=4*a-eps;b=3-a
  if b<0:continue
  for er in combinations(range(0,n,2),a):
   for el in combinations(range(1,n,2),b):
    E=set(er)|set(el);w=''.join('E'if r in E else'W'for r in range(n));hs=base|{1+0j:cv(w)};assert w.count('E')==3 and sum(out(hs[1+0j],r)==0 for r in range(n))==3
    row=next(z for z in J['RLR_uncapped_reader_count_derived_domain']if z['D']==w);ans,wit=test(hs)
    if row['result']=='rank':
     assert ans=='skipped';ev,su,pre=network(hs);path=[(complex(*p),r)for p,r in row['certificate']['path']];assert all(su[x]==y for x,y in zip(path,path[1:]))and path[0][0]==path[-1][0]and path[-1][1]!=path[0][1]+1
    else:assert row['result']=='open' and ans in ('open','clock');shield.append(w)
    if n<=4:
     assert w in['EEWE','WEEE'];ev,su,pre=network(hs);path=[(0j,3),(1+0j,3),(1+1j,3),(1j,3),(0j,3)];assert all(su[x]==y for x,y in zip(path,path[1:]))
    assert w not in domain;domain[w]=row['result'];stats[row['result']]+=1
assert len(domain)==84 and stats==J['RLR_summary']==dict(rank=78,open=6)and set(shield)==set(J['RLR_open_reader_words'])
full=[]
for row in J['full_six_cell_reader_controls']:
 hs=base|{1+2j:cv(row['q']),2j:cv(row['C']),1+0j:cv(row['D'])};ans,wit=test(hs)
 if row['result']=='open':calendar(row);assert ans=='open';full.append(dict(q=row['q'],C=row['C'],D=row['D'],events=row['events'],odd=row['odd_classes']))
 else:assert row['result']=='clock_cycle'and ans=='clock'and sum(e[2]for e in wit)>0
assert len(full)==4 and sum(z['odd']==0 for z in full)==1 and len(J['full_six_cell_reader_controls'])==12
O=dict(status='PASS GLOBAL-M cap4 one-use-capped flow3 RR classification and scoped uncapped-reader controls',proof=sha(P),certificate=sha(JF),script=sha(S),RR_controls=rr,count_derived_reader_summary=stats,uncapped_local_controls=full,analytic_review=[
'Signed f008 section2 explicitly retains one-use endpoint rerouting in the GLOBAL-M maximal-flow3 reduction to RR/RLR; only its later lane/critical consequences require no-one-use. Thus its all-length template reduction applies here, without importing that later restriction.',
'One-use source1to3 and sink3to1 have complete4-read words fixed by signed endpoint domains. RLR square readerEin3/Nout3 under cap4 has onlyEEWE/WEEE, whose third ordinals form an actual SAMEphysicalL3 four-eventcycle. No voltage, exterior connector or period can fix that cycle.',
'In RR, preceding/following b vertices mustLEFT because a thirdRIGHT closes a contractible square. ConstantselectedC makes theirflow1; cap-freeLEFT domains and all four endpoint combinations leave precisely3/3 or4/4. Actual fourR firstreturn and retained oldL1/L3 edges are independently reconstructed; calendars keep all14/16 events, zeroports and open endpoints.',
'Without readerDcap, exact counts give R_E=R_W=a, n=4a-epsilon<=12. Independent even/odd position generation covers84 completehistories,78 literalrankfailures and6 necessary7/8-read balanced-C shields. The six are rank-only survivors; four already have positive clock cycles in the four-cell core, conservatively retained until the author six-cell clock test. GLOBALM alone does not remove the balanced-height alternatives. Complete six-cell knownports leave4 distinct event-disjoint calendars, while8 get explicit positiveclockcycles.',
'The cap-free first-port C-startsSS argument still excludesRIGHT q at the source3 interface. The optional six-cell controls nevertheless impose the displayed q/C histories and do not supply actual exterior paths or full drift voltages. No localcalendar is promoted to a factor/controller; no general one-use coverage, stockpayment, agebound or capture follows.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(stats,rr);print(sha(S.with_suffix('.json')))
