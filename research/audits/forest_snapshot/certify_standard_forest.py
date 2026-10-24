"""Finite exact certificate for ancestry in the entire standard periodic tail.
Only the literal 104-letter word is input; no ant simulator is imported.
All phase/cell equations use integer arithmetic and cover every epoch.
"""
import json
from pathlib import Path
from collections import Counter, defaultdict
HERE=Path(__file__).resolve().parent
W=json.loads((Path('/workspace/shared/langton/recovered_bundle/ant_global/root/standard.json')).read_text())['word']
P=len(W); D=((0,1),(1,0),(0,-1),(-1,0)); OFF=((0,-1),(-1,-1),(-1,0),(0,0))
def plus(a,b):return(a[0]+b[0],a[1]+b[1])
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def scale(k,a):return(k*a[0],k*a[1])
def edge(q):
 x,y=q
 return ((x,y-1),(x-1,y)) if (x+y)%2==0 else ((x-1,y-1),(x,y))
p=(0,0);h=0;pos=[];heads=[];cursor=[]
for c in W:
 pos.append(p);heads.append(h);cursor.append(plus(p,OFF[h]));h=(h+(1 if c=='R' else -1))%4;p=plus(p,D[h])
drift=p;assert h==0 and P==104 and W.count('L')==46 and W.count('R')==58
assert all((pos[i][0]+pos[i][1])%2==heads[i]%2 for i in range(P))
def multiple(v,d):
 for a,b in zip(v,d):
  if b:
   if a%b:return None
   k=a//b;return k if scale(k,d)==v else None
 return 0 if v==(0,0) else None
def qp(t):return plus(pos[t%P],scale(t//P,drift))
def vp(t):return plus(cursor[t%P],scale(t//P,drift))
def letter(t):return W[t%P]
# Every read of the same cell as phase i: phase j, epoch k, with q_j+k*d=q_i.
# These finite 104 comparisons exhaust all integers k, including negative ones.
same={}
for i in range(P):
 times=[]
 for j in range(P):
  k=multiple(sub(pos[i],pos[j]),drift)
  if k is not None:times.append(j+k*P)
 same[i]=sorted(times);assert i in times
 syms=[letter(t) for t in same[i]]
 assert syms[0]=='R' and all(a!=b for a,b in zip(syms,syms[1:]))
# Every L has a unique preceding R. Every R either has one L successor or is eternal.
prev={i:max(t for t in same[i] if t<i) for i in range(P) if W[i]=='L'}
next_read={i:min((t for t in same[i] if t>i),default=None) for i in range(P) if W[i]=='R'}
# Nodes are immediately after an L; use node phase modulo P, allowing node phase 0.
node_phases=sorted((i+1)%P for i,c in enumerate(W) if c=='L')
def owner_node(t):
 # Previous L is at most four earlier letters, and can occur in preceding epoch.
 k=t-1
 while letter(k)!='L':k-=1
 assert t-k<=5
 return k+1
records={}
for c in node_phases:
 death=c-1;b=prev[death%P]+(death//P)*P;a=owner_node(b)
 assert a<c and letter(b)=='R' and qp(b)==qp(death)
 r=0
 while letter(a+r)=='R':r+=1
 assert r in (0,1,2,4)
 # All inserts owned by a share its Tait cursor vertex.
 assert all(vp(a+j)==vp(a) for j in range(r))
 birth_slot=b-a+1;assert 1<=birth_slot<=r
 forward=vp(c)!=vp(a)
 assert vp(a) in edge(qp(b)) and vp(c) in edge(qp(b))
 # Computation of this node's own insertion count, not its parent's.
 cr=0
 while letter(c+cr)=='R':cr+=1
 records[c]=dict(parent_phase=a%P,parent_delay=c-a,child_r=cr,
   birth_slot=birth_slot,forward=forward,spatial_step=sub(vp(c),vp(a)),birth_age=death-b)
cycles=[];done=set()
for start in node_phases:
 if start in done:continue
 seen={};path=[];v=start
 while v not in seen and v not in done:
  seen[v]=len(path);path.append(v);v=records[v]['parent_phase']
 if v in seen:
  phases=path[seen[v]:];delay=sum(records[q]['parent_delay'] for q in phases)
  assert delay>0 and delay%P==0
  cycles.append(dict(phases=phases,winding=delay//P,total_delay=delay))
 done.update(path)
cycle_phases={q for c in cycles for q in c['phases']}
assert len(cycles)==2 and all(len(c['phases'])==2 and c['winding']==1 for c in cycles)
assert all(records[q]['child_r']==4 and records[q]['birth_slot']==2 and records[q]['forward'] and scale(2,records[q]['spatial_step'])==drift for q in cycle_phases)
# Attribute every non-spine node and permanent bud to its unique spine ancestor.
attachments={};maxdepth=0;maxdelay=0
for q in node_phases:
 v=q;depth=0;delay=0
 while v not in cycle_phases:
  depth+=1;delay+=records[v]['parent_delay'];v=records[v]['parent_phase']
  assert depth<=46
 attachments[q]=(v,depth,delay);maxdepth=max(maxdepth,depth);maxdelay=max(maxdelay,delay)
module_nodes=Counter(attachments[q][0] for q in node_phases)
permanent=[i for i in range(P) if W[i]=='R' and next_read[i] is None]
assert len(permanent)==12
module_buds=Counter(attachments[owner_node(i)%P][0] for i in permanent)
max_bud_depth=max(attachments[owner_node(i)%P][1]+1 for i in permanent)
assert max_bud_depth==7
# Every lifetime used in the tail has an explicit age <= maximum below.
output=dict(period=P,drift=drift,read_phase_count=P,node_phase_count=len(node_phases),
 parent_cycles=cycles,cycle_records={q:records[q] for q in sorted(cycle_phases)},
 all_node_records=records,max_black_lifetime_age=max(r['birth_age'] for r in records.values()),
 max_parent_delay=max(r['parent_delay'] for r in records.values()),
 max_cursor_node_bush_depth=maxdepth,max_bud_inclusive_bush_depth=max_bud_depth,max_side_branch_delay=maxdelay,
 module_node_counts=dict(module_nodes),module_permanent_bud_counts=dict(module_buds),
 permanent_bud_phases=permanent,checks='All integer translation-class equations and color alternations passed.')
(HERE/'standard_forest_certificate.json').write_text(json.dumps(output,indent=2))
print(json.dumps({k:v for k,v in output.items() if k!='all_node_records'},indent=2))
