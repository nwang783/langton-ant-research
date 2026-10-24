"""Separate compass-combination inventories and radix-digit conflict replay."""
from pathlib import Path
from itertools import combinations
import json,hashlib
P=Path(__file__).resolve().parents[1];comp=[1j,1,-1j,-1]
def conflict(letters,heading):
 p=0j;colors={};last={}
 for t,d in enumerate(letters):
  z=d/heading;assert z in(1j,-1j);black=z==1j
  if p in colors and colors[p]!=black:return {'status':'CONFLICT','read':t,'previous':last[p],'cell':[int(p.real),int(p.imag)],'turn':3 if black else 1}
  colors[p]=not black;last[p]=t;heading=d;p+=d
 return None
def inventory(k,b,axis):
 target=3+2j if axis==1 else 2+b*1j;axes=[axis*(1j if t%2 else 1)for t in range(k)]
 H=[t for t,z in enumerate(axes)if z.real];V=[t for t,z in enumerate(axes)if z.imag]
 hp=(len(H)+int(target.real))//2;vp=(len(V)+int(target.imag))//2;raw=0;accepted={};rawalien=[]
 for hs in combinations(H,hp):
  for vs in combinations(V,vp):
   pos=set(hs)|set(vs);w=tuple((1 if z.real else 1j)*(1 if t in pos else -1)for t,z in enumerate(axes));assert sum(w)==target;raw+=1
   x=y=0;hits=[]
   for t,d in enumerate(w[:-1],1):
    x+=int(d.real);y+=int(d.imag);u=b*x-2*y;v=-2*x+3*y;det=3*b-4
    if u%det==v%det==0 and complex(x,y)not in(0,target):hits.append([t,x,y,u//det,v//det])
   headings=[h for h in (axis*1j,axis*-1j)if conflict(w,h)is None]
   if hits:rawalien.append((w,hits))
   if headings:accepted[w]={'headings':sorted(comp.index(h)for h in headings),'alien_hits':hits}
 return raw,accepted,rawalien
results=[]
for k,b in [(17,9),(21,11)]:
 src=P/f'causal_reduction/matrix_candidates/first_alien_mixing_k{k}';J=json.loads((src/'inventory.json').read_text());R=json.loads((src/'records.json').read_text());saved=json.loads((src/'result.json').read_text());allsets=[];raws=[];aliens=[]
 for axis,key in [(1,'E'),(1j,'N')]:
  raw,own,rawalien=inventory(k,b,axis);assert raw==J['raw'][len(raws)]
  expected={tuple(comp[d]for d in row['word']):{a:row[a]for a in['headings','alien_hits']}for row in J[key]};assert own==expected
  raws.append(raw);allsets.append(own);aliens.append(sum(bool(v['alien_hits'])for v in own.values()))
  if k==17 and axis==1:
   frozen=json.loads((src/'raw_alien_conflicts.json').read_text());byword={tuple(comp[int(d)]for d in row['word']):row for row in frozen};assert set(byword)=={w for w,hits in rawalien}and len(rawalien)==12
   for w,hits in rawalien:
    row=byword[w];assert row['hits']==[h[:3]for h in hits]
    assert row['conflicts']==[conflict(w,h)for h in[1j,-1j]]
 assert list(map(len,allsets))==J['legal'] and aliens==J['alien_images']
 E=[tuple(comp[d]for d in v['word'])for v in J['E']];N=[tuple(comp[d]for d in v['word'])for v in J['N']]
 expected={(r['east'],r['north'],r['root'],r['heading']):r for r in R};assert len(expected)==len(R)
 count=0;latest=None
 for ie,e in enumerate(E):
  for jn,n in enumerate(N):
   if not(allsets[0][e]['alien_hits']or allsets[1][n]['alien_hits']):continue
   phi={1:e,1j:n,-1:tuple(-d for d in e),-1j:tuple(-d for d in n)}
   for root in[1,1j]:
    p=phi[root][0];period=1
    while p!=root:p=phi[p][0];period+=1;assert period<=2
    for h in[root*1j,root*-1j]:
     def stream():
      for t in range(k**4):
       d=root
       for place in[k**3,k*k,k,1]:d=phi[d][t//place%k]
       yield d
     r=conflict(stream(),h);assert r is not None
     key=(ie,jn,comp.index(root),comp.index(h));record=expected[key]
     assert record==dict(r,east=ie,north=jn,root=comp.index(root),heading=comp.index(h),period=period)
     count+=1;latest=r['read']if latest is None else max(latest,r['read'])
 assert count==saved['cases']and latest==saved['latest_conflict']
 assert not saved['survivors']and hashlib.sha256((src/'records.json').read_bytes()).hexdigest()==saved['records_sha256']
 results.append({'radix':k,'matrix':J['matrix'],'raw_images':raws,'legal_images':list(map(len,allsets)),'alien_images':aliens,'vertex_only_pairs':(len(E)-aliens[0])*(len(N)-aliens[1]),'residual_cases':count,'latest_conflict':latest,'files':{f:hashlib.sha256((src/f).read_bytes()).hexdigest()for f in['inventory.json','records.json','result.json']}})
out={'status':'PASS finite-support half-turn families via signed GN plus complete independent residual replay','results':results,'scope':'Only residual cases are rejected on arbitrary initial colorings; GN uses finite support.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
