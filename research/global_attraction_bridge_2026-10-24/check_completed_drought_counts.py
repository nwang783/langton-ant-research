"""Exact event projection, all-parameter finite-family counts, and full-field literal controls."""
from pathlib import Path
import json,hashlib
from derive_record_projection import model184,model394,model16,project_affine,add,mul
from record_event_projection import project,stats,load,dot
from check_return_permanent_output_debt import future,DXY
P=Path(__file__).parent;U=P.parent/'causal_reduction/unit_scale'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def ev(a,n):return a[0]*n+a[1]
def collapse(r):
 n0=r['domain_start'];events=[];tail=[]
 for st in r['stages']:
  T=tuple(st['start']);pp=st['period']
  for i,a in st['first']:events.append(dict(time=add(T,(0,i)),normal=a,stage=st['stage']))
  for z in st['rays']:
   tm=add(add(T,mul(tuple(z['lo']),pp)),(0,z['phase']))
   if z['hi']is None:tail.append(dict(first_time=tm,normal=z['normal'],phase=z['phase'],first_epoch=z['lo'],period=pp))
   else:
    assert add(tuple(z['hi']),mul(tuple(z['lo']),-1))==(0,1)
    events.append(dict(time=tm,normal=z['normal'],stage=st['stage']))
 events.sort(key=lambda z:ev(z['time'],n0));tail.sort(key=lambda z:ev(z['first_time'],n0));assert tail
 for a,b in zip(events,events[1:]):
  v=add(b['time'],mul(a['time'],-1));assert v[0]>=0 and ev(v,n0)>0
 for z in tail:
  v=add(z['first_time'],mul(tail[0]['first_time'],-1));assert v[0]>=0 and ev(v,n0)>=0
 times=[e['time']for e in events]+[tail[0]['first_time']]
 gaps=[add(b,mul(a,-1))for a,b in zip(times,times[1:])]
 assert all(z['period']==104 for z in tail)
 return dict(finite_events=events,tail_rays=tail,all_pre_tail_completed_gaps=gaps,tail_internal_gap_upper=104,
  exact_count_for_any_H_ge104='sum of indicators gap(parameter)>H over all_pre_tail_completed_gaps; initial waiting excluded')

def physical(name,seed,p,h,stages):
 B=set(seed);head0=p;h0=h;M=[max(dot(q,a)for q in B|{p})for a in range(4)];records=[];t=0;snap=[]
 for stage,w,C in stages:
  if C is None:tail=w;break
  for _ in range(C):
   for c in w:
    for a in range(4):
     z=dot(p,a)
     if z>M[a]:assert z==M[a]+1;records.append([t,a]);M[a]=z
    assert(p in B)==(c=='L'),(name,t,p,c)
    B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=(p[0]+DXY[h][0],p[1]+DXY[h][1]);t+=1
  snap.append(dict(stage=stage,cut=t,pose=[p,h],full_mass=len(B),full_field_sha256=sha_field(B)))
 # Keep the exact complete field. Every phase/ray initial-hit transition is checked.
 tw,dr,_,tests=future({q:i for i,q in enumerate(sorted(B))},p,h);assert tw==tail
 terminal=(set(B),p,h,t)
 # Follow only a bounded number of tail reads. Earlier huge-parameter proof is symbolic.
 for _ in range(208):
  for a in range(4):
   z=dot(p,a)
   if z>M[a]:assert z==M[a]+1;records.append([t,a]);M[a]=z
  c=tail[(t-terminal[3])%104];assert(p in B)==(c=='L');B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=(p[0]+DXY[h][0],p[1]+DXY[h][1]);t+=1
 reg=project(set(seed),head0,h0,stages);pred=[]
 for r in reg:
  upper=(t-r['start']-1)//r['period']+1
  if r['hi']is not None:upper=min(upper,r['hi'])
  for k in range(r['lo'],max(r['lo'],upper)):
   pred.extend([r['start']+k*r['period']+i,a]for i,a in r['phases']if r['start']+k*r['period']+i<t)
 assert pred==records,(name,pred,records)
 return dict(name=name,physical_updates=t,initial_black=sorted(seed),initial_pose=[head0,h0],record_cuts=records,
  stage_full_field_checks=snap,terminal_cut=terminal[3],terminal_pose=[terminal[1],terminal[2]],terminal_full_black=sorted(terminal[0]),
  tail_word=tw,tail_drift=dr,infinite_parity_tests=tests,event_regions=reg,long_gap104=stats(reg,104),long_gap3390=stats(reg,3390))
def sha_field(B):return hashlib.sha256(json.dumps(sorted(B),separators=(',',':')).encode()).hexdigest()
def spec(model,n):
 seed={(ev(q[0],n),ev(q[1],n))for q in model['seed']};p=tuple(ev(q,n)for q in model['pose']);st=[(name,w,None if C is None else ev(C,n))for name,w,C in model['stages']];return seed,p,model['heading'],st

models=[model184(),model394(),model16()];proofs=[]
for m in models:
 r=project_affine(m);r['record_inventory']=collapse(r);proofs.append(r)
 expected={'184':[(0,14),(0,1615),(0,14),(5824,20959),(0,14),(0,1213),(0,90),(0,14),(13940,94279)],
 '394':[(0,90),(0,14),(0,1721),(0,14),(32448,84966),(0,10),(0,1609),(77052,349745)],
 '16':[(728,-209),(208,-291),(0,14),(936,7756)]}
 assert r['record_inventory']['all_pre_tail_completed_gaps']==expected[m['name']]
