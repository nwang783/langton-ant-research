from pathlib import Path
from collections import Counter
from itertools import product
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();files={'flow2_reset_archives_retain_an_exact_L3_tail_v2.md':'3528b7624f52c41b6a345aad410ae1ff5eee7b9ad9bbe74d77cd6a0c529f9599','check_flow2_reset_L3_tail_v2.py':'093a729318c1208a23949e358bca1b4cbee565615b75502e0b0faffd98af5561','check_flow2_reset_L3_tail_v2.json':'d09160536ef8b21c661b2a9943efcbecab4d283b39e2f60b1bd78926b451e318'}
for f,h in files.items():assert sha(D/f)==h
J=json.loads((D/'check_flow2_reset_L3_tail_v2.json').read_text());heads='NESW';V=[1j,1,-1j,-1]
def edges(H):
 ans={}
 for p,w in H.items():
  for h,d in enumerate(V):
   q=p+d
   if q not in H:continue
   src=[r for r,c in enumerate(w)if(heads.index(c)+(1 if r%2==0 else-1))%4==h];dst=[r for r,c in enumerate(H[q])if heads.index(c)==h];assert len(src)==len(dst)
   for r,s in zip(src,dst):ans[p,r]=(q,s)
 return ans
for mode in('WEE','WEEW','WWEE'):
 for qword in('NSSN','NNSS'):
  H={0j:'NSSN',1+0j:mode,1+1j:qword};e=edges(H)
  if mode=='WWEE':assert e[0j,1]==(1+0j,3)and e[1+0j,3]==(1+1j,3 if qword=='NSSN'else 1)
  else:assert e[0j,1]==(1+0j,2)and e[1+0j,1]==(1+1j,3 if qword=='NSSN'else 1)
for mode in('EWW','EWWE'):
 H={0j:'NNSS',1+0j:'EEWW',1+1j:'SNNS',1j:mode};e=edges(H);route=[(1j,1),(0j,3),(1+0j,1),(1+1j,1),(1j,2)]
 for a,b in zip(route,route[1:]):assert e[a]==b
 # The A->B middle step is the non-boundary chord; the other three are selected b edges.
def jump(terms):
 c=Counter()
 for sign,a,b in terms:c[a]+=sign;c[b]-=sign
 return {a:v for a,v in c.items()if v}
rows=[]
for kind in('single','LL'):
 for span in((4,8,12)if kind=='single'else(4,)):
  t=21 if kind=='single'else 23;end=t+span;xs=t+(1 if kind=='single'else 2);ys=end-1
  for ax,ay in product((8,16,36),repeat=2):
   xe=xs+ax;ye=ys+ay;edge=[(t,xs),(ys,end)]if kind=='single'else[(t,t+1),(t+1,xs),(ys,end)]
   lhs=[(1,t,end),(1,ys,ye),(-1,xs,xe)];rhs=[(1,a,b)for a,b in edge]+[(1,xe,ye)];assert jump(lhs)==jump(rhs);rows.append(dict(kind=kind,root_span=span,X13=ax,Y13=ay,tail_sign=(ye>xe)-(ye<xe)))
assert rows==J['mixed_tail_controls']and{r['tail_sign']for r in rows}=={-1,1}
# Exact symbolic cancellation represented by arbitrary symbolic endpoints.
assert jump([(1,'r1','r2'),(1,'Y1','Y3'),(-1,'X1','X3'),(-1,'r1','X1'),(-1,'Y1','r2'),(-1,'X3','Y3')])=={}
for gap in(1,2,3):assert jump([(1,20,40+gap),(1,40,60)])==jump([(1,20,60),(1,40,40+gap)])
out=dict(status='PASS v2 reset L3-tail identities and conditional all-Y cluster relay; no physical erasure',files=files,script=sha(S),controls=len(rows),analytic_review=['Actual complete port ordinals independently reconstructed for singleton O/U and passive V between flat Y and Y/X, and both LL-first O/U squares. Following Y gives rootL1->Y.L3; following X gives rootL1->X.L1. Preceding Y.L1 feeds rootR2. Passive single V gives Y.L1->V.L3->nextY.L3, length2.','The mixed singleton identity retains both T3X and T3Y with an ORIENTED residual interval, either sign. LL-first cleanup has four actual L steps but only three selected boundary edges: its X->Y middle chord remains outside B_selected. Optional U L3 and earlier X R0 are never erased.','For the stated critical/global-M admissible all-Y local profiles, internal gaps are RR1, passive V2, passive VV3, or O wait with two overlaps1. LL-first O/U would force an X and is not included. Flat intervals have length>=8 and adjacent overlap sums<=6; O intervals length>=4 and overlap sum2. Thus starts/ends strictly increase and no third overlap is possible for every finite cluster, without a length scan.','All period translates may be summed only after the physical identity, retaining arbitrary old copies and full voltages. The v2 passive single-V case is required; unpromoted v1 is not signed as a complete general gap list. No curvature theorem, exterior completion, ant deletion, bounded age, fresh-fuel payment or unrestricted all-cap/global classification follows.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
