"""Exact full-field, all-future certificate for the same-sector NW->NE wake corner.
A prepared one-shot interface, not a repeated or renewable construction.
"""
from pathlib import Path
import sys,json,time,hashlib
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'computability/unit_inductive_certificates'))
from presburger_read_set_solver import Context
from certify_highway_wake_reflector import trace,rot,xor
ctx=Context(max_operations=200000000);st=time.monotonic()
standard=json.loads(Path('/workspace/shared/langton/recovered_bundle/ant_global/root/standard.json').read_text());H=standard['word']
def S(c):return ctx.set('[n,m]->{[x,y]:n>=50 and m>=50 and ('+c+')}')
def points(qs):return S(' or '.join(f'(x={x} and y={y})'for x,y in qs)or'false')
def seed(k,x,y):return S(' or '.join(f'(x=({x})+{rot(q,k)[0]} and y=({y})+{rot(q,k)[1]})'for q in standard['seed']))
def arm(h,x,y,count):
 rr,d,hh=trace(H,(0,0),h);assert hh==h
 parity=S('false');support=S('false')
 for q,_,c in rr:
  f=S(f'exists(i:0<=i<({count}) and x=({x})+{q[0]}+{d[0]}*i and y=({y})+{q[1]}+{d[1]}*i)')
  parity=xor(parity,f);support=support.union(f)
 return parity,support.coalesce()
oldparity,_=arm(1,'-2*n','-2*n','2*n');old=xor(seed(2,'-2*n','-2*n'),oldparity)
incoming=seed(3,'2*m+3','-2*m');preparity,presupport=arm(0,'2*m+3','-2*m','m-10')
assert old.intersect(incoming).is_empty();assert old.intersect(presupport).is_empty()
initial=old.union(incoming);entry=xor(initial,preparity)
data=json.loads((P/'opposite_wake_quarter_turn_word.json').read_text());C=data['word'];rr,p,h=trace(C,(23,-20),0)
assert len(C)==43871 and(p,h)==((91,-63),1)
req={};last={};odd=set()
for t,(q,hh,c)in enumerate(rr):
 if q in last:assert last[q]!=c,('internal conflict',t,q)
 else:req[q]=c
 last[q]=c;odd.symmetric_difference_update({q})
needblack=points([q for q,c in req.items()if c=='L']);needwhite=points([q for q,c in req.items()if c=='R'])
assert needblack.subtract(entry).is_empty(),'missing black';assert needwhite.intersect(entry).is_empty(),'extra black'
assert sorted(odd)==list(map(tuple,data['complete_xor']))
after=xor(entry,points(odd));rows,end,hh=trace(H,p,h);assert end==(93,-61)and hh==h
F=[]
for j,(q,head,c)in enumerate(rows):
 f=S(f'exists(i:i>=0 and x={q[0]}+2*i and y={q[1]}+2*i)');F.append((f,j-52*q[0],c))
prior=0
for j,(f,tf,c)in enumerate(F):
 ctx.reset_operations();black=after.intersect(f)
 for g,tg,cg in F:
  if tg>=tf:continue
  a=f.intersect(g)
  if not a.is_empty():prior+=1;black=xor(black,a)
 bad=f.subtract(black)if c=='L'else black
 assert bad.is_empty(),('tail',j,str(bad))
# Exact fixed old-wake damage and collision ownership, not only total counts.
removed=[];changed=[]
for q in odd:
 a=points([q]);hit=old.intersect(a)
 if not hit.is_empty():assert hit.is_equal(a);removed.append(q)
 if -7<=q[0]-q[1]<=3:changed.append(q)
assert old.intersect(points(odd)).is_equal(points(removed))
out=dict(status='EXACT_ALL_PARAMETER_ALL_FUTURE_LEGAL',scope='One prepared same-sector right-angle wake corner; no renewal asserted',domain='n>=50 and m>=50',incoming_seed_rotation_ccw=3,incoming_start=['2*m+3','-2*m','N'],old_start=['-2*n','-2*n','E'],old_periods='2*n',word='H^(m-10) C H^infinity',collision_length=len(C),collision_read_support=len(req),collision_xor_count=len(odd),collision_charge=data['charge'],collision_read_bounds=data['read_bounds'],collision_start=[23,-20,'N'],collision_end=[91,-63,'E'],old_removed_black=sorted(removed),old_removed_black_count=len(removed),old_strip_changed=sorted(changed),old_strip_changed_count=len(changed),tail_time='104*m+42831',tail_pose=[91,-63,'E'],tail_drift=[2,2],tail_mass='24*n+12*m+2027',initial_mass='24*n+26',tail_prior_relations=prior,initial_relation=str(initial.coalesce()),entry_relation=str(entry.coalesce()),postcollision_relation=str(after.coalesce()),collision_word_sha256=data['word_sha256'],source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),seconds=time.monotonic()-st)
(P/'opposite_wake_quarter_turn_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items()if k not in('old_removed_black','old_strip_changed','initial_relation','entry_relation','postcollision_relation')})
