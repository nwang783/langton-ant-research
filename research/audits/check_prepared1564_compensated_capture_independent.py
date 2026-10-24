"""Independent complete finite compensated-route control, including unused-cap removal."""
from pathlib import Path
from collections import defaultdict
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];R=ROOT/'nonlinear_global_budget_2026-10-23';U=ROOT/'causal_reduction/unit_scale'
S=SELF.with_name('check_changed_endpoint_catalog_independent.py');ns={'__file__':str(S)};exec(compile(S.read_text().split('results=[];nchecks=')[0],str(S),'exec'),ns)
rr,C=ns['make_changed']((-12,0));rr,pp,hh,tau,phi=ns['incoming'](rr,C,(26,0));rb=next(r for r in ns['original']['results']if r['channel']==[26,0]);assert rb['entry']==1144
_,_,_,wb=ns['replay'](rr,set(C),pp,hh,1144)
A=json.loads((U/'prepared1564_compensated_crossing.json').read_text());seed=set(map(tuple,A['seed']));unused=set(map(tuple,A['routers'][2]['extra']));assert len(seed)==88 and len(unused)==23 and unused<=seed
H=ns['H'];V=((0,1),(1,0),(0,-1),(-1,0));B=set(seed);p=(-15,10);h=3;history=[];visited=set();snaps={};times={e['time']for e in A['events']}|{239522}
for t in range(A['end_time']+1):
 if t in times:snaps[t]=(set(B),p,h)
 if t==A['end_time']:break
 visited.add(p);c='L'if p in B else'R';history.append(c);B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1])
assert B==set(map(tuple,A['black']))and [list(p),h]==A['end_pose'];assert not visited&unused
for e in A['events']:
 b,q,g=snaps[e['time']];assert[list(q),g]==e['pose']
 if 'mass'in e:assert len(b)==e['mass']
assert ''.join(history[238277:239421])==wb
assert ''.join(history[239421:239522])==rb['tail_word'][:101]
assert snaps[239454][1:]==snaps[239522][1:]==((-188,-209),1)
assert ''.join(history[239522:239626])==H and ''.join(history[239454:239558])!=H
# The claimed complete local routers really occur in this joint history.
router_matches=[]
for t,i in [(93794,0),(183006,1)]:
 ww=A['routers'][i]['word'];hits=[s for s in range(t,t+105)if ''.join(history[s:s+len(ww)])==ww];assert hits==[t+68];router_matches.append(dict(first_pose_visit=t,actual_word_start=t+68))
# Reuse only our independently reviewed generic finite-board tail arithmetic.
S=SELF.with_name('check_prepared1564_connected_capture_independent.py');src=S.read_text();piece=src[src.index('def periodic('):src.index('reports=[]')];exec(compile(piece,str(S),'exec'))
w=A['events'][-1]['word'];assert w in {H[i:]+H[:i]for i in range(104)}
first,d,groups,checks=periodic(B,p,h,w);assert first is None and d==(2,2)
reduced=B-unused;assert periodic(reduced,p,h,w)[0]is None
# Every unused original black is also absent from EVERY future read, not just the sampled past.
q=p;g=h;raw=[]
for c in w:
 raw.append(q);g=(g+(1 if c=='R'else-1))%4;v=V[g];q=(q[0]+v[0],q[1]+v[1])
for z in unused:
 assert not any(z[0]-q[0]==z[1]-q[1]and(z[0]-q[0])%2==0 and z[0]>=q[0]for q in raw)
phase=next(i for i in range(104)if w==H[i:]+H[:i]);delta=(-phase)%104;q=p;g=h
for c in w[:delta]:g=(g+(1 if c=='R'else-1))%4;v=V[g];q=(q[0]+v[0],q[1]+v[1])
assert(q,g)==((412,363),1)
# Independent second literal run from the65-cell seed, not just an inferred prefix.
bb=seed-unused;q=(-15,10);g=3
for t,c in enumerate(history):
 assert ('L'if q in bb else'R')==c;bb.symmetric_difference_update({q});g=(g+(1 if c=='R'else-1))%4;v=V[g];q=(q[0]+v[0],q[1]+v[1])
assert(bb,q,g)==(reduced,p,h)
controls=0
for a in groups:
 z=(a[0]+1000000*d[0],a[1]+1000000*d[1]);assert periodic(reduced^{z},p,h,w)[0]is not None;controls+=1
out=dict(status='PASS independent connected65-cell compensated A-to-B response and complete NE104 capture',source_sha256=hashlib.sha256((U/'prepared1564_compensated_crossing.json').read_bytes()).hexdigest(),note_sha256=hashlib.sha256((U/'prepared1564_connected_routing_status.md').read_bytes()).hexdigest(),router_phase_corrections=router_matches,original_mass=88,unused_removable_cells=23,reduced_seed=sorted(seed-unused),reduced_initial_mass=65,literal_updates_each=277056,B_contact=238277,B_response_length=1144,B_response_end=239421,false_phase0_pose_visit=239454,true_phase0=239522,capture_pose=A['end_pose'],capture_drift=d,capture_mass_88=len(B),capture_mass_65=len(reduced),future_orbits=len(groups),future_critical_levels=checks,far_flip_rejections=controls,next_canonical_phase0=dict(time=277056+delta,pose=[[412,363],1]),scope='One supplied finite seed actually connects the two reactions then captures standard NE104. No all-n route, third reaction, or finite preparation of a nonstandard wave is inferred.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='reduced_seed'})
