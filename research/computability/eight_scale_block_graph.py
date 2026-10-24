"""Necessary successive-scale block graph for eventual affine k8,a=2+2i.
Discovery SAT/UNSAT only, not an independently certified finite exclusion.
Vertices are normalized internally legal eight-turn diagonal-displacement words.
An edge U->V has a literal legal64-turn refinement of U starting with V,
with scale plus or minus(2+2i), allowing half-turn heading normalization.
"""
import sys,pathlib,json,re,time,collections
ROOT=pathlib.Path('/workspace/shared/langton');sys.path.insert(0,str(ROOT/'causal_reduction/morphic_candidates'))
from position_only_refinement import build,Z3,trace,seed,mul
from search_eight_phase_controllers import BY
HERE=pathlib.Path(__file__).resolve().parent
vertices=sorted(w for(h,x,y),ws in BY.items() if h==0 and abs(x)==abs(y)==2 for w in ws)

def lit(x):return f'v{x}' if x>0 else f'(not v{-x})'
def run():
 start=time.time();edges=[];unknown=[];calls=0
 for wi,U in enumerate(vertices):
  for a in ((2,2),(-2,-2)):
   names,clauses,options,cv=build(8,a,U,[])
   Z=Z3();Z.run('\n'.join(['(set-option :timeout 5000)']+[f'(declare-const v{i} Bool)' for i in range(1,len(names)+1)]+['(assert '+(lit(c[0]) if len(c)==1 else '(or '+' '.join(map(lit,c))+')')+')' for c in clauses]))
   for oi,o in enumerate(options[0]):
    if o['heading']!=0:continue
    V=o['word'];assert V in vertices
    status=Z.run(f'(push)\n(assert v{cv[0][oi]})\n(check-sat)').strip();calls+=1
    if status=='sat':
     model=Z.run('(get-value ('+' '.join(f'v{x}' for row in cv for x in row)+'))');true={int(x) for x in re.findall(r'\(v(\d+) true\)',model)}
     chosen=[]
     for opts,row in zip(options,cv):
      inds=[j for j,v in enumerate(row) if v in true];assert len(inds)==1;chosen.append(opts[inds[0]]['word'])
     W=''.join(chosen);assert W[:8]==V and seed(W) is not None
     fp=[(x,y) for x,y,h,c in trace(W)[0]]+[trace(W)[1][:2]];cp=[(x,y) for x,y,h,c in trace(U)[0]]+[trace(U)[1][:2]]
     assert all(fp[8*j]==mul(a,p) for j,p in enumerate(cp))
     edges.append(dict(source=U,target=V,scale=a,refinement=W,fuel=len(seed(W))))
    elif status!='unsat':unknown.append(dict(source=U,target=V,scale=a,status=status))
    Z.run('(pop)')
   Z.close()
  print(wi+1,'/',len(vertices),'edges',len(edges),'unknown',len(unknown),flush=True)
 adj={v:[] for v in vertices}
 for e in edges:adj[e['source']].append(e['target'])
 colors={};stack=[];cycles=[]
 def dfs(v):
  colors[v]=1;stack.append(v)
  for u in adj[v]:
   if colors.get(u)==1:cycles.append(stack[stack.index(u):]+[u])
   elif not colors.get(u):dfs(u)
  stack.pop();colors[v]=2
 for v in vertices:
  if not colors.get(v):dfs(v)
 out=dict(status='NECESSARY_GRAPH_ONLY',vertices=vertices,edges=edges,unknown=unknown,calls=calls,cycles=cycles,seconds=time.time()-start)
 (HERE/'eight_scale_block_graph.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k not in ('vertices','edges','unknown')},indent=2))
if __name__=='__main__':run()
