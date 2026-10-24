from pathlib import Path
import json,gzip,hashlib,time,subprocess,resource
R=Path('/workspace/shared/langton');A=R/'audits';SRC=R/'global_attraction_bridge_2026-10-24/direct_leaf_complete_run';OUT=A/'direct_leaf_replay';OUT.mkdir(exist_ok=True);sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();manifest=SRC/'RUN_INPUT_MANIFEST.json';mh=sha(manifest);M=json.loads(manifest.read_text());exe=A/'replay_direct_leaf_certificates_independent';eh=sha(exe);code=A/'replay_direct_leaf_certificates_independent.cpp';ch=sha(code);start=time.monotonic();totalcpu=0;covered=0;completed=[]
def status(state,why=None):
 r=dict(status=state,reason=why,covered=covered,total=M['total_obligations'],chunks=completed,wall_seconds=time.monotonic()-start,cpu_seconds=totalcpu,input_manifest_sha256=mh,checker_CPP_sha256=ch,checker_binary_sha256=eh,limits=dict(wall_seconds=1800,cpu_seconds=600,address_space_MiB=512))
 (OUT/'INDEPENDENT_RUN_STATUS.json').write_text(json.dumps(r,indent=2)+'\n');return r
for chunk in M['chunks']:
 name=chunk['name'];ac=SRC/(name+'.checkpoint.json');ob=SRC/(name+'.observations.gz');ip=SRC/chunk['input'];ck=OUT/(name+'.checkpoint.json');txt=OUT/(name+'.observations');rp=OUT/(name+'.report')
 assert sha(ip)==chunk['sha256']
 while not ac.exists():
  if time.monotonic()-start>1800:print(status('INCOMPLETE','awaiting author checkpoint within bound'));raise SystemExit(2)
  status('RUNNING','awaiting '+name);time.sleep(10)
 c=json.loads(ac.read_text());assert c['status']=='COMPLETE' and c['count']==chunk['count']and c['input_manifest_sha256']==mh and c['input_sha256']==chunk['sha256']and sha(ob)==c['compressed_output_sha256'];ach=sha(ac)
 if ck.exists():
  x=json.loads(ck.read_text())
  if x['status']=='PASS'and x['author_checkpoint_sha256']==ach and x['checker_CPP_sha256']==ch and x['checker_binary_sha256']==eh and x['report_sha256']==sha(rp):
   covered+=chunk['count'];totalcpu+=x['cpu_seconds'];completed.append(name);continue
 with gzip.open(ob,'rb')as f,txt.open('wb')as g:
  while True:
   b=f.read(1<<20)
   if not b:break
   g.write(b)
 assert sha(txt)==c['uncompressed_output_sha256']
 remaining=600-totalcpu
 if remaining<1:print(status('INCOMPLETE','CPU bound'));raise SystemExit(3)
 def limits():
  resource.setrlimit(resource.RLIMIT_CPU,(min(120,int(remaining)),min(120,int(remaining))));resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
 u=resource.getrusage(resource.RUSAGE_CHILDREN);t=time.monotonic()
 p=subprocess.run([str(exe),str(ip),str(txt),str(rp)],capture_output=True,text=True,timeout=150,preexec_fn=limits)
 v=resource.getrusage(resource.RUSAGE_CHILDREN);cpu=v.ru_utime+v.ru_stime-u.ru_utime-u.ru_stime;totalcpu+=cpu
 if p.returncode!=0:print(status('INCOMPLETE',dict(chunk=name,returncode=p.returncode,stderr=p.stderr)));raise SystemExit(4)
 assert rp.read_text().startswith(f"PASS first={chunk['first_id']} last={chunk['first_id']+chunk['count']-1} count={chunk['count']} ")
 x=dict(status='PASS',chunk=name,count=chunk['count'],author_checkpoint_sha256=ach,author_output_sha256=sha(ob),input_manifest_sha256=mh,input_sha256=sha(ip),checker_CPP_sha256=ch,checker_binary_sha256=eh,report_sha256=sha(rp),cpu_seconds=cpu,wall_seconds=time.monotonic()-t,stderr=p.stderr)
 ck.write_text(json.dumps(x,indent=2)+'\n');txt.unlink();covered+=chunk['count'];completed.append(name);status('RUNNING');print(name,covered,totalcpu,flush=True)
assert covered==M['total_obligations'];print(json.dumps(status('PASS_ALL_PHYSICAL_CERTIFICATES; source/semantic assembly separate')),flush=True)
