from pathlib import Path
from itertools import product
from collections import Counter
import hashlib,json
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23'
s=(SELF.parent/'check_canonical_birth_rank3_balance_independent.py').read_text();ns={'__file__':str(SELF.parent/'check_canonical_birth_rank3_balance_independent.py')};exec(s.split('expected=')[0],ns);base=ns['rows'];assert len(base)==110;heads='NESW';corners={'A':1,'Z':0,'Y':1j,'B':1+1j};other={'A':1-1j,'Z':-1-1j,'Y':-1+1j,'B':1+1j}
def rotatehist(h,q):return ''.join(heads[(heads.index(c)-q)%4]for c in h)
def pose(row,ll,q):
 hs={ll+(1+1j)/2+(p-(1+1j)/2)*1j**q:rotatehist(h,q)for p,h in zip(corners.values(),row[0])};entry=ll+(1+1j)/2+(1-(1+1j)/2)*1j**q
 children={ll+other[k]*1j**q for k in row[2]};return hs,entry,children
physical=[]
for g,f in[('NSSS','EWEE'),('NSSS','EEEW'),('SSNS','EEEW')]:
 for row,q in product(base,(2,3)):
  hs,e,ch=pose(row,-3+1j,q)
  if hs.get(-2+1j)==g and hs.get(-2+2j)==f:physical.append((hs,e,ch,row,q))
assert len(physical)==4
summary=[]
for hs,e,ch,row,q in physical:
 g,f,k,j=(hs[p]for p in[-2+1j,-2+2j,-3+1j,-3+2j]);assert(g,f,k,j)in[('NSSS','EWEE','W','SSNS'),('NSSS','EWEE','EEWE','NNNS'),('SSNS','EEEW','W','SSNS'),('SSNS','EEEW','EEWE','NNNS')];assert len(hs[e])==4 and hs[e][1]==hs[e][3]
 assert ch<=set([-2+0j]);assert ch==({-2+0j}if g=='SSNS'else set())
 summary.append((g,f,k,j,q,[(int(z.real),int(z.imag))for z in ch]))
# Exact D->Q1 injection, including possible rotated canonical frames.
seen={}
for hs,e,ch,row,q in physical:
 for rot in range(4):
  relative={((p-(-3+1j))-(1+1j)/2)*1j**rot+(1+1j)/2:rotatehist(h,rot)for p,h in hs.items()};ent=((e-(-3+1j))-(1+1j)/2)*1j**rot+(1+1j)/2
  key=(tuple(sorted((int(p.real),int(p.imag),h)for p,h in relative.items())),(int(ent.real),int(ent.imag)));source=(3-1j)*1j**rot
  assert key not in seen or seen[key]==source;seen[key]=source
# Align every signed opposite-supplier I profile in all four rotations, retaining its actual canonical entry.
seven=[('EEW','NNSS','EWE','u'),('EEWE','NNN','EWE','u'),('EEWE','NNNS','EWEE','u'),('W','SSN','EWE','t'),('W','SSNS','EWEE','t'),('WE','SSNN','EWE','t'),('WEE','SSNN','EWE','t')];overlaps=[]
for hs,e,ch,row,q in physical:
 matched=[]
 for u,t,a,birth in seven:
  ish={-1+1j:u,-1+2j:t,2j:a,1j:'NSSS'};ie=-1+(1 if birth=='u'else 2)*1j
  for rot in range(4):
   def place(p):return -3+1j+(1+1j)/2+(p-(-1+1j)-(1+1j)/2)*1j**rot
   hh={place(p):rotatehist(h,rot)for p,h in ish.items()}
   if hh==hs and place(ie)==e:matched.append(-3+1j+(1-1j)*1j**rot)
 if hs[-2+1j]=='SSNS':assert not matched
 else:assert matched==[-2+0j]
 overlaps.append({'g':hs[-2+1j],'k':hs[-3+1j],'source_D_positions':[(int(p.real),int(p.imag))for p in matched]})
# Finite flag arithmetic, checked on all small nonnegative capacity parameters.
for O,C,H,S,D4,T,A,sa in product(range(3),repeat=8):
 if O+C+H+S+D4>=max(D4,A)+T:
  assert O+C+H+S+sa>=T+max(0,A-D4)+sa
for O,C,H,S,D4,A,L,LO,sa in product(range(2),repeat=9):
 if L<=D4 and LO<=L and O+C+H+S+D4>=A+L+LO:
  assert O+C+H+S+sa+D4-L>=A+LO+sa
bindings={}
for name,pref in [('late_D4_outward_Q1_terminal_leaf_and_injection.md','6d7d60d4'),('late_D4_outward_extra_leaf_output_capacity.md','64041a32'),('zero_output_duplicator_leaf_saturation_and_one_step_activation.md','56b51121')]:
 h=hashlib.sha256((D/name).read_bytes()).hexdigest();assert h.startswith(pref);bindings[name]=h
out={'status':'PASS outward late-Q1 terminal leaf, physical injections, flag capacity and conditional zero-output one-step activation','notes':bindings,'independent_canonical_face_profiles':len(base),'Q1_profiles':summary,'opposite_leaf_overlap':overlaps,'analytic':['The complete independently rebuilt110 canonical-face inventory matched to the actual two right corners leaves exactly four Q1 profiles. Every incoming flag is1. NSSS rows have no potential child; SSNS rows only potentially target P0, whose genuine parent J is already fixed. Hence every Q1 is an actual leaf, not merely a potential leaf.','Normalizing whole histories and the actual canonical entry fixes D uniquely, even after rotations and full-drift translation. The SSNS/EEEW profiles contain no mandatory positive-flat NSSS corner and cannot equal any signed D-associated I. Exact whole-square matching gives Q1(D)=I(D prime) only in NSSS/EWEE, with D prime=P0(D).','For selected-Gamma sources, actual canonical child descent through off-Gamma J cannot reenter Gamma by unique parent ancestry. Thus each outward Q1 is disjoint from all selected-Gamma I leaves. This does not exclude coincidence with an off-Gamma I.','Global SSNS extra leaves are disjoint from every D-associated I and from early I leaves. The flag identity and signed odd-output partition imply Nodd>=nT+max(0,nA-D4)+nSanc; combine overlapping rise/fall reservations only by maximum. On Gamma, distinct early/late I leaves and extra Q1 leaves imply Nodd+(D4-nL)>=nA+nLout+nSanc. Uncounted off-Gamma D4 capacity remains.','Under Nodd0, all O/DC/DH/DS vanish, so positive flag units are exactly D4. Their distinct terminal I leaves already exhaust all negative units. Every flag1 leaf therefore equals I of a unique ACTUAL positive D4. For an outward late route this excludes SSNS and singleton NSSS modes; the surviving all-four NSSS overlap forces P0 to be an actual positive duplicator, including its formerly only possible LEFT child.','This is only one-step activation. It does not establish the parent relation needed to repeat the late package. In K1 on Gamma the strict-pit alternative gives18D, while the outward alternative activates an off-Gamma duplicator; neither is a capture proof.'],'scope':'Complete WHITE cap4 front and actual canonical quotient, with selected-Gamma/K1 hypotheses only where stated. Output capacity, not original fuel, recursive ancestry, or realized front.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(summary)
