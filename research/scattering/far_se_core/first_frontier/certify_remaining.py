"""Exact bivariate complete-history proofs, not model-to-finite extrapolation."""
import sys,json,hashlib
from full_field import A,infinite_tail,source_field,C,W,plan,HERE
M=(1,0,100);N=(1,1,200)
def main(r):
 assert r in (72,70,75,46,47,57)
 field,O,prefix,I=source_field(M,N);nn=lambda a,b:A.add(A.scale(N,a),C(b))
 qs,_,_,_=plan(W,(0,0),2);core=A.point(*qs[r]);field.add_points([core]);corners={}
 if r!=72:
  x=A.add(nn(2,138 if r==57 else 134),A.scale(M,4)) if r in (46,47,57) else nn(2,-8 if r==70 else 4)
  corners={'c':(x,nn(-2,-14)),'d':(x,nn(2,41))}
  assert A.negative(A.sub(A.add(A.scale(M,4),C(98)),A.sub(corners['c'][0],corners['c'][1])))
  assert A.negative(A.sub(C(71),A.add(corners['d'][0],corners['d'][1])))
  field.add_points(A.psub(q,O) for q in corners.values())
 for key in A.STATS:A.STATS[key]=0
 A.READ_POINTS.clear();A.READ_RAYS.clear();p=A.point(0,0);h=2;elapsed=C(0);records=[]
 path=HERE/f'full_remaining_template_r{r}.json';T=json.loads(path.read_text());assert T['phase']==r
 assert T['segments'][0]['word'][:r]==W[:r] and T['segments'][0]['word'][r]!=W[r]
 standard={W[j:]+W[:j] for j in range(104)};hit=None
 for i,s in enumerate(T['segments']):
  word=s['word'];assert word and set(word)<={'R','L'};data=A.word_data(word,h)
  if i==2 and r!=72:
   k=73 if r==57 else 77;reads,_,_,_=plan(word,(0,0),h);target=corners['c' if r in (70,75) else 'd'];assert A.padd(O,A.translate_local(reads[k],p,0))==target
   hit=A.add(elapsed,C(k));expected=A.add(A.scale(A.sub(N,M) if r in (70,75) else A.add(N,M),104),C({70:5064,75:900,46:4959,47:5003,57:5167}[r]));assert hit==expected
  if s['type']=='finite':p=A.apply_finite(field,data,p,0,'finite'+str(i));elapsed=A.add(elapsed,C(len(word)))
  else:
   an,am,b=s['count_nm'];count=A.add(A.add(A.scale(N,an),A.scale(M,am)),C(b));assert word in standard and data[3]==h and A.nonneg(A.sub(count,A.ONE))
   p=A.apply_periods(field,data,p,0,count,'period'+str(i));elapsed=A.add(elapsed,A.scale(count,104))
  h=data[3];records.append(dict(segment=i,time=elapsed,pose=[p,h]));print(json.dumps(records[-1]),flush=True)
 tw=T['infinite_tail_word'];assert tw in standard;td=A.word_data(tw,h);assert td[3]==h
 assert td[2]==((-2,2) if r in (72,75) else (2,2) if r==70 else (-2,-2))
 tail=infinite_tail(field,td,p);bounds={};unread=[]
 if r==72:
  bounds={'u_minus_4m':98,'z':71}
  def record(q,drift=(0,0),count=None):
   q=A.padd(O,q)
   for typ in bounds:
    v=A.sub(A.sub(q[0],q[1]),A.scale(M,4)) if typ=='u_minus_4m' else A.add(q[0],q[1]);speed=drift[0]-drift[1] if typ=='u_minus_4m' else sum(drift)
    if count is not None and speed>0:v=A.add(v,A.scale(A.sub(count,A.ONE),speed))
    assert v[0]<=0 and v[1]<=0;(None)
    bounds[typ]=max(bounds[typ],v[2])
  for q in A.READ_POINTS:record(q)
  for b,d,count in A.READ_RAYS:record(b,d,count)
  assert td[2]==(-2,2)
  for q in td[0]:record(A.translate_local(q,p,0))
 else:
  name='d' if r in (70,75) else 'c';target=A.psub(corners[name],O)
  for q in A.READ_POINTS:assert A.no_point_collision(q,target)
  for b,d,count in A.READ_RAYS:assert not A.ray_membership(target,b,d,count)
  for q in td[0]:
   k=A.line_coordinate(A.psub(target,A.translate_local(q,p,0)),td[2]);assert k is None or A.negative(k)
  unread.append(name)
 out=dict(status='exact complete-history permanent standard capture',phase=r,domain='m>=100,n-m>=100',initial_cell_count=3 if r==72 else 5,source_capture_time=elapsed,total_capture_time=A.add(prefix,elapsed),total_capture_pose=[A.padd(O,p),h],tail=tail,tail_phase=next(j for j in range(104) if tw==W[j:]+W[:j]),whole_trajectory_upper=bounds,remote_never_read=unread,forced_corner_source_hit_time=hit,statistics=A.STATS.copy(),records=records,interface_sha256=hashlib.sha256((HERE/'clean_interface.json').read_bytes()).hexdigest(),template_sha256=hashlib.sha256(path.read_bytes()).hexdigest())
 (HERE/f'remaining_certificate_r{r}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main(int(sys.argv[1]))
