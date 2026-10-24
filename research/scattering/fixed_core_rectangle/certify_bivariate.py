"""All m>=100,n>=m+100; complete exceptional rectangle plus fixed-phase core.

Use independent variables u=m-100 and v=n-m-100. This extends the fixed-m
witness algebraically, with every input field and every read checked afresh.
"""
import json,hashlib,time
from pathlib import Path
from bivariate import A,infinite_tail
HERE=Path(__file__).resolve().parent
M=(1,0,100);N=(1,1,200)

def interface_bounds(field, omitted=()):
 """Conservative complete-support bounds; u lower may depend on fixed m."""
 pts=[p for p in field.points if p not in omitted]
 for b,d,count,_ in field.rays:
  pts.extend((b,A.padd(b,(A.scale(A.sub(count,A.ONE),d[0]),A.scale(A.sub(count,A.ONE),d[1])))))
 us=[A.sub(p[0],p[1]) for p in pts];zs=[A.add(p[0],p[1]) for p in pts]
 shifted=[A.add(x,A.scale(M,4)) for x in us]
 assert all(x[0]>=0 and x[1]>=0 for x in shifted)
 lower=min(x[2] for x in shifted)
 assert all(x[0]<=0 and x[1]<=0 for x in zs)
 zupper=max(x[2] for x in zs)
 uupper=max(x[2] for x in us) if all(x[0]<=0 and x[1]<=0 for x in us) else None
 return dict(u_lower_m_coefficient=-4,u_lower_constant=lower,u_upper=uupper,z_upper=zupper)

def reads_proxy():
 f=A.Field(set(A.READ_POINTS));f.rays=[(b,d,N,'read') for b,d,N in A.READ_RAYS];return f

def main():
 T=json.loads((HERE/'template.json').read_text())
 for key in A.STATS:A.STATS[key]=0
 A.READ_POINTS.clear();A.READ_RAYS.clear()
 def lin(a,b):return A.add(A.scale(N,a),(0,0,b))
 def lm(a,b):return A.add(A.scale(M,a),(0,0,b))
 inputs={'s':(lm(-2,-23),lm(2,31)),'q':(lin(-2,-33),lin(-2,-14)),'a':(lin(-2,-33),lin(2,41)),'c':(lin(2,8),lin(-2,-14)),'d':(lin(2,8),lin(2,41))}
 for i,p in enumerate(inputs.values()):
  for q in list(inputs.values())[i+1:]:assert A.no_point_collision(p,q)
 periods={1:A.add(N,(0,0,8)),3:A.add(N,(0,0,7)),5:M,7:A.add(M,(0,0,2)),9:A.add(N,(0,0,-20)),11:A.add(A.add(N,M),(0,0,10))}
 field=A.Field(set(inputs.values()));base=A.point(0,0);h=0;elapsed=A.ZERO;contacts={};records=[];interfaces={}
 standard={A.W[i:]+A.W[:i] for i in range(104)}
 for i,s in enumerate(T['segments']):
  word=s['word'];assert word and set(word)<={'R','L'}
  data=A.word_data(word,h);reads=A.plan(word,(0,0),h)[0];hits={}
  # Exhaustively locate first contacts, with all possible isolated incidences
  # either established identically or rejected by exact Diophantine tests.
  for j,local in enumerate(reads):
   p=A.translate_local(local,base,0)
   for label,q in inputs.items():
    if s['type']=='finite':
     if p==q:
      if label not in contacts and label not in hits:hits[label]=A.add(elapsed,(0,0,j))
     else:assert A.no_point_collision(p,q)
    else:
     k=A.line_coordinate(A.psub(q,p),data[2])
     if k is not None and A.in_range(k,periods[i]) and label not in contacts:
      t=A.add(A.add(elapsed,A.scale(k,104)),(0,0,j));hits[label]=A.minimum(hits[label],t) if label in hits else t
  contacts.update(hits)
  if s['type']=='finite':
   base=A.apply_finite(field,data,base,0,'finite'+str(i));elapsed=A.add(elapsed,(0,0,len(word)))
  else:
   assert word in standard and len(word)==104 and data[3]==h and A.nonneg(A.sub(periods[i],A.ONE))
   base=A.apply_periods(field,data,base,0,periods[i],'periods'+str(i));elapsed=A.add(elapsed,A.scale(periods[i],104))
  h=data[3]
  if i==8:
   assert set(contacts)=={'q','s'}
   parent=A.Field(field.points^{inputs['a'],inputs['c'],inputs['d']});parent.rays=list(field.rays)
   pw=T['segments'][9]['word'];assert pw in standard
   parent_tail=A.word_data(pw,h);assert parent_tail[2]==(2,-2) and parent_tail[3]==h
   interfaces['two_bit']={'time':elapsed,'pose':[base,h],'tail':infinite_tail(parent,parent_tail,base),'archive':interface_bounds(parent),'finite_reads':interface_bounds(reads_proxy())}
  records.append(dict(segment=i,time=elapsed,pose=[base,h],contacts=hits));print(json.dumps(records[-1]),flush=True)
 expected_time=A.add(A.add(A.scale(N,416),A.scale(M,312)),(0,0,197704))
 assert elapsed==expected_time and base==(lm(-2,-28),lm(2,68)) and h==0
 assert contacts=={'q':A.add(A.scale(N,104),(0,0,10881)),'s':A.add(A.add(A.scale(N,208),A.scale(M,104)),(0,0,70810)),'c':A.add(A.add(A.scale(N,312),A.scale(M,208)),(0,0,142996))}
 tw=T['infinite_tail_word'];assert tw in standard
 tail=A.word_data(tw,h);assert tail[2]==(-2,2) and tail[3]==h
 proof=infinite_tail(field,tail,base)
 interfaces['three_bit']={'archive':interface_bounds(field,{inputs['a'],inputs['d']}),'finite_reads':interface_bounds(reads_proxy())}
 for label in ('a','d'):
  target=inputs[label]
  for p in A.READ_POINTS:assert A.no_point_collision(p,target)
  for b,d,count in A.READ_RAYS:assert not A.ray_membership(target,b,d,count)
  for p in tail[0]:
   k=A.line_coordinate(A.psub(target,A.translate_local(p,base,0)),tail[2]);assert k is None or A.negative(k)
 out=dict(status='exact bivariate complete-field certificate passed',domain='integers m>=100,n>=m+100',variables='u=m-100>=0,v=n-m-100>=0',capture_time_in_u_v=elapsed,capture_time_in_n_m=[416,312,197704],capture_pose=[base,h],tail=proof,contacts=contacts,never_read=['a','d'],statistics=A.STATS,interfaces=interfaces,records=records,template_sha256=hashlib.sha256((HERE/'template.json').read_bytes()).hexdigest())
 (HERE/'bivariate_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
