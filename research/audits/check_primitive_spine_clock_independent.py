from pathlib import Path
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
MF=D/'PRIMITIVE_SPINE_CLOCK_MANIFEST.json';assert sha(MF)=='791d3c29af66f0f95c8c541f86beeccd71ca155653f7237d83a3867d8d48e517'
for f,h in json.loads(MF.read_text())['files'].items():assert sha(D/f)==h
ref=json.loads((D/'PRIMITIVE_SPINE_CLOCK_CHECKED.json').read_text())
for f,h in ref['dependencies'].items():assert sha(D/f)==h
base=S.with_name('check_chronological_spine_independent.py');ns={'__file__':str(base)};exec(base.read_text().split('# Full finite original-seed')[0],ns)
for k in ('J','A','BL','BP','BD','ml','SH','sp','geom','mc','V','xy','K','sim','future','phases','encB'):globals()[k]=ns[k]
root=-2+372j;time=dict(BL);time[root]=69097
jumps=[(time[p]-time[q],q,p,time[q],time[p])for q,p in BP.items()];assert all(a[0]>0 for a in jumps)
mx=max(jumps,key=lambda a:a[0]);assert mx==(29865,210+186j,210+187j,29029,58894)
tau={r:2762+max(104*a+i for a,i in ls)for r,ls in ml.items()};bulk=[]
for r,ls in ml.items():
 _,i,a=max((104*a+i,i,a)for a,i in ls);rp,delta=mc(r+V[SH[i]])
 assert time[r]==tau[r]and time[r+2+2j]==tau[r]-104
 jump=tau[rp]-tau[r]-104*delta;assert jump>0;bulk.append(dict(cell=xy(r),parent_class=xy(rp),layer_shift=delta,jump=jump))
assert sorted(bulk,key=lambda r:r['cell'])==sorted(ref['bulk_jumps'],key=lambda r:r['cell'])and max(r['jump']for r in bulk)==125
block=[time[sp[i+1]]-time[sp[i]]for i in range(300,304)];assert block==[1,1,5,97]
checks=[];labels=0
for c in J['MT_controls']:
 n=c['n'];k=n-100;start=complex(*c['start_pose'][0]);h=c['start_pose'][1];w=c['complete_prefix_word'][c['start']:c['end']]
 Q,HH,ep,eh=geom(start,h,w);last={q:i for i,q in enumerate(Q)};last[ep]=len(w);assert ep==root
 par={q:(Q+[ep])[i+1]for q,i in last.items()if q!=ep}
 assert max((last[p]-last[q]for q,p in par.items()))==29865
 for q in par:
  if q.real<=364:pred=time[q]+104*k
  elif q.real>=365+2*k:pred=time[q-k*(2+2j)]
  else:r,j=mc(q);pred=tau[r]+104*(k-j)
  assert pred==last[q]
 labels+=len(par);old=206+229j;assert dict((complex(*q),i)for q,i in c['full_start_field'])[old]==20165
 death=c['start']+Q.index(old);assert death==31805+208*n and w[Q.index(old)]=='L';checks.append(dict(n=n,labels=len(par),max_jump=29865,old_birth=20165,old_death=death,old_age=death-20165))
assert labels==37820
out=dict(status='PASS primitive positive last-parent cycles, zero effective turning, and scoped all-n interval-tree clock',manifest=sha(MF),dependencies=ref['dependencies'],baseline_edges=len(BP),maximum=[mx[0],xy(mx[1]),xy(mx[2]),mx[3],mx[4]],all22_bulk_clocks=bulk,inserted_spine_jumps=block,all_time_labels=labels,controls=checks,analytic=[
'The last-parent quotient cycle is an embedded curve in the full-drift cylinder: distinct quotient vertices, unit grid edges and integer deck translation exclude transverse crossings and overlapping edge interiors. The exceptional two-edge backtrack has zero displacement and is ruled out by independently proved positive last-time voltage.',
'A cycle of positive shift m lifts to m disjoint proper periodic lines, each bounded transversely and separating the two transverse ends. Translation by d preserves their transverse linear order yet permutes them cyclically. Thus m=1. This proof uses actual selected grid edges, not an abstract clock graph or black Tait graph.',
'A disjoint straight parallel essential curve and the embedded cycle bound a compact flat annulus. Finite triangle-angle counting with F=2Vi+Vb makes the total boundary turning zero. The straight component contributes zero, so the cycle turning is exactly zero. Sector alternation ensures every nondegenerate selected grid turn is a quarter turn.',
'The general component theorem therefore simplifies to the number of quotient cycles. No uniform bound on the number of cycles, or existence of a translating future, is inferred.',
'Every baseline cap time and parent is independently reconstructed from actual A/SW/F last hits by the prior checker prefix. Upper times have slope0, lower times slope104K; middle tau+104(K-k) agrees at both interfaces through tau(r)=time(r) and time(r+2diag)=tau(r)-104. Consequently every edge jump is exactly baseline or one of22 bulk constants for ALL integer n>=100, not a finite-fit inference.',
'The entire reset drought tree has exact maximum29865 on the fixed lower edge210,186 to210,187. The inserted spine jumps1,1,5,97 add104. All37820 named labels independently reconstruct. The simultaneously consumed R20165 has true lifetime age11640+208n, so bounded selected-edge latency is not bounded identity age.',
'This clock bound is for T_[s_n,t_n], not the historical T_[0,t_n]. All family members capture; no one-orbit infinite drought, global clock occurrence, lifetime-age bound or gross leaf theorem follows.'
])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
