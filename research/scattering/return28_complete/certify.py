"""Complete three-black-cell capture with every old-history write retained."""
import sys,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path.insert(0,str(HERE.parent/'fixed_core_rectangle'));from bivariate import A,infinite_tail
from ant_exact import W,plan
M=(1,0,100);K=(0,1,100);C=lambda v:(0,0,v)
def lin(a,b,c):return A.add(A.add(A.scale(M,a),A.scale(K,b)),C(c))
def main():
 s=(lin(-2,0,-19),lin(-2,0,8));Q=(lin(-2,-2,-26),lin(-2,-2,-5));qC=(lin(-2,2,27),lin(-2,-2,-5));inputs={'s':s,'Q':Q,'C':qC};assert all(A.no_point_collision(p,q) for i,p in enumerate(inputs.values()) for q in list(inputs.values())[i+1:]);field=A.Field(list(inputs.values()));assert len(field.points)==3
 for k in A.STATS:A.STATS[k]=0
 A.READ_POINTS.clear();A.READ_RAYS.clear();base=A.point(0,0);h=0;elapsed=C(0);records=[];contacts={};tp=HERE/'template.json';T=json.loads(tp.read_text());std={W[j:]+W[:j] for j in range(104)}
 for i,seg in enumerate(T['segments']):
  word=seg['word'];assert word and set(word)<={'R','L'} and seg['type'] in ['finite','periods'];data=A.word_data(word,h);reads=plan(word,(0,0),h)[0];count=None if seg['type']=='finite' else lin(*seg['count_mk']);hits={}
  for j,b in enumerate(reads):
   actual=A.translate_local(b,base,0)
   for label,q in inputs.items():
    if label in contacts:continue
    if count is None:
     if actual==q:
      if label not in hits:hits[label]=A.add(elapsed,C(j))
     else:assert A.no_point_collision(actual,q)
    else:
     k=A.line_coordinate(A.psub(q,actual),data[2])
     if k is not None and A.in_range(k,count):
      t=A.add(A.add(elapsed,A.scale(k,104)),C(j));hits[label]=A.minimum(hits[label],t) if label in hits else t
  contacts.update(hits)
  if count is None:base=A.apply_finite(field,data,base,0,'finite'+str(i));elapsed=A.add(elapsed,C(len(word)))
  else:
   assert len(word)==104 and word in std and data[3]==h and A.nonneg(A.sub(count,A.ONE));base=A.apply_periods(field,data,base,0,count,'period'+str(i));elapsed=A.add(elapsed,A.scale(count,104))
  h=data[3];records.append(dict(segment=i,time=elapsed,pose=[base,h],first_contacts=hits));print(json.dumps(records[-1]),flush=True)
 assert elapsed==lin(416,416,173038) and base==A.point(25,-61) and h==2 and T['infinite_tail_word']==W
 assert contacts=={'s':lin(104,0,10005),'Q':lin(104,104,16491),'C':lin(312,312,110526)}
 tw=T['infinite_tail_word'];assert tw in std;data=A.word_data(tw,h);assert data[3]==h and data[2]==(2,-2);proof=infinite_tail(field,data,base)
 def guard(q):assert A.nonneg(A.add(A.sub(*q),C(84))) and A.nonneg(A.sub(C(35),A.add(*q)))
 for q in A.READ_POINTS:guard(q)
 for b,d,count in A.READ_RAYS:guard(b);guard(tuple(A.add(v,A.scale(A.sub(count,A.ONE),e)) for v,e in zip(b,d)))
 for q in data[0]:guard(A.translate_local(q,base,0))
 out=dict(status='exact complete three-cell capture for all independent m,k>=100',domain='m=U+100,k=V+100; U,V independent nonnegative integers',initial=inputs,first_contacts=contacts,capture_time=elapsed,capture_pose=[base,h],tail=proof,tail_phase=next(j for j in range(104) if tw==W[j:]+W[:j]),whole_future_bounds={'u_lower':-84,'z_upper':35},records=records,statistics=A.STATS.copy(),template_sha256=hashlib.sha256(tp.read_bytes()).hexdigest(),scope='Entire finite initial field and full future retained. Recurrence coupling separately handles every allowed incidence shape.')
 (HERE/'certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
