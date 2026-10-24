"""Complete finite q+a field at a mature second-band source checkpoint.
Color validity is inherited from the audited old rectangle and strip proofs;
no point or deposition ray is deleted from the exact XOR field.
"""
import sys,json,hashlib
from pathlib import Path
R=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(R/'scattering/fixed_core_rectangle'))
from bivariate import A,infinite_tail
sys.path.insert(0,str(R/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,plan,canonical_source
C=lambda v:(0,0,v)
def source_field(M,N):
 K=A.sub(N,M)
 for v,lo in ((M,100),(N,200),(K,100)):assert A.nonneg(A.sub(v,C(lo)))
 nn=lambda a,b:A.add(A.scale(N,a),C(b))
 O=(A.add(A.scale(M,-2),C(-62)),A.add(A.scale(M,2),C(2)))
 oldpath=R/'continuation_2026-10-22/ant_continuation2/planar_structure/exceptional_rectangle_template.json'
 I=json.loads((HERE/'strip_interface.json').read_text());assert I['source_template_sha256']==hashlib.sha256(oldpath.read_bytes()).hexdigest() and I['pre_core_read_upper']=={'u':58,'z':71}
 old=json.loads(oldpath.read_text());field=A.Field([(nn(-2,-33),nn(-2,-14)),(nn(-2,-33),nn(2,41))]);p=A.point(0,0);h=0;elapsed=C(0)
 for i,s in enumerate(old['segments'][:7]):
  assert s['word'] and set(s['word'])<={'R','L'}
  _,odd,end,eh=A.word_data(s['word'],h)
  if s['type']=='finite':field.add_points(A.translate_local(q,p,0) for q in odd);p=A.translate_local(end,p,0);elapsed=A.add(elapsed,C(len(s['word'])))
  else:
   count=A.add(A.scale(N,s['count'][0]),C(s['count'][1]));assert len(s['word'])==104 and eh==h and A.nonneg(A.sub(count,A.ONE))
   field.add_rays([A.translate_local(q,p,0) for q in odd],end,count,'old'+str(i));p=A.padd(p,(A.scale(count,end[0]),A.scale(count,end[1])));elapsed=A.add(elapsed,A.scale(count,104))
  h=eh
 assert p==(nn(-2,-62),nn(2,2)) and h==2
 assert old['segments'][7]['word']==W and old['segments'][7]['count']==[1,7]
 _,odd,end,eh=A.word_data(W,h);assert end==(2,-2) and eh==h
 field.add_rays([A.translate_local(q,p,0) for q in odd],end,K,'return_SE');p=A.padd(p,(A.scale(K,2),A.scale(K,-2)));elapsed=A.add(elapsed,A.scale(K,104));assert p==O
 assert elapsed==A.add(A.sub(A.scale(N,416),A.scale(M,104)),C(122376))
 field.points={A.psub(q,O) for q in field.points};field.rays=[(A.psub(b,O),d,count,label) for b,d,count,label in field.rays]
 return field,O,elapsed,I

def absolute_read_bounds(O,taildata,tailbase):
 """Upper u/z bounds for all new finite-prefix reads and separately the tail."""
 out={};tail={}
 for name,normal in [('u',(1,-1)),('z',(1,1))]:
  normal_value=lambda p:A.add(A.scale(p[0],normal[0]),A.scale(p[1],normal[1]))
  def ub(v):assert v[0]<=0 and v[1]<=0,(name,'unbounded upper support',v);return v[2]
  vals=[ub(normal_value(A.padd(O,p))) for p in A.READ_POINTS]
  for b,d,count in A.READ_RAYS:
   v=normal_value(A.padd(O,b));step=d[0]*normal[0]+d[1]*normal[1]
   if step>0:v=A.add(v,A.scale(A.sub(count,A.ONE),step))
   vals.append(ub(v))
  out[name]=max(vals)
  step=taildata[2][0]*normal[0]+taildata[2][1]*normal[1]
  tail[name]=None if step>0 else max(ub(normal_value(A.padd(O,A.translate_local(q,tailbase,0)))) for q in taildata[0])
 return out,tail
