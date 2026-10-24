"""Fixed derived Q108-output to opposite-Q108 exact-pose1/5/9 rewrite interface.
One fixed geometry, unchanged certified image palette. SAT is a prepared bulk
operator only: producer Q itself needs prepared input and no cap is supplied.
"""
from pathlib import Path
import json,collections,subprocess,time,hashlib
import certify_short_refinement_rup as core
import synthesize_multirail_short_refinement as s
P=Path(__file__).resolve().parent;O=P/'q_self_rewrite';O.mkdir(exist_ok=True);s.O=O
Q=json.loads((P/'forward108_prepared_control.json').read_text())['word']
B=set(map(tuple,json.loads((P/'forward108_self_interfaces.json').read_text())['source_output']))
names,C,groups=core.cnf(Q,(0,14),B,nontrivial=False)
cnf=O/'self_rewrite.cnf';cnf.write_text(s.dimacs(names,C));out,model=s.z3solve(names,C,'self_rewrite')
out.update(scope=__doc__,variables=len(names),clauses=len(C),start=[0,14,3],drift=[-2,-2],input_black_classes=sorted(B),scaffold=Q,local_images=core.dom,possible_read_orbits=sorted(groups))
if model:
 images=[next(w for k,w in enumerate(core.dom[c])if model[names[f'x{j}_{k}']])for j,c in enumerate(Q)];w=''.join(images);rr,e,h=core.trace(w,(0,14),3);assert(e,h)==((-2,12),3)
 by=collections.defaultdict(list)
 for t,(p,g,c)in enumerate(rr):by[p[0]-p[1],p[0]%2].append((t+len(w)*(p[0]//2),t,p,g,c))
 for a,ev in by.items():
  ev.sort();assert(ev[0][-1]=='L')==(a in B);assert all(x[-1]!=y[-1]for x,y in zip(ev,ev[1:]))
 out.update(images=images,word=w,length=len(w),charge=w.count('R')-w.count('L'),histories=[dict(orbit=a,events=ev)for a,ev in sorted(by.items())],output_black_classes=sorted(B^{a for a,ev in by.items()if len(ev)%2}),literal_orbit_replay=True)
elif out['result']=='UNSAT_ARCHITECTURE':
 rp=O/'self_rewrite.rup';t=time.monotonic();r=subprocess.run([str(core.HERE/'prove_cnf_rup'),str(cnf),str(rp),'100000'],capture_output=True,text=True,timeout=120);out.update(producer=r.stdout.strip(),producer_returncode=r.returncode,proof_seconds=time.monotonic()-t)
 if r.returncode==0:
  z=subprocess.run([str(core.HERE/'check_drat'),str(cnf),str(rp)],capture_output=True,text=True,timeout=120);assert z.returncode==0,(z.stdout,z.stderr);out['checker']=json.loads(z.stdout)
 out['rup_sha256']=hashlib.sha256(rp.read_bytes()).hexdigest()
out.update(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),cnf_sha256=hashlib.sha256(cnf.read_bytes()).hexdigest())
(O/'result.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in ['local_images','possible_read_orbits','scaffold','producer','images','word','histories']})
