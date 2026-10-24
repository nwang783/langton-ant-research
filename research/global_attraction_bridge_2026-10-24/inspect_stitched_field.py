from probe_stitched_continuation import *
from return_guide_geometry import endpoints,component

def uv(v):X,Y=v;return((X+Y-2)//4,(X-Y)//4)
def graph(B,k):
 g={}
 for q in B:
  a,b=map(uv,endpoints(q,k));g.setdefault(a,[]).append((b,q));g.setdefault(b,[]).append((a,q))
 return g
for q in(3,5):
 B,p,h,z=final(q);k=wwhich(p,h);g=graph(B,k);origin={tuple(x):s for x,s in z['labels']};remain=set(B);print('q',q,'head',p,h,'w',uv(cursors(p,h)[1]))
 while remain:
  e=min(remain);C=component(B,k,endpoints(e,k)[0]);remain-=C;cg=graph(C,k);tip=sorted(a for a in cg if len(cg[a])==1);branches=sorted(a for a in cg if len(cg[a])>2)
  if len(C)>5: print(len(C),{s:sum(origin[e]==s for e in C)for s in set(origin.values())},'tips',tip,'branches',branches)
