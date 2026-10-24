from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'TRANSVERSE_PERMANENT_BUDGET_MANIFEST.json';assert sha(MF)=='36ea5f3665cdd802c6f8284e59f7d3ac83fa7b468cc4a6b5a94da58cbae0da71';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
P=json.loads((D/'TRANSVERSE_PERMANENT_BUDGET_CHECKED.json').read_text())
ns={'__file__':str(S.with_name('check_transverse_far_module_independent.py'))};exec(Path(ns['__file__']).read_text().split('controls=[]')[0],ns)
verify,vec,xy,ray,G,AP,Q,A,U,F,Z,pt,V,counts,parts,target,protected,omega=[ns[k]for k in('verify','vec','xy','ray','G','AP','Q','A','U','F','Z','pt','V','counts','parts','target','protected','omega')]
J=ns['J'];protected_death=ns['death'];normal_fates={q:protected_death.get(-i-1)for i,q in enumerate(sorted(protected,key=lambda q:(q.real,q.imag)))};assert sum(t is not None for t in normal_fates.values())==285
# Rebuild the physical four-cell source, its permanent classes, and three phase72 cuts.
B={q:-i-1 for i,q in enumerate(sorted(G,key=lambda q:(q.real,q.imag)))};p=0j;h=1;dead={};birth={};cuts={};positions=[]
for t,ch in enumerate(A+U*4):
 if t in(254,358,462):cuts[t]=(dict(B),p,h)
 positions.append(p);assert(ch=='L')==(p in B)
 if ch=='L':dead[B.pop(p)]=t;h=(h-1)%4
 else:B[p]=t;birth[t]=p;h=(h+1)%4
 p+=vec[h]
N=len(A)+4*104;word,d,ff,tests=verify(B,p,h);assert word==U and d==2+2j;dead.update({tag:N+t for tag,t in ff.items()})
permanent=[(i-182,q)for i,q in birth.items()if 182<=i<286 and i not in dead];assert len(permanent)==12
refsets=[]
for t,(bb,pp,hh)in cuts.items():
 ww,dd,fates,test=verify(bb,pp,hh);assert ww==U[72:]+U[:72]and dd==2+2j and len(fates)==19 and max(fates.values())==112
 refsets.append(({q for q,tag in bb.items()if tag in fates},t,test))
