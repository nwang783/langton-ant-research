"""Exact two-parameter complete-field certificates for displaced NW channels."""
import sys,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/scattering/fixed_core_rectangle')
from bivariate import A,infinite_tail
M=(1,0,100);N=(1,1,200)
def const(k):return (0,0,k)
def lm(a,b):return A.add(A.scale(M,a),const(b))
def ln(a,b):return A.add(A.scale(N,a),const(b))

def read_bounds(tail,base):
 points=list(A.READ_POINTS)
 for b,d,count in A.READ_RAYS:
  points.extend((b,A.padd(b,(A.scale(A.sub(count,A.ONE),d[0]),A.scale(A.sub(count,A.ONE),d[1])))))
 points.extend(A.translate_local(p,base,0) for p in tail[0])
 out={}
 for label,sgn in [('u',-1),('z',1)]:
  vals=[A.add(p[0],A.scale(p[1],sgn)) for p in points]
  assert all(v[1]<=0 for v in vals),('unbounded-in-n',label)
  coefficient=max(0,max(v[0] for v in vals));at_origin=max(v[2] for v in vals)
  # Bounds in m, independent of n, and valid on the full cone.
  out[label+'_upper']=[coefficient,at_origin-100*coefficient]
 assert tail[2][0]-tail[2][1]==0 and sum(tail[2])<0
 return out

def main(r):
 assert r in (70,75);T=json.loads((HERE/f'template_r{r}.json').read_text());assert T['phase']==r
 for k in A.STATS:A.STATS[k]=0
 A.READ_POINTS.clear();A.READ_RAYS.clear()
 bx,by={70:(-22,30),75:(-21,30)}[r];ay={70:57,75:45}[r]
 inputs={'q':(ln(-2,-33),ln(-2,-14)),'s':(lm(-2,bx),lm(2,by)),'a':(ln(-2,-33),ln(2,ay))}
 for i,p in enumerate(inputs.values()):
  for q in list(inputs.values())[i+1:]:assert A.no_point_collision(p,q)
 field=A.Field(set(inputs.values()));base=A.point(0,0);h=0;elapsed=A.ZERO;contacts={};records=[]
 standard={A.W[i:]+A.W[:i] for i in range(104)}
 for i,s in enumerate(T['segments']):
  word=s['word'];assert word and set(word)<={'R','L'};data=A.word_data(word,h)
  count=tuple(s['count']) if s['type']=='periods' else None
  hits={}
  for j,q in enumerate(A.plan(word,(0,0),h)[0]):
   p=A.translate_local(q,base,0)
   for label,target in inputs.items():
    if count is None:
     if p==target:
      if label not in contacts and label not in hits:hits[label]=A.add(elapsed,const(j))
     else:assert A.no_point_collision(p,target)
    else:
     k=A.line_coordinate(A.psub(target,p),data[2])
     if k is not None and A.in_range(k,count) and label not in contacts:
      t=A.add(A.add(elapsed,A.scale(k,104)),const(j));hits[label]=A.minimum(hits[label],t) if label in hits else t
  contacts.update(hits)
  if count is None:base=A.apply_finite(field,data,base,0,'finite'+str(i));elapsed=A.add(elapsed,const(len(word)))
  else:
   assert len(word)==104 and word in standard and data[3]==h and A.nonneg(A.sub(count,A.ONE))
   base=A.apply_periods(field,data,base,0,count,'periods'+str(i));elapsed=A.add(elapsed,A.scale(count,104))
  h=data[3];records.append(dict(segment=i,time=elapsed,pose=[base,h],contacts=hits));print(json.dumps(records[-1]),flush=True)
 expected_time=A.add(A.scale(N,520),const(153920)) if r==70 else A.add(A.add(A.scale(N,416),A.scale(M,104)),const(148096))
 expected_pose=((ln(-2,-76),ln(-2,-20)),0) if r==70 else ((lm(-2,-72),lm(2,-28)),2)
 assert elapsed==expected_time and (base,h)==expected_pose
 assert contacts=={'q':A.add(A.scale(N,104),const(10881)),'s':A.add(A.add(A.scale(N,208),A.scale(M,104)),const(70738+r)),'a':A.add(A.scale(N,312),const({70:79234,75:74446}[r]))}
 tw=T['infinite_tail_word'];assert tw in standard;tail=A.word_data(tw,h);assert tail[3]==h and tail[2]==(-2,-2)
 proof=infinite_tail(field,tail,base);bounds=read_bounds(tail,base)
 assert tw==A.W[{70:29,75:55}[r]:]+A.W[:{70:29,75:55}[r]]
 assert bounds=={'u_upper':[0,58],'z_upper':[0,{70:87,75:75}[r]]}
 out=dict(status='exact complete-field certificate passed',phase=r,domain='m>=100,n>=m+100',variables='u=m-100>=0,v=n-m-100>=0',capture_time=elapsed,capture_pose=[base,h],tail=proof,tail_phase=next(i for i in range(104) if tw==A.W[i:]+A.W[:i]),all_future_read_bounds_in_m=bounds,contacts=contacts,statistics=A.STATS.copy(),records=records,template_sha256=hashlib.sha256((HERE/f'template_r{r}.json').read_bytes()).hexdigest())
 (HERE/f'certificate_r{r}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main(int(sys.argv[1]))
