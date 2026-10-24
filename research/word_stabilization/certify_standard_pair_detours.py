from pathlib import Path
import sys,json,re
from collections import defaultdict,deque
sys.path.insert(0,str(Path('../computability').resolve()))
from periodic_tail_checker import State,first_mismatch,plan
root=Path('..');W=re.search(r'const string W="([LR]+)"',Path('enumerate_adjacent_pair_spacing.cpp').read_text()).group(1);long=W*5;CW={long[i:i+149]:i for i in range(104)}
legal=(root/'continuation_2026-10-22/ant_continuation/factor_language/words150.txt').read_text().splitlines();rev=defaultdict(list)
for w in legal:rev[w[1:]].append(w[:-1])
reach=set(CW);q=deque(CW);NEXT={}
while q:
 b=q.popleft()
 for a in rev[b]:
  if a not in reach:reach.add(a);q.append(a);NEXT[a]=b
D=((0,1),(1,0),(0,-1),(-1,0))
def trace(word,p=(0,0),h=0):
 out=[]
 for c in word:out.append((p,c));h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return out,p,h
surv=json.loads(Path('standard_single_cluster_probe.json').read_text())['results'][1]['examples'];results=[]
for z in surv:
 if not z['reaches_standard']:continue
 w=z['word'];history=w[-149:];bridge=''
 while history not in CW:history=NEXT[history];bridge+=history[-1]
 w+=bridge;tr,p,h=trace(w);last={};seed=set();ok=True
 for pos,c in tr:
  if last.get(pos)==c:ok=False;break
  if pos not in last and c=='L':seed.add(pos)
  last[pos]=c
 result={'initial_phase':z['phase'],'bridge_length':len(bridge),'literal_bridge_feasible':ok}
 if not ok:results.append(result);continue
 phase=(CW[history]+149)%104;period=W[phase:]+W[:phase];future,_,_=trace(period*10,p,h);seen=set();need=set()
 for pos,c in future:
  if pos not in seen and c=='L':need.add(pos)
  seen.add(pos)
 B=set(seed)
 for pos,c in tr:B.symmetric_difference_update((pos,))
 missing=need-B;illegal=missing&last.keys();result['required_missing_past_cells']=sorted(illegal)
 if illegal:results.append(result);continue
 seed|=missing;B|=missing;s=State(frozenset(B),p,h);mismatch=first_mismatch(s,period);result.update({'infinite_tail_first_mismatch':mismatch,'word':w,'period':period,'seed':sorted(seed),'entry_mass':len(seed),'tail_pose':[*p,h],'tail_mass':len(B),'added_unread_cells':sorted(missing)})
 if mismatch is None:
  # Recheck every prefix turn against the complete prepared seed.
  BB=set(seed)
  for pos,c in tr:assert (pos in BB)==(c=='L');BB.symmetric_difference_update((pos,))
  assert BB==B
 results.append(result)
Path('standard_pair_detour_certificates.json').write_text(json.dumps(results,indent=2));print('candidates',len(results),'certified',sum(z.get('infinite_tail_first_mismatch','fail')is None for z in results));print([{k:v for k,v in z.items()if k not in('word','period','seed','added_unread_cells')}for z in results])
