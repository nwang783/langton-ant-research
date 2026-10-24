"""Explicit SAT models for the23 supplied open words; no external solver."""
from symbolic_capped_word import *
from pathlib import Path
import json,hashlib
P=Path(__file__).parent;SRC=P.parent/'kernel_cycle_lift_2026-10-24/cap7_word_budget_filters_certificate.json';J=json.loads(SRC.read_text());rows={r['word']:r for r in J['first_return_unit_propagation']};out=[]
for word in J['remaining_words']:
 r=rows[word];seed=set(map(tuple,r['first_L_minimal_seed']))|set(map(tuple,r['forced_unread_initial_black']));C=build(word,7);val=C.assignment(seed);model=verify_model(C,val)
 packed=bytearray((C.n+7)//8)
 for v in range(1,C.n+1):
  if val[v]:packed[(v-1)//8]|=1<<((v-1)%8)
 # Decode independently of gate evaluation and check each literal clause again.
 decode={v:bool(packed[(v-1)//8]>>(v-1)%8&1)for v in range(1,C.n+1)};assert C.check(decode)
 out.append({'word':word,'cap':7,'finite_seed':model['finite_seed'],'variables':C.n,'initial_board_bits':len(C.inputs),'clauses':len(C.clauses),'packed_assignment_hex':packed.hex(),'complete_board_replay':model['trace']})
report={'status':'EXPLICIT_SAT_MODELS_ALL_23_SUPPLIED_WORDS_AUTHOR_PENDING_AUDIT','source_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),'builder_sha256':hashlib.sha256((P/'symbolic_capped_word.py').read_bytes()).hexdigest(),'models':out,'scope':'Each word has an exact finite-board capped first-return witness. No claim of adjacent-word compatibility, indefinite continuation or highway capture.'};(P/'cap7_word_cnf_models.json').write_text(json.dumps(report,indent=2)+'\n');print('explicit models',len(out),'maxvariables',max(r['variables']for r in out),'maxblackseed',max(len(r['finite_seed'])for r in out))
