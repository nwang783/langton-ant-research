"""Exact half-plane endpoint state shared by four incoming clean NW tracks.
All affine field reconstruction inherits its color validity from the complete
third-band certificates; restriction itself is proved over the entire quadrant.
"""
import sys,json,hashlib
from pathlib import Path
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'scattering/return_nw_frontier'))
from full_field import A,source_field,C,W,plan,canonical_source
sys.path.insert(0,str(ROOT/'scattering/transverse'))
from crossing import Field,tail,multiple
from ant_exact import D
M=(1,0,100);N=(1,1,200);WIDTH=0
PARENT=ROOT/'scattering/return_nw_frontier'
K0=(A.scale(N,-2),A.scale(N,2))

def restrict(field,origin=K0):
 """Exact XOR restriction to u<=0, all z, producing a constant finite set."""
 out=set();stats=dict(points_outside=0,rays_outside=0,points_inside=0,rays_inside=0)
 def interval(base,drift,count):
  b=A.psub(base,origin);u=A.sub(b[0],b[1]);z=A.add(b[0],b[1])
  end=u if count==1 else A.add(u,A.scale(A.sub(count,A.ONE),drift[0]-drift[1]))
  low=end if drift[0]-drift[1]<0 else u
  if A.negative(A.sub(C(WIDTH),low)):
   stats['points_outside' if count==1 else 'rays_outside']+=1;return
  if count==1:
   assert b[0][:2]==b[1][:2]==(0,0) and u[2]<=WIDTH
   out.symmetric_difference_update({(b[0][2],b[1][2])});stats['points_inside']+=1;return
  assert drift in ((2,-2),(-2,2)) and z[:2]==(0,0) and b[0][0]%2==b[0][1]%2==0,(b,drift,count)
  parity=b[0][2]%2;t=tuple(v//2 for v in A.sub(b[0],C(parity)));upper=(WIDTH+z[2]-2*parity)//4
  if drift==(2,-2):lo=t;hi=A.add(t,A.sub(count,A.ONE))
  else:lo=A.sub(t,A.sub(count,A.ONE));hi=t
  if A.nonneg(A.sub(lo,C(upper+1))):return
  if A.nonneg(A.sub(hi,C(upper))):hi=C(upper)
  else:assert A.nonneg(A.sub(C(upper),hi))
  assert lo[:2]==hi[:2]==(0,0) and lo[2]<=hi[2],(lo,hi)
  out.symmetric_difference_update((2*k+parity,z[2]-2*k-parity) for k in range(lo[2],hi[2]+1));stats['rays_inside']+=1
 for p in field.points:interval(p,(0,0),1)
 for base,drift,count,label in field.rays:interval(base,drift,count)
 return out,stats

def canonical_clip(p,h,phase):
 B,q,hh=canonical_source(0,phase);assert (hh+2)%4==h
 offset=(p[0]+q[0],p[1]+q[1]);out={(offset[0]-x,offset[1]-y) for x,y in B if offset[0]-x-offset[1]+y<=WIDTH}
 for d in D:
  j=1
  while True:
   v=(offset[0]-d[0]+2*j,offset[1]-d[1]-2*j)
   if v[0]-v[1]>WIDTH:break
   out.symmetric_difference_update({v});j+=1
 return out

def main():
 base,O,T,I=source_field(M,N)
 base.points={A.padd(p,O) for p in base.points};base.rays=[(A.padd(b,O),d,c,l) for b,d,c,l in base.rays]
 common,base_stats=restrict(base);records=[];literal_cases=[]
 marker=(10**60,10**60+1);base.add_points([A.padd(K0,A.point(*marker))]);negative,_=restrict(base);assert negative==common^{marker}
 for r in (28,38,60,75):
  file=PARENT/f'full_return_template_r{r}.json';template=json.loads(file.read_text());cert=json.loads((PARENT/f'full_return_certificate_r{r}.json').read_text());assert cert['template_sha256']==hashlib.sha256(file.read_bytes()).hexdigest()
  field,O,T,I=source_field(M,N);qs,_,_,_=plan(W,(0,0),0);field.add_points([A.point(*qs[r]),A.psub((A.add(A.scale(N,2),C(8)),A.add(A.scale(N,2),C(41))),O)])
  field.points={A.padd(p,O) for p in field.points};field.rays=[(A.padd(b,O),d,c,l) for b,d,c,l in field.rays]
  p=O;h=0
  for s in template['segments'][:-1]:
   word=s['word'];assert word and set(word)<={'R','L'};_,odd,end,eh=A.word_data(word,h)
   if s['type']=='finite':field.add_points(A.translate_local(q,p,0) for q in odd);p=A.translate_local(end,p,0)
   else:
    assert len(word)==104 and eh==h;an,am,b=s['count_nm'];count=A.add(A.add(A.scale(N,an),A.scale(M,am)),C(b));assert A.nonneg(A.sub(count,A.ONE))
    field.add_rays([A.translate_local(q,p,0) for q in odd],end,count,'incoming');p=A.padd(p,(A.scale(count,end[0]),A.scale(count,end[1])))
   h=eh
  relative=A.psub(p,K0);assert relative[0][:2]==relative[1][:2]==(0,0);pos=(relative[0][2],relative[1][2]);incoming=template['segments'][-2]['word'];phase=next(j for j in range(104) if incoming==W[j:]+W[:j])
  exact,stats=restrict(field);canonical=canonical_clip(pos,h,phase)
  assert common.isdisjoint(canonical)
  assert exact==common^canonical,('not the same old cap',r,len(exact^common^canonical))
  f=Field((),exact);word=template['segments'][-1]['word'];start=(pos,h);read=[];first=None
  for i,ch in enumerate(word):
   read.append(pos);assert pos[0]-pos[1]<=WIDTH
   pos,h,actual=f.step(pos,h);assert actual==ch,(r,i)
   if first is None and ch!=incoming[i%104]:first=i
  tw=template['infinite_tail_word'];phaseout=next(j for j in range(104) if tw==W[j:]+W[:j]);proof=tail(f,pos,h,tw);assert proof
  qs,_,drift,eh=plan(tw,pos,h);assert (drift[0]-pos[0],drift[1]-pos[1])==(-2,2)
  assert max(x-y for x,y in qs)<=WIDTH
  assert pos==(-32,72) and h==0 and phaseout==100
  residual=f.changes^canonical_clip(pos,h,phaseout)
  assert all(multiple((q[0]-v[0],q[1]-v[1]),(-2,2)) is None or multiple((q[0]-v[0],q[1]-v[1]),(-2,2))<0 for q in residual for v in qs)
  future=(qs[0][0]-2*10**60,qs[0][1]+2*10**60);assert tail(Field((),f.changes^{future}),pos,h,tw) is None
  literal_cases.append((r,start,phase,word,tw,set(read),qs))
  records.append(dict(phase=r,input_pose=start,input_word_phase=phase,endpoint_word_length=len(word),first_clean_word_mismatch=first,output_pose=[pos,h],output_word_phase=phaseout,read_u_upper=max(x-y for x,y in read+qs),cap_black_cells=len(common),full_initial_kernel_size=len(exact),residual_cap_size=len(residual),cap_update_size=len(residual^common),cap_update=sorted(residual^common),restriction_statistics=stats,template_sha256=hashlib.sha256(file.read_bytes()).hexdigest()))
  print(json.dumps({k:v for k,v in records[-1].items() if k!='cap_update'}),flush=True)
 read_cap=set()
 for r,start,phase,word,tw,finite_reads,tail_reads in literal_cases:
  for q in common:
   if q in finite_reads or any((k:=multiple((q[0]-v[0],q[1]-v[1]),(-2,2))) is not None and k>=0 for v in tail_reads):read_cap.add(q)
 reduced=[]
 for r,(p,h),phase,word,tw,finite_reads,tail_reads in literal_cases:
  assert read_cap.isdisjoint(canonical_clip(p,h,phase))
  seed=read_cap^canonical_clip(p,h,phase);f=Field((),seed)
  for ch in word:p,h,actual=f.step(p,h);assert actual==ch
  assert tail(f,p,h,tw) and p==(-32,72) and h==0
  residual=f.changes^canonical_clip(p,h,100)
  reduced.append(dict(phase=r,initial_kernel_size=len(seed),residual_size=len(residual),cap_update_size=len(residual^read_cap),cap_update=sorted(residual^read_cap)))
 assert len(common)==2458 and len(read_cap)==387
 assert [r['cap_update_size'] for r in reduced]==[589,585,1295,589]
 assert [r['residual_size'] for r in reduced]==[774,636,1228,774]
 out=dict(reduced_common_cap=sorted(read_cap),reduced_cap_black_cells=len(read_cap),reduced_rules=reduced,negative_controls='unbounded-z half-plane marker retained; all four tails reject a marker10^60 periods ahead',status='four exact finite half-plane endpoint rules with a common old cap',domain='all incoming configurations agreeing with stated finite kernel throughout u<=0; no restriction outside',common_cap=sorted(common),source_domain='m>=100,n-m>=100',source_restriction_statistics=base_stats,records=records)
 (HERE/'common_cap_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
