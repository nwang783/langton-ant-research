from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];p=SELF.parent/'check_serial_bridge_archive_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('# Fixed local masks')[0],ns)
graph,component,rank,ends,connected,step,wvertex=[ns[k]for k in('graph','component','rank','ends','connected','step','wvertex')]
def phys(v):return 2*v.real+2*v.imag+1+1j*(2*v.real-2*v.imag+1)
def cells(vs):return {(phys(a)+phys(b))/4 for a,b in zip(vs,vs[1:])}
def line(a,b):
 d=b-a;assert d.real==0 or d.imag==0;sg=d/abs(d)if d else 0
 return[a+i*sg for i in range(int(abs(d))+1)]
def build(q):
 v=0j;P=[v];corners=[]
 for j in range(q):
  d=1j**j;v2=v+8*((j+2)//2)*d;P+=line(v,v2)[1:];corners.append(v2);v=v2
 knots=[-1j]
 for j,c in enumerate(corners[:-1]):
  d=1j**j;out=1j*d;knots.extend([c-out,c+2*d-out,c+2*d+out,c+d+out])
 knots.append(P[-1]-1j*(1j**(q-1)))
 C=[knots[0]]
 for b in knots[1:]:C+=line(C[-1],b)[1:]
 conn=[0,-1,-1-1j,-1j]
 assert len(set(C))==len(C)and set(C).isdisjoint(P)
 assert set(conn)&set(P)=={0}and set(conn)&set(C)=={-1j}
 old=cells(P);fixed=cells(C)|cells(conn);assert not old&fixed
 return P,C,conn,old,fixed
# Normalized exact dual corner patches, represented in twice-(a,b) coordinates.
def dual(a,b):
 m=(a+b)/2;d=b-a;return frozenset((2*m+1j*d,2*m-1j*d))
patch=[-1-1j,-1j,1-1j,2-1j,2,2+1j,1+1j,1+2j,1+3j]
pe=[dual(a,b)for a,b in zip(patch,patch[1:])]
assert pe[2]|pe[3]=={3-3j,3-1j,5-1j}
assert pe[4]|pe[5]|pe[6]=={5+1j,3+1j,3+3j,1+3j}
controls=[];stats=Counter()
for q in(1,2,3,4,5,8,12,20):
 P,C,conn,old,fixed=build(q);n=len(old);M=len(old|fixed)
 assert n==8*((q+1)**2//4)and len(C)-1==n+4*(q-1)and M==2*n+4*q-1
 assert M<=(2*q+3)**2 and 4*(q+2)**2>=M
 # Read geometry and complete union of every possible base edge are obtained from the actual literal candidate, before graph assertions.
 base=set(old);p=1+1j;h=1;word='';writes=set()
 for i,c in enumerate([(phys(a)+phys(b))/4 for a,b in zip(P,P[1:])]):
  r=0 if i==0 else 1+int((P[i+1]-P[i])/(P[i]-P[i-1])==1j)
  for ch in'R'*r+'L':
   assert('L'if p in base else'R')==ch
   if ch=='R':writes.add(p)
   p,h,ch2=step(base,p,h);assert ch2==ch;word+=ch
 assert (old|writes).isdisjoint(fixed)
 Vbase=set(graph(old|writes,0));todo=set(fixed);classes=Counter()
 while todo:
  e=next(iter(todo));vs,es=component(fixed,0,ends(e,0)[0]);todo-=es
  assert len(es)==len(vs)-1 and len(vs&Vbase)<=1
  classes[len(es),len(vs&Vbase)]+=1
 expected=Counter({(1,1):n-q+1,(2,0):q-1,(3,1):q-1,(3,0):1});expected+=Counter()
 assert classes==expected
 B=old|fixed;p=1+1j;h=1;assert rank(B,0)==rank(B,2)==0 and component(B,2,wvertex(p,h))[1]==B
 prior=set(B)|{1j};pp,hh,ch=step(prior,1j,2);assert(prior,pp,hh,ch)==(B,p,h,'L')
 marked={k:set(graph(B,k))|{wvertex(p,h)if k==2 else ns['zvertex'](p,h)}for k in(0,2)} if 'zvertex'in ns else {k:set(graph(B,k))for k in(0,2)}
 # Entry z current vertex already lies in an entry core edge; both w and z are marked.
 aw=0;initial=set(B);output=set();li=0
 for ch in word:
  e=p;es=ends(e,2)
  if ch=='R':
   for k in(0,2):assert not connected(B,k,*ends(e,k))
   aw+=len(set(es)-marked[2]);marked[2].update(es);output.add(e)
  else:
   assert e in old and e not in output
   for k in(0,2):assert not connected(B-{e},k,*ends(e,k))
  p,h,ch2=step(B,p,h);assert ch2==ch;stats['fine_reads']+=1
  if ch=='L':
   li+=1;remaining=cells(P[li:]);assert B==remaining|fixed|output
   active=component(B,2,wvertex(p,h))[1];assert active==remaining
   archive=fixed|output;assert component(archive,2,phys(0))[1]==archive
   stats['post_L_suffix_and_one_archive_checks']+=1
 assert li==n and aw==q-1 and len(B)==M+q-2 and len(word)==2*n+q-2
 assert rank(B,0)==rank(B,2)==0 and not graph(B,2).get(wvertex(p,h))
 assert component(B,2,phys(0))[1]==B
 assert len(marked[2])==len(B)+2 # one nontrivial tree and one retained isolated endpoint
 tail=''
 for _ in range(5):p,h,ch=step(B,p,h);tail+=ch
 assert tail=='RRRRL'
 controls.append({'q':q,'n':n,'M':M,'gain':q-2,'epoch_reads':len(word),'new_marked_w_vertices':aw,'fixed_z_components':[[list(k),v]for k,v in sorted(classes.items())]})
D=ROOT/'actual_zipper_spiral_2026-10-23';bind={}
for name,want in [('one_component_paired_forest_collector.md','ed7197b2f981ab73ef47df9a9c30d9a190bd739540bdd7cc19aae1875606956c'),('epoch_component_ledger.md','9996e812118f628afd909c9245e061dc8d13f4b8b0afef90db1342d12bc5e2b3')]:
 sh=hashlib.sha256((D/name).read_bytes()).hexdigest();assert sh==want;bind[name]=sh
out={'status':'PASS all-q charged one-tree paired-forest collector and exact epoch ledger','bindings':bind,'controls':controls,'counts':dict(stats),'analytic':['Spacing8 is a scaled version of the independently proved square-spiral run separation. Every nonconsecutive run is at least8 away in Chebyshev distance. Collector detours lie within distance2 of their own corners, and each run is at least8 long, so nonlocal and adjacent-corner patch contacts are absent. The initial connector near the origin is disjoint from all later spiral runs and patches.','The exact normalized detour dual decomposes into two-edge path {(3,-3),(3,-1),(5,-1)} with no base-union contact, three-edge path {(5,1),(3,1),(3,3),(1,3)} with one contact, and ordinary isolated dual edges with one contact. The connector dual is a disjoint three-edge star with no base-union contact. Coordinates here are doubled w-lattice coordinates. Thus fixed components attach to the UNION of all possible base z vertices at most once, proving z acyclicity at EVERY cut, not just an endpoint.','In w, the collector and connector are fully charged initial resources forming one tree with the path. Each straight/first-corner arm joins the active root to the same archive, while the second corner arm creates a fresh leaf at the deliberately skipped tip. No write touches a future old path vertex; the departing old edge is a bridge. At every L cut the exact active graph is the old suffix and all other black edges form one tree.','The physical predecessor L is explicitly realized but may erase a w cycle, and lies OUTSIDE the claimed ordinary epoch. The next RRRRL block lies after it. The all-q claim concerns the complete finite board, without omitted passive pieces or uncharged connectors.','n=8floor((q+1)^2/4),K=n+4(q-1),M=2n+4q-1, G=q-2, T=2n+q-2. Exactly q-1 new marked w vertices are created. Final marked components are the single archive and the isolated cursor, so G=A_w-1. The conservative half-sqrt(M)-4 bound holds for all q.','Epoch ledger: initial active edges partition into consumed old path P, retained old suffix F and pruned old Q. Passive inputs and all newly written lifetimes remain dormant outside F. Euler on permanently retained marked vertices gives DeltaC=A+B-D-G exactly. For n>=1 the last bridge deletion ensures at least two final marked components, hence G<=A+B+Centry-2. These are identities and a local inequality, not a monotone global progress resource.'],'scope':'All-q one-epoch construction; does not show repeatable concatenation, global cubic sharpness, a finite archive summary or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(dict(stats))
