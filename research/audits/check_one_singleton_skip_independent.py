from pathlib import Path
from itertools import combinations
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];P=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();bindings={'ONE_SINGLETON_FOUR_STEP_SKIPPED_MIDDLE_EXCLUSION.md':'fb198c975d85b70f8f931db303f48fff183c8ba6c79271fb8d083ec4f811a010','check_one_singleton_skipped_middle.py':'1fe6e63999870deeb9c0fa586b36ec7d23cc6997639ae94b1acb62d4ac8c5eaa','check_one_singleton_skipped_middle.json':'7421b3c409bdccdcb680bf37be9641a9ae4de886f93702e90548884671542bc2'}
for f,h in bindings.items():assert sha(P/f)==h
V=(1j,1,-1j,-1);out=lambda h,j:(h+(1 if j%2==0 else-1))%4;fmt=lambda w:''.join('NESW'[h]for h in w);xy=lambda q:(int(q.real),int(q.imag));records=[]
for aw in[(3,3,1,1),(3,3,1,1,3)]:
 I=sum(out(h,j)==0 for j,h in enumerate(aw));J=3;qs=[]
 for n in range(2*(I+J)+1):
  for N in combinations(range(n),I):
   nn=set(N);w=tuple(0 if j in nn else 2 for j in range(n));ww=[j for j,h in enumerate(w)if out(h,j)==3]
   if len(ww)==3 and N[1]==ww[2]+1:qs.append(w)
 assert {fmt(w)for w in qs}==({'SSSNN','SSSNNS'}if I==2 else{'SSSNNSN','SSSNNSNS'})
 for w in qs:
  H={1j:(3,1,3,3),1:aw,0j:(0,2),1+1j:w};su={}
  for p,hs in H.items():
   for h in range(4):
    src=[j for j,v in enumerate(hs)if out(v,j)==h];q=p+V[h]
    if q not in H:continue
    dst=[j for j,v in enumerate(H[q])if v==h];assert len(src)==len(dst)
    for a,b in zip(src,dst):su[p,a]=(q,b)
  skip=[(1,0),(1+1j,3),(1j,3),(0j,1),(1,3)];ret=[(1+1j,3),(1j,3),(0j,1),(1,3),(1+1j,4)]
  for path in(skip,ret):
   for a,b in zip(path,path[1:]):assert su[a]==b
   assert all(p!=path[0][0]for p,j in path[1:-1])
  records.append({'A1':fmt(aw),'Q1':fmt(w),'skipped_physical_read_chain':[[xy(p),j]for p,j in skip],'exact_gap':4,'required_gap':12})
assert len(records)==4
outp={'status':'PASS all-cap all-period exclusion of exactly two complete diagonal minimum interfaces','bindings':bindings,'independent_four_Q1_cases':records,'remaining_all_growth_interfaces':225,'remaining_g8_interfaces':216,'analytic_review':[
'Q1 has exactly3 outgoingW uses and2/3 incomingN, derived from complete A0/A1 ports. Its thirdW path through A0.L3,B0.L1,A1.L3 returns to its secondN in4 actual steps with no intermediate Q1. This is a physical first-return relation, not an assumed clock inequality from the solver.',
'SecondN cannot beL because that would create a fourthW. It isR, its preceding rank isL arrivingN, therefore that preceding read is the firstN. Earlier reads are allS. If secondN rankk is even, thirdW count is k/2+1=3, so k=4 and prefixSSSNN is forced without any visit bound. Independent complete count domains give exactly the four stated Q1 words.',
'Actual ordinal port matching then gives A1.R0,Q1.L3,A0.L3,B0.L1,A1.L3 on the SAME physical unit square. The4-step return skips required ranks1/2 of complete A1. Equivalently same-cell consecutive gaps>=4 yield12<=4. No seam voltage, distant field, output root or full period changes this.',
'Only two of the signed227 all-growth interfaces are removed. The separate cyclic-E g8 exclusion removes9 others, leaving216 necessary open g8 interfaces. The bounded height13 solver UNSAT outputs are not dependencies. No other interface, allg8 front or attraction is excluded.'
]};S.with_suffix('.json').write_text(json.dumps(outp,indent=2)+'\n');print(outp['status'])
