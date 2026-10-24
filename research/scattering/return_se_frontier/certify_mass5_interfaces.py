"""Canonical archive/sector interfaces for ten immediate mass-five exclusions."""
import sys,json,hashlib
from pathlib import Path
R=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(R/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,plan,canonical_source

def rot(q,j):
 x,y=q
 for _ in range(j%4):x,y=y,-x
 return x,y

def main():
 I=json.loads((HERE/'strip_interface.json').read_text());assert I['pre_core_read_upper']=={'u':58,'z':71}
 C=json.loads((HERE/'parallel_model_certificate.json').read_text());assert C['strip_interface_sha256']==hashlib.sha256((HERE/'strip_interface.json').read_bytes()).hexdigest();out=[]
 for row in C['records']:
  if row['finite_history_transfer']!='permanent':continue
  r=row['phase'];p,h=row['local_pose'];phase=row['word_phase'];d=tuple(row['drift'])
  assert d in ((-2,-2),(2,2))
  B0,p0,h0=canonical_source(0,phase);j=1 if d==(-2,-2) else 3
  rp0=rot(p0,j);origin=(p[0]-rp0[0],p[1]-rp0[1]);assert (h0+j)%4==h
  core=[(origin[0]+rot(q,j)[0],origin[1]+rot(q,j)[1]) for q in B0]
  archive_z=max(82,-60+row['source_z_bounds'][1],-60+max(sum(q) for q in core));assert archive_z==82
  assert -464+max(row['source_u_bounds'][1],row['tail_source_u_bounds'][1])<58
  finite_z=max(82,-60+row['source_z_bounds'][1]);assert finite_z==82
  rec=dict(phase=r,archive_z_upper=82,full_prefix_u_upper=58,full_prefix_z_upper=82,core_base=row['core_base'],drift=d)
  if d==(-2,-2):
   tail,_,_,_=plan(W[phase:]+W[:phase],tuple(p),h)
   assert -60+max(sum(q) for q in tail)<=82
   rec['exclusion']='SW output misses every remaining remote marker'
  else:
   _,_,ep,eh=plan(W[phase:],tuple(p),h);assert eh==1 and (sum(ep)+eh)%2==0
   assert [ep[0]+2,ep[1]+8]==row['opposite_exceptional_base']
   parity=[v%2 for v in row['opposite_exceptional_base']]
   rec['opposite_exceptional_parity']=parity
   rec['exclusion']='NE output forces only favorable ordinary opposite-corner hits' if parity==[1,0] else 'opposite exceptional corner still possible'
  out.append(rec)
 complete=[r['phase'] for r in out if r['exclusion']!='opposite exceptional corner still possible']
 assert complete==[29,32,38,46,47,55,56,57,62,71]
 result=dict(status='ten exact interfaces for the established global incidence reduction',excluded_phases=complete,remaining_compatible_NE=[15,45,72],records=out)
 (HERE/'mass5_interfaces.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
