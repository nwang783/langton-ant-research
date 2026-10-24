#!/usr/bin/env python3
"""Bounded exact supplied-word construction attempt, not a general exclusion.
At most four whole prepared80 blocks at six explicit natural phase cuts.
"""
from pathlib import Path
from itertools import product
from collections import defaultdict,Counter
import json,hashlib
from check_extremal_read_coupling import event_word,quotient
from lifetime_boundary_graph import analyze
R=Path(__file__).resolve().parent
W='RRRRLLLLRLRRRRLLLLRLRLRRRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRLRLRRRRLRRRRLLLLRLLRRL'
CUTS=[0,10,27,42,66,1];BLOCKS={i:W[i:]+W[:i]for i in CUTS}
def inspect(seq):
 w=''.join(BLOCKS[i]for i in seq);E,d,h=event_word(w);assert h==0;row={'cuts':seq,'P':len(w),'full_drift':d,'word_sha256':hashlib.sha256(w.encode()).hexdigest()}
 if d==(0,0):row['status']='ZERO_DRIFT_NOT_A_TRANSLATOR';return row
 H=defaultdict(list)
 for e in E:
  q,k=quotient(e['p'],d);H[q].append((e['t']-len(w)*k,e['t'],e['c'],k))
 for q,es in sorted(H.items()):
  es.sort()
  for a,b in zip(es,es[1:]):
   if a[2]==b[2]:row.update(status='NONALTERNATING_ON_ANY_INITIAL_BOARD',witness={'representative':q,'complete_history':es,'consecutive_same_turn_events':[a,b]});return row
 I=[(q,es[0])for q,es in sorted(H.items())if es[0][2]=='L'];O=[(q,es[-1])for q,es in sorted(H.items())if es[-1][2]=='R'];assert len(O)-len(I)==12*len(seq)
 row.update(status='COMPLETE_WHITE_CANDIDATE'if not I else'STABLE_PREPARED_INPUT_REQUIRED',I=len(I),O=len(O),all_input_root_classes_and_owners=I,all_output_root_classes_and_owners=O,word=w)
 if d[0]and d[1]:
  f=analyze(w);row['S']=sum(abs(c['winding'])for c in f['root_skeleton_cycles']);row['boundary_cycles']=f['root_skeleton_cycles']
 return row

def main():
 rows=[];counts={}
 for n in range(1,5):
  rr=[inspect(seq)for seq in product(CUTS,repeat=n)];rows+=rr;counts[n]=dict(Counter(r['status']for r in rr));print(n,counts[n],flush=True)
 white=[r for r in rows if r['status']=='COMPLETE_WHITE_CANDIDATE'];print('WHITE',len(white),flush=True)
 stable=[r for r in rows if r['status']=='STABLE_PREPARED_INPUT_REQUIRED'];print('minimal I',sorted((r['I'],r['cuts'],r['full_drift'],r.get('S'))for r in stable)[:12],flush=True)
 out={'status':'AUTHOR EXACT BOUNDED CONSTRUCTION CHECK; independent review pending','scope':'Exactly1554 labelled words from one through four whole prepared80 blocks at cuts0,10,27,42,66,1. No arbitrary router, other phase, longer composition, active cap, or general macro language is covered.','word':W,'cuts':CUTS,'cut_motivation':'Five actual RRRRLLLLRL module entries, plus phase1 for the missing quarter orientation.','counts':counts,'complete_white_candidates':white,'all_supplied_word_checks':rows}
 (R/'prepared80_natural_phase_compositions.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
