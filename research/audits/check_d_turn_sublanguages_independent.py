"""Independent literal two-bit and ordinary spatial-certificate checker."""
import json,hashlib,sys
from pathlib import Path
from collections import Counter
ROOT=Path('/workspace/shared/langton');P=ROOT/'word_stabilization';M='LLLLRLRRRRL'
CWORD='LLLLRLRRRRLRRRR';D='LLLLRLRRRR';U='LLLLRLRRRRLRLLLLRRRRLRRLRRRR'
F='LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLRRRR'
Q=F+'LRRLRRRR';B=F+'LRLLLLRRRRLRRLRRRR'
mode=sys.argv[1] if len(sys.argv)>1 else 'dcu'
prefix='seven_sub_'+mode;suffix='patch2' if mode=='dcu' else 'plain'
BASE=[U] if mode=='dcu' else [F,Q,B]
words=[D+CWORD*k for k in range(4)]+[w+CWORD*k for w in BASE for k in range(3)];A=range(len(words))
quot=json.loads((P/(prefix+'_port_quotient.json')).read_text())
assert [r['word'] for r in quot['macro_words']]==words
assert quot['classes']==1 and sorted(quot['quotient_edges'])==[[0,a,0] for a in A]
assert all(r['end_marker']==M for r in quot['macro_words'])
DIR=((0,1),(1,0),(0,-1),(-1,0))
def rot(q,h):
 x,y=q
 for _ in range(h%4):x,y=y,-x
 return x,y
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def trace(w):
 p=(0,0);h=0;first={};last={};vis=[];valid=True;counts=Counter()
 for c in w:
  if last.get(p)==c:valid=False
  first.setdefault(p,c);last[p]=c;vis.append((p,c));counts[p]+=1
  h=(h+(1 if c=='R' else -1))%4;p=add(p,DIR[h])
 return dict(first=first,last=last,vis=vis,end=(p,h),valid=valid,counts=counts)
raw=[trace(w) for w in words];ext=[trace(w+M) for w in words]
assert all(z['valid'] for z in raw+ext)
assert not trace(CWORD*5)['valid'] and not trace(CWORD*4+M)['valid']
assert all(not trace(w+CWORD*3+M)['valid'] for w in BASE)
def end(a,p=(0,0),h=0):
 q,k=raw[a]['end'];return add(p,rot(q,h)),(h+k)%4
def norm(a,p,h,b,q,k):return(a,b,*rot(sub(q,p),-h),(k-h)%4)
def aligned(p,h):return (sum(p)-h)%2==0
def feasible(seq):return trace(''.join(words[a] for a in seq)+M)['valid']
GP={(a,b) for a in A for b in A if feasible((a,b))};GT={(a,b,c) for a in A for b in A for c in A if feasible((a,b,c))}
gram=json.loads((P/(prefix+'_grammar.json')).read_text());assert GP==set(map(tuple,gram['pairs'])) and GT==set(map(tuple,gram['triples']))
C=set()
for a in A:
 for b in A:
  for h in range(4):
   for q in raw[a]['first']:
    for z in ext[b]['first']:
     p=sub(q,rot(z,h))
     if aligned(p,h):C.add((a,b,*p,h))
short=set()
for a in A:
 p,h=end(a)
 for b in A:
  if (a,b) in GP:short.add((a,b,*p,h))
  for c in A:
   if (a,c,b) in GT:
    q,k=end(c,p,h);short.add((a,b,*q,k))
S={}
cert=P/(prefix+'_'+suffix+'_kernel.tsv')
for line in cert.read_text().splitlines():
 z=list(map(int,line.split()));assert len(z)==(10 if mode=='dcu' else 8)
 key=tuple(z[:5]);assert key not in S;S[key]=z[5:]
assert set(S)<=C and not(set(S)&short)
counts=Counter();nr=nn=0;special=[];cache={}
def readers(q):
 if q not in cache:
  options=set()
  for c in A:
   for hc in range(4):
    for z in raw[c]['first']:
     pc=sub(q,rot(z,hc))
     if aligned(pc,hc):options.add((c,pc,hc))
  cache[q]=options
 return cache[q]
