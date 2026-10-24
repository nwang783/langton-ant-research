"""Exploratory actual continuation of exact chamfered frames. No capture proof."""
from pathlib import Path
import json,sys
sys.path.insert(0,str(Path(__file__).parent));from probe_square_frames import profile
D=((0,1),(1,0),(0,-1),(-1,0))
def run(r,k,limit=100000):
 I,O,w=profile('LRRL','RL'*k+'R',r);B=set(O);p=(0,0);h=1;out=[];poses=[];returns=[]
 target={ (x,y+2)for x,y in profile('LRRL','RL'*(k+2)+'R',r)[0]}
 for t in range(limit):
  if h==1 and abs(p[0])<=2 and -2<=p[1]<=3:
   delta=len(B^target);returns.append([t,list(p),len(B),delta])
   if p==(0,2)and B==target:return dict(r=r,k=k,status='EXACT_TWO_LAYER_HIT',t=t,returns=returns,word=''.join(out))
  poses.append((p,h));black=p in B;out.append('L'if black else'R');B.symmetric_difference_update({p});h=(h+(3 if black else 1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
  if t>=1040 and t%104==0 and ''.join(out[-1040:])==''.join(out[-104:])*10:
   return dict(r=r,k=k,status='SAMPLED_104_NOT_PROOF',checked_t=t+1,pose=[list(p),h],returns=returns,word=''.join(out))
 return dict(r=r,k=k,status='UNKNOWN_HORIZON',t=limit,returns=returns,word=''.join(out))
if __name__=='__main__':
 R=[run(r,k)for r,k in[(0,0),(0,10),(10,0),(10,10),(20,20),(30,10),(10,30),(40,20),(20,40)]]
 dest=Path(__file__).with_suffix('.json');dest.write_text(json.dumps(R,indent=2)+'\n');print(json.dumps([{z:v for z,v in r.items()if z!='word'}for r in R],indent=2))
