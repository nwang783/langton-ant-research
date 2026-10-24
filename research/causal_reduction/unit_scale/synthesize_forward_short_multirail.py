"""Forward H exact-pose1/5/9 refinements on mature standard-rail bundles.
New input/direction interface, unchanged certified local palette and circuit.
Neither the earlier forward WHITE case nor inverse RAIL case implies this.
"""
from pathlib import Path
import json,hashlib,subprocess,time,collections
import synthesize_multirail_short_refinement as s
P=Path(__file__).resolve().parent;O=P/'forward_short_multirail';O.mkdir(exist_ok=True);s.O=O

def main():
 names,C,groups,rails,conflicts,inp=s.build(word=s.H,mode='rails')
 nonid=[names[f'x{j}_{k}'] for j,c in enumerate(s.H) for k in range(1,len(s.core.dom[c]))];C.append(nonid)
 cnf=O/'all_bundles.cnf';cnf.write_text(s.dimacs(names,C))
 manifest=dict(scope=__doc__,scaffold=s.H,start=[0,0,3],drift=[-2,-2],local_images=s.core.dom,variables=len(names),clauses=len(C),possible_read_orbits=sorted(groups),rails=[{**{k:v for k,v in r.items() if k not in ('read','black')},'read':sorted(r['read']),'black':sorted(r['black'])} for r in rails],rail_conflicts=conflicts)
 (O/'architecture.json').write_text(json.dumps(manifest,indent=2)+'\n')
 out,model=s.z3solve(names,C,'all_bundles',timeout=30000);out.update(variables=len(names),clauses=len(C),rail_candidates=len(rails),rail_conflicts=len(conflicts))
 if model:
  images=[next(w for k,w in enumerate(s.core.dom[c]) if model[names[f'x{j}_{k}']]) for j,c in enumerate(s.H)]
  word=''.join(images);rr,e,h=s.core.trace(word,(0,0),3);assert(e,h)==((-2,-2),3)
  hist=collections.defaultdict(list)
  for t,(q,g,c) in enumerate(rr):hist[s.key(q)].append((t+len(word)*(q[0]//2),t,q,g,c))
  sel=[i for i,r in enumerate(rails) if model[r['selector']]];B=set().union(*(rails[i]['black'] for i in sel)) if sel else set()
  for q,hs in hist.items():
   hs.sort();assert(hs[0][-1]=='L')==(q in B);assert all(a[-1]!=b[-1] for a,b in zip(hs,hs[1:]))
  out.update(images=images,word=word,length=len(word),charge=word.count('R')-word.count('L'),selected_rails=sel,input_black_classes=sorted(B),read_histories=[dict(orbit=q,events=hs) for q,hs in sorted(hist.items())],output_black_classes=sorted(B^{q for q,hs in hist.items() if len(hs)%2}))
 elif out['result']=='UNSAT_ARCHITECTURE':
  proof=O/'all_bundles.rup';t=time.monotonic();p=subprocess.run([str(s.core.HERE/'prove_cnf_rup'),str(cnf),str(proof),'100000'],capture_output=True,text=True,timeout=120)
  out.update(producer=p.stdout.strip(),producer_returncode=p.returncode,proof_seconds=time.monotonic()-t)
  if p.returncode==0:
   c=subprocess.run([str(s.core.HERE/'check_drat'),str(cnf),str(proof)],capture_output=True,text=True,timeout=120);assert c.returncode==0,(c.stdout,c.stderr);out['checker']=json.loads(c.stdout)
  out['rup_sha256']=hashlib.sha256(proof.read_bytes()).hexdigest()
 out.update(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),cnf_sha256=hashlib.sha256(cnf.read_bytes()).hexdigest())
 (O/'result.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ['images','read_histories','producer']},flush=True)
if __name__=='__main__':main()
