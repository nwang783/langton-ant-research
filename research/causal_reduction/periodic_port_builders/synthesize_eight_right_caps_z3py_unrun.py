"""Bounded right-cap synthesis only. SAT is not a full builder: left caps absent.
Every stored bulk read is guarded; omitted reads are strictly left of the fixed
cut and are a conservative abstraction of the stable incoming/outgoing arms.
A SAT result must be independently replayed with all finite-arm boundary guards.
"""
import argparse,json,time,pathlib
import z3
P=pathlib.Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--cycles',type=int,default=4);p.add_argument('--steps',type=int,default=64);p.add_argument('--width',type=int,default=8);p.add_argument('--ymin',type=int,default=-10);p.add_argument('--ymax',type=int,default=11);p.add_argument('--timeout',type=int,default=60000);p.add_argument('--free-final',action='store_true');args=p.parse_args()
A='LRLLRRRRLLRL';B='RRRLLLLRLLLLRLLLLRRRRLRRRRLR';S='RLLR';W='LLRLRRRRLRRRRLLLLRLL';D=((0,1),(1,0),(0,-1),(-1,0));cut=-4;right=args.width+6*args.cycles+6;H=args.ymax-args.ymin+1
sol=z3.Solver();sol.set(timeout=args.timeout);init=z3.Array('initial',z3.IntSort(),z3.BoolSort());field=init
idx=lambda x,y:(x-cut)*H+y-args.ymin
def tile(x,y):return y>=0 and bool(([513,519][x%2]>>y)&1)
for x in range(cut,right+1):
 for y in range(args.ymin,args.ymax+1):
  if x>=args.width:sol.add(z3.Select(init,idx(x,y))==False)
# All complete remote cap columns must have returning-builder charge0 mod4.
for x in range(cut,args.width):
 charge=z3.Sum([z3.If(z3.Select(init,idx(x,y)),1 if y%2==0 else -1,0)for y in range(args.ymin,args.ymax+1)])
 sol.add(charge%4==0)
caps=[];serial=0
def literal(w,pose):
 global field
 x,y,h=pose
 for c in w:
  if x>=cut:
   assert x<=right and args.ymin<=y<=args.ymax
   sol.add(z3.Select(field,idx(x,y))==(c=='L'));field=z3.Store(field,idx(x,y),c=='R')
  h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];x+=dx;y+=dy
 return x,y,h
def cap(start,end,R):
 global field,serial
 k=serial;serial+=1
 xs=[z3.Int(f'x{k}_{t}')for t in range(args.steps+1)];ys=[z3.Int(f'y{k}_{t}')for t in range(args.steps+1)];hs=[z3.Int(f'h{k}_{t}')for t in range(args.steps+1)];done=[z3.Bool(f'd{k}_{t}')for t in range(args.steps+1)]
 sol.add(xs[0]==start[0],ys[0]==start[1],hs[0]==start[2],done[0]==False)
 turns=[]
 for t in range(args.steps):
  x,y,h=xs[t],ys[t],hs[t];c=z3.Select(field,idx(x,y));turns.append(c)
  sol.add(x>=R-4,x<=R+args.width+5,y>=args.ymin,y<=args.ymax,h>=0,h<4)
  target=z3.And(x==end[0],y==end[1],h==end[2]);stop=z3.Or(done[t],target)
  # Stop at the first occurrence of the requested next-arm port.
  sol.add(done[t+1]==stop)
  nh=(h+z3.If(c,3,1))%4
  sol.add(hs[t+1]==z3.If(stop,h,nh),xs[t+1]==z3.If(stop,x,x+z3.If(nh==1,1,z3.If(nh==3,-1,0))),ys[t+1]==z3.If(stop,y,y+z3.If(nh==0,1,z3.If(nh==2,-1,0))))
  field=z3.If(stop,field,z3.Store(field,idx(x,y),z3.Not(c)))
 sol.add(xs[-1]==end[0],ys[-1]==end[1],hs[-1]==end[2])
 caps.append((xs,ys,hs,done,turns,start,end))
for j in range(args.cycles):
 R=6*j;n=(R-cut)//2
 literal(A*n,(cut,0,1));cap((R,0,1),(R,8,3),R);literal(S*((R-cut)//2+1),(R,8,3))
 literal(B*n,(cut,2,1));cap((R,2,1),(R,8,1),R);literal(W*((R-cut)//2+1),(R,8,1))
 literal(A*n,(cut,0,1));cap((R,0,1),(R,10,3),R);literal(S*((R-cut)//2+1),(R,10,3))
 literal(B*n,(cut,2,1));cap((R,2,1),(R-1,9,3),R);literal(S*((R-1-cut)//2+1),(R-1,9,3))
if not args.free_final:
 shift=6*args.cycles
 for x in range(cut,right+1):
  for y in range(args.ymin,args.ymax+1):
   target=z3.BoolVal(tile(x,y))if x-shift<cut else(z3.Select(init,idx(x-shift,y))if x-shift<args.width else z3.BoolVal(False))
   sol.add(z3.Select(field,idx(x,y))==target)
t=time.time();status=sol.check();result=dict(args=vars(args),status=str(status),seconds=time.time()-t,assertions=len(sol.assertions()))
if status==z3.sat:
 m=sol.model();result['seed']=[[x,y]for x in range(cut,args.width)for y in range(args.ymin,args.ymax+1)if z3.is_true(m.eval(z3.Select(init,idx(x,y)),model_completion=True))];result['caps']=[]
 for xs,ys,hs,ds,turns,start,end in caps:
  word=''
  for t,c in enumerate(turns):
   pose=tuple(m.eval(q[t]).as_long()for q in(xs,ys,hs))
   if pose==end:break
   word+='L'if z3.is_true(m.eval(c))else'R'
  result['caps'].append(dict(start=start,end=end,word=word))
else:result['reason']=sol.reason_unknown()if status==z3.unknown else'bounded exclusion only'
name=f'eight_right_c{args.cycles}_s{args.steps}_w{args.width}_h{H}_free{int(args.free_final)}.json';(P/name).write_text(json.dumps(result,indent=2));print(json.dumps(result),flush=True)
