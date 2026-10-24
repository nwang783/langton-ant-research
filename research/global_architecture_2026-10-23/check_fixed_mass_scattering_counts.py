#!/usr/bin/env python3
"""Defect counts from signed turn templates, using two independent detectors."""
import hashlib,json
from pathlib import Path
ROOT=Path('/workspace/shared/langton')
OUT=Path(__file__).resolve().parent
P=ROOT/'causal_reduction/unit_scale'
H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
C=json.loads((P/'four_corner_capture_word.json').read_text())['word']
DD=json.loads((P/'four_corner_capture_word2.json').read_text())['word']
F=json.loads((P/'unequal_four_corner_loop_certificate.json').read_text())['seed_families_ar_as_bx_cr_cs_by']
D=((0,1),(1,0),(0,-1),(-1,0));G={(0,-1),(1,1),(1,3),(2,2)}
allowed={(H*2)[i:i+10] for i in range(104)}
assert len(allowed)==84

def rot(p,n):
 x,y=p
 for _ in range(n%4):x,y=y,-x
 return x,y

def step(B,p,h):
 a='L' if p in B else 'R'
 h=(h+(-1 if a=='L' else 1))%4
 B.symmetric_difference_update({p});dx,dy=D[h]
 return (p[0]+dx,p[1]+dy),h,a

def trace(B,p,h,n):
 B=set(B);w=[]
 for _ in range(n):p,h,a=step(B,p,h);w.append(a)
 return B,p,h,''.join(w)

def history(B,p,h,n=10):
 B=set(B);w=[]
 for _ in range(n):
  dx,dy=D[h];p=(p[0]-dx,p[1]-dy);post=p in B
  h=(h+(-1 if post else 1))%4
  B.symmetric_difference_update({p});w.append('R' if post else 'L')
 return ''.join(w[::-1])

def direct_count(hist,w):
 a=hist+w
 return sum(a[i-10:i] not in allowed and a[i-9:i+1] not in allowed for i in range(10,len(a)))

def bits(s):
 x=0
 for a in s:x=(x<<1)|(a=='L')
 return x
AL={bits(s) for s in allowed}

def streaming_count(hist,w):
 # State is the last ten packed turns, not a string-window implementation.
 state=bits(hist);prior_bad=state not in AL;count=0
 for a in w:
  state=((state<<1)|(a=='L'))&1023
  bad=state not in AL
  count+=prior_bad and bad
  prior_bad=bad
 return count

def both(hist,w):
 a=direct_count(hist,w);b=streaming_count(hist,w);assert a==b;return a

# All moving43-cell seed points miss the inverse-history read neighborhood
# for every r,s>=50: one coordinate has a single coefficient sign and its
# extremum at(50,50) already lies outside[-12,12].
fixed=[];separations=[]
for row in F:
 ar,ass,bx,cr,cs,by=row
 if ar==ass==cr==cs==0:fixed.append((bx,by));continue
 found=[]
 for name,a,b,c in (('x',ar,ass,bx),('y',cr,cs,by)):
  v=50*(a+b)+c
  if a>=0 and b>=0 and v>12:found.append([name,'lower',v])
  if a<=0 and b<=0 and v< -12:found.append([name,'upper',v])
 assert found
 separations.append({'family':row,'separating_coordinate':found[0]})
h43=history(set(fixed),(0,0),0)
assert h43=='RLLLLRLLLL'

def loop_word(r,s):
 return 'R'+H*r+H[:68]+'R'+H*s+H[:68]+'R'+H*r+H[:68]+'R'+H*s+H[:60]

def full43(r,s):return loop_word(r,s)+C+H*(s-10)+DD+H[:10]
compressed43=loop_word(1,1)+C+H+DD+H[:10]
k43=both(h43,compressed43)
assert k43==5963
controls43=[]
for r,s in ((50,50),(50,51),(51,50),(50,100),(100,50),(51,70),(200,53),(53,200)):
 B={(ar*r+ass*s+bx,cr*r+cs*s+by) for ar,ass,bx,cr,cs,by in F}
 assert len(B)==43 and history(B,(0,0),0)==h43
 assert both(h43,full43(r,s))==k43
 controls43.append([r,s])

