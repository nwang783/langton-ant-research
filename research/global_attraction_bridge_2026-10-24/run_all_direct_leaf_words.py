"""Bounded, resumable, exact coverage runner. No hard leaf is skipped."""
import json,hashlib,gzip,subprocess,time,resource,math,re
from pathlib import Path
P=Path(__file__).parent;R=P/'direct_leaf_complete_run';binary=P/'run_all_direct_leaf_words'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
plan=json.loads((R/'RUN_INPUT_MANIFEST.json').read_text());bhash=sha(binary);phash=sha(R/'RUN_INPUT_MANIFEST.json')
wall0=time.monotonic();cpu_spent=0;covered=0;completed=[];failure=None
limits=dict(overall_wall_seconds=1200,total_child_cpu_seconds=1150,per_chunk_cpu_seconds=180,address_space_mib=512,run_directory_disk_mib=512,per_output_file_mib=64)
def disk_bytes():return sum(p.stat().st_size for p in R.iterdir()if p.is_file())
for c in plan['chunks']:
 name=c['name'];mp=R/(name+'.checkpoint.json');ip=R/c['input'];gp=R/(name+'.observations.gz');tmp=R/(name+'.observations.partial')
 if sha(ip)!=c['sha256']:failure=dict(chunk=name,reason='input hash mismatch');break
 if mp.exists():
  m=json.loads(mp.read_text())
  if m.get('status')=='COMPLETE':
   if m['binary_sha256']!=bhash or m['input_manifest_sha256']!=phash or m['input_sha256']!=c['sha256']or sha(gp)!=m['compressed_output_sha256']:
    failure=dict(chunk=name,reason='checkpoint binding mismatch');break
   covered+=c['count'];cpu_spent+=m['cpu_seconds'];completed.append(name);continue
 remaining_wall=limits['overall_wall_seconds']-(time.monotonic()-wall0)
 remaining_cpu=limits['total_child_cpu_seconds']-cpu_spent
 if remaining_wall<=1 or remaining_cpu<=1 or disk_bytes()>limits['run_directory_disk_mib']*1024**2:
  failure=dict(chunk=name,reason='explicit aggregate resource limit');break
 def restrict():
  cpu=max(1,min(limits['per_chunk_cpu_seconds'],math.floor(remaining_cpu)))
  resource.setrlimit(resource.RLIMIT_CPU,(cpu,cpu));resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2));resource.setrlimit(resource.RLIMIT_FSIZE,(64*1024**2,64*1024**2))
 u0=resource.getrusage(resource.RUSAGE_CHILDREN);t0=time.monotonic()
 try:
  rr=subprocess.run([str(binary),str(ip),str(tmp),str(c['first_id']),str(c['count'])],text=True,capture_output=True,timeout=min(240,remaining_wall),preexec_fn=restrict)
  rc=rr.returncode;stderr=rr.stderr
 except subprocess.TimeoutExpired as ex:rc=None;stderr=str(ex.stderr)
 u1=resource.getrusage(resource.RUSAGE_CHILDREN);cpu=(u1.ru_utime+u1.ru_stime)-(u0.ru_utime+u0.ru_stime);cpu_spent+=cpu
 info=dict(chunk=name,first_id=c['first_id'],count=c['count'],returncode=rc,stderr=stderr,cpu_seconds=cpu,wall_seconds=time.monotonic()-t0,max_rss_kib=u1.ru_maxrss,binary_sha256=bhash,input_manifest_sha256=phash,input_sha256=c['sha256'])
 if rc!=0:info['status']='UNKNOWN';mp.write_text(json.dumps(info,indent=2)+'\n');failure=dict(chunk=name,reason='subprocess did not complete',detail=info);break
 digest=hashlib.sha256();count=0;maxT=0
 try:
  with open(tmp,'rb')as raw,gzip.open(gp,'wb',compresslevel=6)as out:
   for line in raw:
    a=list(map(int,line.split()));assert len(a)==13 and a[0]==c['first_id']+count
    _,before,s,T,dx,dy,A,x,y,h,phase,mass,statehash=a
    assert 0<=before<=s<T<=624000 and T-s==104 and abs(dx)==abs(dy)==2 and 0<=h<4 and 0<=phase<104 and mass>=0
    digest.update(line);out.write(line);count+=1;maxT=max(maxT,T)
  assert count==c['count']
 except Exception as ex:info['status']='UNKNOWN';info['validation_error']=repr(ex);mp.write_text(json.dumps(info,indent=2)+'\n');failure=dict(chunk=name,reason='output validation failed');break
 info.update(status='COMPLETE',uncompressed_output_sha256=digest.hexdigest(),compressed_output_sha256=sha(gp),max_global_certificate_end=maxT)
 mp.write_text(json.dumps(info,indent=2)+'\n');tmp.unlink();covered+=count;completed.append(name)
 print(json.dumps(dict(completed_chunk=name,covered=covered,total=plan['total_obligations'],cpu_seconds=round(cpu_spent,2),wall_seconds=round(time.monotonic()-wall0,2),disk_mib=round(disk_bytes()/1024**2,2))),flush=True)
status='COMPLETE'if covered==plan['total_obligations']and not failure else'INCOMPLETE / UNKNOWN'
report=dict(status=status,covered=covered,total=plan['total_obligations'],completed_chunks=completed,failure=failure,limits=limits,total_child_cpu_seconds=cpu_spent,wall_seconds=time.monotonic()-wall0,binary_sha256=bhash,input_manifest_sha256=phash)
(R/'RUN_STATUS.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report),flush=True)
