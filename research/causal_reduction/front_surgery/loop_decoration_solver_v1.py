"""Exact periodic-front synthesis by four-turn-loop decoration.

No fixed period, mass, macro or lift theorem is assumed. A translating
backbone's geometric poses are fixed. At each phase choose no decoration,
one opposite-turn 4-loop, or a same-turn then opposite-turn pair of4-loops.
All white-front read constraints become guarded GF(2) equations.
"""
import argparse,json,time
from pathlib import Path
from collections import defaultdict
DIR=((0,1),(1,0),(0,-1),(-1,0))
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent

def walk(w,pose=(0,0,0)):
 x,y,h=pose;events=[]
 for c in w:
  events.append(((x,y),h,c));h=(h+(1 if c=='R' else -1))%4;dx,dy=DIR[h];x+=dx;y+=dy
 return events,(x,y,h)

def cl_rank(p,d):
 x,y=p;dx,dy=d
 if dx:return (dx*y-dy*x,x%abs(dx)),x//dx
 return (x,y%abs(dy)),y//dy

def build(w,double=True,library=None):
 base,end=walk(w);assert end[2]==0 and end[:2]!=(0,0);d=end[:2];events=[];options=[];byphase=defaultdict(list)
 for i,(p,h,c) in enumerate(base):
  variants=[('L' if c=='R' else 'R')*4]
  if double:variants.append(c*4+variants[0])
  if library is not None:
   variants=[]
   for v in library:
    vv,vend=walk(v);assert vend==(0,0,0)
    last=next(z for p0,h0,z in reversed(vv) if p0==(0,0))
    if last!=c:variants.append(v)
  for j,v in enumerate(variants):
   q=len(options);options.append(dict(phase=i,word=v));byphase[i].append(q)
   ev,back=walk(v,(p[0],p[1],h));assert back==(p[0],p[1],h)
   for t,(p2,h2,c2) in enumerate(ev):events.append((p2,(i,j,t),c2,q))
  events.append((p,(i,len(variants),0),c,None))
 classes=defaultdict(list)
 for p,t,c,q in events:
  cl,a=cl_rank(p,d);classes[cl].append((-a,t,c,q,p))
 equations=[];guards=[[] for _ in options]
 for ev in classes.values():
  ev.sort();mask=parity=0
  for _,t,c,q,p in ev:
   row=(mask,parity^(c=='L'))
   if q is None:equations.append(row);parity^=1
   else:guards[q].append(row);mask^=1<<q
 # Mutually exclusive alternatives at one original phase.
 for ids in byphase.values():
  for q in ids:
   for z in ids:
    if q!=z:guards[q].append((1<<z,0))
 return options,equations,guards,d

def reduce_row(mask,rhs,basis):
 while mask:
  j=mask.bit_length()-1
  if j not in basis:break
  m,b=basis[j];mask^=m;rhs^=b
 return mask,rhs

def add_row(basis,mask,rhs):
 mask,rhs=reduce_row(mask,rhs,basis)
 if not mask:return rhs==0
 basis[mask.bit_length()-1]=(mask,rhs);return True

def known(q,basis):
 m,b=reduce_row(1<<q,0,basis)
 return None if m else b

