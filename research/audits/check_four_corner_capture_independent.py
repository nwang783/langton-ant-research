"""Independent all-r two-contact continuation, retaining the complete loop field."""
from pathlib import Path
import json,time,hashlib
import check_four_corner_loop_independent as L
D=L.D;ctx=L.ctx;B=L.after;started=time.monotonic();J=json.loads((D/'four_corner_capture_certificate.json').read_text())
def S(c):return ctx.set('[r]->{[x,y]:r>=50 and ('+c+')}')
def T(c):return ctx.set('[r]->{[t]:r>=50 and ('+c+')}')
B=B.intersect(S('true'));stages=[];timeA=416;timeB=268;massA=48;massB=87;originA=originB=0j;heading=1j

def points(ps):
 ax,ay=L.xy(originA);bx,by=L.xy(originB)
 return S(' or '.join(f'(x={ax}*r+{bx+x} and y={ay}*r+{by+y})'for x,y in map(L.xy,ps))or'false')
def fixed(name,w):
 global B,originB,heading,timeB,massB
 slots,d,h=L.tr(w,heading);first={};last={};odd=set()
 for z,c,j in slots:
  if z in last:assert last[z]!=c,(name,j,z)
  else:first[z]=c
  last[z]=c;odd.symmetric_difference_update([z])
 black=points([z for z,c in first.items()if c=='L']);white=points([z for z,c in first.items()if c=='R'])
 assert black.subtract(B).is_empty() and white.intersect(B).is_empty(),name
 B=L.xor(B,points(odd));originB+=d;heading=h;timeB+=len(w);massB+=w.count('R')-w.count('L')
 stages.append({'name':name,'length':len(w),'read_cells':len(first),'complete_XOR':len(odd),'word_sha256':hashlib.sha256(w.encode()).hexdigest()})
def arm(name,count):
 global B,originA,originB,heading,timeA,timeB,massA,massB
 slots,d,h=L.tr(L.H,heading);assert d==-2+2j and h==heading
 ax,ay=L.xy(originA);bx,by=L.xy(originB);dx,dy=L.xy(d)
 bound='t>=0'if count is None else f'0<=t<{count[0]}*r+{count[1]}'
 prior_count=0
 for z,c,j in slots:
  ctx.reset_operations();x,y=L.xy(z)
  selector=ctx.map(f'[r]->{{[x,y]->[t]:r>=50 and {bound} and x={ax}*r+{bx+x}+{dx}*t and y={ay}*r+{by+y}+{dy}*t}}')
  black=selector.binary('intersect_domain',B).range()
  for zz,cc,k in slots:
   xx,yy=L.xy(zz);old=T(f'{bound} and exists(u:{bound.replace("t","u")} and {x}+{dx}*t={xx}+{dx}*u and {y}+{dy}*t={yy}+{dy}*u and 104*u+{k}<104*t+{j})')
   if not old.is_empty():prior_count+=1;black=L.xor(black,old)
  assert(T(bound).subtract(black)if c=='L'else black).is_empty(),(name,j)
 assert prior_count==262
 if count is not None:
  a,b=count
  for z,c,j in slots:
   x,y=L.xy(z);family=S(f'exists(t:{bound} and x={ax}*r+{bx+x}+{dx}*t and y={ay}*r+{by+y}+{dy}*t)');B=L.xor(B,family)
  originA+=a*d;originB+=b*d;timeA+=104*a;timeB+=104*b;massA+=12*a;massB+=12*b
 stages.append({'name':name,'ordered_slot_pairs':104**2,'prior_relations':prior_count,'count':count})
C=json.loads((D/'four_corner_capture_word.json').read_text())['word'];W=json.loads((D/'four_corner_capture_word2.json').read_text())['word']
assert set(C+W)<={'R','L'} and (len(C),len(W))==(4954,9458)
fixed('first local continuation',C);assert(originA,originB,heading)==(0j,13+33j,1j)
arm('finite NW segment',(1,-10));assert(originA,originB,heading)==(-2+2j,33+13j,1j)
fixed('remote written-side contact',W);assert(originA,originB,heading)==(-2+2j,2+38j,1j)
assert B.is_equal(ctx.set(J['full_tail_entry']))
assert(timeA,timeB,massA,massB)==(520,13640,60,795)
arm('all future NW periods',None)
out={'status':'PASS independent all-r>=50 complete two-contact capture','candidate_sha256':hashlib.sha256((D/'four_corner_capture_certificate.json').read_bytes()).hexdigest(),'initial_mass':43,'capture_time':'520r+13640','capture_pose':['-2r+2','2r+38','N'],'capture_mass':'60r+795','final_drift':[-2,2],'stages':stages,'seconds':time.monotonic()-started,'scope':'The exact unmodified43-cell prepared loop family only. The first finite NW segment is not misidentified as an infinite capture; the remote second contact is explicitly retained.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
