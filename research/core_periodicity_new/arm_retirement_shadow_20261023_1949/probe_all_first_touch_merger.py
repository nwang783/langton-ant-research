from pathlib import Path
exec((Path(__file__).resolve().parent/'literal_helpers.py').read_text())
def singleton(hit,p):return hit==[[str(p[0]),str(p[1])]]or hit==[list(p)]
def whole_endpoint(a,p,h):
 x,y,dh=G[a]['endpoint'];return place((x,y),p,h),(h+dh)%4
exp={7:[(0,(2,3),3),(1,(2,3),3)],8:[(0,(1,7),2),(4,(2,8),2)],9:[(0,(-3,6),1),(4,(-4,7),1)]}
for s in(7,8,9):
 R=set(map(tuple,G[s]['outputs']));fp,fh=whole_endpoint(s,(0,0),0);z=place((2,0),fp,fh)
 for first in IDS:
  fc=chords(first,fp,fh)
  for goal,gp,gh in exp[s]:
   gc=chords(goal,gp,gh);gctx={place(q[:2],gp,gh)for q in G[goal]['requirements']};gins={place(q,gp,gh)for q in G[goal]['inputs']}
   if first in(7,8,9):
    star={place(q,fp,fh)for q in[(0,0),(0,1),(1,0),(1,1)]};assert star&gctx,(s,first,goal);continue
   assert z in {place(q,fp,fh)for q in G[first]['outputs']};assert z in gctx-gins,(s,first,goal,z)
   surv=[]
   for a in IDS:
    for h in range(4):
     for si,q in enumerate(G[a]['inputs']):
      p=sub(z,rot(q,h));cc=chords(a,p,h);end,eh=whole_endpoint(a,p,h)
      if(sum(p)+h)%2:continue
      if {place(q[:2],p,h)for q in G[a]['requirements']}&R:continue
      bad=False
      for block,bp,bh in[(s,(0,0),0),(first,fp,fh)]:
       old=chords(block,bp,bh);be,bh2=whole_endpoint(block,bp,bh)
       for i,ch in enumerate(old):
        for j,new in enumerate(cc):
         hit=contact(*ch,*new)
         if hit and not(i==len(old)-1 and j==0 and(p,h)==(be,bh2)and singleton(hit,ch[1])):bad=True
      if bad:continue
      for i,ch in enumerate(cc):
       for j,new in enumerate(gc):
        hit=contact(*ch,*new)
        if hit and not(i==len(cc)-1 and j==0 and(end,eh)==(gp,gh)and singleton(hit,ch[1])):bad=True
      if bad:continue
      loc=rot(sub(p,fp),-fh);out=rot(sub(end,fp),-fh);hh=(h-fh)%4
      surv.append((a,loc,hh,out))
   bad=[r for r in surv if not(r[2]==3 and r[1][1]in(0,1)and r[3][1]>=1)]
   print('S,F,G',s,first,goal,'surv',len(surv),'BAD',bad)
