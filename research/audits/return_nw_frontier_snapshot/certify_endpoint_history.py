"""A precise arbitrarily delayed failure of the pristine infinite-tail model."""
import json,gzip,hashlib
from full_field import A,source_field,C,W,plan,HERE,R
M=(1,0,100);N=(1,1,200)
def main():
 field,O,T,I=source_field(M,N);path=HERE/'full_return_template_r28.json';template=json.loads(path.read_text());body,period,last=template['segments'];assert body['type']=='finite' and len(body['word'])==6336 and period['count_nm']==[1,-1,12]
 full=json.loads((HERE/'full_return_certificate_r28.json').read_text());assert full['template_sha256']==hashlib.sha256(path.read_bytes()).hexdigest()
 model=next(r for r in json.loads((HERE/'parallel_model_certificate.json').read_text())['records'] if r['phase']==28)
 discovery=next(r for r in json.loads((HERE/'parallel_model_discovery.json').read_text()) if r['r']==28 and r['mature'])
 modelword=gzip.open(HERE/discovery['word_file'],'rt').read();assert hashlib.sha256(modelword.encode()).hexdigest()==model['word_sha256']
 assert modelword[:6336]==body['word']
 P=period['word'];assert all(ch==P[i%104] for i,ch in enumerate(modelword[6336:]))
 shift=(len(modelword)-6336)%104;assert discovery['tail_word']==P[shift:]+P[:shift]
 j=next(i for i,ch in enumerate(last['word']) if ch!=P[i%104]);assert j==63 and last['word'][j]=='L' and P[j]=='R'
 _,_,end,h=plan(body['word'],(0,0),0);base=A.translate_local(end,O,0)
 _,_,drift,eh=plan(P,(0,0),h);assert drift==(-2,2) and eh==h
 count=A.add(A.sub(N,M),C(12));base=A.padd(base,(A.scale(count,-2),A.scale(count,2)))
 reads,_,_,_=plan(last['word'],(0,0),h);target=A.translate_local(reads[j],base,0)
 impact=A.add(T,A.add(C(6336+63),A.scale(count,104)));assert impact==A.add(A.scale(N,728),C(202729))
 assert field.point_color(A.psub(target,O))
 nn=lambda a,b:A.add(A.scale(N,a),C(b))
 initial=[(nn(-2,-33),nn(-2,-14)),(nn(-2,-33),nn(2,41)),(nn(2,8),nn(-2,-14)),(nn(2,8),nn(2,41)),A.translate_local(plan(W,(0,0),0)[0][28],O,0)]
 assert all(A.no_point_collision(target,q) for q in initial)
 # Read ALL old history, including the moving q/a/c packets and the incoming
 # part of the final NW rail. No old visit is chosen from a finite sample.
 old=json.loads((R/'continuation_2026-10-22/ant_continuation2/planar_structure/exceptional_rectangle_template.json').read_text())
 p=A.point(0,0);h=0;elapsed=C(0);visits=[]
 for index,s in enumerate(old['segments'][:12]):
  qs,_,end,eh=plan(s['word'],(0,0),h)
  count=None if s['type']=='finite' else A.add(A.scale(N,s['count'][0]),C(s['count'][1]))
  if index==11:count=A.add(N,M)
  for i,q in enumerate(qs):
   bp=A.translate_local(q,p,0)
   if count is None:
    if bp==target:visits.append(dict(segment=index,phase=i,time=A.add(elapsed,C(i)),read=s['word'][i]))
    else:assert A.no_point_collision(bp,target)
   elif A.ray_membership(target,bp,end,count):
    k=A.line_coordinate(A.psub(target,bp),end);assert k is not None and A.nonneg(k) and A.nonneg(A.sub(A.sub(count,A.ONE),k))
    visits.append(dict(segment=index,phase=i,time=A.add(elapsed,A.add(A.scale(k,104),C(i))),read=s['word'][i]))
  if count is None:p=A.translate_local(end,p,0);elapsed=A.add(elapsed,C(len(s['word'])))
  else:p=A.padd(p,(A.scale(count,end[0]),A.scale(count,end[1])));elapsed=A.add(elapsed,A.scale(count,104))
  h=eh
 assert p==O and h==0 and elapsed==T and visits
 prior=max(visits,key=lambda q:q['time'][2]);assert all(A.nonneg(A.sub(prior['time'],q['time'])) for q in visits)
 assert prior['read']=='R' and len(visits)==1
 # The modified local prefix has not touched this old bit before the mismatch.
 p=O;h=0
 for s in template['segments']:
  qs,_,end,eh=plan(s['word'],(0,0),h)
  if s is last:qs=qs[:j]
  count=None if s['type']=='finite' else A.add(A.sub(N,M),C(12))
  for q in qs:
   bp=A.translate_local(q,p,0)
   if count is None:assert A.no_point_collision(bp,target)
   else:assert not A.ray_membership(target,bp,end,count)
  if count is None:p=A.translate_local(end,p,0)
  else:p=A.padd(p,(A.scale(count,end[0]),A.scale(count,end[1])))
  h=eh
 new_visits=[i for i,q in enumerate(reads) if q==reads[j]]
 assert new_visits==[63,115,119,127,139,151]
 assert [last['word'][i] for i in new_visits]==list('LRLRLR')
 tailreads,_,drift,eh=plan(template['infinite_tail_word'],(0,0),h);assert drift==(-2,2) and eh==h
 zvals=[A.add(A.translate_local(q,p,0)[0],A.translate_local(q,p,0)[1]) for q in tailreads]
 assert all(v[:2]==(0,0) for v in zvals) and (min(v[2] for v in zvals),max(v[2] for v in zvals))==(35,45)
 assert A.add(target[0],target[1])==C(59)
 out=dict(new_visit_phases=new_visits,final_trigger_bit='black forever after the last recovery read',final_tail_z=[35,45],status='exact first infinite-model mismatch at a retained self-written endpoint bit',domain='m>=100,n-m>=100',target=target,impact_time=impact,impact_source_time=A.sub(impact,T),actual_read='L',infinite_model_read='R',last_old_visit=prior,all_old_visits=visits,bit_age=A.sub(impact,prior['time']),template_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),scope='Obstructs infinite-tail transfer from the pristine strip model; does not obstruct a guarded graph that retains endpoint position and history.')
 (HERE/'endpoint_history_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
