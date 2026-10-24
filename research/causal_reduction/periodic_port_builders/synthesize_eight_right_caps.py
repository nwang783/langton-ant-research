"""Bounded necessary right-cap synthesis. SAT is NOT a whole builder.
Bulk reads left of the fixed cut are conservatively omitted. Any SAT candidate
needs a separate full-arm replay and all-n cap proof. No solver status alone is
a theorem. Uses only the installed libz3 C API.
"""
import argparse,json,time,pathlib,sys,re
ROOT=pathlib.Path('/workspace/shared/langton');sys.path.insert(0,str(ROOT/'causal_reduction/morphic_candidates'));from smt_inflation_refinement import Z3
P=pathlib.Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--cycles',type=int,default=4);p.add_argument('--steps',type=int,default=64);p.add_argument('--width',type=int,default=8);p.add_argument('--ymin',type=int,default=-10);p.add_argument('--ymax',type=int,default=11);p.add_argument('--timeout',type=int,default=60000);p.add_argument('--free-final',action='store_true');args=p.parse_args()
A='LRLLRRRRLLRL';B='RRRLLLLRLLLLRLLLLRRRRLRRRRLR';S='RLLR';W='LLRLRRRRLRRRRLLLLRLL';D=((0,1),(1,0),(0,-1),(-1,0));cut=-4;right=args.width+6*args.cycles+6;H=args.ymax-args.ymin+1
lines=[f'(set-option :timeout {args.timeout})'];counter=0;modelnames=[]
def decl(name,typ):lines.append(f'(declare-const {name} {typ})');return name
def eq(a,b):return f'(= {a} {b})'
def ass(s):lines.append(f'(assert {s})')
def con(*ss):return '(and '+' '.join(ss)+')'
def add(*ss):return '(+ '+' '.join(map(str,ss))+')'
def ite(c,a,b):return f'(ite {c} {a} {b})'
def select(f,i):return f'(select {f} {i})'
def index(x,y):return add(f'(* (- {x} {cut}) {H})',f'(- {y} {args.ymin})')
def fieldnew(expr):
 global counter
 name=decl(f'f{counter}','(Array Int Bool)');counter+=1;ass(eq(name,expr));return name
init=decl('initial','(Array Int Bool)');field=init
idx=lambda x,y:(x-cut)*H+y-args.ymin
def tile(x,y):return y>=0 and bool(([513,519][x%2]>>y)&1)
initialnames={}
for x in range(cut,right+1):
 for y in range(args.ymin,args.ymax+1):
  if x>=args.width:ass(eq(select(init,idx(x,y)),'false'))
  else:
   b=decl(f'b{idx(x,y)}','Bool');ass(eq(b,select(init,idx(x,y))));initialnames[x,y]=b;modelnames.append(b)
for x in range(cut,args.width):
 charge=add(*(ite(initialnames[x,y],1 if y%2==0 else -1,0)for y in range(args.ymin,args.ymax+1)));ass(eq(f'(mod {charge} 4)',0))
caps=[];serial=0
def literal(w,pose):
 global field
 x,y,h=pose
 for c in w:
  if x>=cut:
   assert x<=right and args.ymin<=y<=args.ymax
   ass(eq(select(field,idx(x,y)),'true'if c=='L'else'false'));field=fieldnew(f'(store {field} {idx(x,y)} '+('true'if c=='R'else'false')+')')
  h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];x+=dx;y+=dy
 return x,y,h
def cap(start,end,R):
 global field,serial
 k=serial;serial+=1
 xs=[decl(f'x{k}_{t}','Int')for t in range(args.steps+1)];ys=[decl(f'y{k}_{t}','Int')for t in range(args.steps+1)];hs=[decl(f'h{k}_{t}','Int')for t in range(args.steps+1)];done=[decl(f'd{k}_{t}','Bool')for t in range(args.steps+1)]
 for a,b in zip((xs[0],ys[0],hs[0]),start):ass(eq(a,b))
 ass(eq(done[0],'false'));turns=[];modelnames.extend(done)
 for t in range(args.steps):
  x,y,h=xs[t],ys[t],hs[t];c=decl(f'c{k}_{t}','Bool');ass(eq(c,select(field,index(x,y))));turns.append(c);modelnames.append(c);modelnames.append(done[t])
  ass(con(f'(>= {x} {R-4})',f'(<= {x} {R+args.width+5})',f'(>= {y} {args.ymin})',f'(<= {y} {args.ymax})',f'(>= {h} 0)',f'(< {h} 4)'))
  target=con(eq(x,end[0]),eq(y,end[1]),eq(h,end[2]));stop=f'(or {done[t]} {target})';ass(eq(done[t+1],stop));nh=f'(mod (+ {h} (ite {c} 3 1)) 4)'
  ass(eq(hs[t+1],ite(stop,h,nh)));ass(eq(xs[t+1],ite(stop,x,add(x,ite(eq(nh,1),1,ite(eq(nh,3),-1,0))))));ass(eq(ys[t+1],ite(stop,y,add(y,ite(eq(nh,0),1,ite(eq(nh,2),-1,0))))))
  field=fieldnew(ite(stop,field,f'(store {field} {index(x,y)} (not {c}))'))
 for a,b in zip((xs[-1],ys[-1],hs[-1]),end):ass(eq(a,b))
 caps.append(dict(turns=turns,done=done,start=start,end=end))
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
   target=('true'if tile(x,y)else'false')if x-shift<cut else(select(init,idx(x-shift,y))if x-shift<args.width else'false');ass(eq(select(field,idx(x,y)),target))
name=f'eight_right_c{args.cycles}_s{args.steps}_w{args.width}_h{H}_free{int(args.free_final)}';smt='\n'.join(lines)+'\n(check-sat)\n';(P/(name+'.smt2')).write_text(smt);Z=Z3();t=time.time();status=Z.run(smt).strip();result=dict(args=vars(args),status=status,seconds=time.time()-t,lines=len(lines))
if status=='sat':
 raw=Z.run('(get-value ('+' '.join(modelnames)+'))');values={a:b=='true'for a,b in re.findall(r'\((\w+) (true|false)\)',raw)};result['seed']=[list(q)for q,b in initialnames.items()if values[b]];result['caps']=[]
 for a in caps:
  w=''
  # done[t+1] becomes true at the target; the frozen step itself is not read.
  for t,c in enumerate(a['turns']):
   if values[a['done'][t+1]]:break
   w+='L'if values[c]else'R'
  result['caps'].append(dict(start=a['start'],end=a['end'],word=w))
else:result['scope']='UNKNOWN is inconclusive; UNSAT is bounded only'
(P/(name+'.json')).write_text(json.dumps(result,indent=2));print(json.dumps(result),flush=True);Z.close()
