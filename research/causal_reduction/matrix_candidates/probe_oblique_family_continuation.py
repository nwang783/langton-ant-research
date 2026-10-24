"""Diagnostic for the LIMIT of an oblique fresh-record certificate.
A surviving local continuation is NOT an inflation model or finite seed.
"""
import sys,json,pathlib,time
D=((0,1),(1,0),(0,-1),(-1,0))
def run(ell):
 k=4*ell+1;board={};stats={'E_nodes':0,'S_nodes':0,'E_complete':0};survivor=[]
 targets=[(ell+1,ell+2,ell-1,ell-1),(0,ell-1,2*ell+1,ell+1)]
 def block(pose,target,tag,callback):
  cnt=[0]*4
  def dfs(x,y,h,w):
   stats[tag+'_nodes']+=1
   if len(w)==k:return callback((x,y,h),w)
   p=x,y;old=board.get(p);opts=(old,) if old is not None else ((0,) if -2*x+3*y>=0 else(0,1))
   for bit in opts:
    d=(h+(1 if bit==0 else 3))%4
    if cnt[d]>=target[d]:continue
    board[p]=1-bit;cnt[d]+=1
    stop=dfs(x+D[d][0],y+D[d][1],d,w+'RL'[bit])
    cnt[d]-=1
    if old is None:board.pop(p,None)
    else:board[p]=old
    if stop:return True
   return False
  return dfs(*pose,'')
 def east_done(pose,ew):
  stats['E_complete']+=1
  assert pose[:2]==(3,2)
  def south_done(end,sw):
   assert end[:2]==(1,1-2*ell)
   survivor.append({'east_word':ew,'south_word':sw,'end':end});return True
  return block(pose,targets[1],'S',south_done)
 st=time.monotonic();block((0,0,0),targets[0],'E',east_done)
 return dict(ell=ell,k=k,matrix=[[3,2],[2,2*ell+1]],status='LOCAL SURVIVOR, NOT A MODEL' if survivor else'NO LOCAL CONTINUATION',stats=stats,survivor=survivor,seconds=time.monotonic()-st)
if __name__=='__main__':
 ell=int(sys.argv[1]) if len(sys.argv)>1 else 3
 r=run(ell);p=pathlib.Path(__file__).with_name(f'oblique_family_ell{ell}.json');p.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
