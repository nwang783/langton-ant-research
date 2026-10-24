from pathlib import Path
from itertools import product
from collections import Counter,deque
import ast,json,hashlib,time
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
P=D/'passive_strip_singleton_O_exits_fail_complete_next_contact.md';A=D/'check_passive_strip_O_exit_rank_collision.json';C=D/'check_passive_strip_O_exit_rank_collision.py'
assert sha(P).startswith('1179a3cb')and sha(C).startswith('1798f67d')and sha(A).startswith('1e9c53e8')
ref=json.loads(A.read_text());base=json.loads(S.with_name('check_passive_LL_flat_cap_independent.json').read_text());assert base['status'].startswith('PASS')
H='NESW';V=(1j,1,-1j,-1);cv=lambda w:tuple(H.index(a)for a in w);st=lambda w:''.join(H[a]for a in w);out=lambda w,r:(w[r]+(1 if r%2==0 else-1))%4
words=lambda ax:[w for n in range(5)for w in product(ax,repeat=n)];NS=words((0,2));EW=words((1,3));ins=lambda w,d:tuple(i for i,a in enumerate(w)if a==d);outs=lambda w,d:tuple(i for i in range(len(w))if out(w,i)==d)
ALL=set(NS+EW);inc={(w,d):ins(w,d)for w in ALL for d in range(4)};outc={(w,d):outs(w,d)for w in ALL for d in range(4)}
Qdom=[w for w in EW if w and w[0]==1 and len(inc[w,1])==2 and len(outc[w,2])>=2];assert set(map(st,Qdom))=={'EEWW','EWWE','EWE','EWEW'}
xy=lambda p:[int(p.real),int(p.imag)]
basefixed={complex(*ast.literal_eval(p)):cv(w)for p,w in base['unique_cyclic_inventory'].items()}|{1-1j:cv('NSS'),2-2j:cv('NNSS')}
# Independent physical count cache: the radial edge is incoming iff direction and cell parity agree.
def port(w,p,d):return len(inc[w,(d+2)%4])if d%2==int(p.real+p.imag)%2 else len(outc[w,d])
def reduce(ds,adj):
 q=deque(ds)
 while q:
  p=q.popleft()
  for t,d in adj[p]:
   keep={port(w,p,d)for w in ds[p]};a=[w for w in ds[t]if port(w,t,(d+2)%4)in keep]
   if not a:return None
   if len(a)<len(ds[t]):ds[t]=a;q.append(t)
 return ds

def succ(hs,adj):
 su={}
 for p,w in hs.items():
  for q,d in adj[p]:
   a=outc[w,d];b=inc[hs[q],d];assert len(a)==len(b)
   su.update({(p,i):(q,j)for i,j in zip(a,b)})
 return su

def failure(hs,su):
 best=None
 for p,w in hs.items():
  for r in range(len(w)):
   cur=(p,r);seen={cur};path=[cur]
   while cur in su:
    cur=su[cur];path.append(cur)
    if cur[0]==p:
     if cur[1]!=r+1 and(best is None or len(path)<len(best)):best=path
     break
    if cur in seen:break
    seen.add(cur)
 return best
