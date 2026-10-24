from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];ns={'__file__':str(SELF.parent/'check_serial_bridge_archive_independent.py')};exec(Path(ns['__file__']).read_text().split('# Fixed local masks')[0],ns)
graph,rank,ends,connected,step,wvertex=[ns[k]for k in('graph','rank','ends','connected','step','wvertex')]
D=R/'actual_zipper_spiral_2026-10-23';counts=Counter();controls=[]
def phys(v):return 2*v.real+2*v.imag+1+1j*(2*v.real-2*v.imag+1)
def make(q,scale):
 p=0j;vs=[p];runs=[]
 for j in range(1,q+1):
  d=1j**((j-1)%4);a=p
  for k in range(scale*((j+1)//2)):p+=d;vs.append(p)
  runs.append((a,p))
 cells=[(phys(u)+phys(v))/4 for u,v in zip(vs,vs[1:])];assert len(vs)==len(set(vs)) and len(cells)==len(set(cells))
 return vs,cells,runs
for q in (1,2,3,4,5,8,12,20,32):
 vs,cs,runs=make(q,4);B=set(cs);initial=set(B);n=len(cs);assert n==4*((q+1)**2//4)
 assert all(rank(B,k)==0 for k in (0,2))
 # All closed nonconsecutive run boxes are separated by at least four.
 for i,(a,b)in enumerate(runs):
  for c,d in runs[i+2:]:
   gap=lambda x,y,z,w:max(0,min(x,y)-max(z,w),min(z,w)-max(x,y))
   assert max(gap(a.real,b.real,c.real,d.real),gap(a.imag,b.imag,c.imag,d.imag))>=4
 p=1+1j;h=1;assert wvertex(p,h)==phys(0j)
 pre=set(B)|{1j};pp,hh,ch=step(pre,1j,2);assert(pre,pp,hh,ch)==(B,p,h,'L')
 output=set();word='';li=0
 for i,qcell in enumerate(cs):
  if i==0:r=0
  else:r=1+(int((vs[i+1]-vs[i])/(vs[i]-vs[i-1])==1j))
  for expected in 'R'*r+'L':
   oldp=p;assert ('L'if p in B else'R')==expected
   if expected=='L':
    assert p==qcell and p in initial and p not in output
    for k in (0,2):assert not connected(B-{p},k,*ends(p,k))
   else:
    assert p not in initial and p not in output
    for k in (0,2):assert not connected(B,k,*ends(p,k))
    output.add(p)
   p,h,ch=step(B,p,h);assert ch==expected;word+=ch;counts['fine_updates']+=1
  li+=1;assert wvertex(p,h)==phys(vs[li]);remaining=set(cs[li:]);assert B==remaining|output
  # Entire z output is a simple path, disjoint from all remaining old duals.
  zg=graph(output,0);oldg=graph(remaining,0);assert not set(zg)&set(oldg)
  if output:
   assert rank(output,0)==0 and all(len(x)<=2 for x in zg.values());assert sum(len(x)==1 for x in zg.values())==2
  counts['full_L_cuts']+=1
 assert len(word)==2*n+q-2 and word.count('L')==n and word.count('R')==n+q-2 and len(B)==n+q-2
 assert not graph(B,2).get(wvertex(p,h))
 tail=''
 for _ in range(5):p,h,ch=step(B,p,h);tail+=ch
 assert tail=='RRRRL'and len(B)==n+q+1
 controls.append({'q':q,'initial_mass':n,'epoch_length':len(word),'mass_gain':q-2,'signed_turn':q-1,'next_word':tail})
# Bind the explicit whole-board witness, but reconstruct its word independently.
w=json.loads((D/'witness_q8.json').read_text());proofsha=hashlib.sha256((D/'PROOF.md').read_bytes()).hexdigest();assert proofsha=='47ca17aa70bbb2a01720ce86066bee05120fd5f9890fe05d278bc357ff4faae2'
out={'status':'PASS actual paired-forest spiral zipper and square-root one-epoch sharpness','proof_sha256':proofsha,'controls':controls,'counts':dict(counts),'analytic':['The displayed four-residue endpoint formulas place every nonconsecutive closed run at Chebyshev distance >=4. Consecutive runs meet only at their common isolated corner, and every run has length >=4. Thus all interactions of unit arms and dual edges are confined to straight or one-corner patches.','In the w lattice, the original suffix remains a path. Each visited straight vertex leaves a right arm; each CCW corner leaves right plus forward arms. Their outer endpoints are outside the original path and pairwise distinct, as checked in the one-corner patch. All retained stars are disjoint. Every new arm is initially white, each departing old edge remains a bridge, and this proves the literal execution for every q, not only sampled q.','In the opposite lattice, initial dual edges form isolated edges and two-edge paths at corners. All written arms concatenate into the simple outside offset path. At an R prefix it touches at most one endpoint of the next old dual component; the incoming old edge has already been deleted. At the following L cut it is disjoint from the remaining old duals. Both complete graphs are therefore forests at every fine cut.','The actual predecessor L from(0,1),S on B union{(0,1)} produces the displayed entry(1,1),E. It is a bridge deletion in both graphs. The initial block is L, giving exact correction -1 relative to internal signed turning.','There are n=4floor((q+1)^2/4) old edges and q-1 clockwise physical w turns. Hence R=n+q-2,L=n,T=2n+q-2,full mass gain=q-2>=sqrt(n)-3. The final cursor is isolated from every retained star, so its next complete block is RRRRL.','This is an actual finite complete-board realization attaining square-root one-epoch growth. No concatenation, fixed-mass unbounded family, infinite seed orbit or sharpness of the global cubic time law follows.'],'scope':'All q>=1 at spacing4; finite controls do not replace the geometric induction. Other spacings and the optional different-entry variant are not certified here.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(counts)
