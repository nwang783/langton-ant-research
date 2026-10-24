from collections import defaultdict,Counter
import random,json
D=((0,1),(1,0),(0,-1),(-1,0))
def measure(w):
 a=defaultdict(list);hist=[];x=y=h=0
 for i,c in enumerate(w):
  hist.append(((x,y),h,c));a[x,y].append((i,h,c));h=(h+(1 if c=='R' else -1))%4;dx,dy=D[h];x+=dx;y+=dy
 same={v for v,s in a.items() if len(s)==3 and s[0][2]=='R' and s[0][1]==s[2][1]}
 third={a[v][2][0] for v in same}
 hits=[]
 for i in third:
  if i+1 in third and i>1 and i+3<len(w) and w[i-2:i]=='RL' and w[i+2:i+4]=='LR': hits.append(i)
 return same,hits,hist
rng=random.Random(5)
for it in range(200000):
 B=set(rng.sample([(x,y) for x in range(-5,6) for y in range(-5,6)],rng.randrange(20)));seed=B.copy();reads=Counter();w='';x=y=h=0
 for j in range(300):
  if reads[x,y]==3:break
  reads[x,y]+=1;c='L'if(x,y)in B else'R';w+=c
  B.symmetric_difference_update(((x,y),));h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];x+=dx;y+=dy
 same,hits,hist=measure(w)
 if hits:
  print(json.dumps({'seed':sorted(seed),'word':w,'hits':hits}));break
else: print('none')
