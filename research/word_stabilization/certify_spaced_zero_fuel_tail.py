from pathlib import Path
import json,sys,re
sys.path.insert(0,str(Path('../computability').resolve()))
from periodic_tail_checker import State,first_mismatch
D=json.load(open('spaced_completed_fresh_intersections.json'))['best'];M=json.load(open('spaced_two_marker_macros.json'))['macros'];W=re.search(r'const string W="([LR]+)"',Path('enumerate_adjacent_pair_spacing.cpp').read_text()).group(1)
steps=((0,1),(1,0),(0,-1),(-1,0))
def trace(w,p=(0,0),h=0):
 tr=[]
 for c in w:tr.append((p,c));h=(h+(1 if c=='R'else-1))%4;p=(p[0]+steps[h][0],p[1]+steps[h][1])
 return tr,p,h
word=D['prehistory']+''.join(M[a]['word']for a in D['macros'])+M[37]['word'];tr,p,h=trace(word);last={};seed=set()
for q,c in tr:
 assert last.get(q)!=c
 if q not in last and c=='L':seed.add(q)
 last[q]=c
B=set(seed)
for q,c in tr:B.symmetric_difference_update((q,))
results=[]
for phase in range(104):
 period=W[phase:]+W[:phase];future,_,_=trace(period*10,p,h);seen=set();need=set()
 for q,c in future:
  if q not in seen and c=='L':need.add(q)
  seen.add(q)
 missing=need-B
 if missing&last.keys():continue
 BB=B|missing;mm=first_mismatch(State(frozenset(BB),p,h),period)
 if mm is not None:continue
 complete=seed|missing;CC=set(complete)
 for q,c in tr:assert(q in CC)==(c=='L');CC.symmetric_difference_update((q,))
 assert CC==BB
 results.append({'phase':phase,'period':period,'seed':sorted(complete),'prefix':word,'prefix_macros':D['macros']+[37],'tail_pose':[*p,h],'added_unread_cells':sorted(missing),'seed_mass':len(complete),'exact_tail_first_mismatch':mm})
Path('spaced_completed_zero_fuel_standard_tail.json').write_text(json.dumps(results,indent=2));print('certified standard tails',len(results));print([{k:v for k,v in z.items()if k not in('seed','prefix','period')}for z in results])
