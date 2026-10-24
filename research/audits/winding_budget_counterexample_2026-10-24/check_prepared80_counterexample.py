"""Literal prepared80 counterexample to m*(S-1)<=2min(I,O).
Discovery search is NOT a premise. Everything below checks one exact supplied word.
"""
from pathlib import Path
from collections import defaultdict
from math import gcd
import json,hashlib
PTH=Path(__file__);D=PTH.parent
WORD='RRRRLLLLRLRRRRLLLLRLRLRRRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRLRLRRRRLRRRRLLLLRLLRRL'
V=(1j,1,-1j,-1);xy=lambda q:[int(q.real),int(q.imag)];key=lambda q:(q.real,q.imag)
CAP={-1-1j,-1+0j};INPUT={1j,3+2j};DRIFT=4+4j

def analyze(word):
 P=len(word);p=0j;h=0;E=[]
 for i,c in enumerate(word):
  hi=h;h=(h+(1 if c=='R'else-1))%4;E.append(dict(time=i,cell=xy(p),incoming=hi,outgoing=h,turn=c));p+=V[h]
 d=p;assert h==0 and d.real and d.imag;H=defaultdict(list);ks={}
 for e in E:
  q=complex(*e['cell']);k=int(q.real)//abs(int(d.real))*(1 if d.real>0 else-1);H[q-k*d].append((e['time']-k*P,e['time']));ks[e['time']]=k
 A={};I=set();O=set();lifetimes=[]
 for q,ls in H.items():
  ls.sort();ids=[i for t,i in ls];assert all(word[a]!=word[b]for a,b in zip(ids,ids[1:]));assert len({E[i]['incoming']%2 for i in ids})==1
  if word[ids[0]]=='L':I.add(ids[0])
  if word[ids[-1]]=='R':O.add(ids[-1])
  for a,b in zip(ids,ids[1:]):
   if word[a]=='R':
    vol=ks[a]-ks[b];age=b+vol*P-a;assert age>0 and age%4==0
    assert complex(*E[a]['cell'])==complex(*E[b]['cell'])+vol*d
    A[a]=(b,vol);A[b]=(a,-vol);lifetimes.append(dict(R=a,L=b,voltage=vol,age=age))
 B={(a+1)%P:((b+1)%P,v+(b==P-1)-(a==P-1))for a,(b,v)in A.items()}
 seen=set();paths=[];internal=[]
 for st in range(P):
  if st in seen:continue
  lv={st:0};stack=[st];vertices=set()
  while stack:
   a=stack.pop();seen.add(a);vertices.add(a)
   for M in [A,B]:
    if a not in M:continue
    b,v=M[a];assert E[a]['incoming']%2==E[b]['incoming']%2
    if b in lv:assert lv[b]==lv[a]+v
    else:lv[b]=lv[a]+v;stack.append(b)
  ends=[]
  for a in sorted(vertices):
   if a not in A:ends.append((a,lv[a]))
   if a not in B:ends.append(((a-1)%P,lv[a]-(a==0)))
  if not ends:internal.append(sorted(vertices));continue
  assert len(ends)==2
  (a,ka),(b,kb)=ends;vol=kb-ka;axis='H'if E[st]['incoming']%2 else'V';pa=complex(*E[a]['cell']);pb=complex(*E[b]['cell'])+vol*d
  assert pa.imag==pb.imag if axis=='H'else pa.real==pb.real
  paths.append(dict(a=a,b=b,voltage=vol,axis=axis,events=sorted(vertices)))
 adj=defaultdict(list)
 for ei,e in enumerate(paths):
  a,b,v=e['a'],e['b'],e['voltage'];adj[a].append((b,v,ei));adj[b].append((a,-v,ei))
 assert set(adj)==I|O and all(len(es)==2 for es in adj.values())
 seen=set();circuits=[]
 for st in sorted(adj):
  if st in seen:continue
  a=st;prev=-1;vol=0;steps=[];roots=[]
  while True:
   assert a not in seen;seen.add(a);roots.append(a);b,v,ei=next(e for e in adj[a]if e[2]!=prev);steps.append(dict(a=a,b=b,edge=ei,voltage=v));vol+=v;a=b;prev=ei
   if a==st:break
  circuits.append(dict(roots=roots,winding=vol,input_roots=sorted(set(roots)&I),output_roots=sorted(set(roots)&O),steps=steps))
 # Embedded fibre matching checks with all input/output endpoints. No passive backgrounds are added.
 fibres=[]
 for axis in 'HV':
  fixed=(lambda z:z.imag)if axis=='H'else(lambda z:z.real);var=(lambda z:z.real)if axis=='H'else(lambda z:z.imag)
  for level in range(abs(int(fixed(d)))):
   pairs=[];coords={}
   for e in paths:
    if e['axis']!=axis:continue
    a,b,vol=e['a'],e['b'],e['voltage'];pa=complex(*E[a]['cell']);delta=level-fixed(pa)
    if delta%fixed(d):continue
    n=int(delta//fixed(d));pa+=n*d;pb=complex(*E[b]['cell'])+(n+vol)*d;assert fixed(pa)==fixed(pb)==level
    aa=(a,'I'if a in I else'O');bb=(b,'I'if b in I else'O');coords[aa]=var(pa);coords[bb]=var(pb);pairs.append((aa,bb))
   order=sorted(coords,key=lambda a:(0,coords[a])if a[1]=='I'else(1,-coords[a]));ix={a:i for i,a in enumerate(order)};intervals=[sorted((ix[a],ix[b]))for a,b in pairs]
   for j,(a,b)in enumerate(intervals):
    for c,e in intervals[j+1:]:assert not(a<c<b<e or c<a<e<b)
   fibres.append(dict(axis=axis,level=level,order=order,pairs=pairs))
 return dict(period=P,drift=xy(d),events=E,histories=[dict(representative=xy(q),canonical_reads=[dict(time=t,phase=i,turn=word[i])for t,i in rows])for q,rows in sorted(H.items(),key=lambda z:key(z[0]))],input_roots=sorted(I),output_roots=sorted(O),lifetimes=lifetimes,paths=paths,internal_cycles=internal,boundary_cycles=circuits,fibre_matchings=fibres)

def run(seed,word):
 B={q:('initial',tuple(xy(q)))for q in seed};p=0j;h=0;first={};events=[]
 for t,c in enumerate(word):
  first.setdefault(p,t);old=B.pop(p,None);assert(old is not None)==(c=='L'),(t,p,c)
  events.append(dict(time=t,cell=xy(p),turn=c,old_identity=old))
  if c=='R':B[p]=t
  h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 return B,p,h,first,events
G=analyze(WORD);assert len(WORD)==80 and G['drift']==[4,4]and len(G['histories'])==31
assert G['input_roots']==[15,21]and len(G['output_roots'])==14 and not G['internal_cycles']
S=sum(abs(c['winding'])for c in G['boundary_cycles']);assert sorted((abs(c['winding']),len(c['input_roots']),len(c['output_roots']))for c in G['boundary_cycles'])==[(0,1,1),(3,1,13)]and S==3
m=gcd(*G['drift']);assert m==4 and m*(S-1)==8>4==2*min(len(G['input_roots']),len(G['output_roots']))
assert all(WORD!=WORD[:p]*(80//p)for p in range(1,80)if 80%p==0)
# One full finite field transition with exact initial identities.
B,p,h,first,events=run(CAP|INPUT,WORD);assert(p,h)==(DRIFT,0)
OUT={complex(*G['events'][i]['cell'])for i in G['output_roots']};assert len(OUT)==14 and set(B)=={q+DRIFT for q in CAP}|OUT and not OUT&{q+DRIFT for q in CAP}
assert {q for q,t in first.items()if events[t]['turn']=='L'}==CAP|INPUT
# Full-period ray arithmetic proves all future copies of the supplied inputs are unread now,
# all14 produced output lifetimes are never read later, and output copies do not alias.
E=G['events']
for q in INPUT:
 for e in E:
  delta=complex(*e['cell'])-q
  if int(delta.real)%4==0 and delta.imag==delta.real:assert int(delta.real)//4<=0
for i in G['output_roots']:
 q=complex(*E[i]['cell'])
 for e in E:
  delta=q-complex(*e['cell'])
  if int(delta.real)%4==0 and delta.imag==delta.real:
   k=int(delta.real)//4;assert 80*k+e['time']<=i
for i,q in enumerate(sorted(OUT,key=key)):
 for r in sorted(OUT,key=key)[i+1:]:assert not((int((q-r).real)%4==0)and(q-r).imag==(q-r).real)
# Exact canonical first-future-read construction of the infinite prepared input.
cap=set();rays=[]
for hist in G['histories']:
 q=complex(*hist['representative']);rows=hist['canonical_reads'];lo=-(max(r['time']for r in rows)//80);hi=-min(r['time']for r in rows)//80
 while min(r['time']for r in rows)+80*hi<0:hi+=1
 while not any(r['time']+80*lo>=0 for r in rows):lo+=1
 for k in range(lo,hi):
  e=next(r for r in rows if r['time']+80*k>=0)
  if e['turn']=='L':cap.add(q+k*DRIFT)
 if rows[0]['turn']=='L':rays.append(q+hi*DRIFT)
assert cap==CAP and set(rays)==INPUT
# All-N induction: inputs translate, unchanged output debris is provably never re-read.
controls=[]
for N in [1,2,3,10,100]:
 seed=CAP|{q+j*DRIFT for q in INPUT for j in range(N)};B,p,h,f,ev=run(seed,WORD*N)
 expected={q+N*DRIFT for q in CAP}|{q+j*DRIFT for q in OUT for j in range(N)}
 assert set(B)==expected and len(B)==2+14*N and len(seed)==2+2*N and(p,h)==(N*DRIFT,0)
 assert all(f[q+j*DRIFT]==80*j+(15 if q==1j else 21)for q in INPUT for j in range(N))
 # With no next paid inputs, exact first difference is the next block's tick15.
 pp=p;hh=h;C=set(B)
 for t in range(16):
  ch='L'if pp in C else'R'
  if t<15:assert ch==WORD[t]
  else:assert ch=='R'and WORD[t]=='L'and pp==1j+N*DRIFT
  C.symmetric_difference_update({pp});hh=(hh+(1 if ch=='R'else-1))%4;pp+=V[hh]
 controls.append(dict(N=N,seed=sorted(map(xy,seed)),initial_mass=len(seed),end_pose=[xy(p),h],full_end_black=sorted(map(xy,B)),end_mass=len(B),first_missing_next_input_read=80*N+15))
powers=[]
for q in [1,2,3,5]:
 g=analyze(WORD*q);mm=gcd(*g['drift']);ss=sum(abs(c['winding'])for c in g['boundary_cycles']);ii=len(g['input_roots']);oo=len(g['output_roots']);assert(mm,ss,ii,oo)==(4*q,3,2*q,14*q);assert mm*(ss-1)==8*q>4*q==2*min(ii,oo)
 powers.append(dict(q=q,P=len(WORD)*q,drift=g['drift'],m=mm,S=ss,I=ii,O=oo,left=8*q,right=4*q,boundary_windings=[c['winding']for c in g['boundary_cycles']]))
report=dict(status='VERIFIED LITERAL PREPARED-FRONT COUNTEREXAMPLE; independent peer review requested',word=WORD,word_primitive_period=80,graph=G,cap=sorted(map(xy,CAP)),input_ray_starts=sorted(map(xy,INPUT)),input_ray_drift=xy(DRIFT),one_period_output=sorted(map(xy,OUT)),one_period_full_field_events=events,inequality=dict(m=m,S=S,I=2,O=14,left=8,right=4,false=True),all_N_controls=controls,power_controls=powers,scope=['This falsifies m*(S-1)<=2min(I,O) for actual complete alternating prepared translating fronts, not just for an abstract matching.','The full forward initial field is CAP plus the two input rays for j>=0. Adding all output copies OUT+j*d for j<0 gives a bi-infinite full translating board: one actual period translates that ENTIRE field by d. These old output copies never affect the forward reads.','Finite N realizes exactly N full periods from2+2N black cells and then diverges at80N+15 without another paid input. Infinite exact repetition needs infinitely many prelaid inputs.','This is NOT a WHITE-front counterexample, autonomous finite-seed translating controller, global-attraction counterexample or classification of the live WHITE four boundary types. No discovery-search count or coverage is a proof premise.'],checker_sha256=hashlib.sha256(PTH.read_bytes()).hexdigest())
(D/'prepared80_counterexample.json').write_text(json.dumps(report,indent=2)+'\n');print(report['status']);print(hashlib.sha256((D/'prepared80_counterexample.json').read_bytes()).hexdigest());print('P80,d4,4,I2,O14,S3,m4:8>4; all-N finite seeds2+2N, first missing input80N+15')
