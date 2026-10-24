from synthesize_third_return import *
Dphys=((0,1),(1,0),(0,-1),(-1,0))
q=5;B,p,h,z=final(q);A={tuple(x)for x,s in z['labels']if s=='second'};J=joins(A,0);hist=get_history(z)
forbid={uv(v)for e in set(hist)|set(map(tuple,z['initial']))|J for v in endpoints(e,0)}
vs=list(map(uv,ordered_path(A|J,0,xy((1,-2)))))
for i,v in enumerate(vs[:35]):
 for hh in range(4):
  for xx in range(v[0]+v[1]-1,v[0]+v[1]+3):
   for yy in range(v[0]-v[1]-1,v[0]-v[1]+3):
    pp=(xx,yy)
    if uv(cursors(pp,hh)[1])!=v:continue
    p0=(pp[0]-Dphys[hh][0],pp[1]-Dphys[hh][1]);h0=(hh+1)%4;u=uv(cursors(p0,h0)[1]);pb=(p0[0]-Dphys[h0][0],p0[1]-Dphys[h0][1]);hb=(h0+1)%4;pre=uv(cursors(pb,hb)[1])
    if u in forbid or pre in forbid:continue
    bb=B|J;pos=pp;ph=hh;r=0
    while pos not in bb and r<4:r+=1;pos,ph=step(bb,pos,ph)
    if r>2:continue
    ww=path_word(vs[i:],r);bb=B|J;pos=pp;ph=hh;bad=None
    for t,c in enumerate(ww):
     if c!=('L'if pos in bb else'R'):bad=t;break
     pos,ph=step(bb,pos,ph)
    if bad is None:print('candidate',i,pp,hh,'r',r,'gain',ww.count('R')-ww.count('L'),'reset',p0,h0,'root',u,'pre',pre)
