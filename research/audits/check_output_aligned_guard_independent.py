from pathlib import Path
import json,hashlib,sys
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'stateful_growth_application_2026-10-23'
ns={'__file__':str(SELF.parent/'check_carried_up4_mixed_shuttle_independent.py')};exec((SELF.parent/'check_carried_up4_mixed_shuttle_independent.py').read_text().split('seed=frame')[0],ns)
geometry=ns['geometry'];W=ns['W'][6:]+ns['W'][:6];T=ns['T'];KB=ns['KB'];E=ns['E'];H=ns['H'];S=ns['S'];dirs=ns['dirs']
sys.path.insert(0,str(R/'stateful_growth_quadratic_2026-10-23'));from quadratic_lap_validator import Context
ctx=Context(max_operations=10000000)
assert W=='RRLRRRRLLLLRLLLLRLRR';assert geometry(W,1)[:2]==(-2,0)
assert geometry(W,1)[2][-1]==(-3+0j,0,'R')
# Independent symbolic four-side frame. Coordinates affine in r,k,j.
p=[0j,0j,0j];h=1;hits=ctx.set('[r,k]->{[s,b,j,ph]:false}');frameevents=[]
for side in range(4):
 for b,(w,count) in enumerate(((T,(1,0,0)),('RL',(0,1,0)),('R',(0,0,1)))):
  drift,rot,reads=geometry(w,h);ar,ak,c=count
  for ph,(q,hh,ch) in enumerate(reads):
   coords=[p[0],p[1],p[2]+q]
   dom=f'r>=10 and k>=10 and s={side} and b={b} and ph={ph} and 0<=j<{ar}*r+{ak}*k+{c}'
   eq=[]
   for a,part in enumerate((lambda z:int(z.real),lambda z:int(z.imag))):eq.append(f'{part(coords[0])}*r+{part(coords[1])}*k+{part(drift)}*j+{part(coords[2])}={-1 if a==0 else 0}')
   hit=ctx.set('[r,k]->{[s,b,j,ph]:'+dom+' and '+' and '.join(eq)+'}')
   hits=hits.union(hit);frameevents.append((side,b,ph,hh,ch))
  for a,co in enumerate(count):p[a]+=co*drift
  h=(h+rot)%4
assert p==[0j]*3 and h==1
expected=ctx.set('[r,k]->{[s,b,j,ph]:r>=10 and k>=10 and s=3 and b=2 and j=0 and ph=0}')
assert hits.is_equal(expected);assert frameevents[-1]==(3,2,0,0,'R')
# Short-arm obstruction has a genuinely surviving preceding even W-output.
assert [(ph,z)for ph,(z,h,a)in enumerate(geometry(W,1)[2])if z.imag==0]==[(0,0j),(19,-3+0j)]
assert all(z!=2 for z,h,a in geometry(T,1)[2])
# Full motivated program: derive geometry from literal words, not Program families.
blocks=[(W,3,50)]+KB((3,51),(1,10))+[(S,3,50),(T,3,51),(E,0,1),(T,3,51),('RRRRLL',0,1),(H,1,1)]
p1=p0=0j;h=1;families={};length=[0,0];mass=[0,0]
for b,(w,a,c)in enumerate(blocks):
 drift,rot,reads=geometry(w,h)
 for ph,(q,hh,ch)in enumerate(reads):families[b,ph]=(p1,p0+q,drift,hh,ch,a,c)
 if rot:assert a==0 and c==1
 p1+=a*drift;p0+=c*drift;h=(h+rot*c)%4
 length[0]+=a*len(w);length[1]+=c*len(w);mass[0]+=a*(w.count('R')-w.count('L'));mass[1]+=c*(w.count('R')-w.count('L'))
assert h==1 and(p1/2,p0-p1/2)==(1+1j,1+5j)and length==[408,5344]and mass==[12,56]
g=families[0,19];f=families[12,0];assert g[3:5]==f[3:5]==(0,'R');assert (g[0]+3*g[2],g[1]+49*g[2])==f[:2]==(-6+0j,-101+0j)
# Literal all-initial-colors first-read inference, then copied physical board.
p=0j;h=1;hist={};seed=set();word=[];bad=None
for b,(w,a,c)in enumerate(blocks):
 for j in range(c):
  for ph,ch in enumerate(w):
   i=len(word)
   if p in hist and hist[p][1]==ch:bad=(i,b,j,ph,p,h,hist[p][0]);break
   if p not in hist and ch=='L':seed.add(p)
   hist[p]=(i,ch);word.append(ch);h=(h+(1 if ch=='R'else-1))%4;p+=dirs[h]
  if bad:break
 if bad:break
assert bad==(1899,12,0,0,-101+0j,0,999);assert len(seed)==450
board=set(seed);p=0j;h=1
for ch in word:
 assert(p in board)==(ch=='L');board.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=dirs[h]
assert (p,h,len(board))==(-101+0j,0,453)and p in board
note=D/'output_aligned_guard.md';author=json.loads((D/'output_aligned_guard.json').read_text())
assert author['candidate']['finite_prefix_control']['minimal_seed_mass']==450
out=dict(status='PASS all-parameter phase-six closing guard and independently replayed positive prefix',note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),all_parameter_domain='M>=1,r>=10,k>=10',frame_only_touch=str(hits.coalesce()),geometry={'A':[1,1],'B':[1,5],'length':length,'mass':mass},positive_prefix={'reads':1899,'seed_mass':450,'final_mass':453,'failure_cell':[-101,0],'previous_read':999},analytic='The last W6 read writes black at one cell west of the next entry. The entire first four-side frame touches that cell only at its final prescribed R. Initial colors, later cap state and passive layers cannot alter this consecutive-read R/R obstruction. The r<=M earlier conflict follows from disjoint odd/even output coordinates and T forward endpoint first reach.',scope='This exact prescribed W6-to-K join only; physical clearing operations and other caps are not excluded.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(out)
