from ancestry import simulate
from collections import Counter
import json
G={(0,-1),(1,1),(1,3),(2,2)}
def ccw(q):return(-q[1],q[0])
def root_labels(d):
 labels=[]
 for a in d['nodes']:
  p=a['parent'];labels.append(0 if p is None else p if p<0 else labels[p])
 return labels
D=simulate(10000,{ccw(q) for q in G}); lab=root_labels(D)
last=[a for a in D['nodes'] if 9000<=a['time']<9900]
print('initial ordered',D['initial'])
print('late node roots',Counter(lab[a['id']] for a in last))
# Identify eventual spine nodes without assuming phase alignment: parent repeated after104.
bytime={a['time']:a for a in D['nodes']};same={}
for a in last:
 p=D['nodes'][a['parent']]
 same[a['time']%104]=(p['time']%104,a['time']-p['time'])
cycles=[];done=set()
for s in same:
 path=[];seen={};v=s
 while v not in done and v not in seen:
  seen[v]=len(path);path.append(v);v=same[v][0]
 if v in seen:cycles.append(path[seen[v]:])
 done.update(path)
cycph={v for c in cycles for v in c}
print('cycles',cycles,'spine roots',Counter(lab[a['id']] for a in last if a['time']%104 in cycph))
print('root0 nodes',sum(l==0 for l in lab),'lasttime',max(a['time'] for a,l in zip(D['nodes'],lab) if l==0))
