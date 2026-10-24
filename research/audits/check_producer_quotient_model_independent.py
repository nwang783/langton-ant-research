"""Independent literal geometry and exact partition audit of producer quotients.

This checks conditional model soundness, NOT closure of its hypothesis family.
It does not import either author producer-label implementation.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib,sys,subprocess
from check_protected_patch_model_independent import main as base_check,walk,raws,mark,rotation,xy
ROOT=Path(__file__).resolve().parents[1];W=ROOT/'word_stabilization';OUT=ROOT/'audits/producer_quotient_replays';OUT.mkdir(exist_ok=True)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def relation(p,width=7):return {tuple(map(int,l.split()[:width])) for l in p.read_text().splitlines()}
core={z for z,b in walk(mark)[2].items()if b};geometry=[]
for raw in raws:
 end,h,_,flip=walk(raw);context=walk(raw+mark)[2];entry={z for z,b in context.items()if b}
 geometry.append({'inputs':entry-core,'outputs':sorted((entry^flip)-{end+rotation(z,h)for z in core},key=xy),'context':set(context)})
resource=json.loads((W/'dcv_residual_core_resources.json').read_text())['geometry']
for a,g in enumerate(geometry):
 assert resource[a]['inputs']==[list(xy(p))for p in sorted(g['inputs'],key=xy)]
 assert resource[a]['outputs']==[list(xy(p))for p in g['outputs']]
ordinary=relation(W/'seven_sub_dcv_star4_kernel.tsv',5)
protected=relation(W/'dcv_protected_patch2_kernel.tsv')
assert digest(W/'seven_sub_dcv_star4_kernel.tsv')=='51979b66632b81c04b1dd9dbcfa85bf6a6f759db953252e32040ba4605d80146'
assert digest(W/'dcv_protected_patch2_kernel.tsv')=='395d31eb25954760bbf42520398eb18f510ab97fbee085da683fc9d6374f71ce'
signed_path=W/'dcv_companion_closed_family.tsv'
assert digest(signed_path)=='8da1a5e5fc5c1162c1938890c836602ffd7ea4fa8d91831d0510425bcc16368e'
signed=relation(signed_path)
def check(path,verify_invariant=True):
 path=path.resolve();J=json.loads(path.read_text());exact=J.get('format')=='guarded_xor_reset_v1';resolve=lambda z:Path(z)if Path(z).is_absolute()else(path.parent/str(z)).resolve();bp=resolve(J['base_model_file']);B=json.loads(bp.read_text());base_check(bp)
 if exact:
  J['producer_label_classes']=[dict(cell=L['cell'],offset=L['offset'],bits=L['bits'],classes=[{'members':[lab],'rejected_transitions':None,'outer_origin':bool(lab and lab['outer_origin'])}for lab in L['codes']],outer_class=L['outer_code'],exact_codes_to_class=list(range(len(L['codes']))),exact_codes=L['codes'])for L in J['producer_labels']]
 assert J['base_model_sha256']==digest(bp) and J['base_n']==B['n']
 for field in ['points','poses','out','reentry','keep','source','target','target_pose','protected_q']:assert J[field]==B[field],field
 hp=resolve(J['candidate_hypothesis_file']);ep=resolve(J['extra_guard_file']);xp=path if exact else resolve(J['exact_label_model_file'])
 assert J['candidate_hypothesis_sha256']==digest(hp) and J['extra_guard_sha256']==digest(ep) and(exact or J['exact_label_model_sha256']==digest(xp))
 H=relation(hp);E=relation(ep);assert E<=signed and H=={tuple(r)for r in J['candidate_hypotheses']}
 S=protected|E;n=B['n'];color=(1<<n)-1;start=B['start'].copy();labels=J['producer_label_classes'];cells=[]
 for L in labels:
  q=complex(*L['cell']);assert L['cell']in B['points'] and q not in cells;cells.append(q)
  expected=[None]
  for a in B['keep']:
   for slot,z in enumerate(geometry[a]['outputs']):
    for h in range(4):
     p=q-rotation(z,h)
     if(sum(xy(p))+h)%2==0:expected.append({'packet':a,'slot':slot,'heading':h,'pose':[*xy(p),h],'outer_origin':False})
  outer=0
  if q in geometry[B['source']]['outputs']:
   outer=len(expected);expected.append({'packet':B['source'],'slot':geometry[B['source']]['outputs'].index(q),'heading':0,'pose':[0,0,0],'outer_origin':True})
  assert L['exact_codes']==expected
  classes=L['classes'];maps=L['exact_codes_to_class'];assert len(maps)==len(expected) and maps[0]==0 and L['outer_class']==maps[outer]
  assert L['offset']==n and L['bits']==(len(classes)-1).bit_length()
  bits=L['bits'];start[1]|=((1<<bits)-1)<<n;start[2]|=maps[outer]<<n;n+=bits
  signatures=[]
  for lab in expected:
   sig=[]
   if lab is not None:
    origin=complex(*lab['pose'][:2]);h0=lab['heading'];a0=lab['packet'];outcell=geometry[a0]['outputs'][lab['slot']]
    for ti,(sid,to,k,v,f,goal,a) in enumerate(B['transitions']):
     x,y,h=B['poses'][sid];p=complex(x,y)
     if rotation(q-p,-h)not in geometry[a]['inputs']:continue
     row=(a0,a,*xy(rotation(p-origin,-h0)),(h-h0)%4,*xy(outcell))
     if row[:5]in ordinary or row in S or(row in H and(not goal or not lab['outer_origin'])):sig.append(ti)
   signatures.append(sig)
  for ci,cl in enumerate(classes):
   indices=[i for i,m in enumerate(maps)if m==ci];assert indices
   assert cl['members']==[expected[i]for i in indices]
   if exact:cl['rejected_transitions']=signatures[indices[0]]
   assert all(signatures[i]==cl['rejected_transitions']for i in indices)
   assert all(bool(expected[i]and expected[i]['outer_origin'])==cl['outer_origin']for i in indices)
  assert classes[0]['rejected_transitions']==[]
 assert n==J['n'] and start==J['start'] and n<63
 # Each source transition is independently partitioned into disjoint guard cubes.
 # Subset and cardinality checks avoid copying the author's recursive partitioner.
 grouped=defaultdict(list)
 for sid,to,k,v,f,rm,rv,goal,a in J['transitions']:
  assert not((k|v|f|rm|rv)>>n) and v&~k==0 and rv&~rm==0
  grouped[(sid,to,k&color,v&color,f,goal,a)].append((k&~color,v&~color,rm,rv))
 assert len({tuple(t)for t in B['transitions']})==len(B['transitions'])
 assert set(grouped)=={tuple(t)for t in B['transitions']}
 cube_checks=0
 for ti,base in enumerate(B['transitions']):
  sid,to,k,v,f,goal,a=base;x,y,h=B['poses'][sid];p=complex(x,y);rm=rv=0;allowed_count=1;bad_lists=[]
  for L in labels:
   q=complex(*L['cell']);z=rotation(q-p,-h);off=L['offset'];bits=L['bits'];mask=((1<<bits)-1)<<off
   bad={i for i,c in enumerate(L['classes'])if ti in c['rejected_transitions']};bad_lists.append(bad);allowed_count*=(1<<bits)-len(bad)
   if z in geometry[a]['context']:rm|=mask
   if z in geometry[a]['outputs']:
    lab={'packet':a,'slot':geometry[a]['outputs'].index(z),'heading':h,'pose':[x,y,h],'outer_origin':False}
    code=L['exact_codes'].index(lab);rm|=mask;rv|=L['exact_codes_to_class'][code]<<off
  cubes=grouped[tuple(base)];total=0
  for m,val,reset,value in cubes:
   assert (reset,value)==(rm,rv)
   for L,bad in zip(labels,bad_lists):
    bits=L['bits'];off=L['offset'];lm=(m>>off)&((1<<bits)-1);lv=(val>>off)&((1<<bits)-1)
    assert all(code&lm!=lv for code in bad)
   total+=1<<(n-B['n']-m.bit_count());cube_checks+=1
  for i,(m,v,_,_)in enumerate(cubes):
   for m2,v2,_,_ in cubes[:i]:assert (v^v2)&m&m2
  assert total==allowed_count
 lines=[f"{n} {J['out']+1} {len(J['transitions'])} {len(J['reentry'])}",' '.join(map(str,start))]+[' '.join(map(str,t))for t in J['transitions']]+[' '.join(map(str,J['reentry']))]
 assert path.with_suffix('.dat').read_text()=='\n'.join(lines)+'\n'
 result={'status':'PASS conditional producer-quotient semantics; hypothesis closure NOT asserted','model':str(path.relative_to(ROOT)),'hypotheses':len(H),'watched_cells':len(labels),'variables':n,'base_transitions':len(B['transitions']),'guard_cubes':cube_checks,'sha256':{str(p.relative_to(ROOT)):digest(p)for p in [path,path.with_suffix('.dat'),bp,hp,ep,xp]}}
 if verify_invariant and path.with_suffix('.bdd').exists():
  dest=OUT/(path.stem+'.invariant.json');subprocess.run([str(ROOT/'audits/check_guarded_reset_bdd64_invariant_independent'),str(path.with_suffix('.dat')),str(path.with_suffix('.bdd')),str(dest)],check=True)
  result['invariant']=json.loads(dest.read_text());result['sha256'][str(path.with_suffix('.bdd').relative_to(ROOT))]=digest(path.with_suffix('.bdd'))
 (OUT/(path.stem+'.model_check.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
 return result
if __name__=='__main__':
 for arg in sys.argv[1:]:check(Path(arg))
