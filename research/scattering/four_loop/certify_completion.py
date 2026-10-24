"""Exact all-L>=128 completion of the four-scatterer loop family.

This imports the previous exact affine-field prefix checker, rebuilds its
complete endpoint rather than dropping historical colors, checks a discovered
recovery/flight/recovery template, and proves an infinite P104 tail. No finite
parameter probes supply the universal conclusion.
"""
import hashlib,json,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
SRC=Path('/workspace/shared/langton/continuation_2026-10-22/ant_continuation/wake_clock')
sys.path[:0]=[str(SRC),str(SRC.parent)]
import certify_four_scatterer_prefix as a
from single_blocks import REFERENCE,block
from ant_exact import step,W,PHASES

def reset_checker():
 a.LOW=128
 assert a.LOW==128
 for key in a.STATS:a.STATS[key]=0
 a.READ_POINTS.clear();a.READ_RAYS.clear()

def get_prefix_field():
 source,p,h,_=REFERENCE
 source=source|block((-127,-108))
 prefix_reads=[]
 B=set();bp=(0,0);bh=0
 for _ in range(9977):
  prefix_reads.append(bp);bp,bh,_=step(B,bp,bh)
 assert not (set(prefix_reads)&block((-127,-108)))
 for _ in range(5781):
  assert p not in block((-127,-108))
  prefix_reads.append(p);p,h,_=step(source,p,h)
 assert p==(-127,-107) and h==2
 rb=set(source);rp=p;rh=h;letters=[]
 for _ in range(7183):rp,rh,c=step(rb,rp,rh);letters.append(c)
 F=''.join(letters);P=W[61:]+W[:61]
 fdata=a.word_data(F,2);pdata=a.word_data(P,3)
 assert fdata[2:]==((-24,25),3)
 assert pdata[2:]==((-2,2),3)
 starts=[a.point(-127,-107),((-2,-151),(2,-82)),((0,-126),(4,-58)),((2,-102),(2,-83))]
 G={(0,-1),(0,0),(1,-1),(1,0)}
 remote=[a.translate_local(g,starts[j],j) for j in range(1,4) for g in G]
 initial=[a.translate_local(g,starts[j],j) for j in range(4) for g in G]
 for i,q in enumerate(initial):
  for r in initial[i+1:]:assert a.no_point_collision(q,r)
 for q in prefix_reads:
  for r in remote:assert a.no_point_collision(a.point(*q),r)
 field=a.Field({a.point(*q) for q in source}|set(remote))
 for j in range(4):
  end=a.apply_finite(field,fdata,starts[j],j,'old F'+str(j))
  end=a.apply_periods(field,pdata,end,j,(1,0) if j<3 else (1,-65),'old P'+str(j))
  if j<3:assert end==starts[j+1]
 partial=a.word_data(P[:10],3)
 assert (partial[3]+3)%4==2
 end=a.apply_finite(field,partial,end,3,'old partial period')
 assert end==a.point(4,22) and field.point_color(end)
 return field,end,2

def clip_infinite(lo,hi):
 """Clip closed finite affine interval to integer k>=0; hi=None means infinity."""
 if hi is not None and a.negative(hi):return None
 lo=a.maximum(lo,a.ZERO)
 if hi is not None:
  if a.negative(a.sub(hi,lo)):return None
  assert a.nonneg(a.sub(hi,lo)),('tail interval order changes',lo,hi)
 return lo,hi

def toggle(boundaries,interval):
 if interval is None:return
 lo,hi=interval
 boundaries.symmetric_difference_update({lo})
 if hi is not None:boundaries.symmetric_difference_update({a.add(hi,a.ONE)})

