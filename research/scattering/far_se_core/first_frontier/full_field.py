"""The complete q+a finite field at the far-SE source, without truncation."""
import sys,json,hashlib
from pathlib import Path
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'scattering/fixed_core_rectangle'))
from bivariate import A,infinite_tail
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,plan
C=lambda v:(0,0,v)
def source_field(M,N):
 for v,lo in ((M,100),(N,200),(A.sub(N,M),100)):assert A.nonneg(A.sub(v,C(lo)))
 nn=lambda a,b:A.add(A.scale(N,a),C(b));oldpath=ROOT/'continuation_2026-10-22/ant_continuation2/planar_structure/exceptional_rectangle_template.json'
 I=json.loads((HERE/'clean_interface.json').read_text());assert I['source_template_sha256']==hashlib.sha256(oldpath.read_bytes()).hexdigest() and I['base_prefix_read_upper']=={'u':98,'z':71}
 T=json.loads(oldpath.read_text());field=A.Field([(nn(-2,-33),nn(-2,-14)),(nn(-2,-33),nn(2,41))]);p=A.point(0,0);h=0;elapsed=C(0)
 pieces=T['segments'][:9]+[dict(type='finite',word=W[100:]),dict(type='source_periods',word=W)]
 for i,s in enumerate(pieces):
  word=s['word'];assert word and set(word)<={'R','L'};_,odd,end,eh=A.word_data(word,h)
  if s['type']=='finite':field.add_points(A.translate_local(q,p,0) for q in odd);p=A.translate_local(end,p,0);elapsed=A.add(elapsed,C(len(word)))
  else:
   count=M if s['type']=='source_periods' else nn(*s['count']);assert len(word)==104 and eh==h and A.nonneg(A.sub(count,A.ONE))
   field.add_rays([A.translate_local(q,p,0) for q in odd],end,count,'old'+str(i));p=A.padd(p,(A.scale(count,end[0]),A.scale(count,end[1])));elapsed=A.add(elapsed,A.scale(count,104))
  h=eh
 O=(A.add(A.scale(M,2),C(40)),A.add(A.scale(M,-2),C(-52)))
 assert p==O and h==2 and elapsed==A.add(A.add(A.scale(N,416),A.scale(M,104)),C(146044))
 field.points={A.psub(q,O) for q in field.points};field.rays=[(A.psub(b,O),d,count,label) for b,d,count,label in field.rays]
 return field,O,elapsed,I
