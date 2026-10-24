"""Position-only k8 critical-area exclusion: explicit CNF and monotone RUP proofs."""
import json,gzip,hashlib,subprocess,time
from position_only_refinement import build,HERE
source=json.load(open(HERE/'position_only_prefixes_k8_a2_2.json'))
assert source['status']=='COMPLETE' and source['prefix_count']==2784
outdir=HERE/'position_k8_rup';outdir.mkdir(exist_ok=True);results=[];start=time.time()
cnfpath=outdir/'working.cnf';proofpath=outdir/'working.rup'
for index,prefix in enumerate(source['prefixes']):
 names,clauses,_,_=build(8,(2,2),prefix['word'],prefix['choices'])
 cnf=f'p cnf {len(names)} {len(clauses)}\n'+''.join(' '.join(map(str,c))+' 0\n' for c in clauses)
 cnfpath.write_text(cnf)
 producer=subprocess.run([str(HERE/'prove_cnf_rup'),str(cnfpath),str(proofpath),'100000'],capture_output=True,text=True)
 assert producer.returncode==0 and producer.stdout.startswith('UNSAT '),(index,producer.stdout,producer.stderr)
 proof=proofpath.read_text();assert proof.splitlines()[-1]=='0'
 check=subprocess.run([str(HERE/'check_drat'),str(cnfpath),str(proofpath)],capture_output=True,text=True)
 assert check.returncode==0,(index,check.stdout,check.stderr)
 v=json.loads(check.stdout);assert v['valid'] and v['RAT']==0 and v['deletions']==0
 for ext,data in [('cnf',cnf),('rup',proof)]:
  with gzip.open(outdir/f'case{index:04d}.{ext}.gz','wb') as f:f.write(data.encode())
 results.append(dict(index=index,initial_choices=prefix['choices'],variables=len(names),clauses=len(clauses),cnf_sha256=hashlib.sha256(cnf.encode()).hexdigest(),rup_sha256=hashlib.sha256(proof.encode()).hexdigest(),checker=v,producer=producer.stdout.strip()))
 if index%50==0:
  print(index,'VALID',v['RUP'],round(time.time()-start,2),flush=True)
  (outdir/'manifest.partial.json').write_text(json.dumps(results,indent=2))
assert len(results)==2784
summary=dict(status='ALL_2784_MONOTONE_RUP_CERTIFICATES_VERIFIED',k=8,scale=[2,2],heading_preservation=False,cases=len(results),total_additions=sum(r['checker']['additions'] for r in results),max_additions=max(r['checker']['additions'] for r in results),seconds=time.time()-start,results=results)
(outdir/'manifest.json').write_text(json.dumps(summary,indent=2));print(json.dumps({k:v for k,v in summary.items() if k!='results'},indent=2))
