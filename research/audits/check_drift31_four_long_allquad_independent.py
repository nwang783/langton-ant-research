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

def domain(t,Ih,I,Oh,O,bound,rel,parity=None):
 dd=[]
 for n in range(bound+1):
  if parity is not None and n%2!=parity:continue
  for hs in itertools.product((t%2,t%2+2),repeat=n):
   if len(rk(hs,Ih))!=I or len(rk(hs,Oh,True))!=O:continue
   if all(a<len(rk(hs,oh,True))and b<len(rk(hs,ih))and rk(hs,ih)[b]==rk(hs,oh,True)[a]+1 for oh,ih,a,b,L in rel):dd.append(list(hs))
 return dd

def verify_rel(H,t,sup):
 rel,paths=relations(H,t);assert set(rel)=={(p['outgoing_heading'],p['incoming_heading'],p['outgoing_ordinal'],p['incoming_ordinal'],p['duration'])for p in sup}
 lev=sorted(H)
 for p in sup:
  key=(p['outgoing_heading'],p['incoming_heading'],p['outgoing_ordinal'],p['incoming_ordinal'],p['duration']);start,seq=paths[key]
  assert [int(start.real),int(start.imag)]==p['physical_base']and json.dumps([([lev.index(z),rr],k)for(z,rr),k in seq])==json.dumps(p['lower_chain'])
 return rel

for line in(P/'DRIFT31_FOUR_LONG_ALLQUAD_SHA256SUMS').read_text().splitlines():
 h,f=line.split(None,1);assert sha(P/f)==h
J=json.loads((P/'drift31_four_long_allquad_modes_certificate.json').read_text());source=json.loads((P/'drift31_circle_middle_reads_certificate.json').read_text());modes=[r for r in source['eight_OPEN_interfaces']if len(r['T5'])==4 and len(r['T6'])>=8];assert len(modes)==4
C=collections.Counter();sizes=[]
def cover(H,t,r):
 assert canon(H)==canon({int(z):w for z,w in r['histories_before'].items()})
 if t%2==0:ih,I,oh,O=0,len(rk(H[t-3],0,True)),1,H[t-1].count(1)
 else:ih,I,oh,O=3,len(rk(H[t-1],3,True)),2,H[t-3].count(2)
 bound=2*(I+O)+1;assert r['incoming_heading_count']==[ih,I]and r['outgoing_heading_count']==[oh,O]and r['derived_bound']==bound
 rel=verify_rel(H,t,r['actual_first_returns']);dd=domain(t,ih,I,oh,O,bound,rel,None);assert dd==r['complete_domain'];return dd
for mode,r in zip(modes,J['records']):
 H={t:w for t,w in enumerate(mode['complete_named_histories'])};dd=cover(H,8,r);assert len(dd)==len(r['all_T8_outcomes'])
 for h,oc in zip(dd,r['all_T8_outcomes']):
  assert h==oc['history'];HH={**H,8:h};kind=oc['T8_outcome'];check_witness(HH,dict(outcome=kind,witness=oc.get('witness')));C['T8_'+kind]+=1
  if kind!='open':continue
  if oc['outcome']=='rotated_first_arrival_Rule_B':
   rel=verify_rel(HH,9,oc['actual_T9_returns']);i,j=oc['rule_path_pair'];pa,pb=oc['actual_T9_returns'][i],oc['actual_T9_returns'][j]
   assert pa['outgoing_heading']==pb['outgoing_heading']==2 and pa['incoming_heading']==pb['incoming_heading']==3 and pa['incoming_ordinal']==0 and pb['outgoing_ordinal']==pa['outgoing_ordinal']+1 and pb['incoming_ordinal']!=1
   C['T9_Rule_B']+=1
  else:
   assert oc['outcome']=='complete_T9_domain_rejected';zz=cover(HH,9,oc['T9_cover']);sizes.append(len(zz));assert len(zz)==len(oc['T9_outcomes'])
   for z,q in zip(zz,oc['T9_outcomes']):
    assert z==q['history']and q['outcome']=='skipped_rank';check_witness({**HH,9:z},q);w=q['witness'];assert(w['rank_before'],w['rank_after'])==(0,3)and len(w['segment'])==9;C['T9_skipped_rank']+=1
assert dict(C)==J['counts']and sizes==[2,2,4,2,7,7,18]
remaining=[[r['T6'],r['T7']]for r in source['eight_OPEN_interfaces']if len(r['T5'])==4 and len(r['T6'])<8];assert remaining==J['remaining_short_modes']and len(remaining)==3
report={'status':'PASS four specified long all-quadruple interfaces excluded, three short interfaces remain OPEN','proof_sha256':sha(P/'DRIFT31_FOUR_LONG_ALLQUAD_MODES_EXCLUDED.md'),'certificate_sha256':sha(P/'drift31_four_long_allquad_modes_certificate.json'),'script_sha256':sha(Path(__file__)),'counts':dict(C),'T9_domain_sizes':sizes,'remaining_complete_pairs':remaining,'analytic_checks':['Independent reconstruction from signed complete T0..7 histories; all unnamed classes including T10+ remain UNKNOWN.','All53 derived T8 binary histories covered,17 literal rank skips/13 explicit positive rank-clock cycles/23open. Full voltage actuald3,1 and physical first-return paths independently rebuilt.','16 rotated RuleB cases use firstW afterS_a, forcing that read itselfS_(a+1); supplied next return would skipW1. No firstcolor or unseen multiplicity shortcut.','Seven unrestricted-parity T9 domains 2,2,4,2,7,7,18 exhaust derivedbounds<=19; all42 exact8step rank0-to3 paths checked at same physical cell.','Neither growth8 budget nor global visit/support/period cap is used in this local completion obstruction.'],'not_claimed':['three remaining short modes excluded','arbitrary single-used F-circle existence','all drift3,1 fronts excluded','global attraction']}
p=R/'audits/drift31_four_long_allquad_independent.json';p.write_text(json.dumps(report,indent=2)+'\n');print(sha(p));print(report['status'])
