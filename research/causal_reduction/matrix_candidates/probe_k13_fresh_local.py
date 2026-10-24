"""Controller-free necessary local test for p(13n)=+/-diag(3,5)p(n).
The coarse/fine initial histories are relaxed independently below their fresh
rows. A survivor is ONLY a local necessary witness, not a model or seed.
"""
import json,time,pathlib,sys
D=((0,1),(1,0),(0,-1),(-1,0));K=13

def tail_board():
 x,y,h=1,-1,0;board={}
 for c in 'RRRRLR':
  bit=int(c=='L');old=board.get((x,y),0 if y>=-1 else None)
  assert old is None or old==bit
  board[x,y]=1-bit;h=(h+(1 if bit==0 else 3))%4
  dx,dy=D[h];x+=dx;y+=dy
 assert (x,y,h)==(0,0,0)
 return board

def counts_for(h,d):
 # Odd macro: the axis opposite incoming heading has seven movements.
 nx=7 if h%2==0 else 6;ny=13-nx
 tx,ty=D[d];tx*=3;ty*=5
 assert (nx+tx)%2==0 and (ny+ty)%2==0
 return ((ny+ty)//2,(nx+tx)//2,(ny-ty)//2,(nx-tx)//2)

def enumerate_blocks(board,pose,d,callback,stats):
 x0,y0,h0=pose;target=counts_for(h0,d);counts=[0]*4
 def dfs(x,y,h,word):
  stats['fine_nodes']+=1
  if len(word)==K:
   assert tuple(counts)==target
   return callback((x,y,h),word)
  p=x,y;old=board.get(p);opts=(old,) if old is not None else ((0,) if y>=-1 else (0,1))
  for bit in opts:
   hh=(h+(1 if bit==0 else 3))%4
   if counts[hh]>=target[hh]:continue
   counts[hh]+=1;board[p]=1-bit
   stop=dfs(x+D[hh][0],y+D[hh][1],hh,word+'RL'[bit])
   counts[hh]-=1
   if old is None:board.pop(p,None)
   else:board[p]=old
   if stop:return True
  return False
 return dfs(*pose,'')

def run(depth=2,stop_first=False,nodecap=10000000):
 fine=tail_board();coarse={};stats={'fine_nodes':0,'levels':[0]*(depth+1),'capped':False};witnesses=[]
 def rec(cx,cy,ch,pose,cword,fwords):
  stats['levels'][len(cword)]+=1
  if len(cword)==depth:
   witnesses.append({'coarse_turns':cword,'fine_words':fwords,'fine_pose':pose})
   return stop_first
  if stats['fine_nodes']>nodecap:stats['capped']=True;return True
  cp=cx,cy;old=coarse.get(cp);opts=(old,) if old is not None else ((0,) if cy>=0 else (0,1))
  for bit in opts:
   d=(ch+(1 if bit==0 else 3))%4;coarse[cp]=1-bit
   nx,ny=cx+D[d][0],cy+D[d][1]
   def visit(fp,w):
    assert fp[:2]==(3*nx,5*ny)
    return rec(nx,ny,d,fp,cword+'RL'[bit],fwords+[w])
   stop=enumerate_blocks(fine,pose,d,visit,stats)
   if old is None:coarse.pop(cp,None)
   else:coarse[cp]=old
   if stop:return True
  return False
 started=time.monotonic();rec(0,0,0,(0,0,0),'',[])
 return dict(depth=depth,stop_first=stop_first,status='UNKNOWN CAP' if stats['capped'] else 'LOCAL SURVIVOR' if witnesses else 'NO LOCAL EXTENSION',stats=stats,witnesses=witnesses,seconds=time.monotonic()-started)
if __name__=='__main__':
 depth=int(sys.argv[1]) if len(sys.argv)>1 else 2
 stop_first=bool(int(sys.argv[2])) if len(sys.argv)>2 else False
 out=run(depth,stop_first)
 p=pathlib.Path(__file__).with_name(f'k13_fresh_local_depth{depth}.json');p.write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='witnesses'}));print('witness_count',len(out['witnesses']))
 for w in out['witnesses'][:10]:print(w)
