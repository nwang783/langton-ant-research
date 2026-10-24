"""Independent literal clause checker for six C-free words with common right marker.
No discovery imports or quotient-graph premises.
"""
import json,hashlib
from pathlib import Path
from collections import Counter
B=Path('/workspace/shared/langton');P=B/'word_stabilization'
M='LLLLRLRRRRL'
rows=json.loads((P/'d_cfree_raw_port_quotient.json').read_text())['macro_words'];words=[r['word'] for r in rows];A=range(6)
assert list(map(len,words))==[10,18,28,56,64,74]
assert all(r['end_marker']==M for r in rows)
assert words[0]=='LLLLRLRRRR'
assert all(w.startswith(M) for w in words[1:]) and all(w.startswith('L') for w in words)
DIR=((0,1),(1,0),(0,-1),(-1,0))
def rot(q,h):
 x,y=q
 for _ in range(h%4):x,y=y,-x
 return x,y
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def trace(w):
 p=(0,0);h=0;first={};last={};vis=[];valid=True
 for c in w:
  if p in last and last[p]==c:valid=False
  first.setdefault(p,c);last[p]=c;vis.append((p,c));h=(h+(1 if c=='R' else -1))%4;p=add(p,DIR[h])
 return dict(first=first,last=last,vis=vis,end=(p,h),valid=valid)
raw=[trace(w) for w in words];ext=[trace(w+M) for w in words]
assert all(z['valid'] for z in raw+ext)
assert all(z['end'][1]%2==0 and sum(z['end'][0])%2==0 for z in raw)
def end(a,p=(0,0),h=0):
 q,k=raw[a]['end'];return add(p,rot(q,h)),(h+k)%4
def norm(a,p,h,b,q,k):return(a,b,*rot(sub(q,p),-h),(k-h)%4)
def aligned(p,h):return h%2==0 and (sum(p)-h)%2==0
def feasible(seq):return trace(''.join(words[a] for a in seq)+M)['valid']
GP={(a,b) for a in A for b in A if feasible((a,b))}
GT={(a,b,c) for a in A for b in A for c in A if feasible((a,b,c))}
gram=json.loads((P/'d_cfree_raw_grammar.json').read_text());assert GP==set(map(tuple,gram['pairs'])) and GT==set(map(tuple,gram['triples']))
C=set()
for a in A:
 for b in A:
  for h in (0,2):
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
for line in (P/'d_cfree_raw_even_kernel.tsv').read_text().splitlines():
 z=list(map(int,line.split()));assert len(z)==8
 key=tuple(z[:5]);assert key not in S;S[key]=z[5:]
assert len(C)==3804 and len(short&C)==43 and len(S)==3532
assert set(S)<=C and not(set(S)&short)
counts=Counter();nr=nn=0
for (a,b,x,y,h),(kind,qx,qy) in S.items():
 p=x,y
 if kind==1:
  pc,hc=end(a)
  for c in A:
   if (a,c) not in GP:continue
   for d in A:
    if (d,b) not in GP:continue
    hd=(h-raw[d]['end'][1])%4;pd=sub(p,rot(raw[d]['end'][0],hd));nn+=1
    assert any(z in S for z in [(a,d,*pd,hd),norm(c,pc,hc,b,p,h),norm(c,pc,hc,d,pd,hd)])
 elif kind==2:
  q=qx,qy;local=rot(sub(q,p),-h)
  assert raw[a]['last'].get(q)==ext[b]['first'].get(local) and q in raw[a]['last'] and local in ext[b]['first']
  readers=set()
  for c in A:
   for hc in (0,2):
    for z in raw[c]['first']:
     pc=sub(q,rot(z,hc))
     if aligned(pc,hc):readers.add((c,pc,hc))
  for c,pc,hc in readers:
   nr+=1;assert (a,c,*pc,hc) in S or norm(c,pc,hc,b,p,h) in S
 else:raise AssertionError(kind)
 counts[kind]+=1
q=(-1,0);overlaps=0
for b in A:
 assert raw[b]['vis'][1]==(q,'L') and raw[b]['vis'][0][0]!=q
 for a in A:
  for h in (0,2):
   for old in raw[a]['first']:
    p=sub(old,rot(q,h))
    if aligned(p,h):assert (a,b,*p,h) in S;overlaps+=1
# Independent weighted mark and terminal boundary queries on the checked relation.
marks=json.loads((P/'d_cfree_fuel_marks.json').read_text())
weights=[1,2,3,10,11,14]
startup={(0,0),(-1,-1),(0,-1),(1,0)}
weighted_overlaps=0
terminal_overlaps=0
terminal_points=[]
for b in A:
 selected=marks[str(b)]
 assert len(selected)==weights[b]
 assert len({tuple(z[:2]) for z in selected})==weights[b]
 assert startup.isdisjoint({tuple(z[:2]) for z in selected})
 assert all(raw[b]['first'][q]=='L' for q in startup)
 assert len(words[b])<=10*weights[b]
 assert words[b].count('R')-words[b].count('L')<=2*weights[b]
 for x,y,j in selected:
  q=x,y
  assert raw[b]['vis'][j]==(q,'L') and all(p!=q for p,c in raw[b]['vis'][:j])
  for a in A:
   for h in (0,2):
    for old in raw[a]['first']:
     p=sub(old,rot(q,h))
     if aligned(p,h):assert (a,b,*p,h) in S;weighted_overlaps+=1
 j=len(words[b])+1;q,c=ext[b]['vis'][j]
 assert c=='L' and all(p!=q for p,c in ext[b]['vis'][:j])
 terminal_points.append(q)
 for a in A:
  for h in (0,2):
   for old in raw[a]['first']:
    p=sub(old,rot(q,h))
    if aligned(p,h):assert (a,b,*p,h) in S;terminal_overlaps+=1
assert terminal_points==[(0,1),(0,3),(-1,4),(-3,-2),(-3,-4),(-2,-5)]
out={'status':'independent literal proof-clause audit passed','word_lengths':list(map(len,words)),'candidates':len(C),'short_types':len(short&C),'forbidden_types':len(S),'clauses':dict(counts),'reader_options':nr,'neighbor_options':nn,'charged_overlaps':overlaps,'weighted_mark_counts':weights,'weighted_overlap_queries':weighted_overlaps,'terminal_overlap_queries':terminal_overlaps,'terminal_points':terminal_points,'marks_sha256':hashlib.sha256((P/'d_cfree_fuel_marks.json').read_bytes()).hexdigest(),'certificate_sha256':hashlib.sha256((P/'d_cfree_raw_even_kernel.tsv').read_bytes()).hexdigest(),'scope':'Any physically feasible concatenation of the six literal words followed by actual marker LLLLRLRRRRL has all listed raw first-L marks fresh, with weights 1/2/3/10/11/14 plus four disjoint startup cells. Raw turns <=10(m-4), exit mass <=3m-8. The next terminal-C phase1 input is fresh relative to this entire C-free prefix. No freshness across earlier C, actual-port premise, or marked-site induction.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
