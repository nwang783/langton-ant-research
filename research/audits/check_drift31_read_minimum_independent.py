from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
P=Path(__file__);R=P.parent.parent;D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();bd=D/'DRIFT31_READ_MINIMUM_SHA256SUMS';deps={}
for line in bd.read_text().splitlines():
 h,f=line.split(None,1);assert sha(D/f)==h;deps[f]=h
assert deps['DRIFT31_UNCONDITIONAL_READ_MINIMUM_INTERFACE.md']=='92b5092a879681fc6ff673ea7d3cb8614075562419e4d7b2c38019993004b432'
ref=json.loads((D/'drift31_read_minimum_certificate.json').read_text());v=(1j,1,-1j,-1);dr=3+1j;xy=lambda p:[int(p.real),int(p.imag)];out=lambda h,j:(h+(1 if j%2==0 else-1))%4
canon=lambda a:json.dumps(a,sort_keys=True)
def graph(H):
 pts=[complex(3-i,0)for i in range(len(H))];ix={p:i for i,p in enumerate(pts)};events=[(i,j)for i,h in enumerate(H)for j in range(len(h))];succ={};pred={}
 for i,p in enumerate(pts):
  for hh in range(4):
   dest=p+v[hh];t=int(3*dest.imag-dest.real);rep=complex(-t,0);lift=int(dest.imag)
   if rep not in ix:continue
   ii=ix[rep];ss=[j for j,h in enumerate(H[i])if out(h,j)==hh];tt=[j for j,h in enumerate(H[ii])if h==hh];assert len(ss)==len(tt)
   for j,k in zip(ss,tt):succ[i,j]=((ii,k),lift);pred[ii,k]=((i,j),lift)
 chains=[];seen=set()
 for e in events:
  if e in pred:continue
  seq=[];cur=e;lift=0
  while True:
   assert cur not in seen;seen.add(cur);seq.append((cur,lift))
   if cur not in succ:break
   cur,k=succ[cur];lift+=k
  chains.append(seq)
 assert len(seen)==len(events)
 where={}
 for c,seq in enumerate(chains):
  previous={}
  for a,((i,j),k)in enumerate(seq):
   pos=pts[i]+k*dr
   if pos in previous:assert j==previous[pos]+1
   previous[pos]=j;where[i,j]=(c,a,k)
 edges=[]
 for i,h in enumerate(H):
  for j in range(len(h)-1):
   u,a,ka=where[i,j];w,b,kb=where[i,j+1];edges.append((u,w,4+a-b,kb-ka,i,j))
 return pts,events,succ,chains,edges

def check(H,result,witness):
 pts,events,succ,chains,edges=graph(H)
 if result=='positive_rank_clock_cycle':
  assert canon(chains)==canon(witness['chains']);cy=[tuple(e)for e in witness['inequality_cycle']];assert all(e in edges for e in cy)and all(cy[i][0]==cy[(i+1)%len(cy)][1]for i in range(len(cy)));C=sum(e[2]for e in cy);K=sum(e[3]for e in cy);assert C==witness['constant']and K==witness['period_coefficient']and K>=0 and C+K*len(events)>0
  return C,K
 assert result=='open'and canon(chains)==canon(witness['chains'])and witness['points']==[xy(p)for p in pts]and witness['event_count']==len(events)
 return None

def domains(axis,bound,ih,I,oh,J,rel=()):
 ans=[]
 for n in range(bound+1):
  for h in product((axis,axis+2),repeat=n):
   ins=[j for j,x in enumerate(h)if x==ih];outs=[j for j,x in enumerate(h)if out(x,j)==oh]
   if len(ins)==I and len(outs)==J and all(ins[b]==outs[a]+1 for a,b in rel):ans.append(h)
 return ans
lower=[];stats=Counter();vstats=Counter();bounds=[];clock=[];openrows=[];paths_total=0
for h1,n2s in(((3,),(0,1)),((3,1),(2,3))):
 for n2 in n2s:
  aa=(n2+1)//2
  for h3 in domains(1,2*(aa+1),3,aa,2,1):
   H=[(),(),(),(2,),h1,(2,)*n2,h3];lower.append(H)
