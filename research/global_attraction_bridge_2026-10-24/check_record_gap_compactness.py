"""Exact long next-record waits and a nonreturning pristine local limit; no one-orbit counterexample."""
from pathlib import Path
import json,hashlib
from check_return_permanent_output_debt import DXY,future
from certified_comparison_perturbation import geometry
P=Path(__file__).parent;R=json.loads((P/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());A=json.loads((P/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());K=set(map(tuple,R['canonical_source']));W=R['W'];qm=(202,201);tm=10413;r=8470;remote=set(map(tuple,A['exact_entry_pruning']['remote']));NW=A['controls'][0]['complete_future_certificate']['tail_word']
def run(seed,p,h,word,cuts=()):
 B={q:-i-1 for i,q in enumerate(sorted(seed))};death={};snap={};records=[];maxy=p[1]
 for t,c in enumerate(word):
  if p[1]>maxy:records.append(t);maxy=p[1]
  if t in cuts:snap[t]=(dict(B),p,h,maxy)
  old=B.pop(p,None);assert(c=='L')==(old is not None)
  if old is None:B[p]=t;h=(h+1)%4
  else:death[old]=t;h=(h-1)%4
  p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
 fw,dr,dead,tests=future(B,p,h);death.update({i:len(word)+tt for i,tt in dead.items()});return dict(B=B,p=p,h=h,death=death,snap=snap,records=records,maxy=maxy,tail_word=fw,drift=dr,tests=tests)
pure=run(set(map(tuple,A['T_kernel'])),(0,0),0,A['T_recovery'],[r]);b,p,h,my=pure['snap'][r];assert(p,h)==((3,33),0)and pure['records'][-1]==r and pure['maxy']==33
local={q for q,i in b.items()if i in pure['death']};limitseed={(x-3,y-33)for x,y in local};limit=run(limitseed,(0,0),0,A['T_recovery'][r:]);tq,_,_,_=geometry(limit['p'],limit['h'],limit['tail_word']);assert all(-i-1 in limit['death']for i in range(len(limitseed)))
assert limit['maxy']==0 and max(y for x,y in tq)<=0 and limit['drift'][1]<0 and all(y<0 for x,y in limitseed)
# Exact first next-N record along the full final NW ray stream.
Q,H,_,_=geometry((155,215),1,NW);hits=[]
for i,(x,y)in enumerate(Q):
 if(263-y)%2==0:
  c=(263-y)//2;assert 100+c>=0;hits.append(dict(phase=i,period_offset=c,time_offset=104*c+i,phase_point=(x,y),heading=H[i]))
hits.sort(key=lambda x:x['time_offset']);assert hits[0]==dict(phase=43,period_offset=22,time_offset=2331,phase_point=(158,219),heading=0)
# Exact normalized FULL record-limit field:104 backward rays XOR a fixed finite mask.
WQ,_,_,_=geometry((0,0),1,W);treads,_,_,_=geometry((0,0),0,A['T_recovery']);fixed={(2*a,2*a)for a in[0,1,3,5,6]}
for q in treads[:r]:fixed.symmetric_difference_update({q})
anchors=[]
for i,q in enumerate(WQ):
 u=0 if i<13 else-1;anchors.append((q[0]-2+2*u-3,q[1]-1+2*u-33))
fixed_norm={(x-3,y-33)for x,y in fixed};assert max(y for x,y in anchors+list(fixed_norm))<0
def limit_color(z):
 v=z in fixed_norm
 for a in anchors:
  dx=z[0]-a[0];dy=z[1]-a[1]
  if dx==dy and dx<=0 and dx%2==0:v=not v
 return v
controls=[]
for n in[100,137,500]:
 qt=(qm[0]+2*n+28,qm[1]+2*n+28);seed=K|{(qm[0]+2*a,qm[1]+2*a)for a in[0,1,6,8]}|{(qt[0]+2*a,qt[1]+2*a)for a in[0,1,3,5,6]}
 pre=W*100+W[:13]+R['modes']['M']['recovery_word']+(W[41:]+W[:41])*n+(W[41:]+W[:41])[:76];tT=len(pre);last=tT+r
 cert=pre+A['T_recovery']+A['T_tail_word']*(n-7)+A['T_tail_word'][:100]+'L'+A['postcollision_word'];assert len(cert)==80270+208*n
 nextcut=len(cert)+104*(n+22)+43;word=cert+NW*(n+22)+NW[:43];assert len(word)==nextcut==82601+312*n and nextcut-last==52930+208*n
 z=run(seed,(0,0),1,word,[last]);B,p,h,my=z['snap'][last];assert(p,h)==((qt[0]+3,qt[1]+33),0)and max(y for x,y in B)<p[1]
 assert z['records'][-1]==last and(z['p'],z['h'])==((114-2*n,263+2*n),0)and z['maxy']==z['p'][1]-1
 assert all(i>=0 for i in B.values())and max(y for x,y in seed)<p[1]
 normalized_full={(x-p[0],y-p[1])for x,y in B};box_checks=0
 for xx in range(-40,41):
  for yy in range(-40,41):
   assert((xx,yy)in normalized_full)==limit_color((xx,yy));box_checks+=1
 C={q for q,i in B.items()if i in z['death']};assert C=={(qt[0]+x,qt[1]+y)for x,y in local}|remote
 rho=max(max(abs(x-p[0]),abs(y-p[1]))for x,y in C);assert rho==2*n+100
 assert not any(y>=z['p'][1]for x,y in z['B'])
 _,_,tail_inputs,_=future(z['B'],z['p'],z['h']);nextC={q for q,i in z['B'].items()if i in tail_inputs};next_rho=max(max(abs(x-z['p'][0]),abs(y-z['p'][1]))for x,y in nextC);assert len(nextC)==13 and next_rho==5 and z['tail_word']==W[14:]+W[:14]
 controls.append(dict(n=n,seed=sorted(seed),T_contact=tT,last_N_record_cut=last,last_N_pose=[p,h],whole_last_N_black=[[q,i]for q,i in sorted(B.items())],entire_last_N_pruning=sorted(C),last_pruning_mass=len(C),last_rho=rho,full_limit_box_checks=box_checks,full_limit_agreement_above_y=-2*n-30,next_N_record_cut=nextcut,record_gap=nextcut-last,next_pose=[z['p'],z['h']],whole_next_black=sorted(z['B']),next_entire_pruning=sorted(nextC),next_rho=next_rho,tail_word=z['tail_word'],tail_drift=z['drift'],infinite_parity_tests=z['tests']))
 print(n,'gap',nextcut-last,'oldC',len(C),'rho',rho,'nextC',len(nextC),'nextRho',next_rho,flush=True)
files=['SOUTHWEST_ARCHIVE_IMPORT_MANIFEST.json','../audits/check_southwest_archive_import_independent.json','PRISTINE_RECORD_AFTER_RETIREMENT_MANIFEST.json','../audits/check_pristine_record_after_retirement_independent.json','../audits/relevant_radius_recurrence_bridge_2026-10-24_1018.md','check_return_permanent_output_debt.py']
for f in files:assert(P/f).exists(),f
out=dict(status='AUTHOR record-gap compactness theorem/control; independent audit pending',scope='Bounded record gaps in one direction imply translation; across-family unbounded waits do not give one nontranslating orbit.',source_hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in files},last_N_relative_cut=r,last_N_relative_pose=[[3,33],0],local_pruning=sorted(local),local_population=len(local),entire_population=len(local)+786,limit=dict(seed=sorted(limitseed),pose=[[0,0],0],finite_prefix=A['T_recovery'][r:],complete_output_black=sorted(limit['B']),output_pose=[limit['p'],limit['h']],tail_word=limit['tail_word'],tail_drift=limit['drift'],parity_tests=limit['tests'],maximum_future_N_coordinate=0),full_record_limit=dict(backward_ray_anchors=anchors,step=(-2,-2),ray_domain='all integer k>=0, XOR all104 rays',finite_XOR_mask=sorted(fixed_norm),all_black_strictly_below_record=True,all_n_field_difference_support='normalized y<=-2n-30'),all_next_N_phase_equations=hits,controls=controls)
(P/'RECORD_GAP_COMPACTNESS_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
