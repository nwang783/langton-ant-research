from pathlib import Path
import json
D=((0,1),(1,0),(0,-1),(-1,0))
CAP={(1,-1),(1,0),(-1,1),(0,1),(-3,0),(-3,1),(-2,-1),(-1,-1),(-2,1)}
def initial(n):
 B=set(CAP)
 for j in range(2,n+1):B.update({(j,-j),(j,j-1),(j-1,j),(-j-2,1-j),(-j-2,j),(-j-1,-j),(j-2,-j)})
 return B
def sim(n,T=100000):
 B=initial(n);x=y=h=0;word=[];poses=[]
 for t in range(T):
  poses.append((x,y,h));b=(x,y)in B;word.append('L'if b else'R');B.symmetric_difference_update({(x,y)});h=(h+(-1 if b else 1))%4;dx,dy=D[h];x+=dx;y+=dy
 assert ''.join(word[:2*n])=='RL'*n
 return ''.join(word[2*n:]),[(x-n,y-n,h)for x,y,h in poses[2*n:]],B
if __name__=='__main__':
 runs={n:sim(n)for n in(10,20,40,80,160)};base=runs[160];out=[]
 for n,(w,p,B)in runs.items():
  same=next((i for i,(a,b)in enumerate(zip(w,base[0]))if a!=b),min(len(w),len(base[0])))
  ret=next((i for i,(x,y,h)in enumerate(p)if x<=-n+3 and y<=-n+3),None)
  # Last 104-periodic sample is a diagnostic, not a tail certificate.
  hw=next((t for t in range(len(w)-1040)if all(w[t+i]==w[t+i+104]for i in range(936))),None)
  out.append(dict(n=n,common_prefix_with160=same,near_central_return=ret,sampled_104_start=hw,pose_at_sample=None if hw is None else p[hw],remote_prefix=w[:300]))
  print(out[-1],flush=True)
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