assert len(lower)==17
for bi,(H,b)in enumerate(zip(lower,ref['branches'])):
 assert canon(H)==canon(b['histories']);result=b['lower_outcome'];stats[result]+=1
 if result!='open':clock.append(check(H,result,b['witness']));continue
 pts,events,succ,chains,edges=graph(H);ret=[];paths=[]
 for seq in chains:
  (i,j),k=seq[0];assert k==0;hh=H[i][j];src=pts[i]-v[hh];(ii,jj),kk=seq[-1];oh=out(H[ii][jj],jj);target=pts[ii]+kk*dr+v[oh]
  if src!=target or int(3*src.imag-src.real)!=4:continue
  # Ensure no intervening physical read of this unknown cell, making rank adjacency exact.
  assert all(pts[u]+ell*dr!=src for(u,r),ell in seq)
  a=[r for r,x in enumerate(H[i])if x==hh].index(j);bb=[r for r,x in enumerate(H[ii])if out(x,r)==oh].index(jj);assert(hh,oh,bb,len(seq)+1)==(1,0,0,4);ret.append((a,bb));paths.append(dict(outgoing_heading=hh,incoming_heading=oh,outgoing_ordinal=a,incoming_ordinal=bb,duration=len(seq)+1,physical_base=xy(src),lower_chain=seq))
 assert len(ret)==1 and canon(paths)==canon(b['first_return_paths']);paths_total+=1;I=len(H[4]);J=H[6].count(1);bound=2*(I+J)+1;assert b['V4_I_N_J_E']==[I,J]and b['derived_bound']==bound;bounds.append(bound);dom=domains(0,bound,0,I,1,J,ret);assert canon(dom)==canon(b['complete_V4_domain'])and len(dom)==len(b['V4_outcomes'])
 for qi,(word,z)in enumerate(zip(dom,b['V4_outcomes'])):
  assert list(word)==z['word'];HH=H+[word];vstats[z['outcome']]+=1;c=check(HH,z['outcome'],z['witness'])
  if c:clock.append(c)
  else:
   rank=word.index(0);assert rank in(2,4)and all(x==2 for x in word[:rank]);openrows.append(dict(lower_index=bi,V4_index=qi,complete_histories=HH,first_N_rank=rank))
assert stats=={'open':14,'positive_rank_clock_cycle':3}and vstats=={'open':25,'positive_rank_clock_cycle':5}and max(bounds)==13 and canon(openrows)==canon(ref['all25_open_interfaces'])
model=ref['open_seven_event_clock_model'];H=model['complete_named_histories'];pts,events,succ,chains,edges=graph(H);period=model['period_parameter'];assert period==202;times={(z['level']+3,z['rank']):z['clock']for z in model['events']};assert len(times)==7
for e,(f,k)in succ.items():assert times[f]+k*period==times[e]+1
for i,h in enumerate(H):
 for j in range(len(h)-1):assert times[i,j+1]-times[i,j]>=4 and(times[i,j+1]-times[i,j])%4==0
for z in model['events']:
 t=z['level'];rank=z['rank'];clock=z['clock'];phase=clock%period;lift=(phase-clock)//period;p=complex(-t,0)+lift*dr;assert phase==z['phase']and xy(p)==z['physical_position'];xp,yp=int(p.real)%2,int(p.imag)%2;clockparity=(xp+2*yp)%4 if yp==0 else 3-xp;assert phase%4==clockparity
assert len({t%period for t in times.values()})==7
# Direct physical blank factor replay.
f=ref['blank_factor'];B=set();p=-4+0j;h=2
for i,z in enumerate(f['events']):
 ch='L'if p in B else'R';assert(z['time'],z['point'],z['incoming_heading'],z['turn'])==(i,xy(p),h,ch);B.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=v[h]
assert(p,h)==(-3+1j,0)and sorted(map(xy,B))==f['complete_final_black']
out={'status':'PASS unconditional all-cap full drift(3,1) read-minimum interface:25 necessary open histories','bindings_sha256':sha(bd),'dependencies':deps,'lower_counts':dict(stats),'V4_counts':dict(vstats),'derived_H3_max':6,'derived_V4_max':13,'physical_four_step_returns':paths_total,'positive_cycles':clock,'open_interfaces':openrows,'analytic_review':['The full d=(3,1) quotient is exactly T=3y-x, representative(-T,0), voltagey. N/E/S/W steps changeT by3/-1/-3/1. Complete finite read-footprint minimum exists; incoming-axis invariance leaves only S singleton at minimum. Negative levels are UNREAD, not assigned field colors.','H1 all exitsN and oneW input forceW orWE; V2 allS with E departure counts forceempty/S orSS/SSS. H3 exact mandatory ports derive length<=6, not an imposed global cap. All17 lower complete words regenerated,3 explicit positive clock-cycle sums verified from actual rank edges for every admissible P.','Each of14 survivors has exactly one physical four-step E-departure to FIRST N-arrival return throughH3,V0-d,H1-d with no intermediate physical visit toV4. Thus consecutive local read ranks are necessary. All next-cell complete histories up to derived2(I+J)+1<=13 regenerated, including three empty domains:30 choices,5 explicit positive cycles,25open. Omitted higher levels remain UNKNOWN; no all-cap bound is inferred.','All supplied positive cycles verified by independent full-voltage ordinal graph/inequality edges;8 witnesses have nonnegative P coefficient and positive value at local event-count lower bound. Every surviving firstN is R2 orR4. Open does not assert phase-distinct globally completable clocks for all25.','The one explicit7-event P202 model satisfies every internal actual ordinal edge, local gap4, modulo4 coordinate parity and distinct phases. Its195missing phases are not a completion. Literal blank10read fullboard factor independently replayed, without claiming its local LAST histories persist.','Only full drift(3,1) up to proper rotation/translation is covered, not reflected chirality3,-1, arbitrary growth8 exclusion, controller existence, or capture. Corrected single-use charge is separate conditional theory and is not used as an unconditional premise here.']};P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(P),sha(P.with_suffix('.json')))
