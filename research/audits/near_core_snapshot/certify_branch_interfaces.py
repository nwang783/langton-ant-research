"""Archive bounds and forced exceptional coordinates for m=1 and m=6."""
import json,sys,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation')
from ant_exact import canonical_source,certify_period,plan,PHASES
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation2/planar_structure')
import certify_exceptional_rectangle as old
A=old.A;A.LOW=200

def rot(p,j):
 for _ in range(j%4):p=p[1],-p[0]
 return p

def main():
 rows=[]
 for m,branch in [(1,False),(1,True),(6,False),(6,True)]:
  stem=f'branch_m{m}_' if branch else f'm{m}'
  cpath=HERE/(f'branch_m{m}_certificate.json' if branch else f'certificate_m{m}.json')
  tpath=HERE/(f'branch_m{m}_template.json' if branch else f'template_m{m}.json')
  C=json.loads(cpath.read_text());T=json.loads(tpath.read_text());assert C['status']=='exact complete-field all-n proof passed' and C['domain']=='integer n>=200' and C['m']==m
  assert C['template_sha256']==hashlib.sha256(tpath.read_bytes()).hexdigest()
  coeff=T['pose_coeff'];p=tuple(coeff[i]*200+T['pose_constant'][i] for i in (0,1));h=T['heading'];tw=T['infinite_tail_word'];phase=PHASES[tw]
  B,bp,bh=canonical_source(0,phase);r=(h-bh)%4;bp=rot(bp,r);delta=(p[0]-bp[0],p[1]-bp[1]);clean={(rot(q,r)[0]+delta[0],rot(q,r)[1]+delta[1]) for q in B}
  assert tuple(certify_period(clean,p,h,tw)['drift'])==tuple(C['tail']['drift'])
  corebounds={}
  for name,norm in [('u',(1,-1)),('z',(1,1))]:
   slope=sum(coeff[i]*norm[i] for i in (0,1));values=[sum(q[i]*norm[i] for i in (0,1)) for q in clean]
   corebounds[name+'_lower']=min(values) if slope>=0 else None
   corebounds[name+'_upper']=max(values) if slope<=0 else None
  archive={}
  for k,v in C['complete_field_support_bounds'].items():
   cv=corebounds[k];archive[k]=None if v is None or cv is None else (min(v,cv) if k.endswith('lower') else max(v,cv))
  assert archive['z_upper'] is not None
  key='u_upper' if C['tail']['drift']==[2,-2] else 'u_lower'
  assert archive[key] is not None
  exc=tuple(tuple(a) for a in C['exceptional_phase72_ray'][0]);d=tuple(C['exceptional_phase72_ray'][1])
  if m==1 and not branch:target=((-2,-33),(2,-21));expected_index=(1,-10)
  elif m==1:target=((2,-100),(-2,-14));expected_index=(1,-46)
  elif not branch:target=((2,12),(-2,-14));expected_index=(1,-17)
  else:target=((-2,-33),(2,93));expected_index=(2,30)
  j=A.line_coordinate(A.psub(target,exc),d);assert j==expected_index and A.nonneg(j)
  if d==(-2,2):assert target[0]==(-2,-33)
  else:assert target[1]==(-2,-14)
  rows.append(dict(m=m,stage='three_bit' if branch else 'two_bit',certificate_sha256=hashlib.sha256(cpath.read_bytes()).hexdigest(),archive_bounds=archive,canonical_core_bounds=corebounds,finite_read_bounds=C['finite_read_bounds'],tail_fixed_normals=C['tail_fixed_normals'],exceptional_ray=C['exceptional_phase72_ray'],forced_target=target,ray_index=j,capture_time=C['capture_time']))
 assert len(rows)==4
 out=dict(status='four exact parent interfaces verified',domain='integer n>=200',rows=rows)
 (HERE/'branch_interfaces.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
