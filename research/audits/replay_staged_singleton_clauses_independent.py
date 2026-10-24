"""Rebuild literal inputs and run the independent C++ clause verifier."""
from pathlib import Path
import json,subprocess,hashlib,time
R=Path(__file__).resolve().parents[1];P=R/'word_stabilization';A=R/'audits'
m=json.loads((P/'staged_two_cell_singletons_manifest.json').read_text())
for f,h in m['files'].items():assert hashlib.sha256((P/f).read_bytes()).hexdigest()==h,f
exe=A/'check_literal_spatial_clauses';src=exe.with_suffix('.cpp')
subprocess.run(['g++','-O3','-std=c++17',str(src),'-o',str(exe)],check=True)
records=[]
for label,suffs in [('lrrlrrrrlrl',['','_residual0','_residual0_residual0']),('rrrlrllrrrr',['','_residual0'])]:
 for suff in suffs:
  t=time.time();stem='direct_mono_'+label+'_history4_scc0_context2'+suff
  qfile=P/(stem+'_port_quotient.json');q=json.loads(qfile.read_text());rows=q['macro_words'];edges=q['quotient_edges'];assert all(s==a for s,a,tgt in edges)
  literal=A/(stem+'_literal.txt');literal.write_text('\n'.join([str(len(rows))]+[z['word']+' '+z['end_marker'] for z in rows]+[str(len(edges))]+[f'{s} {tgt}' for s,a,tgt in edges])+'\n')
  cert=P/(stem+('_patch2_cone.tsv' if not suff else '_patch2_kernel.tsv'));marks=P/(stem+('_selected_marks.tsv' if not suff else '_raw_marks.tsv'))
  out=A/f'check_staged_{label}_{suff.count("residual0")}.json'
  with out.with_suffix('.log').open('w') as f:subprocess.run([str(exe),str(literal),str(cert),str(marks),str(out)],stdout=f,stderr=f,check=True)
  results=json.loads(out.read_text());records.append(dict(stem=stem,seconds=time.time()-t,results=results,hashes={str(f.relative_to(R)):hashlib.sha256(f.read_bytes()).hexdigest() for f in [qfile,literal,cert,marks,out]}));print('PASS',stem,flush=True)
(A/'staged_singleton_clause_replay_manifest.json').write_text(json.dumps({'status':'PASS all five independent literal clause checks','checker_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'records':records},indent=2)+'\n')
