"""Exact one-depth source certificates plus algebraic all-source-age transport."""
import sys,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/scattering/fixed_core_rectangle')
from bivariate import A,infinite_tail
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation')
from ant_exact import canonical_source,W,D,P,DRIFT,plan,multiple,step,certify_period
K=(0,1,200);AGE=100;BASE=(-15,29)
EX={29:(2,57),56:(4,59),62:(2,45)}
CFG={29:(64254,-49,0,103,(-68,86)),56:(59158,-47,0,59,(-52,86)),62:(58950,-33,2,91,(-64,74))}
def c(x):return (0,0,x)
def lk(a,b):return A.add(A.scale(K,a),c(b))

def main(r):
 assert r in EX;T=json.loads((HERE/f'source_template_r{r}.json').read_text());assert T['phase']==r and T['source_age']==AGE
 ordinary=next(q for q in json.loads((HERE.parent/'ordinary_interfaces.json').read_text())['rows'] if q['phase']==r)
 assert tuple(ordinary['exceptional_ray_base_constant'])==EX[r]
 assert ordinary['outgoing_drift']==[2,2]
 assert W==A.W and DRIFT==(2,-2) and len(P)==13 and len(D)==12
 assert certify_period(set(P),(0,0),2,W)
 period=set(P);pp=(0,0);hh=2
 for letter in W:
  pp,hh,got=step(period,pp,hh);assert got==letter
 assert pp==DRIFT and hh==2 and period=={(x+2,y-2) for x,y in P}|set(D)
 for p in D:
  for q in D:
   v=multiple((p[0]-q[0],p[1]-q[1]),DRIFT);assert v is None or v==0
 for p in P:
  for q in D:
   v=multiple((q[0]-p[0],q[1]-p[1]),DRIFT);assert v is None or v<=0
 for key in A.STATS:A.STATS[key]=0
 A.READ_POINTS.clear();A.READ_RAYS.clear()
 B,p,h=canonical_source(AGE,0);assert p==(0,0) and h==2
 assert B==set(P)|{(x-2*j,y+2*j) for x,y in D for j in range(1,AGE+1)}
 reads=plan(W,(0,0),2)[0];core=reads[r];assert core not in B
 assert [BASE[0]-core[0],BASE[1]-core[1]]==ordinary['core_ray_base']
 ex,ey=EX[r];corner=(lk(-2,BASE[0]-ex),lk(-2,BASE[1]-ey));core_aff=A.point(*core)
 assert A.negative(A.sub(corner[1],c(min(y for x,y in B|{core}))))
 field=A.Field({A.point(*q) for q in B|{core}}|{corner});base=A.point(0,0);elapsed=A.ZERO;records=[];contacts={}
 standard={W[i:]+W[:i] for i in range(104)}
 for i,s in enumerate(T['segments']):
  word=s['word'];assert word and set(word)<={'R','L'};data=A.word_data(word,h)
  count=lk(*s['count']) if s['type']=='periods' else None;hits={}
  for j,q in enumerate(A.plan(word,(0,0),h)[0]):
   bp=A.translate_local(q,base,0)
   for name,target in [('core',core_aff),('opposite',corner)]:
    if count is None:
     if bp==target:
      if name not in contacts and name not in hits:hits[name]=A.add(elapsed,c(j))
     else:assert A.no_point_collision(bp,target)
    else:
     k=A.line_coordinate(A.psub(target,bp),data[2])
     if k is not None and A.in_range(k,count) and name not in contacts:
      t=A.add(A.add(elapsed,A.scale(k,104)),c(j));hits[name]=A.minimum(hits[name],t) if name in hits else t
  contacts.update(hits)
  if count is None:base=A.apply_finite(field,data,base,0,'finite'+str(i));elapsed=A.add(elapsed,c(len(word)))
  else:
   assert word in standard and len(word)==104 and data[3]==h and A.nonneg(A.sub(count,A.ONE))
   base=A.apply_periods(field,data,base,0,count,'periods'+str(i));elapsed=A.add(elapsed,A.scale(count,104))
  h=data[3];records.append(dict(segment=i,time=elapsed,pose=[base,h],contacts=hits));print(json.dumps(records[-1]),flush=True)
 tw=T['infinite_tail_word'];assert tw in standard;tail=A.word_data(tw,h);assert tail[2]==(2,2) and tail[3]==h
 proof=infinite_tail(field,tail,base)
 expected_time,y_constant,expected_heading,expected_phase,expected_bounds=CFG[r]
 assert elapsed==lk(104,expected_time)
 assert base==(lk(-2,29),lk(-2,y_constant)) and h==expected_heading
 assert tw==W[expected_phase:]+W[:expected_phase]
 pts=list(A.READ_POINTS)
 for b,d,count in A.READ_RAYS:
  pts.extend((b,A.padd(b,(A.scale(A.sub(count,A.ONE),d[0]),A.scale(A.sub(count,A.ONE),d[1])))))
 pts.extend(A.translate_local(q,base,0) for q in tail[0])
 us=[A.sub(q[0],q[1]) for q in pts];assert all(q[:2]==(0,0) for q in us)
 lo,hi=min(q[2] for q in us),max(q[2] for q in us);assert (lo,hi)==expected_bounds
 # Every extra source age is contained below this u half-plane, for ALL m>=AGE.
 extra_u_max=max(x-y for x,y in D)-4*(AGE+1);assert extra_u_max<lo
 # Actual q-parent map is G_m(p)=BASE-p+m(-2,2). Its H1 has u>=-82.
 actual_upper_constant=BASE[0]-BASE[1]-lo
 assert actual_upper_constant-4*AGE < -82
 assert contacts['core']==c(r) and set(contacts)=={'core','opposite'}
 ordinary_elapsed=ordinary['capture_time_coefficients_n_m_constant'][2]-70738
 assert contacts['opposite']==lk(104,ordinary_elapsed+(72-ordinary['tail_phase'])%104)
 assert elapsed[0]==0 and elapsed[1]==104
 # Full-cycle a/c stay outside the COMPLETE actual u envelope on n>=m+100.
 # a_u= -2n-2m-2k-33-ey; c_u=2n-2m+2k+ex+14.
 actual_lower_constant=BASE[0]-BASE[1]-hi
 assert -2*100-2*200-33-ey < actual_lower_constant
 assert 2*100+2*200+ex+14 > 58
 # Incoming q-parent NW periods before the local source checkpoint are bounded
 # below by -4m+min u(BASE-p_i), and by -82 on the earlier finite prefix.
 incoming_u_min=min((BASE[0]-q[0])-(BASE[1]-q[1]) for q in reads)
 assert -2*100-2*200-33-ey < incoming_u_min
 assert -2*100-2*200-33-ey-4*AGE < -82
 # The far opposite cell is not read by q's finite prefix or the incoming NW leg.
 assert ex-ey-4*AGE < -82
 incoming_z_max=max(sum(BASE)-sum(q) for q in reads)
 assert ex+ey+4*200 > incoming_z_max
 out=dict(status='exact source-depth certificate and all-age half-plane transport passed',phase=r,source_age=AGE,depth_domain='k>=200',source_all_future_u_bounds=[lo,hi],extra_older_deposit_u_max=extra_u_max,source_capture_time=elapsed,source_capture_pose=[base,h],tail=proof,tail_phase=next(i for i in range(104) if tw==W[i:]+W[:i]),actual_postcore_u_bounds=[[-4,actual_lower_constant],[-4,actual_upper_constant]],actual_scope='n>=200,m>=100,k>=200 for three-bit q+s+d; n>=m+100 additionally for full rectangular a,c',contacts=contacts,statistics=A.STATS.copy(),records=records,template_sha256=hashlib.sha256((HERE/f'source_template_r{r}.json').read_bytes()).hexdigest())
 (HERE/f'source_certificate_r{r}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main(int(sys.argv[1]))
