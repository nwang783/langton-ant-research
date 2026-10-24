"""Continue one literal prepared D4 prefix toward its fixed remaining complete histories.
Known cells start white. All exterior first-read colors are explicitly prepared.
No translating-front, global-WHITE or unbounded negative conclusion is possible.
"""
from pathlib import Path
from collections import Counter
import json,ast,heapq,time
H='NESW';D=((0,1),(1,0),(0,-1),(-1,0))
rr=json.loads(Path(__file__).with_name('canonical_duplicator_local_parent_return.json').read_text())['rows']
row=rr[0]
hh={ast.literal_eval(k):v for k,v in row['headings'].items()};ps=sorted(hh);ix={p:i for i,p in enumerate(ps)};target=sum(len(h)for h in hh.values());goal=sum(len(hh[p])<<(3*i)for i,p in enumerate(ps));ext=[(x,y)for x in range(-6,6)for y in range(-4,7)if(x,y)not in ix];ei={p:i for i,p in enumerate(ext)}
# Records are (position, incoming heading index, packed known ranks, seen exterior,
# current exterior black mask, initial exterior black mask, length, predecessor, turn).
prefix=json.loads(Path(__file__).with_name('prepared_D4_manual_connected_prefix.json').read_text())
known_ranks={ast.literal_eval(k):v for k,v in prefix['known_ranks'].items()}
all_seen={ast.literal_eval(k):v for k,v in prefix['all_seen'].items()}
c0=sum(known_ranks[p]<<(3*i)for i,p in enumerate(ps))
seen0=sum(1<<i for p,i in ei.items()if p in all_seen)
black0=sum(1<<ei[tuple(p)]for p in prefix['current_black']if tuple(p)in ei)
seed0=sum(1<<ei[tuple(p)]for p in prefix['prepared_black'])
pose=prefix['end_pose'];records=[(tuple(pose[0]),H.index(pose[1]),c0,seen0,black0,seed0,prefix['raw_length'],None,None)];heap=[(0,0)];memo={};best=(prefix['known_reads'],0);serial=1;start=time.monotonic();expanded=0;found=None
while heap and expanded<250000 and time.monotonic()-start<18:
 _,si=heapq.heappop(heap);p,h,c,seen,black,seed,t,prev,tr=records[si]
 if c==goal:found=si;break
 if t>=256:continue
 key=(p,h,c,seen,black)
 if memo.get(key,10**9)<=t:continue
 memo[key]=t;expanded+=1
 if p in ix:
  i=ix[p];r=(c>>(3*i))&7
  if r>=len(hh[p])or H[h]!=hh[p][r]:continue
  choices=(('R'if r%2==0 else'L'),)
 elif p in ei:
  i=ei[p];b=1<<i
  choices=(('L'if black&b else'R'),)if seen&b else('R','L')
 else:continue
 for turn in choices:
  nc,nseen,nblack,nseed=c,seen,black,seed
  if p in ix:nc+=1<<(3*ix[p])
  else:
   b=1<<ei[p]
   if not(seen&b):
    nseen|=b
    if turn=='L':nseed|=b;nblack|=b
   nblack^=b
  nh=(h+(1 if turn=='R'else-1))%4;dx,dy=D[nh];np=(p[0]+dx,p[1]+dy)
  if np not in ix and np not in ei:continue
  prog=sum((nc>>(3*i))&7 for i in range(len(ps)))
  ni=len(records);records.append((np,nh,nc,nseen,nblack,nseed,t+1,si,turn))
  if prog>best[0]:best=(prog,ni)
  # Greedily prioritize completed actual known reads, then short outside connectors.
  remaining=[(q,hh[q][(nc>>(3*i))&7])for i,q in enumerate(ps)if((nc>>(3*i))&7)<len(hh[q])]
  dist=min((abs(np[0]-q[0])+abs(np[1]-q[1])for q,need in remaining),default=0)
  heapq.heappush(heap,(t+1-24*prog+dist,ni))
end=found if found is not None else best[1];chain=[];j=end
while records[j][7]is not None:
 r=records[j];prev=records[r[7]];chain.append(dict(p=prev[0],incoming=H[prev[1]],turn=r[8]));j=r[7]
chain.reverse();chain=prefix['trace']+chain;record=records[end];seed=[p for p,i in ei.items()if record[5]&(1<<i)]
out=dict(scope=__doc__,inventory=row['headings'],target_known_reads=target,completed_known_reads=sum((record[2]>>(3*i))&7 for i in range(len(ps))),found=found is not None,raw_length=len(chain),prepared_black=seed,expanded=expanded,elapsed_seconds=time.monotonic()-start,box=[-6,5,-4,6],maximum_raw_length=256,word=''.join(x['turn']for x in chain),trace=chain)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k not in['inventory','trace','word']},indent=2))
