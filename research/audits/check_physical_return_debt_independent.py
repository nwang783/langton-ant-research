from pathlib import Path
from collections import Counter
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for line in(D/'PHYSICAL_RETURN_DEBT_SHA256SUMS').read_text().splitlines():
 h,f=line.split();assert sha(D/f)==h
F=D/'PHYSICAL_RETURN_DEBT_AND_ORDINAL_INTERFACE.md';assert sha(F)=='697949854107878c9e36adbf91e63008351ea36553a446abf2d4b5175893d6ea'
J=json.loads((D/'physical_return_debt_certificate.json').read_text());V=[1j,1,-1j,-1];xy=lambda q:[int(q.real),int(q.imag)];quot=lambda q:(int(3*q.imag-q.real),int(q.imag))
for f,h in J['dependency_hashes'].items():assert sha(D/f)==h
# Rebuild all16 charges and the shared-endpoint conflict physically.
for row in J['sixteen_rotated_endpoint_charge_cases']:
 alpha=row['loop_orientation'];v=row['incoming_return_heading'];u=(v+alpha)%4;sigma=row['source_turn'];p=0j;h=(u-sigma)%4;ev=[]
 for i,s in enumerate([sigma]+[alpha]*3+[-sigma]):
  ev.append([xy(p),h,s]);h=(h+s)%4;p+=V[h]
 assert ev==row['events']and ev[4][0]==[0,0]and ev[4][1]==v
 charge=0 if sigma==alpha else 4;assert charge==row['charged_endpoint']and ev[charge][1:]==[v,alpha]
 # Only possible double charge is adjacent loops: alpha endpoint at middle; both first helpers SAME physical point.
 p=0j;h=(u+alpha)%4;reads=[]
 for s in[-alpha]+[alpha]*7:
  reads.append((p,s));h=(h+s)%4;p+=V[h]
 assert reads[1][0]==reads[5][0]and reads[1][1]==reads[5][1]==alpha and all(q!=reads[1][0]for q,s in reads[2:5])
# Complete finite factor replay, retaining all initial and final cells.
def replay(z):
 B={complex(*q)for q in z['initial_black']};p=complex(*z['events'][0]['position']);h=z['events'][0]['incoming_heading']
 for t,c in enumerate(z['word']):
  assert ('L'if p in B else'R')==c;assert z['events'][t]==dict(time=t,position=xy(p),incoming_heading=h,turn=c)
  B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 assert sorted(map(xy,B))==z['final_black']and xy(p)==z['final_position']and h==z['final_heading']
replay(J['sharp_five_read_prepared_control']);assert not J['sharp_five_read_prepared_control']['final_black']
for z in J['arbitrary_length_prepared_first_return_controls']:
 replay(z);n=z['n'];moves=([1,0]*n)+([1,2]*n)+([3,2]*n)+([3,0]*n);p=0j;h=0;seen=set();seed=set();word=''
 for hh in moves:
  assert p not in seen;seen.add(p);c='R'if(hh-h)%4==1 else'L';assert(hh-h)%4 in(1,3)
  if c=='L':seed.add(p)
  word+=c;p+=V[hh];h=hh
 assert p==0 and h==0 and len(seen)==8*n and len(seed)==4*n-2 and word+'L'==z['word']and sorted(map(xy,seed))==z['initial_black']and len(z['final_black'])==4*n+1
