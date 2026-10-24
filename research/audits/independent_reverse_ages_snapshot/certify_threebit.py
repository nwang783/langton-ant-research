"""Exact independent n,p exceptional parent with complete old history."""
import sys,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'scattering/fixed_core_rectangle'))
from bivariate import A,infinite_tail
TFILE=ROOT/'continuation_2026-10-22/ant_continuation2/planar_structure/exceptional_rectangle_template.json'
N=(1,0,200);P=(0,1,200);C=lambda v:(0,0,v)
def ln(a,b):return A.add(A.scale(N,a),C(b))
def lp(a,b):return A.add(A.scale(P,a),C(b))
def main():
 assert hashlib.sha256(TFILE.read_bytes()).hexdigest()=='16246ec40cbdd4ad94c35698992582b27a942dc7d539683f1b3684892cd5687d'
 T=json.loads(TFILE.read_text());A.READ_POINTS.clear();A.READ_RAYS.clear()
 for key in A.STATS:A.STATS[key]=0
 q=(ln(-2,-33),ln(-2,-14));a=(ln(-2,-33),ln(2,41));c=(lp(2,8),lp(-2,-14))
 inputs={'q':q,'a':a,'c':c};field=A.Field(inputs.values());base=A.point(0,0);h=0;elapsed=C(0)
 periods={1:ln(1,8),3:ln(1,7),5:ln(1,5),7:ln(1,7),9:lp(1,-20),11:A.add(A.add(N,P),C(15)),13:C(13)}
 records=[];contacts={};post_points=[];post_rays=[];std={A.W[j:]+A.W[:j] for j in range(104)}
 for i,s in enumerate(T['segments']):
  word=s['word'];assert word and set(word)<={'R','L'} and s['type'] in ['finite','periods'];data=A.word_data(word,h);reads=A.plan(word,(0,0),h)[0];hits={}
  for j,b in enumerate(reads):
   actual=A.translate_local(b,base,0)
   for label,target in inputs.items():
    if label in contacts:continue
    if s['type']=='finite':
     if actual==target:
      if label not in hits:hits[label]=A.add(elapsed,C(j))
     else:assert A.no_point_collision(actual,target)
    else:
     k=A.line_coordinate(A.psub(target,actual),data[2])
     if k is not None and A.in_range(k,periods[i]):
      time=A.add(A.add(elapsed,A.scale(k,104)),C(j));hits[label]=A.minimum(hits[label],time) if label in hits else time
  contacts.update(hits)
  if i>=5:
   if s['type']=='finite':post_points.extend(A.translate_local(b,base,0) for b in reads)
   else:post_rays.extend((A.translate_local(b,base,0),data[2],periods[i]) for b in reads)
  if s['type']=='finite':base=A.apply_finite(field,data,base,0,'finite'+str(i));elapsed=A.add(elapsed,C(len(word)))
  else:
   count=periods[i];assert len(word)==104 and word in std and data[3]==h and A.nonneg(A.sub(count,A.ONE))
   base=A.apply_periods(field,data,base,0,count,'period'+str(i));elapsed=A.add(elapsed,A.scale(count,104))
  h=data[3];records.append(dict(segment=i,time=elapsed,pose=[base,h],contacts=hits));print(json.dumps(records[-1]),flush=True)
  if i==4:assert base==A.point(-15,26) and h==1 and elapsed==ln(208,70733)
 tw=T['infinite_tail_word'];assert tw==A.W[100:]+A.W[:100];data=A.word_data(tw,h);assert data[2]==(-2,2) and data[3]==h
 tail=infinite_tail(field,data,base)
 assert elapsed==A.add(A.add(A.scale(N,520),A.scale(P,208)),C(200304)) and base==(ln(-2,-58),ln(2,98)) and h==0
 assert contacts=={'q':ln(104,10881),'a':ln(312,71330),'c':A.add(A.add(A.scale(N,416),A.scale(P,104)),C(144036))}
 # Exact complete post-boundary z-strip, including every infinite-tail read.
 values=[A.add(q[0],q[1]) for q in post_points]
 for b,d,count in post_rays:
  z=A.add(b[0],b[1]);values.extend([z,A.add(z,A.scale(A.sub(count,A.ONE),sum(d)))])
 for b in data[0]:
  x=A.translate_local(b,base,0);assert sum(data[2])==0;values.append(A.add(x[0],x[1]))
 assert all(v[:2]==(0,0) for v in values);bounds=[min(v[2] for v in values),max(v[2] for v in values)];assert bounds==[-93,75]
 out=dict(status='exact complete three-cell parent for independent n,p>=200',domain='n=U+200,p=V+200; U,V nonnegative independent',initial=inputs,capture_time=elapsed,capture_pose=[base,h],tail=tail,tail_phase=100,first_contacts=contacts,post_boundary_z_bounds=bounds,records=records,statistics=A.STATS.copy(),source_template_sha256=hashlib.sha256(TFILE.read_bytes()).hexdigest(),scope='The independent retained-core age m is transferred separately using the exact complete-field half-plane identity.')
 (HERE/'threebit_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
