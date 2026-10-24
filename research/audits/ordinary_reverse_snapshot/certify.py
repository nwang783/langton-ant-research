"""Exact all-k complete finite-kernel proof and arbitrary-archive interface.

Uses the previously audited one-variable XOR engine. No sampled orbit supplies
an acceptance condition. Every word, including the infinite tail, is replayed
symbolically from the complete finite field P XOR 42 deposits XOR two bits.
"""
import sys,json,hashlib
from pathlib import Path
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import P,D,W,plan,canonical_source,step,certify_period
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation/wake_clock'))
import certify_four_scatterer_prefix as A
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation2/planar_structure'))
from certify_exceptional_rectangle import verify_infinite_period
SOURCE=ROOT/'continuation_2026-10-22/ant_continuation/one_bit_certificate_restored.json'
FRESH=[13,14,15,27,28,29,32,38,45,46,47,55,56,57,60,61,62,70,71,75,89]
Q,_,_,_=plan(W,(0,0),2)
u=lambda q:q[0]-q[1];z=lambda q:sum(q)
def main(r):
 assert r in FRESH;A.LOW=100;A.READ_POINTS.clear();A.READ_RAYS.clear()
 for key in A.STATS:A.STATS[key]=0
 S=json.loads(SOURCE.read_text());age=S['thresholds'][r];R=next(x for x in S['cases'] if x['n']==age and x['r']==r)
 B,p,h=canonical_source(age,r);assert p==Q[r] and p not in B;B.add(p)
 for _ in range(R['steps']):p,h,ch=step(B,p,h)
 assert list(p)==R['position'] and h==R['heading'] and hashlib.sha256(repr(sorted(B)).encode()).hexdigest()==R['field_sha256']
 phase=R['phase'];tw=W[phase:]+W[:phase];ordinary=certify_period(B,p,h,tw);assert ordinary and list(ordinary['drift'])==R['tail']['drift']
 delta=(72-phase)%104;ex=plan(tw[:delta],p,h)[2];d=ordinary['drift'];q2=((d[0],ex[0]),(d[1],ex[1]));targettime=(104,r+R['steps']+delta)
 # The complete finite kernel has 42 old deposits. Any older canonical
 # deposit is entirely below u=-160. It is not silently discarded.
 assert max(map(u,D))-4*43 < -160
 clean,cp,ch=canonical_source(42,0);assert certify_period(clean,cp,ch,W)
 field=A.Field({A.point(*b) for b in P});field.add_rays([A.point(b[0]-2,b[1]+2) for b in D],(-2,2),(0,42),'complete42olddeposits')
 field.add_points([A.point(*Q[r]),q2]);p=A.point(0,0);h=2;elapsed=A.ZERO;records=[];hits=[]
 path=HERE/f'template_r{r}.json';T=json.loads(path.read_text());assert T['phase']==r;standard={W[i:]+W[:i] for i in range(104)}
 assert T['segments'][0]['word'][:r]==W[:r] and T['segments'][0]['word'][r]!=W[r]
 for i,s in enumerate(T['segments']):
  assert s['type'] in ('finite','periods');word=s['word'];assert word and set(word)<={'R','L'};data=A.word_data(word,h)
  reads,_,_,_=plan(word,(0,0),h)
  for j,b in enumerate(reads):
   actual=A.translate_local(b,p,0)
   if s['type']=='finite':
    if actual==q2:hits.append(A.add(elapsed,(0,j)))
    else:A.no_point_collision(actual,q2)
   else:
    count=tuple(s['count']);k=A.line_coordinate(A.psub(q2,actual),data[2])
    if k is not None and A.in_range(k,count):hits.append(A.add(elapsed,A.add(A.scale(k,104),(0,j))))
  if s['type']=='finite':p=A.apply_finite(field,data,p,0,'finite'+str(i));elapsed=A.add(elapsed,(0,len(word)))
  else:
   count=tuple(s['count']);assert word in standard and len(word)==104 and data[3]==h and A.nonneg(A.sub(count,A.ONE))
   p=A.apply_periods(field,data,p,0,count,'period'+str(i));elapsed=A.add(elapsed,A.scale(count,104))
  h=data[3];records.append(dict(segment=i,time=elapsed,pose=[p,h]));print(json.dumps(records[-1]),flush=True)
 assert hits
 first=hits[0]
 for t in hits[1:]:first=A.minimum(first,t)
 assert first==targettime
 word=T['infinite_tail_word'];assert word in standard;data=A.word_data(word,h);assert data[3]==h
 cert=verify_infinite_period(field,data,p);drift=data[2]
 # Sharp uniform lower bound through tail entry, accounting for both endpoints
 # of every long period interval. This guards all omitted older deposits.
 lower=0
 def bound(q,d=(0,0),count=None):
  nonlocal lower
  val=A.sub(q[0],q[1]);speed=u(d)
  if count is not None and speed<0:val=A.add(val,A.scale(A.sub(count,A.ONE),speed))
  assert val[0]>=0,('unbounded negative prefix',r,val)
  lower=min(lower,A.val(val))
 for q in A.READ_POINTS:bound(q)
 for base,d,count in A.READ_RAYS:bound(base,d,count)
 assert lower>=-160
 qs,_,_,_=plan(word,(0,0),h);tail_u=[];tail_z=[]
 for b in qs:
  actual=A.translate_local(b,p,0);uu=A.sub(actual[0],actual[1]);zz=A.add(actual[0],actual[1]);assert uu[0]>=0
  tail_u.append(A.val(uu));tail_z.append(zz)
 forward=u(drift)>=0
 if forward:lower=min(lower,min(tail_u));assert lower>=-160
 else:
  assert drift==(-2,2) and all(v[0]==0 for v in tail_z)
  # The escaping reverse tail misses the infinite omitted canonical rail,
  # but arbitrary finite history in the same transverse band may still hit it.
  assert min(v[1] for v in tail_z)>max(map(z,D))
 out=dict(status='exact all-k complete finite-kernel capture',phase=r,domain='integer k>=100',input_old_deposit_count=42,second_marker_affine=q2,second_first_hit=first,capture_time=elapsed,capture_pose=[p,h],tail=cert,tail_phase=next(j for j in range(104) if word==W[j:]+W[:j]),whole_future_forward_guard=forward,prefix_u_lower=lower,full_future_u_lower=lower if forward else None,tail_z_bounds=[min(v[1] for v in tail_z),max(v[1] for v in tail_z)] if all(v[0]==0 for v in tail_z) and z(drift)==0 else None,records=records,source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),template_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),statistics=A.STATS.copy(),scope='All older canonical deposits are avoided. Arbitrary finite history contained in u<-160 is protected iff whole_future_forward_guard is true; the other cases need a return/endcap condition.')
 (HERE/f'certificate_r{r}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main(int(sys.argv[1]))
