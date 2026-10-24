from pathlib import Path
import json,hashlib,itertools,collections
R=Path('/workspace/shared/langton');P=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for line in(P/'DRIFT31_ODD20_SHA256SUMS').read_text().splitlines():h,f=line.split(None,1);assert sha(P/f)==h
J=json.loads((P/'drift31_inventory20_certificate.json').read_text());odd={0,1,2,5,6,8,13,20};v=[1j,1,-1j,-1];d=3+1j;T=lambda p:int(3*p.imag-p.real);o=lambda h,r:(h+(1 if r%2==0 else-1))%4;rk=lambda w,h,out=False:[r for r,x in enumerate(w)if(o(x,r)if out else x)==h];canon=lambda H:tuple((t,tuple(w))for t,w in sorted(H.items()))
def graph(H):
 levels=sorted(H);su={};pr={};events={(t,r)for t,w in H.items()for r in range(len(w))}
 for t,w in H.items():
  for h in range(4):
   q=-t+v[h];u=T(q);k=int(q.imag)
   if u not in H:continue
   a=rk(w,h,True);b=rk(H[u],h);assert len(a)==len(b)
   for r,s in zip(a,b):su[t,r]=((u,s),k);pr[u,s]=((t,r),k)
 chains=[];seen=set()
 for st in sorted(events-set(pr)):
  at=st;k=0;seq=[]
  while True:
   assert at not in seen;seen.add(at);seq.append((at,k))
   if at not in su:break
   at,a=su[at];k+=a
  chains.append(seq)
 return su,events,chains,seen,levels

def relations(H,t):
 su,events,ch,seen,lev=graph(H);assert seen==events;out=[];paths={}
 for seq in ch:
  (u,r),k=seq[0];ih=H[u][r];start=-u-v[ih]
  (z,s),kk=seq[-1];oh=o(H[z][s],s);end=-z+kk*d+v[oh]
  if T(start)!=t or start!=end:continue
  assert all(-a+q*d!=start for(a,b),q in seq)
  a=rk(H[u],ih).index(r);b=rk(H[z],oh,True).index(s);key=(ih,oh,a,b,len(seq)+1);out.append(key);paths[key]=(start,seq)
 return out,paths

def check_witness(H,rec):
 su,events,ch,seen,lev=graph(H);kind=rec['outcome'];w=rec.get('witness');N=len(events)
 def decode(seq):return [((lev[e[0]],e[1]),k)for e,k in seq]
 def valid_path(seq):
  for (a,k),(b,l)in zip(seq,seq[1:]):assert a in su and su[a]==(b,l-k)
 if kind=='open':assert seen==events;return
 if kind=='skipped_rank':
  seq=decode(w['segment']);valid_path(seq);(a,r),k=seq[0];(b,s),l=seq[-1];assert -a+k*d==-b+l*d and s!=r+1
  assert(r,s)==(w['rank_before'],w['rank_after']);assert all(-c+m*d!=-a+k*d for(c,rr),m in seq[1:-1]);return
 if kind=='closed_component':
  seq=decode(w['cycle']);valid_path(seq);(a,k)=seq[-1];(b,l)=seq[0];assert su[a][0]==b;wind=k+su[a][1]-l;assert wind==w['winding'];outside=N-len(seq);assert outside==w['other_local_events']
  assert wind<=0 or outside>0
  if wind==1:assert(len(seq),outside)==(30,67)
  return
 assert kind=='positive_rank_clock_cycle'and seen==events
 supplied=[[([lev.index(t),r],k)for(t,r),k in seq]for seq in ch];assert json.dumps(supplied)==json.dumps(w['chains'])
 loc={e:(i,j,k)for i,seq in enumerate(ch)for j,(e,k)in enumerate(seq)};allowed=set()
 for t,hs in H.items():
  for r in range(len(hs)-1):
   u,a,ka=loc[t,r];vv,b,kb=loc[t,r+1];allowed.add((u,vv,4+a-b,kb-ka,lev.index(t),r))
 cy=[tuple(x)for x in w['inequality_cycle']];assert all(e in allowed for e in cy)
 assert collections.Counter(e[0]for e in cy)==collections.Counter(e[1]for e in cy)
 C=sum(e[2]for e in cy);K=sum(e[3]for e in cy);assert C==w['constant']and K==w['period_coefficient']and N==w['local_event_count']and K>=0 and C+K*N==w['positive_at_minimum_period']>0
records=J['all_proof_records'];used=set();counts=collections.Counter();empty=0

