from pathlib import Path
from collections import defaultdict
root=Path('/workspace/shared/langton/word_stabilization')
lines=(root/'macros.txt').read_text().splitlines();macros={};k=1
while k<len(lines):
 a=lines[k].split();k+=1;name=a[0];n=int(a[4]);reads=[]
 for _ in range(n):
  x,y,c=map(int,lines[k].split());reads.append(((x,y),'L' if c else 'R'));k+=1
 macros[name]=reads
D=((0,1),(1,0),(0,-1),(-1,0))
def rot(q,h):
 x,y=q
 for _ in range(h%4):x,y=y,-x
 return x,y

def trace(word):
 p=(0,0);h=0;history={};tokens={};nodes=[];reads=[];cur=None;depth=[];parent=[];nodeinfo=[];feasible=True;fuel=0
 for block,m in enumerate(word):
  for j,(q,c) in enumerate(macros[m]):
   if cur is None:
    cur=len(nodes);nodes.append([]);nodeinfo.append((block,m,j));parent.append(-1);depth.append(0)
   if p in history and history[p]==c:return None
   if p not in history and c=='L':fuel+=1
   history[p]=c;reads.append((p,c,block,m,j,cur))
   if c=='R':tokens[p]=cur;nodes[cur].append(p)
   else:
    pp=tokens.pop(p,None);cur=len(nodes);nodes.append([]);nodeinfo.append((block,m,j+1));parent.append(-1 if pp is None else pp);depth.append(0 if pp is None else depth[pp]+1)
   h=(h+(1 if c=='R' else -1))%4;d=D[h];p=(p[0]+d[0],p[1]+d[1])
 return dict(fuel=fuel,maxdepth=max(depth),nodes=nodes,depth=depth,parent=parent,nodeinfo=nodeinfo)
for w in ['V'*n for n in [1,2,3,10,100]]+['U'*10,'CV'*10,'VBCV'*10]:
 o=trace(w);print(len(w),w[:20],None if o is None else (o['fuel'],o['maxdepth']))

# Node phase vertices; all crossing-macro parent relations conservatively allowed
# only when physical read cells can coincide on determinant-ten center lattice.

def entry(a,b,h):
 f=D[h];r=D[(h+1)%4]
 return ((-1+2*a-6*b-f[0]+r[0])//2,(1+6*a+2*b-f[1]+r[1])//2)

def subtract(a,b):return a[0]-b[0],a[1]-b[1]

def center_match(q):
 x,y=q
 if (x+3*y)%10 or (-3*x+y)%10:return None
 return (x+3*y)//10,(-3*x+y)//10

def phase_graph(alphabet):
 graph=defaultdict(set);records=[];types={};owners={}
 for m in alphabet:
  a=macros[m];lastL=-1
  for j,(q,c) in enumerate(a):
   if c=='L':lastL=j
   else:
    u=(m,lastL+1);owners[m,j]=u;types.setdefault(u,[]).append(j)
 for m in alphabet:
  seen={}
  for j,(q,c) in enumerate(macros[m]):
   if c=='L' and j+1<len(macros[m]) and macros[m][j+1][1]=='R':
    target=(m,j+1)
    if q in seen:
     i=seen[q];assert macros[m][i][1]=='R';source=owners[m,i];graph[source].add(target);records.append((source,target,'internal',i,j))
    else:
     if m=='V' and j==13:continue
     for n in alphabet:
      last={q:i for i,(q,c) in enumerate(macros[n])}
      for q0,i in last.items():
       if macros[n][i][1]!='R':continue
       for h in range(4):
        p0=entry(0,0,h);rq=rot(q0,h);base=(p0[0]+rq[0],p0[1]+rq[1]);off=subtract(q,base);ab=center_match(off)
        if ab is not None:
         source=owners[n,i];graph[source].add(target);records.append((source,target,'cross',n,i,m,j,h,ab))
   seen[q]=j
 for u in types:graph[u]|=set()
 return graph,records,types

def scc(graph):
 done=set();order=[]
 def dfs(u):
  if u in done:return
  done.add(u)
  for v in graph[u]:dfs(v)
  order.append(u)
 for u in graph:dfs(u)
 rev=defaultdict(set)
 for u,vs in graph.items():
  for v in vs:rev[v].add(u)
 done=set();comps=[]
 def dfs2(u,c):
  if u in done:return
  done.add(u);c.add(u)
  for v in rev[u]:dfs2(v,c)
 for u in reversed(order):
  if u not in done:
   c=set();dfs2(u,c);comps.append(c)
 return comps
for a in ['CV','CVB']:
 graph,recs,types=phase_graph(a);cs=scc(graph)
 print('graph',a,'vertices',len(graph),'edges',sum(map(len,graph.values())),'nontrivial',[(sorted(c),[(u,v) for u in c for v in graph[u] if v in c]) for c in cs if len(c)>1 or next(iter(c)) in graph[next(iter(c))]])
