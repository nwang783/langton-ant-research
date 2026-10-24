"""Independent literal affine program, exact all-r read parity and full fields."""
from pathlib import Path
import json,sys,time,hashlib
R=Path(__file__).resolve().parents[1];D=R/'causal_reduction/unit_scale';J=json.loads((D/'four_corner_loop_certificate.json').read_text());S0=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text());H=S0['word'];assert S0['heading']==3
sys.path.insert(0,str(R/'sources/kehao95-core/defect_synthesis/verification/presburger_defects'));from isl_exact import Context
ctx=Context(max_operations=200000000);started=time.monotonic()
def xy(z):return int(z.real),int(z.imag)
def xor(a,b):return a.subtract(b).union(b.subtract(a)).coalesce()
def S(c):return ctx.set('[r]->{[x,y]:r>=3 and ('+c+')}')
def I(c):return ctx.set('[r]->{[i]:r>=3 and ('+c+')}')
def tr(w,h):
 z=0j;slots=[]
 for j,c in enumerate(w):slots.append((z,c,j));h*=(-1j if c=='R'else 1j);z+=h
 return slots,z,h
# Derive all family poses and absolute times from the literal program only.
pA=pB=0j;h=1j;tA=tB=0;fam=[];caps=[]
program=[]
for side in range(4):program += [('R',0,1),(H,1,0),(H[:68 if side<3 else 60],0,1)]
for w,a,b in program:
 slots,d,hh=tr(w,h)
 if (a,b)!=(0,1):assert hh==h
 if w=='R':caps.append((pA,pB,h))
 for z,c,j in slots:
  ax,ay=xy(pA);bx,by=xy(pB+z);dx,dy=xy(d)
  fam.append({'xy':(ax,bx,dx,ay,by,dy),'time':(tA,tB+j,len(w)),'bound':(a,b),'turn':c})
 pA+=a*d;pB+=b*d;tA+=a*len(w);tB+=b*len(w);h=hh
assert(pA,pB,h,tA,tB)==(0j,0j,1j,416,268)
K={complex(x,y)for x,y in((1,4),(1,5),(1,6),(2,0),(2,1),(2,2),(2,5),(3,0),(3,3),(3,4))}
seed=[(0j,1-complex(x,y))for x,y in S0['seed']]
for j,(a,b,hcap)in enumerate(caps[1:],1):seed.extend((a,b+(1j**j)*q)for q in K)
assert len(seed)==43
initial=S('false')
for a,b in seed:
 ax,ay=xy(a);bx,by=xy(b);q=S(f'x={ax}*r+{bx} and y={ay}*r+{by}')
 assert initial.intersect(q).is_empty();initial=initial.union(q)
assert initial.is_equal(ctx.set(J['initial_relation']))
def dom(f,var='i'):
 a,b=f['bound'];return f'0<={var}<{a}*r+{b}'
def spatial(f,var='i'):
 ax,bx,dx,ay,by,dy=f['xy'];return f'x={ax}*r+{bx}+{dx}*{var} and y={ay}*r+{by}+{dy}*{var}'
for f in fam:f['support']=S(f'exists(i:{dom(f)} and {spatial(f)})')
relations=0
for j,f in enumerate(fam):
 ctx.reset_operations();ax,bx,dx,ay,by,dy=f['xy'];ta,tb,tl=f['time']
 selector=ctx.map(f'[r]->{{[x,y]->[i]:r>=3 and {dom(f)} and {spatial(f)}}}')
 black=selector.binary('intersect_domain',initial).range()
 for g in fam:
  if f['support'].intersect(g['support']).is_empty():continue
  gx,gb,gd,gy,ge,gf=g['xy'];ua,ub,ul=g['time']
  prior=I(f'{dom(f)} and exists(u:{dom(g,"u")} and {ax}*r+{bx}+{dx}*i={gx}*r+{gb}+{gd}*u and {ay}*r+{by}+{dy}*i={gy}*r+{ge}+{gf}*u and {ua}*r+{ub}+{ul}*u<{ta}*r+{tb}+{tl}*i)')
  if not prior.is_empty():relations+=1;black=xor(black,prior)
 assert(I(dom(f)).subtract(black)if f['turn']=='L'else black).is_empty(),j
 if j%100==0:print('independent family',j,'relations',relations,flush=True)
after=initial
for f in fam:after=xor(after,f['support'])
assert after.is_equal(ctx.set(J['output_relation']))
keep=0
for a,b in seed:
 ax,ay=xy(a);bx,by=xy(b);q=S(f'x={ax}*r+{bx} and y={ay}*r+{by}')
 if q.subtract(after).is_empty():keep+=1
 else:assert q.intersect(after).is_empty()
assert keep==11 and S('x=0 and y=0').subtract(after).is_empty()
assert len(fam)==684 and relations==1604
assert H.count('R')-H.count('L')==12
assert sum(w.count('R')-w.count('L')for w,a,b in program if a==0)==44
out={'status':'PASS independent all-r>=3 closed-pose loop, every literal read and complete output','candidate_sha256':hashlib.sha256((D/'four_corner_loop_certificate.json').read_bytes()).hexdigest(),'read_families':len(fam),'prior_relations':relations,'initial_mass':43,'final_mass':'48r+87','retained_initial':keep,'erased_initial':43-keep,'complete_XOR':'48r+108','duration':'416r+268','final_pose':[0,0,'N'],'next_actual_turn':'L','seconds':time.monotonic()-started,'scope':'One finite prepared excursion per seed, no renewal or finite-seed infinite loop.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
