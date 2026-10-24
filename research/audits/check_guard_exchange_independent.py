from pathlib import Path
import json,hashlib,sys
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'stateful_growth_application_2026-10-23';ref=json.loads((D/'guard_exchange.json').read_text());sample=json.loads((D/'guard_exchange_M50_r51.json').read_text());W='RRLRRRRLLLLRLLLLRLRR';T='LRRL';E=json.loads((R/'new_constructive_2026-10-23/two_layer_restored_bulk_shuttle.json').read_text())['stages'][1]['word'];dirs=(1j,1,-1j,-1)
sys.path.insert(0,str(R/'stateful_growth_quadratic_2026-10-23'));from quadratic_lap_validator import Context
ctx=Context(max_operations=100000000);domain='M>=1 and r>=10 and r>M'
def empty():return ctx.set('[M,r]->{[x,y]:false}')
def xor(a,b):return a.subtract(b).union(b.subtract(a)).coalesce()
def expr(v):return f'({v[0]}*M+{v[1]}*r+{v[2]})'
def part(v,a):return tuple(int(z.real if a==0 else z.imag)for z in v)
def image(f):
 con=domain+f' and exists(j:0<=j<{expr(f["count"])} and x={expr(part(f["p"],0))}+{int(f["d"].real)}*j and y={expr(part(f["p"],1))}+{int(f["d"].imag)}*j)'
 return ctx.set('[M,r]->{[x,y]:'+con+'}')
p=[0j,0j,0j];h=1;clock=[0,0,0];families=[]
for stage,(w,count)in enumerate([(W,(1,0,0)),(T,(0,1,0)),(E,(0,0,1)),(T,(0,1,0)),('RRRRLL',(0,0,1))]):
 pp=0j;hh=h;reads=[]
 for a in w:reads.append((pp,hh,a));hh=(hh+(1 if a=='R'else-1))%4;pp+=dirs[hh]
 if count!=(0,0,1):assert hh==h and pp!=0
 for ph,(z,hd,a)in enumerate(reads):
  f=dict(stage=stage,p=(p[0],p[1],p[2]+z),d=pp,count=count,time=(clock[0],clock[1],clock[2]+ph),dt=len(w),letter=a,heading=hd);f['set']=image(f);families.append(f)
 p=[p[k]+count[k]*pp for k in range(3)];clock=[clock[k]+count[k]*len(w)for k in range(3)];h=hh
assert p==[-2+0j,0j,0j]and h==1 and clock==[20,8,52]and len(families)==80
seed=ctx.set('[M,r]->{[x,y]:'+domain+' and ((y=-3 and -2M<=x<0) or (y=0 and (x=-2M or x=-1 or 1<=x<2r-2M)) or (y=-1 and (x=-1 or x=2r-2M or x=2r-2M+1)) or (x=0 and y=-2))}')
firstL=empty();pairs=0
for f in families:
 ctx.reset_operations();before=empty();current=seed.intersect(f['set'])
 for g in families:
  if g is f:continue
  eq=[domain,f'0<=j<{expr(f["count"])}',f'0<=k<{expr(g["count"])}']
  for a,name in enumerate(('x','y')):
   eq.extend([f'{name}={expr(part(f["p"],a))}+{int(f["d"].real if a==0 else f["d"].imag)}*j',f'{name}={expr(part(g["p"],a))}+{int(g["d"].real if a==0 else g["d"].imag)}*k'])
  eq.append(f'{expr(g["time"])}+{g["dt"]}*k<{expr(f["time"])}+{f["dt"]}*j')
  prior=ctx.set('[M,r]->{[x,y]:exists(j,k:'+' and '.join(eq)+')}');pairs+=1;before=before.union(prior);current=xor(current,prior)
 if f['letter']=='L':
  assert current.is_equal(f['set']);firstL=firstL.union(f['set'].subtract(before))
 else:assert current.is_empty()
assert firstL.is_equal(seed);before=seed;after=seed
for f in families:
 after=xor(after,f['set'])
 if f['stage']==0:before=xor(before,f['set'])
assert before.is_equal(ctx.set(ref['complete_before_shuttle_relation']))and after.is_equal(ctx.set(ref['complete_returned_relation']))
clears=[(-1,0,False),(0,-1,True),(1,-1,True)];adds=[(0,1,False),(0,2,False),(-1,2,False)]+[(x,y,True)for x,y in[(-1,-1),(2,-1),(3,0),(3,1),(0,1),(1,1),(-1,2),(0,2),(1,2),(2,2),(0,3),(1,3)]]
def finite(vs):return ctx.set('[M,r]->{[x,y]:'+domain+' and ('+' or '.join(f'(x=-2M+{2 if far else 0}r+{x} and y={y})'for x,y,far in vs)+')}')
C=finite(clears);A=finite(adds);assert C.intersect(A).is_empty()and before.intersect(C).is_equal(C)and before.intersect(A).is_empty();assert after.is_equal(before.subtract(C).union(A))
# One physical original-board replay and exact saved complete field.
word=W*50+T*51+E+T*51+'RRRRLL';assert word==sample['word'];black={complex(*q)for q in sample['seed']};initial=set(black);p=0j;h=1
for ch in word:assert(p in black)==(ch=='L');black.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=dirs[h]
assert(p,h,len(initial),len(black),len(word))==(-100+0j,1,107,119,1460);assert black=={complex(*q)for q in sample['returned']}
# Arbitrary preceding history cannot change the final local six-read ownership.
p=-1+1j;h=3;reads=[]
for ch in'RRRRLLLR':reads.append((p,h,ch));h=(h+(1 if ch=='R'else-1))%4;p+=dirs[h]
assert [x[0]for x in reads]==[-1+1j,-1+2j,2j,1j,-1+1j,-1,0j,1j];assert reads[3][2]==reads[7][2]=='R'
note=D/'guard_exchange.md';assert hashlib.sha256(note.read_bytes()).hexdigest()=='27d898092de97b28ae9bf9fbc722445b754429436abccd66d03a69603e7292de'
out=dict(status='PASS all-parameter original-board W6-to-J guard exchange and fixed-local-cap restart obstruction',note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),families=len(families),strict_prior_family_pairs=pairs,domain=domain,minimum_seed='2r+5',duration='20M+8r+52',complete_output='Before-J complete rod and four markers, minus three listed cells plus fifteen listed cells; all other physical bits unchanged.',sample={'reads':1460,'input':107,'output':119,'pose':[-100,0,1]},analytic='The exact prior-color test quantifies both copy indices directly and confirms all read colors on the entire two-parameter cone, including minimum first-L support. The last local RRRRLL writes the new near gate black; immediate LRRL requires the next read of that same cell R after only three off-cell reads. Changing arbitrary earlier remote behavior cannot repair that fixed-local-cap/immediate-T interface.',scope='A positive finite supplied guard-clearing operation with complete endpoint changes, not a renewable cap. Different near caps, entry poses or outbound words remain unclassified.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(pairs)