counts={};lens=Counter();rows=[];sample=[];started=time.time()
for post,nxt in product(('EEWW','EWWE'),Qdom):
 fixed=basefixed|{2-1j:cv(post),3-2j:nxt};pts=set(fixed)
 while True:
  outside={p+v for p in pts for v in V}-pts;add={q for q in outside if sum(q+v in pts for v in V)>=2}
  if not add:break
  pts|=add
 assert pts=={complex(x,y)for x in range(4)for y in range(-2,3)}
 order=sorted(pts,key=lambda p:(p.real,p.imag));adj={p:[(p+v,d)for d,v in enumerate(V)if p+v in pts]for p in order}
 ar=next(r for r in ref['rows']if r['post']==post and r['next']==st(nxt));assert sorted(ar['cells'])==sorted(map(xy,pts))
 expected={}
 for r in ar['rank_collision_certificates']:
  hs={complex(*ast.literal_eval(p)):cv(w)for p,w in r['histories'].items()};key=tuple(hs[p]for p in order);assert key not in expected
  expected[key]=[(complex(*p),rank)for p,rank in r['literal_wrong_rank_path']]
 seen=set();local=Counter();localhash=hashlib.sha256()
 def search(ds):
  ds=reduce(ds,adj)
  if ds is None:return
  un=[p for p in order if len(ds[p])>1]
  if un:
   p=min(un,key=lambda p:len(ds[p]))
   for w in ds[p]:search(ds|{p:[w]})
   return
  hs={p:a[0]for p,a in ds.items()};key=tuple(hs[p]for p in order);assert key not in seen;seen.add(key)
  su=succ(hs,adj);best=failure(hs,su);assert best
  path=expected[key];assert all(su.get(a)==b for a,b in zip(path,path[1:]))
  assert path[0][0]==path[-1][0]and path[-1][1]!=path[0][1]+1 and all(p!=path[0][0]for p,r in path[1:-1])
  lens[len(best)-1]+=1;local[len(best)-1]+=1
  localhash.update(('|'.join(st(w)for w in key)+'\n').encode())
  if len(sample)<12:sample.append(dict(post=post,next=st(nxt),histories={str(tuple(xy(p))):st(hs[p])for p in order},path=[[xy(p),r]for p,r in best]))
 search({p:[fixed[p]]if p in fixed else(NS[:]if int(p.real+p.imag)%2==0 else EW[:])for p in order})
 assert seen==set(expected)and len(seen)==(11150 if st(nxt)in('EEWW','EWWE')else 100)
 counts[post+','+st(nxt)]=len(seen);rows.append(dict(post=post,next=st(nxt),count=len(seen),witness_lengths=dict(local),ordered_domain_digest=localhash.hexdigest()))
 print(post,st(nxt),len(seen),dict(local),'elapsed',round(time.time()-started,2),flush=True)
assert sum(counts.values())==45000 and lens=={4:44808,8:108,12:84}
reports=['check_passive_LL_flat_cap_independent.json','check_passive_packet_exit_independent.json','check_mixed_flow2_flat_islands_independent.json','check_mixed_LL_gate_independent.json'];deps={}
for f in reports:
 p=S.with_name(f);assert json.loads(p.read_text())['status'].startswith('PASS');deps[f]=sha(p)
O=dict(status='PASS complete passive-strip singleton-O exit exclusion in critical GLOBAL-M no-one-use complete-WHITE cap-four scope',proof=sha(P),author_checker=sha(C),author_certificate=sha(A),script=sha(S),signed_dependencies=deps,derived_Q_domain=list(map(st,Qdom)),total=45000,witness_lengths=dict(lens),rows=rows,samples=sample,analytic_review=[
'The last passive packet has the exact signed unique cyclic3x3 inventory, not an arbitrary earlier local profile. Its Y endpoint followed by singletonO gives rootNSS and the signed singleton-island flatC and next passiveV. Earlier passive-strip length never enters.',
'If the next contact after V wereLEFT, criticality makes itV; mixedLL with precedingflatC makes the opposite flankflat, so the mandatory flat-ended passive-cap theorem applies. It requires a precedingRIGHT forC, contradicting its actual precedingrootO. Thus nextQ isRIGHT. ExactlyEin2 and selectedSout>=2 with firstE derive allEEWW/EWWE/EWE/EWEW including source4.',
'Independent corner closure gives exactly20physicalcells. Each unknown retainsEMPTY/allWHITE1..4 axiswords, and independent bidirectional count propagation matches every internal zero/nonzeroport. All45000 complete leaves independently enumerated and matched one-to-one against the certificate. Every stored path checked as an actual physical successor path and independent shortest failures rederived:44808length4,108length8,84length12.',
'No height, clock, period, finiteage, inputfuel or exterior filter is used to reject a leaf. A full-drift alias adds equality constraints but cannot repair a wrong physical next-rank visit inside a contiguous known path. Completeness uses globalcap4 at addedreaders; no exteriorcapfree claim.',
'This excludes exactly the singletonO exit of a maximal passivePstrip. Other singletonO contexts, K>=2, some-oneuse circles and unrestricted all-cap fronts are not excluded. Signed weaker prepared/local controls remain valid.'
]);S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
