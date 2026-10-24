"""Exact localized ordinary-core corrections for four same-rail channels."""
import json,sys,hashlib
from pathlib import Path
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,DRIFT,canonical_source,step,plan,multiple,certify_period
SOURCE=ROOT/'continuation_2026-10-22/ant_continuation/one_bit_certificate_restored.json'
BASE=(-15,29)

def main():
 S=json.loads(SOURCE.read_text());rows=[]
 for r in (13,14,27,89):
  N=S['thresholds'][r];R=next(x for x in S['cases'] if x['n']==N and x['r']==r)
  B,p,h=canonical_source(N,r);B.symmetric_difference_update({p});changed_reads=[]
  for _ in range(R['steps']):
   changed_reads.append(p);p,h,_=step(B,p,h)
  assert hashlib.sha256(repr(sorted(B)).encode()).hexdigest()==R['field_sha256']
  _,rp,rh=canonical_source(0,R['phase']);k=multiple((p[0]-rp[0],p[1]-rp[1]),DRIFT);assert k is not None and h==rh and N+k>=0
  unperturbed,up,uh=canonical_source(N+k,R['phase']);unperturbed={(x+k*DRIFT[0],y+k*DRIFT[1]) for x,y in unperturbed}
  assert p==(up[0]+k*DRIFT[0],up[1]+k*DRIFT[1]) and h==uh
  tw=W[R['phase']:]+W[:R['phase']];assert certify_period(B,p,h,tw) and certify_period(unperturbed,p,h,tw)
  scar=B^unperturbed;reads,_,end,eh=plan(tw,p,h)
  for q in scar:
   for v in reads:
    j=multiple((q[0]-v[0],q[1]-v[1]),DRIFT);assert j is None or j<0
  points=sorted((BASE[0]-x,BASE[1]-y) for x,y in scar)
  read_z_absmax=max(abs(sum(BASE)-sum(q)) for q in changed_reads);assert read_z_absmax<=82
  dt=r+R['steps']-104*k-R['phase']
  rows.append(dict(phase=r,source_age=N,source_recovery=R['steps'],geometric_period_shift=k,outgoing_phase=R['phase'],time_delay=dt,scar_base=points,scar_translation_per_m=[-2,2],scar_size=len(points),changed_read_z_absmax=read_z_absmax,z_range=[min(x+y for x,y in points),max(x+y for x,y in points)],u_range_base=[min(x-y for x,y in points),max(x-y for x,y in points)],join_pose_base=[[BASE[0]-p[0],BASE[1]-p[1]],(h+2)%4]))
 out=dict(status='exact localized corrections; all larger ages use already verified ordinary age guard',rows=rows)
 (HERE/'localized_scars.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
