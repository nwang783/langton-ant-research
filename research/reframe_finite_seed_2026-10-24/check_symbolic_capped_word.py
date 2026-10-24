"""Author independent-formulation controls: CNF gates versus literal full board."""
from symbolic_capped_word import *
from itertools import combinations
import random,hashlib
P=Path(__file__).parent;rng=random.Random(620247);checks=0;positive=[]
fixtures=[('RRRRL',4,set()),('RRRRLRL',5,{(-1,1)}),('RRRRLRLRL',6,{(-1,1),(-2,2)}),('RRRRLRLRRL',6,{(-1,1),(-1,2)}),('RRRRLRLRLRL',7,{(-i,i)for i in range(1,4)})]
for word,M,seed in fixtures:
 C=build(word,M);val=C.assignment(seed);assert C.check(val);model=verify_model(C,val)
 positive.append({'word':word,'cap':M,'model':model,'variables':C.n,'initial_board_bits':len(C.inputs),'clauses':len(C.clauses)})
 tests=[]
 if M==4:
  box=[(x,y)for x in range(-1,2)for y in range(-1,2)]
  tests +=[{q for i,q in enumerate(box)if mask>>i&1}for mask in range(1<<len(box))]
 else:
  box=[(x,y)for x in range(-4,5)for y in range(-4,5)]
  tests +=[set(rng.sample(box,rng.randrange(15)))for _ in range(100)]
 # Far unread archives must not be dropped from actual replay, but cannot affect cap.
 tests +=[set(seed)|{(100+j,100-j)for j in range(8)}, {(-i,i)for i in range(1,M+9)}]
 for B in tests:
  got=C.check(C.assignment(B));want,trace=actual_property(B,word,M);assert got==want,(word,M,B,got,want)
  checks+=1
 # Require both satisfiable-model clauses and every full-board intermediate field.
 val=C.assignment(seed);assert all(val[z] in(False,True)for z in range(1,C.n+1))
# Build longest grammar word, without calling any solver or expanding profiles.
Q=json.loads((P/'cap7_turn_word_quotient.json').read_text());word=max(Q['word_counts'],key=lambda w:(len(w),w));C=build(word,7);C.write_dimacs(P/'cap7_longest_word.cnf');meta={'word':word,'cap':7,'variables':C.n,'initial_board_bits':len(C.inputs),'clauses':len(C.clauses),'input_map':[{'cell':q,'variable':z}for q,z in sorted(C.inputs.items())],'cuts':C.cuts,'solver_status':'NOT_RUN'};(P/'cap7_longest_word_cnf_map.json').write_text(json.dumps(meta,indent=2)+'\n')
out={'status':'AUTHOR_CNF_EQUIVALENCE_CONTROLS_PENDING_INDEPENDENT_AUDIT','board_assignments_checked':checks,'positive_models':positive,'longest_word_circuit':{k:v for k,v in meta.items()if k not in('input_map','cuts')},'scope':'Finite exact fixed-word capped-first-return formula. No SAT/UNSAT conclusion for the longest word and no global decision procedure.'};(P/'symbolic_capped_word_controls.json').write_text(json.dumps(out,indent=2)+'\n');print('controls',checks,'longest',{k:v for k,v in meta.items()if k not in('input_map','cuts')})
