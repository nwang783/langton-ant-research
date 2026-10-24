"""Four literal controls for the UNIVERSAL saturated-port S/T lemma.
Universality is proved separately; these controls alone would not establish it.
"""
from active_flight import *
from pathlib import Path
import json
P=Path(__file__).parent
WORDS={'S':'RRRRLRLRL','T':'RRRRLLLLRLRL'}
BASE={'S':{(-1,-1),(-1,1),(-2,2)},'T':{(-1,-1),(-1,0),(2,1)}}
CONNECT={'S':(-3,1),'T':(1,2)}
def components(B):
 left=set(B);out=[]
 while left:
  q=min(left);D=comp(B,1,ends(q,1)[0]);out.append(D);left-=D
 return out
def small_count(B):return sum(1 for D in components(B)if len(D)<=2)
def run(Y,Z):
 seed=BASE[Y]|({CONNECT[Y]}if Z=='T'else set());B=set(seed);p=(0,0);h=0;trace=[];events=[];birth={q:'PREEXISTING_UNREAD_UNTIL_CONSUMED'for q in B}
 for t in range(len(WORDS[Y])+1):
  C=comp(B,1,cursor(p,h));trace.append({'t':t,'pose':[p,h],'field':sorted(B),'active':sorted(C),'components':[sorted(D)for D in components(B)]})
  assert len(C)<=7
  if t in(0,len(WORDS[Y])):assert not C
  else:assert C
  if t==len(WORDS[Y]):break
  old=set(C);q=p;c='L'if q in B else'R';assert c==WORDS[Y][t];p,h=step(B,p,h);N=comp(B,1,cursor(p,h))
  if c=='R':
   imported=N-old-{q};birth[q]=t
   if imported:events.append({'t':t,'kind':'R_IMPORT','complete_component':sorted(imported),'prior_births':{str(z):birth[z]for z in imported}})
  else:
   emitted=old-{q}-N;consumed=birth.pop(q)
   if emitted:events.append({'t':t,'kind':'L_EMIT','complete_component':sorted(emitted),'births':{str(z):birth[z]for z in emitted}})
 final_hook=(p[0]+rot((-1,-1),h)[0],p[1]+rot((-1,-1),h)[1]);assert final_hook in B
 expected_hook={final_hook}
 if Z=='T':expected_hook.add(CONNECT[Y])
 assert comp(B,1,ends(final_hook,1)[0])==expected_hook
 before,after=small_count(seed),small_count(B);want={('S','S'):1,('S','T'):2,('T','S'):0,('T','T'):1}[Y,Z];assert before-after==want
 return {'current_word':Y,'successor_word':Z,'turn_word':WORDS[Y],'initial_field':sorted(seed),'full_trace':trace,'events':events,'final_hook_component':sorted(expected_hook),'small_components_before':before,'small_components_after':after,'small_component_drop':want,'maximum_active_mass':max(len(q['active'])for q in trace)}
out={'status':'AUTHOR_FOUR_FULL_FIELD_CONTROLS_PENDING_AUDIT','scope':'Representative fields of universally pinned interior profiles; arbitrary-exterior pinning is the separate proof, not inferred from these controls.','profiles':[run(Y,Z)for Y in'ST'for Z in'ST']};(P/'st_interior_ledger_controls.json').write_text(json.dumps(out,indent=2)+'\n');print([(r['current_word']+r['successor_word'],r['small_component_drop'])for r in out['profiles']])
