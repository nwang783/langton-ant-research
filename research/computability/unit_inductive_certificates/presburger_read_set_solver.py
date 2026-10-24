"""Execute the exact Euler-count read-set construction using existing libisl.
This module does not infer first-read colors or decide unknown-seed existence.
"""
import pathlib,sys,json,time
HERE=pathlib.Path(__file__).parent
CORE=HERE.parents[1]/'sources/kehao95-core/defect_synthesis/verification/presburger_defects'
sys.path.insert(0,str(CORE))
from isl_exact import Context
from check_read_sets import typed,literal

def lin(terms):
 terms=[f'{a}*n{i}' for i,a in terms if a]
 return '+'.join(terms) if terms else '0'

def relation(ctx,vertices,edges,start):
 """Edges are (source,target,(dx,dy)); zero length is included exactly."""
 vertices=tuple(vertices);edges=sorted(set(edges));m=len(edges)
 out={v:[i for i,e in enumerate(edges) if e[0]==v] for v in vertices}
 inc={v:[i for i,e in enumerate(edges) if v in e[:2]] for v in vertices}
 bal={v:lin([(i,int(u==v)-int(w==v)) for i,(u,w,p) in enumerate(edges)]) for v in vertices}
 rank={v:f'h{i}' for i,v in enumerate(vertices)}
 clauses=[f'n{i}>=0' for i in range(m)]
 clauses += [f'0<={rank[v]}<={len(vertices)}' for v in vertices]+[f'{rank[start]}=0']
 clauses += [f'r={lin([(i,1) for i in range(m)])}',
  f'x={lin([(i,e[2][0]) for i,e in enumerate(edges)])}',
  f'y={lin([(i,e[2][1]) for i,e in enumerate(edges)])}']
 ends=[]
 for end in vertices:
  ends.append('('+' and '.join(f'{bal[v]}={int(v==start)-int(v==end)}' for v in vertices)+')')
 clauses.append('('+' or '.join(ends)+')')
 for v in vertices:
  if v==start:continue
  pieces=[f'{lin([(i,1) for i in inc[v]])}=0']
  for i in inc[v]:
   u,w,p=edges[i];other=w if u==v else u
   if other!=v:pieces.append(f'(n{i}>0 and {rank[other]}<{rank[v]})')
  clauses.append('('+' or '.join(pieces)+')')
 names=[f'n{i}' for i in range(m)]+list(rank.values())
 formula='{ [r,x,y] : exists ('+','.join(names)+' : '+' and '.join(clauses)+') }'
 return ctx.set(formula).coalesce(),formula

def main():
 start=time.monotonic();ctx=Context(max_operations=20000000);records=[]
 for name,images,roots in [('identity',['R','L']*4,[0,1]),('right_five',['RRRRR','LLLLL']*4,[0])]:
  phi=typed(images)
  for root in roots:
   reachable={root}
   while True:
    new=reachable|{t for s in reachable for t,p in phi[s]}
    if new==reachable:break
    reachable=new
   edges=[(s,t,p) for s in reachable for t,p in phi[s]]
   ctx.reset_operations();R,formula=relation(ctx,reachable,edges,root)
   if name=='identity':expected=ctx.set('{ [r,x,y] : r>=0 and x=0 and y=0 }')
   else:expected=ctx.set('{ [r,x,y] : (r=0 and x=0 and y=0) or (r>=1 and 0<=x<=1 and -1<=y<=0) }')
   assert R.is_equal(expected),(name,str(R));checks=0
   for depth in range(6):
    reads=literal(images,root,depth)[0]
    for x in range(-3,4):
     for y in range(-3,4):
      point=ctx.set(f'{{ [r,x,y] : r={depth} and x={x} and y={y} }}')
      assert (not R.intersect(point).is_empty())==((x,y) in reads);checks+=1
   records.append(dict(name=name,root=root,vertices=len(reachable),edges=len(set(edges)),formula=formula,
    exact_relation=str(R),literal_checks=checks))
 out=dict(libisl_version=ctx.version,records=records,total_literal_checks=sum(r['literal_checks'] for r in records),
  scope='Exact all-depth read-set compiler controls only; chronology and seed existence not inferred.',seconds=time.monotonic()-start)
 (HERE/'presburger_read_set_solver.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
