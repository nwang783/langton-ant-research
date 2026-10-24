"""Greatest sound-candidate family via source companion flags. Discovery, not audit."""
from pathlib import Path
import json,subprocess,hashlib,time
P=Path(__file__).resolve().parent; B=P.parent/'core_periodicity_new'; O=P/'dcv_mutual_family';O.mkdir(exist_ok=True)
rows=[tuple(map(int,l.split()))for l in(P/'dcv_companion_candidate221.tsv').read_text().splitlines()];idx={r:i for i,r in enumerate(rows,1)};signed={tuple(map(int,l.split()))for l in(P/'dcv_anchored_signed38.tsv').read_text().splitlines()};controls={tuple(map(int,l.split()))for l in(P/'dcv_companion_observed19.tsv').read_text().splitlines()};assert signed<=set(rows);assert not signed&controls
active=set(rows)-controls; summary={'status':'DISCOVERY ONLY: requires independent literal model and invariant audit','candidate_rows':len(rows),'fixed_signed':len(signed),'removed_observed_controls':len(controls),'stages':[]}; gen=B/'generate_protected_transfer_patch.py'; flags=B/'add_protected_source_flags.py'; engine=B/'protected_patch_bdd_flags'; checker=B/'verify_protected_patch_bdd_flags.py'
for stage in range(20):
 S=O/f'stage{stage:02}';S.mkdir(exist_ok=True);H=S/'hypotheses.tsv';H.write_text(''.join(' '.join(map(str,r))+'\n'for r in sorted(active)));record={'stage':stage,'active_count':len(active),'hypotheses_sha256':hashlib.sha256(H.read_bytes()).hexdigest(),'results':[]};summary['stages'].append(record);supported=set(signed)
 for row in sorted(active-signed):
  i=idx[row];prefix=O/f'base{i:03}';mod=prefix.with_suffix('.json')
  if not mod.exists():
   p=subprocess.run(['python',str(gen),*map(str,row),str(prefix),'source'],capture_output=True,text=True,check=True);prefix.with_suffix('.gen.txt').write_text(p.stdout+p.stderr)
  out=S/f'candidate{i:03}';t=time.time();p=subprocess.run(['python',str(flags),str(mod),str(out),str(H)],capture_output=True,text=True,check=True);out.with_suffix('.gen.txt').write_text(p.stdout+p.stderr)
  p=subprocess.run([str(engine),str(out.with_suffix('.dat')),'1000000',str(out.with_suffix('.bdd'))],capture_output=True,text=True);out.with_suffix('.txt').write_text(p.stdout);out.with_suffix('.log').write_text(p.stderr);words=p.stdout.strip().splitlines()[-1].split();status=words[1];rr={'candidate_index':i,'tuple':row,'status':status,'seconds':round(time.time()-t,3),'engine_result':p.stdout.strip()}
  if status=='EXHAUSTED_NO_HIT':
   v=subprocess.run(['python',str(checker),str(out.with_suffix('.dat')),str(out.with_suffix('.bdd')),str(out.with_suffix('.verified.json'))],capture_output=True,text=True);out.with_suffix('.verify.txt').write_text(v.stdout+v.stderr);assert v.returncode==0;supported.add(row)
  record['results'].append(rr);(O/'summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps({'stage':stage,**rr}),flush=True)
 record['supported_count']=len(supported);record['removed_candidate_indices']=[idx[r]for r in sorted(active-supported)];(O/'summary.json').write_text(json.dumps(summary,indent=2))
 if supported==active:
  summary['stable']=True;summary['stable_new_candidate_indices']=[idx[r]for r in sorted(supported-signed)];(O/'summary.json').write_text(json.dumps(summary,indent=2));print('STABLE',summary['stable_new_candidate_indices'],flush=True);break
 active=supported
