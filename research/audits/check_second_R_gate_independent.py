from pathlib import Path
from itertools import product
from collections import defaultdict,Counter
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]; B=ROOT/'rank_two_plateau_2026-10-23'; D=((0,1),(1,0),(0,-1),(-1,0))
# Literal alternating histories, generated as port-bit strings; no candidate imports.
def hs(axis,n):
 for bits in product(range(2),repeat=n):
  yield tuple(axis+2*b for b in bits)
def out(h,j):return (h+(1 if j%2==0 else -1))%4
def kind(h,face):
 n=sum(x==face for x in h[::2]);o=len(h[::2])-n
 return None if n==0 or n<o else ('single_R_boundary' if n+o==1 else 'flat_two_R' if n==o else 'same_face_defect')
ordinal=[]
for n in (3,4):
 for h in hs(1,n):
  a=1+sum(x==h[2] for x in h[:2]); b=1+sum(out(x,j)==out(h[2],2)for j,x in enumerate(h[:2]))
  assert sorted((a,b))==([2,3]if h[0]==h[2]else[1,2])
  ordinal.append((h,a,b,'same_face_defect'if h[0]==h[2]else'flat_two_R'))
pairs=[]
for ns in range(1,5):
 for s in hs(0,ns):
  sk=kind(s,0)
  if sk is None:continue
  uses=[j for j,h in enumerate(s)if out(h,j)==1]
  for nt in(3,4):
   for t in hs(1,nt):
    tk=kind(t,1)
    if tk is None or t[2]!=1 or len(uses)!=t.count(1):continue
    ordinal2=t[:3].count(1);j=uses[ordinal2-1]
    pairs.append((s,t,sk,tk,len(uses),ordinal2,j,j//2*2))
    if j<2:
     if tk=='same_face_defect':
      assert ordinal2==2 and j==1 and out(s[0],0)==out(s[1],1)==1
      assert s[0]!=s[1]and t[0]==t[2]!=t[1]
     elif ordinal2==1 and j==1:
      assert sk=='flat_two_R'and out(s[0],0)!=out(s[1],1)
     elif ordinal2==2:
      assert j==1 and out(s[0],0)==out(s[1],1)
J=json.loads((B/'paired_r_controls.json').read_text())
assert set(ordinal)=={(tuple(r['incoming']),r['input_ordinal'],r['output_ordinal'],r['kind'])for r in J['ordinal_rows']}
assert set(pairs)=={(tuple(r['source']),tuple(r['target']),r['source_class'],r['target_class'],r['edge_flow'],r['target_second_R_input_ordinal'],r['supplier_rank'],r['source_pair_R_rank'])for r in J['compatible_pairs']}
assert len(ordinal)==24 and len(pairs)==78
# Enumerate complete words; infer a finite input board from first read, then
# compare each repeated read against the accumulated flip parity.
def literal(w):
 p=(0,0);h=0;black=set();first={};hist=defaultdict(list)
 for t,c in enumerate(w):
  desired=c=='L'
  if p not in first:first[p]=desired;black.update([p]if desired else[])
  if (p in black)!=desired:return None
  hist[p].append((t,h,c));black.symmetric_difference_update({p})
  h=(h+(1 if c=='R'else-1))%4;v=D[h];p=(p[0]+v[0],p[1]+v[1])
 return p,h,hist,{p for p,v in first.items()if v}
returns=[]
for n in(4,8,12,16):
 candidates=[];gates=[]
 for suffix in product('LR',repeat=n-2):
  w='RR'+''.join(suffix);a=literal(w)
  if a is None:continue
  p,h,H,seed=a
  if p!=(0,0)or h!=2 or len(H[0,0])!=1:continue
  candidates.append(w)
  if len(H[1,0])==2 and H[1,0][0]==(1,1,'R')and H[1,0][1][1:]==(3,'L'):
   a2=literal(w+'LR');assert a2 is not None;gates.append(w)
 returns.append(dict(n=n,candidates=sorted(candidates),gates=sorted(gates)))
A=json.loads((B/'gate_word_enumeration.json').read_text())
for r,s in zip(returns,A['returns']):
 assert r['n']==s['span']and r['candidates']==sorted(x['word']for x in s['opposite_first_return_candidates'])and r['gates']==sorted(x['word']for x in s['gates'])
assert [len(r['candidates'])for r in returns]==[0,0,2,13]
assert [len(r['gates'])for r in returns]==[0,0,0,1]
seed={(-1,-1),(-1,0),(0,-1),(1,-1),(2,-1),(2,0)}
def simulate(seed,n):
 b=set(seed);p=(0,0);h=0;H=defaultdict(list);w=''
 for t in range(n):
  c='L'if p in b else'R';w+=c;H[p].append((t,h,c));b.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;v=D[h];p=(p[0]+v[0],p[1]+v[1])
 return w,H
w,H=simulate(seed,18);assert w=='RRLLLLRLRRLRRLRRLR';assert H[0,0]==[(0,0,'R'),(16,2,'L')];assert H[1,0]==[(1,1,'R'),(5,3,'L'),(17,1,'R')]
w,H=simulate(set(),52);assert H[1,-1]==[(2,2,'R'),(50,0,'L')];assert H[0,-1]==[(3,3,'R'),(15,1,'L'),(51,3,'R')]
# Fresh exact three-port inventory for the subsequent E-to-E nesting addendum.
triples=[]
for n in range(3,5):
 for h in hs(1,n):
  arrivals=[j for j,x in enumerate(h)if x==1]
  if len(arrivals)<3:continue
  assert arrivals[2]in(2,3)
  k=kind(h,1);triples.append(dict(incoming=h,third_target_rank=arrivals[2],type=k))
  if h[:3]==(1,3,1):assert arrivals[:3]==[0,2,3]
assert len(triples)==6
result=dict(status='PASS independent local ordinal/supplier reconstruction and synchronized gate exhaustion',two_R_rows=len(ordinal),max_C_compatible_pairs=len(pairs),returns=returns,exact_gate_minimum=16,six_black_positive=True,blank_positive_span=48,three_port_target_rows=triples,scope='Complete white cap-four paired-R gate/corridor necessity; no existence of homogeneous second-R cycles or global gate budget. Gate local sharpness allows arbitrary colors elsewhere. Mixed paired-R cycle clock retains total winding k.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
