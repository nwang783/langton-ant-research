from pathlib import Path
from collections import Counter
import json
D=((0,1),(1,0),(0,-1),(-1,0))
def ep(q):
 x,y=q;a,b=(1,1) if (x+y)%2==0 else (1,-1)
 return ((2*x-a,2*y-b),(2*x+a,2*y+b))
def edge_components(cells):
 remaining=set(cells);out=[]
 while remaining:
  a=remaining.pop();piece={a};vertices=set(ep(a));changed=True
  while changed:
   changed=False
   for q in list(remaining):
    if vertices.intersection(ep(q)):
     remaining.remove(q);piece.add(q);vertices.update(ep(q));changed=True
  out.append(piece)
 return out
def f(a):return 3**abs(a)-1
def norm(C,ax):
 zz=[x+(y if ax=='v' else -y) for x,y in C]
 return min(sum(f(z-c) for z in zz) for c in range(min(zz),max(zz)+1))
B=set();p=(0,0);h=0;boards=[set(B)];poses=[(p,h)];reads=[]
for t in range(17):
 bit=p in B;reads.append((p,'L' if bit else 'R'))
 h=(h+(-1 if bit else 1))%4;B^={p};p=(p[0]+D[h][0],p[1]+D[h][1])
 boards.append(set(B));poses.append((p,h))
assert poses[9]==poses[17]==((-1,0),3)
word=''.join(c for p,c in reads[9:17]);assert word=='LRRRRLLL'
E=boards[9]^boards[17];parts=edge_components(E)
expected=[{(-2,-1),(-2,0)},{(0,-1),(0,0)}]
assert {frozenset(C) for C in parts}=={frozenset(C) for C in expected}
counts=Counter(q for q,c in reads[9:17]);restored=set(counts)-E
assert restored=={(-1,-1),(-1,0)} and all(counts[q]==2 for q in restored)
assert len(edge_components(set(counts)))==1
for ax in ('v','u'):
 assert all(norm(C,ax)==2 for C in parts)
 assert norm(E,ax)==12
# Exact signed x+y gain by component, sector +1.
def gain(C,c):
 return sum(-(1 if (x+y)%2==0 else -1)*(1 if (x,y) in boards[17] else -1)*f(x+y-c) for x,y in C)
assert [gain(C,-3) for C in expected]==[-2,18]
assert [gain(C,0) for C in expected]==[18,-2]
assert min(sum(gain(C,c) for C in expected) for c in range(-10,10))==8
# Exact continuous-cursor port correction, with one center per read region.
def J(p,h,c):
 a=sum(p)-c;value=f(a);e=1 if h in (0,1) else -1
 return value//2 if e*a>=0 else -3*value//2
increments=[]
for r in range(9,17):
 q=reads[r][0];c=-2 if q in expected[0] else -1 if q in expected[1] else -2
 increments.append(J(*poses[r+1],c)-J(*poses[r],c))
assert increments==[3,1,-1,1,-1,1,1,-1] and sum(increments)==4
assert gain(expected[0],-2)+gain(expected[1],-1)+sum(increments)==8
out={'status':'all exact literal controls passed','actual_blank_interval':[9,17],
 'same_pose':[[-1,0],'W'],'word':word,'duration':8,
 'complete_XOR_components':[sorted(C) for C in expected],
 'restored_read_edges':sorted(restored),'component_norm_sum_each_diagonal':4,
 'complete_XOR_norm_each_diagonal':12,'minimum_signed_gain':8,'port_head_increments':increments,'port_debt':sum(increments),
 'scope':'Actual finite trajectory countercontrol to additive net-support-component return charging.'}
Path(__file__).with_name('causal_component_countercontrol.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
