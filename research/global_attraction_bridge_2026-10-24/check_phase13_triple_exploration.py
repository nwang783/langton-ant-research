from pathlib import Path
import hashlib,json
from check_return_permanent_output_debt import DXY,future
from blank_collision_operator import H
P=Path(__file__).parent;D=json.loads((P/'ALL_LENGTH_TWO_SIDED_MINIMUM_CHECKED.json').read_text());K=set(map(tuple,D['base']));W=D['base_word'];out=[];master=None
for k,N in[(10,6552),(100,23816),(500,65416)]:
 q=(2*k+2,2*k+1);T=104*k+13;seed=K|{(q[0]+2*a,q[1]+2*a)for a in range(3)};B={z:-i-1 for i,z in enumerate(sorted(seed))};p=(0,0);h=1;post=[];reads=[];imports=[];first={}
 for t in range(N):
  if p in seed and p not in first:first[p]=t
  old=B.pop(p,None)
  if old is None:B[p]=t;h=(h+1)%4;c='R'
  else:
   if t>=T and 0<=old<T:imports.append(dict(cell=p,birth=old,death=t))
   h=(h-1)%4;c='L'
  if t<T:assert c==(W*k+W[:13])[t]
  else:post.append(c);reads.append((p[0]-q[0],p[1]-q[1]))
  p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
 w,dr,dead,tests=future(B,p,h);assert w in{H[i:]+H[:i]for i in range(104)}
 pw=''.join(post)
 if k==100:master=pw
 if k==500:assert pw==master
 out.append(dict(k=k,seed=sorted(seed),contact=T,certificate_cut=N,post_word=pw,post_word_sha256=hashlib.sha256(pw.encode()).hexdigest(),post_bbox=[min(x for x,y in reads),max(x for x,y in reads),min(y for x,y in reads),max(y for x,y in reads)],initial_first_reads=[dict(cell=z,time=first[z])for z in sorted(seed)],finite_prefix_precontact_R_consumptions=imports,terminal_full_black=sorted(B),terminal_pose=[p,h],tail_word=w,tail_drift=dr,full_future_parity_tests=tests))
 print(k,hashlib.sha256(pw.encode()).hexdigest(),len(imports),flush=True)
(P/'PHASE13_TRIPLE_EXPLORATORY_CHECKED.json').write_text(json.dumps(dict(status='AUTHOR named controls only; not independently signed',scope='No all-k or arbitrary-cluster claim. Counts of old inputs cover the finite replay only.',controls=out),indent=2)+'\n')
