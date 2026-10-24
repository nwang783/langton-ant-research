"""Exact all-parameter finite-history / three parallel-rail strip interface.
Color validity of the old prefix is inherited from the audited rectangle proof.
All subsequent equality is complete-field XOR algebra, not sampled matching.
"""
import sys,json,hashlib,math
from collections import defaultdict
from pathlib import Path
R=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(R/'scattering/fixed_core_rectangle'))
from bivariate import A
sys.path.insert(0,str(R/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,P,D,plan,multiple
TFILE=R/'continuation_2026-10-22/ant_continuation2/planar_structure/exceptional_rectangle_template.json'
M=(1,0,100);K=(0,1,100);N=A.add(M,K);SE=(2,-2);NW=(-2,2);WIDTH=200

def c(v):return (0,0,v)
def pt(x,y):return c(x),c(y)
def lin(a,b):return A.add(A.scale(N,a),c(b))
def u(p):return A.sub(p[0],p[1])
def z(p):return A.add(p[0],p[1])
def far_outside(p,d=(0,0),count=None):
 lo=hi=u(p)
 if count is not None:
  e=A.add(lo,A.scale(A.sub(count,A.ONE),d[0]-d[1]))
  if d[0]-d[1]>0:hi=e
  else:lo=e
 return A.negative(A.sub(hi,c(-WIDTH))) or A.negative(A.sub(c(WIDTH),lo))

def main():
 T=json.loads(TFILE.read_text());field=A.Field([(lin(-2,-33),lin(-2,-14)),(lin(-2,-33),lin(2,41)),(lin(2,8),lin(-2,-14))])
 O=(A.add(A.scale(M,-2),c(37)),A.add(A.scale(M,2),c(25)))
 rows=json.loads((R/'scattering/retained_frontier/ordinary_interfaces.json').read_text())['rows']
 phases=sorted([r['phase'] for r in rows]+[72]);assert len(phases)==len(set(phases))==22
 qs,_,_,_=plan(W,(0,0),0)
 cores={r:A.translate_local(qs[r],O,0) for r in phases}
 omitted={'d':(lin(2,8),lin(2,41))}
 # All cores are genuinely fresh for an incoming NW period, including every
 # strictly earlier whole period, not only a chosen finite source age.
 for r in phases:
  assert qs[r] not in qs[:r]
  for q in qs:
   ell=multiple((qs[r][0]-q[0],qs[r][1]-q[1]),NW)
   assert ell is None or ell>=0
 p=pt(0,0);h=0;elapsed=c(0);avoidance=0;read_upper={'u':-10**9,'z':-10**9}
 def record_bounds(q,drift=(0,0),count=None):
  for name,normal in [('u',u),('z',z)]:
   bound=normal(q);speed=drift[0]-drift[1] if name=='u' else sum(drift)
   if count is not None and speed>0:bound=A.add(bound,A.scale(A.sub(count,A.ONE),speed))
   if name=='u':bound=A.sub(bound,A.scale(N,4))
   assert bound[0]<=0 and bound[1]<=0
   read_upper[name]=max(read_upper[name],bound[2])
 for i,s in enumerate(T['segments'][:11]):
  word=s['word'];assert word and set(word)<={'R','L'}
  reads,_,end,eh=plan(word,(0,0),h);_,odd,_,_=A.word_data(word,h)
  count=A.add(A.scale(N,s['count'][0]),c(s['count'][1])) if s['type']=='periods' else None
  if count is not None:assert len(word)==104 and eh==h and A.nonneg(A.sub(count,A.ONE))
  for q in set(reads):
   q=A.translate_local(q,p,0)
   record_bounds(q,end,count)
   for target in list(cores.values())+list(omitted.values()):
    if count is None:assert A.no_point_collision(q,target)
    else:assert not A.ray_membership(target,q,end,count)
    avoidance+=1
  if count is None:
   field.add_points(A.translate_local(q,p,0) for q in odd);p=A.translate_local(end,p,0);elapsed=A.add(elapsed,c(len(word)))
  else:
   field.add_rays([A.translate_local(q,p,0) for q in odd],end,count,f'old{i}')
   p=A.padd(p,(A.scale(count,end[0]),A.scale(count,end[1])));elapsed=A.add(elapsed,A.scale(count,len(word)))
  h=eh
 assert p==(lin(2,37),lin(-2,25)) and h==0
 assert elapsed==A.add(A.scale(N,520),c(195082))
 # n+m entire incoming NW periods end at the fixed retained-core epoch.
 assert T['segments'][11]['word']==W and T['segments'][11]['count']==[2,15]
 L=A.add(N,M);assert A.nonneg(A.sub(A.add(A.scale(N,2),c(15)),L))
 _,odd,end,eh=A.word_data(W,h);assert end==NW and eh==h
 for q in qs:
  record_bounds(A.translate_local(q,p,0),NW,L)
  for target in omitted.values():assert not A.ray_membership(target,A.translate_local(q,p,0),NW,L)
 field.add_rays([A.translate_local(q,p,0) for q in odd],NW,L,'incoming_return')
 p=A.padd(p,(A.scale(L,-2),A.scale(L,2)));assert p==O
 elapsed=A.add(elapsed,A.scale(L,104))
 assert elapsed==A.add(A.add(A.scale(N,624),A.scale(M,104)),c(195082))
 # Translate the COMPLETE finite field to the core-epoch source frame.
 points=[A.psub(q,O) for q in field.points]
 rays=[(A.psub(b,O),d,count,label) for b,d,count,label in field.rays]
 # XOR the complete proposed infinite model: new NW core, settled old
 # NW rail at(-52,4), and settled old SE return rail at(-99,-23).
 points += [pt(-q[0],-q[1]) for q in P]
 rays += [(pt(-d[0]+2,-d[1]-2),SE,None,'model_incoming') for d in D]
 rays += [(pt(-52-d[0],4-d[1]),NW,'bilateral','model_old_NW') for d in D]
 rays += [(pt(-99+d[0],-23+d[1]),NW,'bilateral','model_old_SE') for d in D]
 groups=defaultdict(set);discarded=defaultdict(int);included=0
 def toggle_interval(base,drift,count,label):
  nonlocal included
  if count not in (None,'bilateral',1) and far_outside(base,drift,count):discarded[label]+=1;return
  if count==1 and far_outside(base):discarded[label]+=1;return
  zz=z(base);assert zz[:2]==(0,0),(label,'variable transverse class',base,drift,count)
  assert base[0][0]%2==base[0][1]%2==0
  parity=base[0][2]%2;key=(zz[2],parity)
  t=tuple(v//2 for v in A.sub(base[0],c(parity)))
  key_u=2*parity-zz[2]
  L=-((WIDTH+key_u)//4)
  U=(WIDTH-key_u)//4
  assert isinstance(L,int)
  if count=='bilateral':lo=hi=None
  elif count is None:
   assert drift in (NW,SE)
   lo,hi=(None,t) if drift==NW else (t,None)
  elif count==1:lo=hi=t
  elif drift==SE:lo=t;hi=A.add(t,A.sub(count,A.ONE))
  elif drift==NW:lo=A.sub(t,A.sub(count,A.ONE));hi=t
  else:raise AssertionError(('nonparallel ray reaches strip',label,base,drift,count))
  if lo is not None and A.nonneg(A.sub(lo,c(U+1))):return
  if hi is not None and A.nonneg(A.sub(c(L-1),hi)):return
  if lo is None or A.nonneg(A.sub(c(L),lo)):lo=c(L)
  else:assert A.nonneg(A.sub(lo,c(L))),(label,'lower bound crosses strip',lo,L)
  if hi is None or A.nonneg(A.sub(hi,c(U))):hi=c(U)
  else:assert A.nonneg(A.sub(c(U),hi)),(label,'upper bound crosses strip',hi,U)
  assert A.nonneg(A.sub(hi,lo)),(label,'interval order',lo,hi)
  groups[key].symmetric_difference_update({lo,A.add(hi,A.ONE)});included+=1
 for q in points:
  if far_outside(q):discarded['point']+=1
  else:toggle_interval(q,SE,1,'point')
 for b,d,count,label in rays:toggle_interval(b,d,count,label)
 assert all(not edges for edges in groups.values()),{str(k):list(v) for k,v in groups.items() if v}
 # A discrepancy one astronomically distant NE period ahead still lies in
 # this unbounded strip and must be detected; finite z truncation is invalid.
 assert read_upper=={'u':98,'z':71}
 saved={key:set(edges) for key,edges in groups.items()};saved_included=included
 toggle_interval(pt(2*10**60,2*10**60),SE,1,'negative_control')
 assert any(groups.values())
 groups.clear();groups.update(saved);included=saved_included
 result=dict(pre_core_read_upper={'u_minus_4n':read_upper['u'],'z':read_upper['z']},negative_control='future marker at NE depth10^60 rejected',status='complete finite q+a+c history equals NW core plus two old parallel rails throughout closed source strip',domain='m>=100,k=n-m>=100',strip_u=[-WIDTH,WIDTH],source_origin=O,source_time=elapsed,old_NW_rail_offset=[-52,4],old_SE_rail_offset=[-99,-23],fresh_phases=phases,pre_core_nonincidences=avoidance,strip_translation_classes=len(groups),included_terms=included,discarded_terms=dict(discarded),source_template_sha256=hashlib.sha256(TFILE.read_bytes()).hexdigest(),scope='This proves exact initial-field equality only inside the strip. A future trajectory transfers only if every one of its reads remains inside, or until its first exit.')
 (HERE/'strip_interface.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
