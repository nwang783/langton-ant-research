from pathlib import Path
import subprocess,time,json
P=Path('/workspace/shared/langton/core_periodicity_new');cases=[45,46,47,48,49,50,51,52,53,54,55,56,62,69];report=[]
for i in cases:
 pre=P/f'protected_vc24_case{i:02d}';start=time.time()
 if i!=45:
  with pre.with_suffix('.txt').open('w')as o,pre.with_suffix('.log').open('w')as e:
   try:r=subprocess.run([str(P/'protected_patch_bdd'),str(pre.with_suffix('.dat')),'1000000',str(pre.with_suffix('.bdd'))],stdout=o,stderr=e,timeout=180)
   except subprocess.TimeoutExpired:pre.with_suffix('.txt').write_text('status TIME_CAP\n')
 status=pre.with_suffix('.txt').read_text().strip();v=None
 if'EXHAUSTED_NO_HIT'in status:
  r=subprocess.run(['python',str(P/'verify_protected_patch_bdd.py'),str(pre.with_suffix('.dat')),str(pre.with_suffix('.bdd')),str(pre)+'.verified.json'],capture_output=True,text=True)
  assert r.returncode==0,(i,r.stderr);v=json.loads(r.stdout)
 record={'index':i,'status':status,'verification':v,'seconds':round(time.time()-start,3),'prefix':str(pre)};report.append(record);print(json.dumps(record),flush=True)
 (P/'protected_vc24_batch_summary.json').write_text(json.dumps(report,indent=2))
