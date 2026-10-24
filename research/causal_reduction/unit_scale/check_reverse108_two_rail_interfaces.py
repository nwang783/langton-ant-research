"""Exact bulk-only attempt to fund P108 with TWO white-written parallel rails.
First rail H NE, second H SW; second's complete read strip must start white.
No cap or finite producer itinerary is inferred from a bulk match.
"""
from pathlib import Path
import json,collections,hashlib
from probe_perpendicular_highway_wake import H
from certify_highway_wake_reflector import trace
P=Path(__file__).resolve().parent;z=json.loads((P/'reverse108_prepared_control.json').read_text());word=z['word']
def key(q):return(q[0]-q[1],q[0]%2)
def prof(w,start,h):
 r,e,g=trace(w,start,h);d=(e[0]-start[0],e[1]-start[1]);assert d in[(2,2),(-2,-2)]
 a=collections.defaultdict(list)
 for t,(q,hh,c)in enumerate(r):a[key(q)].append((t-(1 if d[0]>0 else-1)*len(w)*(q[0]//2),c))
 for l in a.values():l.sort();assert all(x[1]!=y[1]for x,y in zip(l,l[1:]))
 return a
T=prof(H,(0,0),1);assert all(l[0][1]=='R'for l in T.values());TB={a for a,l in T.items()if len(l)%2}
U=prof(H,(0,0),3);assert all(l[0][1]=='R'for l in U.values());UB={a for a,l in U.items()if len(l)%2}
def tr(a,n,p):return(a[0]+n,(a[1]+p)%2)
results=[];matches=[];single_checks=[]
for orient,start,h in[('SW',(0,6),3),('NE',(0,-6),1)]:
 V=prof(word,start,h);VB={a for a,l in V.items()if l[0][1]=='L'}
 for writer,B in [('NE',TB),('SW',UB)]:
  tests={(b[0]-v[0],(b[1]-v[1])%2)for b in B for v in VB if(b[0]-v[0])%2==0};good=[]
  for n,q in tests:
   if all((tr(a,n,q)in B)==(l[0][1]=='L')for a,l in V.items()):good.append((n,q))
  assert not good
  single_checks.append(dict(writer=writer,consumer=orient,anchored_placements=len(tests),matches=good))
 placements={(t[0]-v[0],(t[1]-v[1])%2)for t in TB for v in VB if(t[0]-v[0])%2==0}
 for m,p in sorted(placements):
  target={tr(a,m,p):l[0][1]for a,l in V.items()};need={a for a,c in target.items()if c=='L'};missing=need-TB
  if not missing:continue # Adding a disjoint rail cannot repair any existing white-demand violation.
  anchor=min(missing);uplacements={(anchor[0]-u[0],(anchor[1]-u[1])%2)for u in UB if(anchor[0]-u[0])%2==0}
  for n,q in sorted(uplacements):
   readU={tr(a,n,q)for a in U}
   if readU&TB:continue
   bulk=TB|{tr(a,n,q)for a in UB}
   badB=sorted(a for a,c in target.items()if c=='L'and a not in bulk);badW=sorted(a for a,c in target.items()if c=='R'and a in bulk)
   r=dict(consumer_orientation=orient,consumer_translation_normal=m,consumer_x_parity=p,second_writer_translation_normal=n,second_writer_x_parity=q,missing_black=badB,polluted_white=badW)
   results.append(r)
   if not badB and not badW:matches.append(r)
out=dict(scope=__doc__,first_writer_read=sorted(T),first_writer_black=sorted(TB),second_writer_read=sorted(U),second_writer_black=sorted(UB),feasible_writer_pair_candidate_interfaces=len(results),matches=matches,records=results,single_rail_checks=single_checks,completeness='Any valid consumer must use a black class from rail1 and a missing black class supplied by rail2; anchors generate every relative normal shift and x parity. If all black demands came from one rail, its directly checked single-rail white-demand conflict cannot be repaired by a disjoint added black rail.',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'reverse108_two_rail_interfaces.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in('records','first_writer_read','first_writer_black','second_writer_read','second_writer_black')})
