"""Small complete geometric controls of the charge-free unit-pose identity.
No assertion that an internally illegal geometric word is realizable.
"""
import itertools,json,pathlib,collections
D=((0,1),(1,0),(0,-1),(-1,0))
def inspect(w,h0,parent):
 h=h0;x=y=0;counts=[0]*8;own=[];legal=True;last={}
 for j,c in enumerate(w):
  t=2*h+(c=='L');counts[t]+=1
  if t==parent:own.append((j,(x,y)))
  if (x,y) in last and last[x,y]==c:legal=False
  last[x,y]=c
  h=(h+(1 if c=='R' else -1))%4;dx,dy=D[h];x+=dx;y+=dy
 coarse_h=(h0+(1 if parent%2==0 else -1))%4
 if h!=coarse_h or (x,y)!=D[coarse_h]:return None
 delta=counts[:];delta[parent]-=1
 A=delta[1];B=delta[3];z=delta[0]-B
 expected=[B+z,A,A+z,B,B+z,A,A+z,B]
 assert delta==expected and min(delta)>=0
 assert len(w)==1+4*(A+B+z)
 assert w.count('R')-w.count('L')==(1 if parent%2==0 else -1)+4*z
 return dict(A=A,B=B,z=z,legal=legal,self=own)
def main():
 per={};cases=0;leg=0;nonzero=[]
 # All raw words through length13 in the required congruence class;
 # all four headings and both coarse actions, no half-turn inference used.
 for n in (1,5,9,13):
  count=legal=0
  for bits in itertools.product('RL',repeat=n):
   w=''.join(bits)
   for h in range(4):
    for c in range(2):
     o=inspect(w,h,2*h+c)
     if o is None:continue
     count+=1;legal+=o['legal']
     if len(o['self'])==1 and o['self'][0][1]!=(0,0):
      if len(nonzero)<3:nonzero.append(dict(word=w,heading=h,turn=c,**o))
  per[n]=dict(geometric=count,internally_legal=legal);cases+=count;leg+=legal
 out=dict(scope='Exact all-charge incidence identity, complete raw word controls only; no all-length ant obstruction.',per_length=per,total_geometry=cases,total_internal_legal=leg,
 geometric_single_self_nonzero_offset_controls=nonzero)
 p=pathlib.Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