# Retained20-cell circuit. Reconstruct the fixed774-turn recovery from the
# first certified parameter using a fresh literal simulator, then compare
# independent larger complete physical runs to its certified template.
_,_,_,A=trace(G,(0,0),1,182)
assert len(A)==182

def seed20(n):
 poses=[((0,0),1),((n-1,n),0),((-n,3*n-4),3),((-5*n+5,-n),2),((-3*n,-3*n+8),1)]
 B=set()
 for p,h in poses:
  gg={(p[0]+q[0],p[1]+q[1]) for q in (rot(z,h-1) for z in G)}
  assert not B&gg;B|=gg
 return B

def words20(k,compress=False):
 ns=[k-4,2*k-5,4*k-6,2*k-7,3*k-4];ph=[61,71,61,71,14]
 assert min(ns)>=1
 return ''.join(A+H*(1 if compress else n)+H[:a] for n,a in zip(ns,ph))

b20=seed20(20);e20=624*20-1516
_,_,_,run20=trace(b20,(0,0),1,e20+774+10)
assert run20[:e20]==words20(10)
R=run20[e20:e20+774]
TAIL=H[103:]+H[:103]
assert run20[e20+774:]==TAIL[:10]
h20=history(G,(0,0),1)
assert history(b20,(0,0),1)==h20
compressed20=words20(10,True)+R+TAIL[:10]
k20=both(h20,compressed20)
controls20=[]
for n in (20,22,24,30,50,100,202):
 B=seed20(n);e=624*n-1516
 assert history(B,(0,0),1)==h20
 _,_,_,run=trace(B,(0,0),1,e+774+10)
 assert run==words20(n//2)+R+TAIL[:10]
 assert both(h20,run)==k20
 controls20.append(n)

# Generic cyclic-standard pumping test in arbitrary fixed contexts and phases.
# The analytic proof treats arbitrary contexts; controls exercise all104 phases.
pumpcases=0
left='LLLRLRRLLLR';right='RLLLRLRRRLLL'
for a in range(104):
 U=H[a:]+H[:a]
 for n in (1,2,3,7):
  assert both(h43,left+U*n+right)==both(h43,left+U+right)
  pumpcases+=1

report={
 'status':'PASS exact finite-word counts and independent literal controls',
 'scope':'All-parameter count constancy follows the written standard-power compression lemma and imported signed execution templates, not parameter samples.',
 'standard_factor_count':84,'generic_phase_power_controls':pumpcases,
 'forty_three_cell_family':{'domain':'r,s>=50','true_inverse_history':h43,'fixed_seed_cells':len(fixed),'separated_moving_seed_cells':len(separations),'separations':separations,'compressed_word_length_including_tail10':len(compressed43),'total_future_K':k43,'capture_time':'208*r+312*s+13640','parameter_controls':controls43},
 'twenty_cell_family':{'domain':'even n>=20','true_inverse_history':h20,'recovery_length':len(R),'recovery_sha256':hashlib.sha256(R.encode()).hexdigest(),'compressed_word_length_including_tail10':len(compressed20),'total_future_K':k20,'capture_time':'624*n-742','parameter_controls':controls20,'source_execution_status':'Retained all-parameter circuit theorem; fresh controls reconstruct words but do not re-audit its all-parameter geometry.'},
 'source_sha256':{str(q.relative_to(ROOT)):hashlib.sha256(q.read_bytes()).hexdigest() for q in [P/'unequal_four_corner_loop_certificate.json',P/'unequal_four_corner_capture_certificate.json',P/'four_corner_capture_word.json',P/'four_corner_capture_word2.json',ROOT/'sources/kehao95-core/memory_feedback/proof/scalable-feedback-circuit.md']}
}
(OUT/'check_fixed_mass_scattering_counts.json').write_text(json.dumps(report,indent=2)+'\n')
(OUT/'feedback20_recovery_word.json').write_text(json.dumps({'word':R,'length':774,'source':'fresh literal n20 reconstruction; all-parameter constancy imported from retained circuit theorem'},indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='source_sha256'},indent=2))
