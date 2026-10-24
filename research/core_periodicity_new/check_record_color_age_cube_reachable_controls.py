"""Separate finite-DAG controls for hybrid color/resource backward engine.
Forward oracle enumerates all consumed age submultisets, not the engine's formula.
Every no-hit basis is also checked for all color values and unbounded-resource
predecessor closure using the already signed tail-preimage formula.
"""
from pathlib import Path
from itertools import product
from random import Random
from collections import defaultdict
import json,subprocess,struct
rng=Random(904812);directory=Path('chronology_dcuv/delayed_height_probe/color_age_cube_reachable_controls');directory.mkdir(exist_ok=True)
def tails(a):return[sum(a[j:])for j in range(5)]
def consume(x,I):
 for e in product(*[range(v+1)for v in x]):
  if sum(e)==sum(I)and all(a>=b for a,b in zip(tails(e),tails(I))):yield[x[j]-e[j]for j in range(5)]
def forward(np,nb,start,ops,edges):
 V=[set()for _ in range(np)];p,k,v=start
 for col in range(1<<nb):
  if col&k==v:V[p].add((col,(0,0,0,0,0)))
 adj=defaultdict(list)
 for e in edges:adj[e[0]].append(e)
 for p in range(np):
  for col,x in list(V[p]):
   for fr,to,a,oi,K,B,F,C,R in adj[p]:
    if col&K!=B:continue
    c,I,O=ops[oi]
    for rem in consume(x,I):
     after=[0]*5
     for j in range(5):after[min(4,j+c)]+=rem[j]
     after[c]+=O;cc=((col^F)&~C)|R;V[to].add((cc,tuple(after)))
 return bool(V[-1])
results=[];checkedbases=0
for case in range(180):
 np=rng.randrange(3,9);nb=rng.randrange(1,5);allbits=(1<<nb)-1;K=rng.randrange(1<<nb);B=rng.randrange(1<<nb)&K;start=(0,K,B);ops=[]
 for _ in range(rng.randrange(3,10)):
  c=rng.randrange(3);I=[0]*5
  for _ in range(rng.randrange(3)):I[rng.randrange(5)]+=1
  O=rng.randrange(3);ops.append((c,I,O))
 edges=[]
 for p in range(np-1):
  for q in range(p+1,np):
   if rng.random()>.4:continue
   for _ in range(1+(rng.random()<.12)):
    k=rng.randrange(1<<nb);v=rng.randrange(1<<nb)&k;f=rng.randrange(1<<nb);cl=rng.randrange(1<<nb);rs=rng.randrange(1<<nb)&cl;edges.append((p,q,0,rng.randrange(len(ops)),k,v,f,cl,rs))
 pre=directory/f'case{case:03}';dat=pre.with_suffix('.dat');basis=pre.with_suffix('.basis')
 with dat.open('w')as f:
  f.write(f'COLOROPS 1 {np} {len(edges)} {len(ops)} 1 1 {nb}\n');f.write(' '.join(map(str,start))+'\n');f.write(str(np-1)+'\n')
  for c,I,O in ops:f.write(' '.join(map(str,[c]+tails(I)+[O]))+'\n')
  for e in edges:f.write(' '.join(map(str,e))+'\n')
 reach=[set()for _ in range(np)]
 for col in range(1<<nb):
  if col&K==B:reach[0].add(col)
 for pp in range(np):
  for col in reach[pp]:
   for fr,to,a,oi,k,v,fl,cl,rs in edges:
    if fr==pp and col&k==v:reach[to].add(((col^fl)&~cl)|rs)
 rf=pre.with_suffix('.reach');wf=pre.with_suffix('.weights');wf.write_text('1 1 1 1 1\n')
 with rf.open('wb')as ff:
  ff.write(b'COLRCH1\0');ff.write(struct.pack('<III',nb,np,1))
  for cols in reach:ff.write(struct.pack('<Q',sum(1<<c for c in cols)))
 p=subprocess.run(['./record_color_age_cube_reachable_backward',str(dat),'20000',str(basis),str(wf),str(rf)],text=True,capture_output=True,check=True);expected=forward(np,nb,start,ops,edges);hit=p.stdout.startswith('status COLOR_AGE_WITNESS');assert hit==expected,(case,expected,p.stdout,p.stderr);assert 'CAP'not in p.stdout
 if not hit:
  rows=basis.read_text().splitlines();assert rows[0].startswith('REACH_RESTRICTED ');rows=rows[1:];head=list(map(int,rows[0].split()));assert head[:3]==[1,np,nb];by=defaultdict(list)
  for s in rows[1:]:
   pp,mask,val,*r=map(int,s.split());assert val&~mask==0 and r==sorted(r,reverse=True);by[pp].append((mask,val,r))
  def covered(pp,col,r):return any(col&mask==val and all(a<=b for a,b in zip(rr,r))for mask,val,rr in by[pp])
  for col in range(1<<nb):
   assert(col not in reach[np-1])or covered(np-1,col,[0]*5)
   if col&K==B:assert not covered(0,col,[0]*5)
  inc=defaultdict(list)
  for e in edges:inc[e[1]].append(e)
  for pp,lab in by.items():
   for mask,val,t in lab:
    for fr,to,a,oi,k,v,fl,cl,rs in inc[pp]:
     c,ii,O=ops[oi];I=tails(ii);need=[I[0]+max(0,t[0]-O,t[c+1]if c<4 else 0)]+[I[j]+(t[j+c]if j+c<5 else 0)for j in range(1,5)]
     for col in range(1<<nb):
      if col in reach[fr]and col&k==v and((((col^fl)&~cl)|rs)&mask)==val:assert covered(fr,col,need),(case,fr,to,col,need)
  checkedbases+=1
 results.append({'case':case,'vertices':np,'color_bits':nb,'edges':len(edges),'reachable':expected})
R={'status':'PASS','controls':len(results),'independently_checked_no_hit_bases':checkedbases,'explicit_oracle':'Acyclic finite graph with all actual age-submultiset consumptions and all initial color values. No resource-count cap.','results':results};(directory/'summary.json').write_text(json.dumps(R,indent=2)+'\n');print({k:v for k,v in R.items()if k!='results'})
