"""Exact two-contact capture for the43-cell four-corner loop, every r>=50.
The NW front after the first local transient is NOT prematurely called capture:
it collides with the remote side written by the first loop, then resumes NW.
"""
from pathlib import Path
import sys,json,time,hashlib
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'computability/unit_inductive_certificates'))
from presburger_read_set_solver import Context
from certify_highway_wake_reflector import trace,xor
from probe_perpendicular_highway_wake import H
ctx=Context(max_operations=200000000);st=time.monotonic()
def S(c):return ctx.set('[r]->{[x,y]:r>=50 and ('+c+')}')
def pts(ps,org):
 ax,bx,ay,by=org
 return S(' or '.join(f'(x={ax}*r+{bx+x} and y={ay}*r+{by+y})'for x,y in ps)or'false')
loop=json.loads((P/'four_corner_loop_certificate.json').read_text());B=ctx.set(loop['output_relation']).intersect(S('true'));stages=[]
def fixed(name,w,org,h):
 global B
 rr,d,h1=trace(w,(0,0),h);last={};first={};odd=set()
 for q,hh,c in rr:
  if q in last:assert last[q]!=c
  else:first[q]=c
  last[q]=c;odd.symmetric_difference_update({q})
 black=pts([q for q,c in first.items()if c=='L'],org);white=pts([q for q,c in first.items()if c=='R'],org)
 assert black.subtract(B).is_empty(),name+' missing black';assert white.intersect(B).is_empty(),name+' extra black'
 B=xor(B,pts(odd,org));stages.append(dict(name=name,length=len(w),read_cells=len(first),complete_xor=len(odd),charge=w.count('R')-w.count('L'),word_sha256=hashlib.sha256(w.encode()).hexdigest()))
 return(org[0],org[1]+d[0],org[2],org[3]+d[1]),h1
def arm(name,org,h,count):
 global B
 rr,d,h1=trace(H,(0,0),h);assert h1==h and d==(-2,2)
 ax,bx,ay,by=org;F=[];prior=0
 for j,(q,hh,c)in enumerate(rr):
  bound='i>=0'if count is None else f'0<=i<{count}'
  f=S(f'exists(i:{bound} and x={ax}*r+{bx+q[0]}-2*i and y={ay}*r+{by+q[1]}+2*i)')
  F.append((f,j+52*q[0],c))
 for f,tf,c in F:
  ctx.reset_operations();black=B.intersect(f)
  for g,tg,cg in F:
   if tg>=tf:continue
   before=f.intersect(g)
   if not before.is_empty():prior+=1;black=xor(black,before)
  bad=f.subtract(black)if c=='L'else black
  assert bad.is_empty(),(name,str(bad))
 stages.append(dict(name=name,periods=count if count else'infinite',prior_relations=prior))
 if count is not None:
  for f,tf,c in F:B=xor(B,f)
C=json.loads((P/'four_corner_capture_word.json').read_text())['word'];D=json.loads((P/'four_corner_capture_word2.json').read_text())['word']
org,h=fixed('local continuation',C,(0,0,0,0),0);assert(org,h)==((0,13,0,33),0)
arm('intervening NW front',org,h,'r-10')
org,h=fixed('remote written-side collision',D,(-2,33,2,13),0);assert(org,h)==((-2,2,2,38),0)
full_tail_entry=str(B.coalesce());arm('final NW front',org,h,None)
q=C.count('R')-C.count('L')+D.count('R')-D.count('L')
out=dict(status='EXACT_ALL_R_ALL_FUTURE_CAPTURE',domain='r>=50',initial_mass=43,word='L_r C H^(r-10) D H^infinity',local_C_length=len(C),remote_D_length=len(D),capture_time='520*r+13640',capture_pose=['-2*r+2','2*r+38','N'],drift=[-2,2],capture_mass=f'60*r+{87+q-120}',stages=stages,full_tail_entry=full_tail_entry,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),loop_certificate_sha256=hashlib.sha256((P/'four_corner_loop_certificate.json').read_bytes()).hexdigest(),seconds=time.monotonic()-st)
(P/'four_corner_capture_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='full_tail_entry'})
