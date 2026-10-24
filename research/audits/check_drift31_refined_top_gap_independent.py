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

def verify_rel(H,t,sup):
 rel,paths=relations(H,t);assert set(rel)=={(p['outgoing_heading'],p['incoming_heading'],p['outgoing_ordinal'],p['incoming_ordinal'],p['duration'])for p in sup}
 lev=sorted(H)
 for p in sup:
  key=(p['outgoing_heading'],p['incoming_heading'],p['outgoing_ordinal'],p['incoming_ordinal'],p['duration']);start,seq=paths[key]
  assert [int(start.real),int(start.imag)]==p['physical_base']and json.dumps([([lev.index(z),rr],k)for(z,rr),k in seq])==json.dumps(p['lower_chain'])
 return rel

for line in(P/'DRIFT31_REFINED_TOP_ODD_GAP_SHA256SUMS').read_text().splitlines():
 h,f=line.split(None,1);assert sha(P/f)==h
J=json.loads((P/'drift31_refined_top_odd_gap_certificate.json').read_text());records=J['records'];used=set();counts={};states=[{20:[0],21:[],22:[],23:[]}];finalskips=collections.Counter();bounds=[]
def fastdomain(ih,I,oh,O,bound,rel,par):
 dd=[]
 for n in range(bound+1):
  if par is not None and n%2!=par:continue
  ev=list(range(0,n,2));od=list(range(1,n,2));rr=len(ev);ll=len(od)
  z=O-ll+I if o(ih,0)==oh else rr+I-O
  if z%2:continue
  a=z//2;b=I-a
  if not(0<=a<=rr and 0<=b<=ll):continue
  for E in itertools.combinations(ev,a):
   for L in itertools.combinations(od,b):
    hs=[(ih+2)%4]*n
    for k in E+L:hs[k]=ih
    assert len(rk(hs,ih))==I and len(rk(hs,oh,True))==O
    if all(x<len(rk(hs,h1,True))and y<len(rk(hs,h2))and rk(hs,h2)[y]==rk(hs,h1,True)[x]+1 for h1,h2,x,y,duration in rel):dd.append(hs)
 return dd
for t in range(19,12,-1):
 nxt=[];C=collections.Counter()
 for H in states:
  ii=[i for i,r in enumerate(records)if r['level']==t and canon({int(k):w for k,w in r['complete_named_before'].items()})==canon(H)];assert len(ii)==1;i=ii[0];assert i not in used;used.add(i);r=records[i]
  if t%2==0:ih,I,oh,O=2,len(rk(H[t+3],2,True)),3,H[t+1].count(3)
  else:ih,I,oh,O=1,len(rk(H[t+1],1,True)),0,H[t+3].count(0)
  bound=2*(I+O)+1;par=0 if t not in[13,16]else None;bounds.append(bound);assert r['incoming_heading_count']==[ih,I]and r['outgoing_heading_count']==[oh,O]and r['derived_bound']==bound and r['required_parity']==par
  rel=verify_rel(H,t,r['actual_first_returns']);dd=fastdomain(ih,I,oh,O,bound,rel,par);assert len(dd)==len(set(map(tuple,dd)))and set(map(tuple,dd))==set(map(tuple,r['complete_domain']))
  assert len(r['outcomes'])==len(dd)
  for oc in r['outcomes']:
   hs=oc['word'];assert hs in dd;HH={**H,t:hs};check_witness(HH,oc);C[oc['outcome']]+=1
   if oc['outcome']=='open':nxt.append(HH)
   if t==13:
    w=oc['witness'];assert len(w['segment'])==9;finalskips[w['rank_before'],w['rank_after']]+=1
 counts[str(t)]=dict(C);states=nxt
assert not states and len(used)==len(records)and counts==J['counts']and max(bounds)==23 and finalskips=={(0,2):58,(2,5):4}
report={'status':'PASS unrestricted five-position odd-read obligation below full drift3,1 read maximum','proof_sha256':sha(P/'DRIFT31_REFINED_TOP_ODD_GAP.md'),'certificate_sha256':sha(P/'drift31_refined_top_odd_gap_certificate.json'),'script_sha256':sha(Path(__file__)),'complete_counts':counts,'final_eightstep_rank_skips':[[*p,n]for p,n in finalskips.items()],'greatest_derived_bound':max(bounds),'analytic_checks':['Complete WHITE full drift3,1; invariantverticaleven sector; actual READ maximumM even singletonN. NormalizeM20; onlyaboveMempty, lowerUNKNOWN.','EvennessassumedonlyM-1,M-2,M-3,M-5,M-6. M-4=T16 andT13 bothUNRESTRICTEDparity.','Independent closedformcount inversion: a incomingih atRranks determinedby2a=J-l+I orr+I-J, then allR/Lpositionsubsets enumerateeachcompletebinarywordonce. Bound2(I+J)+1derived, notexternalcap.','Allphysicalsamecellfirstreturns, exactordinalsuccessors andpositiveclockcyclememberships independentlyrebuilt.62 finalhistories all8step rankskips:58zero-to2,4two-to5.','Conclusiononlyexistenceoddclassinthefivepositions. No specificfulloddinventoryfamilyownership inferred withoutseparateproof.'],'not_claimed':['particularshortmodeexcluded','growth8closure','unconditionalsingleusedcircle','globalattraction']}
p=R/'audits/drift31_refined_top_gap_independent.json';p.write_text(json.dumps(report,indent=2)+'\n');print(sha(p));print(report['status'])
