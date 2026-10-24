from pathlib import Path
from collections import Counter,defaultdict
from itertools import product
import hashlib,json
S=Path(__file__).resolve();R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files={'one_use_paths_have_an_exact_reverse_ordered_R0_R2_relay.md':'f85b114f810bef99105c0648650475b835cbbe60c4da4b81234a0716ce83cdad','check_one_use_R0_R2_relay.py':'513369d34de4327259ff639a497ade02f088f0703d7fae7fa77b2c53dd3142df','check_one_use_R0_R2_relay.json':'ada6a5acafc14f7ac87a41ff93bd8d57be6623b8e7d797708ebc177391dac8ab'}
for f,h in files.items():assert sha(D/f)==h
assert sha(R/'audits/check_cap_free_endpoint_domains_independent.json')=='dadad5807501e5f4d8a92e0b61060cb5f4f92c592113e6cef327417fe69ea51e'
J=json.loads((D/'check_one_use_R0_R2_relay.json').read_text());H='NESW';vec=(1j,1,-1j,-1)
local=[]
for k in range(4):
 for w,inc,out,r in [('E','E','S',0),('WWE','E','N',2),('WWEW','E','N',2)]:
  ww=''.join(H[(H.index(c)+k)%4]for c in w);ii=H[(H.index(inc)+k)%4];oo=H[(H.index(out)+k)%4]
  deps=[H[(H.index(c)+(1 if j%2==0 else-1))%4]for j,c in enumerate(ww)];assert[j for j,c in enumerate(ww)if c==ii]==[r]and[j for j,c in enumerate(deps)if c==oo]==[0];local.append(dict(word=ww,incoming=ii,outgoing=oo,arrival_rank=r,departure_rank=0))
assert local==J['rotated_local_target_rows']
def covers(a,b,t,P):return(2*t+1-2*a)//(2*P)-(2*t+1-2*b)//(2*P)
cal=[]
for z in J['controls']:
 n=z['n_LEFT'];cs=z['c'];ds=z['Delta'];P=z['P'];assert P==sum(ds)-sum(cs)>0 and len(cs)==len(ds)==n
 rs=[0]
 for i in range(n):rs.append(rs[-1]+cs[i]-ds[(i+1)%n])
 assert rs[-1]==-P;ss=[rs[i]+ds[i]for i in range(n)];units=Counter((rs[i]+j)%P for i,c in enumerate(cs)for j in range(c));assert max(units.values())==1
 for t in range(P):assert sum(covers(rs[i],ss[i],t,P)for i in range(n))==1+units[t]
 for i in range(n):
  nxts=ss[(i+1)%n]-(P if i==n-1 else 0);assert nxts==rs[i]+cs[i]and rs[i]-rs[i+1]>=5 and ss[i]-nxts>=5
  if n>=2:assert 8<=ds[i]<=P-5*(n-1)+3<P
  else:assert ds[i]==P+cs[0]
 cal.append(dict(n=n,P=P,maximum_age=max(ds),cover_checked_cuts=P))
