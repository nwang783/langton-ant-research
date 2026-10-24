"""Paired-time direction substitutions, not turn substitutions.
Each paired displacement is a cardinal unit in rotated coordinates. Decode every
paired move into the unique two ant turns given its incoming vertical heading.
A finite chronology conflict excludes that rooted model on ANY coloring.
"""
import itertools,json,pathlib,sys,time
HERE=pathlib.Path(__file__).resolve().parent
D=((1,0),(0,1),(-1,0),(0,-1))
def rot(p,r):
 x,y=p
 for _ in range(r):x,y=-y,x
 return x,y

def check(prods,swap,sx,sy,limit):
 k=len(prods[0]);old=(0,0);dy_old=1;last={};firstL=[];word=''
 def direction(n):
  digits=[]
  while n:digits.append(n%k);n//=k
  c=0
  for d in reversed(digits):c=prods[c][d]
  return c
 for n in range(limit):
  u,v=D[direction(n)]
  if swap:u,v=v,u
  u*=sx;v*=sy;dx,dy=u+v,u-v
  reads=[(old,'R' if dx==dy_old else 'L'),((old[0]+dx,old[1]),'R' if dy==-dx else 'L')]
  for j,(p,c) in enumerate(reads):
   t=2*n+j
   if p in last and last[p][1]==c:
    return dict(status='CONFLICT',time=t,cell=p,letter=c,previous=last[p][0],firstL_count=len(firstL))
   if p not in last and c=='L':firstL.append(p)
   last[p]=(t,c)
  old=(old[0]+dx,old[1]+dy);dy_old=dy
 return dict(status='HORIZON_ONLY',pairs=limit,firstL_count=len(firstL),distinct_cells=len(last),endpoint=old)

def run(k,limit=100000):
 by={}
 for w in itertools.product(range(4),repeat=k):
  p=(sum(D[c][0] for c in w),sum(D[c][1] for c in w))
  if p[0]*p[0]+p[1]*p[1]>1:by.setdefault(p,[]).append(w)
 out=[];start=time.time()
 for a,rootwords in sorted(by.items()):
  rootwords=[w for w in rootwords if w[0]==0]
  if not rootwords:continue
  opts=[by[rot(a,r)] for r in range(4)];opts[0]=rootwords
  for prods in itertools.product(*opts):
   for swap,sx,sy in itertools.product([0,1],[-1,1],[-1,1]):
    result=check(prods,swap,sx,sy,limit)
    out.append(dict(scale=a,productions=prods,embedding=[swap,sx,sy],**result))
 counts={s:sum(z['status']==s for z in out) for s in ['CONFLICT','HORIZON_ONLY']}
 summary=dict(k=k,pairs_horizon=limit,cases=len(out),counts=counts,latest_conflict=max([z.get('time',0) for z in out],default=0),seconds=time.time()-start,results=out)
 (HERE/f'paired_direction_substitutions_k{k}.json').write_text(json.dumps(summary,indent=2))
 print(json.dumps({key:value for key,value in summary.items() if key!='results'},indent=2),flush=True)
if __name__=='__main__':
 for k in range(int(sys.argv[1]),int(sys.argv[2])+1):run(k)
