from pathlib import Path
from collections import Counter,defaultdict
import hashlib,json
S=Path(__file__).resolve();R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for line in(D/'WAVE_SCOPE_SHA256SUMS').read_text().splitlines():h,p=line.split(None,1);assert sha(R/p)==h
ns={'__file__':str(S.with_name('check_all_cap_extremal_read_coupling_independent.py'))};exec(Path(ns['__file__']).read_text().split('std=json.loads')[0],ns);trace,key,loops,V=[ns[k]for k in['trace','key','loops','V']]
G=R/'nonlinear_global_budget_2026-10-23';std=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text());W={'S104':std['word'],'P1564':json.loads((G/'prepared_travelling_wave_certificate.json').read_text())['word'],'Q4352':json.loads((G/'second_prepared_wave_certificate.json').read_text())['word']};ref=json.loads((D/'wave_roots_and_stock_scope.json').read_text());ints=json.loads((D/'all_cut_wave_interfaces.json').read_text());xy=lambda p:(int(p.real),int(p.imag));cx=lambda p:complex(*p);mask=lambda p:int(p.real)%2==0 and int(p.real+p.imag)%28==20
roots={}
for name,w in W.items():
 ev,dr,hh=trace(w);assert hh==0;H=defaultdict(list)
 for t,p,hi,ho,c in ev:
  q,k=key(p,dr);H[q].append((t-k*len(w),hi,ho,c))
 for q in H:H[q].sort();assert all(a[3]!=b[3]for a,b in zip(H[q],H[q][1:]))
 F={q:key(q+V[es[0][2]],dr)for q,es in H.items()if es[0][3]=='R'};L={q:key(q-V[es[-1][1]],dr)for q,es in H.items()if es[-1][3]=='L'}
 got={'period':len(w),'drift':list(xy(dr)),'read_classes':len(H),'first_black_roots':sum(es[0][3]=='L'for es in H.values()),'last_black_roots':sum(es[-1][3]=='R'for es in H.values()),'first_R_cycles':[(len(c),a)for c,a in loops(F)],'reverse_last_L_cycles':[(len(c),a)for c,a in loops(L)],'selected_stock_delta':sum((1 if c=='R'else-1)for t,p,hi,ho,c in ev if mask(p))}
 for k in('period','drift','read_classes','first_black_roots','last_black_roots','selected_stock_delta'):assert got[k]==ref['graphs'][name][k]
 for k in('first_R_cycles','reverse_last_L_cycles'):assert got[k]==[(len(z['cells']),z['winding'])for z in ref['graphs'][name][k]]
 assert mask(0j)==mask(dr) and all(mask(p)==mask(p+dr)for _,p,_,_,_ in ev);roots[name]=got
mixed=[];canonical=[]
for row in ints['reports']:
 a,b=W[row['source']],W[row['target']];i,j=row['witness_phases'];w=a[i:]+a[:i]+b[j:]+b[:j];wit=row['witness'];B={cx(q)for q in wit['minimum_black']};p=0j;h=0;first={}
 for t,c in enumerate(w):
  assert(c=='L')==(p in B);first.setdefault(p,c);B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 assert B=={cx(q)for q in wit['final_black']}and xy(p)==tuple(wit['final_position'])and h==wit['final_heading']==0
 assert {q for q,c in first.items()if c=='L'}=={cx(q)for q in wit['minimum_black']}
 mixed.append({'source':row['source'],'target':row['target'],'phases':(i,j),'seed_mass':len(wit['minimum_black']),'final_mass':len(B),'reads':len(w)})
 last={};bad=None
 for t,p,hi,ho,c in trace(a+b)[0]:
  if p in last and last[p][1]==c:bad={'time':t,'cell':list(xy(p)),'requested':c,'previous_read_time':last[p][0],'previous_read_turn':last[p][1]};break
  last[p]=(t,c)
 assert bad==row['canonical_cut_pair']['first_conflict'];canonical.append(bad)
