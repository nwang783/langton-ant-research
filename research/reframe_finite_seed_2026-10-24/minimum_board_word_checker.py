"""Primary exact existence checker for a capped first-return literal word.
Minimum-board monotonicity is retained reasoning, not a claim of novelty.
"""
from symbolic_capped_word import actual_property
from active_flight import DIR,step,comp,cursor
import json
from pathlib import Path
from itertools import product
import random
P=Path(__file__).parent

def minimum(word):
 p=(0,0);h=0;parity=set();bits={};visited=set()
 for t,c in enumerate(word):
  required=int(c=='L')^(p in parity)
  if p in bits and bits[p]!=required:return None,{'cut':t,'cell':p,'required_initial':required,'previous_initial':bits[p]}
  bits[p]=required;visited.add(p)
  if p in parity:parity.remove(p)
  else:parity.add(p)
  h=(h+(1 if c=='R'else-1))%4;p=(p[0]+DIR[h][0],p[1]+DIR[h][1])
 return {q for q,b in bits.items()if b},visited

def decide(word,M):
 seed,info=minimum(word)
 if seed is None:return {'status':'IMPOSSIBLE_READ_PARITY','conflict':info}
 ok,trace=actual_property(seed,word,M)
 return {'status':'EXISTS_FINITE_BOARD'if ok else'IMPOSSIBLE_BY_MINIMUM_BOARD','minimum_seed':sorted(seed),'trace':trace}

if __name__=='__main__':
 rng=random.Random(11124);cases=0;consistent=0
 for n in range(1,9):
  for cs in product('RL',repeat=n):
   word=''.join(cs);seed,vs=minimum(word)
   if seed is None:continue
   consistent+=1;unread=[(x,y)for x in range(-4,5)for y in range(-4,5)if(x,y)not in vs]
   for _ in range(8):
    extra=set(rng.sample(unread,rng.randrange(10)));B=set(seed)|extra;p=(0,0);h=0;Bmin=set(seed)
    for t,c in enumerate(word):
     assert('L'if p in B else'R')==c and('L'if p in Bmin else'R')==c
     assert comp(Bmin,1,cursor(p,h))<=comp(B,1,cursor(p,h))
     if t+4<=len(word)and word[t:t+4]=='RRRR':assert not comp(B,1,cursor(p,h))
     pp,hh=step(Bmin,p,h);p,h=step(B,p,h);assert(p,h)==(pp,hh)
    for M in(4,7):
     small,_=actual_property(seed,word,M);large,_=actual_property(set(seed)|extra,word,M)
     assert not large or small,(word,M,seed,extra)
    cases+=1
 source=P.parent/'kernel_cycle_lift_2026-10-24/cap7_word_budget_filters_certificate.json';J=json.loads(source.read_text());results=[{'word':w,**decide(w,7)}for w in J['remaining_words']];assert all(r['status']=='EXISTS_FINITE_BOARD'for r in results)
 out={'status':'AUTHOR_MINIMUM_BOARD_EQUIVALENCE_CONTROLS_PENDING_AUDIT','consistent_words_length_at_most8':consistent,'extra_background_tests':cases,'open_word_models':results,'scope':'Exact bare finite-word existence with upper active cap and empty first-return endpoints. Additional prescribed modules/resources are separate constraints.'};(P/'minimum_board_word_controls.json').write_text(json.dumps(out,indent=2)+'\n');print('consistent',consistent,'extra backgrounds',cases,'models',len(results))
