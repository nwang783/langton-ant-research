from probe_marked_skeleton import word,F,SIX,D
from collections import Counter,defaultdict
n=8;w=word(n);p=(0,0);h=0;visited={};initial=set();reads=[];poses=[]
O=((0,-1),(-1,-1),(-1,0),(0,0))
for t,a in enumerate(w):
 if p not in visited and a=='L':initial.add(p)
 visited[p]=a;reads.append(p);poses.append((p,h))
 h=(h+(1 if a=='R' else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
initial=sorted(initial);owner={p:-(i+1)for i,p in enumerate(initial)}
parents={0:None};children=defaultdict(list);marks=Counter();starts={0:0};r=Counter();i=0
for t,(p,a) in enumerate(zip(reads,w)):
 if t>=10 and w[t-10:t]not in F and w[t-9:t+1]not in F and w[t-10:t+1]not in SIX:marks[i]+=1
 if a=='R':owner[p]=i;r[i]+=1
 else:par=owner.pop(p);i+=1;parents[i]=par;children[par].append(i);starts[i]=t+1
closure=set(marks)
for a in list(closure):
 while a is not None:closure.add(a);a=parents.get(a)
ac={a:[b for b in children[a]if b in closure]for a in closure}
b={};c={};root={};parentchain={}
for a in sorted(closure):
 par=parents.get(a);b[a]=b.get(par,0)+(a in marks);c[a]=c.get(par,0)+(len(ac[a])>=2);root[a]=root.get(par,a)
maxnode=max(b,key=b.get);chain=[]
a=maxnode
while a is not None:
 chain.append(a);a=parents.get(a)
print('maxdepth',b[maxnode],'root',chain[-1], 'rootposition',initial[-chain[-1]-1] if chain[-1]<0 else 'cursor')
for a in chain[::-1]:
 if a<0:continue
 t=starts[a];p,h=poses[t]if t<len(poses) else ((-n,n),0);v=(p[0]+O[h][0],p[1]+O[h][1])
 print('node',a,'t',t,'p,h',p,h,'Tait',v,'r',r[a],'marks',marks[a], 'markchildren',ac[a])
rr=Counter(root[a]for a in marks)
maxroot=max(rr,key=rr.get)
print('maxroot',maxroot,'initial',initial[-maxroot-1],rr[maxroot])
for a in sorted(closure):
 if a>=0 and root[a]==maxroot:
  t=starts[a];p,h=poses[t];v=(p[0]+O[h][0],p[1]+O[h][1])
  print('rootnode',a,'t',t,'Tait',v,'r',r[a],'marks',marks[a],'children',ac[a])
