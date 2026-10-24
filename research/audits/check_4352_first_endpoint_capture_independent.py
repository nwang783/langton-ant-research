"""Actual original394-cell N1 control, with full finite-board tail thresholds."""
from pathlib import Path
from collections import defaultdict
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];U=ROOT/'causal_reduction/unit_scale';R=ROOT/'nonlinear_global_budget_2026-10-23';V=((0,1),(1,0),(0,-1),(-1,0))
M=json.loads((U/'prepared4352_uniform_support_manifest.json').read_text());E=json.loads((U/'prepared4352_first_finite_endpoint.json').read_text());A=json.loads((U/'prepared4352_first_endpoint_capture.json').read_text());H=json.loads((ROOT/'deliverables/constant_184_capturing_family/family_data.json').read_text())['standard_word'];W=json.loads((R/'second_prepared_wave_certificate.json').read_text())['word']
seed={(sum(x),sum(y))for x,y in M['seed_families']};assert len(seed)==394;p=(139,114);h=3;B=set(seed);history=[];first={};snap={};times={E['time'],A['capture_time'],*[e['time']for e in A['events']]}
for t in range(A['capture_time']+1):
 if t in times:snap[t]=set(B),p,h
 if t==A['capture_time']:break
 c='L'if p in B else'R';first.setdefault(p,t);history.append(c);B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;v=V[h];p=p[0]+v[0],p[1]+v[1]
entry=178202;failure=197941;offset=failure-entry;assert offset==19739 and divmod(offset,4352)==(4,2331)
assert ''.join(history[entry:failure])==''.join(W[i%4352]for i in range(offset))and history[failure]=='R'and W[offset%4352]=='L'
eb,ep,eh=snap[failure];assert(ep,eh)==((139,117),2)and ep not in seed and first[ep]==failure
assert eb==set(map(tuple,E['field_before_contact']))and len(eb)==21393
assert ''.join(history[failure:])==A['continuation_word']and[p,h]==[tuple(A['capture_pose'][0]),A['capture_pose'][1]]and len(B)==27571
hashfield=lambda b:hashlib.sha256(json.dumps(sorted(b),separators=(',',':')).encode()).hexdigest();assert hashfield(B)==A['final_field_sha256']
s=SELF.with_name('check_prepared1564_connected_capture_independent.py').read_text();exec(compile(s[s.index('def periodic('):s.index('reports=[]')],str(SELF),'exec'))
reports=[]
for e in A['events']:
 b,q,g=snap[e['time']];assert[list(q),g]==e['pose']and len(b)==e['mass'];w=e['word'];assert w in{H[i:]+H[:i]for i in range(104)}
 mismatch,d,groups,n=periodic(b,q,g,w);assert mismatch==e['next_mismatch']
 if mismatch is not None:
  assert ''.join(history[e['time']:e['time']+mismatch])==''.join(w[i%104]for i in range(mismatch))and history[e['time']+mismatch]!=w[mismatch%104]
 reports.append(dict(time=e['time'],pose=e['pose'],mass=len(b),next_mismatch=mismatch,drift=d,orbits=len(groups),critical_tests=n))
w=A['capture_word'];mismatch,d,groups,n=periodic(B,p,h,w);assert mismatch is None;flips=0
for a in groups:
 z=a[0]+1000000*d[0],a[1]+1000000*d[1];assert periodic(B^{z},p,h,w)[0]is not None;flips+=1
allowed={(H*2)[i:i+10]for i in range(104)};stream='LRLRRRRLLL'+''.join(history)+w[:10];count=sum(stream[i:i+10]not in allowed and stream[i+1:i+11]not in allowed for i in range(len(history)+10))
phase=next(i for i in range(104)if w==H[i:]+H[:i]);advance=(-phase)%104;q=p;g=h
for c in w[:advance]:g=(g+(1 if c=='R'else-1))%4;v=V[g];q=q[0]+v[0],q[1]+v[1]
out=dict(status='PASS original394-cell N1 finite endpoint and complete all-future standard tail',source_sha256=hashlib.sha256((U/'prepared4352_first_endpoint_capture.json').read_bytes()).hexdigest(),initial_mass=394,literal_reads=len(history),first_missing_fuel=dict(time=failure,offset=offset,phase=2331,pose=[[139,117],2],wanted='L',actual='R',previous_read=None),events=reports,capture_pose=[p,h],capture_mass=len(B),final_field_sha256=hashfield(B),total_future_K=count,far_flip_rejections=flips,next_canonical_phase0=dict(time=len(history)+advance,pose=[q,g]),scope='Only N1,R252 original finite board. Four temporary highways retain exact next collisions. No family-wide capture, infinite finite-board4352 or renewal theorem.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
