"""All SAME-SECTOR translations of one fixed short-refinement scaffold.
The finite list is derived from complete possible-read support, not a radius.
Outside it every selected read is on initially white profile classes.
"""
from pathlib import Path
import json,hashlib,subprocess,time
import certify_short_refinement_rup as C
P=Path(__file__).resolve().parent;O=P/'reverse_short_all_translations';O.mkdir(exist_ok=True)
rev=''.join('L'if c=='R'else'R'for c in C.H[::-1]);_,_,groups=C.cnf(rev,(-1,0),C.wake,nontrivial=False)
placements=set()
for a in groups:
 for b in C.wake:
  normal=b[0]-a[0];tx=(b[1]-a[1])%2
  if normal%2:placements.add((tx,tx-normal))
placements=sorted(placements)
results=[]
for index,tr in enumerate(placements+[None]):
 start=(-1+tr[0],tr[1])if tr is not None else(0,0);inp=C.wake if tr is not None else set()
 names,clauses,g=C.cnf(rev,start,inp,nontrivial=False);text=f'p cnf {len(names)} {len(clauses)}\n'+''.join(' '.join(map(str,c))+' 0\n'for c in clauses)
 a=O/f'case{index:02d}.cnf';b=O/f'case{index:02d}.rup';a.write_text(text);t=time.monotonic()
 r=subprocess.run([str(C.HERE/'prove_cnf_rup'),str(a),str(b),'100000'],capture_output=True,text=True,timeout=120)
 z=dict(index=index,translation=tr,case='overlap'if tr else'all-white-outside',variables=len(names),clauses=len(clauses),producer=r.stdout.strip(),returncode=r.returncode,seconds=time.monotonic()-t)
 if r.returncode==0:
  s=subprocess.run([str(C.HERE/'check_drat'),str(a),str(b)],capture_output=True,text=True,timeout=120);assert s.returncode==0,(s.stdout,s.stderr);v=json.loads(s.stdout);assert v['valid']and v['RAT']==0 and v['deletions']==0;z['checker']=v
 z.update(cnf_sha256=hashlib.sha256(a.read_bytes()).hexdigest(),rup_sha256=hashlib.sha256(b.read_bytes()).hexdigest());results.append(z)
 (O/'manifest.partial.json').write_text(json.dumps(results,indent=2)+'\n');print(z,flush=True)
out=dict(scope=__doc__,base_read_orbits=sorted(groups),wake_black_orbits=sorted(C.wake),placements=placements,results=results,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),cnf_source_sha256=hashlib.sha256(Path(C.__file__).read_bytes()).hexdigest())
(O/'manifest.json').write_text(json.dumps(out,indent=2)+'\n')
