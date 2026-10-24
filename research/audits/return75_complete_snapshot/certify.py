"""Exact one-variable cap75 parent and complete rectangular cycle."""
import sys,json,gzip,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];CAP=HERE.parent/'blank_return_cap'
sys.path.insert(0,str(HERE.parent/'fixed_core_rectangle'));from bivariate import A,infinite_tail
from ant_exact import W,plan
sys.path.insert(0,str(CAP));from discover import initial
from crossing import tail
N=(1,0,200);C=lambda v:(0,0,v)
def lin(a,b):return A.add(A.scale(N,a),C(b))
def main(kind):
 assert kind in ['parent','cycle'];mp=CAP/'manifest.json';assert hashlib.sha256(mp.read_bytes()).hexdigest()=='2827291464278a15841e21a0430de38d18f990f01827f7adb0d43cfb5dbe9237';mf=json.loads(mp.read_text())['files']
 for name in ['fixed_caps.json','bridge.json','discover.py','word_r75.txt.gz']:assert hashlib.sha256((CAP/name).read_bytes()).hexdigest()==mf[name]
 row=next(x for x in json.loads((CAP/'fixed_caps.json').read_text())['rows'] if x['phase']==75);F,p,h=initial(75);assert [list(p),h]==row['start'];word=gzip.open(CAP/'word_r75.txt.gz','rt').read();assert len(word)==row['capture']==19656 and set(word)<={'R','L'} and hashlib.sha256(word.encode()).hexdigest()==row['word_sha256']
 for c in word:p,h,ch=F.step(p,h);assert c==ch
 assert (p,h)==((46,-37),1) and row['tail_phase']==55 and tail(F,p,h,W[55:]+W[:55])
 points=[A.point(*q) for q in F.changes];qC=(lin(2,24),lin(-2,-12));qA=(lin(-2,-35),lin(2,109));qD=(lin(2,24),lin(2,109));inputs={'C':qC} if kind=='parent' else {'C':qC,'A':qA,'D':qD}
 for q in inputs.values():assert all(A.no_point_collision(q,v) for v in points)
 for q in inputs.values():
  for b,d,lo,hi in F.rays:assert A.line_coordinate(A.psub(q,A.point(*b)),d) is None
 field=A.Field(points+list(inputs.values()));ray_u=[]
 for i,(b,d,lo,hi) in enumerate(F.rays):
  assert lo==0 and hi is None and d==(-2,-2);assert sum(b)+100*sum(d)<-250;field.add_rays([A.point(*b)],d,C(100),'oldrail'+str(i));ray_u.append(b[0]-b[1])
 for k in A.STATS:A.STATS[k]=0
 A.READ_POINTS.clear();A.READ_RAYS.clear();base=A.point(*p);elapsed=C(0);records=[];contacts={};tp=HERE/f'template_{kind}.json';T=json.loads(tp.read_text());assert T['kind']==kind;std={W[j:]+W[:j] for j in range(104)}
 for i,s in enumerate(T['segments']):
  word=s['word'];assert word and set(word)<={'R','L'} and s['type'] in ['finite','periods'];data=A.word_data(word,h);reads=plan(word,(0,0),h)[0];count=None if s['type']=='finite' else lin(*s['count_n']);hits={}
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
  if count is None:base=A.apply_finite(field,data,base,0,'fixed'+str(i));elapsed=A.add(elapsed,C(len(word)))
  else:
   assert len(word)==104 and word in std and data[3]==h and A.nonneg(A.sub(count,A.ONE));base=A.apply_periods(field,data,base,0,count,'flight'+str(i));elapsed=A.add(elapsed,A.scale(count,104))
  h=data[3];records.append(dict(segment=i,time=elapsed,pose=[base,h],contacts=hits));print(json.dumps(records[-1]),flush=True)
 assert contacts['C']==lin(104,-1231)
 if kind=='cycle':assert contacts=={'C':lin(104,-1231),'A':lin(312,54047)}
 tw=T['infinite_tail_word'];assert tw in std;data=A.word_data(tw,h);assert data[3]==h;proof=infinite_tail(field,data,base)
 def bounds(q):
  z=A.add(q[0],q[1]);assert A.nonneg(A.add(z,C(51)))
  if kind=='cycle':assert A.nonneg(A.sub(C(137),z))
 for q in A.READ_POINTS:bounds(q)
 for b,d,count in A.READ_RAYS:bounds(b);bounds(tuple(A.add(v,A.scale(A.sub(count,A.ONE),e)) for v,e in zip(b,d)))
 tus=[];tzs=[]
 for q in data[0]:
  q=A.translate_local(q,base,0);u=A.sub(q[0],q[1]);z=A.add(*q);tus.append(u);tzs.append(z)
  if kind=='parent':assert A.nonneg(A.add(z,C(51)))
  else:
   assert A.nonneg(A.sub(C(min(ray_u)-1),u));assert A.nonneg(A.sub(C(-250),u));assert A.nonneg(A.sub(C(137),z));assert A.nonneg(A.sub(A.add(*qD),A.add(z,C(1))))
 assert data[2]==((-2,2) if kind=='parent' else (-2,-2))
 assert tw==W
 if kind=='parent':assert elapsed==lin(104,49815) and base==(lin(2,53),lin(-2,27)) and h==0
 else:assert elapsed==lin(520,133554) and base==(lin(-2,-67),lin(2,72)) and h==3
 tail_ub=[min(tus,key=lambda a:a[2]),max(tus,key=lambda a:a[2])];assert all(v[:2]==tail_ub[0][:2] for v in tus)
 out=dict(status='exact all-N finite-kernel color theorem with complete infinite-rail transfer',kind=kind,domain='N=U+200, U>=0',initial_new_markers=inputs,first_contacts=contacts,capture_time=elapsed,capture_pose=[base,h],tail=proof,tail_phase=next(j for j in range(104) if tw==W[j:]+W[:j]),prefix_z_lower=-51,prefix_z_upper=137 if kind=='cycle' else None,tail_u_bounds=tail_ub,tail_u_values=tus,tail_z_values=tzs,omitted_rail_u_range=[min(ray_u),max(ray_u)],D_never_read=kind=='cycle',records=records,statistics=A.STATS.copy(),template_sha256=hashlib.sha256(tp.read_bytes()).hexdigest(),cap_manifest_sha256=hashlib.sha256(mp.read_bytes()).hexdigest(),scope='Actual finite-history comparison additionally requires the separate cap interface and final-tail discrepancy guard.')
 (HERE/f'{kind}_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main(sys.argv[1])