# Full normal-form periodic backgrounds plus finite XOR edits are retained.
prepared=[]
for nr,(fn,name,bkey)in enumerate([('prepared_wave_five_band_normal_form.json','P1564','full_black_orbit_profiles'),('three_standard_band_wave_normal_form.json','Q4352','full_black_profiles')]):
 d=json.loads((G/fn).read_text());rf=ref['complete_prepared_fields'][nr];assert sha(G/fn)==rf['normal_form_sha256'];start=cx(d['pose'][0]);p=start;h=h0=d['pose'][1];stride=d['drift'][0];bulk=set(map(tuple,d[bkey]));X={cx(q)for q in d['finite_XOR_cap']};H=defaultdict(list)
 for t,c in enumerate(W[name]*3):
  x,y=xy(p);black=((x-y,x%2)in bulk)^(p in X);assert black==(c=='L')
  if t<len(W[name]):H[(x-y,x%stride)].append((t-len(W[name])*((x-x%stride)//stride),c))
  X.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 assert p==start+3*stride*(1+1j)and h==h0
 for r in H:H[r].sort();assert all(a[1]!=b[1]for a,b in zip(H[r],H[r][1:]))
 BB={(t,a)for t,b in bulk for a in range(b,stride,2)};unused=BB-set(H);need={r for r,es in H.items()if es[0][1]=='L'};assert need==BB&set(H);OO=BB^{r for r,es in H.items()if len(es)%2};selected=lambda r:mask((complex(r[1],r[1]-r[0])-start)*(-1j)**(-h0))
 got={'full_bulk_black_classes':len(BB),'full_output_black_classes':len(OO),'untouched_black_classes':len(unused),'selected_full_input':sum(map(selected,BB)),'selected_full_output':sum(map(selected,OO)),'selected_untouched':sum(map(selected,unused)),'retained_finite_XOR_cap_count':len(d['finite_XOR_cap']),'final_full_XOR_count':len(X),'final_full_XOR_sha256':hashlib.sha256(json.dumps(sorted(map(xy,X)),separators=(',',':')).encode()).hexdigest()}
 for k,v in got.items():assert v==rf[k]
 prepared.append(got)
# Independently reconstruct phase14 finite seed from the original actual seed.
B={cx(q)for q in std['seed']};p=0j;h=std['heading']
for c in W['S104'][:14]:assert(c=='L')==(p in B);B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=V[h]
B={(q-p)*(-1j)**(-h)for q in B};counter=ref['phase14_countercontrol'];assert B=={cx(q)for q in counter['initial_black']};w=W['S104'][14:]+W['S104'][:14];ev,dr,hh=trace(w);assert dr==-2+2j and hh==0
# Every phase's bit is a piecewise-constant function of period number. Test
# all previous-phase alignment thresholds and the isolated initial-seed hits.
def mult(q,d):
 k=int(q.real)//int(d.real)
 return k if q==k*d else None
period_cases=0
for i,q,hi,ho,c in ev:
 thresholds=[];tests={0}
 for j,r,_,_,_ in ev:
  k=mult(r-q,dr)
  if k is not None and(k>0 or(k==0 and j<i)):thresholds.append(k);tests.add(k)
 for r in B:
  k=mult(r-q,dr)
  if k is not None and k>=0:tests|={k,k+1}
 for n in tests:
  assert((q+n*dr in B)^(sum(k<=n for k in thresholds)%2))==(c=='L');period_cases+=1
stockgain=sum((1 if c=='R'else-1)for _,p,_,_,c in ev if mask(p));assert stockgain==1
out={'status':'PASS supplied wave roots, complete background controls, SIX representatives only, and exact standard stock replenishment','author_note':sha(D/'WAVE_RENEWAL_SCOPE_COUNTERCHECKS.md'),'graphs':roots,'six_mixed_replays':mixed,'six_canonical_immutable_conflicts':canonical,'complete_background_controls':prepared,'phase14_all_future_threshold_cases':period_cases,'phase14_stock_gain_per_period':stockgain,'scope':['All-cut legal-pair counts remain author discovery data; they were NOT independently enumerated or used as a premise.','Each supplied finite minimum board and complete final field was replayed without discarding unread cells. These are one-period mixed joins, not recurrent controllers or mature-output conversions.','The complete normal-form background and finite XOR cap are retained in three-period controls. Their all-future prepared-wave validity remains the attributed retained certificate, not this replay.','The phase14 standard finite seed has a fresh exact all-period color certificate. Drift preserves the stock mask and each period contributes+1, so the proposed phase-blind stock is not monotone even in a standard tail.','First/last causal graphs retain genuine prepared input roots; supplied prepared waves are not autonomous WHITE translators. This does not classify other controllers.']}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
