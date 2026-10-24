from pathlib import Path
from itertools import product,combinations
from collections import Counter
import json,hashlib,ast
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'one_use_L3_falls_require_a_double_LEFT.md';JF=D/'check_one_use_L3_transport.json';assert sha(P)=='58fb54278ae797cc2a643a20177fc6b9b937a9e8fd4ba8074962c41eb391dd20'and sha(JF).startswith('64ff894f')and sha(D/'check_one_use_L3_transport.py').startswith('b0a94353');J=json.loads(JF.read_text());H='NESW';V=(1j,1,-1j,-1);xy=lambda p:[int(p.real),int(p.imag)];out=lambda w,r:H[(H.index(w[r])+(1 if r%2==0 else-1))%4]
def check(hs,row):
 su={};bad=[]
 for p,w in hs.items():
  for h,d in zip(H,V):
   if p+d not in hs:continue
   aa=[r for r in range(len(w))if out(w,r)==h];bb=[r for r,v in enumerate(hs[p+d])if v==h]
   if len(aa)!=len(bb):bad.append(dict(source=xy(p),direction=h,source_ranks=aa,target=xy(p+d),target_ranks=bb))
   else:su.update({(p,a):(p+d,b)for a,b in zip(aa,bb)})
 if bad:assert row['result']=='port'and row['certificate']in bad;return'port',su
 wrong=[]
 for p,w in hs.items():
  for r in range(len(w)):
   cur=(p,r);path=[cur];seen={cur}
   while cur in su:
    cur=su[cur];path.append(cur)
    if cur[0]==p:
     if cur[1]!=r+1:wrong.append(path)
     break
    assert cur not in seen;seen.add(cur)
 if wrong:
  assert row['result']=='rank';path=[(complex(*p),r)for p,r in row['certificate']['path']];assert path in wrong;return'rank',su
 assert row['result']=='open';return'open',su
rows={(r['start_bit'],r['end_bit'],r['D']):r for r in J['LRL_all14_maximum_compatible_reader_rows']};seen=set();stats=Counter();opens=[]
for s,t in product([0,1],repeat=2):
 k,l=2+t,2+s
 for a in range(min(k,l)+1):
  for eps in(0,1):
   b=k-a;dd=l-a;c=k+l-3*a+eps
   if min(b,dd,c)<0 or a<c:continue
   n=a+b+c+dd;assert n==2*(k+l-2*a)+eps<=5
   for rs in combinations(range(0,n,2),a):
    for ls in combinations(range(1,n,2),b):
     ss=set(rs)|set(ls);w=''.join('S'if i in ss else'N'for i in range(n));key=s,t,w;assert key not in seen;seen.add(key);assert w.count('S')==k and sum(out(w,r)=='W'for r in range(n))==l
     hs={1+0j:'WWE'+('W'if s else''),1+1j:'N',2+1j:'WWE'+('W'if t else''),2+0j:w};why,su=check(hs,rows[key]);stats[why]+=1
     if why=='open':opens.append(key)
     if(s,t)==(1,0):
      assert w=='SNS';path=[(1+0j,0),(1+1j,0),(2+1j,2),(2+0j,2),(1+0j,3)];assert all(su[a]==b for a,b in zip(path,path[1:]))
assert seen==set(rows)and len(seen)==14 and stats=={'rank':9,'open':5};assert sorted(opens)==[(0,0,'SSNN'),(0,1,'SSS'),(1,1,'SSNNS'),(1,1,'SSSN'),(1,1,'SSSNN')]
for row in J['LRRL_complete_bit_pairs']:
 s,t=row['start_bit'],row['end_bit'];hs={1+0j:'WWE'+('W'if s else''),1+1j:'N',2+1j:'E',2+0j:'NNS'+('N'if t else'')};assert sum(out(hs[2+0j],r)=='W'for r in range(len(hs[2+0j])))==2+t and hs[1+0j].count('W')==2+s;why,su=check(hs,row);assert(why=='open')==(s==t)
 if s==t:
  path=[(1+0j,0),(1+1j,0),(2+1j,0),(2+0j,2),(1+0j,1)];assert all(su[a]==b for a,b in zip(path,path[1:]));assert not s or su[2+0j,3]==(1+0j,3)
