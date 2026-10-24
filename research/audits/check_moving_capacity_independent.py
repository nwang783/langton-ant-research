from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];P=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=P/'MOVING_MODULE_CAPACITY_MANIFEST.json';assert sha(MF)=='e982c78710874aa009286582660c5a4dc4f7362ccd29ae0ed2bbd73a8dc5a6f5';M=json.loads(MF.read_text())
for group in('files','signed_dependencies'):
 for name,h in M[group].items():assert sha(P/name)==h
J=json.loads((P/'MOVING_CAPACITY_REGRESSION_CHECKED.json').read_text());ns={};exec((S.parent/'check_return_permanent_debt_independent.py').read_text().split('def check_case')[0],ns);verify=ns['verify_future'];vec=ns['vec'];xy=ns['pair'];ray=ns['ray_k'];G=ns['G'];B={z:-i-1 for i,z in enumerate(sorted(G,key=lambda z:(z.real,z.imag)))};p=0j;h=1;birth={};death={};cuts=[];trace=[]
for t in range(800):
 cuts.append((dict(B),p,h));trace.append(p)
 if p in B:death[B.pop(p)]=t;h=(h-1)%4
 else:B[p]=t;birth[t]=p;h=(h+1)%4
 p+=vec[h]
word,d,ff,checks=verify(cuts[182][0],cuts[182][1],cuts[182][2]);assert d==2+2j and word==J['word']and checks==J['full_infinite_parity_tests'];source,p0,h0=cuts[182];assert(p0,h0,len(source))==(5+1j,1,36);assert sorted(map(xy,source))==J['source_black']
Q=trace[182:286];Rph=[(i,q)for i,q in enumerate(Q) if 182+i in birth];permanent=[];returns=[]
for phase,q in Rph:
 hits=[]
 for i,r in enumerate(Q):
  k=ray(q-r,d)
  if k is not None and k>=0:hits.append([k,i])
 later=[104*k+i for k,i in hits if 104*k+i>phase]
 if not later:permanent.append(dict(phase=phase,cell=xy(q),all_nonnegative_ray_equalities=hits))
 else:returns.append(dict(phase=phase,cell=xy(q),death=min(later)))
assert permanent==J['actual_permanent_phase_cells']and len(permanent)==12
marked=next(x for x in returns if x['phase']==68);assert marked==dict(phase=68,cell=[7,7],death=184)
Sret={complex(*r['cell'])+k*d for r in permanent for k in range(2) if 68<104*k+r['phase']<184};assert len(Sret)==13 and sorted(map(xy,Sret))==J['translating_marked_return']['permanent_return_support']
assert len(Sret&{q+d for q in Sret})==1
all_shifts=set()
for a in Sret:
 for b in Sret:
  m=ray(a-b,d)
  if m is not None:all_shifts.add(m)
assert all_shifts=={-1,0,1}
for j in range(5):assert birth[250+104*j]==7+7j+j*d and death[250+104*j]==366+104*j
W={complex(*r['cell'])for r in permanent};assert not any((m:=ray(a-b,d))not in(None,0)for a in W for b in W)
# Actual relevant fields, not only birth-phase calculations; all-future parity at both endpoints.
_,_,f182,_=verify(*cuts[182]);_,_,f286,_=verify(*cuts[286]);L182={q for q,tag in cuts[182][0].items()if tag in f182};L286={q for q,tag in cuts[286][0].items()if tag in f286};assert L286=={q+d for q in L182}
all_death=dict(death);all_death.update({tag:182+t for tag,t in f182.items()})
for phase,q in Rph:
 rr=next((x for x in returns if x['phase']==phase),None)
 if rr:all_death[182+phase]=182+rr['death']
Lmax=max(sum(tag in all_death for tag in c[0].values())for c in cuts[:286]);assert Lmax==22
rect=0
for w,H in((1,1),(3,7),(150,9)):
 shape={complex(x,y)for x in range(w)for y in range(H)}
 for dx,dy in((0,0),(1,0),(-1,2),(2,2),(w+1,H+1)):
  assert len({q+complex(dx,dy)for q in shape}-shape)==w*H-max(0,w-abs(dx))*max(0,H-abs(dy))<=H*abs(dx)+w*abs(dy);rect+=1
out=dict(status='PASS moving physical-capacity correction and literal canonical positive regression',manifest=sha(MF),proof=M['files']['MOVING_MODULE_CAPACITY_CORRECTION.md'],all_future_source_parity_tests=checks,full_source182_mass=36,drift=xy(d),marked_birth250_death366=[7,7],all_period_return_age=116,permanent_phase_slots=12,return_permanent_support=sorted(map(xy,Sret)),only_translate_overlap_shifts=sorted(all_shifts),support_union_K='12K+1',entire_relevant_cap22_by_pruned_period_closure=True,rectangle_controls=rect,analytic_review=[
'The signed per-return linewise lower cost is charged to ACTUAL permanent physical cells. At each permanent birth at mostM marked lifetimes are simultaneously relevant, giving4N(w-M)<=M|union_i(S+z_i)|. Disjoint lifetime intervals removeM. Per-episode normalization cannot merge distinct physical births.',
'Each new translated set adds at most its difference from the immediately preceding translate, because the prior union contains that set. Rectangle overlap is max(0,w-|dx|)max(0,H-|dy|), bounded new area byH|dx|+w|dy|. No bound on actual frame travel is supplied.',
'Fresh full four-cell trajectory, complete36-black182state and exact all-future ray parity establish the canonical positive. R250+104j at(7,7)+j(2,2) nextreadsL366+104j. All13permanent births per return and all-integer translate overlaps independently match. One shared cell in adjacent intervals is one permanent birth, not rebirth.',
'The complete future-relevant field at286 is the translated182field, and the fullprefix/period relevant maximum22 is independently recovered. Whole old archive is retained for future parity; only the retrospective relevance projection repeats.',
'This captured bounded-age example does NOT meet unbounded-age, guard-avoidance, or positive w>M debt hypotheses. It falsifies only conserving normalized finite capacity under moving frames, not the proposed nontranslating localization theorem. The reverse-return strip aside is an attributed signed dependency, not evidence of migrated old cohorts.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
