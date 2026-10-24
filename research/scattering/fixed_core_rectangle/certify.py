"""Exact all-n>=200 certificate with fixed core(-223,231)."""
import sys,json,hashlib,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation2/planar_structure')
import certify_exceptional_rectangle as old
A=old.A

def main():
 T=json.loads((HERE/'template.json').read_text());A.LOW=200
 for key in A.STATS:A.STATS[key]=0
 A.READ_POINTS.clear();A.READ_RAYS.clear();A.no_point_collision=old.fast_no_point_collision
 inputs={'s_fixed':A.point(-223,231),'q':((-2,-33),(-2,-14)),'a':((-2,-33),(2,41)),'c':((2,8),(-2,-14)),'d':((2,8),(2,41))}
 for i,p in enumerate(inputs.values()):
  for q in list(inputs.values())[i+1:]:assert A.no_point_collision(p,q)
 field=A.Field(set(inputs.values()));base=A.point(0,0);h=0;elapsed=A.ZERO;contacts={};records=[]
 standard={A.W[i:]+A.W[:i] for i in range(104)}
 for i,s in enumerate(T['segments']):
  assert s['word'] and set(s['word'])<={'R','L'}
  data=A.word_data(s['word'],h)
  hits=old.first_contacts(s,data,base,h,elapsed,inputs,contacts)
  if s['type']=='finite':
   base=A.apply_finite(field,data,base,0,'finite'+str(i));elapsed=A.add(elapsed,(0,len(s['word'])))
  else:
   assert s['type']=='periods' and s['word'] in standard and len(s['word'])==104
   N=tuple(s['count']);assert A.nonneg(A.sub(N,A.ONE)) and data[3]==h
   base=A.apply_periods(field,data,base,0,N,'periods'+str(i));elapsed=A.add(elapsed,A.scale(N,104))
  h=data[3];records.append(dict(segment=i,time=elapsed,base=base,heading=h,contacts=hits))
  print(json.dumps(records[-1]),flush=True)
 assert elapsed==(416,228904) and base==A.point(-228,268) and h==0
 assert contacts=={'q':(104,10881),'s_fixed':(208,81210),'c':(312,163796)}
 tw=T['infinite_tail_word'];assert tw in standard and set(tw)<={'R','L'}
 tail=A.word_data(tw,h);assert tail[3]==h and tail[2]==(-2,2)
 tailproof=old.verify_infinite_period(field,tail,base)
 for label in ('a','d'):
  target=inputs[label]
  for p in A.READ_POINTS:assert A.no_point_collision(p,target)
  for b,d,N in A.READ_RAYS:assert not A.ray_membership(target,b,d,N)
  for p in tail[0]:
   j=A.line_coordinate(A.psub(target,A.translate_local(p,base,0)),tail[2])
   assert j is None or A.negative(j)
 out=dict(status='exact complete-field all-parameter proof passed',domain='integer n>=200',fixed_core=[-223,231],capture_time=elapsed,capture_pose=[base,h],tail=tailproof,first_contacts=contacts,never_read=['a','d'],statistics=A.STATS,template_sha256=hashlib.sha256((HERE/'template.json').read_bytes()).hexdigest(),records=records)
 (HERE/'certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
