"""Guarded GF(2) synthesis of a fixed cap backbone with pose-return options.
A SAT answer is rechecked by the complete-history checker. UNKNOWN is not UNSAT.
"""
from mixed_shuttle_caps import *
from loop_decoration_solver import solve,assemble

def build_cap(w,side,library):
 base,en=walk(w,(0,0,1));assert en==((0,4,1) if side=='left' else (0,0,1))
 events=[];options=[];at=defaultdict(list)
 for i,(p,h,c) in enumerate(base):
  variants=[]
  for v in library:
   ve,back=walk(v);assert back==(0,0,0)
   last=next(cc for pp,hh,cc in reversed(ve) if pp==(0,0))
   if last!=c:variants.append(v)
  for j,v in enumerate(variants):
   q=len(options);options.append(dict(phase=i,word=v));at[i].append(q)
   ev,back=walk(v,(*p,h));assert back==(*p,h)
   for k,(pp,hh,cc) in enumerate(ev):events.append((pp,(0,i,j,k),cc,q))
  events.append((p,(0,i,len(variants),0),c,None))
 I,O=(WE,SE) if side=='left' else (SE,WE);step=2 if side=='left' else -2;OY=4 if side=='left' else 0
 xs=[p[0] for p,t,c,q in events]+[p[0]+step for p,h,c in I]+[p[0] for p,h,c in O]
 lo=min(xs)-4;hi=max(xs)+4
 for x in range(lo,hi+1):
  for i,((a,b),h,c) in enumerate(I):
   z=x-a
   if z%step==0 and z//step>=1:
    k=z//step;events.append(((x,b),(-1,-len(I)*k+i,0,0),c,None))
  for i,((a,b),h,c) in enumerate(O):
   z=x-a
   if z%step==0 and z//step>=0:
    k=z//step;events.append(((x,b+OY),(1,len(O)*k+i,0,0),c,None))
 classes=defaultdict(list)
 for (x,y),t,c,q in events:classes[x,y%4].append((-y,t,c,q))
 eq=[];guards=[[] for _ in options]
 for ev in classes.values():
  ev.sort();mask=parity=0
  for a,t,c,q in ev:
   row=(mask,parity^(c=='L'))
   if q is None:eq.append(row);parity^=1
   else:guards[q].append(row);mask^=1<<q
 for ids in at.values():
  for q in ids:
   for z in ids:
    if q!=z:guards[q].append((1<<z,0))
 return options,eq,guards

if __name__=='__main__':
 N=int(sys.argv[1]) if len(sys.argv)>1 else 16
 lib=json.loads((HERE.parent/'front_surgery/pose_loops_24.json').read_text());lib=[w for w in lib if len(w)<=N]
 out=[]
 for side,w in [('left','LLRLRRLR'),('right','LRRRRLRRRRLL'),('right','RRRRLRRRRLRRRRLL')]:
  options,eq,guards=build_cap(w,side,lib);z,ans=solve(eq,guards,False,100000,30)
  z.update(side=side,backbone=w,library_max=N,options=len(options))
  if ans is not None:
   ww=assemble(w,options,ans);v=test(ww,side);assert not v['bad_count'];z['verified']=v
  print(json.dumps(z),flush=True);out.append(z)
 (HERE/f'mixed_cap_decorations_{N}.json').write_text(json.dumps(out,indent=2))
