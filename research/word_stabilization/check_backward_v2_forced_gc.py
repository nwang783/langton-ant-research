import pathlib,subprocess,json
R=pathlib.Path(__file__).resolve().parents[1];B=R/'core_periodicity_new';D=B/'chronology_dcuv/backward_controls';o=D/'v2_forced_gc';o.mkdir(exist_ok=True);results=[];gcs=0
for p in sorted(D.glob('c*.dat')):
 a=subprocess.run(list(map(str,[B/'guarded_reset_bdd_backward',p,50000])),capture_output=True,text=True);z=subprocess.run(list(map(str,[B/'guarded_reset_bdd_backward_v2',p,50000,o/(p.stem+'.bdd'),10,0])),capture_output=True,text=True);assert a.returncode==z.returncode==0,(p,a.stdout,z.stdout);assert a.stdout.split()[:6]==z.stdout.split()[:6],(p,a.stdout,z.stdout);gcs+=z.stderr.count('midgc ')
 if 'EXHAUSTED_NO_HIT'in z.stdout:
  v=subprocess.run(list(map(str,['python',B/'verify_protected_patch_bdd_labels.py',p,o/(p.stem+'.bdd')])),capture_output=True,text=True);assert v.returncode==0,(p,v.stdout,v.stderr)
 results.append({'case':p.name,'status':z.stdout.strip(),'gc_count':z.stderr.count('midgc ')})
(o/'comparison.json').write_text(json.dumps({'status':'PASS','controls':len(results),'forced_gc_calls':gcs,'cases':results},indent=2));print('PASS',len(results),'forced gc',gcs)
