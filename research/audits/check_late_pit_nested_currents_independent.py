from pathlib import Path
from collections import Counter
from itertools import product
import hashlib,json
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23'
ns={'__file__':str(R/'audits/check_canonical_birth_rank3_balance_independent.py')};exec(Path(ns['__file__']).read_text().split('rows=[];candidates=0')[0],ns)
choices,possible,departures=(ns[k]for k in('choices','possible','departures'));H='NESW';vec={'N':1j,'E':1,'S':-1j,'W':-1}
parents=[]
for x,g in product(choices('W'),choices('N')):
 hs={'A':'NNSN','Z':x[0],'Y':g[0],'B':'EEWE'}
 if all(len(v)==4 for v in hs.values())and possible(hs):parents.append((x,g))
assert{(x[0],g[0])for x,g in parents}=={('WWWE','NNNS'),('WWWE','NSNN'),('WWEW','NSSS'),('EWWW','SSNS')}
def closure(x,g,f):
 hs={-1:'NNSN',-2:x,-2+1j:g,-1+1j:'EEWE',-1+2j:'NNNS',2j:'EWEE',1j:'NSSS',-2+2j:f};oo={p:departures(s)for p,s in hs.items()};nodes=[(p,r)for p,s in hs.items()for r in range(4)];edges=[]
 for p in hs:edges.extend(((p,r),(p,r+1),4)for r in range(3))
 for p,s in hs.items():
  for hd in'EW'if s[0]in'NS'else'NS':
   q=p+vec[hd]
   if q not in hs:continue
   a=[(p,r)for r,c in enumerate(oo[p])if c==hd];b=[(q,r)for r,c in enumerate(hs[q])if c==hd]
   if len(a)!=len(b):return False
   for u,v in zip(a,b):edges.extend([(u,v,1),(v,u,-1)])
 for birth,bd in[((-1,1),[(-1,'W'),(-2,'N'),(-2+1j,'E'),(-1+1j,'S')]),((-1+1j,1),[(-1+1j,'N'),(-1+2j,'E'),(2j,'S'),(1j,'W')])]:
  for p,hd in bd:
   v=(p,oo[p].index(hd))
   if v!=birth:edges.append((birth,v,1))
 dist={v:0 for v in nodes}
 for _ in nodes:
  changed=False
  for u,v,k in edges:
   if dist[v]<dist[u]+k:dist[v]=dist[u]+k;changed=True
  if not changed:return True
 return False
rows=[]
for x,g in parents:
 for f in(['EEWE','WEEE']if g[1]=='M-2'else['EWEE','EEEW']):
  if closure(x[0],g[0],f):rows.append((x[0],g[0],f,g[1]))
assert{(g,f)for x,g,f,h in rows if h=='M-2'}=={('NNNS','WEEE'),('NSNN','EEWE')}
assert all(h=='M'for x,g,f,h in rows if x!='WWWE')
# Stream heights at the strict flat f, choosing M0,b=-2,a=b-1=-3.
heights=[]
for f in('EEWE','WEEE'):
 r=Counter(f[::2]);l=Counter(f[1::2]);a=-3
 HNW=1-l['E']+a;HNE=r['W']+a;HSE=1-l['W']+a;HSW=r['E']+a
 assert(HNE,HSW,HNW-1)==(-2,-2,-5);heights.append((f,HNW-1))
# Every selected WHITE flat max contact has opposite R and at most2 L at either heading.
for l0,l1 in product('EW',repeat=2):
 assert min(-1-(l0+l1).count('E'),-1-(l0+l1).count('W'))>=-3
bindings={}
for name,prefix in [('D4_late_parent_lower_depth_or_outward_maximum.md','54e05517'),('nested_C_L_birth_cuts_three_current_budget.md','f3a81d5f'),('strict_late_D4_pit_LEFT_localization_and_two_cut_alternative.md','4769bd41'),('reverse_read_event_conjugacy_clarification.md','0353c796')]:
 p=D/name;s=hashlib.sha256(p.read_bytes()).hexdigest();assert s.startswith(prefix);bindings[name]=s
out={'status':'PASS conditional late-D4 pit, nested physical current partition, LEFT localization and reverse convention','note_hashes':bindings,'independent_P0_parents':parents,'independent_f_port_closure':rows,'strict_unshifted_L_heights_M0':heights,'analytic':['The independently reconstructed one-face max-plus inventory gives exactly four all-four P0 alternatives. Closing its shared ports with the actual I square and f gives the strict pairs gNNNS/fWEEE and gNSNN/fEEWE. Their C heights equal b and two E-arriving L reads give unshifted NW L height b-3=M-5. Non-strict alternatives have a genuine extra outward max Q1, not a new component.','For two disjoint essential C/L cuts with constant heights lambda and m in the specified order, define far-left stream h-m on that band, far-right h-lambda on that band, and middle stream m/h/lambda. Their sum is h. Because cut faces have exactly the matching constants, each physical edge receives its entire old nonnegative multiplicity in exactly one band, including an edge between adjacent cut faces. Stream telescoping gives balanced integer currents; no diagonal contact edge is counted as physical flow.','The original-drift homologies are -K_L, K_C+K_L+1, -K_C. Checker balance gives equal horizontal/vertical occurrence totals in each band, so its length is at least2||d||infinity times absolute homology. Hence P>=2D[2(K_C+K_L)+1], and18D when K_C1,K_L>=3. These are disjoint spatial currents, not additions to overlapping chronology budgets.','A genuine canonical child J leaving D into the LEFT sector cannot later enter Gamma: unique canonical parent ancestry would force it to be D\'s Gamma successor, contrary to the actual successor G. Thus J,P0,I stay LEFT, also after full-drift quotient identifications. In the strict case g joins max P0 to lower Q1 and cannot be a selected max/max contact. The corridor through g,Q1 and an interior physical edge reaches pit V without meeting Gamma.','At every selected Gamma contact both incident L heights are>=M-3=b-1, so an L-contact component of h<=b-3 cannot cross Gamma. The pit component stays LEFT and has finite full-drift classes because it lies below both exterior levels. A minimum plateau in that component is also locally minimal in the entire lattice: any lower corner-neighbor belongs to the same sublevel component.','An odd-output-free such plateau yields the signed reverse WHITE-selected curve, with K_L>=3, wholly LEFT and disjoint from Gamma. Otherwise an actual LEFT odd-output contact is retained, with no per-D injection. The local D158 finite prepared control supplies no global stream premise.','Exact reversal at a forward read uses the postflip board and incoming heading opposite forward outgoing heading. This gives H_rev=1-H_original because sectors swap and h_rev=-h; it is not reversal of the incoming heading at the unshifted poststep state.'],'scope':'All local-route and two-cut existence/order/odd-collar hypotheses are explicit. No unconditional18D for K1, no original K>=2, original fuel, per-route output charge, repeated supplier mechanism or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(rows);print(bindings)