assert len(cal)==363
# Genuine standard fronts, all retained physical histories and full drift voltages.
base=(R/'word_stabilization/standard_word.txt').read_text().strip();actual=[]
for copies,phase,rotation in product((1,2,3),(0,17),range(4)):
 w=(base[phase:]+base[:phase])*copies;P=len(w);p=0j;hd=vec[rotation]
 for c in w:hd*=(-1j if c=='R'else 1j);p+=hd
 d=p;assert hd==vec[rotation]and d!=0
 def canon(q):
  axis=0 if d.real else 1;co=lambda z:int(z.real)if axis==0 else int(z.imag);k=co(q)//co(d);return q-k*d,k
 hist=defaultdict(list);p=0j;hd=vec[rotation]
 for t,c in enumerate(w):q,k=canon(p);hist[q].append((t-k*P,hd,c));hd*=(-1j if c=='R'else 1j);p+=hd
 hist={q:sorted(v)for q,v in hist.items()};edge={};flow=Counter()
 for q,es in hist.items():
  assert all(c==('R'if j%2==0 else'L')for j,(t,h,c)in enumerate(es))
  for t,h,c in es:flow[q,h*(-1j if c=='R'else 1j)]+=1
  t,h,c=es[0];v=-1j*h;n,k=canon(q+v);r=next(i for i,(tt,hh,cc)in enumerate(hist[n])if hh==v);assert hist[n][r][0]+k*P==t+1;edge[q]=(n,k,v,r)
 visited=set();ccs=[]
 for q in edge:
  path=[];where={};cur=q
  while cur not in visited and cur not in where:where[cur]=len(path);path.append(cur);cur=edge[cur][0]
  if cur in where:
   cyc=path[where[cur]:]
   if all(flow[z,edge[z][2]]==1 for z in cyc):ccs.append(cyc)
  visited.update(path)
 assert len(ccs)==1
 for cyc in ccs:
  ell=len(cyc);lift=0;rs=[];ss=[];left=[];unit=[]
  for i,q in enumerate(cyc):
   arrival=edge[cyc[(i-1)%ell]][3];assert arrival in(0,2);isleft=arrival==2
   if isleft:assert len(hist[q])in(3,4)
   else:assert len(hist[q])==1
   rt=hist[q][0][0]+lift*P;unit.append(rt)
   if isleft:left.append(i);rs.append(rt);ss.append(hist[q][2][0]+lift*P)
   lift+=edge[q][1]
  assert lift==-1 and ell==2*len(left);n=len(left);units=Counter(t%P for t in unit);assert max(units.values())==1
  for t in range(P):assert sum(covers(a,b,t,P)for a,b in zip(rs,ss))==1+units[t]
  for i in range(n):
   c=(left[(i+1)%n]-left[i])%ell;assert 1<=c<=3;nrs=rs[(i+1)%n]-(P if i==n-1 else 0);nss=ss[(i+1)%n]-(P if i==n-1 else 0);assert nss==rs[i]+c and rs[i]-nrs>=5 and ss[i]-nss>=5 and 8<=ss[i]-rs[i]<=P-5*(n-1)+3<P
  assert P>=3*ell;actual.append(dict(copies=copies,phase=phase,rotation=rotation,P=P,drift=[int(d.real),int(d.imag)],ell=ell,LEFT_classes=n,physical_R0=rs,physical_R2=ss,ages=[b-a for a,b in zip(rs,ss)]))
assert len(actual)==24
review=['Signed cap-free complete-WHITE one-use port domains make internal RIGHT cells singletonR and internal LEFT cells rotatedWWE/WWEW. The unique selected incoming port is actualR0 at RIGHT orR2 at LEFT, while every departure is actualR0. The finite RIGHT-ended path sum therefore retains m minus every internalDelta, and an endpointq+kd contributes its actual+kP voltage. Total one-use, not first-ordinal-only, is essential.',
'The retained cap-free first-departure theorem gives an embedded essential b-circle full winding-1, and zero signed turning gives ell=2nLEFT. Each selected forward unit edge is an actual successor edge at a distinct source event class; all full-drift copies are event-disjoint, soB is0/1. Formal backward R2-toR0 intervals close the temporal cochain; endpoint cancellation and total integral-P give N=1+B at every half-integer cut. The count includes ALL period translates, without any assumed age bound.',
'Between successive LEFTs, three consecutiveRIGHTs would force a closed physical unit square, impossible in an embedded essential circle. Thus the actual contiguous successor channel has1..3edges through only singletonRIGHTs. Distinct sourceR0, intermediateRIGHT and terminalR2 ranks form disjoint components of the selected successor subgraph, not overlapping arbitrary windows.',
'Actual successive same-cell reads require at least4 steps, soDelta02>=8. The channel yields both R0 andR2 endpoint sequences strictly reverse-ordered by>=5. After n LEFTclasses each sequence shifts by-P. For n>=2, comparing s_(i+n)=r_(i+n-1)+c with r_i givesDelta<=P-5(n-1)+3<P. For n1 the exact equation instead givesDelta=P+c and is retained. SummingDelta>=8n andell=2n gives onlyP>=3ell.',
'All363 supplied calendars are checked with exact floor counts over infinitely many translates, rather than a truncated k-range. They are arithmetic controls, not fronts. Additionally24 genuine standard full-history rotation/phase/power controls reconstruct the actual one-use cycle, all port ranks and physical voltages; all have n>=2 and satisfy the theorem.',
'No mixed-boundary all-one-use implication, critical-height extension, external cap, universal same-cell age<P, additive fuel charge, source-sink splicing or whole-front exclusion follows. OptionalL3 and every exterior supplier remain.']
out=dict(status='PASS exact cap-free one-use path relay and whole-circle reverse chronological cover',files=files,dependencies={'audits/check_cap_free_endpoint_domains_independent.json':sha(R/'audits/check_cap_free_endpoint_domains_independent.json'),'periodic_classification_new/white_first_departure_counterflow.md':sha(R/'periodic_classification_new/white_first_departure_counterflow.md'),'audits/check_first_departure_counterflow_independent.json':sha(R/'audits/check_first_departure_counterflow_independent.json')},local_rows=local,arithmetic_controls=cal,genuine_standard_controls=actual,analytic_review=review)
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(sha(S.with_suffix('.json')))
