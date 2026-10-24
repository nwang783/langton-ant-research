"""Exact first-contact rays for the signed inward record limit, retaining full fields."""
from pathlib import Path
import hashlib,json
from certified_comparison_perturbation import reference,first_hit,perturbation_event,geometry
from check_return_permanent_output_debt import DXY
P=Path(__file__).parent;src=json.loads((P/'RECORD_GAP_COMPACTNESS_CHECKED.json').read_text());j=src['limit'];K=set(map(tuple,j['seed']));ref=reference(K,(0,0),0,j['finite_prefix'],j['tail_word']);Q=ref['Q'];dx,dy=ref['dr'];assert (dx,dy)==(-2,-2)
def multiple(v):
 x,y=v
 return x//dx if x%dx==0 and y==(x//dx)*dy else None
phases=[];threshold=0
for i,q in enumerate(Q):
 earlier=[]
 for a,v in enumerate(Q):
  m=multiple((q[0]-v[0],q[1]-v[1]))
  if m is not None and 104*m+a<i:earlier.append((a,m))
 if earlier:
  a,m=max(earlier,key=lambda x:x[1]);threshold=max(threshold,-m)
  phases.append(dict(phase=i,stable_first_visit=False,earlier_phase=a,earlier_period_offset=m))
 else:
  finite_hits=[]
  for v in set(ref['P'])|K:
   k=multiple((v[0]-q[0],v[1]-q[1]))
   if k is not None and k>=0:finite_hits.append(k)
  bound=max(finite_hits,default=-1)+1;threshold=max(threshold,bound)
  assert ref['word'][i]=='R'
  phases.append(dict(phase=i,stable_first_visit=True,finite_prefix_seed_last_period=max(finite_hits,default=None),ray_anchor=q,normal_depth_offset=-q[1],delay_depth_constant=ref['L']+i+52*q[1]))
good=[p for p in phases if p['stable_first_visit']];assert len(good)==22
# Algebraic branch witnesses plus positive finite tests on both sides of the threshold.
for k in range(threshold,threshold+4):
 for i,q in enumerate(Q):
  z=(q[0]+k*dx,q[1]+k*dy);hit=first_hit(ref,{z});assert hit is not None
  assert (hit[0]==ref['L']+104*k+i)==phases[i]['stable_first_visit']
cyclic=[]
for shift in range(104):
 w=ref['word'][shift:]+ref['word'][:shift];qq,_,end,eh=geometry((0,0),1,w);dd=end;assert abs(dd[0])==abs(dd[1])==2 and eh==1
 novel=[];fringe_bound=0
 for i,q in enumerate(qq):
  isnew=True
  for a,v in enumerate(qq):
   x=q[0]-v[0];y=q[1]-v[1]
   if x%dd[0]==0 and y==(x//dd[0])*dd[1] and 104*(x//dd[0])+a<i:
    isnew=False;fringe_bound=max(fringe_bound,-(x//dd[0]));break
  if isnew:novel.append(i);assert w[i]=='R'
 assert len(novel)==22
 seen=set();required=[]
 for k in range(fringe_bound+1):
  for i,q in enumerate(qq):
   z=(q[0]+k*dd[0],q[1]+k*dd[1])
   if z not in seen and w[i]=='L':required.append(z)
   seen.add(z)
 assert 11<=len(required)<=22
 cyclic.append(dict(shift=shift,drift=dd,stable_first_visit_phases=novel,finite_fringe_period_bound=fringe_bound,required_initial_black=required))
controls=[]
for c in src['controls']:
 n=c['n'];p,h=c['last_N_pose'];B={(q[0]-p[0],q[1]-p[1]):ident for q,ident in c['whole_last_N_black']};assert K<=set(B)
 extra=set(B)-K;event=perturbation_event(ref,extra);assert event['kind']=='EXACT first original-extra collision';t=event['time'];q=tuple(event['cell']);assert(t,q)==(104*n+2134,(-2*n-27,-2*n-33))
 per,phase=divmod(t-ref['L'],104);assert (per,phase)==(n-7,100);depth=-q[1];assert t==52*depth+418
 # Full physical replay through the mismatch; all reference turns before it agree.
 full=dict(B);head=(0,0);heading=0;trace=ref['prefix']+ref['word']*per+ref['word'][:phase]
 assert len(trace)==t
 for s,ch in enumerate(trace):
  old=full.pop(head,None);assert(ch=='L')==(old is not None)
  if old is None:full[head]=10**12+s;heading=(heading+1)%4
  else:heading=(heading-1)%4
  head=(head[0]+DXY[heading][0],head[1]+DXY[heading][1])
 assert head==q and heading==event['incoming_heading'] and full[q]==20165 and B[q]==20165
 assert c['last_N_record_cut']+t==10413+21392+208*n
 age=c['last_N_record_cut']+t-B[q];assert age==208*n+11640 and age>=53*depth+418
 controls.append(dict(n=n,full_record_black_mass=len(B),extra_mass=len(extra),first_contact_delay=t,cell=q,normal_depth=depth,tail_phase=phase,tail_period=per,old_record_lifetime_birth=B[q],consumption_age=age,age_geometric_lower_bound=53*depth+418,physical_prefix_reads=t))
files=['RECORD_GAP_COMPACTNESS_MANIFEST.json','certified_comparison_perturbation.py','PHASE13_DOUBLE_SCATTER_MANIFEST.json','../audits/check_phase13_double_scatter_independent.json']
for f in files:assert(P/f).exists(),f
out=dict(status='AUTHOR frozen candidate; independent audit pending',scope='Conditional canonical trapped record-limit geometry; not occurrence or renewal obstruction',source_hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in files},prefix_length=ref['L'],tail_word=ref['word'],tail_drift=ref['dr'],stable_threshold=threshold,stable_first_visit_phase_count=len(good),all_104_phase_witnesses=phases,all_cyclic_first_visit_inventories=cyclic,controls=controls)
(P/'RECORD_LIMIT_RAY_DEPENDENCY_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
print('stable phases',len(good),'threshold',threshold,'full-prefix reads',sum(c['physical_prefix_reads']for c in controls))
