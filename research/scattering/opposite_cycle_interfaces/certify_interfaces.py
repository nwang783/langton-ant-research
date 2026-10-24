"""Bindings and complete archive bounds for the three protected cycle proofs."""
import json,hashlib,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];SRC=HERE.parent/'ordinary_reverse_interface'
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'));from ant_exact import W,P,D,plan,step,multiple
add=lambda a,b:tuple(x+y for x,y in zip(a,b));scale=lambda a,k:tuple(x*k for x in a)
def main():
 blank=set();bp=(0,0);bh=0
 for _ in range(9977):bp,bh,_=step(blank,bp,bh)
 assert bp==(-15,10) and bh==3
 E=blank^{(bp[0]+y,bp[1]-x) for x,y in P};assert max(x-y+25 for x,y in E)==73
 assert max(x+y for x,y in P)<=73 and max(x+y for x,y in D)<=73
 rows=[]
 for r in [38,55,62]:
  cp=HERE/f'certificate_r{r}.json';cert=json.loads(cp.read_text());oldp=SRC/f'certificate_r{r}.json';old=json.loads(oldp.read_text());assert cert['source_certificate_sha256']==hashlib.sha256(oldp.read_bytes()).hexdigest() and cert['template_sha256']==hashlib.sha256((HERE/f'template_r{r}.json').read_bytes()).hexdigest()
  expected={38:([312,208,205541],[[[-2,0,-249],[-2,0,-208]],3],100,[-94,116]),55:([312,208,165430],[[[-2,0,-193],[-2,0,-233]],2],0,[-92,96]),62:([312,208,197815],[[[-2,0,-248],[-2,0,-215]],3],100,[-64,124])}[r]
  assert (cert['capture_time'],cert['capture_pose'],cert['tail_phase'],cert['prefix_u_bounds'])==expected
  q1,q2full,q3full=cert['initial'];assert all(sum(q[j][i] for j in range(2))<=0 for q in [q2full] for i in range(2)) and sum(q[2] for q in q2full)<-9
  assert all(sum(q3full[j][i] for j in range(2))>=0 for i in range(2)) and sum(q[2] for q in q3full)>73
  assert all(v[:2]==[0,0] for v in q1) and sum(v[2] for v in q1)<=73
  assert cert['unused_corners_never_read'] and cert['whole_future_u_lower']>=-160
  T=json.loads((SRC/f'template_r{r}.json').read_text());assert old['template_sha256']==hashlib.sha256((SRC/f'template_r{r}.json').read_bytes()).hexdigest()
  p=((0,0),(0,0));h=2;us=[];zs=[]
  for seg in T['segments']:
   assert seg['type'] in ['finite','periods'];w=seg['word'];assert set(w)<={'R','L'};qs,_,end,eh=plan(w,(0,0),h);count=None if seg['type']=='finite' else tuple(seg['count'])
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
  p0=tuple(v[1] for v in p);qs,_,end,eh=plan(W,p0,h);assert tuple(end[i]-p0[i] for i in range(2))==(2,2) and eh==h
  us.extend(x-y for x,y in qs);q2=old['second_marker_affine'];par=[v[1]%2 for v in q2];q3=plan(W[:72],p0,h)[2];assert [v%2 for v in q3]==[1-v for v in par]
  fresh=[]
  for i,q in enumerate(qs):
   if not any((k:=multiple((v[0]-q[0],v[1]-q[1]),(2,2))) is not None and (k>0 or k==0 and j<i) for j,v in enumerate(qs)):fresh.append(i)
  assert fresh==[13,14,15,27,28,29,32,38,45,46,47,55,56,57,60,61,62,70,71,72,75,89]
  allowed=[i for i in fresh if sum(qs[i])%2==1];assert allowed==[14,28,32,38,46,56,60,62,70,72]
  corez=max(-y+x for x,y in P)+sum(p0)-400 # rotate SE core counterclockwise to NE; n>=100.
  archive=max(73,max(zs),corez);assert archive==73
  rows.append(dict(phase=r,two_bit_future_u_bounds=[min(us),max(us)],complete_two_bit_archive_z_upper=archive,third_fresh_favorable_phases=allowed,third_exceptional_parity=[v%2 for v in q3],capture_time=cert['capture_time'],capture_pose=cert['capture_pose'],tail_phase=cert['tail_phase'],tail_drift=cert['tail']['drift'],whole_future_u_lower=cert['whole_future_u_lower'],certificate_sha256=hashlib.sha256(cp.read_bytes()).hexdigest()))
 out=dict(status='complete archive and sector interfaces for three protected cycles',rows=rows,scope='Fixed m>=100 recurrence consequence; not an arbitrary independent-m five-cell seed theorem.')
 (HERE/'interfaces.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
