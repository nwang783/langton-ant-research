"""Exact bounded-memory traveling fronts on an INFINITE striped input.
A state remembers W columns through the current rightmost visited column F.
Left or vertical exits reject. On a new right column, discard the old left
column and insert the pristine stripe. Positive-shift functional-graph cycles
are exact infinite-input fronts, not finite-support ant counterexamples.
"""
import json,pathlib,time,sys
HERE=pathlib.Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0))
def run(H=6,W=2,input_masks=None):
 if input_masks is None:input_masks=(0,(1<<H)-1)
 bits=H*W;M=1<<bits;ports=4*H*W;N=2*ports*M;done=bytearray(N);cycles=[];starttime=time.time();maxpath=0
 def decode(s):
  board=s%M;q=s//M;head=q%ports;phase=q//ports;h=head%4;cell=head//4;x=cell//H;y=cell%H
  return board,x,y,h,phase
 def step(s):
  board,x,y,h,phase=decode(s);bit=1<<(x*H+y);black=bool(board&bit);board^=bit;h=(h+(-1 if black else 1))%4;dx,dy=D[h];x+=dx;y+=dy;shift=0
  if y<0 or y>=H or x<0:return -1,0,'L'if black else'R'
  if x>=W:
   phase^=1;board>>=H
   board|=input_masks[phase]<<(H*(W-1))
   x-=1;shift=1
  return (((phase*ports+(x*H+y)*4+h)*M)+board),shift,'L'if black else'R'
 for seed in range(N):
  if done[seed]:continue
  path=[];where={};s=seed
  while s>=0 and not done[s]:
   done[s]=1;where[s]=len(path);path.append(s);s=step(s)[0]
  maxpath=max(maxpath,len(path))
  if s>=0 and done[s]==1:
   cyc=path[where[s]:];trans=[step(v)for v in cyc];drift=sum(z[1]for z in trans);assert drift>0
   board,x,y,h,phase=decode(cyc[0]);sector=(phase-(W-1)+x+y+h)%2
   cycles.append(dict(period=len(cyc),drift=drift,word=''.join(z[2]for z in trans),entry=dict(board=board,x=x,y=y,h=h,front_parity=phase),sector=sector))
  for v in path:done[v]=2
 return dict(H=H,W=W,input_masks=input_masks,states=N,status='COMPLETE_FINITE_INTERFACE_GRAPH',cycles=cycles,max_transient_path=maxpath,seconds=time.time()-starttime)
if __name__=='__main__':
 W=int(sys.argv[1])if len(sys.argv)>1 else 2;out=run(W=W);(HERE/f'striped_front_w{W}.json').write_text(json.dumps(out,indent=2));print({k:v for k,v in out.items()if k!='cycles'});print('cycles',len(out['cycles']));print(out['cycles'][:10])
