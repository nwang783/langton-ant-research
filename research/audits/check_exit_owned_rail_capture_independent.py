from pathlib import Path
from collections import defaultdict
import json,hashlib,sys
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'stateful_growth_application_2026-10-23';a=json.loads((D/'exit_owned_rail_capture.json').read_text());src=json.loads((D/'guard_exchange_exit.json').read_text());C=a['C63'];F=a['C148'];H=a['H104'];std=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];dirs=(1j,1,-1j,-1);domain='M>=1 and r>=10 and r>M'
assert (C.count('R')-C.count('L'))-1+(F.count('R')-F.count('L'))==42
W6='RRLRRRRLLLLRLLLLRLRR';assert len(W6)==20 and W6[2]=='L' and W6[106%20]=='R'
assert len(C)==63 and len(F)==148 and H in{(std+std)[k:k+104]for k in range(104)}
sys.path.insert(0,str(R/'stateful_growth_quadratic_2026-10-23'));from quadratic_lap_validator import Context
ctx=Context(max_operations=100000000);B=ctx.set(src['complete_returned_relation'])
def xor(a,b):return a.subtract(b).union(b.subtract(a)).coalesce()
def point(p,remote=False):return ctx.set(f'[M,r]->{{[x,y]:{domain} and x=-2M+{2 if remote else 0}r+{int(p.real)} and y={int(p.imag)}}}')
def physical(w,p,h,remote=False):
 global B
 reads=[]
 for ch in w:
  cell=point(p,remote);got=B.intersect(cell);assert got.is_equal(cell)if ch=='L'else got.is_empty();reads.append((p,h,ch));B=xor(B,cell);h=(h+(1 if ch=='R'else-1))%4;p+=dirs[h]
 return p,h,reads
p,h,reads=physical(C,-4,3);assert(p,h)==(1,2);assert all(not(q.imag==0 and q.real>=1)for q,hd,ch in reads)
assert (min(q.real for q,hd,ch in reads),max(q.real for q,hd,ch in reads),min(q.imag for q,hd,ch in reads),max(q.imag for q,hd,ch in reads))==(-4,1,-4,1)
# This is a first physical contact with the same intact restored rod.
p,h,_=physical('L',p,h);assert(p,h)==(2,1)
rail=[]
for off,ch in[(0,'L'),(1j,'R'),(1+1j,'R'),(1,'L')]:
 q=ctx.set(f'[M,r]->{{[x,y]:{domain} and exists(j:0<=j<r-1 and x=-2M+2+2j+{int(off.real)} and y={int(off.imag)})}}');got=B.intersect(q);assert got.is_equal(q)if ch=='L'else got.is_empty();rail.append(q)
for i,q in enumerate(rail):
 assert all(q.intersect(v).is_empty()for v in rail[:i]);B=xor(B,q)
p,h,_=physical(F,0,1,True);assert(p,h)==(2-2j,1);assert B.is_equal(ctx.set(a['complete_capture_board']))
# Independent complete-history orbit certificate, not the author's phase-pair
# parity query. For each physical d=(2,2) orbit, order all eligible occurrences
# by descending copy-offset then phase, and test every finite eligibility fringe
# and its infinite ray against the complete pre-tail board.
slots=defaultdict(list);pos=p;hd=h
for i,ch in enumerate(H):
 x,y=int(pos.real),int(pos.imag);par=x%2;normal=y-x;rep=complex(par,par+normal);k=(x-par)//2;slots[par,normal].append((k,i,ch,rep));hd=(hd+(1 if ch=='R'else-1))%4;pos+=dirs[hd]
assert pos-p==2+2j and hd==h
checks=0;fringes=0
for key,sl in slots.items():
 lo=min(k for k,i,ch,r in sl);hi=max(k for k,i,ch,r in sl);rep=sl[0][3]
 for cut in range(lo,hi+1):
  eligible=sorted((s for s in sl if s[0]<=cut),key=lambda s:(-s[0],s[1]));letters=[s[2]for s in eligible];assert all(x!=y for x,y in zip(letters,letters[1:]));need=letters[0]=='L'
  # The complete full list applies to every N>=hi; earlier cuts are singleton.
  dom=f'{domain} and n>={cut}'if cut==hi else f'{domain} and n={cut}'
  amap=ctx.map(f'[M,r]->{{[n]->[x,y]:{dom} and x=-2M+2r+{int(rep.real)}+2n and y={int(rep.imag)}+2n}}')
  present=amap.reverse().binary('intersect_domain',B).range();allN=ctx.set('[M,r]->{[n]:'+dom+'}')
  assert present.is_equal(allN)if need else present.is_empty();checks+=1;fringes+=cut<hi
# Full copied original finite-board sample through tail entry and two periods.
sample=json.loads((D/'guard_exchange_exit_M50_r51.json').read_text());word=sample['word']+C+'L'+'LRRL'*50+F;black={complex(*q)for q in sample['seed']};pp=0j;hh=1
for i,ch in enumerate(word+H*2):
 if i==len(word):
  capture=set(black);fixed=ctx.set('[M,r]->{[x,y]:M=50 and r=51 and ('+' or '.join(f'(x={int(q.real)} and y={int(q.imag)})'for q in black)+')}');assert B.intersect_params(ctx.set('[M,r]->{[]:M=50 and r=51}')).is_equal(fixed)
 assert(pp in black)==(ch=='L');black.symmetric_difference_update({pp});hh=(hh+(1 if ch=='R'else-1))%4;pp+=dirs[hh]
assert len(word)==1892 and(pp,hh)==(8+2j,1)
out=dict(status='PASS all-parameter self-owned rod reuse and complete infinite standard104 capture',source_sha256=hashlib.sha256((D/'check_exit_owned_rail_capture.py').read_bytes()).hexdigest(),domain=domain,capture_time='20M+12r+280',capture_pose=['-2M+2r+2',-2,1],capture_mass='2r+61',restart_obstruction='No W6^6 substring after capture: 104-periodicity identifies indices 2 and 106, whose W6 letters differ.',tail={'period':104,'drift':[2,2],'physical_orbits':len(slots),'complete_field_tests':checks,'finite_eligibility_fringes':fringes},sample={'original_mass':len(sample['seed']),'capture_reads':len(word),'capture_mass':len(capture),'literal_tail_periods':2},scope='Every member of this explicit finite supplied family captures; no new supply, hidden reset or proxy-only field. No renewable nonstandard mechanism or arbitrary-input capture theorem.')
note=D/'exit_owned_rail_capture.md'
if note.exists():out['note_sha256']=hashlib.sha256(note.read_bytes()).hexdigest()
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(out)
