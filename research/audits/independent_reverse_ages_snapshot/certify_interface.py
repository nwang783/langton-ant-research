"""Exact half-plane stabilization of complete one-bit blank-parent fields.

Geometry/XOR corollary of the already color-certified exceptional rectangle.
It does not replace its color validation or infer it from parameter samples.
"""
import sys,json,hashlib,math
from pathlib import Path
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,P,plan
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation/wake_clock'))
import certify_four_scatterer_prefix as A
TFILE=ROOT/'continuation_2026-10-22/ant_continuation2/planar_structure/exceptional_rectangle_template.json'
Z=-250

def main():
 A.LOW=200;assert hashlib.sha256(TFILE.read_bytes()).hexdigest()=='16246ec40cbdd4ad94c35698992582b27a942dc7d539683f1b3684892cd5687d'
 certificate=TFILE.with_name('exceptional_rectangle_affine_certificate.json')
 assert hashlib.sha256(certificate.read_bytes()).hexdigest()=='e59bf6b1cf859383a9dd61a8915852e878fb9bca71e7559c846c57655342a1f4'
 source=json.loads(certificate.read_text());assert source['parameter_minimum']==200 and source['initial_cell_first_read_times']['a_northwest']==[312,71330]
 assert source['segments'][4]['one_bit_infinite_tail']=={'distinct_required_cells':44,'odd_read_cells':36,'drift':[-2,2],'heading':1}
 assert source['segments'][8]['two_bit_infinite_tail']=={'distinct_required_cells':44,'odd_read_cells':36,'drift':[2,-2],'heading':2}
 T=json.loads(TFILE.read_text());field=A.Field([((-2,-33),(-2,-14))]);p=A.point(0,0);h=0;elapsed=A.ZERO;lower_u=10**9;upper_u=-10**9
 for i,s in enumerate(T['segments'][:5]):
  assert s['type'] in ('finite','periods');word=s['word'];assert word and set(word)<={'R','L'};reads,_,end,eh=plan(word,(0,0),h);_,odd,_,_=A.word_data(word,h)
  count=None if s['type']=='finite' else tuple(s['count'])
  if count:assert len(word)==104 and eh==h and A.nonneg(A.sub(count,A.ONE))
  for b in reads:
   q=A.translate_local(b,p,0);u=A.sub(q[0],q[1]);speed=end[0]-end[1]
   hi=u
   if count and speed>0:hi=A.add(hi,A.scale(A.sub(count,A.ONE),speed))
   if count and speed<0:u=A.add(u,A.scale(A.sub(count,A.ONE),speed))
   assert u[0]>=0 and hi[0]<=0;lower_u=min(lower_u,A.val(u));upper_u=max(upper_u,A.val(hi))
  if count is None:field.add_points(A.translate_local(q,p,0) for q in odd);p=A.translate_local(end,p,0);elapsed=A.add(elapsed,(0,len(word)))
  else:field.add_rays([A.translate_local(q,p,0) for q in odd],end,count,'segment'+str(i));p=A.padd(p,(A.scale(count,end[0]),A.scale(count,end[1])));elapsed=A.add(elapsed,A.scale(count,104))
  h=eh
 assert p==A.point(-15,26) and h==1 and elapsed==(208,70733) and lower_u==-82 and upper_u==58
 # Restrict every complete-field XOR component to z>=Z. The surviving
 # segment endpoints become fixed after reindexing, proving exact equality
 # of the ENTIRE half-plane fields for every n>=200.
 restricted=set();components=[]
 for q in field.points:
  v=A.add(q[0],q[1])
  if v[0]==0:
   if v[1]>=Z:
    assert q[0][0]==q[1][0]==0;restricted.symmetric_difference_update({(q[0][1],q[1][1])})
  else:assert A.negative(A.sub(v,(0,Z)))
 for base,d,count,label in field.rays:
  vz=sum(d);a,b=A.add(base[0],base[1]);assert vz in (-4,4) and a%vz==0
  if vz>0:
   lo=A.maximum(A.ZERO,(-a//vz, -((b-Z)//vz)))
   hi=A.sub(count,A.ONE)
  else:
   lo=A.ZERO;hi=A.minimum(A.sub(count,A.ONE),(-a//vz,(b-Z)//(-vz)))
  assert A.nonneg(A.sub(hi,lo)) and hi[0]==lo[0]
  start=A.padd(base,(A.scale(lo,d[0]),A.scale(lo,d[1])));assert start[0][0]==start[1][0]==0
  length=hi[1]-lo[1]+1;assert length>0
  for j in range(length):restricted.symmetric_difference_update({(start[0][1]+j*d[0],start[1][1]+j*d[1])})
  components.append(dict(start=[start[0][1],start[1][1]],drift=d,length=length,label=label))
 assert all(sum(q)>=Z for q in restricted)
 # The complete two-bit parent after this boundary never leaves the region.
 # Include the whole remaining finite/repeated prefix and the infinite tail.
 lower_z=10**9;upper_z=-10**9;two_prefix_upper_u=upper_u
 for i,s in enumerate(T['segments'][5:9],5):
  assert s['type'] in ('finite','periods');word=s['word'];assert set(word)<={'R','L'};reads,_,end,eh=plan(word,(0,0),h);count=None if s['type']=='finite' else tuple(s['count'])
  if count:assert len(word)==104 and eh==h
  for b in reads:
   q=A.translate_local(b,p,0);v=A.add(q[0],q[1]);speed=sum(end)
   if count and speed<0:v=A.add(v,A.scale(A.sub(count,A.ONE),speed))
   hi=A.add(q[0],q[1])
   if count and speed>0:hi=A.add(hi,A.scale(A.sub(count,A.ONE),speed))
   uv=A.sub(q[0],q[1]);uvspeed=end[0]-end[1]
   if count and uvspeed>0:uv=A.add(uv,A.scale(A.sub(count,A.ONE),uvspeed))
   assert v[0]>=0 and hi[0]<=0 and uv[0]<=0;lower_z=min(lower_z,A.val(v));upper_z=max(upper_z,A.val(hi));two_prefix_upper_u=max(two_prefix_upper_u,A.val(uv))
  if count is None:p=A.translate_local(end,p,0);elapsed=A.add(elapsed,(0,len(word)))
  else:p=A.padd(p,(A.scale(count,end[0]),A.scale(count,end[1])));elapsed=A.add(elapsed,A.scale(count,104))
  h=eh
 assert p==A.point(40,-50) and h==2 and elapsed==(416,146040)
 tw=T['segments'][9]['word'];assert tw==W[100:]+W[:100];qs,_,end,eh=plan(tw,(0,0),h);assert end==(2,-2) and eh==h
 for q in qs:
  actual=A.translate_local(q,p,0);v=A.add(actual[0],actual[1]);assert v[0]==0;lower_z=min(lower_z,A.val(v));upper_z=max(upper_z,A.val(v))
 assert lower_z==-93 and lower_z>=Z and upper_z==71 and two_prefix_upper_u==98
 qs,_,phase0,hh=plan(tw[:4],(40,-50),2);assert phase0==(40,-52) and hh==2
 assert max(x-y for x,y in qs)<=98 and max(phase0[0]+x-phase0[1]-y for x,y in P)==98
 # The second marker a_n has u=-74-4n, strictly outside every q_m prefix.
 assert -74-4*200<lower_u
 out=dict(status='exact complete-field half-plane stabilization and independent-age transfer',domain='independent integers m,n>=200',source_boundary={'time_for_q_index_i':[208,70733],'pose':[[-15,26],1]},comparison_halfplane_z_lower=Z,restricted_field_size=len(restricted),restricted_field_sha256=hashlib.sha256(repr(sorted(restricted)).encode()).hexdigest(),pre_boundary_u_lower=lower_u,pre_boundary_u_upper=upper_u,two_bit_future_z_lower=lower_z,two_bit_future_z_upper=upper_z,two_bit_prefix_and_archive_u_upper=two_prefix_upper_u,initial_seed={'q_m':[[-2,-33],[-2,-14]],'a_n':[[-2,-33],[2,41]]},capture_time_m_n_constant=[208,208,146040],capture_pose=[[40,-50],2],tail_phase=100,drift=[2,-2],source_template_sha256=hashlib.sha256(TFILE.read_bytes()).hexdigest(),scope='Analytic first-difference transfer between previously color-certified parent families. The two source ages are independent; this is not a general finite-history theorem.')
 (HERE/'interface.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));return restricted
if __name__=='__main__':main()
