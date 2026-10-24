"""Four supplied H^m-router-H^infinity interfaces, uniformly m>=30.
Exact finite m30 all-future certificates plus explicit old-incoming-ray separation.
"""
from pathlib import Path
import json,sys,hashlib
from check_prepared1564_router_geometry import H,trace,infer
P=Path(__file__).resolve().parent;sys.path.insert(0,str(P.parents[1]/'computability'))
from periodic_tail_checker import State,first_mismatch
J=json.loads((P/'prepared4352_noncrossing_router_plan.json').read_text());V=((0,1),(1,0),(0,-1),(-1,0));out=[]
for r in J['routers']:
 h=r['source_lane'][2];d=(2,2)if h==1 else(-2,-2);q=30*d[0],30*d[1]
 base=infer(H*30,(0,0),h)['input'];extra={(q[0]+x,q[1]+y)for x,y in r['extra_black_relative_input']};assert not base&extra
 B=base|extra;p=(0,0);head=h
 for c in H*30+r['word']:
  assert(p in B)==(c=='L');B.symmetric_difference_update({p});head=(head+(1 if c=='R'else-1))%4;v=V[head];p=p[0]+v[0],p[1]+v[1]
 assert first_mismatch(State(frozenset(B),p,head),H)is None
 # Old incoming copies before the last30 have u farther than every router/cap cell.
 rr=list(trace(r['word'],(0,0),h))[:-1];pts=[a[1]for a in rr]+[tuple(z)for z in r['extra_black_relative_input']]
 hrs=list(trace(H,(0,0),h))[:-1];incoming_t={p[0]-p[1]for _,p,hh,c in hrs}
 oq=tuple(r['endpoint'][0]);oh=r['endpoint'][1];orr=list(trace(H,oq,oh))[:-1];outgoing_t={p[0]-p[1]for _,p,hh,c in orr};assert not incoming_t&outgoing_t
 umin=min(sum(p)for p in pts);umax=max(sum(p)for p in pts)
 if h==1:
  old_bound=max(sum(p)for _,p,hh,c in hrs)-4*31;assert old_bound<umin
 else:
  old_bound=min(sum(p)for _,p,hh,c in hrs)+4*31;assert old_bound>umax
 out.append({'router':r['index'],'status':'exact H30-router-H-infinity PASS','incoming_min_periods':30,
 'initial_mass':len(base|extra),'extra_mass':len(extra),'router_and_cap_u_bounds':[umin,umax],
 'strict_older_incoming_u_bound':old_bound,'incoming_t_bounds':[min(incoming_t),max(incoming_t)],
 'outgoing_t_bounds':[min(outgoing_t),max(outgoing_t)],'all_future_tail':True})
result={'scope':__doc__,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'plan_sha256':hashlib.sha256((P/'prepared4352_noncrossing_router_plan.json').read_bytes()).hexdigest(),'routers':out}
(P/'prepared4352_four_local_router_certificates.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
