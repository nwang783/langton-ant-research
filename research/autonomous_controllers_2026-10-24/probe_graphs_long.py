exec(open('/workspace/shared/langton/autonomous_controllers_2026-10-24/probe.py').read().split("print('d'")[0])
B=set(map(tuple,a['seed']));p=(0,0);h=a['heading']
def edges(q,sig):
 x,y=q;a=1;b=1 if (x+y)%2==sig else -1
 return ((2*x-a,2*y-b),(2*x+a,2*y+b))
def cyc(B,sig):
 parent={};sizes={};e=0
 def find(a):
  parent.setdefault(a,a)
  while parent[a]!=a: parent[a]=parent[parent[a]];a=parent[a]
  return a
 for q in B:
  v,w=edges(q,sig);v,w=find(v),find(w)
  if v!=w:parent[v]=w
  else:e+=1
 return e
sig=(sum(p)+h)%2
stats=[]
for t in range(21*P):
 if t%P==0:stats.append((t%P,cyc(B,sig),cyc(B,1-sig)))
 c='L' if p in B else 'R';assert c==w[t%P];B.symmetric_difference_update((p,));h=(h+(1 if c=='R' else -1))%4;p=tuple(p[j]+D[h][j] for j in range(2))
print(stats)
