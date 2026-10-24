"""Discovery only. Candidate assumptions are not signed until stable mutual replay."""
from pathlib import Path
import json,subprocess,hashlib,sys,time,re
P=Path(__file__).resolve().parent;B=P.parent/'core_periodicity_new'; mode=sys.argv[1] if len(sys.argv)>1 else '69'; O=P/('dcv_mutual_source_flags_'+mode);O.mkdir(exist_ok=True)
J=json.loads((P/'dcv_conditional_confinement_optimized.json').read_text()); rows=J['unproved_bad_transfers'];signed={6,8,9,10,11,13,25,29,32,37,38,57,58,59,60,61,63,64,65,66,67,68,*range(45,57),69,27,34};indices=[i for i in range(1,70)if i not in signed and i>5]
def row(r):return [r['source_packet'],r['target_packet'],*r['target_pose'],*r['source_output']]
H=O/'hypotheses.tsv'
if mode=='69':H.write_text(''.join(' '.join(map(str,row(r)))+'\n' for r in rows))
else:H.write_bytes((P/'dcv_companion_candidate221.tsv').read_bytes())
result={'status':'PROVISIONAL discovery under unsiged mutual hypotheses; no new theorem','mode':mode,'hypotheses_sha256':hashlib.sha256(H.read_bytes()).hexdigest(),'results':[]}
for i in indices:
 pref=O/f'case{i:02}';base=B/f'protected_flagbase_case{i:02}.json';t=time.time();gen=subprocess.run(['python',str(B/'add_protected_source_flags.py'),str(base),str(pref),str(H)],capture_output=True,text=True,check=True);(pref.with_suffix('.gen.txt')).write_text(gen.stdout)
 p=subprocess.run([str(B/'protected_patch_bdd_flags'),str(pref.with_suffix('.dat')),'1000000',str(pref.with_suffix('.bdd'))],capture_output=True,text=True);pref.with_suffix('.txt').write_text(p.stdout);pref.with_suffix('.log').write_text(p.stderr)
 status='UNKNOWN';parsed=None
 try:
  line=p.stdout.strip().splitlines()[-1].split();status=line[1];parsed={line[j]:line[j+1]for j in range(0,len(line)-1,2)}
 except:pass
 if pref.with_suffix('.bdd').exists():
  v=subprocess.run(['python',str(B/'verify_protected_patch_bdd_flags.py'),str(pref.with_suffix('.dat')),str(pref.with_suffix('.bdd')),str(pref.with_suffix('.verified.json'))],capture_output=True,text=True);pref.with_suffix('.verify.txt').write_text(v.stdout+v.stderr);assert v.returncode==0
 rec={'index':i,'status':status,'returncode':p.returncode,'seconds':round(time.time()-t,3),'result':parsed};result['results'].append(rec);(O/'summary.json').write_text(json.dumps(result,indent=2));print(json.dumps(rec),flush=True)
