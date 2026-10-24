"""Find the canonical first fresh R after the signed two-phase checkpoint,
and prove its complete all-M prior READ/seed disjointness before any edit.
No modified trajectory is executed by this tool.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib
from check4352_noncrossing_producer import V
from check_prepared1564_router_geometry import trace
P=Path(__file__).resolve().parent;J=json.loads((P/'prepared4352_two_phase_manifest.json').read_text())
fam=defaultdict(set)
for s in J['stages']:
 base=(s['start_x_N_constant'][1],s['start_y_N_constant'][1]);a=(s['start_x_N_constant'][0],s['start_y_N_constant'][0]);cc=tuple(s['count_N_constant']);rr=list(trace(s['word'],base,s['heading']));d=(rr[-1][1][0]-base[0],rr[-1][1][1]-base[1])if cc!=(0,1)else(0,0)
 for _,q,h,c in rr[:-1]:fam[q[0]-q[1]].add((q,a,d,cc,s['kind']))
def eligible(q,f):
 base,a,d,count,kind=f;lo=1;hi=None;assert a[0]==a[1]
 if d==(0,0):
  n=None
  for j in range(2):
   dif=q[j]-base[j]
   if not a[j]:
    if dif:return None
   elif dif%a[j]:return None
   else:
    nn=dif//a[j]
    if n is not None and nn!=n:return None
    n=nn
  return(1,None)if n is None else((n,n)if n>=1 else None)
 assert d[0]==d[1]and a[0]%d[0]==0
 if(q[0]-base[0])%d[0]or(q[1]-base[1])!=(q[0]-base[0]):return None
 alpha=-a[0]//d[0];beta=(q[0]-base[0])//d[0]
 for m,c in[(alpha,beta),(count[0]-alpha,count[1]-1-beta)]:
  if not m:
   if c<0:return None
  elif m>0:lo=max(lo,-(c//m))
  else:
   bound=c//(-m);hi=bound if hi is None else min(hi,bound)
 return None if hi is not None and lo>hi else(lo,hi)
seedfam=[((x[1],y[1]),(x[0],y[0]),(0,0),(0,1),'seed')for x,y in J['seed_families']]
# Literal unmodified M1 history, solely to identify its first fresh R.
v=lambda a:a[0]+a[1];B={(v(x),v(y))for x,y in J['seed_families']};initial=set(B);p=(v(J['initial_pose']['x_N_constant']),v(J['initial_pose']['y_N_constant']));h=3;t=0;read=set()
for s in J['stages']:
 for r in range(v(s['count_N_constant'])):
  for c in s['word']:
   assert(p in B)==(c=='L');read.add(p);B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=(p[0]+V[h][0],p[1]+V[h][1]);t+=1
assert(p,h)==((117,111),0);cp=t;word=J['stages'][-1]['word'];tested=[];extra=[];extra_cells=set();earlier_R_covered=[]
for i,c in enumerate(word):
 assert(p in B)==(c=='L')
 if c=='R' and p not in extra_cells and p in read:
  ranges=sorted([eligible(p,f)for f in fam.get(p[0]-p[1],())if eligible(p,f)is not None],key=lambda z:z[0]);covered=0
  for lo,hi in ranges:
   if lo>covered+1:break
   if hi is None:covered=None;break
   covered=max(covered,hi)
  assert covered is None,('earlier R not always old',i,p,covered)
  earlier_R_covered.append([i,list(p),len(ranges)])
 if p not in read and c=='R':
  hits=[(f,eligible(p,f))for f in fam.get(p[0]-p[1],())if eligible(p,f)is not None];seedhits=[(f,eligible(p,f))for f in seedfam if eligible(p,f)is not None]
  tested.append({'offset':i,'pose':[p,h],'all_M_prior_hits':len(hits),'all_M_seed_hits':len(seedhits)})
  if not hits and not seedhits:
   out={'scope':__doc__,'status':'CANONICAL FRESH MARKER ALL-M PROVED','marker':list(p),'incoming_heading':h,'offset_after_checkpoint':i,'read_time_M_constant':[129780,455161+i],'actual_unmodified_turn':'R','original_black_mass':394,'hypothetical_preloaded_mass':395,'relevant_unique_affine_read_families_tested':len(fam.get(p[0]-p[1],())),'all_unique_affine_read_families':sum(map(len,fam.values())),'seed_families_tested':len(seedfam),'first_M1_fresh_candidates':tested,'earlier_R_prior_union_covered_all_M':earlier_R_covered,'preceding_unmodified_return_prefix':''.join(extra),'complete_prior_read_miss_all_M':True,'original_seed_miss_all_M':True,'manifest_sha256':hashlib.sha256((P/'prepared4352_two_phase_manifest.json').read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
   (P/'prepared4352_fresh_return_marker.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));break
 extra_cells.add(p);read.add(p);B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=(p[0]+V[h][0],p[1]+V[h][1]);t+=1;extra.append(c)
else:raise AssertionError('no canonical fresh R in the first return period')
