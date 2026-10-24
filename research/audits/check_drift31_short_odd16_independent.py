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

for line in(P/'DRIFT31_SHORT_ODD16_SHA256SUMS').read_text().splitlines():
 h,f=line.split(None,1);assert sha(P/f)==h
J=json.loads((P/'drift31_short_inventory16_certificate.json').read_text());odd=set(J['full_odd_inventory']);assert odd=={0,1,2,6,7,13,14,16};records=J['proof_records'];used=set();counts=collections.Counter();empty=0
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

bot={int(k):v for k,v in J['short_prefix'].items()};assert [bot[t]for t in range(8)]==[[2],[3],[2],[1,1,3,1],[2,2,0,2],[1,1,3,1],[0,0,0,2,2],[1,1,1,3,3]]
bots=[{**bot,-3:[],-2:[],-1:[]}];tops=[{16:[0],17:[],18:[],19:[]}]
for t in[15,14,13,12,11]:tops=expand(tops,t,'top')
for t in[8,9]:bots=expand(bots,t,'bottom')
assert len(tops)==8 and len(bots)==16 and dict(counts)==J['local_counts']and len(used)==len(records)
assert [canon(h)for h in tops]==[canon({int(k):v for k,v in r.items()})for r in J['top_interfaces']]
assert [canon(h)for h in bots]==[canon({int(k):v for k,v in r.items()})for r in J['bottom_interfaces']]
join=collections.Counter();keys=set();closed=[]
for r in J['all128_joins']:
 i,j=r['bottom_id'],r['top_id'];assert(i,j)not in keys;keys.add((i,j));H={**bots[i],**tops[j]};assert 10 not in H;kind=r['outcome'];w=r['witness']
 if kind=='physical_port_count_mismatch':
  t,u,hh=w['source_level'],w['target_level'],w['heading'];q=-t+v[hh];assert T(q)==u and int(q.imag)==w['full_drift_voltage'];aa=rk(H[t],hh,True);bb=rk(H[u],hh);assert aa==w['source_departure_ranks']and bb==w['target_arrival_ranks']and len(aa)!=len(bb)
 else:
  check_witness(H,r)
  if kind=='closed_component':closed.append([len(w['cycle']),w['winding'],w['other_local_events']])
 join[kind]+=1
assert len(keys)==128 and dict(join)==J['join_counts']
report={'status':'PASS exact supplied full O16 inventory excluded for specified short all-quadruple interface','proof_sha256':sha(P/'DRIFT31_SHORT_ODD16_SUPPLIED_INVENTORY_EXCLUSION.md'),'certificate_sha256':sha(P/'drift31_short_inventory16_certificate.json'),'script_sha256':sha(Path(__file__)),'full_odd_inventory':sorted(odd),'local_counts':dict(counts),'join_counts':dict(join),'closed_component_size_winding_outside':closed,'analytic_checks':['Read extrema0/16 follow signed actual read-minimum/maximum singleton lemmas plus EXACT FULL odd inventory, not treating a partial odd subset as wake. Only below0/above16 declared empty;T10alwaysUNKNOWN.','Every upper/lower binary-heading domain regenerated from literal perpendicular-port counts, exactparity and allphysicalfirstreturns, derivedbound<=15.','Every128join rejection checked by exactnamedphysicalports or actualfullvoltageeventpaths; allrankclock cycles positiveforP>=namedcount. Closedcomponents rejectnonpositivewinding orpropernesswithnamedoutsideevents, not positivewindingalone.','UnknownmiddleT10 orarbitraryhighercompletioncannotchangethe alreadycomplete ordinalpaths/ports. This isonefullinventory/oneprefixonly, notwidth16classification.'],'not_claimed':['threegeneralshortmodesexcluded','newcontroller','unconditionalsingleusedcircle','globalattraction']}
p=R/'audits/drift31_short_odd16_independent.json';p.write_text(json.dumps(report,indent=2)+'\n');print(sha(p));print(report['status'])
