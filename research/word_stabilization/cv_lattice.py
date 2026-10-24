from verify_macro_word import D,rot
# z0=(-.5,.5), displacement basis d=(1,3), e=(-3,1), pose at a,b,h determined.
def pose(a,b,h):
 f=rot((0,1),h);r=rot((1,0),h)
 return ((-1+2*a-6*b-f[0]+r[0])//2,(1+6*a+2*b-f[1]+r[1])//2)
def occurrences(q,alphabet='CV'):
 out=[]
 for k in alphabet:
  for h in range(4):
   for z in D[k]['trace']:
    dx,dy=rot(z['p'],h);p=(q[0]-dx,q[1]-dy);p0=pose(0,0,h);x,y=p[0]-p0[0],p[1]-p0[1]
    if (x+3*y)%10==0 and (-3*x+y)%10==0:
     a=(x+3*y)//10;b=(-3*x+y)//10
     out.append((a,b,h,k,z['i'],z['c']))
 return out
if __name__=='__main__':
 for q in [(1,2),(-1,0),(0,0),(0,2)]:print(q,occurrences(q))