base=refsets[0][0]
for ss,t,_ in refsets:assert ss=={q+(t-254)//104*(2+2j)for q in base}
assert all(tag in dead for tag in range(-4,0))
# The finite launch permanent residue is outside the protected region for every k>=10.
for t,q in birth.items():
 if t<182 and t not in dead:assert q.real+q.imag-12*10-3 < -73
old=[]
for phase,q in permanent:
 for v in range(-30,36):
  z=q+v*(2+2j)-3j
  if(v<-3 or v==-3 and phase<=71)and normal_fates.get(z) is not None:old.append(dict(relative_cell=xy(z),outgoing_phase=phase,relative_copy=v,post_contact_death=normal_fates[z]))
canon=lambda r:json.dumps(r,sort_keys=True);assert len(old)==len({tuple(r['relative_cell'])for r in old})==191 and min(r['relative_copy']for r in old)>=-30
assert set(map(canon,old))==set(map(canon,P['already_written_relevant_periodic_output']))
# No extra distant periodic class is missed: exact Omega bounds bound v; all finite fates were independently classified.
for _,q in permanent:
 assert (q-31*(2+2j)-3j).real+(q-31*(2+2j)-3j).imag < -73
 assert (q+36*(2+2j)-3j).real+(q+36*(2+2j)-3j).imag > 17
bal=lambda w:w.count('R')-w.count('L');assert{key:bal(val)for key,val in{'A':A,'U':U,'U61':U[:61],'U71':U[:71],'U56':U[:56],'U72':U[:72]}.items()}==P['source_word_balances']
# All affine upper extrema at k>=10. Lower extrema come from the independently rebuilt main certificate.
upper=[]
for st,points in enumerate(V):
 for q in points:
  for axis,bound in [(0,(14,1)),(1,(18,-1))]:
   coeff=lambda z:int(z.real)if axis==0 else int(z.imag);a,b=bound[0]-coeff(q[0]),bound[1]-coeff(q[1]);assert a>=0 and 10*a+b>=0;upper.append((st,axis,a,b))
assert len(upper)==3618==P['exact_affine_upper_extrema_tests']
peak_pose=pt(1,Q[56],counts[1]);assert peak_pose==(10+18j,2-1j)
assert 182+104*counts[0][1]+parts[0]+182+104*counts[1][1]+56==-455 and 104*(counts[0][0]+counts[1][0])==936
controls=[]
for rr in J['controls']:
 n=rr['n'];k=n//2;value=lambda q:q[0]*k+q[1];seed={complex(*q)for q in rr['initial_black']};b=156*n-59;a=b+1;c=780*n-1207;peak=468*n-455;qn=3*n+(3*n+3)*1j
 B={q:-i-1 for i,q in enumerate(sorted(seed,key=lambda q:(q.real,q.imag)))};p=0j;h=1;dead={};positions=[];events=[];snap={}
 expected=''.join(A+U*int(value(counts[i]))+U[:parts[i]]for i in range(4))+F+Z*2
 for t,ch in enumerate(expected):
  if t in(a,c,peak):snap[t]=(dict(B),p,h)
  positions.append(p);assert(ch=='L')==(p in B);events.append(ch)
  if ch=='L':dead[B.pop(p)]=t;h=(h-1)%4
  else:B[p]=t;h=(h+1)%4
  p+=vec[h]
 N=len(expected);ww,dd,fates,test=verify(B,p,h);dead.update({tag:N+s for tag,s in fates.items()});assert ww==Z and dd==2-2j
 relsets={t:{q for q,tag in bb.items()if tag in dead}for t,(bb,pp,hh)in snap.items()}
 remote={value(pt(i,q))for i in(1,2,3)for q in G};assert len(remote)==12
 phase_reference={q+(3*k-3)*(2+2j)for q in base};written={qn+complex(*r['relative_cell'])for r in old}
 assert not(remote&phase_reference or remote&written or phase_reference&written)
 assert relsets[a]==remote|phase_reference|written and len(relsets[a])==222
 assert relsets[c]=={qn+q for q,t in normal_fates.items()if t is not None}and len(relsets[c])==285
 assert len(snap[a][0])==18*n+24 and len(snap[c][0])==90*n-67
 pc=sum(events[t]=='R'and t not in dead for t in range(a,c));assert pc==72*n-154
 radius=max(max(abs(z.real-qn.real),abs(z.imag-qn.imag))for z in positions[a:c+1]);assert radius==6*n-4 and positions[peak]==5*n+2+(9*n-1)*1j
 ref=next(r for r in P['controls']if r['n']==n);assert ref['actual_permanent_births_during_return']==pc and ref['peak_relevant']==len(relsets[peak])and ref['full_future_tests']==test
 controls.append(dict(n=n,birth_cut_relevant=len(relsets[a]),predeath_relevant=len(relsets[c]),peak_relevant=len(relsets[peak]),actual_permanent_births=pc,exact_radius=int(radius),entire_normalized_relevant_field_equal=True,all_future_tests=test))
out=dict(status='PASS all-parameter exact transverse-family relevant stock, actual permanent production, and return radius',manifest_sha256=sha(MF),script_sha256=sha(S),main_audit_sha256=sha(S.with_name('check_transverse_far_module_independent.json')),birth_cut_partition=[12,19,191],birth_cut_relevant=222,predeath_relevant=285,periodic_output_classes=12,independent_phase72_cuts=[254,358,462],phase72_latest_first_read=112,upper_affine_extrema=len(upper),controls=controls,analytic_review=[
'Future-relevant current positions are exactly future first-L cells. Hence equal future word and pose give an exact translated pruned field, not an assumption of equal birth timestamps. Three independent phase72 comparisons each give19 current future inputs all read by112; the first remote port is208n-115 updates away.',
'Twelve remote initial lifetimes are distinct and consumed in their own first59 reads. The other reference-current cells are either one of19 near-future inputs, finite launch permanent residue, or a genuinely permanent periodic-output class. Launch residue is outside protected Omega for allk>=10. The complete12-class/finite-Omega matching yields exactly191 already-born actual protected-future inputs; required copy indices exist already at k10. No cross-stage read can retire these identities beforec by the signed complete-read separators.',
'At predeathc the entire normalized330-cell protected field is exact and all exterior is never read; its independently computed finite fates give the same285-cell entire relevant field for everyparameter. Full mass balances then imply actual new permanent birthsP=72n-154 on[b+1,c), not template-predicted wake or total final permanent stock.',
'Fresh3618 affine upper extrema and signed lower extrema give radius<=6n-4; actual stage1 phase56 at time468n-455 gives equality. The named fullboards independently check all relevance partitions, complete fields, permanent lifetimes and infinite futures.',
'Identical normalized current relevant field determines the same future word, but does not bound the past returning lifetime age or permanent physical production uniformly across finite seeds. Every member captures; no contradiction to one-time deletion coupling, eventual per-orbit bounded age, or global attraction is asserted.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
