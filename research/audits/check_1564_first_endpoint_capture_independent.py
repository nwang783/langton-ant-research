"""Whole-seed replay and complete finite-board tail proof for R100,N3 only."""
from pathlib import Path
from collections import defaultdict
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];U=ROOT/'causal_reduction/unit_scale';R=ROOT/'nonlinear_global_budget_2026-10-23'
J=json.loads((U/'prepared1564_noncrossing_R100_N3.json').read_text());E=json.loads((U/'prepared1564_first_finite_endpoint.json').read_text());A=json.loads((U/'prepared1564_first_endpoint_capture.json').read_text());H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];W=json.loads((R/'prepared_travelling_wave_certificate.json').read_text())['word']
V=((0,1),(1,0),(0,-1),(-1,0));seed=set(map(tuple,J['initial_seed']));B=set(seed);p=(33,70);h=3;history=[];visited=set();snapshots={};wantedtimes={97293,154679,154933,158226,96439,91747}
for t in range(158227):
 if t in wantedtimes:snapshots[t]=(set(B),p,h)
 if t==158226:break
 c='L'if p in B else'R';history.append(c);visited.add(p);B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1])
assert ''.join(history[91747:97293])==''.join(W[i%1564]for i in range(5546))
assert history[97293]=='R' and W[5546%1564]=='L'
efield,ep,eh=snapshots[97293];assert (ep,eh)==((31,71),2) and ep not in seed
# First unmet fuel really was never read earlier, rather than a replacement.
q=(33,70);g=3
for c in history[:97293]:assert q!=ep;g=(g+(1 if c=='R'else-1))%4;v=V[g];q=(q[0]+v[0],q[1]+v[1])
assert efield==set(map(tuple,E['field_before_contact'])) and len(efield)==11187
assert ''.join(history[97293:])==A['continuation_word'];assert (p,h)==((34,129),1) and len(B)==13386
hashfield=lambda b:hashlib.sha256(json.dumps(sorted(b),separators=(',',':')).encode()).hexdigest()
assert hashfield(B)==A['final_field_sha256']
# Only our previously independently proved finite-board ray arithmetic is reused.
s=SELF.with_name('check_prepared1564_connected_capture_independent.py').read_text();exec(compile(s[s.index('def periodic('):s.index('reports=[]')],str(SELF),'exec'))
reports=[]
for e in A['events']:
 b,q,g=snapshots[e['time']];assert [list(q),g]==e['pose'] and len(b)==e['mass']
 w=e['word'];assert w in {H[i:]+H[:i]for i in range(104)}
 mismatch,d,groups,n=periodic(b,q,g,w);assert mismatch==e['next_mismatch'] and d==(-2,2)
 if mismatch is not None:
  assert ''.join(history[e['time']:e['time']+mismatch])==''.join(w[i%104]for i in range(mismatch))
  assert history[e['time']+mismatch]!=w[mismatch%104]
 reports.append(dict(time=e['time'],pose=e['pose'],mass=len(b),next_mismatch=mismatch,drift=d,orbits=len(groups),critical_levels=n))
# Fresh far-black flips must defeat every retained active full ray.
w=A['capture_word'];_,d,groups,n=periodic(B,p,h,w);flips=0
for a in groups:
 z=(a[0]+1000000*d[0],a[1]+1000000*d[1]);assert periodic(B^{z},p,h,w)[0]is not None;flips+=1
# Compute the exact next canonical phase-zero rather than infer it from pose.
phase=next(i for i in range(104)if w==H[i:]+H[:i]);delta=(-phase)%104;q=p;g=h
for c in w[:delta]:g=(g+(1 if c=='R'else-1))%4;v=V[g];q=(q[0]+v[0],q[1]+v[1])
out=dict(status='PASS independent whole184-cell sample through finite wave exhaustion and exact NW104 capture',sources={f:hashlib.sha256((U/f).read_bytes()).hexdigest()for f in ['prepared1564_noncrossing_R100_N3.json','prepared1564_first_finite_endpoint.json','prepared1564_first_endpoint_capture.json']},literal_updates=158226,initial_mass=184,first_wave_mismatch=dict(time=97293,offset=5546,phase=854,pose=[[31,71],2],wanted='L',actual='R',previous_read=None),events=reports,capture_mass=len(B),final_field_sha256=hashfield(B),far_flip_rejections=flips,next_canonical_phase0=dict(time=158226+delta,pose=[list(q),g]),scope='Only supplied R100,N3 finite seed. No all-N eventual capture is inferred.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