row=J['LL_drop_necessary_control'];hs={complex(*ast.literal_eval(p)):w for p,w in row['histories'].items()};_,su=check(hs,{'result':'open'});tt={(complex(*ast.literal_eval(k)[0]),ast.literal_eval(k)[1]):v for k,v in row['distinct_mod4_calendar'].items()};ev={(p,r)for p,w in hs.items()for r in range(len(w))};assert set(tt)==ev and len(ev)==len(set(tt.values()))==13
for a,b in su.items():assert tt[b]==tt[a]+1
for p,w in hs.items():
 x,y=map(int,(p.real,p.imag));phase=2*(x%2)if(x+y)%2==0 else 3-2*(x%2)
 for r in range(len(w)):
  assert tt[p,r]%4==phase
  if r:assert tt[p,r]-tt[p,r-1]>=4
pre=set(su.values());comps=[];used=set()
for e in sorted(ev-pre,key=lambda e:(e[0].real,e[0].imag,e[1])):
 cur=e;cc=[]
 while True:
  assert cur not in used;used.add(cur);cc.append(cur)
  if cur not in su:break
  cur=su[cur]
 comps.append(cc)
assert used==ev and[[[xy(p),r]for p,r in c]for c in comps]==row['components'];order=row['component_order'];assert sorted(order)==list(range(len(comps)))and all(tt[comps[a][-1]]<tt[comps[b][0]]for a,b in zip(order,order[1:]))
# Independently solve the complete stream/clock local control through the signed generic checker.
ns={'__file__':str(S.with_name('check_global_max_flow2_staircase_independent.py'))};exec(Path(ns['__file__']).read_text().split('rows=[];stats=Counter()')[0],ns);assert ns['test']({p:ns['cv'](w)for p,w in hs.items()})[0]=='open'
O=dict(status='PASS cap-free GLOBAL-M one-use L3-state no-fall across LRL and equality across LRRL; scoped LL-drop local control',proof=sha(P),certificate=sha(JF),script=sha(S),derived_domain_count=14,counts=stats,necessary_profiles=opens,LL_drop_events=13,analytic_review=[
'Exact LRL counts SinD=2+t,WoutD=2+s and completeWHITE R/L positions give c=k+l-3a+epsilon,n=2(k+l-2a)+epsilon. KnownD NW=M gives a>=c by unrestricted curl, without assuming DfirstRselectsmaximum. Independent position-subset generation proves the derivedn<=5 and all14 candidates, nine physicalrankfailures andfive necessaryopens.',
'For bit1->0 the only integerpossibilitya2,c0,epsilon1 forcesSNS. Its actual fourstepA0->R0->C2->D2->A3 skips requiredranks at SAMEphysicalA. The two five-read1->1 readers remain necessaryuncappedescapes, not factors.',
'LRRL closingC->A completeportcounts2+t and2+s forcebitequality independentlyofGLOBALM/exteriorcap. Allfour pairs and surviving actualfourR firstreturn plusoptionalL3edge checked. ThreeRIGHTs closeaphysicalsquare, forbidden on the actualembeddedessentialbpath, so allpossiblegaps betweenconsecutiveLEFTs are0/1/2RIGHTs. Everybitfall therefore occursatLL; no pathlength/voltage/lifespan bound is inferred.',
'ActualGLOBALM stock-tail fourreadbit1 to evenUportal forcedthree-readbit0 implies someLL, inadditionto the separatelysigned internalRIGHTsingleton. Those are geometricnecessities, not independentfuel payments or a contradiction. Changedendpointroles/startbits are not covered.',
'The13eventLLdrop local inventory retains allcompleteports, exactheight/clockconsistency and disjoint injective mod4wholecomponentcalendar. Its exteriorconnections remain unfilled; it is not anactualpreparedfactor orfront.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(stats,opens);print(sha(S.with_suffix('.json')))
