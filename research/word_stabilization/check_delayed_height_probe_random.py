from pathlib import Path
import random,subprocess,json,collections,hashlib
rng=random.Random(57193);R=Path('/workspace/shared/langton');B=R/'core_periodicity_new';O=B/'chronology_dcuv/delayed_height_probe/random_controls';O.mkdir(exist_ok=True)
checks=[]
for case in range(150):
 n=rng.randrange(1,4);np=rng.randrange(2,6);F=0;cap=4;N=rng.randrange(2,12);E=[]
 for i in range(N):
  fr=rng.randrange(np);to=rng.randrange(np);k=rng.randrange(1<<n);v=rng.randrange(1<<n)&k;f=rng.randrange(1<<n);cl=rng.randrange(1<<n);r=rng.randrange(1<<n)&cl;goal=int(rng.randrange(12)==0);a=rng.randrange(10);h=rng.randrange(4);lo=rng.randrange(-3,3);hi=rng.randrange(lo,4);mo=rng.randrange(-1,2);c=rng.randrange(3);mi=[-999,-999]+[rng.choice([-999,-2,-1,0,1,2])for _ in range(3)];E.append([fr,to,k,v,f,cl,r,goal,a,h,lo,hi,mo,c,*mi])
 sid=0;sv=rng.randrange(1<<n);p=O/f'case{case:03}.dat'
 p.write_text(f'{n} {np} {N} {F} {cap}\n{sid} {(1<<n)-1} {sv}\n'+''.join(' '.join(map(str,e))+'\n'for e in E))
 start=(sid,sv,(0,)*5);seen={start};queue=collections.deque([(start,0)]);depth=None
 while queue:
  (pos,col,Q),d=queue.popleft()
  for e in E:
   fr,to,k,v,f,cl,r,g,a,h,lo,hi,mo,c,*mi=e
   if fr!=pos or col&k!=v:continue
   allowed=[q for q in range(lo,hi+1)if(q-h)%2==0 and all(z<-900 or q+z<=Q[j]for j,z in enumerate(mi))]
   if not allowed:continue
   if g:depth=d+1;queue.clear();break
   col2=((col^f)&~cl)|r
   for q in allowed:
    Q2=tuple(max(Q[max(j-c,0)],q+mo if j<=c else -999)for j in range(5));assert min(Q2)>=0 and max(Q2)<=cap
    nxt=(to,col2,Q2)
    if nxt not in seen:seen.add(nxt);queue.append((nxt,d+1))
  if depth is not None:break
 s=subprocess.check_output([str(B/'delayed_height_color_probe'),str(p),'1000000'],stderr=subprocess.DEVNULL,text=True);ln=s.splitlines()[0].split()
 if depth is None:assert ln[1]=='EXHAUSTED'and int(ln[3])==len(seen),(case,s,len(seen))
 else:assert ln[1]=='WITNESS'and int(ln[3])==depth,(case,s,depth)
 checks.append(dict(case=case,status=ln[1],depth=depth,explicit_states=len(seen)))
# Independent integer interval-image checks, including collapsed lower intervals.
for case in range(10000):
 Q=sorted([rng.randrange(-10,14)for _ in range(5)],reverse=True);h=rng.randrange(4);lo=rng.choice([-999999,rng.randrange(-20,15)]);hi=rng.randrange(-20,15);mo=rng.randrange(-6,8);c=rng.randrange(3);mi=[-999,-999]+[rng.choice([-999,*range(-6,8)])for _ in range(3)]
 hi2=min([hi]+[Q[j]-v for j,v in enumerate(mi)if v>-900]);hi2-=((hi2-h)%2)
 qs=[q for q in range(max(lo,-60),hi2+1)if(q-h)%2==0];brute={tuple(max(Q[max(j-c,0)],q+mo if j<=c else -999)for j in range(5))for q in qs}
 images=set();z=min(hi2,Q[0]-mo);z-=((z-h)%2)
 if z>=lo:
  images.add(tuple(Q[0]if j<=c else Q[j-c]for j in range(5)))
 z=max(lo,Q[0]-mo+1);z+=(h-z)%2
 for q in range(z,hi2+1,2):images.add(tuple(q+mo if j<=c else Q[j-c]for j in range(5)))
 assert images==brute,(case,Q,lo,hi,images,brute)
(O/'summary.json').write_text(json.dumps({'status':'PASS','random_graphs':checks,'interval_controls':10000,'engine_sha256':hashlib.sha256((B/'delayed_height_color_probe.cpp').read_bytes()).hexdigest()},indent=2)+'\n');print('PASS150 explicit graph controls and10000 interval image controls')
