"""Literal controls for the supplied eventually-periodic matrix-power read graph."""
import json,itertools,pathlib,time
from check_read_sets import typed,literal,graph_walks,D
HERE=pathlib.Path(__file__).parent
I=((1,0),(0,1))
def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def mp(A,r):
 P=I
 for _ in range(r):P=mm(P,A)
 return P

def mv(A,p):return tuple(sum(A[i][j]*p[j] for j in range(2)) for i in range(2))

def images_for(A):
 images=[]
 for s in range(8):
  incoming=s//2;outgoing=(incoming+(1 if s%2==0 else -1))%4;target=mv(A,D[outgoing]);found=None
  for k in range(3,16,2):
   for cs in itertools.product('RL',repeat=k):
    p=(0,0);h=incoming
    for c in cs:
     h=(h+(1 if c=='R' else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
    if p==target and h==outgoing:found=''.join(cs);break
   if found:break
  assert found,(A,s)
  images.append(found)
 return images

def finite_graph(images,A,mu,q):
 assert mp(A,mu+q)==mp(A,mu)
 subst=typed(images);graph={}
 for s in range(8):
  if mu==0:
   for ph in range(q):graph[s,'h',ph]=[((t,'h',(ph-1)%q),mv(mp(A,ph),p)) for t,p in subst[s]]
  else:
   for ph in range(q):
    edges=[]
    for t,p in subst[s]:
     w=mv(mp(A,mu+ph),p)
     edges.append(((t,'h',(ph-1)%q),w))
     if ph==0:edges.append(((t,'l',mu-1),w))
    graph[s,'h',ph]=edges
   for ph in range(mu):
    graph[s,'l',ph]=[((t,'l',ph-1) if ph else (t,'t',0),mv(mp(A,ph),p)) for t,p in subst[s]]
   graph[s,'t',0]=[]
 return graph

def reads(graph,s,r,mu,q):
 if r==0:return {(0,0)}
 if mu==0:start=(s,'h',(r-1)%q)
 elif r>mu:start=(s,'h',(r-1-mu)%q)
 else:start=(s,'l',r-1)
 return {p for st,p in graph_walks(graph,start,r) if mu==0 or st[1]=='t'}

def main():
 start=time.monotonic();cases=[];checks=letters=0
 inputs=[(((1,2),(0,-1)),0,2),(((1,1),(0,0)),1,1),(((-1,-1),(0,0)),1,2),(((1,1),(0,0)),3,2)]
 for A,mu,q in inputs:
  images=images_for(A);graph=finite_graph(images,A,mu,q);counts=[]
  for s in range(8):
   out=(s//2+(1 if s%2==0 else -1))%4
   for r in range(6):
    actual,p,h,n=literal(images,s,r);expected=reads(graph,s,r,mu,q)
    assert actual==expected,(A,mu,q,s,r,actual^expected)
    assert p==mv(mp(A,r),D[out]) and h==out
    checks+=1;letters+=n;counts.append([s,r,len(actual),n])
  cases.append(dict(matrix=A,preperiod=mu,period=q,images=images,counts=counts))
 result=dict(literal_checks=checks,literal_letters=letters,cases=cases,
 scope='Exact read-set graph controls; no ant legality or successful growing seed claimed.',seconds=time.monotonic()-start)
 (HERE/'finite_power_graph.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))
if __name__=='__main__':main()
