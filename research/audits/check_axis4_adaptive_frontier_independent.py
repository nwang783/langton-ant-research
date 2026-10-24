"""Complete independent adaptive-clock/first-return axis-four frontier replay.
Unpruned local histories are joined by independently computed exact ports.
Clock projection uses infinitesimal Bellman-Ford, not producer closure.
"""
from pathlib import Path
from itertools import product
from collections import Counter,deque
from functools import lru_cache
import ast,json,sys,time,hashlib
B=Path('/workspace/shared/langton');P=B/'periodic_classification_new/axis4_first_return_adaptive_real_w2_cap5_N16_S64_M128_mod2.certificate.json';J=json.loads(P.read_text());par=J['parameters'];start=time.monotonic();dirs=(1j,1,-1j,-1);D=dirs;INF=10**9;N=4;MOD=par['modulus'];BOUND=par['bound'];SCALE=par['clock_scale'];CAP=par['cap'];NMIN=par['minimum_period'];TCAP=par['read_counter_cap'];assert CAP==5 and SCALE==TCAP==64 and NMIN==16 and BOUND==128 and MOD==2
# Independent matching / shortest-path routines previously replayed completely.
src=B/'audits/check_normalized_real_zones_independent.py';tree=ast.parse(src.read_text());chosen=[n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name in('outheading','successors','zone')];text=ast.unparse(ast.Module(body=chosen,type_ignores=[])).replace('1 - SCALE * w','UPPER - SCALE * w').replace('key = (old, new, paths, flat)','key = (old, new, paths, flat, UPPER)');exec(compile(text,str(src),'exec'))
src=B/'audits/check_first_return_windows_independent.py';tree=ast.parse(src.read_text());fun=next(n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name=='ref');exec(compile(ast.Module(body=[fun],type_ignores=[]),str(src),'exec'))
horizontal=[h for n in range(6)for h in product((1,-1),repeat=n)];vertical=[h for n in range(6)for h in product((1j,-1j),repeat=n)];vgroups={}
for h in vertical:
 c=Counter(outheading(x,j)for j,x in enumerate(h));vgroups.setdefault((c[1],c[-1]),[]).append(h)
raw0=[]
for a,c in product(horizontal,repeat=2):
 ai,ci=Counter(a),Counter(c)
 for b in vgroups.get((ci[1],ai[-1]),[]):
  for d in vgroups.get((ai[1],ci[-1]),[]):raw0.append((a,b,c,d))
assert len(set(raw0))==len(raw0);raw=[raw0,[r[1:]+r[:1]for r in raw0]]
certrows=[[tuple(tuple(dirs[d]for d in c['h'])for c in row)for row in hs]for hs in J['histories']]
for p in(0,1):assert set(raw[p])==set(certrows[p])and len(raw[p])==len(certrows[p])
ports={}
for p in(0,1):
 for row in raw[p]:ports[p,row]=tuple((Counter(h),Counter(outheading(x,j)for j,x in enumerate(h)))for h in row)
adj={}
for p in(0,1):
 ix={}
 for row in raw[1-p]:
  v=ports[1-p,row];sig=tuple(z[0][1j]for z in v)+tuple(z[1][-1j]for z in v);ix.setdefault(sig,[]).append(row)
 for row in raw[p]:
  v=ports[p,row];sig=tuple(z[1][1j]for z in v)+tuple(z[0][-1j]for z in v);adj[p,row]=ix.get(sig,[])
print('independent exact rows',list(map(len,raw)),'seconds',time.monotonic()-start,flush=True)
def normalize(s):
 p,i,T,paths,flat=s;return(p,certrows[p][i],T,tuple((tuple(a),tuple(b),w)for a,b,w in paths),tuple(None if x==INF else x for x in flat))
known={normalize(s):i for i,s in enumerate(J['states'])};assert len(known)==len(J['states']);zero=(0,((),)*4,0,(),());assert known[zero]==0
@lru_cache(maxsize=300000)
def bad(p,old,new):
 hs=tuple(tuple(tuple(dirs.index(h)for h in col)for col in row)for row in(old,new));return ref(hs,4,0,p)
zonecache={};maximum_nodes=closurecalls=0;seen={zero};todo=deque([zero]);edges=set();attempts=rejects=0;done=0;last=time.monotonic()
while todo:
 state=todo.popleft();p,old,T,paths,flat=state
 if len(zonecache)>50000:zonecache.clear()
 for new in adj[p,old]:
  attempts+=1
  if bad(p,old,new):rejects+=1;continue
  TT=min(TCAP,T+sum(map(len,new)));lower=max(NMIN,TT);UPPER=(SCALE+lower-1)//lower
  for np,nf in zone(old,new,paths,flat):
   target=(1-p,new,TT,np,nf);assert target in known,('UNCOVERED',target)
   edges.add((known[state],known[target],new))
   if target not in seen:seen.add(target);todo.append(target)
 done+=1
 if time.monotonic()-last>20:
  print('processed',done,'seen',len(seen),'edges',len(edges),'attempts',attempts,'closures',closurecalls,'seconds',time.monotonic()-start,flush=True);last=time.monotonic()
assert seen==set(known),(len(seen),len(known))
expected={(u,v,certrows[1-J['states'][u][0]][j])for u,v,j in J['edges']};assert edges==expected
out=dict(status='PASS complete independent adaptive-clock and first-return graph closure',full_drift=[4,0],cap=5,minimum_period=NMIN,scale=SCALE,read_counter_cap=TCAP,bound=BOUND,modulus=MOD,unpruned_local_histories=len(horizontal)+len(vertical),independently_joined_rows=list(map(len,raw)),states=len(seen),edges=len(edges),attempts=attempts,proper_path_rejections=rejects,shortest_path_closures=closurecalls,largest_transition_nodes=maximum_nodes,seconds=time.monotonic()-start,certificate_sha256=hashlib.sha256(P.read_bytes()).hexdigest(),scope='Full positive-axis-four drift and quarter rotations, cap five, every period and strip width. No general multiplicity or global capture claim.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
