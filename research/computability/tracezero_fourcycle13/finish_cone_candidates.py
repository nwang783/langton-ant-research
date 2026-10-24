#!/usr/bin/env python3
"""Complete the justified trace-zero escape using spectral and literal filters."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,itertools,json,math,time,hashlib
root=Path(__file__).parent
spec=importlib.util.spec_from_file_location('cone',root/'cone_filter.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
domains=mod.domains;F=mod.F;k=13;D=((0,1),(1,0),(0,-1),(-1,0));limit=3000
digits=[]
for n in range(limit):
 z=n;ds=[0]*4
 for j in range(3,-1,-1):ds[j]=z%k;z//=k
 digits.append(ds)
def local_check(indices,ex,ey,den):
 imgs=[domains[d][indices[d]]['word'] for d in range(4)]
 p=(0,0);h=0;board={};previous={};origin_bits={1:0,3:1};fail={};walk=[]
 # First movement N: incoming E gives L (black), W gives R (white).
 # After the first read the origin current colors are consequently0 and1.
 for t,ds in enumerate(digits):
  if ex*p[0]+ey*p[1] < 2*den*max(abs(p[0]),abs(p[1])):
   return dict(kind='cone',read=t,cell=p,initial_heading_conflicts=fail)
  d=0
  for j in ds:d=imgs[d][j]
  assert t or d==0
  if t:
   bit=int((d-h)%4==3);assert (d-h)%4 in(1,3)
   if p==(0,0):
    for ih in list(origin_bits):
     if origin_bits[ih]!=bit:
      fail[ih]=dict(read=t,cell=p,previous=previous.get(p),wanted=bit,available=origin_bits[ih]);del origin_bits[ih]
     else:origin_bits[ih]^=1
   elif p in board and board[p]!=bit:
    for ih in origin_bits:fail[ih]=dict(read=t,cell=p,previous=previous[p],wanted=bit,available=board[p])
    origin_bits.clear()
   else:board[p]=1-bit
   if not origin_bits:return dict(kind='literal',read=t,cell=p,initial_heading_conflicts=fail)
  previous[p]=t;p=(p[0]+D[d][0],p[1]+D[d][1]);h=d
 return dict(kind='survivor',reads=limit,headings=list(origin_bits))
start=time.monotonic();records=[];summaries=[];survivors=[]
for bits in itertools.product((0,1),repeat=4):
 G=tuple((F[d]+2*bits[d])%4 for d in range(4));states,t,q=mod.map_powers(G)
 weighted=[]
 for d in range(4):
  opts=[]
  for index,row in enumerate(domains[d]):
   w=row['word']
   if w[-1]!=G[d]:continue
   bs=[]
   for fp,gp in states:
    b=[0]*4;b[d]=sum(1 if (fp[v]-gp[u])%4==1 else -1 for u,v in zip(w,w[1:]));bs.append(b)
   opts.append((index,mod.constants(bs,t,q)))
  weighted.append(opts)
 cd=math.lcm(*(v[0].denominator for opts in weighted for _,v in opts));ed=math.lcm(*(z.denominator for opts in weighted for _,v in opts for z in v[1:]))
 ww=[[(i,int(v[0]*cd),int(v[1]*ed),int(v[2]*ed)) for i,v in opts] for opts in weighted]
 pairmaps=[]
 for d1,d2 in [(0,1),(2,3)]:
  mp={}
  for i,c,x,y in ww[d1]:
   for j,f,z,w in ww[d2]:mp.setdefault(c+f,[]).append((x+z,y+w,i,j))
  pairmaps.append(mp)
 counts=dict(controllers=math.prod(map(len,ww)),zero_C=0,root_cone_pass=0,cone_conflicts=0,literal_conflicts=0,survivors=0)
 for C,left in pairmaps[0].items():
  right=pairmaps[1].get(-C,[])
  counts['zero_C']+=len(left)*len(right)
  for x,y,i,j in left:
   for z,w,l,m in right:
    if y+w<2*ed:continue
    counts['root_cone_pass']+=1;indices=(i,j,l,m);r=local_check(indices,x+z,y+w,ed)
    if r['kind']=='survivor':counts['survivors']+=1;survivors.append(dict(indices=indices,last_map=G,ell=[str(Q(x+z,ed)),str(Q(y+w,ed))],**r))
    else:counts[r['kind']+'_conflicts']+=1
    records.append(dict(indices=indices,last_map=G,ell=[str(Q(x+z,ed)),str(Q(y+w,ed))],**r))
 summaries.append(dict(last_map=G,charge_denominator=cd,coordinate_denominator=ed,**counts))
 print(json.dumps(summaries[-1]),flush=True)
raw=json.dumps(records,sort_keys=True,separators=(',',':')).encode()+b'\n';(root/'cone_candidates.records.json').write_bytes(raw)
out=dict(status='COMPLETE SCOPED FILTER' if not survivors else'LOCAL SURVIVORS REQUIRE ALL-TIME CERTIFICATION',
 matrix=mod.A,k=k,first_map=F,root=0,literal_limit=limit,
 totals={key:sum(r[key] for r in summaries) for key in counts},
 latest=max((r['read'] for r in records if r['kind']!='survivor'),default=None),
 survivors=survivors,last_map_summaries=summaries,
 records_sha256=hashlib.sha256(raw).hexdigest(),seconds=time.monotonic()-start)
(root/'cone_candidates.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='last_map_summaries'}))
