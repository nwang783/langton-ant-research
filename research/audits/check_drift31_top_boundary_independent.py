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

for fname in ['DRIFT31_TOP_ODD_GAP_SHA256SUMS','DRIFT31_ADJACENT_TOP_ODD_SHA256SUMS']:
 for line in(P/fname).read_text().splitlines():
  h,f=line.split(None,1);assert sha(P/f)==h
J=json.loads((P/'drift31_top_odd_gap_certificate.json').read_text());records=J['records'];used=set();counts={};states=[{20:[0],21:[],22:[],23:[]}]
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
for t in range(19,12,-1):
 new=[];C=collections.Counter()
 for H in states:
  ix=[i for i,r in enumerate(records)if r['level']==t and canon({int(a):b for a,b in r['complete_named_before'].items()})==canon(H)];assert len(ix)==1;i=ix[0];assert i not in used;used.add(i);r=records[i]
  if t%2==0:ih,I,oh,O=2,len(rk(H[t+3],2,True)),3,H[t+1].count(3)
  else:ih,I,oh,O=1,len(rk(H[t+1],1,True)),0,H[t+3].count(0)
  bound=2*(I+O)+1;assert r['incoming_heading_count']==[ih,I]and r['outgoing_heading_count']==[oh,O]and r['derived_bound']==bound
  parity=0 if t>13 else None;assert r['required_parity']==parity
  rel=verify_rel(H,t,r['actual_first_returns']);dd=domain(t,ih,I,oh,O,bound,rel,parity);assert dd==r['complete_domain']and len(dd)==len(r['outcomes'])
  for h,oc in zip(dd,r['outcomes']):
   assert h==oc['word'];HH={**H,t:h};check_witness(HH,oc);C[oc['outcome']]+=1
   if oc['outcome']=='open':new.append(HH)
   if t==13:
    assert h[:2]==[3,1];w=oc['witness'];lev=sorted(HH);seq=[((lev[e[0]],e[1]),k)for e,k in w['segment']]
    expected=[((14,0),0),((13,1),0),((16,1),1),((17,0),1),((20,0),2),((19,0),2),((16,2),1),((17,1),1),((14,2),0)];assert seq==expected
 counts[str(t)]=dict(C);states=new
assert not states and len(used)==len(records)and counts==J['counts']
A=json.loads((P/'drift31_adjacent_top_odd_certificate.json').read_text());H={20:[0],21:[],22:[],23:[]}
for t,ih,oh,par in [(19,1,0,1),(18,2,3,0),(17,1,0,0)]:
 I=len(rk(H[t+(1 if t%2 else 3)],ih,True));O=H[t+(3 if t%2 else 1)].count(oh);dd=domain(t,ih,I,oh,O,2*(I+O)+1,[],par)
 r=A['upper_propagation'][19-t];assert r=={'level':t,'incoming_heading_count':[ih,I],'outgoing_heading_count':[oh,O],'parity':par,'domain':dd};assert len(dd)==1;H[t]=dd[0]
assert H[19]==[1]and H[18]==[]and H[17]==[3,3]
rel=verify_rel(H,16,[A['same_physical_four_return']]);assert rel==[(3,2,0,0,4)]
dd=domain(16,2,1,3,2,7,[]);ev=[h for h in dd if len(h)%2==0];assert ev==[[2,0],[0,0,0,0,0,2],[0,0,0,2,0,0],[0,2,0,0,0,0]]or set(map(tuple,ev))=={(2,0),(0,0,0,0,0,2),(0,0,0,2,0,0),(0,2,0,0,0,0)}
for h,r in zip(ev,A['all_even_complete_histories']):assert h==r['word']and h.index(2)==r['first_S_rank']and rk(h,3,True)[0]==r['first_W_departure_rank']and h.index(2)!=rk(h,3,True)[0]+1
assert [h for h in dd if len(h)%2 and h.index(2)==rk(h,3,True)[0]+1]==[[0,0,2]]==A['odd_histories_passing_this_one_return']
# Independent physical square, no intermediate visit at start.
pts=[-16+0j,-17+0j,-17+1j,-16+1j,-16+0j];assert all(pts[i]!=pts[0]for i in range(1,4))
assert [[int(q.real),int(q.imag)]for q in pts]==[r['point']for r in A['physical_path']]
report={'status':'PASS both unrestricted top-read boundary lemmas; conditional two-quadruple single-used F-circle branch excluded','proofs':{f:sha(P/f)for f in ['DRIFT31_UNIFORM_TOP_ODD_GAP.md','DRIFT31_ADJACENT_TOP_ODD_OBSTRUCTION.md']},'certificates':{f:sha(P/f)for f in ['drift31_top_odd_gap_certificate.json','drift31_adjacent_top_odd_certificate.json']},'script_sha256':sha(Path(__file__)),'top_gap_counts':counts,'adjacent_even_histories':ev,'analytic_review':['Full actual read maximum, not field/odd-subset maximum. Sector normalized to vertical-even; even maximum translates to20 without changing it. Above20 classes empty, lower omitted classes UNKNOWN.','Every domain is exhaustive binary heading words within derived2(I+J)+1, with parity unrestricted atT13. All upper physical return paths, positive clock witnesses and ten eight-step rank0-to2 skips independently rebuilt.','At adjacent top odd, exact ports S1/W2 and physical firstW-to-firstS four-return force rankS=rankW+1. Even length2m implies m=1+2u,u0/1; both analytic cases contradict firstness. Four even words explicitly checked; odd NNS only local open control.','For signed exact full two-quad odd inventory, six-level theorem forcesa=c; then M-1odd and M-2,M-3,M-4even contradict adjacent theorem. All c>=3 and1<=b<c covered algebraically.'],'not_claimed':['all-quadruple circle branch excluded','single-used F-circle existence for arbitrary fronts','unconditional drift3,1 growth8 exclusion','global attraction']}
out=R/'audits/drift31_top_boundary_independent.json';out.write_text(json.dumps(report,indent=2)+'\n');print(sha(out));print(report['status'])
