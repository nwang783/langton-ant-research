"""Finite exact controls for three components of the automatic forced-seed proof.
Not an implementation of the complete arbitrary-mass ant-presentation solver.
"""
import pathlib,sys,json,time,itertools,collections,functools
HERE=pathlib.Path(__file__).parent
sys.path.insert(0,str(HERE.parent/'unit_inductive_certificates'))
from check_read_sets import typed,D

# Support-preserving base reduction and exact genuine-cycle reinsertion.
def vertices(edges,start,word):
 out=[start]
 for e in word:
  u,v=edges[e];assert u==out[-1];out.append(v)
 return out

def compress(edges,start,word):
 original=collections.Counter(word);base=list(word)
 while True:
  vs=vertices(edges,start,base);counts=collections.Counter(base);cut=None
  for i in range(len(base)):
   for j in range(i+1,len(base)+1):
    if vs[i]!=vs[j]:continue
    removed=collections.Counter(base[i:j])
    if all(counts[e]>removed[e] for e in removed):cut=(i,j);break
   if cut:break
  if cut is None:break
  i,j=cut;base=base[:i]+base[j:]
 assert set(base)==set(word)
 V=len(set(itertools.chain.from_iterable(edges)))
 assert len(base)<=V*(len(edges)+1)-1
 remaining=original-collections.Counter(base);cycles=collections.Counter()
 while remaining:
  first=min(remaining);v=edges[first][0];path=[];seen={v:0}
  while True:
   e=min(e for e,c in remaining.items() if c and edges[e][0]==v)
   path.append(e);v=edges[e][1]
   if v in seen:
    cycle=path[seen[v]:];break
   seen[v]=len(path)
  # Canonical directed cyclic rotation; the edge alphabet is distinct.
  cycle=min(tuple(cycle[i:]+cycle[:i]) for i in range(len(cycle)))
  mult=min(remaining[e] for e in cycle)
  for e in cycle:
   remaining[e]-=mult
   if not remaining[e]:del remaining[e]
  cycles[cycle]+=mult
 result=[];done=set();vs=vertices(edges,start,base)
 for i,v in enumerate(vs):
  if v not in done:
   for c,m in sorted(cycles.items()):
    if edges[c[0]][0]==v:result.extend(c*m)
   done.add(v)
  if i<len(base):result.append(base[i])
 assert collections.Counter(result)==original
 assert vertices(edges,start,result)[-1]==vertices(edges,start,word)[-1]
 return len(base),len(cycles)

# Sibling decomposition, independently compared to incremental literal parity.
def prefix_controls(images,root,maxdepth):
 phi=typed(images)
 @functools.lru_cache(None)
 def parity(s,r):
  if not r:return frozenset({(0,0)})
  out=set()
  for t,p in phi[s]:out.symmetric_difference_update((x+p[0],y+p[1]) for x,y in parity(t,r-1))
  return frozenset(out)
 checks=0
 for depth in range(maxdepth+1):
  leaves=[]
  def unfold(s,r,p,path):
   if not r:leaves.append((s,p,path));return
   for j,(t,w) in enumerate(phi[s]):unfold(t,r-1,(p[0]+w[0],p[1]+w[1]),path+(j,))
  unfold(root,depth,(0,0),())
  actual=set()
  for terminal,z,path in leaves:
   total=set();s=root;v=(0,0)
   for d,j in enumerate(path,1):
    for t,w in phi[s][:j]:
     total.symmetric_difference_update((x+v[0]+w[0],y+v[1]+w[1]) for x,y in parity(t,depth-d))
    t,w=phi[s][j];v=(v[0]+w[0],v[1]+w[1]);s=t
   assert s==terminal and v==z and total==actual
   checks+=1
   actual.symmetric_difference_update({z})
  assert actual==set(parity(root,depth))
 return checks

