"""Discovery-only sparse record refinement with height/heading far packet walks.
Every far packet retains DFA history. Refine visible conflicts first, then a missing residual
input on the backward ancestry slice of the actual abstract goal inputs.
"""
from pathlib import Path
import sys,json,subprocess
R=Path(__file__).resolve().parents[1];B=R/'core_periodicity_new';D=B/'chronology_dcuv';sys.path.insert(0,str(B));from resource_profile import load_profile
profile,pot,dfa=map(Path,sys.argv[1:4]);target,phase,maxbits=map(int,sys.argv[4:7]);directory=Path(sys.argv[7]);directory.mkdir(exist_ok=True,parents=True);P,data,M=load_profile(profile);G=data['geometry']['geometry'];v=json.loads(pot.read_text())['values'];points=set(map(tuple,G[target]['inputs']));history=[]
def rot(q,h):x,y=q;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def height(q):z=rot(q,phase);return v['ax']*z[0]+v['ay']*z[1]
def run(cmd,output):
 with open(output,'w')as f:return subprocess.run(list(map(str,cmd)),stdout=f,stderr=subprocess.STDOUT).returncode
for stage in range(maxbits):
 pre=directory/f'round{stage:02}';patch=pre.with_suffix('.patch.json');patch.write_text(json.dumps(sorted(points)));out=directory/f'round{stage:02}_out';prod=directory/f'round{stage:02}_height';live=prod
 cmds=[['python',B/'generate_resource_global_record_residual.py',profile,pot,target,phase,pre,'file:'+str(patch)],['python',B/'normalize_global_record_initial_out.py',pre.with_suffix('.json'),out],['python',B/'refine_global_record_far_height.py',out.with_suffix('.json'),dfa,prod]]
 for i,cmd in enumerate(cmds):assert run(cmd,str(pre)+f'.generate{i}.log')==0
 run([B/'guarded_reset_bdd_backward_witness',live.with_suffix('.dat'),750000,live.with_suffix('.bdd')],live.with_suffix('.log'));J=json.loads(out.with_suffix('.json').read_text());PJ=json.loads(prod.with_suffix('.json').read_text());LJ=json.loads(live.with_suffix('.json').read_text());log=live.with_suffix('.log').read_text();status=[x for x in log.splitlines()if x.startswith('status')][-1];method='BDD'
 if 'CAP'in status and (LJ['out']+1)*(1<<J['n'])<=300000000:
  run([B/'guarded_reset_dense',live.with_suffix('.dat'),300000000],live.with_suffix('.dense.log'));log=live.with_suffix('.dense.log').read_text();status=[x for x in log.splitlines()if x.startswith('status')][-1];method='dense'
 entry={'stage':stage,'n':len(points),'prefix':str(live),'status':status,'method':method};history.append(entry);(directory/'summary.json').write_text(json.dumps(history,indent=2)+'\n');print(json.dumps(entry),flush=True)
 if 'EXHAUSTED_NO_HIT'in status:
  if method=='BDD':run(['python',B/'verify_protected_patch_bdd_labels.py',live.with_suffix('.dat'),live.with_suffix('.bdd')],live.with_suffix('.verified.json'))
  break
 if 'ABSTRACT_WITNESS'not in status or len(points)>=maxbits:break
 rawpath=[tuple(map(int,x.split()[1:]))for x in log.splitlines()if x.startswith('WITNESS')];path=[]
 for sid,mask,a in rawpath:
  bp,c=PJ['position_map'][sid];pose=PJ['poses'][sid]
  path.append({'pose':pose,'packet':a,'base_pose_id':bp,'mask':mask})
 pre.with_suffix('.witness.json').write_text(json.dumps(path,indent=2)+'\n');known={};labels={};records={};conflicts=[]
 for step,row in enumerate(path):
  a=row['packet'];p=row['pose']
  if p is None or a==99:known={};continue
  x,y,h=p
  def at(q):z=rot(q,h);return x+z[0],y+z[1]
  req={at(q[:2]):bool(q[2])for q in G[a]['requirements']}
  for q,b in req.items():
   if q in known and known[q]!=b and q not in points:conflicts.append((step,q))
  known.update(req)
  for q in map(at,G[a]['raw_odd']):known[q]=not known[q]
  inp=set(map(at,G[a]['inputs']));outputs=set(map(at,G[a]['outputs']));records[step]={'inputs':[(q,labels.get(q))for q in sorted(inp)],'outputs':sorted(outputs),'packet':a}
  for q in list(labels):
   if q in req:del labels[q]
  for q in outputs&points:labels[q]=step
 goal=max(records);needed={goal};stack=[goal];missing=[]
 while stack:
  s=stack.pop()
  for q,parent in records[s]['inputs']:
   if q not in points:missing.append((s,q))
   elif parent is not None and parent not in needed:needed.add(parent);stack.append(parent)
 if conflicts:s,q=min(conflicts);reason={'kind':'visible-block literal conflict','step':s,'cell':q}
 elif missing:
  s,q=min(missing,key=lambda z:(z[0],-height(z[1]),abs(z[1][0])+abs(z[1][1]),z[1]));reason={'kind':'missing input in goal ancestry','step':s,'cell':q}
 else:entry['stop']='No omitted visible conflict or goal-ancestry input';(directory/'summary.json').write_text(json.dumps(history,indent=2)+'\n');break
 entry['refinement']=reason;points.add(q);(directory/'summary.json').write_text(json.dumps(history,indent=2)+'\n')
