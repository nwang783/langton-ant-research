"""Test existing invariants against weakened, fully signed source-flag graphs."""
from pathlib import Path
import json,subprocess,hashlib,time
P=Path(__file__).resolve().parent;B=P.parent/'core_periodicity_new';O=P/'dcv_direct_source_flags40';O.mkdir(exist_ok=True);stage=P/'dcv_mutual_family/stage00';summary=json.loads((P/'dcv_mutual_family/summary.json').read_text());rows=[r for r in summary['stages'][0]['results']if r['status']=='EXHAUSTED_NO_HIT'];records=[];H=P/'dcv_anchored_signed40.tsv'
for r in rows:
 i=r['candidate_index'];out=O/f'candidate{i:03}';base=P/f'dcv_mutual_family/base{i:03}.json';bdd=stage/f'candidate{i:03}.bdd';t=time.time()
 p=subprocess.run(['python',str(B/'add_protected_source_flags.py'),str(base),str(out),str(H)],capture_output=True,text=True,check=True);out.with_suffix('.gen.txt').write_text(p.stdout+p.stderr)
 p=subprocess.run(['python',str(B/'verify_protected_patch_bdd_flags.py'),str(out.with_suffix('.dat')),str(bdd),str(out.with_suffix('.verified.json'))],capture_output=True,text=True);out.with_suffix('.verify.txt').write_text(p.stdout+p.stderr)
 rec={'candidate_index':i,'tuple':r['tuple'],'invariant_verified_under_signed40':p.returncode==0,'invariant_file':str(bdd),'invariant_sha256':hashlib.sha256(bdd.read_bytes()).hexdigest(),'seconds':round(time.time()-t,3)};records.append(rec);(O/'summary.json').write_text(json.dumps({'status':'Independent-model audit required; every pass uses ONLY signed facts','fixed_signed_file':str(H),'fixed_signed_sha256':hashlib.sha256(H.read_bytes()).hexdigest(),'results':records},indent=2));print(json.dumps(rec),flush=True)
