from pathlib import Path
import json,hashlib
from prune_two_original_inputs_v2 import prune2,comparison_certificate,first_omitted_hit,sparse_interior_radius_test
from check_return_permanent_output_debt import DXY
P=Path(__file__).parent
base=comparison_certificate({(0,0)},budget=200000)
candidates={(10000+i,10000-i)for i in range(8)};assert first_omitted_hit(base,candidates)is None
jobs=[('empty',set()),('one_hit_plus_unread',{(0,0)}|candidates),('two_black',{(0,0),(1,0)}),('three_black',{(0,0),(1,0),(0,1)}),('four_G',{(0,-1),(1,1),(1,3),(2,2)})]
# Actual current finite field, not just the initial tiny input.
d=json.loads((P/'MINIMAL_COHORT_RESTART_CHECKED.json').read_text());jobs.append(('defect14',set(map(tuple,d['initial_seed']))))
results=[]
for name,B in jobs:
 r=prune2(B,budget=200000);end=r['contacts'][-1]['time']+1 if r['contacts'] else 0
 actual=set(B);p=(0,0);h=0;read_orig=set();hits=[]
 for t in range(end):
  if p in B and p not in read_orig:read_orig.add(p);hits.append(dict(time=t,cell=p))
  old=p in actual
  if old:actual.remove(p);h=(h-1)%4
  else:actual.add(p);h=(h+1)%4
  p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
 assert hits==r['contacts'];r['name']=name;r['initial_black']=sorted(B);r['initial_pose']=[[0,0],0];results.append(r)
 print(name,r['kind'],r['contacts'],[z['certified_prefix']for z in r['comparisons']],flush=True)
# A direct force-BLACK first-hit equivalence regression, before any later divergence.
force=[]
for B,q in [(set(),(0,0)),({(0,0)},(1,0)),({(0,0)},(10000,10000))]:
 X=set(B);Y=set(B)|{q};px=py=(0,0);hx=hy=0;hit=None
 for t in range(20000):
  assert(px,hx)==(py,hy)
  if px==q:hit=t;break
  for board,which in [(X,0),(Y,1)]:
   pp,hh=(px,hx)if which==0 else(py,hy);old=pp in board
   if old:board.remove(pp);hh=(hh-1)%4
   else:board.add(pp);hh=(hh+1)%4
   pp=(pp[0]+DXY[hh][0],pp[1]+DXY[hh][1])
   if which==0:px,hx=pp,hh
   else:py,hy=pp,hh
 cert=comparison_certificate(B,budget=200000);exact=first_omitted_hit(cert,{q});assert exact is None if hit is None else exact[0]==hit
 force.append(dict(board=sorted(B),target=q,first_hit_in_checked_prefix=hit,checked_prefix=20000 if hit is None else hit,certified_first_hit=exact,comparison_tail_cut=cert['prefix_length']))
rad=[]
for B,R,answer in [({(0,0)}|candidates,0,True),({(0,0),(1,0),(0,1)},0,False),(candidates,0,True)]:
 r=sparse_interior_radius_test(B,R,budget=200000);assert r['rho_at_input_le_R']==answer;rad.append(dict(board=sorted(B),radius=R,result=r))
out=dict(sparse_interior_radius_controls=rad,status='AUTHOR restricted exact pruning interface; independent audit requested',scope='Total mathematical algorithm uses signed <=2-black theorem. Named executions each had200000 comparison-read budget; none exhausted. First3 original inputs only, no cohort resetting, no decision of full pruning/capture on three-input branch.',source_hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in ['TWO_BLACK_CANONICAL_COMPLETION_MANIFEST.json','blank_collision_operator.py','check_return_permanent_output_debt.py'] if (P/f).exists()},controls=results,force_black_regressions=force)
(P/'PRUNE_TWO_ORIGINAL_INPUTS_V2_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
