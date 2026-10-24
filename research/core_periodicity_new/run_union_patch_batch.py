from pathlib import Path
import subprocess,time,json
P=Path('/workspace/shared/langton/core_periodicity_new');cases=[3,4,5,7,12,14,15,16,17,18,19,20,21,22,23,24,26,27,28,30,31,33,34,35,36,39,40,41,42,43,44];report=[];J=json.load(open('/workspace/shared/langton/word_stabilization/dcv_conditional_confinement_optimized.json'))['unproved_bad_transfers']
for i in cases:
 pre=P/f'protected_union_case{i:02d}';z=J[i-1];args=[z['source_packet'],z['target_packet'],*z['target_pose'],*z['source_output'],pre.name,'both'];subprocess.run(['python',str(P/'generate_protected_transfer_patch.py'),*map(str,args)],check=True,capture_output=True);start=time.time()
 with pre.with_suffix('.txt').open('w')as o,pre.with_suffix('.log').open('w')as e:
  try:r=subprocess.run([str(P/'protected_patch_bdd'),str(pre.with_suffix('.dat')),'1000000',str(pre.with_suffix('.bdd'))],stdout=o,stderr=e,timeout=90)
  except subprocess.TimeoutExpired:pre.with_suffix('.txt').write_text('status TIME_CAP\n')
 status=pre.with_suffix('.txt').read_text().strip();v=None
 if'EXHAUSTED_NO_HIT'in status:
  r=subprocess.run(['python',str(P/'verify_protected_patch_bdd.py'),str(pre.with_suffix('.dat')),str(pre.with_suffix('.bdd')),str(pre)+'.verified.json'],capture_output=True,text=True)
  assert r.returncode==0,(i,r.stderr);v=json.loads(r.stdout)
 record={'index':i,'status':status,'verification':v,'seconds':round(time.time()-start,3),'prefix':str(pre)};report.append(record);print(json.dumps(record),flush=True)
 (P/'protected_union_batch_summary.json').write_text(json.dumps(report,indent=2))
