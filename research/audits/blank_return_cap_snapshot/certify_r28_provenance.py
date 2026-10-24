"""Exact all-parameter chronology of the nested old-wake collision."""
import sys,json,hashlib
from pathlib import Path
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'scattering/fixed_core_rectangle'))
from bivariate import A
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,plan
M=(1,0,100);K=(0,1,100);C=lambda x:(0,0,x)
def linear(a,b,c):return A.add(A.add(A.scale(M,a),A.scale(K,b)),C(c))
def main():
 path=HERE/'r28_complete_template.json';T=json.loads(path.read_text());R=json.loads((HERE/'r28_complete_certificate.json').read_text());assert R['template_sha256']==hashlib.sha256(path.read_bytes()).hexdigest()
 target=(linear(-2,0,8),linear(-2,0,-5));p=A.point(0,0);h=0;elapsed=C(0);hits=[]
 for i,s in enumerate(T['segments']):
  word=s['word'];assert set(word)<={'R','L'};reads,_,end,eh=plan(word,(0,0),h)
  if i==8:reads=reads[:57]
  for j,b in enumerate(reads):
   q=A.translate_local(b,p,0)
   if s['type']=='finite':
    if q==target:hits.append(dict(time=A.add(elapsed,C(j)),letter=word[j],segment=i,index=j))
    else:A.no_point_collision(q,target)
   else:
    count=linear(*s['count_mk']);epoch=A.line_coordinate(A.psub(target,q),end)
    if epoch is not None and A.in_range(epoch,count):hits.append(dict(time=A.add(elapsed,A.add(A.scale(epoch,104),C(j))),letter=word[j],segment=i,index=j))
  if i==8:break
  if s['type']=='finite':p=A.translate_local(end,p,0);elapsed=A.add(elapsed,C(len(word)))
  else:p=A.padd(p,(A.scale(count,end[0]),A.scale(count,end[1])));elapsed=A.add(elapsed,A.scale(count,104))
  h=eh
 assert len(hits)==2 and hits[0]['time']==linear(104,0,14867) and hits[0]['letter']=='R' and hits[0]['segment']==2 and hits[0]['index']==4890
 assert hits[1]['time']==linear(312,208,72723) and hits[1]['letter']=='L' and hits[1]['segment']==8 and hits[1]['index']==56
 assert T['segments'][7]['word']==W and T['segments'][8]['word'][:56]==W[:56] and W[56]=='R'
 age=A.sub(hits[1]['time'],hits[0]['time']);assert age==linear(208,208,57856)
 out=dict(status='exact unique earlier read and unbroken black lifetime',domain='independent integers m,k>=100',old_cell=target,creation_time=hits[0]['time'],next_read_time=hits[1]['time'],black_lifetime_age=age,all_pre_collision_visits=hits,scope='The late read consumes a black cell created in the ordinary first-core recovery, after the distant reversal and central blank-endcap collision. No finite-input bit is freshly supplied at this third interaction.',source_certificate_sha256=hashlib.sha256((HERE/'r28_complete_certificate.json').read_bytes()).hexdigest())
 (HERE/'r28_provenance.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