# Reconstruct each open physical-ordinal graph without the author's graph function.
stage_reports=[]
for stage in J['specified_open_debt_interface']:
 H={int(t):list(w)for t,w in stage['named_histories'].items()};nodes={(t,r)for t,w in H.items()for r in range(len(w))};succ={};inc={};outs={e:(H[e[0]][e[1]]+(1 if e[1]%2==0 else-1))%4 for e in nodes}
 for t,w in H.items():
  for h in range(4):
   dest,vol=quot(-t+V[h]);src=[r for r in range(len(w))if outs[t,r]==h]
   if dest not in H:continue
   dst=[r for r,c in enumerate(H[dest])if c==h];assert len(src)==len(dst)
   for r,s in zip(src,dst):succ[t,r]=((dest,s),vol);inc[dest,s]=((t,r),vol)
 chains=[];seen=set();where={}
 for start in sorted(nodes-set(inc)):
  at=start;v=0;seq=[]
  while True:
   assert at not in seen;seen.add(at);seq.append((at,v));where[at]=(len(chains),len(seq)-1,v)
   if at not in succ:break
   at,dv=succ[at];v+=dv
  chains.append(seq)
 assert seen==nodes
 records=[];same=[]
 for chain in chains:
  previous={}
  for j,((t,r),vol)in enumerate(chain):
   p=-t+vol*(3+1j)
   if p in previous:assert r==previous[p]+1
   previous[p]=r
  (t,r),a=chain[0];source=-t-V[H[t][r]];ts,vs=quot(source)
  (t,r),b=chain[-1];target=-t+b*(3+1j)+V[outs[t,r]];td,vd=quot(target)
  records.append((ts,td,vd-vs,len(chain)+1))
  if source==target:same.append(len(chain)+1)
 supplied=stage['all_boundary_chains'];assert Counter(records)==Counter((z['source_level'],z['target_level'],z['voltage'],z['outside_read_distance'])for z in supplied)
 assert sorted(same)==sorted(p['duration']for p in stage['same_physical_returns'])
 # Necessary rank clocks, not a distinct-phase or full-front completion.
 E=[]
 for t,w in H.items():
  for r in range(len(w)-1):
   i,a,va=where[t,r];j,b,vb=where[t,r+1];E.append((i,j,4+a-b,vb-va))
 Ptest=10*len(nodes)+100;dist=[0]*len(chains)
 for step in range(len(chains)):
  changed=False
  for i,j,c,k in E:
   if dist[j]<dist[i]+c+Ptest*k:dist[j]=dist[i]+c+Ptest*k;changed=True
  if not changed:break
 assert not changed
 stage_reports.append(dict(target=stage['target_level'],events=len(nodes),chains=len(chains),same_cell_return_durations=sorted(same),total_outside_distances=sum(z[3]for z in records),max_outside_distance=max(z[3]for z in records),rank_clock_test_period=Ptest))
assert [z['same_cell_return_durations']for z in stage_reports]==[[4],[4,8],[]]
assert stage_reports[-1]['events']==79 and stage_reports[-1]['chains']==18 and stage_reports[-1]['max_outside_distance']==36 and stage_reports[-1]['total_outside_distances']==97
out=dict(status='PASS physical four-return capacity, specified OPEN chain interface and prepared finite controls',proof=sha(F),certificate=sha(D/'physical_return_debt_certificate.json'),rotated_charge_cases=16,open_stages=stage_reports,analytic_review=[
'Every4step physical first return is a unit square: three helper turns have the same signalpha. Either its source already has alpha/incomingv, or alternation makes its returned endpoint alpha/incomingv. Distinct returns can share that charge only as adjacent same-face excursions, whose first helper would be read twice withalpha and no intervening read. Thus the port-labelled charge is injective, for arbitrary initial color and multiplicity.',
'The supplied lower T0..10 interface forces Q=(-8,1) S-departure ordinal2 -> W-arrival ordinal1 through three literal L helper ranks. Capacity gives lambda>=1, excluding only its proposed lambda0 count-pump extension. No universal eta-lambda sign follows.',
'All named internal physical ordinal matches/full voltages and complete chains were rebuilt independently. Necessary rank-clock constraints pass at the stated large test period; this is NOT a distinct-phase clock model or physical factor. Visible returns4 ->4,8 ->none become18 cross-cell chains, with79 events and97 total endpoint distances, maximum36. No actual growth8 trajectory with disappearing debt is claimed.',
'The sharp preparedRLLLL control clears its entire3-black input. The staircase8n first-return family has four disjoint stair interiors for n>=2, distinct pre-return reads,4n-2 initial BLACK and4n+1 final BLACK after endpointL. Each inter-side intersection is a shared endpoint only; the final origin is the unique repeat. Complete supplied n2,3,5,20 boards replay.',
'Unbounded prepared factor clock span cannot imply arbitrary WHITE growth8 completion. Existing stronger short-return density theorems remain attributed; solver UNKNOWN and discovery3109 counts are not proof premises. No finite-state impossibility or monotone full weighted debt is proved.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
