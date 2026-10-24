"""Finite exact algebra controls for canonical frame -> initial-board XOR edges.
This is not the integrated all-level automatic graph construction.
"""
import sys,pathlib,json,random,time
HERE=pathlib.Path(__file__).parent
sys.path.insert(0,str(HERE.parent/'unit_inductive_certificates'))
from check_read_sets import typed,D

def replay(states):
 p=(0,0);odd=set();reads=set();prefix=[]
 for s in states:
  prefix.append(p);reads.add(p)
  if p in odd:odd.remove(p)
  else:odd.add(p)
  h=(s//2+(1 if s%2==0 else -1))%4
  p=(p[0]+D[h][0],p[1]+D[h][1])
 return odd,reads,p,prefix

def refine(word,phi,r):
 for _ in range(r):word=[t for s in word for t,p in phi[s]]
 return word

def references(phi,root):
 reach={root}
 while True:
  nxt=reach|{t for s in reach for t,p in phi[s]}
  if nxt==reach:break
  reach=nxt
 word=[root]
 while not reach<=set(word):word=refine(word,phi,1)
 return {s:word[:word.index(s)] for s in reach}

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def shifted(B,p):return {add(b,p) for b in B}

def satisfiable(edges,pins):
 parent={};par={}
 def find(v):
  if v not in parent:parent[v]=v;par[v]=0
  if parent[v]!=v:
   old=parent[v];root,c=find(old);par[v]^=c;parent[v]=root
  return parent[v],par[v]
 for u,v,c in list(edges)+[(u,'CONST_ZERO',c) for u,c in pins]:
  a,pa=find(u);b,pb=find(v)
  if a==b:
   if pa^pb!=c:return False
  else:parent[a]=b;par[a]=pa^pb^c
 return True

def main():
 start=time.monotonic();rng=random.Random(202610230345);records=[];checks=edges_total=0
 controls=[('identity',['R','L']*4),('five_monochromatic',['RRRRR','LLLLL']*4),
  ('five_defect',['RLLLL','LRRRR']*4),('nine_exact',['RLLLLRRRR','LRRRRLLLL']*4)]
 for name,images in controls:
  phi=typed(images);refs=references(phi,0);z={s:replay(w)[2] for s,w in refs.items()}
  pins=[];edges=[];snapshots=[]
  for s,v in refs.items():pins.append((z[s],int(s%2==1)^int(z[s] in replay(v)[0])))
  for r in range(3):
   Q={s:replay(refine([s],phi,r))[0] for s in refs}
   R={s:replay(refine([s],phi,r))[1] for s in refs}
   V={s:replay(refine(v,phi,r))[0] for s,v in refs.items()}
   V1={s:replay(refine(v,phi,r+1))[0] for s,v in refs.items()}
   for s in refs:
    earlier=set()
    for t,d in phi[s]:
     for w in shifted(R[t],d):
      u=add(w,z[s]);v=add(sub(w,d),z[t])
      c=int(u in V1[s])^int(w in earlier)^int(v in V[t])
      edges.append((u,v,c));edges_total+=1
      # Independently form COMPLETE canonical local boards for varying B,
      # then compare the literal frame discrepancy with the derived XOR.
      for _ in range(3):
       B={(rng.randrange(-3,4),rng.randrange(-3,4)) for _ in range(9)}
       Iparent=shifted(B^V1[s],(-z[s][0],-z[s][1]))
       Ichild=shifted(B^V[t],(-z[t][0],-z[t][1]))
       discrepancy=int(w in Iparent^earlier)^int(sub(w,d) in Ichild)
       assert discrepancy==(int(u in B)^int(v in B)^c)
       checks+=1
     earlier^=shifted(Q[t],d)
   snapshots.append(dict(max_child_depth=r,edges=len(edges),consistent=satisfiable(edges,pins)))
  if name=='identity':assert all(s['consistent'] for s in snapshots)
  else:assert not snapshots[-1]['consistent']
  records.append(dict(name=name,images=images,reachable_states=sorted(refs),pins=pins,levels=snapshots))
 out=dict(frame_equation_checks=checks,generated_edge_instances=edges_total,records=records,
 scope='Finite algebra controls only; all-level automatic projection and seed existence not executed.',seconds=time.monotonic()-start)
 (HERE/'parity_graph_controls.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
 print([(r['name'],r['levels']) for r in records])
if __name__=='__main__':main()
