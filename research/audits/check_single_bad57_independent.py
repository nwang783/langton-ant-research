"""Verify the seven-word standard-capture forbidden-pair certificate from literal words and integer geometry.
No imports from the discovery code; verifies clauses, rather than its fixed point.
"""
import json, hashlib
from pathlib import Path
from collections import Counter
R=Path(__file__).resolve().parents[1]; P=R/'word_stabilization'
N='RRRLLRLLRRRR'
words={0:'RRRLLRLLR',2:'LLLLRLRRRRLRRRR',3:'RRRLLRLLRRRRLLR',26:'RRRLLRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRR',37:'RRRLLRLLRRRRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRR',39:'LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLR',57:'LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLLRLRLLR'}
M='LLLLRLRRRRLR'
EM={0:N,2:M,3:N,26:M,37:M,39:N,57:N}
SM={0:N,2:M,3:N,26:N,37:N,39:M,57:M}
G={(0,3),(0,37),(2,39),(2,57),(3,0),(3,26),(26,2),(37,2),(39,37),(57,3),(57,37)}
assert all((words[a]+EM[a]).startswith(SM[a]) for a in words)
assert all(EM[a]==SM[b] for a,b in G)
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
raw={a:trace(w) for a,w in words.items()};extended={a:trace(w+EM[a]) for a,w in words.items()}
assert all(z['valid'] for z in list(raw.values())+list(extended.values()))
def end(a,p=(0,0),h=0):
 q,k=raw[a]['end'];return plus(p,rot(q,h)),(h+k)%4
def normalize(a,p,h,b,q,k):
 x,y=rot(minus(q,p),-h);return a,b,x,y,(k-h)%4
def feasible(seq):
 if any((a,b) not in G for a,b in zip(seq,seq[1:])):return False
 return trace(''.join(words[a] for a in seq)+EM[seq[-1]])['valid']
def aligned(p,h):return (sum(p)-h)%2==0
J=json.loads((P/'spatial_single_bad57_kernel.json').read_text())
assert tuple(J['alphabet'])==A
stored=json.loads((P/'spaced_two_marker_macros.json').read_text())['macros']
assert {a:stored[a]['word'] for a in A}==words
GP={(a,b) for a in A for b in A if feasible((a,b))}
assert GP==set(map(tuple,J['good_pairs']))==G
GG=json.loads((P/'single_bad57_scc_grammar.json').read_text())
assert set(map(tuple,GG['pairs']))==G
assert set(map(tuple,GG['triples']))=={(a,b,c) for a,b in G for bb,c in G if b==bb}
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
assert len(S)==len(J['kernel'])==8028
assert len(candidates)==J['candidate_count']==8501
assert len(short&candidates)==J['short_count']==23
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
# Five charged sites are raw; the sixth lies in 26's required successor 2.
marks={0:[(2,-3)],26:[(2,-3),(1,-5),(1,-6),(2,-7)],57:[(-3,-3)]};overlaps=0
for b,qs in marks.items():
 for marker in qs:
  assert extended[b]['first'][marker]=='L'
  if marker not in raw[b]['first']:
   assert b==26 and marker==(2,-7)
   assert {c for a,c in G if a==26}=={2} and 2 not in marks
   assert words[2].startswith(EM[26])
   hit=next(i for i,(q,c) in enumerate(extended[b]['vis']) if q==marker)
   assert len(words[b])<=hit<len(words[b])+12
  else:assert raw[b]['first'][marker]=='L'
  for a in A:
   for h in range(4):
    for old in raw[a]['first']:
     p=minus(old,rot(marker,h))
     if aligned(p,h):
      assert (a,b,*p,h) in S;overlaps+=1
W=json.loads((R/'computability/singleton_first_block_input.json').read_text())['word']
cycle=words[2]+words[39]+words[37];assert len(cycle)==104
phases=[j for j in range(104) if cycle==(W+W)[j:j+104]];assert phases
remaining=set(A)-set(marks)
remaining_edges={(a,b) for a,b in G if a in remaining and b in remaining}
assert remaining_edges=={(2,39),(39,37),(37,2)}
out={'status':'independent proof-clause verification passed','candidate_count':len(candidates),'short_types':len(short&candidates),'forbidden_pairs':len(S),'clauses':dict(counts),'neighbor_options':nopt,'intermediate_reader_options':nr,'charged_marker_overlaps':overlaps,'charged_sites':marks,'standard_cycle':[2,39,37],'standard_phase_in_audited_W':phases,'theorem':'Seven literal words with the eleven listed allowed pairs and actual right marker context: n0+4*n26+n57 <= entry black mass. Every infinite finite-support word in this language is eventually standard104. No larger graph coverage claimed.','source_certificate_sha256':hashlib.sha256((P/'spatial_single_bad57_kernel.json').read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
