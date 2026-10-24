from pathlib import Path
from fractions import Fraction
import json,hashlib,sys
R=Path(__file__).resolve().parents[1];B=R/'stateful_growth_application_2026-10-23';P=R/'new_constructive_2026-10-23'
report=json.loads((B/'carried_up4_mixed_shuttle.json').read_text())
assert hashlib.sha256((B/'carried_up4_mixed_shuttle.md').read_bytes()).hexdigest()=='d9ae4b4ee2241155bbe128d5be85ff848ce0730cf91484498633829818cf8ebc'
assert hashlib.sha256((B/'check_carried_up4_mixed_shuttle.py').read_bytes()).hexdigest()=='3652cbcf0395ac12927fc61479072511301e77f4dd899a8c42f49c56c4c31c50'
for f,h in report['bindings'].items():assert hashlib.sha256((P/f).read_bytes()).hexdigest()==h
carrier=json.loads((P/'two_layer_carried_endpoint.json').read_text());shuttle=json.loads((P/'two_layer_restored_bulk_shuttle.json').read_text());H=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
T='LRRL';W='LLRLRRRRLRRRRLLLLRLL';S='RLLR';E=shuttle['stages'][1]['word'];dirs=(1j,1,-1j,-1)
def geometry(w,h):
 p=0j;reads=[];old=h
 for a in w:
  reads.append((p,h,a));h=(h+(1 if a=='R'else-1))%4;p+=dirs[h]
 return p,(h-old)%4,reads
assert len(E)==46
assert geometry('RRLL',1)[:2]==(-2j,0)
assert [p+4j for p,h,a in geometry('RRLL',1)[2]]==[4j,3j,-1+3j,-1+2j]
def KB(r=(1,10),k=(1,10)):
 b=[]
 for j in range(4):b.extend([(T,*r),('RL',*k),('R',0,1)])
 for row in carrier['stages']:
  ar,ak,c=row['count'];b.append((row['word'],ar*r[0]+ak*k[0],ar*r[1]+ak*k[1]+c))
 return b+[(T,*r),(E,0,1),(T,*r),('RR',0,1)]
def JB():return[(T,1,10),(E,0,1),(T,1,10),('RRRRLL',0,1)]
# Independent literal four-side input, no imported geometry generator.
def frame(r,k,j=0):
 k+=j;v=complex(2*r+k,-k-1);p=0j;B=set();local={complex(x,0)for x in range(2*r)}|{complex(2*r+a,-a-1)for a in range(k)}
 for h in range(4):B|={p+q*(-1j)**h+j*1j for q in local};p+=v*(-1j)**h
 assert p==0;return B
seed=frame(10,10)|frame(10,10,2);kw=''.join(w*b for w,a,b in KB((0,10),(0,10)));assert len(seed)==248 and len(kw)==956
assert kw==(P/'two_layer_gap_frame_r10_k10.word.txt').read_text()[:956]
black=set(seed);p=0j;h=1
for a in kw:
 assert (p in black)==(a=='L');black.symmetric_difference_update({p});h=(h+(1 if a=='R'else-1))%4;p+=dirs[h]
assert(p,h,len(black))==(4j,1,280)
# Exact relation algebra uses the generic libisl context only, not Program geometry.
sys.path.insert(0,str(R/'stateful_growth_quadratic_2026-10-23'))
from quadratic_lap_validator import Context
ctx=Context(max_operations=10000000);X=ctx.set('[r,k]->{[x,y]:r>=10 and k>=10 and ((x=0 and y=4)or(x=0 and y=3)or(x=-1 and y=3)or(x=-1 and y=2))}')
F=ctx.set(shuttle['complete_returned_relation']);expected=F.subtract(X).union(X.subtract(F)).coalesce()
assert expected.is_equal(ctx.set(report['cap']['complete_returned_relation']))
concrete=ctx.set('[r,k]->{[x,y]:r=10 and k=10 and ('+'or'.join(f'(x={int(z.real)} and y={int(z.imag)})'for z in black)+')}')
assert expected.intersect_params(ctx.set('[r,k]->{[]:r=10 and k=10}')).is_equal(concrete)
results=[]
for powered in (False,True):
 blocks=[(W,3,50)]+KB()+[(S,3,50)]+JB()+([(H,1,1)]if powered else[])
 slope=0j;constant=0j;h=1;events={};ma=mb=la=lb=0
 for b,(w,a,c)in enumerate(blocks):
  drift,rot,reads=geometry(w,h)
  if a:assert rot==0
  for phase,(z,hh,ch)in enumerate(reads):events[b,phase]=(slope,constant+z,drift,hh,ch)
  if not rot:slope+=a*drift;constant+=c*drift
  else:
   assert a==0
   for _ in range(c):d,rr,_=geometry(w,h);constant+=d;h=(h+rr)%4
  ma+=a*(w.count('R')-w.count('L'));mb+=c*(w.count('R')-w.count('L'));la+=a*len(w);lb+=c*len(w)
 assert h==1;AA=slope/2;BB=constant-AA
 gs,gc,gd,gh,ga=events[0,17];fs,fc,fd,fh,fa=events[1,1]
 assert gh==2 and fh==0 and ga==fa=='R'
 ns=gs+3*gd;nc=gc+49*gd;assert(ns,nc)==(fs,fc)
 offsets=[]
 for b,ph in ((0,18),(0,19),(1,0)):
  s,c,d,_,_=events[b,ph]
  if b==0:s+=3*d;c+=49*d
  assert s==ns;offsets.append(c-nc)
 assert offsets==[-1,-1-1j,-1j]
 assert (AA,BB,la,lb,ma,mb)==((1+1j,1+5j,264,2392,12,56)if powered else(0j,4j,160,2288,0,44))
 results.append(dict(powered=powered,A=[int(AA.real),int(AA.imag)],B=[int(BB.real),int(BB.imag)],lap_length=[la,lb],lap_mass=[ma,mb],shared_linear=[int(ns.real),int(ns.imag)],shared_constant=[int(nc.real),int(nc.imag)]))
# Completely general W^M / K join: last W, then first2T reads only.
p,h,reads=geometry(W,1);assert p==-2 and h==0
assert reads[17]==(-2+1j,2,'R')
assert [x[0]for x in reads[18:]]==[-3+1j,-3]
assert geometry(T,1)[2][:2]==[(0j,1,'L'),(1j,0,'R')]
out=dict(status='PASS positive full-field up4 prefix and all-parameter R/R W-to-K port exclusion',note_sha256=hashlib.sha256((B/'carried_up4_mixed_shuttle.md').read_bytes()).hexdigest(),positive_contract={'duration':'64r+16k+156','mass_gain':32,'all_parameter_basis':'Actual prefix of the already signed complete-field P-plus-whole-shuttle contract, undo final RRLL only.','sample_reads':956,'sample_input_mass':248,'sample_output_mass':280},programs=results,scope='One actual positive prepared growing cap, but this prescribed W20-to-K interface is impossible on ANY field by consecutive same-cell R/R. No other connector, phase, mechanism or infinite-seed theorem is excluded.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(results)
