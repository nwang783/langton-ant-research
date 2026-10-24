from probe_stitched_continuation import *
from return_guide_geometry import cells_of,xy,endpoints,connected,component
uv=lambda v:((v[0]+v[1]-2)//4,(v[0]-v[1])//4)

def joins(A,k):
 g={}
 for e in A:
  u,v=endpoints(e,k);g.setdefault(u,[]).append(v);g.setdefault(v,[]).append(u)
 tips=[u for u in g if len(g[u])==1];J=set()
 for u in tips:
  for v in tips:
   a,b=uv(u),uv(v)
   if abs(a[0]-b[0])+abs(a[1]-b[1])==1:
    e=next(iter(cells_of([a,b])))
    if e not in A:J.add(e)
 return J
for q in(3,5,7):
 B,p,h,z=final(q);k=wwhich(p,h);A={tuple(x)for x,s in z['labels']if s=='second'};J=joins(A,k);AP=A|J
 start=xy((1,-2));vs=ordered_path(AP,k,start);wv=list(map(uv,vs)); print('q',q,'A',len(A),'J',len(J),'ends',wv[0],wv[-1])
 for hh in range(4):
  off=__import__('check_renewal_archive').r((1,-1),hh) if False else None
  for pp in[(x,y)for x in range(-4,5)for y in range(-4,5)if cursors((x,y),hh)[1]==start]:
   BB=B|J;ph=hh;pos=pp;first_r=0
   while pos not in BB and first_r<4:first_r+=1;pos,ph=step(BB,pos,ph)
   # Build fixed positive path word using entry turn count then replay on untouched input.
   word=path_word(wv,first_r);BB=B|J;pos=pp;ph=hh;ordinary=True;bad=None
   for t,c in enumerate(word):
    if c!=('L'if pos in BB else'R'):bad=(t,pos,c,'L'if pos in BB else'R');break
    if c=='L'and connected(BB-{pos},k,*endpoints(pos,k)):ordinary=False
    pos,ph=step(BB,pos,ph)
   print('entry',pp,hh,'r',first_r,'gain',word.count('R')-word.count('L'),'bad',bad,'ordinary',ordinary)
