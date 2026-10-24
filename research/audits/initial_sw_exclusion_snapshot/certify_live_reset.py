"""Four distinct ordinary packets reset the entire live upper half-plane."""
import json,hashlib,gzip,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];CAP=HERE.parent/'blank_return_cap';SRC=HERE.parent/'ordinary_reverse_interface'
sys.path.insert(0,str(CAP));from discover import initial
sys.path.insert(0,str(HERE.parent/'independent_reverse_ages'));import certify_interface as I
from ant_exact import W,P,plan
C=lambda a:(0,0,a);M=(1,0,100);K=(0,1,100)
add=lambda a,b:tuple(x+y for x,y in zip(a,b));scale=lambda a,k:tuple(x*k for x in a)
def plus(p,q):return add(p[0],q[0]),add(p[1],q[1])
def off(p,q):return plus(p,(C(q[0]),C(q[1])))
def main():
 for path,digest in [(SRC/'manifest.json','2cd64e957de70ed25e5ab7bb58ac87ce36765cfc6a1c234c05d65441aa8550a1'),(CAP/'manifest.json','2827291464278a15841e21a0430de38d18f990f01827f7adb0d43cfb5dbe9237')]:assert hashlib.sha256(path.read_bytes()).hexdigest()==digest
 sm=json.loads((SRC/'manifest.json').read_text())['files'];cm=json.loads((CAP/'manifest.json').read_text())['files']
 for name in ['fixed_caps.json','bridge.json']:assert hashlib.sha256((CAP/name).read_bytes()).hexdigest()==cm[name]
 cap=next(x for x in json.loads((CAP/'fixed_caps.json').read_text())['rows'] if x['phase']==13)
 word=gzip.open(CAP/'word_r13.txt.gz','rt').read();assert hashlib.sha256(word.encode()).hexdigest()==cap['word_sha256']
 f,p,h=initial(13);assert [list(p),h]==cap['start'];minimum=10**9
 for expected in word[:10262]:minimum=min(minimum,sum(p));p,h,ch=f.step(p,h);assert ch==expected
 assert p==(-15,26) and h==1 and minimum>=-250
 actual={q for q in f.changes if sum(q)>=-250}
 for b,d,lo,hi in f.rays:
  assert d==(-2,-2) and hi is None
  for j in range(lo,(sum(b)+250)//4+1):actual.symmetric_difference_update({(b[0]-2*j,b[1]-2*j)})
 target=I.main();assert actual==target and len(actual)==2442 # exact set equality, not hash equality
 bridges=json.loads((CAP/'bridge.json').read_text())['rows'];rows=[]
 for r in [13,14,27,89]:
  cp=SRC/f'certificate_r{r}.json';assert hashlib.sha256(cp.read_bytes()).hexdigest()==sm[cp.name];cert=json.loads(cp.read_text());tp=SRC/f'template_r{r}.json';assert hashlib.sha256(tp.read_bytes()).hexdigest()==cert['template_sha256'];T=json.loads(tp.read_text())
  bridge=next(x for x in bridges if x['phase']==r);assert bridge['cap_type']==13 and bridge['packet_certificate_sha256']==hashlib.sha256(cp.read_bytes()).hexdigest()
  p=(add(scale(M,-2),C(-15)),add(scale(M,-2),C(10)));h=3;elapsed=add(scale(M,104),C(9977));us=[-34,48];zu=[35]
  def collect(q):
   u=add(q[0],scale(q[1],-1));z=add(q[0],q[1]);assert u[:2]==(0,0) and z[0]<=0 and z[1]<=0;us.append(u[2]);zu.append(z[2])
  def segment(w,count=None):
   nonlocal p,h,elapsed
   assert w and set(w)<={'R','L'};qs,_,end,eh=plan(w,(0,0),h)
   if count is None:
    for q in qs:collect(off(p,q))
    p=off(p,end);elapsed=add(elapsed,C(len(w)))
   else:
    assert len(w)==104 and eh==h and all(v>=0 for v in add(count,C(-1)))
    for q in qs:
     first=off(p,q);collect(first);collect(plus(first,(scale(add(count,C(-1)),end[0]),scale(add(count,C(-1)),end[1]))))
    p=plus(p,(scale(count,end[0]),scale(count,end[1])));elapsed=add(elapsed,scale(count,104))
   h=eh
  for s in T['segments']:
   assert s['type'] in ['finite','periods'];segment(s['word'],None if s['type']=='finite' else add(scale(K,s['count'][0]),C(s['count'][1])))
  assert cert['tail_phase']==0 and h==1
  segment(W,add(add(M,K),C(-20+bridge['extra_NE_period'])))
  assert p==(C(-22),C(-71)) and h==1
  a,b,c=bridge['cap_entry_time_m_k_constant'];assert elapsed==add(add(scale(M,a),scale(K,b)),C(c))
  segment(word[:10262]);assert p==(C(-15),C(26)) and h==1;reset=elapsed
  segment((W[99:]+W[:99])[:5]);assert p==(C(-15),C(29)) and h==0
  for x,y in P:us.append(-15-x-(29-y));zu.append(-15-x+29-y)
  bounds=[min(us),max(us)];upperz=max(zu)
  assert bounds==[-82,58] and upperz==39
  qpar=[(-15+cert['second_marker_affine'][1][1])%2,(10-cert['second_marker_affine'][0][1])%2];assert qpar==[1,0]
  rows.append(dict(phase=r,reset_time_m_k_constant=[208,208,c+10262],reset_pose=[[-15,26],1],complete_prefix_and_archive_u_bounds=bounds,complete_prefix_z_upper=upperz,first_remote_parity=qpar))
 out=dict(status='exact entire live-half-plane reset for four distinct ordinary packets',domain='independent m,k>=100',region='z>=-250',restricted_field_size=len(actual),restricted_field_sha256=hashlib.sha256(repr(sorted(actual)).encode()).hexdigest(),rows=rows,scope='All old information below the region is retained, not erased. The coupled reference futures must remain inside the region.')
 (HERE/'live_reset.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
