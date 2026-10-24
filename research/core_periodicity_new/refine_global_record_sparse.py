"""Discovery-only deterministic patch refinement for OUT-normalized record models.
Prefer a literal contradiction inside a visible no-OUT block; else add a missing
input of the first packet that installs a retained token, ranked by target height.
Every stage regenerates the approved residual model; no extra guard is invented.
"""
import json,sys,subprocess
from pathlib import Path
from resource_profile import load_profile
profile,pot=map(Path,sys.argv[1:3]);target,phase,maxbits=map(int,sys.argv[3:6]);directory=Path(sys.argv[6]);directory.mkdir(exist_ok=True,parents=True)
P,D,M=load_profile(profile);G=D['geometry']['geometry'];K=set(map(tuple,D['geometry']['core']));v=json.loads(pot.read_text())['values'];points=set(map(tuple,G[target]['inputs']));history=[]
def rot(q,h):x,y=q;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def height(q):z=rot(q,phase);return v['ax']*z[0]+v['ay']*z[1]
def run(args,stdout):
 with open(stdout,'w')as f:return subprocess.run(list(map(str,args)),stdout=f,stderr=subprocess.STDOUT).returncode
for stage in range(maxbits):
 prefix=directory/f'round{stage:02}';patch=prefix.with_suffix('.patch.json');patch.write_text(json.dumps(sorted(points)));run(['python','generate_resource_global_record_residual.py',profile,pot,target,phase,prefix,'file:'+str(patch)],prefix.with_suffix('.generate.log'));out=directory/f'round{stage:02}_out';run(['python','normalize_global_record_initial_out.py',prefix.with_suffix('.json'),out],out.with_suffix('.generate.log'));run(['./protected_patch_bdd_labels_witness_v2',out.with_suffix('.dat'),750000,out.with_suffix('.bdd')],out.with_suffix('.log'));J=json.loads(out.with_suffix('.json').read_text());log=out.with_suffix('.log').read_text();status=[s for s in log.splitlines()if s.startswith('status')][-1];entry={'stage':stage,'n':len(points),'prefix':str(out),'status':status};history.append(entry);(directory/'summary.json').write_text(json.dumps(history,indent=2));print(json.dumps(entry),flush=True)
 if 'EXHAUSTED_NO_HIT'in status:
  run(['python','verify_protected_patch_bdd_labels.py',out.with_suffix('.dat'),out.with_suffix('.bdd')],out.with_suffix('.verify.json'));break
 if 'ABSTRACT_WITNESS'not in status or len(points)>=maxbits:break
 path=[tuple(map(int,s.split()[1:]))for s in log.splitlines()if s.startswith('WITNESS')];known={};conflicts=[];choices=[]
 for step,(sid,mask,a)in enumerate(path):
  if a==99:known={};continue
  if a<0:continue
  x,y,h=J['poses'][sid]
  def absolute(q):z=rot(q,h);return x+z[0],y+z[1]
  oldcore=set(map(absolute,K));req={absolute(r[:2]):bool(r[2])for r in G[a]['requirements']}
  for q,b in req.items():
   if q in known and known[q]!=b and q not in points:conflicts.append((step,q))
  known.update(req)
  for q in map(absolute,G[a]['raw_odd']):known[q]=not known[q]
  outs=set(map(absolute,G[a]['outputs']));ins=set(map(absolute,G[a]['inputs']));missing=ins-points
  if outs&points and missing:choices.append((step,sorted(missing,key=lambda q:(-height(q),abs(q[0])+abs(q[1]),q))))
 if conflicts:q=min(conflicts)[1];reason={'kind':'literal visible-block conflict','step':min(conflicts)[0],'cell':q}
 elif choices:q=choices[0][1][0];reason={'kind':'missing input of earliest visible retained producer','step':choices[0][0],'cell':q}
 else:
  entry['stop']='No selected omitted input/conflict';(directory/'summary.json').write_text(json.dumps(history,indent=2));break
 entry['refinement']=reason;points.add(q);(directory/'summary.json').write_text(json.dumps(history,indent=2))
