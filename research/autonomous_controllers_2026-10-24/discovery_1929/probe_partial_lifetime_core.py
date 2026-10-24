import json,collections
from check_extremal_read_coupling import D
from partial_drift31_graph import quotient31
for j,H0 in enumerate(json.load(open('middle_short_coincident_C_cycles_certificate.json'))['six_open_T0_through_T10_interfaces']):
 H={int(t):h for t,h in H0.items()};A={};B={};out={};nodes={(t,r)for t,hs in H.items()for r in range(len(hs))};roots={};unknown={}
 for t,hs in H.items():
  for r in range(0,len(hs)-1,2):A[t,r]=((t,r+1),0);A[t,r+1]=((t,r),0)
  if len(hs)%2:roots[(t,len(hs)-1),'A']=(t,0)
  for d in range(4):
   src=[r for r,h in enumerate(hs)if(h+(1 if r%2==0 else-1))%4==d];q,k=quotient31((-t+D[d][0],D[d][1]));u=-q[0]
   dst=[r for r,h in enumerate(H[u])if h==d]if u in H else None
   if dst is not None:assert len(src)==len(dst)
   for ordinal,r in enumerate(src):
    target=(u,dst[ordinal])if dst is not None else('ext',u,d,ordinal)
    out[t,r]=(target,k);nodes.add(target)
 for v,(u,zero)in A.items():
  x,k=out[v];y,l=out[u];B[x]=(y,l-k)
 for (v,side),(t,z)in list(roots.items()):
  u,k=out[v];roots[u,'B']=(t,-k)
 for v in nodes:
  if v not in A and(v,'A')not in roots:unknown[v,'A']=True
  if v not in B and(v,'B')not in roots:unknown[v,'B']=True
 unseen=set(nodes);components=[]
 while unseen:
  seed=next(iter(unseen));stack=[seed];lv={seed:0};verts=set();cy=[]
  while stack:
   v=stack.pop();verts.add(v);unseen.discard(v)
   for M in [A,B]:
    if v not in M:continue
    u,k=M[v]
    if u in lv:
     if lv[u]!=lv[v]+k:cy.append(lv[v]+k-lv[u])
    else:lv[u]=lv[v]+k;stack.append(u)
  ends=[]
  for v in verts:
   for s,M in [('A',A),('B',B)]:
    if v not in M:
     if(v,s)in roots:
      t,k=roots[v,s];ends.append(('root',t,lv[v]+k))
     else:ends.append(('open',v,s,lv[v]))
  assert len(ends)in[0,2]
  components.append((len(verts),ends,cy))
 print('INTERFACE',j,'roots',[x for x in components if any(a[0]=='root'for a in x[1])],'cycles',[x for x in components if not x[1]])
