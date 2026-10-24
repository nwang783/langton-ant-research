#!/usr/bin/env python3
"""Complete necessary four-cell chronology classification. Open outside ports.
Does not imply global realizability. No package imports from discovery code.
"""
from itertools import product
import json
from pathlib import Path
D=((0,1),(1,0),(0,-1),(-1,0))
POS=((0,0),(0,1),(-1,1),(-1,0)); HEAD=(0,3,2,1)
def states(p):
 axis=1 if sum(p)%2==0 else 0
 out=[('0',[])]
 for h in (axis,(axis+2)%4):
  out.extend([('R'+str(h),[(1,h)]),('D'+str(h),[(1,h),(-1,h)]),('S'+str(h),[(1,h),(-1,(h+2)%4)]),('A'+str(h),[(1,h),(-1,h),(1,(h+2)%4)]),('B'+str(h),[(1,h),(-1,(h+2)%4),(1,(h+2)%4)])])
 return out
SS=[states(p) for p in POS]
def check(sts):
 n=12; eq=[[] for _ in range(n)]; flow=[]
 for i in range(4):
  nxt=(i+1)%4;h=HEAD[i]
  out=[j for j,(c,hh) in enumerate(sts[i][1]) if (hh+c)%4==h]
  inc=[j for j,(c,hh) in enumerate(sts[nxt][1]) if hh==h]
  if len(out)!=len(inc):return
  flow.append(len(out))
  for j,k in zip(out,inc):eq[3*i+j].append((3*nxt+k,1));eq[3*nxt+k].append((3*i+j,-1))
 # Collapse exact equalities T_b=T_a+delta.
 grp={};off={};ng=0
 active=[3*i+j for i,s in enumerate(sts) for j in range(len(s[1]))]
 for a in active:
  if a in grp:continue
  grp[a]=ng;off[a]=0; todo=[a]
  while todo:
   x=todo.pop()
   for y,d in eq[x]:
    if y in grp:
     if off[y]!=off[x]+d:return
    else:grp[y]=ng;off[y]=off[x]+d;todo.append(y)
  ng+=1
 # Distinct events cannot have exactly forced equal times.
 if len({(grp[x],off[x]) for x in active})<len(active):return
 # Every equality component is a contiguous chronological successor chain.
 # Distinct components therefore occupy disjoint time intervals. Each
 # intercomponent history-order constraint forces the entire block order.
 succ=[set() for _ in range(ng)]
 for i,s in enumerate(sts):
  for j in range(len(s[1])-1):
   a=3*i+j;b=a+1
   if grp[a]==grp[b]:
    if off[a]>=off[b]:return
   else:succ[grp[a]].add(grp[b])
 color=[0]*ng
 def dfs(a):
  if color[a]==1:return False
  if color[a]==2:return True
  color[a]=1
  if not all(dfs(b) for b in succ[a]):return False
  color[a]=2;return True
 if not all(dfs(a) for a in range(ng)):return
 hc=''.join(sts[i][0][0] if flow[i-1]==flow[i]==1 else '.' for i in range(4))
 dc=''.join(sts[i][0][0] if flow[i-1]==flow[i]==2 else '.' for i in range(4))
 return ''.join(map(str,flow)),hc,dc
if __name__=='__main__':
 out={};num=0
 for sts in product(*SS):
  a=check(sts)
  if a:
   f,h,d=a;out.setdefault(f,{}).setdefault(h+'|'+d,[]).append([s[0] for s in sts]);num+=1
 fn=Path(__file__).with_suffix('.json');fn.write_text(json.dumps(out,indent=2)+'\n')
 print('retained',num,'flow patterns',len(out))
 for f,cs in sorted(out.items()):print(f,' '.join(sorted(cs)))
