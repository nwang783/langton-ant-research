"""Exact local parallel-rail model and finite-history transfer obligations."""
import sys,json,gzip,hashlib
from pathlib import Path
R=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(R/'continuation_2026-10-22/ant_continuation'))
sys.path.insert(0,str(R/'scattering/transverse'))
from ant_exact import P,D,W,plan,PHASES,canonical_source
import crossing as c

def main():
 source=json.loads((HERE/'parallel_model_discovery.json').read_text())
 rows=[r for r in source if r['mature']]
 interface=json.loads((HERE/'strip_interface.json').read_text())
 assert len(rows)==22 and sorted(r['r'] for r in rows)==interface['fresh_phases']
 assert interface['strip_u']==[-200,200] and interface['old_rail_offset']==[47,27]
 reads,_,_,_=plan(W,(0,0),2);NW=(-2,2)
 rays=[((d[0]-2,d[1]+2),NW,0,None) for d in D]+[((47-d[0],27-d[1]),NW,None,None) for d in D]
 assert c.tail(c.Field(rays,P),(0,0),2,W)
 records=[]
 for row in rows:
  r=row['r'];B=set(P);B.symmetric_difference_update({reads[r]});f=c.Field(rays,B)
  word=gzip.open(HERE/row['word_file'],'rt').read();assert len(word)==row['capture'] and set(word)<={'R','L'}
  p=(0,0);h=2;qs=[]
  for t,expected in enumerate(word):
   qs.append(p)
   direct=False
   for b,d,lo,hi in rays:
    k=c.multiple(c.minus(p,b),d);direct^=k is not None and (lo is None or k>=lo) and (hi is None or k<=hi)
   assert direct==f.background(p)
   p,h,actual=f.step(p,h);assert actual==expected,(r,t)
   if t<r:assert actual==W[t]
   elif t==r:assert actual!=W[t]
  assert (list(p),h)==(row['pose'][0],row['pose'][1])
  tw=row['tail_word'];phase=row['phase'];assert tw==W[phase:]+W[:phase]
  proof=c.tail(f,p,h,tw);assert proof and list(proof['drift'])==row['drift']
  tailqs,end,eh=c.trace(tw,h,p);drift=c.minus(end,p);assert eh==h
  ub=[min(x-y for x,y in qs),max(x-y for x,y in qs)]
  zb=[min(x+y for x,y in qs),max(x+y for x,y in qs)]
  assert ub==row['u_bounds'] and zb==row['z_bounds']
  assert -200<=ub[0]<=ub[1]<=200
  eternal=drift[0]==drift[1]
  tail_u=[min(x-y for x,y in tailqs),max(x-y for x,y in tailqs)]
  if eternal:assert -200<=tail_u[0]<=tail_u[1]<=200
  rec=dict(phase=r,core_base=[-62+reads[r][0],2+reads[r][1]],local_capture=row['capture'],local_pose=[p,h],word_phase=phase,drift=drift,source_u_bounds=ub,source_z_bounds=zb,tail_source_u_bounds=tail_u,finite_history_transfer='permanent' if eternal else 'finite recovery only',word_sha256=hashlib.sha256(word.encode()).hexdigest())
  if drift==(2,2):
   _,_,ep,eh=plan(W[phase:],p,h);assert eh==1
   exceptional=(ep[0]+2,ep[1]+8)
   rec['opposite_exceptional_base']=exceptional;rec['opposite_exceptional_parity']=[v%2 for v in exceptional]
  records.append(rec);print(json.dumps(rec),flush=True)
 assert [r['phase'] for r in records if r['finite_history_transfer']=='permanent']==[15,29,32,38,45,46,47,55,56,57,62,71,72]
 result=dict(status='all22 exact local models;13 complete finite three-cell permanent transfers',domain='m>=100,n-m>=100',time_base=[416,-104,122376],actual_pose_origin=[[-2,-62],[2,2]],records=records,strip_interface_sha256=hashlib.sha256((HERE/'strip_interface.json').read_bytes()).hexdigest())
 (HERE/'parallel_model_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()
