#!/usr/bin/env python3
"""At most two literal four-turn pose-return insertions into fixed prepared80.
This is an exact finite candidate family, not an arbitrary period/visit bound.
"""
from pathlib import Path
from itertools import combinations_with_replacement,product
from collections import defaultdict,Counter
import json,hashlib
from check_extremal_read_coupling import event_word,quotient
from lifetime_boundary_graph import analyze
R=Path(__file__).resolve().parent
W='RRRRLLLLRLRRRRLLLLRLRLRRRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRLRLRRRRLRRRRLLLLRLLRRL'
def inspect(w):
 E,d,h=event_word(w);assert d==(4,4)and h==0;H=defaultdict(list)
 for e in E:
  q,k=quotient(e['p'],d);H[q].append((e['t']-len(w)*k,e['t'],e['c'],k))
 for q,es in sorted(H.items()):
  es.sort()
  for a,b in zip(es,es[1:]):
   if a[2]==b[2]:return {'status':'NONALTERNATING_ON_ANY_INITIAL_BOARD','witness':{'representative':q,'complete_history':es,'same_turn_neighbors':[a,b]}}
 I=[(q,es[0])for q,es in sorted(H.items())if es[0][2]=='L'];O=[(q,es[-1])for q,es in sorted(H.items())if es[-1][2]=='R'];f=analyze(w)
 return {'status':'COMPLETE_WHITE_CANDIDATE'if not I else'STABLE_PREPARED_INPUT_REQUIRED','I':len(I),'O':len(O),'input_roots':I,'output_roots':O,'S':sum(abs(c['winding'])for c in f['root_skeleton_cycles']),'boundary_cycles':f['root_skeleton_cycles'],'word':w}
def main():
 rows=[];seen={};counts={};labelled=0
 for n in[1,2]:
  fresh=[]
  for cuts in combinations_with_replacement(range(80),n):
   for turns in product('RL',repeat=n):
    labelled+=1;insert={}
    for cut,c in zip(cuts,turns):insert[cut]=insert.get(cut,'')+4*c
    w=''.join(insert.get(i,'')+c for i,c in enumerate(W))
    if w in seen:continue
    result=inspect(w);result.update(cuts=cuts,loop_turns=turns,P=len(w),word_sha256=hashlib.sha256(w.encode()).hexdigest());seen[w]=len(rows);rows.append(result);fresh.append(result)
  counts[n]=dict(Counter(r['status']for r in fresh));print(n,counts[n],flush=True)
 stable=[r for r in rows if r['status']!='NONALTERNATING_ON_ANY_INITIAL_BOARD'];print('labelled',labelled,'distinct',len(rows),'WHITE',sum(r['I']==0 for r in stable),'minI',min([r['I']for r in stable],default=None),flush=True)
 print('best',[(r['I'],r['O'],r['S'],r['cuts'],r['loop_turns'])for r in sorted(stable,key=lambda r:(r['I'],r['P']))[:15]],flush=True)
 result={'status':'AUTHOR EXACT BOUNDED CONSTRUCTION CHECK; independent review pending','scope':'Exactly one or two literal RRRR/LLLL pose-return loop insertions at the80 cuts of the supplied prepared80 word, preserving actual turn order otherwise. No router, longer excursion, third insertion, or arbitrary controller exclusion.','backbone_word':W,'labelled_candidates':labelled,'distinct_words':len(rows),'counts_by_insertion_number':counts,'all_distinct_word_checks':rows}
 (R/'prepared80_four_turn_owner_repairs.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()
