"""All m,k>=100 proof from the complete two-black-cell initial seed."""
import sys,json,hashlib
from pathlib import Path
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'scattering/fixed_core_rectangle'))
from bivariate import A,infinite_tail
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,plan
M=(1,0,100);K=(0,1,100);C=lambda x:(0,0,x)
def linear(a,b,c):return A.add(A.add(A.scale(M,a),A.scale(K,b)),C(c))
def main():
 cap=next(r for r in json.loads((HERE/'fixed_caps.json').read_text())['rows'] if r['phase']==28)
 bridge=json.loads((HERE/'bridge.json').read_text());assert bridge['fixed_caps_sha256']==hashlib.sha256((HERE/'fixed_caps.json').read_bytes()).hexdigest()
 entry=next(r for r in bridge['rows'] if r['phase']==28);assert entry['cap_start']==cap['start'] and entry['cap_entry_time_m_k_constant']==[208,208,65457]
 R=json.loads((ROOT/'scattering/ordinary_reverse_interface/certificate_r28.json').read_text());Q,_,_,_=plan(W,(0,0),2);q=Q[28];ex,ey=R['second_marker_affine'];assert ex[0]==2 and ey[0]==-2
 first=(linear(-2,0,-15+q[1]),linear(-2,0,10-q[0]));second=(linear(-2,-2,-15+ey[1]),linear(-2,-2,10-ex[1]));field=A.Field([first,second]);assert len(field.points)==2 and A.no_point_collision(first,second)
 for key in A.STATS:A.STATS[key]=0
 A.READ_POINTS.clear();A.READ_RAYS.clear();p=A.point(0,0);h=0;elapsed=C(0);records=[]
 path=HERE/'r28_complete_template.json';T=json.loads(path.read_text());standard={W[j:]+W[:j] for j in range(104)};failure=None
 for i,s in enumerate(T['segments']):
  word=s['word'];assert word and set(word)<={'R','L'} and s['type'] in ('finite','periods');data=A.word_data(word,h)
  if i==8:
   assert word[:56]==W[:56] and word[56]=='L' and W[56]=='R'
   reads,_,_,_=plan(word,(0,0),h);point=A.translate_local(reads[56],p,0);assert point==(linear(-2,0,8),linear(-2,0,-5));failure=A.add(elapsed,C(56));assert failure==linear(312,208,72723)
  if s['type']=='finite':p=A.apply_finite(field,data,p,0,'finite'+str(i));elapsed=A.add(elapsed,C(len(word)))
  else:
   assert word in standard and len(word)==104 and data[3]==h;count=linear(*s['count_mk']);assert A.nonneg(A.sub(count,A.ONE))
   if i==7:
    assert word==W and s['count_mk']==[1,0,-8] and elapsed==linear(208,208,73499) and p==A.point(-4,-15) and h==3
    cap_time=linear(*entry['cap_entry_time_m_k_constant']);cap_time=A.add(cap_time,C(cap['capture']));offset=A.sub(cap_time,elapsed);assert offset==C(382)
    _,_,cp,ch=plan(W*3+W[:70],(-4,-15),3);assert [list(cp),ch]==cap['pose'] and cap['tail_phase']==70 and cap['drift']==[-2,-2]
    assert A.nonneg(A.sub(A.scale(count,104),C(382)))
   p=A.apply_periods(field,data,p,0,count,'period'+str(i));elapsed=A.add(elapsed,A.scale(count,104))
  h=data[3];records.append(dict(segment=i,time=elapsed,pose=[p,h]));print(json.dumps(records[-1]),flush=True)
 tw=T['infinite_tail_word'];assert tw in standard;data=A.word_data(tw,h);assert data[3]==h and data[2]==(2,-2)
 tail=infinite_tail(field,data,p)
 assert elapsed==linear(312,208,111801) and p==(linear(-2,0,45),linear(-2,0,-26)) and h==3 and tw==W[99:]+W[:99]
 # Exact old black-lifetime provenance: the first ordinary recovery visits
 # the return point (15,23) in its own canonical source coordinates.
 source=json.loads((ROOT/'scattering/ordinary_reverse_interface/template_r28.json').read_text());word=source['segments'][0]['word'];assert len(word)==6336
 reads,_,_,_=plan(word,(0,0),2);visits=[(t,word[t]) for t,q in enumerate(reads) if q==(15,23)];assert visits and visits[-1][1]=='R'
 # Its next read is the checked late cap-return collision. All intervening
 # segment incidences will be separately certified in the provenance check.
 out=dict(status='exact complete two-cell capture for all independent m,k>=100',initial=[first,second],capture_time=elapsed,capture_pose=[p,h],tail=tail,tail_phase=next(j for j in range(104) if tw==W[j:]+W[:j]),first_cap_tail_failure_time=failure,first_cap_tail_failure_point=[linear(-2,0,8),linear(-2,0,-5)],ordinary_local_prior_visits=visits,records=records,statistics=A.STATS.copy(),template_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),packet_certificate_sha256=hashlib.sha256((ROOT/'scattering/ordinary_reverse_interface/certificate_r28.json').read_bytes()).hexdigest())
 (HERE/'r28_complete_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
