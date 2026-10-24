"""No external SAT engine: explicit CNF, plain proof search, separate RUP checking."""
import json,gzip,hashlib,subprocess,time
from cnf_inflation_refinement import HERE,cnf_refinement
O=next(z['images']for z in json.load(open(HERE/'free_inflations_k9.json'))['results']if z['scale']==[3,0]);words=O['R']+O['L'];outdir=HERE/'k9_rup';outdir.mkdir(exist_ok=True);results=[];start=time.time()
cnfpath=HERE/'k9_drat'/'plain_working.cnf';proofpath=HERE/'k9_drat'/'plain_working.rup'
for index,line in enumerate(open(HERE/'free_nine_coarse81_prefixes.csv')):
 ids=list(map(int,line.split(',')));fixed=[words[i]for i in ids];names,clauses=cnf_refinement(''.join(fixed),fixed,O)
 cnf=f'p cnf {len(names)} {len(clauses)}\n'+''.join(' '.join(map(str,c))+' 0\n'for c in clauses)
 cnfpath.write_text(cnf)
 producer=subprocess.run([str(HERE/'prove_cnf_rup'),str(cnfpath),str(proofpath),'100000'],capture_output=True,text=True)
 assert producer.returncode==0 and producer.stdout.startswith('UNSAT '),(index,producer.stdout,producer.stderr)
 proof=proofpath.read_text();assert proof.splitlines()[-1]=='0'
 check=subprocess.run([str(HERE/'check_drat'),str(cnfpath),str(proofpath)],capture_output=True,text=True);assert check.returncode==0,(index,check.stdout,check.stderr)
 v=json.loads(check.stdout);assert v['valid']and v['RAT']==0 and v['deletions']==0
 for ext,data in [('cnf',cnf),('rup',proof)]:
  with gzip.open(outdir/f'case{index:04d}.{ext}.gz','wb')as f:f.write(data.encode())
 record=dict(index=index,initial_choices=ids,variables=len(names),clauses=len(clauses),cnf_sha256=hashlib.sha256(cnf.encode()).hexdigest(),rup_sha256=hashlib.sha256(proof.encode()).hexdigest(),checker=v,producer=producer.stdout.strip());results.append(record)
 if index%50==0:print(index,'VALID',v['RUP'],round(time.time()-start,2),flush=True)
 (outdir/'manifest.partial.json').write_text(json.dumps(results,indent=2))
assert len(results)==1280
summary=dict(status='ALL_1280_MONOTONE_RUP_CERTIFICATES_VERIFIED',producer='plain first-UIP CDCL, no preprocessing/minimization',cases=len(results),total_additions=sum(r['checker']['additions']for r in results),max_additions=max(r['checker']['additions']for r in results),seconds=time.time()-start,results=results)
(outdir/'manifest.json').write_text(json.dumps(summary,indent=2));print(json.dumps({k:v for k,v in summary.items()if k!='results'},indent=2))
