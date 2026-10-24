from pathlib import Path
from collections import defaultdict,Counter
from math import gcd
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'NORMALIZED_LIFETIME_WINDING_BUDGET_TARGET.md';J=json.loads((D/'normalized_lifetime_winding_budget_controls.json').read_text());assert sha(D/'normalized_lifetime_winding_budget_controls.json')=='688708114d220166f2728ff3d1e59565b90412992da7e5ac8a622422675046d3';assert sha(D/'explore_normalized_lifetime_winding_budget.py')=='2ac5ceeb4fe5aa59fed2e1f5e75cc831945703220c05c1264b98ce0260e9e82e'
for f,h in J['dependency_hashes'].items():assert sha(D/f)==h
assert sha(D/J['complete_background_dependency']['path'])==J['complete_background_dependency']['sha256']
ns={'__file__':str(S.with_name('check_lifetime_boundary_graph_independent.py'))};text=Path(ns['__file__']).read_text().split('\nW={')[0];text=text.replace('def analyze(w):','def analyze(w,h0=0):').replace('P=len(w);p=0j;h=0;E=[]','P=len(w);p=0j;h=h0;E=[]').replace('assert h==0 and d.real and d.imag','assert h==h0 and d.real and d.imag');exec(text,ns);analyze=ns['analyze'];quo=ns['quo'];xy=ns['xy']
G=R/'nonlinear_global_budget_2026-10-23';words={'S104':json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word'],'P1564':json.loads((G/'prepared_travelling_wave_certificate.json').read_text())['word'],'Q4352':json.loads((G/'second_prepared_wave_certificate.json').read_text())['word'],'prepared10':'RRRRLLLLRL'}
def stats(w,h=0):
 E,d,I,O,paths,cyc,rc,H=analyze(w,h);m=gcd(abs(int(d.real)),abs(int(d.imag)));winds=sorted(v for _,v,_,_ in rc);ss=sum(winds)
 return dict(P=len(w),initial_heading=h,full_drift=xy(d),m=m,I=len(I),O=len(O),absolute_boundary_windings=winds,S=ss,candidate_left=m*(ss-1),candidate_right=2*min(len(I),len(O)),candidate_holds_on_this_control=m*(ss-1)<=2*min(len(I),len(O)),internal_component_lengths={str(k):v for k,v in Counter(map(len,cyc)).items()})
controls=0;phasecontrols=0;interactions={}
for name,w in words.items():
 r=J['controls'][name];assert hashlib.sha256(w.encode()).hexdigest()==r['word_sha256'];base=stats(w);assert base==r['base']
 for row in r['power_rotation_controls']:
  q=row['P']//len(w);h=row['initial_heading'];assert q in(1,2,3,5)and stats(w*q,h)==row
  expected=sorted(z//gcd(q,z)for z in base['absolute_boundary_windings']for _ in range(gcd(q,z)));assert row['absolute_boundary_windings']==expected and row['S']==base['S']
  for k in('m','I','O','candidate_left','candidate_right'):assert row[k]==q*base[k]
  controls+=1
 for row in r['phase_controls']:
  c=row['cut'];assert stats(w[c:]+w[:c])==row['statistics'];phasecontrols+=1
 # Independent physical ownership inventory; use supplied orientation only as a certificate path.
 E,d,I,O,paths,cyc,rc,H=analyze(w);N=len(w);ks={e['t']:quo(complex(*e['p']),d)[1]for e in E};life={}
 for records in H.values():
  ids=[i for t,i in sorted(records)]
  for a,b in zip(ids,ids[1:]):
   if w[a]=='R':
    k=ks[a]-ks[b];age=b+k*N-a;assert age>=4 and age%4==0 and complex(*E[a]['p'])==complex(*E[b]['p'])+k*d;life[a]=(b,k,age)
 expected=set()
 for a,(b,k,age)in life.items():expected.add((a,b,k,'alpha',a,age));expected.add(((a+1)%N,(b+1)%N,k+(b==N-1)-(a==N-1),'beta',a,age))
 expected|={(i,(i+1)%N,int(i==N-1),'I'if i in I else'O',i,1)for i in I|O}
 rr=J['full_shared_lifetime_interactions'][name];edges=[tuple(x)for x in rr['directed_edges_with_positive_age']];assert len(edges)==len(expected)and set(edges)==expected and set(rr['I'])==I and set(rr['O'])==O
 adj=Counter(x for a,b,*other in edges for x in(a,b));assert adj==Counter({i:2 for i in range(N)});seen=set();where={};eventseen=set()
 for ci,c in enumerate(rr['expanded_circuits']):
  seq=c['oriented_edges'];wind=0;rootsteps=0;debt=0;nodes=[];prev=None
  for ei,sign in seq:
   assert ei not in seen and sign in(-1,1);seen.add(ei);a,b,k,typ,owner,age=edges[ei];start,end=(a,b)if sign==1 else(b,a)
   if prev is not None:assert prev==start
   prev=end;nodes.append(start);wind+=sign*k;where[ei]=(ci,sign)
   if typ in('I','O'):rootsteps+=sign
   else:debt+=sign*age
   assert end-start+sign*k*N==sign*age
  assert prev==nodes[0]and len(nodes)==len(set(nodes))and not eventseen.intersection(nodes);eventseen.update(nodes)
  assert(wind,rootsteps,debt,len(seq))==(c['winding'],c['signed_root_step_count'],c['signed_lifetime_age_sum'],c['event_count'])and wind*N==rootsteps+debt
  assert sum(edges[i][3]in('I','O')for i,sign in seq)==c['unsigned_root_step_count']
 assert seen==set(range(len(edges)))and eventseen==set(range(N));assert sorted(abs(c['winding'])for c in rr['expanded_circuits']if c['unsigned_root_step_count'])==base['absolute_boundary_windings'];assert all(c['winding']==0 for c in rr['expanded_circuits']if not c['unsigned_root_step_count'])
 summary=Counter();owners=set()
 for row in rr['every_owned_lifetime_and_both_copies']:
  a=row['R_phase'];owners.add(a);b,k,age=life[a];assert(row['L_phase'],row['alpha_voltage'],row['actual_lifetime_age'])==(b,k,age)
  aa=next(i for i,e in enumerate(edges)if e[3]=='alpha'and e[4]==a);bb=next(i for i,e in enumerate(edges)if e[3]=='beta'and e[4]==a);ca,sa=where[aa];cb,sb=where[bb];assert row['alpha_copy']==dict(component=ca,traversal_sign=sa)and row['beta_copy']==dict(component=cb,traversal_sign=sb);summary[ca==cb,sa==sb]+=1
 assert owners==set(life)and [dict(same_component=a,same_sign=b,count=n)for(a,b),n in sorted(summary.items())]==rr['shared_copy_summary'];interactions[name]=dict(lifetimes=len(life),circuits=len(rr['expanded_circuits']),shared=rr['shared_copy_summary'])
assert controls==64 and phasecontrols==12
std=interactions['S104']['shared'];assert sum(x['count']for x in std if x['same_component']and x['same_sign'])==12 and sum(x['count']for x in std if x['same_component']and not x['same_sign'])==12 and sum(x['count']for x in std if not x['same_component'])==22
out=dict(status='PASS exact cover invariance and full shared-lifetime circuit identities ONLY; input-budget inequality UNPROVED',proof=sha(P),script=sha(S),controls_certificate=sha(D/'normalized_lifetime_winding_budget_controls.json'),power_rotation_controls=controls,phase_controls=phasecontrols,full_interactions=interactions,analytic_review=['A q-fold full-period cover changes each cycle sheet by w modq, so a w!=0 cycle lifts to gcd(q,absw) cycles of absolute windingabsw/gcd. Zero winding hasq copies. The absolute sum S is unchanged, while m,I,O scaleq. This is exact representation invariance, not permission to replace the physical full quotient by a primitive one.','Quarter rotations are physical bijections; phase changes alter gauges only. All64 supplied power/rotation and12 phase cases are independently reconstructed. Complete prepared backgrounds/passive strands and finite caps remain the previously signed dependency, not finite-seed input-free histories.','Adding the exact unmatched-root sigma edge fills the missing alpha and beta half-edges and gives a degree-two multigraph on ALL P phases. Supplied oriented circuit certificates exhaust every actual event and edge, retaining zero-voltage internal circuits and distinct input/output endpoints.','Each physical ownedR-to-nextL age is positive and divisible4. Its alpha and beta copies have exactly the same elapsed age, including seam terms, but may lie in different circuits or be traversed with equal signs. Direct endpoint telescoping gives wP=r+sum(sign*age). Every owner and both copies are independently reconstructed, not canceled by name.','Standard has12 equal-sign same-circuit lifetime pairs,12 opposite-sign same-circuit pairs and22 split pairs. These genuine WHITE incidences invalidate naive cancellation. No positivity, bounded debt, owner injection or proposed m(S-1)<=2min(I,O) proof follows. The four middle-short necessary boundary types remain OPEN. Discovery searches are not theorem premises.'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