def ray_intersection_infinite(q,d,base,e,M):
 delta=a.psub(base,q);det=d[0]*e[1]-d[1]*e[0]
 if det==0:
  m=a.line_coordinate(delta,d)
  if m is None:return None
  if e==d:lo,hi=m,a.add(m,a.sub(M,a.ONE))
  else:
   assert e==(-d[0],-d[1]);lo,hi=a.sub(m,a.sub(M,a.ONE)),m
  return clip_infinite(lo,hi)
 k=a.integer_affine(a.cross(delta,e),det)
 ell=a.integer_affine(a.cross(delta,d),det)
 if k is None or ell is None:return None
 if not a.in_range(ell,M):return None
 return clip_infinite(k,k)

def certify_infinite(field,data,base,j=0):
 required,odd,end,eh=data
 d=a.rotate(end,j);local_flips=[a.translate_local(q,base,j) for q in odd]
 assert d!=(0,0)
 counts=[]
 for q0,bit in required.items():
  q=a.translate_local(q0,base,j);boundaries=set();terms=0
  if bit:toggle(boundaries,(a.ZERO,None))
  for b in field.points:
   k=a.line_coordinate(a.psub(b,q),d)
   if k is not None:toggle(boundaries,clip_infinite(k,k));terms+=1
  for b,e,M,label in field.rays:
   interval=ray_intersection_infinite(q,d,b,e,M)
   toggle(boundaries,interval);terms+=interval is not None
  for b in local_flips:
   m=a.line_coordinate(a.psub(b,q),d)
   if m is not None:
    assert m[0]==0
    if m[1]>0:toggle(boundaries,(m,None));terms+=1
  assert not boundaries,('infinite tail mismatch',q0,sorted(boundaries))
  counts.append(terms)
 return {'read_ray_constraints':len(counts),'interval_terms':sum(counts),'drift':d}

def main():
 reset_checker()
 template=json.loads((HERE/'completion_template.json').read_text())
 for key in ('prefix_word','period_word','suffix_word'):
  assert template[key] and set(template[key])<={'R','L'}
 field,p,h=get_prefix_field()
 base_stats=dict(a.STATS)
 first=template['prefix_word'];period=template['period_word'];last=template['suffix_word']
 fd=a.word_data(first,h)
 p=a.apply_finite(field,fd,p,0,'recovery after old-core collision');h=fd[3]
 assert p==a.point(-19,33) and h==0
 pd=a.word_data(period,h)
 assert period in PHASES and pd[2:]==((-2,2),0)
 p=a.apply_periods(field,pd,p,0,(1,2),'new NW flight');h=pd[3]
 assert p==((-2,-23),(2,37)) and h==0
 ld=a.word_data(last,h)
 p=a.apply_finite(field,ld,p,0,'recovery after old-trail collision');h=ld[3]
 assert p==((-2,-40),(2,57)) and h==1
 tail=last[-104:]
 assert tail in PHASES
 td=a.word_data(tail,h)
 assert td[3]==h
 cert=certify_infinite(field,td,p)
 capture_time=a.add((416,37740),a.add((0,len(first)+len(last)),a.scale((1,2),len(period))))
 assert capture_time==(520,43111)
 out={'status':'all parameter integer proof passed; no global-conjecture claim',
  'parameter_domain':'integer L >= 128','initial_black_cells':16,
  'first_collision_time':[416,37740], 'first_collision_position':[4,22],
  'first_recovery_length':len(first), 'intermediate_flight_periods':[1,2],
  'second_recovery_length':len(last),'capture_time':capture_time,
  'capture_pose_affine':{'x':[-2,-40],'y':[2,57],'heading':'E'},
  'infinite_tail_certificate':cert,'tail_phase':PHASES[tail],
  'prefix_statistics':base_stats,'total_statistics':dict(a.STATS),
  'field_representation':{'affine_point_terms':len(field.points),'finite_ray_terms':len(field.rays)},
  'dependencies':{str(SRC/'certify_four_scatterer_prefix.py'):hashlib.sha256((SRC/'certify_four_scatterer_prefix.py').read_bytes()).hexdigest(),
   str(HERE/'completion_template.json'):hashlib.sha256((HERE/'completion_template.json').read_bytes()).hexdigest()}}
 (HERE/'completion_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
