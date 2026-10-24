"""Complete five-cell cycle closures for both central-crossing SE branches."""
import sys,json,hashlib
from full_field import A,infinite_tail,source_field,C,W,plan,HERE
M=(1,0,100);N=(1,1,200)
def main(r):
 assert r in (28,60);off={28:-40,60:-52}[r]
 field,O,prefix,I=source_field(M,N);assert r in I['fresh_phases']
 qs,_,_,_=plan(W,(0,0),2);core=A.point(*qs[r]);nn=lambda a,b:A.add(A.scale(N,a),C(b))
 ca=(nn(2,off),nn(-2,-14));da=(nn(2,off),nn(2,41));cs=A.psub(ca,O);ds=A.psub(da,O)
 assert A.negative(A.sub(C(58),A.sub(ca[0],ca[1]))) and A.negative(A.sub(C(71),A.add(da[0],da[1])))
 field.add_points([core,cs,ds])
 parentpath=HERE/f'displaced_se_certificate_r{r}.json';parent=json.loads(parentpath.read_text());assert parent['phase']==r and parent['tail_phase']==0 and parent['tail']['drift']==[2,-2]
 assert parent['forced_c_x_offset']==off
 pp,ph=parent['total_capture_pose'];assert ph==2 and all(v[:2]==[0,0] for v in pp);pp=tuple(v[2] for v in pp)
 assert A.negative(A.sub(C(parent['full_prefix_read_upper']['u']),A.sub(ca[0],ca[1])))
 assert A.negative(A.sub(C(parent['full_prefix_read_upper']['z']),A.add(da[0],da[1])))
 reads,_,_,_=plan(W,pp,2);assert max(sum(q) for q in reads)<A.add(da[0],da[1])[2]
 j=A.add(N,C((pp[1]+12)//2));assert (pp[1]+12)%2==0 and A.nonneg(j)
 assert ca==(A.add(C(pp[0]+8),A.scale(j,2)),A.add(C(pp[1]-2),A.scale(j,-2)))
 constants=[]
 for i,q in enumerate(reads):
  delta=(pp[0]+8-q[0],pp[1]-2-q[1])
  if delta[0]==-delta[1] and delta[0]%2==0:constants.append(104*(delta[0]//2)+i)
 assert min(constants)==72
 firstc=A.add(tuple(parent['total_capture_time']),A.add(A.scale(j,104),C(72)))
 for key in A.STATS:A.STATS[key]=0
 A.READ_POINTS.clear();A.READ_RAYS.clear();p=A.point(0,0);h=2;elapsed=C(0);records=[]
 path=HERE/f'displaced_se_cycle_template_r{r}.json';T=json.loads(path.read_text());assert T['phase']==r
 standard={W[j:]+W[:j] for j in range(104)}
 for i,s in enumerate(T['segments']):
  word=s['word'];assert word and set(word)<={'R','L'};data=A.word_data(word,h)
  if s['type']=='finite':p=A.apply_finite(field,data,p,0,'finite'+str(i));elapsed=A.add(elapsed,C(len(word)))
  else:
   an,am,b=s['count_nm'];count=A.add(A.add(A.scale(N,an),A.scale(M,am)),C(b));assert word in standard and data[3]==h and A.nonneg(A.sub(count,A.ONE))
   p=A.apply_periods(field,data,p,0,count,'period'+str(i));elapsed=A.add(elapsed,A.scale(count,104))
  h=data[3];records.append(dict(segment=i,time=elapsed,pose=[p,h]));print(json.dumps(records[-1]),flush=True)
 tw=T['infinite_tail_word'];assert tw in standard;td=A.word_data(tw,h);assert td[3]==h and td[2]==((2,2) if r==28 else (-2,-2))
 tail=infinite_tail(field,td,p)
 for q in A.READ_POINTS:assert A.no_point_collision(q,ds)
 for b,d,count in A.READ_RAYS:assert not A.ray_membership(ds,b,d,count)
 for q in td[0]:
  b=A.translate_local(q,p,0);v=A.line_coordinate(A.psub(ds,b),td[2]);assert v is None or A.negative(v)
 out=dict(status='complete finite five-cell cycle with eternal standard tail',phase=r,domain='m>=100,n-m>=100',variables='u=m-100>=0,v=n-m-100>=0',forced_c_x_offset=off,first_c_read_time=firstc,first_c_phase=72,source_capture_time=elapsed,total_capture_time=A.add(prefix,elapsed),total_capture_pose=[A.padd(O,p),h],tail=tail,tail_phase=next(j for j in range(104) if tw==W[j:]+W[:j]),remote_d_never_read=True,statistics=A.STATS.copy(),records=records,template_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),parent_certificate_sha256=hashlib.sha256(parentpath.read_bytes()).hexdigest())
 (HERE/f'displaced_se_cycle_certificate_r{r}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main(int(sys.argv[1]))
