"""Independent physical-coordinate successor and first-return chronology controls."""
from pathlib import Path
from collections import Counter,defaultdict
import json,random,sys,hashlib
B=Path('/workspace/shared/langton');H=B/'periodic_classification_new';sys.path.insert(0,str(H))
import axis4_first_return_window as A
import general_first_return_window as G
from frontier_drift_geometry import Geometry
D=(1j,1,-1j,-1)
def ref(rows,a,b,p=0):
 events=[(y,x,j)for y,row in enumerate(rows)for x,h in enumerate(row)for j in range(len(h))];succ={}
 def pos(e):y,x,j=e;return complex(x,p+y+b*x//a)
 def out(e):y,x,j=e;return D[rows[y][x][j]]*(-1j if j%2==0 else 1j)
 for e in events:
  y,x,j=e;d=out(e);q=pos(e)+d;shift=int(q.real)//a;xx=int(q.real)-shift*a;yy=int(q.imag)-shift*b-b*xx//a-p
  if not 0<=yy<len(rows):continue
  rank=sum(D[t]*(-1j if u%2==0 else 1j)==d for u,t in enumerate(rows[y][x][:j]));arr=[u for u,t in enumerate(rows[yy][xx])if D[t]==d]
  if rank>=len(arr):raise AssertionError('unmatched test window')
  succ[e]=(yy,xx,arr[rank])
 for start in events:
  cur=start;q=pos(start);seen={start:(0,q)};steps=0;returned=False
  while cur in succ:
   q+=out(cur);cur=succ[cur];steps+=1
   if cur in seen:
    n,z=seen[cur];w=int((q-z).real)//a
    if steps-n!=len(events) or w!=1:return True
    break
   seen[cur]=(steps,q)
   if q==pos(start) and not returned:
    if cur[2]!=start[2]+1:return True
    returned=True
   if cur[:2]==start[:2]:
    w=int((q-pos(start)).real)//a
    if (cur[2]>start[2] and w>0) or (cur[2]<start[2] and w<=0):return True
 return False
# Random necessary-compatible windows, independent matching signatures.
J=json.loads((H/'axis4_normalized_real_cap4_N8_M16_mod2.certificate.json').read_text());rows=[[tuple(tuple(c['h'])for c in row)for row in hs]for hs in J['histories']]
ports={}
for p in(0,1):
 for i,row in enumerate(rows[p]):ports[p,i]=tuple((Counter(h),Counter((t+(1 if j%2==0 else -1))%4 for j,t in enumerate(h)))for h in row)
index={}
for p in(0,1):
 for i,row in enumerate(rows[p]):
  v=ports[p,i];sig=tuple(z[0][0]for z in v)+tuple(z[1][2]for z in v);index.setdefault((p,sig),[]).append(i)
rng=random.Random(231037);count=bad=0
for _ in range(4000):
 p=rng.randrange(2);i=rng.randrange(len(rows[p]));v=ports[p,i];sig=tuple(z[1][0]for z in v)+tuple(z[0][2]for z in v);choices=index.get((1-p,sig),[])
 if not choices:continue
 hs=[rows[p][i],rows[1-p][rng.choice(choices)]];expected=ref(hs,4,0,p);x=A.bad_window(hs);y=G.bad_window(hs,p,Geometry(4,0));assert bool(x)==bool(y)==expected;count+=1;bad+=expected
# Genuine white-front positive windows from direct complex standard-word traces.
word=(B/'word_stabilization/standard_word.txt').read_text().strip();positive=[]
for copies in (1,2,3):
 for clockwise in (0,1):
  a=2*copies;b=a if not clockwise else -a;period=104*copies;start=(-1+0j if not clockwise else 1j);h=(1j if not clockwise else 1+0j);q=start;hist=defaultdict(list)
  for t,c in enumerate(word*copies):
   k=int(q.real)//a;rep=q-k*complex(a,b);hist[rep].append((t-k*period,D.index(h),c));h*=(-1j if c=='R'else 1j);q+=h
  assert q==start+complex(a,b)
  low=min(int(z.imag)-b*int(z.real)//a for z in hist);high=max(int(z.imag)-b*int(z.real)//a for z in hist);rs=[]
  for t in range(low,high+1):
   row=[]
   for x in range(a):
    visits=sorted(hist[complex(x,t+b*x//a)]);assert all(c==('R'if j%2==0 else'L')for j,(_,h,c)in enumerate(visits));row.append(tuple(h for _,h,c in visits))
   rs.append(row)
  n=0
  for width in (2,3,4):
   for t in range(len(rs)-width+1):
    hs=rs[t:t+width];p=(low+t)%2;assert not ref(hs,a,b,p);assert G.bad_window(hs,p,Geometry(a,b))is None;n+=1
  positive.append(dict(period=period,drift=[a,b],windows=n))
out=dict(status='PASS independent exact-coordinate first-return controls',random_compatible_windows=count,correctly_rejected=bad,genuine_standard_controls=positive,scope='Necessary local chronology implementation only, not a new whole-front exclusion.',hashes={p:hashlib.sha256((H/p).read_bytes()).hexdigest()for p in('axis4_first_return_window.py','general_first_return_window.py')})
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
