"""Independent two-signature quotient and clean-epoch Boolean relation audit."""
from pathlib import Path
from collections import defaultdict
import json,sys,subprocess
from check_dcuv_producer_model_independent import check as exact_check,resolve_file,digest,relation,geometry,ordinary,protected,rotation,xy,ROOT
OUT=ROOT/'audits/dcuv_scoped_replays';OUT.mkdir(exist_ok=True)
TRUST={'macro_words':'23d4a8ed66eb91599c91c8b3e501cd22271e1a9806d4487713085f3eee318fd2','geometry':'7fdb41445719db8328b02113af7d44879398d8b0aea7b17319253994df1bea06','ordinary':'51979b66632b81c04b1dd9dbcfa85bf6a6f759db953252e32040ba4605d80146','protected':'395d31eb25954760bbf42520398eb18f510ab97fbee085da683fc9d6374f71ce','signed_extra':'c4585979213b8f6bdec63aee6daec119ab16226bce6a9d5401a3ae5968d994e4'}
def check(path):
 path=Path(path).resolve();J=json.loads(path.read_text());assert J['format']=='guarded_xor_reset_scoped_producer_quotient_v1'
 resolve=lambda x:resolve_file(path,x)
 xp=resolve(J['exact_label_model_file']);assert digest(xp)==J['exact_label_model_sha256'];exact_check(xp,False);X=json.loads(xp.read_text())
 bp=resolve(J['base_model_file']);assert digest(bp)==J['base_model_sha256'];B=json.loads(bp.read_text())
 for key in ['points','poses','out','reentry','keep','source','target','target_pose','protected_q','resource_profile_file','resource_profile_sha256','base_n','base_model_file','base_model_sha256','candidate_hypothesis_file','candidate_hypothesis_sha256','candidate_hypotheses','extra_guard_file','extra_guard_sha256']:assert J[key]==X[key],key
 hp=resolve(J['candidate_hypothesis_file']);ep=resolve(J['extra_guard_file']);assert digest(hp)==J['candidate_hypothesis_sha256']and digest(ep)==J['extra_guard_sha256']
 H=relation(hp);E=relation(ep);assert not E and H=={tuple(r)for r in J['candidate_hypotheses']}
 sp=resolve(J['scope_specification_file']);assert digest(sp)==J['scope_specification_sha256'];spec=json.loads(sp.read_text());assert spec['keep']==J['scope_packet_types']==[0,1,4,5,6]
 assert J['scope_start_out_forgets'] is True and J['scope_near_to_out_forgets'] is True
 assert set(spec['files'])==set(TRUST)
 for key,h in TRUST.items():assert spec['files'][key]['sha256']==h==digest(Path(spec['files'][key]['path']))
 sf=relation(Path(spec['files']['ordinary']['path']),5);ss=relation(Path(spec['files']['protected']['path']))|relation(Path(spec['files']['signed_extra']['path']));allowed=set(spec['keep'])
 labels=J['producer_label_classes'];assert len(labels)==len(X['producer_labels']);n=B['n'];start=B['start'].copy();sign_checks=0
 for L,exact in zip(labels,X['producer_labels']):
  assert L['cell']==exact['cell']and L['exact_codes']==exact['codes'];codes=L['exact_codes'];maps=L['exact_codes_to_class'];classes=L['classes'];q=complex(*L['cell'])
  assert len(maps)==len(codes)and maps[0]==0 and L['outer_class']==maps[exact['outer_code']]
  bits=(len(classes)-1).bit_length();assert L['bits']==bits and L['offset']==n
  start[1]|=((1<<bits)-1)<<n;start[2]|=L['outer_class']<<n;n+=bits
  sigs=[]
  for lab in codes:
   full=[];scoped=[]
   if lab is not None:
    p0=complex(*lab['pose'][:2]);h0=lab['heading'];a0=lab['packet'];slot=geometry[a0]['outputs'][lab['slot']]
    for ti,(sid,to,k,v,f,goal,a)in enumerate(B['transitions']):
     x,y,h=B['poses'][sid];p=complex(x,y)
     if rotation(q-p,-h)not in geometry[a]['inputs']:continue
     row=(a0,a,*xy(rotation(p-p0,-h0)),(h-h0)%4,*xy(slot))
     if row[:5]in ordinary or row in protected or(row in H and(not goal or not lab['outer_origin'])):full.append(ti)
     if a0 in allowed and a in allowed and(row[:5]in sf or row in ss):scoped.append(ti)
     sign_checks+=1
   sigs.append((full,scoped))
  for ci,cl in enumerate(classes):
   ids=[i for i,m in enumerate(maps)if m==ci];assert ids
   assert cl['members']==[codes[i]for i in ids]
   for i in ids:assert sigs[i]==(cl['rejected_transitions'],cl['scoped_rejected_transitions'])and bool(codes[i]and codes[i]['outer_origin'])==cl['outer_origin']
  assert not classes[0]['rejected_transitions']and not classes[0]['scoped_rejected_transitions']
 for L in labels:
  assert L['scope_offset']==n;start[1]|=1<<n
  if L['outer_class']and B['source']in allowed and B['start'][0]!=B['out']:start[2]|=1<<n
  n+=1
 assert n==J['n']and n<63 and start==J['start'];color=(1<<B['n'])-1
 grouped=defaultdict(list)
 for sid,to,k,v,f,rm,rv,goal,a in J['transitions']:
  assert not((k|v|f|rm|rv)>>n)and not(v&~k)and not(rv&~rm)
  grouped[(sid,to,k&color,v&color,f,goal,a)].append((k&~color,v&~color,rm,rv))
 assert set(grouped)=={tuple(t)for t in B['transitions']};cube_checks=0;retirements=installs=0
 for ti,base in enumerate(B['transitions']):
  sid,to,k,v,f,goal,a=base;x,y,h=B['poses'][sid];p=complex(x,y);rm=rv=0;allowed_count=1;badsets=[]
  for L in labels:
   q=complex(*L['cell']);z=rotation(q-p,-h);bits=L['bits'];off=L['offset'];sb=1<<L['scope_offset'];mask=((1<<bits)-1)<<off
   bad={i for i,c in enumerate(L['classes'])if ti in c['rejected_transitions']};scoped={i for i,c in enumerate(L['classes'])if ti in c['scoped_rejected_transitions']};badsets.append((bad,scoped))
   allowed_count*=2*(1<<bits)-len(bad)-len(bad|scoped)
   if z in geometry[a]['context']:rm|=mask
   if a not in allowed or to==B['out']or z in geometry[a]['context']:rm|=sb;retirements+=1
   if z in geometry[a]['outputs']:
    desc={'packet':a,'slot':geometry[a]['outputs'].index(z),'heading':h,'pose':[x,y,h],'outer_origin':False};code=L['exact_codes'].index(desc);rm|=mask|sb;rv|=L['exact_codes_to_class'][code]<<off
    if a in allowed and to!=B['out']:rv|=sb
    installs+=1
  cubes=grouped[tuple(base)];total=0
  for cm,cv,reset,value in cubes:
   assert(reset,value)==(rm,rv)
   for L,(bad,scoped)in zip(labels,badsets):
    off=L['offset'];bits=L['bits'];lm=(cm>>off)&((1<<bits)-1);lv=(cv>>off)&((1<<bits)-1);sb=1<<L['scope_offset']
    assert all(code&lm!=lv for code in bad)
    if not(cm&sb)or(cv&sb):assert all(code&lm!=lv for code in scoped)
   total+=1<<(n-B['n']-cm.bit_count());cube_checks+=1
  for i,(m,v,_,_)in enumerate(cubes):
   for m2,v2,_,_ in cubes[:i]:assert(v^v2)&m&m2
  assert total==allowed_count
 lines=[f"{n} {B['out']+1} {len(J['transitions'])} {len(B['reentry'])}",' '.join(map(str,start))]+[' '.join(map(str,t))for t in J['transitions']]+[' '.join(map(str,B['reentry']))]
 assert path.with_suffix('.dat').read_text()=='\n'.join(lines)+'\n'
 result={'status':'PASS independent clean-epoch scoped quotient semantics; no new transfer exclusion','model':str(path.relative_to(ROOT)),'initial_OUT':start[0]==B['out'],'scope_initial_values':[(start[2]>>L['scope_offset'])&1 for L in labels],'variables':n,'watched_cells':len(labels),'signature_queries':sign_checks,'guard_cubes':cube_checks,'scope_retirements':retirements,'output_installs':installs,'hashes':{str(p.relative_to(ROOT)):digest(p)for p in[path,path.with_suffix('.dat'),bp,xp,hp,sp]}}
 if path.with_suffix('.bdd').exists():
  dest=OUT/(path.stem+'.invariant.json');subprocess.run([str(ROOT/'audits/check_guarded_reset_bdd64_invariant_independent'),str(path.with_suffix('.dat')),str(path.with_suffix('.bdd')),str(dest)],check=True);result['invariant']=json.loads(dest.read_text())
 (OUT/(path.stem+'.model_check.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
 return result
if __name__=='__main__':
 for arg in sys.argv[1:]:check(arg)
