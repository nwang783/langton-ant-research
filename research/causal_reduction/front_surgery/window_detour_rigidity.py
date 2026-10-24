"""Finite white-front window; no periodic identification of detour choices."""
import sys,json,time
from collections import defaultdict
from loop_decoration_solver import walk,cl_rank,add_row,known,reduce_row,ROOT,HERE
standard=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];base,end=walk(standard);d=end[:2]

def build_window(K):
 local=[];options=[];groups=[]
 for i,(p,h,c) in enumerate(base):
  vv=[('L' if c=='R' else 'R')*4,c*4+('L' if c=='R' else 'R')*4];ids=[]
  for j,v in enumerate(vv):
   q=len(options);options.append((i,j));ids.append(q)
   for t,(p2,h2,c2) in enumerate(walk(v,(p[0],p[1],h))[0]):local.append((p2,(i,j,t),c2,q))
  groups.append(ids);local.append((p,(i,2,0),c,None))
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
  for a,b in groups:
   aa=k*len(options)+a;bb=k*len(options)+b;guards[aa].append((1<<bb,0));guards[bb].append((1<<aa,0))
 return N,eq,guards,list(range(K*len(options),(K+1)*len(options))),sorted(ev)

def closure(N,eq,guards):
 bs={};active=set();rounds=[]
 for m,b in eq:
  if not add_row(bs,m,b):return None,[]
 while True:
  zeros=ones=0
  for q in range(N):
   value=known(q,bs)
   if value==1 and q not in active:
    active.add(q);ones+=1
    for m,b in guards[q]:
     if not add_row(bs,m,b):return None,rounds
   elif value is None:
    if any(reduce_row(m,b,bs)==(0,1) for m,b in guards[q]):
     if not add_row(bs,1<<q,0):return None,rounds
     zeros+=1
  rounds.append(dict(forced_zero=zeros,activated=ones,rank=len(bs)))
  if not zeros and not ones:return bs,rounds

if __name__=='__main__':
 out=[]
 for K in range(1,int(sys.argv[1])+1):
  start=time.time();N,eq,g,central,cells=build_window(K);b,rounds=closure(N,eq,g)
  assert b is not None # Zero detours and the genuine standard highway are feasible.
  vals=[known(q,b) for q in central];r=dict(radius_periods=K,variables=N,complete_cells=len(cells),original_read_equations=len(eq),central_options=len(central),forced_central_zero=sum(v==0 for v in vals),unknown_central=[i for i,v in enumerate(vals) if v is None],rounds=rounds,seconds=time.time()-start)
  if K==3:
   classes=defaultdict(list)
   for p in cells:classes[cl_rank(p,d)[0]].append(p)
   assert len(cells)==143
   assert all(v==0 for v in vals)
   assert max(map(len,classes.values()))==7
   cert=dict(r,standard=standard,drift=d,cells=cells,maximum_black_token_window_multiplicity=max(map(len,classes.values())),central_variables=central,final_linear_rank=len(b),claim='All208 central optional excursions are forced absent without periodic identification.')
   (HERE/'window_rigidity_certificate.json').write_text(json.dumps(cert,indent=2))
  out.append(r);print(json.dumps(r),flush=True);(HERE/'window_detour_rigidity.json').write_text(json.dumps(out,indent=2))
