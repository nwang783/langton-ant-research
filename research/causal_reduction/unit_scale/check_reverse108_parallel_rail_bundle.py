"""Bulk-only standard-rail bundle test for the one frozen prepared P108 word.
At most two pairwise disjoint11-normal writer bands can meet its11-normal
required-black span; all further rails can only pollute its white demands.
"""
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent
q=json.loads((P/'reverse108_two_rail_interfaces.json').read_text());v=json.loads((P/'reverse108_prepared_family.json').read_text());c=json.loads((P/'reverse108_prepared_control.json').read_text())
TB=set(map(tuple,q['first_writer_black']));TR=set(map(tuple,q['first_writer_read']));SWB=set(map(tuple,q['second_writer_black']));SWR=set(map(tuple,q['second_writer_read']));VB=set(map(tuple,c['input_black_classes']));VR={tuple(t['orbit'])for t in v['orbit_tables']}
def tr(a,n,p):return(a[0]+n,(a[1]+p)%2)
assert max(a[0]for a in VB)-min(a[0]for a in VB)==10
# Both writer read bands contain both parity classes at each of11 normals;
# black endpoints and no internal gap wider than1 force another11-normal
# initially-white read band to lie completely outside the earlier band.
for R,B in[(TR,TB),(SWR,SWB)]:
 lo=min(a[0]for a in R);hi=max(a[0]for a in R);assert hi-lo==10
 assert R=={(n,p)for n in range(lo,hi+1)for p in[0,1]}
 assert all((n,p)in B for n in[lo,hi]for p in[0,1])
 normals=sorted({a[0]for a in B});assert max(b-a for a,b in zip(normals,normals[1:]))<=2
records=[];single=[];matches=[]
for orientation in['SW','NE']:
 black=VB if orientation=='SW'else{(-a,p)for a,p in VB};read=VR if orientation=='SW'else{(-a,p)for a,p in VR}
 for wt,B in [('NE',TB),('SW',SWB)]:
  opts={(b[0]-a[0],(b[1]-a[1])%2)for b in B for a in black if(b[0]-a[0])%2==0};good=[]
  for n,p in opts:
   if all((tr(a,n,p)in B)==(a in black)for a in read):good.append((n,p))
  assert not good;single.append(dict(writer=wt,consumer=orientation,cases=len(opts)))
 placements={(t[0]-a[0],(t[1]-a[1])%2)for t in TB for a in black if(t[0]-a[0])%2==0}
 for m,p in sorted(placements):
  reqB={tr(a,m,p)for a in black};reqW={tr(a,m,p)for a in read-black};missing=reqB-TB
  if not missing:continue
  anchor=min(missing)
  for second,R,B in [('NE',TR,TB),('SW',SWR,SWB)]:
   opts={(anchor[0]-a[0],(anchor[1]-a[1])%2)for a in B if(anchor[0]-a[0])%2==0}
   for n,s in sorted(opts):
    if {tr(a,n,s)for a in R}&TB:continue
    full=TB|{tr(a,n,s)for a in B};badB=sorted(reqB-full);badW=sorted(reqW&full)
    row=dict(second_writer=second,consumer=orientation,consumer_offset=[m,p],writer_offset=[n,s],missing_black=badB,polluted_white=badW);records.append(row)
    if not badB and not badW:matches.append(row)
assert not matches
out=dict(scope=__doc__,single_checks=single,pair_cases=len(records),pair_matches=matches,records=records,required_black_normal_span=11,writer_read_normal_span=11,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'reverse108_parallel_rail_bundle.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='records'})
