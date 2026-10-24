"""No fixed substitution: allow every geometrically eligible five-step macro.
Complete finite exhaustion is a proof candidate; any node/depth cap is UNKNOWN.
"""
import sys,json,pathlib,collections,time
sys.setrecursionlimit(20000)
HERE=pathlib.Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0))
MAC={'A':'RLLRR','B':'LRRLR','C':'RRRLR','D':'LLLRR'}
OPTIONS={'R':'AB','L':'CD'}
nodecap=int(sys.argv[1])if len(sys.argv)>1 else 1000000
depthcap=int(sys.argv[2])if len(sys.argv)>2 else 1024
fuelcap=int(sys.argv[3])if len(sys.argv)>3 else None
last={};letters=[];poses=[(0,0,0)];choices=[];firstL=set();nodes=0;maxdepth=0;best=None;counts=collections.Counter();levelcounts=collections.Counter();stop=None;conflicts=[];start=time.time()

def append(label):
 w=MAC[label];undo=[];newL=[];p0=len(poses);l0=len(letters)
 for c in w:
  x,y,h=poses[-1];p=x,y;old=last.get(p)
  if old is not None and old[0]==c:
   counts['alternation_conflict']+=1
   if len(conflicts)<20:conflicts.append(dict(choices=''.join(choices)+label,time=len(letters),earlier=old[1],cell=p,turn=c))
   rollback(undo,newL,p0,l0);return None
  if old is None and c=='L':firstL.add(p);newL.append(p)
  if fuelcap is not None and len(firstL)>fuelcap:
   counts['fuel_cap']+=1;rollback(undo,newL,p0,l0);return None
  undo.append((p,old));last[p]=(c,len(letters));letters.append(c);h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];poses.append((x+dx,y+dy,h))
 return undo,newL,p0,l0

def rollback(undo,newL,p0,l0):
 for p,old in reversed(undo):
  if old is None:last.pop(p)
  else:last[p]=old
 for p in newL:firstL.remove(p)
 del poses[p0:];del letters[l0:]

def dfs(n):
 global nodes,maxdepth,best,stop
 nodes+=1;levelcounts[n]+=1
 if n>maxdepth:
  maxdepth=n;best=dict(macros=n,choices=''.join(choices),turns=''.join(letters),seed=sorted(firstL),pose=poses[-1]);
  if n<=20 or n%100==0:print('DEPTH',n,'fuel',len(firstL),'nodes',nodes,flush=True)
 if n>=depthcap:stop='DEPTH_CAP';return
 if nodes>=nodecap:stop='NODE_CAP';return
 opts='AD'if n==0 else OPTIONS[letters[n]]
 for a in opts:
  saved=append(a)
  if saved is None:continue
  choices.append(a)
  # Full self-embedding identity, not merely individually compatible endpoints.
  x,y,h=poses[n+1];X,Y,H=poses[-1]
  assert (X,Y,H)==(x-2*y,2*x+y,h)
  dfs(n+1)
  choices.pop();rollback(*saved)
  if stop:return

dfs(0)
out=dict(status=stop or'EXHAUSTED',node_cap=nodecap,depth_cap=depthcap,fuel_cap=fuelcap,nodes=nodes,maxdepth=maxdepth,counts=dict(counts),levelcounts=dict(levelcounts),best=best,example_conflicts=conflicts,seconds=time.time()-start)
p=HERE/('free_five_inflation_'+('any'if fuelcap is None else str(fuelcap))+'.json');p.write_text(json.dumps(out,indent=2));print('DONE',out['status'],nodes,maxdepth,dict(counts),'seconds',out['seconds'],flush=True)
