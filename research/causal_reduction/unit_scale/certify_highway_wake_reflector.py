"""Exact two-parameter whole-board certificate for a one-shot104 wake reflector.
The complete collision word and all future tail reads are checked; no finite
period match is accepted as an infinite-tail proof.
"""
from pathlib import Path
import json,sys,hashlib,time
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parents[1]/'computability/unit_inductive_certificates'))
from presburger_read_set_solver import Context
D=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,k):
 x,y=p
 for _ in range(k):x,y=-y,x
 return x,y

def trace(w,p,h):
 rr=[]
 for c in w:
  rr.append((p,h,c));h=(h+(1 if c=='R'else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return rr,p,h

def xor(a,b):return a.subtract(b).union(b.subtract(a)).coalesce()
def main():
 st=time.monotonic();ctx=Context(max_operations=100000000)
 standard=json.loads(Path('/workspace/shared/langton/recovered_bundle/ant_global/root/standard.json').read_text());H=standard['word'];data=json.loads(HERE.joinpath('highway_wake_reflector_collision.json').read_text())
 domain='n>=30 and m>=30'
 def S(cond):return ctx.set('[n,m]->{[x,y]:'+domain+' and ('+cond+')}')
 def points(ps):return S(' or '.join(f'(x={x} and y={y})'for x,y in ps)or'false')
 def seed(k,x,y):return S(' or '.join(f'(x=({x})+{rot(p,k)[0]} and y=({y})+{rot(p,k)[1]})'for p in standard['seed']))
 def arm(h,x,y,count):
  rr,d,hh=trace(H,(0,0),h);assert hh==h
  parity=S('false');support=S('false')
  for p,_,c in rr:
   f=S(f'exists(i:0<=i<({count}) and x=({x})+{p[0]}+{d[0]}*i and y=({y})+{p[1]}+{d[1]}*i)')
   parity=xor(parity,f);support=support.union(f)
  return parity,support.coalesce()
 oldseed=seed(2,'-2*n','-2*n');oldparity,_=arm(1,'-2*n','-2*n','2*n');old=xor(oldseed,oldparity)
 incoming=seed(1,'-2*m+1','2*m');preparity,presupport=arm(2,'-2*m+1','2*m','m-10')
 assert old.intersect(incoming).is_empty(),'seed overlap'
 assert old.intersect(presupport).is_empty(),'old wake changes incoming prefix'
 initial=old.union(incoming);entry=xor(initial,preparity)
 C=data['collision_word'];rr,p,h=trace(C,(-19,20),2);assert len(C)==19872 and (p,h)==((-31,-10),0)
 req={};last={};odd=set()
 for t,(q,hh,c)in enumerate(rr):
  if q in last:assert last[q]!=c,('internal collision conflict',t,q)
  else:req[q]=c
  last[q]=c;odd.symmetric_difference_update({q})
 needblack=points([q for q,c in req.items()if c=='L']);needwhite=points([q for q,c in req.items()if c=='R'])
 assert needblack.subtract(entry).is_empty(),'collision missing input'
 assert needwhite.intersect(entry).is_empty(),'collision extra input'
 assert [list(q)for q in sorted(odd)]==data['complete_xor']
 after=xor(entry,points(odd))
 # The exact collision is not guard-renewable even just on the old wake strip.
 damaged=entry.intersect(points(odd)).intersect(old)
 old_changes=points(odd).intersect(S('-7<=x-y<=3'))
 # A full, infinite canonical104 tail from its exact endpoint.
 rows,d,hh=trace(H,p,h);assert d==(-33,-8) and hh==h
 F=[]
 for j,(q,head,c)in enumerate(rows):
  f=S(f'exists(i:i>=0 and x={q[0]}-2*i and y={q[1]}+2*i)')
  # time=104*i+j=-52*x+52*q_x+j
  F.append((f,52*q[0]+j,c))
 prior_count=0;bad=[]
 for i,(f,tf,c)in enumerate(F):
  ctx.reset_operations();black=after.intersect(f)
  for j,(g,tg,cg)in enumerate(F):
   if tg>=tf:continue
   prior=f.intersect(g)
   if not prior.is_empty():prior_count+=1;black=xor(black,prior)
  failure=f.subtract(black)if c=='L'else black
  if not failure.is_empty():bad.append(dict(slot=i,bad=str(failure)))
 assert not bad,bad[:1]
 # Verify fixed finite local ownership claims uniformly, not just their counts.
 # Restrict parametric differences to n=m=30; equality to a constant relation
 # proves the old-wake damage does not depend on either large parameter.
 def constant_slice(z):
  # Reconstruct by enumerating the finite literal XOR support, never scan a box.
  chosen=[]
  for q in odd:
   if not z.intersect(points([q])).intersect(ctx.set('[n,m]->{[x,y]:n=30 and m=30}')).is_empty():chosen.append(q)
  assert z.is_equal(points(chosen));return sorted(chosen)
 removed=constant_slice(damaged);changed=constant_slice(old_changes)
 out=dict(status='EXACT_ALL_PARAMETER_ALL_FUTURE_LEGAL',scope='One finite prepared-wake family, not a renewable reflector',domain='integers n>=30,m>=30',initial_old_seed_rotation_ccw=2,old_start=['-2*n','-2*n','E'],old_periods='2*n',incoming_seed_rotation_ccw=1,incoming_start=['-2*m+1','2*m','S'],incoming_prefix='H^(m-10)',cut_pose=[-19,20,'S'],collision_length=len(C),collision_read_support=len(req),complete_collision_xor=sorted(odd),complete_collision_xor_count=len(odd),erased_old_black_cells=removed,erased_old_black_count=len(removed),changed_old_wake_strip_cells=changed,changed_old_wake_strip_count=len(changed),tail_time='104*m+18832',tail_pose=[-31,-10,'N'],tail_word=H,tail_drift=[-2,2],tail_prior_relations=prior_count,tail_bad_sets=bad,initial_relation=str(initial.coalesce()),entry_relation=str(entry.coalesce()),postcollision_relation=str(after.coalesce()),collision_word_sha256=hashlib.sha256(C.encode()).hexdigest(),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),seconds=time.monotonic()-st,isl_version=ctx.version)
 HERE.joinpath('highway_wake_reflector_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in('complete_collision_xor','erased_old_black_cells','changed_old_wake_strip_cells','initial_relation','entry_relation','postcollision_relation','tail_word')},indent=2))
if __name__=='__main__':main()
