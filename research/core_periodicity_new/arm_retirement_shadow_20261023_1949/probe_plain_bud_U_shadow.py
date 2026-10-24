from pathlib import Path
exec((Path(__file__).resolve().parent/'literal_helpers.py').read_text())
L={(0,0),(0,1),(1,0),(1,1)};R=set(map(tuple,G[7]['outputs']));goal=7;gp=(5,4);gh=3;gc=chords(goal,gp,gh);gctx={place(q[:2],gp,gh)for q in G[goal]['requirements']}
def ep(a,p,h):
 x,y,dh=G[a]['endpoint'];return place((x,y),p,h),(h+dh)%4
def single(hit,p):return hit==[[str(p[0]),str(p[1])]]or hit==[list(p)]
cases=[(first,(0,4),0,(3,5)if first==1 else(2,5),[(7,(0,0),0)])for first in(1,4,5,6)]+[(a,(1,5),0,(3,5),[(7,(0,0),0),(0,(0,4),0)])for a in(0,1,4,5,6)]
for first,fp,fh,z,past in cases:
 assert z in{place(q,fp,fh)for q in G[first]['outputs']};assert z in gctx
 fullpast=past+[(first,fp,fh)];surv=[]
 for a in IDS:
  for h in range(4):
   for si,q in enumerate(G[a]['inputs']):
    p=sub(z,rot(q,h));cc=chords(a,p,h);end,eh=ep(a,p,h)
    if(sum(p)+h)%2:continue
    if {place(q[:2],p,h)for q in G[a]['requirements']}&R:continue
    if a in(7,8,9)and {place(q,p,h)for q in L}&gctx:continue
    bad=False
    for b,bp,bh in fullpast:
     old=chords(b,bp,bh);be,bh2=ep(b,bp,bh)
     for i,ch in enumerate(old):
      for j,new in enumerate(cc):
       hit=contact(*ch,*new)
       if hit and not(i==len(old)-1 and j==0 and(p,h)==(be,bh2)and single(hit,ch[1])):bad=True
    if bad:continue
    for i,ch in enumerate(cc):
     for j,new in enumerate(gc):
      hit=contact(*ch,*new)
      if hit and not(i==len(cc)-1 and j==0 and(end,eh)==(gp,gh)and single(hit,ch[1])):bad=True
    if bad:continue
    surv.append((a,p,h,end,eh))
 print('PRODUCER',first,fp,'guard',z,'surv',len(surv),surv)
for p in((0,4),(1,5)):
 print('immediate USTAR',p,{place(q,p,0)for q in L}&gctx)
