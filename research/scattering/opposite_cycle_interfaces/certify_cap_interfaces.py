"""Complete archive, sector and parity guards for three permanent cap returns."""
import json,sys,hashlib
from pathlib import Path
from certify_caps import HERE,ROOT,blank
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'));from ant_exact import W,P,D,plan,multiple
SRC=HERE.parent/'ordinary_reverse_interface';add=lambda a,b:tuple(x+y for x,y in zip(a,b));scale=lambda a,k:tuple(x*k for x in a)
def main():
 O,E=blank();assert max(x-y+25 for x,y in E)==73 and max(map(sum,E))==35
 assert max(x+y for x,y in P)<=73 and max(x+y for x,y in D)<=73
 bridge=json.loads((HERE/'cap_bridge.json').read_text());caps=json.loads((HERE/'caps.json').read_text());assert bridge['caps_sha256']==hashlib.sha256((HERE/'caps.json').read_bytes()).hexdigest();rows=[]
 for r in [29,32,71]:
  cap=next(x for x in caps['rows'] if x['phase']==r);B=next(x for x in bridge['rows'] if x['phase']==r);path=HERE/f'backward_certificate_r{r}.json';C=json.loads(path.read_text());assert B['packet_certificate_sha256']==hashlib.sha256(path.read_bytes()).hexdigest();assert B['permanent_transfer'] and B['pose']==cap['pose'] and B['final_phase']==cap['tail_phase']
  oldpath=SRC/f'certificate_r{r}.json';old=json.loads(oldpath.read_text());assert C['source_certificate_sha256']==hashlib.sha256(oldpath.read_bytes()).hexdigest();Tpath=SRC/f'template_r{r}.json';T=json.loads(Tpath.read_text());assert old['template_sha256']==hashlib.sha256(Tpath.read_bytes()).hexdigest()
  p=((0,0),(0,0));h=2;us=[];zs=[]
  for seg in T['segments']:
   assert seg['type'] in ['finite','periods'];w=seg['word'];assert w and set(w)<={'R','L'};qs,_,end,eh=plan(w,(0,0),h);count=None if seg['type']=='finite' else tuple(seg['count'])
   if count:assert len(w)==104 and eh==h and count[0]>=0 and 100*count[0]+count[1]>=1
   for q in qs:
    x=add(p[0],(0,q[0]));y=add(p[1],(0,q[1]));corners=[(x,y)]
    if count:corners.append((add(x,scale(add(count,(0,-1)),end[0])),add(y,scale(add(count,(0,-1)),end[1]))))
    for x,y in corners:
     u=add(x,scale(y,-1));z=add(x,y);assert u[0]==0 and z[0]<=0;us.append(u[1]);zs.append(100*z[0]+z[1])
   if count:p=(add(p[0],scale(count,end[0])),add(p[1],scale(count,end[1])))
   else:p=(add(p[0],(0,end[0])),add(p[1],(0,end[1])))
   h=eh
  assert [list(p[0]),list(p[1])]==old['capture_pose'][0] and h==1 and old['tail_phase']==0
  p0=tuple(v[1] for v in p);qs,_,end,eh=plan(W,p0,h);assert tuple(end[i]-p0[i] for i in range(2))==(2,2) and eh==h;us.extend(x-y for x,y in qs)
  assert max(sum(v[2] for v in q) for q in C['initial'][:2])<=73
  q2,q3=C['initial'][1:];assert [v[2]%2 for v in q3]==[1-v[2]%2 for v in q2]
  fresh=[]
  for i,q in enumerate(qs):
   if not any((k:=multiple((v[0]-q[0],v[1]-q[1]),(2,2))) is not None and (k>0 or k==0 and j<i) for j,v in enumerate(qs)):fresh.append(i)
  allowed=[i for i in fresh if sum(qs[i])%2==1];assert allowed==[14,28,32,38,46,56,60,62,70,72]
  corez=max(-y+x for x,y in P)+sum(p0)-400;archive=max(73,max(zs),corez);assert archive==73
  finalpose,finalh=cap['pose'];phase=cap['tail_phase'];tw=W[phase:]+W[:phase];finalqs,_,end,eh=plan(tw,tuple(finalpose),finalh);drift=tuple(end[i]-finalpose[i] for i in range(2));assert list(drift)==cap['drift']
  final_archive=max(35,cap['prefix_z_bounds'][1],B['local_packet_z_upper_at_m100']);parity_guard=None
  if r in [29,32]:
   assert phase==0 and finalh==1 and drift==(2,2)
   # Source NW corner becomes actual NE under O_m+(y,-x), m arbitrary.
   corner_parity=[(1+q3[1][2])%2,q2[0][2]%2];exceptional_parity=[v%2 for v in finalqs[72]];assert corner_parity!=exceptional_parity
   final_allowed=[i for i in fresh if sum(finalqs[i])%2==sum(corner_parity)%2];assert final_allowed==allowed
   final_archive=max(final_archive,max(finalpose[0]-y+finalpose[1]+x for x,y in P));assert final_archive==35
   parity_guard=dict(actual_NE_corner=corner_parity,actual_NE_phase72=exceptional_parity,fresh_allowed=final_allowed)
  else:assert r==71 and drift==(-2,2) and final_archive==37
  rows.append(dict(phase=r,two_bit_future_u_bounds=[min(us),max(us)],complete_two_bit_archive_z_upper=archive,third_favorable_phases=allowed,complete_pre_final_archive_z_upper=final_archive,last_parity_guard=parity_guard,capture_time_m_n_p_constant=B['capture_time_m_n_p_constant'],pose=cap['pose'],tail_phase=phase,drift=drift))
 out=dict(status='three additional fixed-m>=100 retained-core recurrence exclusions',rows=rows,bridge_sha256=hashlib.sha256((HERE/'cap_bridge.json').read_bytes()).hexdigest(),scope='Remote distances tend to infinity with m fixed. Phase56 is not included.')
 (HERE/'cap_interfaces.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
