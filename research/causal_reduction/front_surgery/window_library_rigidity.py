"""Open-window local-closure exploration for broader pose-loop libraries.
Only an all-central-zero result is a local rigidity certificate. Partial
closure is explicitly inconclusive; no search cap is reported as exclusion.
"""
import sys,json,time
from collections import defaultdict
from loop_decoration_solver import walk,cl_rank,ROOT,HERE,known
from window_detour_rigidity import closure
standard=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];base,end=walk(standard);d=end[:2]

def build_window(K,library):
 local=[];options=[];groups=[]
 for i,(p,h,c) in enumerate(base):
  vv=[]
  for v in library:
   ve,vend=walk(v);assert vend==(0,0,0)
   last=next(z for p0,h0,z in reversed(ve) if p0==(0,0))
   if last!=c:vv.append(v)
  ids=[]
  for j,v in enumerate(vv):
   q=len(options);options.append((i,v));ids.append(q)
   for t,(p2,h2,c2) in enumerate(walk(v,(p[0],p[1],h))[0]):local.append((p2,(i,j,t),c2,q))
  groups.append(ids);local.append((p,(i,len(vv),0),c,None))
 span={}
 for p,t,c,q in local:
  cl,a=cl_rank(p,d)
  if cl not in span:span[cl]=[a,a]
  else:span[cl]=[min(span[cl][0],a),max(span[cl][1],a)]
 N=len(options)*(2*K+1);ev=defaultdict(list)
 for k in range(-K,K+1):
  for p,t,c,q in local:
   pp=(p[0]+k*d[0],p[1]+k*d[1]);cl,a=cl_rank(pp,d);lo,hi=span[cl]
   if a-hi < -K or a-lo>K:continue
   qq=None if q is None else (k+K)*len(options)+q
   ev[pp].append(((k,)+t,c,qq))
 eq=[];guards=[[] for _ in range(N)]
 for es in ev.values():
  es.sort();mask=bit=0
  for t,c,q in es:
   row=(mask,bit^(c=='L'))
   if q is None:eq.append(row);bit^=1
   else:guards[q].append(row);mask^=1<<q
 for k in range(2*K+1):
  for ids in groups:
   for a in ids:
    for b in ids:
     if a!=b:guards[k*len(options)+a].append((1<<(k*len(options)+b),0))
 return N,eq,guards,list(range(K*len(options),(K+1)*len(options))),sorted(ev),options

if __name__=='__main__':
 L=int(sys.argv[1]);Ks=list(map(int,sys.argv[2:])) or [3,4,5]
 dat=json.loads((HERE/'pose_loops_24.json').read_text())
 if isinstance(dat,dict):
  print('KEYS',list(dat),flush=True)
  library=dat['loops']
 else:library=dat
 library=[w for w in library if len(w)<=L]
 out=[]
 for K in Ks:
  t=time.time();N,eq,g,central,cells,options=build_window(K,library);print('BUILT',K,N,len(cells),len(eq),flush=True)
  b,rounds=closure(N,eq,g);assert b is not None
  vals=[known(q,b) for q in central]
  r=dict(library_max=L,radius_periods=K,variables=N,options_per_period=len(options),complete_cells=len(cells),original_equations=len(eq),central_zero=sum(v==0 for v in vals),unknown_central=[options[i] for i,v in enumerate(vals) if v is None],rounds=rounds,seconds=time.time()-t,rigid=all(v==0 for v in vals))
  out.append(r);print('RESULT',json.dumps(r),flush=True);(HERE/f'window_library_{L}.json').write_text(json.dumps(out,indent=2))
