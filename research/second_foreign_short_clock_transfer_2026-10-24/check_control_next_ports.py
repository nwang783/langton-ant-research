"""Exactly21 prescribed next-word ports of three real two-foreign controls.
'No next complete7' is not physical termination; actual M11 may already
contain a shorter RAW such as D10 whose own M11 later fails.
"""
from pathlib import Path
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h

def spell(s):return ''.join(W[a]for a in s)
basejson=json.loads((H/'second_foreign_transfer.json').read_text());controls={q['word']:q for q in basejson['all3_genuine_complete_two_FOREIGN_positive_controls']};rows=[];positives=[]
for base in['UQUF','UBVF','UBUF']:
 raw=spell(base);bt=l.trace(raw+l.M);assert bt['feasible'];sourceU=l.trace(W['U'])
 for a in'DCVUFQB':
  full=raw+W[a]+l.M;t=l.trace(full)
  if not t['feasible']:
   off=t['conflict_read']-len(raw);assert 0<=off<len(W[a])+11 and t['previous_read']<len(W['U']);cell=tuple(t['cell']);old=sourceU['last'][cell];assert old[1]==t['previous_read']
   before=l.trace(full[:t['conflict_read']]);assert before['feasible']and before['last'][cell]==old
   q=dict(base_control=base,actual_next_atom=a,feasible=False,immutable_conflict=t,actual_next_owner=o.describe(a,off),original_U_source_last_read=dict(cell=cell,own_tick0=old[1],own_read_number1=old[1]+1,turn=old[0],state='WHITE hole after actual L'if old[0]=='L'else'SAME BLACK source-R identity'),no_intermediate_visit_since_initial_U=True)
  else:
   assert(base,a)==('UBUF','D');seed={p for p,(c,k)in t['first'].items()if c=='L'};oldseed=set(map(tuple,controls[base]['complete_seed']));assert seed-oldseed=={(1,-2)}and oldseed<=seed and(1,-2)not in bt['first'];B={p:('initial',p)for p in seed};p=(0,0,0);tick=0
   for c in raw+W[a]+l.M:
    cell=p[:2];assert(cell in B)==(c=='L')
    if c=='L':del B[cell]
    else:B[cell]=tick
    p=after(c,p);tick+=1
   q=dict(base_control=base,actual_next_atom=a,feasible=True,complete_seed=sorted(seed),seed_mass=len(seed),all_physical_reads=tick,extra_initial_unread_BLACK_for_this_extension=(1,-2),extra_cell_first_actual_read=t['first'][(1,-2)],same47_board_not_claimed_to_continue=True,statement='This48-cell complete field executes UBUFD+actualM. It differs from the47-cell base control by one cell genuinely unread through that base plus its suppliedM. No retcon to an already-executed47-cell board is asserted.');positives.append(q)
  rows.append(q)
assert len(rows)==21 and len(positives)==1 and positives[0]['seed_mass']==48
for base in['UQUF','UBVF']:
 rs=[q for q in rows if q['base_control']==base];assert all(not q['feasible']for q in rs)
 for q in rs:
  a=q['actual_next_atom'];f=q['immutable_conflict'];off=f['conflict_read']-len(spell(base))
  assert(f['previous_read'],tuple(f['cell']),f['turn'],off)==((3,(0,-1),'L',11)if a=='D'else(4,(0,0),'R',12)if a in'CV'else(1,(-1,0),'L',13))
D=[H/'manifest.json',R/'audits/check_second_foreign_short_clock_independent.json',R/'word_stabilization/check_foreign_return_interfaces.py',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Only21 prescribed immediate next COMPLETE seven-atom RAW+actualM ports of the three actual twoforeign controls. No continuation tree or arbitrary-depth claim.',all21_prescribed_next_ports=rows,exact_port_obligation='UQUF andUBVF have unchanged initial-U holes(0,-1)L3 and(-1,0)L1 plus SAME r(0,0)R4. NextD needs firstholeBLACK at marker-owned read2; nextC/V need rWHITE at ownR12; nextU/F/Q/B need secondholeBLACK at ownL13. Every target fails with no intermediatevisit.',marker_qualification='The source control already has11 actual continuation readsM. They do not constitute a complete NEXT7 RAW+itsOWN M. In particular D10 may be physically executed inside those11 reads, then its own marker read2 fails. Maximal retained7 factor is not physical ant termination.',one_real_48_cell_extension=positives[0],not_claimed=['No arbitrary twoforeign reserve or repeatable return state.','No48-cell behavior attributed to the original47-cell seed.','No physical trajectory termination or global attraction.','No other histories at the same pose are excluded.'],dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'control_next_ports.json').write_text(json.dumps(out,indent=2)+'\n');print('TwoFORE controls nextports:UQUF/UBVF all7 immutable debts; UBUF onlyD via48-cell field with one genuinely unread added root.21 prescribed tests, not physical termination.')
