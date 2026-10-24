"""Independent semantics audit for individual freshness and joint U fuel.
Exact guard cubes are checked by allowed-value sets, disjointness and counts.
No closed mutual family or transfer exclusion is inferred from a model check.
"""
from pathlib import Path
from collections import defaultdict
from math import prod
import json,sys,subprocess
from check_dcuv_producer_model_independent import base_check,resolve_file,digest,relation,geometry,ordinary,protected,rotation,xy,ROOT
OUT=ROOT/'audits/dcuv_fused_replays';OUT.mkdir(exist_ok=True)
UPPER={-1+4j,2j,3j}
def check(path):
 path=Path(path).resolve();J=json.loads(path.read_text());joint=J['format']=='guarded_reset_fused_joint_upper_fuel_v1';assert joint or J['format']=='guarded_reset_fused_upper_freshness_v1'
 bp=resolve_file(path,J['base_model_file']);assert digest(bp)==J['base_model_sha256'];B=json.loads(bp.read_text());base_check(bp)
 for f in ['points','poses','out','reentry','keep','source','target','target_pose','protected_q','resource_profile_file','resource_profile_sha256']:assert B[f]==J[f],f
 hp=resolve_file(path,J['candidate_hypothesis_file']);assert digest(hp)==J['candidate_hypothesis_sha256'];H=relation(hp);assert H==set(map(tuple,J['candidate_hypotheses']))
 targets=set(B['keep'])&{7,8,9};needed=set()
 for a in B['keep']:
  for q in geometry[a]['outputs']:
   for b in targets:
    assert UPPER<=geometry[b]['inputs']
    for z in UPPER:
     for h in range(4):
      p=q-rotation(z,h);r=(a,b,*xy(p),h,*xy(q))
      if (sum(xy(p))+h)%2==0 and r[:5]not in ordinary and r not in protected:needed.add(r)
 assert needed<=H and needed==set(map(tuple,J['required_full_family']))
 assert J['upper_target_types']==sorted(targets)and J['upper_inputs']==sorted([list(xy(z))for z in UPPER])
 assert J['origin_encoding']=={'white':0,'black_unknown':1,'black_outer':2,'black_internal':3}
 cells=J['origin_cells'];assert len(cells)==len(B['points']);n=0;start=[B['start'][0],0,0]
 for i,c in enumerate(cells):
  assert c['cell']==B['points'][i]and c['old_color_bit']==i and c['offset']==n and c['bits']in(1,2)and c['watched']==(c['bits']==2)
  width=c['bits'];mask=(1<<width)-1;known=B['start'][1]>>i&1;bit=B['start'][2]>>i&1
  if width==1:
   if known:start[1]|=1<<n;start[2]|=bit<<n
  elif complex(*c['cell'])in geometry[B['source']]['outputs']:
   assert known and bit;start[1]|=3<<n;start[2]|=2<<n
  else:
   start[1]|=2<<n
   if known:start[1]|=1<<n;start[2]|=bit<<n
  n+=width
 assert J['n']==n and J['start']==start
 grouped=defaultdict(list)
 for sid,to,k,v,f,rm,rv,goal,a in J['transitions']:
  assert not((k|v|f|rm|rv)>>n)and not(v&~k)and not(rv&~rm)
  grouped[sid,to,goal,a].append((k,v,f,rm,rv))
 assert set(grouped)=={(s,t,g,a)for s,t,k,v,f,g,a in B['transitions']}
 cubes_checked=0
 for sid,to,k,v,f,goal,a in B['transitions']:
  pos=complex(*B['poses'][sid][:2]);h=B['poses'][sid][2];choices=[];upperids=[];flip=rm=rv=0
  for i,c in enumerate(cells):
   width=c['bits'];off=c['offset'];mask=(1<<width)-1;touch=k>>i&1;bit=v>>i&1;z=rotation(complex(*c['cell'])-pos,-h)
   if width==1:
    choices.append({bit}if touch else{0,1})
    if f>>i&1:flip|=1<<off
    continue
   if z in UPPER and a in targets:upperids.append(i)
   if not touch:
    assert not(f>>i&1);choices.append({0,1,2,3});continue
   allowed={0}if not bit else{1,2,3}
   if not joint and a in targets and z in UPPER:
    assert bit;allowed={1,2}if goal else{1}
   choices.append(allowed);rm|=3<<off
   final=3 if z in geometry[a]['outputs']else bit^(f>>i&1);rv|=final<<off
  active_joint=joint and len(upperids)==3
  if joint and goal:assert active_joint
  expected=prod(map(len,choices))
  if active_joint:
   knowncount=prod(len(s&{2,3})if i in upperids else len(s)for i,s in enumerate(choices))
   expected=knowncount if goal else expected-knowncount
  cubes=grouped[sid,to,goal,a];volume=0
  for cm,cv,actualflip,reset,value in cubes:
   assert (actualflip,reset,value)==(flip,rm,rv)
   cubechoices=[]
   for c,allowed in zip(cells,choices):
    off=c['offset'];mask=(1<<c['bits'])-1;localmask=cm>>off&mask;localvalue=cv>>off&mask
    vals={z for z in range(1<<c['bits'])if z&localmask==localvalue};assert vals<=allowed;cubechoices.append(vals)
   if active_joint:
    if goal:assert all(cubechoices[i]<={2,3}for i in upperids)
    else:assert any(not(cubechoices[i]&{2,3})for i in upperids)
   volume+=1<<(n-cm.bit_count());cubes_checked+=1
  for i,(cm,cv,*_)in enumerate(cubes):
   for m2,v2,*_ in cubes[:i]:assert (cv^v2)&cm&m2
  assert volume==expected
 lines=[f"{n} {B['out']+1} {len(J['transitions'])} {len(B['reentry'])}",' '.join(map(str,start))]+[' '.join(map(str,t))for t in J['transitions']]+[' '.join(map(str,B['reentry']))]
 assert path.with_suffix('.dat').read_text()=='\n'.join(lines)+'\n'
 targetq=rotation(complex(*B['protected_q'])-complex(*B['target_pose'][:2]),-B['target_pose'][2])
 out=dict(status='PASS conditional fused origin model, not a closed family',semantics='joint all-three-produced event'if joint else'individual upper-input freshness',keep=B['keep'],variables=n,required_family=len(needed),guard_cubes=cubes_checked,anchor_is_upper_input=targetq in UPPER,hashes={str(p.relative_to(ROOT)):digest(p)for p in[path,path.with_suffix('.dat'),bp,hp]})
 if path.with_suffix('.bdd').exists():
  dest=OUT/(path.stem+'.invariant.json');subprocess.run([str(ROOT/'audits/check_guarded_reset_bdd64_invariant_independent'),str(path.with_suffix('.dat')),str(path.with_suffix('.bdd')),str(dest)],check=True);out['invariant']=json.loads(dest.read_text())
 (OUT/(path.stem+'.model_check.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out));return out
if __name__=='__main__':
 for arg in sys.argv[1:]:check(arg)
