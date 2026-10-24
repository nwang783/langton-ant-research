"""All-parameter complete finite three-cell continuation after central crossing."""
import sys,json,hashlib
from pathlib import Path
from full_field import A,infinite_tail,source_field,absolute_read_bounds,C,W,plan,canonical_source,HERE
M=(1,0,100);N=(1,1,200)
def main(r):
 field,O,elapsed,I=source_field(M,N);assert r in I['fresh_phases']
 qs,_,_,_=plan(W,(0,0),2);field.add_points([A.point(*qs[r])]);prefix=elapsed
 for key in A.STATS:A.STATS[key]=0
 A.READ_POINTS.clear();A.READ_RAYS.clear();p=A.point(0,0);h=2;elapsed=C(0);records=[]
 path=HERE/f'displaced_se_template_r{r}.json';T=json.loads(path.read_text());assert T['phase']==r
 standard={W[j:]+W[:j] for j in range(104)}
 for i,s in enumerate(T['segments']):
  word=s['word'];assert word and set(word)<={'R','L'};data=A.word_data(word,h)
  if s['type']=='finite':p=A.apply_finite(field,data,p,0,'finite'+str(i));elapsed=A.add(elapsed,C(len(word)))
  else:
   an,am,b=s['count_nm'];count=A.add(A.add(A.scale(N,an),A.scale(M,am)),C(b));assert word in standard and data[3]==h and A.nonneg(A.sub(count,A.ONE))
   p=A.apply_periods(field,data,p,0,count,'period'+str(i));elapsed=A.add(elapsed,A.scale(count,104))
  h=data[3];records.append(dict(segment=i,time=elapsed,pose=[p,h]));print(json.dumps(records[-1]),flush=True)
 tw=T['infinite_tail_word'];assert tw in standard;td=A.word_data(tw,h);assert td[3]==h
 expected=(2,-2) if r in (28,60) else (-2,2) if r==75 else (-2,-2);assert td[2]==expected
 tail=infinite_tail(field,td,p);bounds,tailbounds=absolute_read_bounds(O,td,p)
 phase=next(j for j in range(104) if tw==W[j:]+W[:j]);assert phase=={28:0,60:0,61:0,70:0,75:100}[r];actualp=A.padd(O,p)
 fullbounds={key:max(I['pre_core_read_upper'][key],v) for key,v in bounds.items()}
 assert fullbounds=={'u':{28:78,60:78,61:106,70:58,75:58}[r],'z':71}
 out=dict(status='exact full three-cell field and eternal standard tail',phase=r,domain='m>=100,n-m>=100',variables='u=m-100>=0,v=n-m-100>=0',source_capture_time=elapsed,source_capture_pose=[p,h],total_capture_time=A.add(prefix,elapsed),total_capture_pose=[actualp,h],tail=tail,tail_phase=phase,full_prefix_read_upper=fullbounds,tail_read_upper=tailbounds,statistics=A.STATS.copy(),records=records,template_sha256=hashlib.sha256(path.read_bytes()).hexdigest())
 if r in (28,60):
  assert phase==0 and h==2
  core,_,_=canonical_source(0,0);cmax=max(x-y for x,y in core)
  au=A.sub(actualp[0],actualp[1]);assert au[:2]==(0,0)
  out['archive_u_upper']=max(fullbounds['u'],au[2]+cmax)
  # Phase72 is the only unfavorable-for-capture favorable-color channel.
  e=(A.add(actualp[0],C(8)),A.add(actualp[1],C(-2)));assert all(v[:2]==(0,0) for v in e)
  out['SE_exceptional_c_line_z']=e[0][2]+e[1][2]
  out['forced_c_x_offset']=out['SE_exceptional_c_line_z']+14
 else:
  assert all(v is not None for v in tailbounds.values())
  out['all_future_read_upper']={key:max(fullbounds[key],tailbounds[key]) for key in fullbounds}
 (HERE/f'displaced_se_certificate_r{r}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main(int(sys.argv[1]))