# General F2 projection of ONE bounded hidden binary coordinate.
def project(states,start,accept,visible,delta):
 initial=1<<start;queue=[initial];index={initial:0};trans=[];outputs=[]
 acceptmask=sum(1<<s for s in accept)
 for mask in queue:
  row=[]
  for a in visible:
   new=0
   for s in states:
    if mask>>s&1:
     for qbit in (0,1):new^=1<<delta(s,a,qbit)
   if new not in index:index[new]=len(queue);queue.append(new)
   row.append(index[new])
  trans.append(row);outputs.append((mask&acceptmask).bit_count()%2)
 return trans,outputs

def bitsrun(machine,values,pad=0):
 trans,out=machine;L=max(1,*[v.bit_length() for v in values])+pad;s=0
 for j in range(L-1,-1,-1):
  a=tuple(v>>j&1 for v in values);letter=sum(v<<(len(a)-1-i) for i,v in enumerate(a));s=trans[s][letter]
 return out[s]

def main():
 start=time.monotonic();coverchecks=0;maxbase=0
 graphs=[(2,[(0,0),(0,1),(1,0),(1,1)]),(3,[(0,1),(1,0),(1,2),(2,1),(2,2)]),
  (4,[(0,1),(1,0),(2,3),(3,2)]),(3,[(0,1),(0,1),(1,2),(2,0),(1,1),(2,2)])]
 for nv,edges in graphs:
  for source in range(nv):
   words=[[]]
   for length in range(9):
    for w in words:
     b,c=compress(edges,source,w);maxbase=max(maxbase,b);coverchecks+=1
    words=[w+[e] for w in words for e,(u,v) in enumerate(edges) if u==vertices(edges,source,w)[-1]]
 prefixchecks=0
 for images,depth in [(['R','L']*4,5),(['RRRRR','LLLLL']*4,4),(['RLLLLRRRR','LRRRRLLLL']*4,3)]:
  for root in range(8):prefixchecks+=prefix_controls(images,root,depth)
 # q<n and Thue-Morse(q)=1. Comparison states -1,0,1 and bit parity.
 st=list(itertools.product((-1,0,1),(0,1)));idx={s:i for i,s in enumerate(st)}
 def delta(s,a,q):
  c,p=st[s];n=a[0];c=c if c else (q>n)-(q<n)
  return idx[c,p^q]
 m=project(range(len(st)),idx[0,0],{idx[-1,1]},[(0,),(1,)],delta)
 projectionchecks=0
 for n in range(1024):
  expected=sum(q.bit_count()%2 for q in range(n))%2
  for padding in (0,1,3):assert bitsrun(m,(n,),padding)==expected;projectionchecks+=1
 # q<n and q+a=0 mod3; a is a visible second parameter.
 st2=list(itertools.product((-1,0,1),range(3),range(3)));idx2={s:i for i,s in enumerate(st2)}
 def delta2(s,a,q):
  c,res,ar=st2[s];nb,ab=a;c=c if c else (q>nb)-(q<nb)
  return idx2[c,(2*res+q)%3,(2*ar+ab)%3]
 m2=project(range(len(st2)),idx2[0,0,0],{i for i,(c,r,a) in enumerate(st2) if c==-1 and (r+a)%3==0},list(itertools.product((0,1),repeat=2)),delta2)
 for n in range(64):
  for a in range(64):
   expected=sum((q+a)%3==0 for q in range(n))%2
   for padding in (0,2):assert bitsrun(m2,(n,a),padding)==expected;projectionchecks+=1
 out=dict(genuine_cover_reconstructions=coverchecks,largest_base_in_controls=maxbase,
  all_position_prior_parity_equalities=prefixchecks,finite_fiber_projection_checks=projectionchecks,
  determinized_projection_states=[len(m[0]),len(m2[0])],seconds=time.monotonic()-start,
  scope='Exact finite controls of bounded genuine covers, full sibling-prefix parity and F2 hidden-coordinate projection. Not an integrated arbitrary-mass ant solver.')
 (HERE/'forced_seed_components.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
