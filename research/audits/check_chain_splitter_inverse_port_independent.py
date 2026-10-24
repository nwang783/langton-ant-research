from pathlib import Path
from collections import Counter
import hashlib,json
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'reframe_finite_seed_2026-10-24';p=SELF.with_name('check_cycle_birth_finite_fuel_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('cells=')[0],ns)
ends,component,step,wvertex,graph=[ns[x]for x in('ends','component','step','wvertex','graph')]
def xy(p):return int(p.real),int(p.imag)
H={-1j,1-1j,1+0j};records=[]
for n in range(1,65):
 Q={complex(-i,i)for i in range(1,n+1)};B=set(Q);p=0j;h=0;wm=[];trace=[];word='RRRRL'+'RL'*n
 assert not component(B,0,wvertex(p,h))[1]
 for t in range(len(word)+1):
  _,C=component(B,0,wvertex(p,h));wm.append(len(C));assert(int(p.real+p.imag)+h)%2==0
  if t>=5 and (t-5)%2==0:
   j=(t-5)//2;tail={complex(-i,i)for i in range(j+1,n+1)};out={complex(-i,i-1)for i in range(1,j+1)}
   assert B==H|tail|out and C==tail and(p,h)==(complex(-j-1,j),3)
  if n<=3:trace.append([t,xy(p),h,len(C),sorted(map(xy,B))])
  if t<len(word):p,h,ch=step(B,p,h);assert ch==word[t]
 assert max(wm)==n+4;output=set(B);assert component(B,0,1-1j)[1]==H
 for q in B-H:assert component(B,0,ends(q,0)[0])[1]=={q}
 # The opposite graph is one exact chain, with all degree2 except endpoints.
 g=graph(B,2);ext=sorted((v for v,a in g.items()if len(a)==1),key=xy)
 assert set(ext)=={complex(-2*n-1,2*n-1),1+1j}and all(len(a)in(1,2)for a in g.values())
 p-=1j*(-1j)**h;h=(h+2)%4;assert(p,h)==(complex(-n,n),1)and component(B,2,wvertex(p,h))[1]==B
 assert(int(p.real+p.imag)+h)%2==1
 reverse=''
 for _ in word:p,h,ch=step(B,p,h);reverse+=ch
 assert B==Q and(p,h)==(-1j,2)
 records.append({'n':n,'maximum_active':max(wm),'inverse_word':reverse,'full_trace':trace if n<=3 else None})
# Algebraic endpoint formulas determine all integer index coincidences.
for i in range(1,8):
 p=complex(-i,i-1);q=complex(-i,i)
 assert set(ends(p,0))=={complex(-2*i-1,2*i-3),complex(-2*i+1,2*i-1)}
 assert set(ends(q,0))=={complex(-2*i-1,2*i+1),complex(-2*i+1,2*i-1)}
 assert set(ends(p,2))=={complex(-2*i-1,2*i-1),complex(-2*i+1,2*i-3)}
# J conjugacy checked symbolically on the two possible read bits, all headings.
for h in range(4):
 for black in[False,True]:
  p=2+3j;B={p}if black else set();pn,hn,ch=step(B,p,h)
  jp=pn-1j*(-1j)**hn;jh=(hn+2)%4
  jp,jh,_=step(B,jp,jh);backp=jp-1j*(-1j)**jh;backh=(jh+2)%4
  assert(backp,backh)==(p,h)and B==({p}if black else set())
mf=json.loads((D/'splitter_manifest.json').read_text())
for f,h in mf.items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
out={'status':'PASS all-n one-shot chain splitter and exact inverse-port sector obstruction','dependencies':mf,'independent_controls':records,'analytic':['Q_i fixed-w endpoints are(-2i-1,2i+1),(-2i+1,2i-1), making one straight n-edge path disjoint from initialw. FirstR imports it; firstfourR create4arms, giving peakn+4. FirstL removes origin and detaches exact3starH.','Afterj RL pairs the displayed complete field H+P_1..j+Q_j+1..n and head(-j-1,j),W hold. The next R addsP_j+1 and next L removesQ_j+1. P_i endpoints are(-2i-1,2i-3),(-2i+1,2i-1); solving these affine equalities shows differentP_i vertex-disjoint, and P_i can meet a Q_k only for k=i or i-1, both already removed after that pair. H has no such vertex coincidence. This proves complete isolated singleton outputs for alln, not only the64 controls.','In the opposite graph P_i endpoints are(-2i-1,2i-1),(-2i+1,2i-3), so consecutive outputs form a chain attached to the3-edge H path at(-1,-1), ending at(-2n-1,2n-1). Alln+3 output edges are one active path at the inverse entry, not dispersed modules in that sector.','The retained involution J(p,h,B)=(p-DIR(h),h+2,B) is directly checked on both read bits and all headings, with JTJ=T^-1. Its inverse entry is(-n,n,E), opposite invariant epsilon from the forward run. Since every actual update changes both position parity and heading parity, epsilon is conserved; no arbitrary routing continuation reaches that exact inverse pose on those coordinates. Translation or rotation of another gadget changes the required field and does not supply a linked construction.'],'scope':'Exact complete finite input n>=1, one-shot RRRRL(RL)^n splitter. n2 shows singleton component fuel can increase at cap6. No all-cap rank obstruction, reusable compiler, recurrence or noncapture example.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
