"""All-index RRLL temporal-relay identity controls, not front realizations.
The arbitrary translate periods below test interval algebra ONLY.
"""
from pathlib import Path
import json
lib={};exec(Path(__file__).with_name('check_open_flat_RRLL_strip_family.py').read_text().split('rows=[make(k)')[0],lib)
make=lib['make'];rows=[]
for k in[1,2,3,7]:
 z=make(k);T={tuple([tuple(p),r]):b['start_time']+i for b in z['blocks']for i,(p,r)in enumerate(b['events'])}
 a=lambda j:(2*j,0);b=lambda j:(2*j+1,0);u=lambda j:(2*j,-1);v=lambda j:(2*j+1,-1)
 it=[(T[p,1],T[p,3])for j in range(k)for p in[a(j),b(j)]]
 U=T[b(k-1),1],T[a(0),3]
 edge=[]
 for j in range(k):
  assert T[b(j),3]==T[a(j),1]+1
  edge.append((T[a(j),1],T[b(j),3]))
  if j:
   seq=[(a(j),2),(b(j-1),1),(v(j-1),3),(u(j),3),(a(j),3),(b(j-1),2)]
   ts=[T[e]for e in seq];assert ts==list(range(ts[0],ts[0]+6))
   edge.extend((ts[q],ts[q+1])for q in[1,2,3])
 assert len(edge)==4*k-3 and sum(y-x for x,y in it)==U[1]-U[0]+4*k-3
 for q in range(U[0]-2,U[1]+2):
  t=q+.5
  c=lambda xs:sum(x<=t<y for x,y in xs)
  assert c(it)==c([U])+c(edge)
  assert c(it)<=2
 def covers(x,y,t,P):return max(0,int((t-x)//P-((t-y)//P+1)+1))
 for P in[19,38]:
  for q in range(P):
   t=q+.5;c=lambda xs:sum(covers(x,y,t,P)for x,y in xs)
   assert c(it)==c([U])+c(edge)
 rows.append(dict(k=k,flat_intervals=it,effective_interval=U,selected_internal_edges=edge,all_physical_and_translated_equalities=True))
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,rows=rows,proof='All k follows from the exact adjacent-rank relay, not these four finite controls.'),indent=2)+'\n')
print('PASS all-index relay controls',[(r['k'],len(r['selected_internal_edges']))for r in rows])
