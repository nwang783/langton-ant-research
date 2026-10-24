from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'K1_pipeline_detours_2026-10-23';ns={'__file__':str(SELF.parent/'check_zero_output_Q2_and_same_curve_ear_independent.py')};exec(Path(ns['__file__']).read_text().split('def close(')[0],ns);base,locate,outs,cp=[ns[x]for x in('base','locate','outs','cp')]
def pos(h):return len(h)==3 and h[0]!=h[2]and h[1]==h[2]
upper=[];lower=[];nextparents=[]
for row in base:
 for turn in range(4):
  hh,ht,en,bd=locate(row,-1+1j,turn)
  if hh[1j]=='SSNS'and ht.get(2j)==-2:
   odd={p for p,h in hh.items()if len(h)%2};cover={p for p in(-1+1j,-1+2j,2j)if len(hh[p])%2 and not pos(hh[p])};assert not odd or cover
   upper.append((tuple(hh[p]for p in(-1+1j,-1+2j,2j,1j)),sorted((int(p.real),int(p.imag))for p in cover)))
  hh,ht,en,bd=locate(row,-1-1j,turn)
  if hh[0]=='WWEW'and en==0 and hh[-1].count('S')==1 and outs(hh[-1j]).count('E')==1:
   odd={p for p,h in hh.items()if len(h)%2};cover={p for p in(-1j,-1-1j)if len(hh[p])%2 and not pos(hh[p])};assert not odd or cover
   lower.append((tuple(hh[p]for p in(-1-1j,-1,0,-1j)),sorted((int(p.real),int(p.imag))for p in cover)))
  # Critical omitted-odd-test challenge: use ALL110, not just even next parents.
  hh,ht,en,bd=locate(row,-2,turn)
  children={-2+(.5+.5j)+(cp[v]-(.5+.5j))*1j**turn for v in row[2]}
  if hh[-1+1j]=='EEWE'and hh[-1]=='NNSN'and -1+1j in children:
   assert en==-1;nextparents.append(row[0])
assert len(upper)==5 and len(lower)==9 and len(nextparents)==5
assert {x[0]for x in upper}=={('EEW','NNSS','EWE','SSNS'),('EEWE','NNN','EWE','SSNS'),('EEWE','NNNS','EEEW','SSNS'),('EEWE','NNNS','EWEE','SSNS'),('W','SSNS','EEEW','SSNS')}
S={-1+1j,-1+2j,2j,-1j,-1-1j};union=set()
for q in range(4):union|={(.5+.5j)+(p-(.5+.5j))*1j**q for p in S}
assert len(union)==12 and Counter(int(p.real+p.imag)%2 for p in union)=={0:6,1:6}
note=D/'half_turn_rail_excludes_positive_flat_output_capacity.md';sha=hashlib.sha256(note.read_bytes()).hexdigest();assert sha.startswith('0a9e95c9')
out={'status':'PASS typed half-turn rail output capacity excluding all positive-flat three-read classes','note_sha256':sha,'fresh_upper_five':upper,'fresh_lower_nine':lower,'all110_next_parent_challenge_five_profiles':nextparents,'rotated_witness_offsets':sorted((int(p.real),int(p.imag))for p in union),'analytic':['Every odd upper completion has a non-positive-flat witness among z/y/v. Every odd lower completion has a same-R witness at l or s, even when a itself is positive-flat. Therefore the five designated witness offsets cover every odd obstruction in those actual squares.','For the even upper pair, the signed carried k/j ordinal +12 cycle still eliminates EWEE. For the lower NNSN alternatives, I additionally tested ALL110 possible next-parent profiles, allowing uninspected odd corners: all five completions with actual upper child and NE EEWE have canonical entry exactly a. Hence the physical canonical cycle excludes them without a hidden evenness assumption on the next source.','The remaining lower R is a stable flag-one leaf. If outside the exact residual set U, its definition makes it the I leaf of an ACTUAL D4. Unique inverse-I recovery identifies the next source and forces its still-uninspected corners four-read. No extra odd test is silently skipped in activation.','The signed nonmerge and quotient-equivariant stopping arguments apply to the unchanged carried full interface. Five offsets generate12 physical offsets, six per checker parity. Each non-positive odd class covers at most six distinct stopping sources; each U leaf determines its unique parent source.','The exact residual U output payment uses only negative-flat canonical entries, same-R helpers and singleton classes, all disjoint from positive-flat Npos and the optional signed S-ancestor singletons. Thus |U|+Npos+nSanc<=Nodd.','This yields H<=6(Nodd-Npos)+|U|<=7(Nodd-Npos)-nSanc. The now-signed early x/e pair supplies Npos>=2n3, giving H<=7Nodd-14n3-nSanc without adding overlapping output budgets.'],'scope':'Exact initial half-turn interfaces only, complete WHITE cap4 translating fronts. Rail itself needs no K1/zero-output assumption; optional early-family coupling is K1 scoped. OUTPUT capacity, not initial fuel or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha)
