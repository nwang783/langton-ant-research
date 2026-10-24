"""Independent literal owner propagation for the signed all-n spiral overlap.
The controls verify the formulas; the note's all-n induction is audited separately.
"""
from pathlib import Path
from itertools import combinations
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
H=(ROOT/'word_stabilization/standard_word.txt').read_text().strip()
F={(H*2)[i:i+10]for i in range(104)}
SIX={'RRRLLRLLRLR','LLRLRLLRRLL','RRRRLRLLRLL','RRRLRRRRLRL','RRRLRRRRLRR','LRRLRRRRLRR'}
label='LRRLLRRLLRR';assert label[:10]not in F and label[1:]not in F and label not in SIX
params=list(range(4,45))+[53,71,101];reads_count=windows=0
for n in params:
 word=''.join('RLLR'*j+'L'+'RLLR'*j+'RLL'+'RLLR'*j+'L'+'RLLR'*j+'L'for j in range(n,0,-1))
 p=0j;h=1j;last={};seed=set();trace=[]
 for c in word:
  trace.append((p,h))
  if p in last:assert last[p]!=c
  elif c=='L':seed.add(p)
  last[p]=c;h*=(-1j if c=='R'else 1j);p+=h
 assert len(seed)==11*n+2
 owners={z:z for z in seed};cursor=('initial head',);before=[]
 for c,(p,h)in zip(word,trace):
  before.append(cursor)
  if c=='R':assert p not in owners;owners[p]=cursor
  else:cursor=owners.pop(p)
 pairs=set();endpoints=set();cnt=0
 for k in range(1,n):
  j=n-k;t=k*(16*n+6)-8*k*(k-1);west=t+4*j+1
  expected=[complex(-2*s,2*n+1)for s in range(1,j+1)for _ in range(4 if s<j else 3)]
  assert before[west+2:west+4*j+1]==expected
  for l in range(n-k-2):
   a=west+2+4*l;b=a+11;rs=[complex(-2*s,2*n+1)for s in range(l+1,l+4)]
   assert word[a:b]==label and before[a:b]==[rs[0]]*4+[rs[1]]*4+[rs[2]]*3
   assert b-1==t+4*j+13+4*l
   assert trace[b-1]==(complex(-k-2*l-7,2*n-k),-1)
   assert b-1 not in endpoints;endpoints.add(b-1)
   pairs.update(frozenset(q)for q in combinations(rs,2));cnt+=1
 assert cnt==(n-3)*(n-2)//2 and len(pairs)==2*n-5
 windows+=cnt;reads_count+=len(word)
N=ROOT/'cut_order_obstruction_2026-10-23/mass_sensitive/repeated_initial_root_pairs.md'
out=dict(status='PASS independent literal passive-owner windows and root-pair inventory',parameters=len(params),literal_reads=reads_count,selected_windows=windows,note_sha256=hashlib.sha256(N.read_bytes()).hexdigest(),scope='All-n owner induction separately checked against the signed adjacent-circuit overlap. No bounded-use charge to co-occurring initial-root pairs; not a fixed-mass counterexample or rejection of an O(m^2) bound.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