def expand(states,t,side,exact=False):
 global empty
 result=[];counts[f'{side}_T{t}_parents']+=len(states)
 for H in states:
  ix=[i for i,r in enumerate(records)if r['level']==t and r['side']==side and canon({int(a):b for a,b in r['complete_named_before'].items()})==canon(H)];assert len(ix)==1;i=ix[0];assert i not in used;used.add(i);r=records[i]
  if side=='bottom':
   if t%2==0:ih,I,oh,JJ=0,len(rk(H[t-3],0,True)),1,H[t-1].count(1)
   else:ih,I,oh,JJ=3,len(rk(H[t-1],3,True)),2,H[t-3].count(2)
  else:
   if t%2==0:ih,I,oh,JJ=2,len(rk(H[t+3],2,True)),3,H[t+1].count(3)
   else:ih,I,oh,JJ=1,len(rk(H[t+1],1,True)),0,H[t+3].count(0)
  bound=(H[8].count(2)+H[14].count(0)if t==11 else len(rk(H[9],0,True))+len(rk(H[15],2,True)))if exact else 2*(I+JJ)+1
  assert r['known_incoming_heading_count']==[ih,I]and r['known_outgoing_heading_count']==[oh,JJ]and r['derived_bound']==bound and r['bound_is_exact_length']==exact
  rel,paths=relations(H,t);sup=r['actual_first_return_paths'];assert set(rel)=={(p['outgoing_heading'],p['incoming_heading'],p['outgoing_ordinal'],p['incoming_ordinal'],p['duration'])for p in sup}
  levels=sorted(H)
  for p in sup:
   key=(p['outgoing_heading'],p['incoming_heading'],p['outgoing_ordinal'],p['incoming_ordinal'],p['duration']);start,seq=paths[key]
   assert [int(start.real),int(start.imag)]==p['physical_base']and json.dumps([([levels.index(z),rr],k)for(z,rr),k in seq])==json.dumps(p['lower_chain'])
  dom=[]
  for n in([bound]if exact else range(bound+1)):
   if n%2!=(t in odd):continue
   for hs in itertools.product((t%2,t%2+2),repeat=n):
    if len(rk(hs,ih))!=I or len(rk(hs,oh,True))!=JJ:continue
    ok=True
    for hh,ii,a,b,L in rel:
     aa=rk(hs,hh,True);bb=rk(hs,ii)
     if a>=len(aa)or b>=len(bb)or bb[b]!=aa[a]+1:ok=False;break
    if ok:dom.append(list(hs))
  assert dom==r['complete_domain_after_necessary_returns']and len(r['outcomes'])==len(dom)
  if t==12 and not dom:empty+=1
  for hs,oc in zip(dom,r['outcomes']):
   assert hs==oc['history'];HH={**H,t:hs};check_witness(HH,oc);counts[f'{side}_T{t}_{oc["outcome"]}']+=1
   if oc['outcome']=='open':result.append(HH)
 return result
bot={int(k):v for k,v in J['forced_two_quad_prefix'].items()};assert {k:bot[k]for k in range(8)}=={0:[2],1:[3],2:[2],3:[1,1,3,1],4:[2,2,0,2],5:[1,1,3],6:[0,0,0],7:[1,1,1,3]};assert all(bot[t]==[]for t in[-3,-2,-1])
top={20:[0],21:[],22:[],23:[]};tops=[top]
for t in[19,18,17,16,15,14]:tops=expand(tops,t,'top')
bots=[bot]
for t in[8,9,10]:bots=expand(bots,t,'bottom')
assert len(tops)==2 and len(bots)==4
merged=[{**a,**b}for a in bots for b in tops];mid=expand(merged,11,'bottom',True);assert len(mid)==44;final=expand(mid,12,'bottom',True);assert not final and empty==31 and len(used)==len(records)and dict(counts)==J['counts']
report={'status':'PASS exact full O20 inventory excluded for supplied two-quadruple single-used F-circle branch','proof_sha256':sha(P/'DRIFT31_ODD20_TWO_ENDED_EXCLUSION.md'),'certificate_sha256':sha(P/'drift31_inventory20_certificate.json'),'script_sha256':sha(Path(__file__)),'complete_case_counts':dict(counts),'empty_T12_domains':empty,'proof_records':len(used),'analytic_scope':['Complete read maximum20, not just odd-set or field maximum, follows signed extreme lemma; only outer classes below0/above20 declared empty. T13 remains UNKNOWN throughout.','All domains regenerated over invariant axes from both actual port counts, exact parity and every physical first-return. Loose local bound2(I+J)+1 is derived; atT11 both outputs giveexact10, atT12 both inputs giveexact12.','Every skipped-rank path follows exact complete ordinal edges and closes in the same physical lift. Every positive cycle consists of independently reconstructed consecutive-rank inequalities and is positive for everyP>=named-event count.','All six +1 closed components have30 events and67 other named events, so cannot be the unique actual period orbit. Positive winding alone is never used as rejection.','Coverage tree starts with exact two independent boundaries and enumerates every surviving join. No timeout, SMT, imposed global cap or fixed-period search.'],'not_claimed':['all larger interleavings excluded','all-quadruple branch excluded','unconditional single-used circle existence','d(3,1) or growth8 classification']}
p=R/'audits/drift31_odd20_independent.json';p.write_text(json.dumps(report,indent=2)+'\n');print(sha(p));print(report['status'])
