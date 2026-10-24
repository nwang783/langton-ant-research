D=[(0,1),(1,0),(0,-1),(-1,0)]
B=set();x=y=h=0;st=[];c=0;largest=-999;oldM=None
for t in range(1000):
 # Frozen active loop, with current reduced lift as prefix.
 p0=(x,y,h);xx,yy,hh=p0;ss=[list(z) for z in st];cc=c;M=cc;k=0
 while True:
  a=-1 if (xx,yy) in B else 1
  cc+=a
  if ss and ss[-1][0]==a:
   ss[-1][1]+=1
   if ss[-1][1]==4:ss.pop();cc-=4*a
  else:ss.append([a,1])
  M=max(M,cc);hh=(hh+a)%4;dx,dy=D[hh];xx+=dx;yy+=dy;k+=1
  if (xx,yy,hh)==p0:break
  assert k<10000
 if M>largest:largest=M;print('newmax',t,M,c,'looplength',k)
 if oldM is not None and M>oldM:print('increase',t,oldM,M)
 if M>3:print('FAIL',t,M,c,sorted(B),st);break
 oldM=M
 a=-1 if (x,y) in B else 1
 if a<0:B.remove((x,y))
 else:B.add((x,y))
 c+=a
 if st and st[-1][0]==a:
  st[-1][1]+=1
  if st[-1][1]==4:st.pop();c-=4*a
 else:st.append([a,1])
 h=(h+a)%4;dx,dy=D[h];x+=dx;y+=dy
