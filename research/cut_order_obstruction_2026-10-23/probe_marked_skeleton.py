from pathlib import Path
from collections import defaultdict,Counter
D=((0,1),(1,0),(0,-1),(-1,0))
W=Path('/workspace/shared/langton/word_stabilization/standard_word.txt').read_text().strip()
F={(W*2)[i:i+10] for i in range(104)}
SIX={'RRRLLRLLRLR','LLRLRLLRRLL','RRRRLRLLRLL','RRRLRRRRLRL','RRRLRRRRLRR','LRRLRRRRLRR'}

def word(n):return ''.join(('RLLR'*j+'L'+'RLLR'*j+'RLL'+'RLLR'*j+'L'+'RLLR'*j+'L')for j in range(n,0,-1))

def forest(w):
 # First derive required initial tokens from all first reads.
 p=(0,0);h=0;seen={};initial=set();reads=[]
 for t,a in enumerate(w):
  if p not in seen:
   if a=='L':initial.add(p)
  else:assert a!=seen[p]
  seen[p]=a;reads.append(p)
  h=(h+(1 if a=='R' else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 owner={p:-(i+1) for i,p in enumerate(sorted(initial))}
 parents={0:None};children=defaultdict(list);marks=Counter();n=0
 for t,(p,a) in enumerate(zip(reads,w)):
  if t>=10 and w[t-10:t] not in F and w[t-9:t+1] not in F and w[t-10:t+1] not in SIX:marks[n]+=1
  if a=='R':
   assert p not in owner;owner[p]=n
  else:
   assert p in owner;par=owner.pop(p);n+=1;parents[n]=par;children[par].append(n)
 # root-color ancestry, marked ancestor closure.
 closure=set(marks)
 for a in list(closure):
  while a is not None:
   closure.add(a);a=parents.get(a)
 activechildren={a:[b for b in children[a] if b in closure] for a in closure}
 roots=[a for a in closure if parents.get(a) is None]
 # Ascending chronological IDs have parents earlier, except virtual roots negative.
 b={};c={};root={}
 for a in sorted(closure):
  par=parents.get(a)
  b[a]=b.get(par,0)+(a in marks)
  c[a]=c.get(par,0)+(len(activechildren[a])>=2)
  root[a]=root.get(par,a)
 rootcounts=Counter(root[a] for a in marks)
 return {'nroots':len(roots),'mass':len(initial),'R':sum(marks.values()),'M':len(marks),'b':max(b.values(),default=0),'c':max(c.values(),default=0),'maxrootmarks':max(rootcounts.values(),default=0),'rootmarks':sorted(rootcounts.values())}
if __name__=='__main__':
 for n in range(1,21):
  r=forest(word(n));print(n,{k:v for k,v in r.items() if k!='rootmarks'})
