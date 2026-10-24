#!/usr/bin/env python3
from boundary_probe import *
from collections import deque

def components(B):
    if not B:return []
    V={v for e in B for v in e};x0=min(x for x,y in V)-1;x1=max(x for x,y in V)+1;y0=min(y for x,y in V)-1;y1=max(y for x,y in V)+1
    seen=set();comps=[]
    for v in V:
        if v in seen:continue
        q=[v];seen.add(v);esc=False;i=0;E=0
        while i<len(q):
            v=q[i];i+=1
            if v[0] in (x0,x1) or v[1] in (y0,y1):esc=True
            for d in range(4):
                if edge(v,d) in B:continue
                w=(v[0]+DIR[d][0],v[1]+DIR[d][1])
                if not(x0<=w[0]<=x1 and y0<=w[1]<=y1):continue
                E+=1
                if w not in seen:seen.add(w);q.append(w)
        if not esc:comps.append(dict(vertices=len(q),edges=E//2,cycle_rank=E//2-len(q)+1,points=sorted(q)))
    return comps

if __name__=='__main__':
 B=set();dart=((0,0),0);best=0;out=[]
 for t in range(20001):
    if t%100==0:
      C=components(B)
      if C:
        M=max(C,key=lambda c:c['vertices'])
        if M['vertices']>best or any(c['cycle_rank'] for c in C):
            out.append(dict(t=t,max_component=M,num_components=len(C),total_cycle_rank=sum(c['cycle_rank'] for c in C)));best=max(best,M['vertices'])
            if any(c['cycle_rank'] for c in C):break
    E=edge(*dart);nxt=perm(dart,B)
    if E in B:B.remove(E)
    else:B.add(E)
    dart=nxt
 print(json.dumps(out,indent=2))
