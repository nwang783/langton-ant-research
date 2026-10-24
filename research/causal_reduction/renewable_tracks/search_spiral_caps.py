"""Exploratory inverse synthesis of expanding clockwise rail-shift circuits.
S=RLLR shifts a solid rail one cell outward. Try a rotationally repeated
quarter-turn cap K and a distinguished between-laps seam T. A finite prefix
is NOT an infinite countermodel; retain full first-read and repeat guards.
"""
import sys,itertools,json,time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'front_surgery'))
from loop_decoration_solver import walk
HERE=Path(__file__).resolve().parent;S='RLLR'

def feasible(w):
 ev,end=walk(w);last={}
 for p,h,c in ev:
  if last.get(p)==c:return False
  last[p]=c
 return True

def words(maxlen,heading=None,disp=None):
 for n in range(1,maxlen+1):
  for z in itertools.product('RL',repeat=n):
   w=''.join(z);ev,end=walk(w)
   if heading is not None and end[2]!=heading:continue
   if disp is not None and end[:2]!=disp:continue
   if feasible(w):yield w,end

def trace_laps(K,T,n0=5,laps=15):
 x=y=h=0;last={};roots=[];counts=[];clock=0
 for n in range(n0,n0+laps):
  w=(S*n+K)*4+T;firstL=0
  for c in w:
   p=(x,y)
   if last.get(p)==c:return dict(status='CONTRADICTION',lap=n,n0=n0,time=clock,cell=p,turn=c,roots=len(roots))
   if p not in last and c=='L':roots.append(p);firstL+=1
   last[p]=c;h=(h+(1 if c=='R' else -1))%4;dx,dy=((0,1),(1,0),(0,-1),(-1,0))[h];x+=dx;y+=dy;clock+=1
  counts.append(firstL)
 return dict(status='PREFIX',first_L_by_lap=counts,roots=len(roots),seed=roots,endpoint=[x,y,h],time=clock)

if __name__=='__main__':
 capmax=int(sys.argv[1]) if len(sys.argv)>1 else 13
 seammax=int(sys.argv[2]) if len(sys.argv)>2 else 14
 start=time.time();caps=[];cnt=0
 for K,end in words(capmax,heading=1):
  cnt+=1
  if feasible((S*5+K)*4):caps.append(dict(word=K,end=end))
 print('CAPS',cnt,len(caps),time.time()-start,flush=True)
 (HERE/f'caps_through{capmax}.json').write_text(json.dumps(dict(tested=cnt,viable=caps),indent=2))
 seams=list(words(seammax,heading=0,disp=(-1,-1)));print('SEAMS',len(seams),flush=True)
 out=[];tested=0
 for cap in caps:
  for T,end in seams:
   tested+=1;r=trace_laps(cap['word'],T)
   if r['status']=='PREFIX':
    v=dict(cap=cap,seam=T,trace=r);out.append(v);print('CANDIDATE',json.dumps(v),flush=True)
 print('DONE',tested,len(out),time.time()-start,flush=True)
 (HERE/f'spiral_caps_{capmax}_{seammax}.json').write_text(json.dumps(dict(capmax=capmax,seammax=seammax,tested=tested,prefix_candidates=out,seconds=time.time()-start),indent=2))
