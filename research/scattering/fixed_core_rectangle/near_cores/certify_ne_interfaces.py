"""Geometry/canonical-core side of nine independently certified NE parents."""
import json,sys,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation')
from ant_exact import canonical_source,certify_period,plan,W,PHASES

def rot(p,j):
 for _ in range(j%4):p=p[1],-p[0]
 return p

def main():
 rows=[]
 for m in (0,2,3,4,5,7,8,9,10):
  path=HERE/f'certificate_m{m}.json';C=json.loads(path.read_text());T=json.loads((HERE/f'template_m{m}.json').read_text())
  assert C['status']=='exact complete-field all-n proof passed' and C['domain']=='integer n>=200' and C['m']==m
  assert C['template_sha256']==hashlib.sha256((HERE/f'template_m{m}.json').read_bytes()).hexdigest()
  assert T['pose_coeff']==[0,0];p=tuple(T['pose_constant']);h=T['heading'];tw=T['infinite_tail_word'];phase=PHASES[tw]
  B,bp,bh=canonical_source(0,phase);r=(h-bh)%4;bp=rot(bp,r);delta=(p[0]-bp[0],p[1]-bp[1])
  clean={(rot(q,r)[0]+delta[0],rot(q,r)[1]+delta[1]) for q in B}
  assert certify_period(clean,p,h,tw)['drift']==(2,2)
  assert all(v is not None for k,v in C['finite_read_bounds'].items() if k in ('u_lower','u_upper','z_upper'))
  assert C['complete_field_support_bounds']['z_upper'] is not None
  qs,hs,end,eh=plan(tw,p,h);assert end==(p[0]+2,p[1]+2) and eh==h
  assert C['tail_fixed_normals']['u']==[min(x-y for x,y in qs),max(x-y for x,y in qs)]
  _,_,exc,_=plan(tw[:(72-phase)%104],p,h)
  assert C['exceptional_phase72_ray']==[[[0,exc[0]],[0,exc[1]]],[2,2]]
  assert tuple(v%2 for v in exc)==(1,0)
  # A positive opposite rectangle corner shares neither q parity: q=(odd,even), d=(even,odd).
  archive_z_upper=max(C['complete_field_support_bounds']['z_upper'],max(x+y for x,y in clean))
  rows.append(dict(m=m,certificate_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),capture_time=C['capture_time'],pose=[p,h],phase=phase,finite_read_bounds=C['finite_read_bounds'],tail_u_bounds=C['tail_fixed_normals']['u'],phase72_ray=[exc,[2,2]],archive_z_upper=archive_z_upper,canonical_core_z_upper=max(x+y for x,y in clean)))
 assert len(rows)==9
 out=dict(status='nine NE capture interfaces verified from exact parent certificates',domain='integer n>=200; m in {0,2,3,4,5,7,8,9,10}',rows=rows)
 (HERE/'ne_interfaces.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
