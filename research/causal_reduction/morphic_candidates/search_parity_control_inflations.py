"""Four-symbol, time-parity-controlled k9,a3 inflations. Discovery enumerator.
A finite conflict excludes a candidate on every board; a horizon survivor is UNKNOWN.
"""
import json,itertools,pathlib,time,collections,sys
HERE=pathlib.Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0))
def check(images,root,limit):
 depth=0;n=1
 while n<limit:depth+=1;n*=9
 stack=[(root,depth)];x=y=h=t=0;last={};black=[]
 while stack and t<limit:
  s,d=stack.pop()
  if d:
   stack.extend((v,d-1)for v in reversed(images[s]));continue
  c=s//2;p=x,y;old=last.get(p)
  if old is not None and old[0]==c:return dict(status='CONFLICT',time=t,earlier=old[1],cell=p,turn='RL'[c],seed_size=len(black))
  if old is None and c:black.append(p)
  last[p]=(c,t);h=(h+(1 if c==0 else-1))%4;dx,dy=D[h];x+=dx;y+=dy;t+=1
 return dict(status='HORIZON_UNKNOWN',time=t,pose=[x,y,h],seed_size=len(black),seed=black)
if __name__=='__main__':
 limit=int(sys.argv[1])if len(sys.argv)>1 else 100000
 r=next(z for z in json.load(open(HERE/'free_inflations_k9.json'))['results']if z['scale']==[3,0]);opts=r['images'];records=[];counts=collections.Counter();latest=0;start=time.time()
 for choice in itertools.product(range(9),repeat=4):
  words=[opts['R'][choice[0]],opts['R'][choice[1]],opts['L'][choice[2]],opts['L'][choice[3]]]
  images=[[(s%2+j)%2+2*int(c=='L')for j,c in enumerate(w)]for s,w in enumerate(words)]
  for root in(0,2):
   if images[root][0]!=root:continue
   z=check(images,root,limit);z.update(choice=choice,words=words,images=images,root=root);records.append(z);counts[z['status']]+=1
   if z['status']=='HORIZON_UNKNOWN':print('SURVIVOR',root,choice,z['seed_size'],flush=True)
   else:latest=max(latest,z['time'])
 summary=dict(k=9,scale=[3,0],control='turn and time-index parity',limit=limit,cases=len(records),counts=dict(counts),latest_conflict=latest,seconds=time.time()-start,survivors=[r for r in records if r['status']=='HORIZON_UNKNOWN'])
 (HERE/'parity_control_inflations.json').write_text(json.dumps(summary,indent=2));(HERE/'parity_control_inflations_records.json').write_text(json.dumps(records));print(json.dumps({k:v for k,v in summary.items()if k!='survivors'},indent=2))
