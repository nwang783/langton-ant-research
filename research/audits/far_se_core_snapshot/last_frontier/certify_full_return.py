"""Exact entire-field two-parameter closures for the five nonlocal far-SE returns."""
import sys,json,hashlib,gzip
from full_field import A,infinite_tail,source_field,C,W,plan,HERE
M=(1,0,100);N=(1,1,200)
def main(r):
 assert r in (28,60,61,70,75)
 field,O,prefix,I=source_field(M,N);assert r in I['fresh_phases']
 qs,_,_,_=plan(W,(0,0),0);core=A.point(*qs[r]);nn=lambda a,b:A.add(A.scale(N,a),C(b))
 da=(nn(2,8),nn(2,41));ds=A.psub(da,O);assert A.negative(A.sub(C(71),A.add(da[0],da[1])))
 field.add_points([core,ds])
 for key in A.STATS:A.STATS[key]=0
 A.READ_POINTS.clear();A.READ_RAYS.clear();p=A.point(0,0);h=0;elapsed=C(0);records=[]
 path=HERE/f'full_return_template_r{r}.json';T=json.loads(path.read_text());assert T['phase']==r
 model=json.loads((HERE/'parallel_model_certificate.json').read_text());assert model['strip_interface_sha256']==hashlib.sha256((HERE/'strip_interface.json').read_bytes()).hexdigest()
 row=next(q for q in model['records'] if q['phase']==r)
 modelword=gzip.open(HERE/f'word_r{r}_mature1.txt.gz','rt').read()
 assert hashlib.sha256(modelword.encode()).hexdigest()==row['word_sha256']
 assert T['segments'][0]['type']=='finite' and modelword.startswith(T['segments'][0]['word'])
 assert T['segments'][0]['word'][:r]==W[:r] and T['segments'][0]['word'][r]!=W[r]
 standard={W[j:]+W[:j] for j in range(104)}
 for i,s in enumerate(T['segments']):
  word=s['word'];assert word and set(word)<={'R','L'};data=A.word_data(word,h)
  if s['type']=='finite':p=A.apply_finite(field,data,p,0,'finite'+str(i));elapsed=A.add(elapsed,C(len(word)))
  else:
   an,am,b=s['count_nm'];count=A.add(A.add(A.scale(N,an),A.scale(M,am)),C(b));assert word in standard and data[3]==h and A.nonneg(A.sub(count,A.ONE))
   p=A.apply_periods(field,data,p,0,count,'period'+str(i));elapsed=A.add(elapsed,A.scale(count,104))
  h=data[3];records.append(dict(segment=i,time=elapsed,pose=[p,h]));print(json.dumps(records[-1]),flush=True)
 tw=T['infinite_tail_word'];assert tw in standard;td=A.word_data(tw,h);assert td[3]==h
 assert td[2]==((2,-2) if r==46 else (-2,-2) if r==70 else (-2,2))
 tail=infinite_tail(field,td,p)
 # A separate all-future z bound rules out the remaining initial d forever.
 def zupper(v):assert v[0]<=0 and v[1]<=0,('unbounded z',v);return v[2]
 vals=[71]
 for q in A.READ_POINTS:
  actual=A.padd(O,q);vals.append(zupper(A.add(actual[0],actual[1])))
 for b,d,count in A.READ_RAYS:
  actual=A.padd(O,b);v=A.add(actual[0],actual[1]);speed=sum(d)
  if speed>0:v=A.add(v,A.scale(A.sub(count,A.ONE),speed))
  vals.append(zupper(v))
 assert sum(td[2])<=0
 for q in td[0]:
  actual=A.padd(O,A.translate_local(q,p,0));vals.append(zupper(A.add(actual[0],actual[1])))
 zbound=max(vals);assert A.negative(A.sub(C(zbound),A.add(da[0],da[1])))
 out=dict(status='complete finite five-cell family with eternal standard tail',phase=r,domain='m>=100,n-m>=100',variables='u=m-100>=0,v=n-m-100>=0',source_capture_time=elapsed,total_capture_time=A.add(prefix,elapsed),total_capture_pose=[A.padd(O,p),h],tail=tail,tail_phase=next(j for j in range(104) if tw==W[j:]+W[:j]),all_future_z_upper=zbound,remote_d_never_read=True,statistics=A.STATS.copy(),records=records,template_sha256=hashlib.sha256(path.read_bytes()).hexdigest())
 assert out['tail_phase']=={28:100,38:100,46:100,60:100,61:0,70:99,75:100}[r]
 assert zbound=={28:77,38:71,46:79,60:97,61:123,70:89,75:81}[r]
 (HERE/f'full_return_certificate_r{r}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main(int(sys.argv[1]))
