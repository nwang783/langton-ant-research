"""Produce and independently check monotone RUP certificates for all 1,280 cases."""
import json,gzip,hashlib,subprocess,time,collections
from cnf_inflation_refinement import HERE,prove
O=next(z['images']for z in json.load(open(HERE/'free_inflations_k9.json'))['results']if z['scale']==[3,0]);words=O['R']+O['L'];outdir=HERE/'k9_rup';outdir.mkdir(exist_ok=True);results=[];start=time.time()
canon=lambda a:tuple(sorted(set(a)))
for index,line in enumerate(open(HERE/'free_nine_coarse81_prefixes.csv')):
 ids=list(map(int,line.split(',')));fixed=[words[i]for i in ids];r=prove(''.join(fixed),fixed,O,'working');assert r['status']=='unsat',r
 cnf=open(r['cnf']).read();known=set()
 for s in cnf.splitlines():
  if s and s[0]not in'pc':known.add(canon(map(int,s.split()[:-1])))
 compact=[]
 for s in open(r['proof']):
  p=s.split()
  if not p or p[0]=='d':continue
  if p[0]=='i':p=p[1:]
  assert p[-1]=='0';a=list(map(int,p[:-1]));key=canon(a)
  if key not in known:compact.append(' '.join(map(str,a))+' 0\n'if a else'0\n');known.add(key)
 proof=''.join(compact);assert compact and compact[-1]=='0\n'
 path=HERE/'k9_drat'/'working.rup';path.write_text(proof)
 check=subprocess.run([str(HERE/'check_drat'),r['cnf'],str(path)],capture_output=True,text=True);assert check.returncode==0,(index,check.stdout,check.stderr)
 v=json.loads(check.stdout);assert v['valid']and v['RAT']==0 and v['deletions']==0
 for ext,data in [('cnf',cnf),('rup',proof)]:
  with gzip.open(outdir/f'case{index:04d}.{ext}.gz','wb')as f:f.write(data.encode())
 record=dict(index=index,initial_choices=ids,variables=r['variables'],clauses=r['clauses'],cnf_sha256=hashlib.sha256(cnf.encode()).hexdigest(),rup_sha256=hashlib.sha256(proof.encode()).hexdigest(),checker=v,solve_seconds=r['seconds']);results.append(record)
 if index%50==0:print(index,'VALID',v['RUP'],round(time.time()-start,2),flush=True)
 (outdir/'manifest.partial.json').write_text(json.dumps(results,indent=2))
assert len(results)==1280
summary=dict(status='ALL_1280_MONOTONE_RUP_CERTIFICATES_VERIFIED',cases=len(results),total_additions=sum(r['checker']['additions']for r in results),max_additions=max(r['checker']['additions']for r in results),seconds=time.time()-start,results=results)
(outdir/'manifest.json').write_text(json.dumps(summary,indent=2));print(json.dumps({k:v for k,v in summary.items()if k!='results'},indent=2))
