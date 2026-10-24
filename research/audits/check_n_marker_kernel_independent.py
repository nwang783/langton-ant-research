"""Verify the N-return forbidden-pair certificate from literal words and integer geometry.
No imports from the discovery code; verifies clauses, rather than its fixed point.
"""
import json, hashlib
from pathlib import Path
from collections import Counter
R=Path(__file__).resolve().parents[1]; P=R/'word_stabilization'
N='RRRLLRLLRRRR'
words={0:'RRRLLRLLR',3:'RRRLLRLLRRRRLLR',8:'RRRLLRLLRRRRLLRLLRLRLLR',10:'RRRLLRLLRRRRLLRLRRRRLRLLR',45:'RRRLLRLLRRRRLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLR',71:'RRRLLRLLRRRRLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLR'}
A=tuple(words);E=set(A)-{0,3};D=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):
 x,y=p
 for _ in range(h%4):x,y=y,-x
 return x,y
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def minus(a,b):return a[0]-b[0],a[1]-b[1]
def trace(w):
 p=(0,0);h=0;vis=[];first={};last={};valid=True
 for c in w:
  if p in last and last[p]==c:valid=False
  first.setdefault(p,c);last[p]=c;vis.append((p,c));h=(h+(1 if c=='R' else -1))%4;p=plus(p,D[h])
 return dict(first=first,last=last,vis=vis,end=(p,h),valid=valid)
raw={a:trace(w) for a,w in words.items()};extended={a:trace(w+N) for a,w in words.items()}
assert all(z['valid'] for z in list(raw.values())+list(extended.values()))
def end(a,p=(0,0),h=0):
 q,k=raw[a]['end'];return plus(p,rot(q,h)),(h+k)%4
def normalize(a,p,h,b,q,k):
 x,y=rot(minus(q,p),-h);return a,b,x,y,(k-h)%4
def feasible(seq):
 if any(a in E and c==3 and b in E for a,c,b in zip(seq,seq[1:],seq[2:])):return False
 return trace(''.join(words[a] for a in seq)+N)['valid']
def aligned(p,h):return (sum(p)-h)%2==0
J=json.loads((P/'spatial_n_marker_separated_kernel.json').read_text())
assert tuple(J['alphabet'])==A
stored=json.loads((P/'spaced_two_marker_macros.json').read_text())['macros']
assert {a:stored[a]['word'] for a in A}==words
GP={(a,b) for a in A for b in A if feasible((a,b))}
assert GP==set(map(tuple,J['good_pairs']))=={(a,3) for a in A if a!=3}|{(3,a) for a in A if a!=3}
candidates=set()
for a in A:
 for b in A:
  for h in range(4):
   for x in raw[a]['first']:
    for y in extended[b]['first']:
     p=minus(x,rot(y,h))
     if aligned(p,h):candidates.add((a,b,*p,h))
short=set()
for a in A:
 p,h=end(a)
 for b in A:
  if feasible((a,b)):short.add((a,b,*p,h))
  for c in A:
   if feasible((a,c,b)):
    q,k=end(c,p,h);short.add((a,b,*q,k))
S={tuple(row[:5]):row[5] for row in J['kernel']}
assert len(S)==len(J['kernel'])==6562
assert len(candidates)==J['candidate_count']==7221
assert len(short&candidates)==J['short_count']==20
assert set(S)<=candidates and not(set(S)&short)
counts=Counter();nopt=nr=0
for (a,b,x,y,h),proof in S.items():
 p=(x,y)
 if proof[0]=='neighbors':
  assert len(proof)==1
  pc,hc=end(a)
  for c in A:
   if (a,c) not in GP:continue
   for d in A:
    if (d,b) not in GP:continue
    hd=(h-raw[d]['end'][1])%4;pd=minus(p,rot(raw[d]['end'][0],hd));nopt+=1
    smaller=((a,d,*pd,hd),normalize(c,pc,hc,b,p,h),normalize(c,pc,hc,d,pd,hd))
    assert any(z in S for z in smaller),((a,b,x,y,h),c,d)
 elif proof[0]=='equal-read':
  assert len(proof)==3;q=tuple(proof[1:]);local=rot(minus(q,p),-h)
  assert q in raw[a]['last'] and local in extended[b]['first']
  assert raw[a]['last'][q]==extended[b]['first'][local]
  readers=set()
  for c in A:
   for hc in range(4):
    for z in raw[c]['first']:
     pc=minus(q,rot(z,hc))
     if aligned(pc,hc):readers.add((c,pc,hc))
  for c,pc,hc in readers:
   nr+=1
   assert (a,c,*pc,hc) in S or normalize(c,pc,hc,b,p,h) in S
 else:raise AssertionError(proof)
 counts[proof[0]]+=1
# The charged sites are INSIDE raw macros, not in the shared right context.
marker=(2,-3);overlaps=0
for b in A:
 if b==3:continue
 assert raw[b]['vis'][7]==(marker,'L')
 assert marker not in {q for q,c in raw[b]['vis'][:7]}
 for a in A:
  for h in range(4):
   for old in raw[a]['first']:
    p=minus(old,rot(marker,h))
    if aligned(p,h):
     assert (a,b,*p,h) in S;overlaps+=1
# Bind the 16 short separation premises to the independently audited W.
W=json.loads((R/'computability/singleton_first_block_input.json').read_text())['word']
legal={(W+W)[i:i+10] for i in range(104)};assert len(legal)==84
offsets={8:19,10:27,45:51,71:48};distances=[]
for a in E:
 for b in E:
  w=words[a]+words[3]+words[b]+N;ta=offsets[a];tb=len(words[a])+len(words[3])+offsets[b]
  for t in (ta,tb):assert w[t-10:t] not in legal and w[t-9:t+1] not in legal
  distances.append(tb-ta)
assert (min(distances),max(distances))==(32,95)
other=json.loads((P/'spatial_n_marker_spacing_kernel.json').read_text())
assert set(S)=={tuple(row[:5]) for row in other['kernel']}
out={'status':'independent proof-clause verification passed','candidate_count':len(candidates),'short_types':len(short&candidates),'forbidden_pairs':len(S),'clauses':dict(counts),'neighbor_options':nopt,'intermediate_reader_options':nr,'charged_marker_overlaps':overlaps,'designated_K_spacing_range':[min(distances),max(distances)],'theorem':'Six literal N-return macros, with actual next N right context and no E,3,E factor: charged phase7 sites fresh relative to factor; at most 2m+1 macros and 92m+15 raw turns. Spacing >=96 implies the short premise. No claim about arbitrary 88-macro paths.','source_certificate_sha256':hashlib.sha256((P/'spatial_n_marker_separated_kernel.json').read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
