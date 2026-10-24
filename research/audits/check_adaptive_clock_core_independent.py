"""Independent infinitesimal Bellman-Ford controls for adaptive clock steps.
No new complete frontier graph is claimed. Physical splicing is reconstructed.
"""
from pathlib import Path
from collections import Counter
import ast,sys,json,random,hashlib
B=Path('/workspace/shared/langton');H=B/'periodic_classification_new';sys.path.insert(0,str(H))
import probe_adaptive_real_zone_core as A
from probe_axis_zone_core import splice
J=json.loads((H/'axis4_normalized_real_cap4_N8_M16_mod2.certificate.json').read_text())
# Read independently written exact physical matching / Bellman-Ford functions.
source=(B/'audits/check_normalized_real_zones_independent.py').read_text();tree=ast.parse(source)
chosen=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('outheading','successors','zone')]
text=ast.unparse(ast.Module(body=chosen,type_ignores=[]));text=text.replace('1 - SCALE * w','UPPER - SCALE * w').replace("assert not terminal, ('POTENTIAL WHOLE FRONT', key)","\n    if terminal:\n        zonecache[key]='POTENTIAL_COMPLETE_FRONT'\n        return 'POTENTIAL_COMPLETE_FRONT'")
N=4;MOD=2;dirs=(1j,1,-1j,-1);INF=10**9;zonecache={};maximum_nodes=0;closurecalls=0
exec(compile(text,'independent_Bellman_Ford','exec'))
raw=[[tuple(tuple(dirs[x]for x in cell['h'])for cell in row)for row in rows]for rows in J['histories']]
ports={}
for p in (0,1):
 for i,row in enumerate(raw[p]):ports[p,i]=tuple((Counter(h),Counter(outheading(x,j) for j,x in enumerate(h))) for h in row)
ix={}
for p in (0,1):
 for j,row in enumerate(raw[p]):
  v=ports[p,j];sig=tuple(a[0][1j] for a in v)+tuple(a[1][-1j] for a in v);ix.setdefault((p,sig),[]).append(j)
rng=random.Random(290731);checks=0;accepted=rejected=0
for _ in range(1500):
 state=J['states'][rng.randrange(len(J['states']))];p,i,path,flat=state;v=ports[p,i];sig=tuple(a[1][1j]for a in v)+tuple(a[0][-1j]for a in v);choices=ix.get((1-p,sig),[])
 if not choices:continue
 j=rng.choice(choices);old,new=raw[p][i],raw[1-p][j];paths=tuple((tuple(a),tuple(b),w)for a,b,w in path);f=tuple(None if x==INF else x for x in flat)
 SCALE=rng.choice((8,16,64,72));UPPER=rng.choice((1,2,3,4));BOUND=rng.choice((16,32,128));zonecache={}
 want=zone(old,new,paths,f)
 oh=[tuple(c['h'])for c in J['histories'][p][i]];nh=[tuple(c['h'])for c in J['histories'][1-p][j]]
 actual,reason=A.transitions(paths,tuple(flat),oh,nh,p,splice,MOD,BOUND,SCALE,UPPER)
 if actual==['POTENTIAL_COMPLETE_FRONT']:got='POTENTIAL_COMPLETE_FRONT'
 else:got={(a,tuple(None if b==INF else b for b in mat))for a,mat in actual}
 assert got==want,(state,j,SCALE,UPPER,BOUND,got,want)
 accepted+=bool(actual);rejected+=not actual;checks+=1
# Independent lower-bound arithmetic, including saturation and period>S.
arith=0
for S in (16,64,72):
 for N0 in (8,16):
  for T in range(150):
   Tcap=min(T,S);lower=max(N0,Tcap);U=(S+lower-1)//lower
   for P in (max(T,N0),max(T,N0)+1,1000):
    if P<T or P<N0:continue
    assert S<=U*P;arith+=1
out=dict(status='PASS independent adaptive-step physical splicing and strict shortest-path comparison',transition_controls=checks,accepted=accepted,rejected=rejected,clock_lower_bound_controls=arith,maximum_nodes=maximum_nodes,shortest_path_closures=closurecalls,sha256=hashlib.sha256((H/'probe_adaptive_real_zone_core.py').read_bytes()).hexdigest(),scope='Core implementation controls only; no complete adaptive frontier graph exclusion.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
