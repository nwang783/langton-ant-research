"""Independent literal 124-case prefix exclusion, with complete conflicts."""
import ast,json,itertools,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
source=HERE/'search_completed_c_marker_reuse.py';tree=ast.parse(source.read_text())
W=next(ast.literal_eval(n.value)for n in tree.body if isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='WORDS'for t in n.targets))
allowed={'QCV':['','C','U','V'],'QCCV':[''],'BCV':['','C','U'],'BCCV':['','C']}
def verify(word):
 p=(0,0);h=0;last={};t=0
 for j,a in enumerate(word):
  for k,c in enumerate(W[a]):
   if p in last and last[p][0]==c:return dict(feasible=False,cell=p,old=last[p],new=(c,t,j,k))
   last[p]=(c,t,j,k);h=(h+(1 if c=='R'else -1))%4;d=((0,1),(1,0),(0,-1),(-1,0))[h];p=p[0]+d[0],p[1]+d[1];t+=1
 return dict(feasible=True)
rows=[]
for suffix,pres in allowed.items():
 for n in range(3):
  for ls in itertools.product(W,repeat=n):
   pre=''.join(ls);r=verify(pre+suffix);assert r['feasible']==(pre in pres)
   rows.append(dict(word=pre+suffix,**r))
assert len(rows)==124
out=dict(status='all literal cases matched; no feasible two-macro prefix',rows=rows,words_sha256=hashlib.sha256(json.dumps(W,sort_keys=True).encode()).hexdigest())
(HERE/'fold_turn_prefix_independent.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS',len(rows),sum(r['feasible']for r in rows))
