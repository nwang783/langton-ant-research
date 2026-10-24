from pathlib import Path
from itertools import product
from collections import Counter
import hashlib,json
SELF=Path(__file__).resolve();R=SELF.parents[1];ns={'__file__':str(SELF.parent/'check_zero_output_Q2_and_same_curve_ear_independent.py')};exec(Path(ns['__file__']).read_text().split('results=[]')[0],ns)
base,even,priors,F,locate,close,outs,find=[ns[k]for k in('base','even','priors','F','locate','close','outs','find')];D=R/'K1_pipeline_detours_2026-10-23'
rr=[r for r in even if locate(r,-3-1j,1)[0].get(-3-1j)=='WEWW'and locate(r,-3-1j,1)[0].get(-3)=='SNNN'];assert len(rr)==1
U=find(('NNSN','WWWE','NNNS','EEWE'));uc=Counter()
for packs,z in priors:
 for u,q in product(even,range(4)):
  if close(packs+[(rr[0],-3-1j,1),(F,-4,2),(u,-5+1j,q)])is not None:uc[(u[0],q)]+=1
assert uc=={(U[0],3):3}
rows=[];candidates=0
for packs,z in priors:
 old=packs+[(rr[0],-3-1j,1),(F,-4,2),(U,-5+1j,3)]
 for r,d,q in product(even,even,(0,2,3)):
  rh=locate(r,-5-1j,1)[0];dh=locate(d,-6,q)[0]
  if rh.get(-4)!='WWEW'or outs(rh[-4-1j]).count('E')!=1 or rh[-5].count('S')!=1:continue
  if dh.get(-5+1j)!='EEWE'or dh.get(-5)!=rh[-5]:continue
  candidates+=1;c=close(old+[(r,-5-1j,1),(d,-6,q)])
  if c is not None:rows.append((r,d,q,c))
assert candidates==120 and len(rows)==3
for r,d,q,(hh,ht)in rows:assert r==rr[0]and d==F and q==2;assert hh[-5]=='SNNN'and hh[-5-1j]=='WEWW'
# Exact displayed U, shifted second half-turn and canonical terminal types.
uh=locate(U,-5+1j,3)[0];assert uh=={-5+1j:'EEWE',-5+2j:'NNNS',-4+2j:'EEEW',-4+1j:'SSNS'}
assert rr[0][2]==()and rr[0][3]==-1;assert U[2]==('B',)
name='zero_output_half_turn_two_source_finite_closure.md';sha=hashlib.sha256((D/name).read_bytes()).hexdigest();assert sha=='29334de0b4735fded73b36dfe0e920b0da365be40133d0d828b543a7326cd39c'
out={'status':'PASS zero-output half-turn finite LOCAL four-duplicator/four-leaf motif; ancestry unclosed','note_sha256':sha,'independent_even_priors':12,'rigid_U_profile':U[0],'U_rotation':3,'new_candidates':120,'survivors':3,'analytic':['Known Q2 actual flag-one child and zero-output q balance force its parent U to have entry flag1; otherwise U would be a forbidden odd positive source. All seven even flag1 profiles in all four rotations, merged with complete known ports/heights/canonical minima, leave only the displayed EEWE/NNNS/EEEW/SSNS physical U, with one RIGHT child Q2. Its genuine parent is D_left=(-6,0).','The other actual Q2 child Rprime can locally have either a=NNSN, giving a canonical Rprime->D_left, or a=SNNN, giving a flag1 leaf. The first closes a finite physical parent cycle D_left->U->Q2->Rprime->D_left and contradicts strict first-boundary birth order. It is not a quotient-winding argument.','Thus Rprime is a genuine leaf. Zero-output saturation plus the unique all-four I overlap forces D_left to be an actual positive half-turned duplicator, not just a potential two-child face. Independent complete closure gives120 candidates and3 rows, differing only at the far-right earlier G square.','Actual edges are D->J->P0 with childrenI0,R; D_left->U->Q2 with childrenQ1,Rprime. Opposite-I associations are D->I0,P0->Q1,Q2->R,D_left->Rprime. Hence that half-turn late-route activation returns to the existing P0; these finite local identities alone do not imply an infinite left chain or exclude a separate ancestry induction.','All interiors are only necessary complete local histories, not a single connected physical WHITE front. The earlier ear locates Q2 off/LEFT of original Gamma but does not locate D_left; earlier same-Gamma, off-Gamma or other-curve ancestry stays open.'],'scope':'Conditional zero-output exact late-route half-turn mode. No literal realization, new original root, component count, unbounded regress, global K1 exclusion or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