controls=[]
for n in (1,2,3,4,10):controls.append(physical(f'184_N{n}',*load('prepared1564_uniform_support_manifest.json',n)));print(controls[-1]['name'],'reads',controls[-1]['physical_updates'],flush=True)
for n in (1,2):controls.append(physical(f'394_M{n}',*load('prepared4352_capture_manifest.json',n)));print(controls[-1]['name'],'reads',controls[-1]['physical_updates'],flush=True)
for k in (10,20,40):controls.append(physical(f'16_n{2*k}',*spec(models[2],k)));print(controls[-1]['name'],'reads',controls[-1]['physical_updates'],flush=True)
# Two already signed finite concatenations: no all-parameter extension is assumed.
D=json.load(open(P/'TWO_TRANSVERSE_MODULES_CHECKED.json'));m=models[2];A=m['stages'][0][1];W=m['stages'][1][1];F=m['stages'][-2][1]
concat=[]
for c in D['controls']:
 n,J=c['n2'],c['spacing_periods'];st0=spec(m,10)[3][:-2];st1=spec(m,n//2)[3][1:-2]
 st=st0+[('first_recovery',F,1),('interflight',W,J)]+st1+[('second_recovery',F,1),('tail',W,None)]
 v=physical(f'28_n20_n{n}',set(map(tuple,c['initial_black'])),(0,0),1,st)
 assert v['long_gap104']['count']==3
 old=controls[7]['initial_black'] # 16_n20 follows five184 and two394 controls.
 assert controls[7]['name']=='16_n20'
 old=set(map(tuple,old));new=set(map(tuple,c['initial_black']));assert old<new
 added=new-old;old_hull=[max(dot(q,a)for q in old)for a in range(4)];new_hull=[max(dot(q,a)for q in new)for a in range(4)]
 # Whole prefix words are fixed by the signed two-module control; only record qualification changes.
 lost=[];kept=[];p=(0,0);h=1;oldM=old_hull[:];newM=new_hull[:];t=0
 for _,w,C in st0:
  for _ in range(C):
   for ch in w:
    for a in range(4):
     z=dot(p,a)
     if z>oldM[a]:
      assert z==oldM[a]+1;entry=dict(cut=t,normal=a,pose=p,new_initial_bound=new_hull[a]);(kept if z>newM[a]else lost).append(entry);oldM[a]=z
     newM[a]=max(newM[a],z)
    h=(h+(1 if ch=='R'else-1))%4;p=(p[0]+DXY[h][0],p[1]+DXY[h][1]);t+=1
 assert[(z['cut'],z['normal'])for z in lost]==[(3,2),(7074,1)]
 assert[(z['cut'],z['normal'])for z in kept]==[(8863,0),(8877,0)]
 v['prefix_hull_mask']=dict(old_initial_hull=old_hull,new_initial_hull=new_hull,added_cells=sorted(added),removed_record_events=lost,retained_record_events=kept)
 concat.append(v);print(v['name'],'reads',v['physical_updates'],flush=True)
# Explicit huge parameters use geometry only, never fine replay or field expansion.
huge=[]
for model in models:
 n=10**9;v=project(*spec(model,n));s=stats(v,104);expected_count=4 if model['name']in('184','394') else 3;assert s['count']==expected_count
 huge.append(dict(name=model['name'],parameter=n,event_regions=v,gaps=s))
files=['derive_record_projection.py','record_event_projection.py','check_return_permanent_output_debt.py',
 '../causal_reduction/unit_scale/prepared1564_uniform_support_manifest.json','../causal_reduction/unit_scale/prepared1564_source_endpoint_family.json',
 '../audits/check_1564_constant_mass_family_independent.json','../audits/check_1564_family_endpoint_capture_independent.json',
 '../causal_reduction/unit_scale/prepared4352_capture_manifest.json','../audits/check_4352_allM_capture_independent.json',
 'TRANSVERSE_FAR_MODULE_MANIFEST.json','TRANSVERSE_FAR_MODULE_SOURCE.json','../audits/check_transverse_far_module_independent.json',
 'TWO_TRANSVERSE_MODULES_MANIFEST.json','TWO_TRANSVERSE_MODULES_CHECKED.json','../audits/check_two_transverse_modules_independent.json',
 'MT_COMPLETED_DROUGHT_INVENTORY_MANIFEST.json','../audits/check_MT_completed_drought_inventory_independent.json']
files += ['../causal_reduction/unit_scale/prepared1564_endpoint_N%d.json'%n for n in(1,2,3,4)]
for f in files:assert(P/f).exists(),f
out=dict(status='AUTHOR exact event-projection theorem and family inventory; independent audit pending',source_hashes={f:sha(P/f)for f in files},
 all_parameter_proofs=proofs,full_field_controls=controls,paid_concatenations=concat,huge_parameter_geometry_controls=huge,
 total_physical_updates=sum(c['physical_updates']for c in controls+concat),
 scope='Complete augmented-initial-seed/head hull union records in four AXIAL normals. Initial wait is not a completed gap. Family counts are exact; no universal mass-only bound, no arbitrary concatenation theorem, no global record-clock occurrence.')
(P/'COMPLETED_DROUGHT_COUNTS_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
print('TOTAL',out['total_physical_updates'],flush=True)
