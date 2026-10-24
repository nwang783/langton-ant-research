"""Independent unpruned upper histories, physical chronology and affine cycles."""
from pathlib import Path
from itertools import product
from collections import Counter
import ast,json,hashlib,time
B=Path('/workspace/shared/langton');P=B/'periodic_classification_new/axis4_cap5_bottom_reduction.certificate.json';J=json.loads(P.read_text());start=time.monotonic();D=(1j,1,-1j,-1)
src=B/'audits/check_first_return_windows_independent.py';tree=ast.parse(src.read_text());fun=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='ref');exec(compile(ast.Module(body=[fun],type_ignores=[]),str(src),'exec'))
profiles=[(m,)*4 for m in range(2,6)]+[(2,2,3,3),(4,4,5,5),(1,2,2,1),(3,4,4,3)]
assert [tuple(p['bottom'])for p in J['profiles']]==profiles
results=[];totalraw=0;allcandidates=0;cyclecount=0
for ns,cert in zip(profiles,J['profiles']):
 bottom=tuple(tuple((3 if j%2==0 else 1)if c%2==0 else 2 for j in range(m))for c,m in enumerate(ns));domains=[]
 for c,m in enumerate(ns):
  options=[]
  for length in range(6):
   for h in product((0,2)if c%2==0 else(1,3),repeat=length):
    ih=Counter(h);oh=Counter((d+(1 if j%2==0 else-1))%4 for j,d in enumerate(h))
    if (ih[0]if c%2==0 else oh[2])==m:options.append((h,ih,oh))
  domains.append(options)
 expected={tuple(tuple(c)for c in row['upper']):row for row in cert['cases']};assert len(expected)==len(cert['cases']);seen=set();localraw=0;proper=0;cycles=0
 for row in product(*domains):
  allcandidates+=1
  if any(row[c][2][d]!=row[(c+(1 if d==1 else-1))%4][1][d]for c in range(4)for d in(1,3)):continue
  hs=(bottom,tuple(c[0]for c in row));key=hs[1];assert key in expected;seen.add(key);item=expected[key];localraw+=1;bad=ref(hs,4,0)
  if item['kind']=='proper_path':assert bad;proper+=1;continue
  assert item['kind']=='affine_negative_cycle' and not bad
  edges=set();events=[(y,x,j)for y,hrow in enumerate(hs)for x,h in enumerate(hrow)for j in range(len(h))]
  for y,x,j in events:
   if j:edges.add(((y,x,j),(y,x,j-1),0,-4,'rank'))
   d=D[hs[y][x][j]]*(-1j if j%2==0 else 1j);xx=x+int(d.real);yy=y+int(d.imag)
   if not 0<=yy<2:continue
   ordn=sum(D[t]*(-1j if u%2==0 else 1j)==d for u,t in enumerate(hs[y][x][:j]));arr=[u for u,t in enumerate(hs[yy][xx%4])if D[t]==d];assert ordn<len(arr);v=(yy,xx%4,arr[ordn]);u=(y,x,j);w=xx//4
   edges.add((u,v,-w,1,'physical'));edges.add((v,u,w,-1,'physical_reverse'))
  cyc=[(tuple(e[0]),tuple(e[1]),*e[2:])for e in item['edges']];assert cyc and all(e in edges for e in cyc)
  assert all(cyc[i][0]==cyc[(i+1)%len(cyc)][1]for i in range(len(cyc)))
  a=sum(e[2]for e in cyc);b=sum(e[3]for e in cyc);assert a==item['slope']and b==item['intercept']and a<=0 and 16*a+b<0
  cycles+=1
 assert seen==set(expected)
 totalraw+=localraw;cyclecount+=cycles;results.append(dict(bottom=ns,raw_upper_histories=localraw,proper_path_rejections=proper,affine_cycles=cycles));print(results[-1],flush=True)
# All possible bottom counts via exact two horizontal matching equations.
allcounts=[]
for n in product(range(6),repeat=4):
 if not any(n):continue
 if all((n[2*i]+1)//2==(n[2*i+1]+1)//2 and n[2*i]//2==n[(2*i-1)%4]//2 for i in range(2)):allcounts.append(n)
normalized={min(n,n[2:]+n[:2])for n in allcounts};known={min(n,n[2:]+n[:2])for n in profiles+[(0,0,1,1),(1,1,1,1)]};assert normalized==known
out=dict(status='PASS complete independent local boundary enumeration and explicit all-P negative cycles',full_drift=[4,0],cap=5,minimum_period=16,unpruned_local_products=allcandidates,raw_upper_histories=totalraw,affine_cycles=cyclecount,profiles=results,remaining_bottom_profiles=[[0,0,1,1],[1,1,1,1]],seconds=time.monotonic()-start,certificate_sha256=hashlib.sha256(P.read_bytes()).hexdigest(),scope='Lowest active A-even row only, full positive axis-four and cap five. No upper width/period cap, no top-boundary or complete-front exclusion.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
