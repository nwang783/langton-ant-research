"""Greedy orbit-constraint deletion for the frozen one-bit-deficit Q interface.
This reduces a certificate; it does not enlarge the architecture.
"""
from pathlib import Path
import json,time,subprocess,hashlib
import certify_short_refinement_rup as core
import synthesize_multirail_short_refinement as s
P=Path(__file__).resolve().parent;O=P/'q_self_rewrite';s.O=O
Q=json.loads((P/'forward108_prepared_control.json').read_text())['word'];B=set(map(tuple,json.loads((P/'forward108_self_interfaces.json').read_text())['source_output']))
_,_,gr=core.cnf(Q,(0,14),B,nontrivial=False);cur=set(gr);log=[]
for a in sorted(gr):
 names,C,_=core.cnf(Q,(0,14),B,nontrivial=False,only=cur-{a});out,_=s.z3solve(names,C,'reduce_probe',timeout=10000);log.append(dict(removed=a,status=out['result']))
 if out['result']=='UNSAT_ARCHITECTURE':cur.remove(a)
names,C,_=core.cnf(Q,(0,14),B,nontrivial=False,only=cur);cn=O/'local_core.cnf';rp=O/'local_core.rup';cn.write_text(s.dimacs(names,C));r=subprocess.run([str(core.HERE/'prove_cnf_rup'),str(cn),str(rp),'100000'],capture_output=True,text=True,timeout=120);assert r.returncode==0,r.stdout
v=subprocess.run([str(core.HERE/'check_drat'),str(cn),str(rp)],capture_output=True,text=True,timeout=120);assert v.returncode==0,v.stdout
out=dict(scope=__doc__,orbits=sorted(cur),variables=len(names),clauses=len(C),checker=json.loads(v.stdout),log=log,cnf_sha256=hashlib.sha256(cn.read_bytes()).hexdigest(),rup_sha256=hashlib.sha256(rp.read_bytes()).hexdigest())
(O/'local_core.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='log'})
