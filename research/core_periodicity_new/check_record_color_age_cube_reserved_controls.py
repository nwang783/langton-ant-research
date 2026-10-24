"""Independent finite-DAG tests for physical-domain reduced cube search.
All patch cells lie in one resource place. Every edge guards all reset cells,
consumes exactly their old black mass, and emits exactly their new black mass.
Thus the explicit forward oracle preserves resource mass == black-bit count.
The no-hit checker separately verifies source-domain predecessor closure for
EVERY individual reachable color, using all-count signed tail preimages.
"""
from pathlib import Path
from itertools import product
from random import Random
from collections import defaultdict
import json, subprocess, struct
rng=Random(1904812)
directory=Path('chronology_dcuv/delayed_height_probe/color_age_cube_reserved_controls');directory.mkdir(exist_ok=True)
def tails(a):return [sum(a[j:]) for j in range(5)]
def consume(x,I):
 for e in product(*[range(v+1) for v in x]):
  if sum(e)==sum(I) and all(a>=b for a,b in zip(tails(e),tails(I))):yield [x[j]-e[j] for j in range(5)]
def forward(np,nb,ops,edges):
 V=[set() for _ in range(np)];V[0].add((0,(0,0,0,0,0)))
 adj=defaultdict(list)
 for e in edges:adj[e[0]].append(e)
 for p in range(np):
  for col,x in list(V[p]):
   assert sum(x)==col.bit_count()
   for fr,to,a,oi,K,B,F,C,R in adj[p]:
    if col&K!=B:continue
    c,I,O=ops[oi]
    for rem in consume(x,I):
     after=[0]*5
     for j in range(5):after[min(4,j+c)]+=rem[j]
     after[c]+=O;cc=((col^F)&~C)|R
     assert sum(after)==cc.bit_count();V[to].add((cc,tuple(after)))
 return bool(V[-1]),sum(map(len,V))
results=[];checkedbases=0
for case in range(500):
 np=rng.randrange(3,10);nb=rng.randrange(1,5);allbits=(1<<nb)-1;start=(0,allbits,0);ops=[];edges=[]
 for p in range(np-1):
  for q in range(p+1,np):
   if rng.random()>.45:continue
   for _ in range(1+(rng.random()<.15)):
    cl=rng.randrange(1<<nb);k=cl|rng.randrange(1<<nb);v=rng.randrange(1<<nb)&k;rs=rng.randrange(1<<nb)&cl
    c=rng.randrange(3);I=[0]*5
    for _ in range((v&cl).bit_count()):I[rng.randrange(5)]+=1
    oi=len(ops);ops.append((c,I,rs.bit_count()));edges.append((p,q,0,oi,k,v,0,cl,rs))
 # A disconnected graph is still a useful exact no-hit control.
 pre=directory/f'case{case:03}';dat=pre.with_suffix('.dat');basis=pre.with_suffix('.basis')
 with dat.open('w')as f:
  f.write(f'COLOROPS 1 {np} {len(edges)} {len(ops)} 1 1 {nb}\n');f.write(' '.join(map(str,start))+'\n');f.write(str(np-1)+'\n')
  for c,I,O in ops:f.write(' '.join(map(str,[c]+tails(I)+[O]))+'\n')
  for e in edges:f.write(' '.join(map(str,e))+'\n')
 reach=[set()for _ in range(np)];reach[0].add(0)
 for pp in range(np):
  for col in reach[pp]:
   for fr,to,a,oi,k,v,fl,cl,rs in edges:
    if fr==pp and col&k==v:reach[to].add(((col^fl)&~cl)|rs)
 rf=pre.with_suffix('.reach');wf=pre.with_suffix('.weights');sf=pre.with_suffix('.reservations');wf.write_text('1 1 1 1 1\n');sf.write_text(str(allbits)+'\n')
 with rf.open('wb')as f:
  f.write(b'COLRCH1\0');f.write(struct.pack('<III',nb,np,1))
  for cols in reach:f.write(struct.pack('<Q',sum(1<<c for c in cols)))
 p=subprocess.run(['./record_color_age_cube_reserved_backward',str(dat),'20000',str(basis),str(wf),str(rf),str(sf)],text=True,capture_output=True)
 assert p.returncode==0,(case,p.stdout,p.stderr)
 expected,nstates=forward(np,nb,ops,edges);hit=p.stdout.startswith('status COLOR_AGE_WITNESS');assert hit==expected,(case,expected,p.stdout,p.stderr);assert 'CAP'not in p.stdout
 if not hit:
  rows=basis.read_text().splitlines();assert rows[0].startswith('REACH_RESTRICTED ');assert rows[1].startswith('PHYSICAL_DOMAIN_REDUCED ');rows=rows[2:];head=list(map(int,rows[0].split()));assert head[:3]==[1,np,nb];by=defaultdict(list)
  for s in rows[1:]:
   pp,mask,val,*r=map(int,s.split());assert val&~mask==0 and r==sorted(r,reverse=True);by[pp].append((mask,val,r))
  def covered(pp,col,r):return any(col&mask==val and all(a<=b for a,b in zip(rr,r))for mask,val,rr in by[pp])
  for col in reach[np-1]:assert covered(np-1,col,[col.bit_count(),0,0,0,0])
  assert not covered(0,0,[0]*5)
  inc=defaultdict(list)
  for e in edges:inc[e[1]].append(e)
  for pp,lab in by.items():
   for mask,val,t in lab:
    for fr,to,a,oi,k,v,fl,cl,rs in inc[pp]:
     c,ii,O=ops[oi];I=tails(ii);need=[I[0]+max(0,t[0]-O,t[c+1]if c<4 else 0)]+[I[j]+(t[j+c]if j+c<5 else 0)for j in range(1,5)]
     for col in reach[fr]:
      if col&k==v and((((col^fl)&~cl)|rs)&mask)==val:
       domneed=need.copy();domneed[0]=max(domneed[0],col.bit_count());assert covered(fr,col,domneed),(case,fr,to,col,domneed)
  checkedbases+=1
 results.append({'case':case,'vertices':np,'color_bits':nb,'edges':len(edges),'reachable':expected,'explicit_states':nstates})
R={'status':'PASS','controls':len(results),'independently_checked_no_hit_bases':checkedbases,'explicit_oracle':'Finite acyclic graph; enumerates all actual consumed age submultisets. Every physical state has resource mass exactly equal to patch black-bit count. No resource-count cap.','basis_scope':'Reach-restricted, physical-domain reduced closure, not unrestricted cube closure.','results':results};(directory/'summary.json').write_text(json.dumps(R,indent=2)+'\n');print({k:v for k,v in R.items()if k!='results'})
