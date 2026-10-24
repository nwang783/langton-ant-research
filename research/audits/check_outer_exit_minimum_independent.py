from pathlib import Path
from collections import defaultdict
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files={'OUTERMOST_EXIT_BASIN_OUTPUT_TARGET_AND_EXACT_BOUNDARY.md':'9956058bff409f142ca1e0f3ee4a859cbdc8535d97a7629838d8299cd10e49fe','certify_outer_exit_component_minimum.py':'4d5f62a5fb98f075e8f36e490df48e549ad12f31f3beb4013be256d13be9ba4b','outer_exit_component_minimum_certificate.json':'394eec5388245b60faa9dd0f04e17dce8f2de80a3d966fa87b49a6e2a943c7ce'}
for f,h in files.items():assert sha(D/f)==h
ref=json.loads((D/'outer_exit_component_minimum_certificate.json').read_text())
for f,h in ref['dependencies'].items():assert sha(D/f)==h
lib=S.with_name('check_exit_component_flux_independent.py');ns={'__file__':str(lib)};exec(lib.read_text().split('base={};summaries={}')[0],ns);analyze,V,xy=ns['analyze'],ns['V'],ns['xy'];checks=[]
def probe(z):
 a=analyze(z['word'],z['heading']);P=a['P'];d=a['d'];E=a['E'];H=a['H'];normal=lambda q:int(d.real*q.imag-d.imag*q.real)
 cs=sorted(a['comp'],key=lambda c:min(normal(q)for q in c['cycle']));order={c['cid']:i for i,c in enumerate(cs)};cellbasin={q:order[c['cid']]for c in cs for q in c['cells']};white=all(E[ls[0][1]][3]=='R'for ls in H.values());assert white==z['WHITE']
 for c,r in zip(cs,z['ordered_basins']):
  assert(c['O'],c['I'],c['g'],c['phi'],c['Q'],c['phi']%4)==(r['O'],r['I'],r['charge'],r['fixed_heading_Phi'],r['Q'],r['Phi_mod4']);assert sorted(map(xy,c['cells']))==r['read_classes']
 for value,rank in[(min(map(normal,H)),0),(max(map(normal,H)),len(cs)-1)]:
  qs={q for q in H if normal(q)==value};assert all(cellbasin[q]==rank for q in qs)
  zz=next(x for x in z['extrema']if x['ordered_basin']==rank and x['normal_value']==value);assert {complex(*x['class'])for x in zz['complete_extreme_histories']}==qs
  if white and d.real and d.imag:assert all(len(H[q])==1 and E[H[q][0][1]][3]=='R'for q in qs)
 def qu(q):
  v=int(q.real if d.real else q.imag);dd=int(d.real if d.real else d.imag);k=(v//abs(dd))*(1 if dd>0 else-1);return q-k*d,k
 crossings=[]
 for x in a['cross']:
  t=x['source_phase'];p=complex(*x['source_position']);v=complex(*x['target_position']);q,k=qu(p);r,l=qu(v);A=H[q][0][0]+k*P;B=H[q][-1][0]+k*P;C=H[r][0][0]+l*P;F=H[r][-1][0]+l*P
  assert A<=t and B>=t+4 and C<=t+1<=F
  if white and x['target_complete_rank']==0:assert C==t+1 and x['target_turn']=='R'
  crossings.append(dict(source_phase=t,source_basin=order[x['source_component']],target_basin=order[x['target_component']],source_first_time=A,source_last_time=B,target_first_time=C,target_last_time=F,source_turn=x['source_turn'],source_rank=x['source_complete_rank'],target_turn=x['target_turn'],target_rank=x['target_complete_rank'],actual_next_source_read=x['required_next_same_cell_read']))
 assert crossings==z['every_cut_crossing_first_last_clock'];checks.append([P,xy(d),[(c['O'],c['I'],c['phi'],c['Q'])for c in cs],len(crossings)]);return a
base={n:probe(z)for n,z in ref['base_controls'].items()}
for z in ref['all4_standard_rotations']:probe(z)
zz=ref['reversed_standard_prepared_premise_check'];a=probe(zz['analysis']);w=a['E'];P=a['P'];d=a['d'];E=a['E'];H=a['H'];norm=zz['full_background'];word=zz['analysis']['word'];assert word==ref['base_controls']['S104']['word'][::-1].translate(str.maketrans('RL','LR'))
def layer(q,p):
 return int((p.real-q.real)/d.real)if d.real else int((p.imag-q.imag)/d.imag)
cap=set();rays={};profiles={}
for q,ls in H.items():
 rows=[(t,layer(q,E[i][0]),i)for t,i in ls];lo=min(k for t,k,i in rows);hi=max(k for t,k,i in rows);cc=[]
 for k in range(lo,hi):
  t,_,i=min(x for x in rows if x[1]<=k)
  if E[i][3]=='L':cc.append(k);cap.add(q+k*d)
 ray=hi if E[ls[0][1]][3]=='L'else None
 if ray is not None:rays[q]=hi
 assert E[ls[-1][1]][3]=='L'
 profiles[q]=(lo,hi,cc,ray)
 rr=next(z for z in norm['full_class_profiles']if complex(*z['class'])==q);assert(rr['lowest_read_lift'],rr['highest_read_lift'],rr['cap_lifts'],rr['ray_start'])==(lo,hi,cc,ray)
 for row,(t,k,i)in zip(rr['stable_events'],rows):
  p,hin,hout,c=E[i];assert row==dict(canonical_time=t,lift=k,t=i,p=xy(p),hi=hin,ho=hout,c=c)
assert len(cap)==13 and len(rays)==12 and sorted(map(xy,cap))==norm['complete_forward_cap']
assert {(complex(*z['class']),z['start_lift'])for z in norm['complete_forward_input_rays']}==set(rays.items())
def bit(q,k):
 lo,hi,cc,ray=profiles[q];return k in cc or ray is not None and k>=ray
for q,ls in H.items():
 ts=defaultdict(list)
 for t,i in ls:ts[layer(q,E[i][0])].append(i)
 lo,hi,cc,ray=profiles[q]
 for k in range(lo-2,hi+4):
  state=bit(q,k)
  for i in sorted(ts[k]):assert state==(E[i][3]=='L');state=not state
  assert state==bit(q,k-1)
 # Below lo both sides and all flips are zero; above hi+1 both constant ray bits agree.
 assert not bit(q,lo-2)and not bit(q,lo-3)
 for k in[hi+2,hi+3]:assert bit(q,k)==bit(q,k-1)
# Finite N preparations are the full cap plus precisely N points per ray.
finite=[]
for z in norm['finite_prepared_controls']:
 N=z['copies'];seed=cap|{q+(start+j)*d for q,start in rays.items()for j in range(N)};assert len(seed)==13+12*N and sorted(map(xy,seed))==z['complete_minimal_initial_BLACK'];state=set(seed);p=0j;h=0;seen=set();required=set();reads=[]
 for t,c in enumerate(word*N):
  if p not in seen and c=='L':required.add(p)
  seen.add(p);assert(p in state)==(c=='L');reads.append([t,xy(p),h,c]);state.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 assert required==seed and reads==z['all_reads'];assert state=={q+N*d for q in cap}and sorted(map(xy,state))==z['complete_final_BLACK'];assert p==N*d and h==0 and xy(p)==z['final_head'];finite.append([N,len(seed),len(state)])
std=ref['base_controls']['S104']['every_cut_crossing_first_last_clock'];assert[x['source_phase']for x in std if x['target_rank']==0]==[31]and[x['source_phase']for x in std if x['source_rank']==0]==[38]
rr=ref['one_named_odd_OPEN_minimum_interface'];words=rr['complete_named_histories'];assert words==[[2],[3,1],[2,2],[1,1,3],[2,2,0,0]];arrows={str(i):i+int(3*V[(hs[-1]+(1 if len(hs)%2 else-1))%4].imag-V[(hs[-1]+(1 if len(hs)%2 else-1))%4].real)for i,hs in enumerate(words)};assert arrows==rr['last_arrows']
outreport=dict(status='PASS non-axis outer-basin singleton lower bound and exact prepared premise checks; four-output target OPEN',script=sha(S),bindings=files,complete_control_summaries=checks,inverse_cap=13,inverse_input_rays=12,finite_controls=finite,analytic_review=[
'Physical full-drift last-spine basins are connected embedded sets. For the lowest spine, n below its minimum is wholly on its negative side; a point at that minimum but not on the spine is also negative, since it has a disjoint neighborhood meeting that half-plane. Every higher basin is connected to a higher spine and cannot cross the lowest spine. Thus every global read-footprint minimum belongs to the lowest basin. This does not require a monotone spine or globally separated normal ranges.',
'For non-axis drift, the normal changes nontrivially on each grid axis. At a complete physical read minimum, incoming normal change must be negative and outgoing change positive. The fixed arrival axis permits only one incoming and one outgoing heading, hence one fixed turn. Complete WHITE makes it R, and alternation forbids another visit. Symmetrically each outer basin has at least one permanent singleton. Axis drift is not included.',
'Each cross-basin actual departure is strictly before its source last read and therefore has an actual next same-cell opposite read at a positive multiple of four. Full physical lifts give the stated source/target first/last inequalities. Source lifetime owners remain in the source physical read basin, but intervening movement and root excursions need not. No monotonicity or flux cancellation follows.',
'All five supplied fronts, four proper standard rotations and the reversed/exchanged standard word independently reconstruct. Standard only-first-arrival crossing31 and only-first-R departure crossing38 have opposite basin directions. Branch-cut Phi is additive and integer accounting gives O_outer congruent Phi mod4 under WHITE; divisibility by four would be sufficient, not equivalent, to the open four-output target.',
'The reverse-standard prepared premise check has complete13-cell cap and twelve forward input rays. Every stable class, finite threshold and full one-period field bit relation is independently verified, with empty below-threshold and constant above-threshold tails. All classes end L, so there is no omitted output background. Truncating each input ray after N points agrees on every first-N-copy read and leaves exactly the translated cap: N-copy read lifts never exceed high+N-1, while omitted ray cells begin at high+N. N1 shows every cap bit is actually consumed; the ray farthest-phase first-L witness shows every truncated ray bit is necessary. Thus the all-N13+12N to13 statement is analytic, not extrapolated.',
'The exact inverse outer I7/I5,O0, flux residues1/3 shows the WHITE premise matters and is not a WHITE counterexample. The named minimum-cover interface leaves upper cells unknown; it cannot be called a complete one-output basin. In the live middle-short case an eventual four-output theorem would force one basin, not itself exclude the branch. No second-component theorem, universal output minimum beyond singleton, or global attraction is proved.'
],dependencies=ref['dependencies'])
S.with_suffix('.json').write_text(json.dumps(outreport,indent=2)+'\n');print(outreport['status']);print(sha(S.with_suffix('.json')));print(finite)
