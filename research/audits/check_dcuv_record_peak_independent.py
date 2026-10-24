"""Literal strict-historical-record abstraction; no unproved hypotheses.
Rebuild geometric threshold and exact fused transition partitions independently.
"""
from pathlib import Path
from collections import defaultdict
from math import prod
import json,sys,subprocess
from check_dcuv_producer_model_independent import base_check,resolve_file,digest,geometry,rotation,xy,ROOT,walk,raws
OUT=ROOT/'audits/dcuv_record_replays';OUT.mkdir(exist_ok=True)
def check(path):
 path=Path(path).resolve();J=json.loads(path.read_text());assert J['format']=='guarded_reset_fused_record_peak_v1'
 bp=resolve_file(path,J['base_model_file']);assert digest(bp)==J['base_model_sha256'];B=json.loads(bp.read_text());base_check(bp)
 for f in ['points','poses','out','reentry','keep','source','target','target_pose','protected_q','resource_profile_file','resource_profile_sha256']:assert B[f]==J[f],f
 pp=resolve_file(path,J['potential_file']);assert digest(pp)==J['potential_sha256'];P=json.loads(pp.read_text());assert P['profile_sha256']==B['resource_profile_sha256'];weights=P['values'];phase=J['source_global_phase'];assert phase in range(4)
 L=lambda z:int(z.real*weights['ax']+z.imag*weights['ay'])
 core=lambda h:L(rotation(-1+1j,h))+weights[f'c{h%4}']
 def created(a,h):
  h%=4;end,dh,_,_=walk(raws[a]);return max([2*L(rotation(end,h))+core(h+dh)]+[2*L(rotation(z,h))+weights[f'w_{a}_{i}_{h}']for i,z in enumerate(geometry[a]['outputs'])])
 def peak(a,pos,h):return 2*L(rotation(pos,phase))+max(core(h+phase),created(a,h+phase))
 tp=complex(*B['target_pose'][:2]);th=B['target_pose'][2];dst=B['target'];threshold=2*L(rotation(tp,phase))+created(dst,th+phase);sp=peak(B['source'],0j,0)
 assert created(dst,th+phase)>core(th+phase)and sp<threshold
 assert J['record_threshold']==threshold and J['source_peak']==sp and J['core_offsets']==[core(h)for h in range(4)]
 assert J['created_peaks']==[[a,h,created(a,h)]for a in B['keep']for h in range(4)]
 watch={tp+rotation(z,th)for z in geometry[dst]['inputs']};assert watch and watch<=set(complex(*p)for p in B['points'])
 assert J['goal_input_cells']==sorted([list(xy(z))for z in watch])
 assert complex(*B['protected_q'])in watch and complex(*B['protected_q'])in geometry[B['source']]['outputs']
 assert J['origin_encoding']=={'white':0,'black_unknown':1,'black_known_produced':3}
 cells=J['origin_cells'];assert len(cells)==len(B['points']);n=0;start=[B['start'][0],0,0]
 for i,c in enumerate(cells):
  q=complex(*B['points'][i]);width=2 if q in watch else 1
  assert c==dict(cell=B['points'][i],old_color_bit=i,offset=n,bits=width,watched=width==2)
  known=B['start'][1]>>i&1;bit=B['start'][2]>>i&1
  if width==1:
   if known:start[1]|=1<<n;start[2]|=bit<<n
  elif q in geometry[B['source']]['outputs']:
   assert known and bit;start[1]|=3<<n;start[2]|=3<<n
  else:
   start[1]|=2<<n
   if known:start[1]|=1<<n;start[2]|=bit<<n
  n+=width
 assert J['n']==n and J['start']==start
 grouped=defaultdict(list)
 for sid,to,k,v,f,rm,rv,goal,a in J['transitions']:
  assert not((k|v|f|rm|rv)>>n)and not(v&~k)and not(rv&~rm)
  grouped[sid,to,goal,a].append((k,v,f,rm,rv))
 expectedkeys=set();filtered=[];cubes_checked=0
 for bi,(sid,to,k,v,f,goal,a)in enumerate(B['transitions']):
  pos=complex(*B['poses'][sid][:2]);h=B['poses'][sid][2]
  if not goal and peak(a,pos,h)>=threshold:filtered.append(bi);continue
  key=sid,to,goal,a;expectedkeys.add(key);choices=[];flip=rm=rv=0
  for i,c in enumerate(cells):
   width=c['bits'];off=c['offset'];touch=k>>i&1;bit=v>>i&1;z=rotation(complex(*c['cell'])-pos,-h)
   if width==1:
    choices.append({bit}if touch else{0,1})
    if f>>i&1:flip|=1<<off
   else:
    if not touch:assert not(f>>i&1);choices.append({0,1,2,3});continue
    allowed={0}if not bit else{1,3}
    if goal:assert bit and z in geometry[a]['inputs'];allowed={3}
    choices.append(allowed);rm|=3<<off;final=3 if z in geometry[a]['outputs']else bit^(f>>i&1);rv|=final<<off
  cubes=grouped[key];volume=0
  for cm,cv,actualflip,reset,value in cubes:
   assert(actualflip,reset,value)==(flip,rm,rv)
   for c,allowed in zip(cells,choices):
    off=c['offset'];mask=(1<<c['bits'])-1;localmask=cm>>off&mask;localvalue=cv>>off&mask
    vals={z for z in range(1<<c['bits'])if z&localmask==localvalue};assert vals<=allowed
   volume+=1<<(n-cm.bit_count());cubes_checked+=1
  for i,(cm,cv,*_)in enumerate(cubes):
   for m2,v2,*_ in cubes[:i]:assert (cv^v2)&cm&m2
  assert volume==prod(map(len,choices))
 assert set(grouped)==expectedkeys and J['geometrically_filtered_base_transition_indices']==filtered
 lines=[f"{n} {B['out']+1} {len(J['transitions'])} {len(B['reentry'])}",' '.join(map(str,start))]+[' '.join(map(str,t))for t in J['transitions']]+[' '.join(map(str,B['reentry']))]
 assert path.with_suffix('.dat').read_text()=='\n'.join(lines)+'\n'
 result=dict(status='PASS conditional strict-record event abstraction',source=B['source'],target=dst,target_pose=B['target_pose'],phase=phase,threshold=threshold,source_peak=sp,variables=n,guard_cubes=cubes_checked,filtered_strict_transitions=len(filtered),scope='Only the fixed-weight strict historical-record event under all stated conditioning. NOT an unconditional protected-transfer exclusion or a global potential proof.',hashes={str(p.relative_to(ROOT)):digest(p)for p in[path,path.with_suffix('.dat'),bp,pp]})
 if path.with_suffix('.bdd').exists():
  dest=OUT/(path.stem+'.invariant.json');subprocess.run([str(ROOT/'audits/check_guarded_reset_bdd64_invariant_independent'),str(path.with_suffix('.dat')),str(path.with_suffix('.bdd')),str(dest)],check=True);result['invariant']=json.loads(dest.read_text())
 (OUT/(path.stem+'.model_check.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result));return result
if __name__=='__main__':
 for p in sys.argv[1:]:check(p)
