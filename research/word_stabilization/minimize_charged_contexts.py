import json,random,sys
from pathlib import Path
p=sys.argv[1];r=json.load(open(p+'_patch2_pruned_graph.json'));g=json.load(open(p+'_grammar.json'));n=len(g['macros']);charged=set(r['charged']);E=g['pairs']
def good(removed):
 A=[[]for _ in range(n)];I=[0]*n
 for a,b in E:
  if a not in removed and b not in removed:A[a].append(b)
 # Remove vertices not on any cycle by full SCC, because ordinary topological deletion retains cycle-downstream vertices.
 idx=[-1]*n;low=[0]*n;stk=[];on=set();count=0;ok=True
 def dfs(a):
  nonlocal count,ok
  idx[a]=low[a]=count;count+=1;stk.append(a);on.add(a)
  for b in A[a]:
   if idx[b]<0:dfs(b);low[a]=min(low[a],low[b])
   elif b in on:low[a]=min(low[a],idx[b])
  if low[a]==idx[a]:
   s=[]
   while True:
    b=stk.pop();on.remove(b);s.append(b)
    if b==a:break
   if len(s)>1 or a in A[a]:
    if any(b in charged for b in s):ok=False
 for a in range(n):
  if a not in removed and idx[a]<0:dfs(a)
 return ok
best=charged
rng=random.Random(20261022)
for trial in range(120):
 rem=set(charged);order=sorted(charged);rng.shuffle(order)
 for a in order:
  rem.remove(a)
  if not good(rem):rem.add(a)
 if len(rem)<len(best):best=rem;print('best',len(best),sorted(best),flush=True)
assert good(best)
Path(p+'_selected_charges.json').write_text(json.dumps({'selected':sorted(best),'all_charged':sorted(charged),'scope':'Removing selected charged contexts leaves every recurrent vertex among the originally uncharged contexts.'},indent=2))