def solve(equations,guards,nonzero=True,limit=1000000,timeout=60):
 N=len(guards);basis={}
 for m,b in equations:
  if not add_row(basis,m,b):return dict(status='UNSAT',reason='unconditional GF2 equations inconsistent',nodes=0,rank=len(basis)),None
 initial_rank=len(basis);nodes=0;started=time.time();cut=False;maxdepth=0
 def rec(bs,active,depth):
  nonlocal nodes,cut,maxdepth
  nodes+=1;maxdepth=max(maxdepth,depth)
  if nodes>limit or time.time()-started>timeout:cut=True;return None
  while True:
   triggered=[q for q in range(N) if q not in active and known(q,bs)==1]
   if not triggered:break
   for q in triggered:
    active.add(q)
    for m,b in guards[q]:
     if not add_row(bs,m,b):return None
  unknown=[q for q in range(N) if known(q,bs) is None]
  if not unknown:
   ans=[known(q,bs) for q in range(N)]
   if nonzero and not any(ans):return None
   return ans
  # Prefer an option with many currently independent parity conditions.
  def score(q):
   rows=[reduce_row(m,b,bs) for m,b in guards[q]]
   return (sum(m==0 and b for m,b in rows),sum(bool(m) for m,b in rows),-q)
  q=max(unknown,key=score)
  for value in (1,0):
   nb=dict(bs)
   if add_row(nb,1<<q,value):
    ans=rec(nb,set(active),depth+1)
    if ans is not None:return ans
   if cut:return None
  return None
 ans=rec(basis,set(),0)
 return dict(status='SAT' if ans is not None else 'UNKNOWN' if cut else 'UNSAT',variables=N,unconditional_rank=initial_rank,unconditional_free=N-initial_rank,nodes=nodes,max_branch_depth=maxdepth,seconds=time.time()-started),ans

def assemble(w,options,ans):
 at={o['phase']:o['word'] for o,v in zip(options,ans) if v}
 return ''.join(at.get(i,'')+c for i,c in enumerate(w))

def verify(w):
 ev,end=walk(w);d=end[:2];assert end[2]==0 and d!=(0,0);classes=defaultdict(list)
 for i,(p,h,c) in enumerate(ev):
  cl,a=cl_rank(p,d);classes[cl].append((a,i,p,c))
 seed=set();odd=0
 for evs in classes.values():
  evs.sort(key=lambda e:(-e[0],e[1]));assert all(c==('R' if j%2==0 else 'L') for j,(_,i,p,c) in enumerate(evs)),evs
  odd+=len(evs)%2;lo=min(a for a,i,p,c in evs);hi=max(a for a,i,p,c in evs)
  ref=next(p for a,i,p,c in evs if a==lo)
  for k in range(lo,hi+1):
   if sum(a>k for a,i,p,c in evs)%2:seed.add((ref[0]+(k-lo)*d[0],ref[1]+(k-lo)*d[1]))
 board=set(seed);x=y=h=0
 for t,c in enumerate(w*5):
  assert ((x,y) in board)==(c=='L'),(t,x,y,c)
  board.symmetric_difference_update({(x,y)});h=(h+(1 if c=='R' else -1))%4;dx,dy=DIR[h];x+=dx;y+=dy
 assert (x,y,h)==(5*d[0],5*d[1],0)
 return dict(period=len(w),drift=d,seed=sorted(seed),seed_mass=len(seed),wake_growth=odd,translation_classes=len(classes),five_period_replay=True,exact_all_future_chronology=True)

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--backbone',default='standard');ap.add_argument('--single',action='store_true');ap.add_argument('--allow-zero',action='store_true');ap.add_argument('--limit',type=int,default=1000000);ap.add_argument('--timeout',type=float,default=60);args=ap.parse_args()
 if args.backbone=='standard':w=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
 else:w=args.backbone
 options,eq,guards,d=build(w,not args.single)
 z,ans=solve(eq,guards,not args.allow_zero,args.limit,args.timeout)
 z.update(backbone=w,backbone_period=len(w),backbone_drift=d,variants='single only' if args.single else 'single or double',nonzero_required=not args.allow_zero)
 if ans is not None:
  ww=assemble(w,options,ans);z['chosen']=[dict(index=q,**o) for q,(o,a) in enumerate(zip(options,ans)) if a];z['word']=ww;z['verified']=verify(ww)
 print(json.dumps(z,indent=2));name=('standard' if args.backbone=='standard' else 'backbone'+str(len(w)))+('_single' if args.single else '_double')+('_zero_control' if args.allow_zero else '')
 (HERE/(name+'_result.json')).write_text(json.dumps(z,indent=2)+'\n')
