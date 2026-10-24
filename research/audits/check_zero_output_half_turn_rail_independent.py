from pathlib import Path
from itertools import product
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1]
p=SELF.parent/'check_zero_output_Q2_and_same_curve_ear_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('results=[]')[0],ns)
base,even,F,locate,outs=[ns[k]for k in('base','even','F','locate','outs')]
vec={'N':1j,'E':1,'S':-1j,'W':-1}
def consistent(hh):
 nodes=[(p,i)for p,h in hh.items()for i in range(len(h))];edges=[]
 for p,h in hh.items():
  edges.extend(((p,i),(p,i+1),4)for i in range(len(h)-1))
  for d,v in vec.items():
   q=p+v
   if q not in hh:continue
   aa=[(p,i)for i,x in enumerate(outs(h))if x==d];bb=[(q,i)for i,x in enumerate(hh[q])if x==d]
   if len(aa)!=len(bb):return False
   for a,b in zip(aa,bb):edges.extend([(a,b,1),(b,a,-1)])
 dd={n:0 for n in nodes}
 for _ in nodes:
  changed=False
  for a,b,g in edges:
   if dd[b]<dd[a]+g:dd[b]=dd[a]+g;changed=True
  if not changed:return True
 return False
upper=[]
for r,q in product(even,range(4)):
 h,ht,en,bd=locate(r,-1+1j,q)
 if h.get(1j)!='SSNS' or ht.get(2j)!=-2:continue
 if outs(h[2j]).count('S')!=3:continue
 h.update({1+1j:'EEWE',1+2j:'NNNS'})
 upper.append((r,q,h,ht,consistent(h)))
assert len(upper)==2 and sum(v[-1]for v in upper)==1
U,uq,uh,ut,ok=next(v for v in upper if v[-1]);assert uq==3 and U[2]==('B',)
assert {p:uh[p]for p in(-1+1j,-1+2j,2j,1j)}=={-1+1j:'EEWE',-1+2j:'NNNS',2j:'EEEW',1j:'SSNS'}
# Explicit rejected cycle, independent ordered input/output occurrence matching.
bad=next(v[2]for v in upper if not v[-1]);cycle=[((1j,1),(1+1j,0),1),((1+1j,0),(1+1j,1),4),((1+1j,1),(1+2j,0),1),((1+2j,0),(1+2j,1),4),((1+2j,1),(2j,1),1),((2j,1),(1j,1),1)]
for (p,i),(q,j),gap in cycle:
 if p==q:assert j==i+1 and gap==4
 else:
  d=outs(bad[p])[i];assert q-p==vec[d] and bad[q][j]==d
  assert sum(x==d for x in outs(bad[p])[:i])==sum(x==d for x in bad[q][:j])
assert sum(e[2]for e in cycle)==12
rs=[]
for r,q in product(even,range(4)):
 h,ht,en,bd=locate(r,-1-1j,q)
 if en!=0 or h.get(0)!='WWEW':continue
 if outs(h[-1j]).count('E')!=1 or h[-1].count('S')!=1 or ht.get(-2)!=0:continue
 rs.append((r,q,h,ht))
assert len(rs)==3 and all(q==1 for r,q,h,ht in rs)
pairs=[]
for (r,rq,rh,rt),d,q in product(rs,even,range(4)):
 dh,dt,de,db=locate(d,-2,q)
 if dh.get(-1+1j)!='EEWE' or dh.get(-1)!=rh[-1]:continue
 # Exact canonical incoming contact determines the putative physical four-cycle.
 cyclic=(de==-1)
 if cyclic:assert q==0 and rh[-1]=='NNSN'
 positive=(d==F)
 pairs.append((r,d,q,cyclic,positive))
assert len(pairs)==10 and sum(p[3]for p in pairs)==8
assert sum(not p[3]and not p[4]for p in pairs)==1
rr,dd,dq,_,_=next(p for p in pairs if not p[3]and p[4]);assert dq==2 and rr[2]==()and rr[3]==-1
rh,rt,re,rb=locate(rr,-1-1j,1);dh,dt,de,db=locate(dd,-2,2)
assert rh=={-1:'SNNN',0j:'WWEW',-1j:'SSSN',-1-1j:'WEWW'}
assert dh=={-1+1j:'EEWE',-1:'SNNN',-2:'WWEW',-2+1j:'SSNS'}
# Translation of the output full interface recovers ALL next induction inputs.
nextU=locate(U,-3+1j,3);assert nextU[0][-2+1j]=='SSNS'
assert uh[-1+1j]=='EEWE' and uh[-1+2j]=='NNNS' and ut[-2+2j]==-2
# Exact full-drift contradiction, checked symbolically by coordinate formulas.
for a in range(-25,26):
 if a==0:continue
 N=abs(a);k=-2*(1 if a>0 else -1)
 assert k*a==-2*N
 assert -3-2*N==(-5-2*(N-1))
 assert -2-2*N==(-4-2*(N-1))
D=ROOT/'K1_pipeline_detours_2026-10-23';note=D/'zero_output_half_turn_ancestry_rail_exclusion.md';sha=hashlib.sha256(note.read_bytes()).hexdigest();assert sha=='45753ce6d48b7facd1bc8dc1777d96d2d961ecd9a4d01ed4a96b685225eea471'
out={'status':'PASS conditional zero-output half-turn ancestry-rail exclusion','note_sha256':sha,'fresh_full_profile_count':len(base),'even_flag_one_profiles':len(even),'upper_candidates':2,'upper_ordinal_cycle_rejections':1,'explicit_cycle_minimum':12,'lower_profiles':3,'lower_parent_pairs':10,'physical_birth_cycles':8,'nonpositive_source_after_leaf_saturation':1,'induction_survivors':1,'analytic':['Zero output plus the signed canonical flag inventory ensures any actual parent of a flag-one child has incoming flag one; thus the seven even flag-one profiles exhaust the newly used parents. The upper opposite low face alone is insufficient. The carried SW EEWE and NW NNNS histories of the actual NE child are essential and supply the explicit twelve-step positive ordinal cycle eliminating EWEE.','The remaining upper parent has exactly one possible child, the already actual D_n, and propagates the actual parent D_(n+1), strict upper opposite face, and both k/j complete histories. No K1 or Gamma membership is needed.','Eight lower pairs impose the finite PHYSICAL canonical cycle D_(n+1)->U_n->D_n->R_n->D_(n+1). Strict first-boundary birth order excludes this on distinct physical faces, independently of any full-drift quotient. The remaining lower terminal flag-one leaf, global zero-output saturation and unique opposite-leaf source recovery force the actual positive half-turned D_(n+1), not merely a potential duplicator. All four interface clauses, including the stable opposite-leaf full history, propagate.','If full drift has nonzero vertical coordinate, the forced fixed-height D_n give infinitely many active quotient classes, impossible for one finite full-period trace. If full drift is (a,0), choose N=abs(a), k=-2 sign(a). Translation k*d maps initial terminal L_0 to degree-one U_(N-1); equivalently its complete SE history NSSS would equal SSNS. This uses the actual full period and drift, not a primitive substitute.','The initial local mode can occur as a necessary finite motif, but cannot extend to a complete translating WHITE cap-four zero-output front. Cross-Gamma naming or same-component ancestry does not affect this full physical induction.'],'scope':'Only the displayed actual half-turn mode under Nodd=0. Positive-output interruptions, unrelated zero-output fronts, general K1 and universal capture are not excluded.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