for (a,b,x,y,h),proof in S.items():
 kind=proof[0];p=x,y
 if kind==1:
  pc,hc=end(a)
  for c in A:
   if (a,c) not in GP:continue
   for d in A:
    if (d,b) not in GP:continue
    hd=(h-raw[d]['end'][1])%4;pd=sub(p,rot(raw[d]['end'][0],hd));nn+=1
    assert any(z in S for z in [(a,d,*pd,hd),norm(c,pc,hc,b,p,h),norm(c,pc,hc,d,pd,hd)])
 elif kind==2:
  q=tuple(proof[1:3]);local=rot(sub(q,p),-h)
  assert q in raw[a]['last'] and local in ext[b]['first']
  letter=raw[a]['last'][q];assert letter==ext[b]['first'][local]
  for c,pc,hc in readers(q):
   z=rot(sub(q,pc),-hc)
   if mode=='dcu':
    if raw[c]['counts'][z]%2==0 or raw[c]['first'][z]==letter:continue
    assert raw[c]['first'][z]==raw[c]['last'][z]
   nr+=1;assert (a,c,*pc,hc) in S or norm(c,pc,hc,b,p,h) in S
 elif kind==3:
  assert mode=='dcu';qs=[tuple(proof[1:3]),tuple(proof[3:5])];assert qs[0]!=qs[1]
  start=goal=0
  for j,q in enumerate(qs):
   z=rot(sub(q,p),-h);assert q in raw[a]['last'] and z in ext[b]['first']
   start|=(raw[a]['last'][q]=='R')<<j;goal|=(ext[b]['first'][z]=='L')<<j
  graph={i:set() for i in range(4)};poses=readers(qs[0])|readers(qs[1]);retained=0
  for c,pc,hc in poses:
   if (a,c,*pc,hc) in S or norm(c,pc,hc,b,p,h) in S:continue
   retained+=1
   for inp in range(4):
    state=inp;ok=True
    # Replay every literal RAW read in order, rather than author's endpoint masks.
    for z,letter in raw[c]['vis']:
     physical=add(pc,rot(z,hc))
     if physical in qs:
      j=qs.index(physical)
      if bool(state&(1<<j))!=(letter=='L'):ok=False;break
      state^=1<<j
    if ok:graph[inp].add(state)
  reached={start};todo=[start]
  for v in todo:
   for w in graph[v]:
    if w not in reached:reached.add(w);todo.append(w)
  assert goal not in reached
  special.append(dict(pair=[a,b,x,y,h],cells=qs,start=start,goal=goal,all_readers=len(poses),retained_readers=retained,graph={str(v):sorted(ws) for v,ws in graph.items()},reachable=sorted(reached)))
 else:raise AssertionError(kind)
 counts[kind]+=1
startup={(0,0),(-1,0),(-1,-1),(0,-1),(1,0)};marks=[];overlaps=0
for b in A:
 if b<4:selected=[(0,1,11)]
 elif mode=='dcu':selected=[(0,2,12),(0,3,23)]+([(-1,4,29)] if b>4 else [])
 else:selected=[(-3,-1,42)]
 marks.append(selected)
 assert startup.isdisjoint({tuple(z[:2]) for z in selected}) and all(raw[b]['first'].get(q)=='L' for q in startup)
 assert len({tuple(z[:2]) for z in selected})==len(selected)
 assert raw[b]['vis'][1][0] not in {tuple(z[:2]) for z in selected}
 for x,y,j in selected:
  q=x,y
  assert ext[b]['vis'][j]==(q,'L') and all(v!=q for v,c in ext[b]['vis'][:j])
  for a in A:
   for h in range(4):
    for old in raw[a]['first']:
     p=sub(old,rot(q,h))
     if aligned(p,h):assert (a,b,*p,h) in S;overlaps+=1
 weight=len(selected);assert len(words[b])<=(55 if mode=='dcu' else 104)*weight
 if mode=='dcu':assert words[b].count('R')-words[b].count('L')<=9*weight
assert end(0)==((1,1),0)
assert raw[0]['vis'][6]==(end(0)[0],'R')
assert all(q!=end(0)[0] for q,c in raw[0]['vis'][7:])
assert words[0]+'L'==M
# D's external selected read is precisely the successor's phase1 in every possible successor.
for b in A:
 p,h=end(0);assert add(p,rot(raw[b]['vis'][1][0],h))==(0,1)
out=dict(status='PASS independent literal clauses, short controls and first-L mark queries',mode=mode,packets=len(words),pairs=len(GP),triples=len(GT),candidates=len(C),shorts=len(C&short),forbidden=len(S),clause_types=dict(counts),reader_options=nr,neighbor_options=nn,special_two_cell_clauses=special,marks=marks,mark_overlap_queries=overlaps,certificate_sha256=hashlib.sha256(cert.read_bytes()).hexdigest())
if mode=='dcu':assert (len(C),len(C&short),len(S),dict(counts))==(8111,47,7510,{1:6801,2:707,3:2})
else:assert (len(C),len(C&short),len(S))==(53398,57,52837)
Path(__file__).with_name('check_d_turn_'+mode+'_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
