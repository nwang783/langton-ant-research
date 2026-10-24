"""Exact complete-field one-parameter proofs of discovered two-bit parents."""
import json,sys,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation2/planar_structure')
import certify_exceptional_rectangle as old
A=old.A

def bounds(points,rays):
 vals={'z':[],'u':[]}
 def add(q):
  vals['z'].append(A.add(q[0],q[1]));vals['u'].append(A.sub(q[0],q[1]))
 for q in points:add(q)
 for ray in rays:
  b,d,N=ray[:3]
  add(b);add(A.padd(b,(A.scale(A.sub(N,A.ONE),d[0]),A.scale(A.sub(N,A.ONE),d[1]))))
 result={}
 for norm,coords in vals.items():
  result[norm+'_upper']=max(a*A.LOW+b for a,b in coords) if all(a<=0 for a,b in coords) else None
  result[norm+'_lower']=min(a*A.LOW+b for a,b in coords) if all(a>=0 for a,b in coords) else None
 return result

def main(m):
 T=json.loads((HERE/f'branch_m{m}_template.json').read_text());A.LOW=200
 for k in A.STATS:A.STATS[k]=0
 A.READ_POINTS.clear();A.READ_RAYS.clear();A.no_point_collision=old.fast_no_point_collision
 inputs={'s':A.point(-23-2*m,31+2*m),'q':((-2,-33),(-2,-14))}
 assert m in (1,6)
 if m==1:inputs['a']=((-2,-33),(2,-21))
 else:inputs['c']=((2,12),(-2,-14))
 for i,p in enumerate(inputs.values()):
  for q in list(inputs.values())[i+1:]:assert A.no_point_collision(p,q)
 field=A.Field(set(inputs.values()));base=A.point(0,0);h=0;elapsed=A.ZERO;contacts={};records=[]
 standard={A.W[i:]+A.W[:i] for i in range(104)}
 for i,s in enumerate(T['segments']):
  assert s['word'] and set(s['word'])<={'R','L'}
  data=A.word_data(s['word'],h);hits=old.first_contacts(s,data,base,h,elapsed,inputs,contacts)
  if s['type']=='finite':
   base=A.apply_finite(field,data,base,0,'finite'+str(i));elapsed=A.add(elapsed,(0,len(s['word'])))
  else:
   assert s['type']=='periods' and s['word'] in standard and len(s['word'])==104
   N=tuple(s['count']);assert A.nonneg(A.sub(N,A.ONE)) and data[3]==h
   base=A.apply_periods(field,data,base,0,N,'periods'+str(i));elapsed=A.add(elapsed,A.scale(N,104))
  h=data[3];records.append(dict(segment=i,time=elapsed,base=base,heading=h,contacts=hits))
  print(json.dumps(dict(m=m,**records[-1])),flush=True)
 assert elapsed==tuple(T['time']);assert base==tuple(zip(T['pose_coeff'],T['pose_constant']));assert h==T['heading']
 expected={'q':(104,10881),'s':(208,104*m+70810)}
 expected.update({'a':(312,92814)} if m==1 else {'c':(312,112212)})
 assert contacts==expected
 tw=T['infinite_tail_word'];assert tw in standard and set(tw)<={'R','L'}
 tail=A.word_data(tw,h);assert tail[3]==h and tail[2]==tuple(T['drift'])
 tailproof=old.verify_infinite_period(field,tail,base)
 # Exact support envelopes include all full-field terms, conservatively before XOR cancellation.
 fb=bounds(field.points,field.rays);rb=bounds(A.READ_POINTS,A.READ_RAYS)
 phase=next(i for i in range(104) if A.W[i:]+A.W[:i]==tw)
 skip=(72-phase)%104;offset=A.word_data(tw[:skip],h)[2] if skip else (0,0)
 exc=A.translate_local(offset,base,0)
 tailnormals={}
 for norm,name in [((1,1),'z'),((1,-1),'u')]:
  if sum(norm[i]*tail[2][i] for i in (0,1))==0:
   vv=[A.add(A.scale(A.add(base[0],(0,q[0])),norm[0]),A.scale(A.add(base[1],(0,q[1])),norm[1])) for q in tail[0]]
   assert all(v[0]==0 for v in vv)
   tailnormals[name]=[min(v[1] for v in vv),max(v[1] for v in vv)]
 out=dict(status='exact complete-field all-n proof passed',m=m,domain='integer n>=200',capture_time=elapsed,capture_pose=[base,h],tail=tailproof,tail_phase=phase,exceptional_phase72_ray=[exc,tail[2]],tail_fixed_normals=tailnormals,first_contacts=contacts,complete_field_support_bounds=fb,finite_read_bounds=rb,statistics=A.STATS.copy(),template_sha256=hashlib.sha256((HERE/f'branch_m{m}_template.json').read_bytes()).hexdigest(),records=records)
 (HERE/f'branch_m{m}_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
 return out

if __name__=='__main__':
 which=list(map(int,sys.argv[1:])) or [1,6]
 for m in which:main(m)
