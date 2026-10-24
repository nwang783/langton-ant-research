"""Literal two-parameter family derivation and exact whole-board chronology."""
from pathlib import Path
import json,sys,time,hashlib
R=Path(__file__).resolve().parents[1];D=R/'causal_reduction/unit_scale';J=json.loads((D/'unequal_four_corner_loop_certificate.json').read_text());S0=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text());H=S0['word'];assert S0['heading']==3
sys.path.insert(0,str(R/'sources/kehao95-core/defect_synthesis/verification/presburger_defects'));from isl_exact import Context
ctx=Context(max_operations=200000000);started=time.monotonic()
def xy(z):return int(z.real),int(z.imag)
def xor(a,b):return a.subtract(b).union(b.subtract(a)).coalesce()
def S(c):return ctx.set('[r,s]->{[x,y]:r>=3 and s>=3 and ('+c+')}')
def I(c):return ctx.set('[r,s]->{[i]:r>=3 and s>=3 and ('+c+')}')
def aff(a):return f'({a[0]}*r+{a[1]}*s+{a[2]})'
def tr(w,h):
 z=0j;slots=[]
 for j,c in enumerate(w):slots.append((z,c,j));h*=(-1j if c=='R'else 1j);z+=h
 return slots,z,h
p=[0j]*3;h=1j;t=[0]*3;fam=[];caps=[];program=[]
for side in range(4):program += [('R',(0,0,1)),(H,(1,0,0)if side%2==0 else(0,1,0)),(H[:68 if side<3 else 60],(0,0,1))]
for w,count in program:
 slots,d,hh=tr(w,h)
 if count!=(0,0,1):assert hh==h
 if w=='R':caps.append((p[:],h))
 for z,c,j in slots:
  px=[int(v.real)for v in p];py=[int(v.imag)for v in p];px[2]+=int(z.real);py[2]+=int(z.imag)
  tt=t[:];tt[2]+=j
  fam.append({'x':px,'y':py,'d':xy(d),'time':tt,'step':len(w),'bound':count,'turn':c})
 p=[v+a*d for v,a in zip(p,count)];t=[v+a*len(w)for v,a in zip(t,count)];h=hh
assert(p,h,t)==([0j]*3,1j,[208,208,268])
K={complex(x,y)for x,y in((1,4),(1,5),(1,6),(2,0),(2,1),(2,2),(2,5),(3,0),(3,3),(3,4))}
seed=[[0j,0j,1-complex(x,y)]for x,y in S0['seed']]
for j,(p,hcap)in enumerate(caps[1:],1):seed.extend([p[0],p[1],p[2]+(1j**j)*q]for q in K)
assert len(seed)==43
initial=S('false')
def point(p):return S('x='+aff([int(z.real)for z in p])+' and y='+aff([int(z.imag)for z in p]))
for p in seed:
 q=point(p);assert initial.intersect(q).is_empty();initial=initial.union(q)
assert initial.is_equal(ctx.set(J['initial_relation']))
def dom(f,v='i'):return f'0<={v}<{aff(f["bound"])}'
def spatial(f,v='i'):return f'x={aff(f["x"])}+{f["d"][0]}*{v} and y={aff(f["y"])}+{f["d"][1]}*{v}'
for f in fam:f['support']=S(f'exists(i:{dom(f)} and {spatial(f)})')
relations=0
for j,f in enumerate(fam):
 ctx.reset_operations();selector=ctx.map(f'[r,s]->{{[x,y]->[i]:r>=3 and s>=3 and {dom(f)} and {spatial(f)}}}')
 black=selector.binary('intersect_domain',initial).range()
 for g in fam:
  if f['support'].intersect(g['support']).is_empty():continue
  equal=f'{aff(f["x"])}+{f["d"][0]}*i={aff(g["x"])}+{g["d"][0]}*u and {aff(f["y"])}+{f["d"][1]}*i={aff(g["y"])}+{g["d"][1]}*u'
  prior=I(f'{dom(f)} and exists(u:{dom(g,"u")} and {equal} and {aff(g["time"])}+{g["step"]}*u<{aff(f["time"])}+{f["step"]}*i)')
  if not prior.is_empty():relations+=1;black=xor(black,prior)
 assert(I(dom(f)).subtract(black)if f['turn']=='L'else black).is_empty(),j
 if j%100==0:print('independent two-parameter family',j,'relations',relations,flush=True)
after=initial
for f in fam:after=xor(after,f['support'])
assert after.is_equal(ctx.set(J['output_relation']))
keep=0
for p in seed:
 q=point(p)
 if q.subtract(after).is_empty():keep+=1
 else:assert q.intersect(after).is_empty()
assert keep==11 and S('x=0 and y=0').subtract(after).is_empty();assert len(fam)==684 and relations==1604
assert H.count('R')-H.count('L')==12 and sum(w.count('R')-w.count('L')for w,c in program if c==(0,0,1))==44
out={'status':'PASS independent all r,s>=3 closed-pose loop and whole field','candidate_sha256':hashlib.sha256((D/'unequal_four_corner_loop_certificate.json').read_bytes()).hexdigest(),'read_families':len(fam),'prior_relations':relations,'initial_mass':43,'final_mass':'24(r+s)+87','retained_input':11,'erased_input':32,'complete_XOR':'24(r+s)+108','duration':'208(r+s)+268','final_pose':[0,0,'N'],'next_turn':'L','seconds':time.monotonic()-started,'scope':'Exact finite excursion, not renewal or capture.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
