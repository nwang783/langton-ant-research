"""Actual foreign-to-foreign interval grammar, not an ant coverage theorem.
No immediate C before a later foreign; empty QF/BF intervals are retained.
"""
from pathlib import Path
from collections import Counter
import importlib.util,json,hashlib
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent

def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',ROOT/'word_stabilization/check_foreign_return_interfaces.py')
o=load('owner',ROOT/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return (*q,h)
def spell(packet):return ''.join(W[a]for a in packet)
def reader(packet,tick):
 offset=0
 for index,a in enumerate(packet):
  if tick<offset+len(W[a]):
   return dict(actual_atom_index0=index,atom=a,global_tick0=tick,actual_owner=o.describe(a,tick-offset))
  offset+=len(W[a])
 assert tick<offset+len(l.M)
 return dict(actual_atom_index0=None,atom='actual final M11 prefix',global_tick0=tick,actual_owner=o.describe(packet[-1],len(W[packet[-1]])+tick-offset))
def conflict(packet):
 trace=l.trace(spell(packet)+l.M);assert not trace['feasible']
 return dict(packet=packet,immutable_conflict=trace,previous_actual_reader=reader(packet,trace['previous_read']),new_actual_reader=reader(packet,trace['conflict_read']))
def control(packet,mass):
 raw=spell(packet);trace=l.trace(raw+l.M);assert trace['feasible']
 seed={q for q,(c,t)in trace['first'].items()if c=='L'};assert len(seed)==mass
 black=set(seed);p=(0,0,0)
 for c in raw+l.M:
  q=p[:2];assert(q in black)==(c=='L');black.symmetric_difference_update({q});p=after(c,p)
 return dict(packet=packet,complete_seed=sorted(seed),seed_mass=len(seed),actual_reads=len(raw)+len(l.M),RAW_EXIT=after(raw),after_actual_M_prefix=p,final_physical_mass=len(black))

leading=[]
for n in(1,2):
 for a in'FQB':
  for b in'FQB':leading.append(conflict(a+'C'*n+b))
assert len(leading)==18
triple=[conflict(a+'CCC')for a in'FQB']
# Same physical 24-pair table as signed735; we recheck it literally and
# import no FIRST-foreign ancestry assumption.
packets=('D','DC','V','VC','VCC','U','UC','UCC')
boundaries=[]
for packet in packets:
 for b in'FQB':
  trace=l.trace(spell(packet+b)+l.M)
  row=dict(last_actual_G8_packet=packet,next_foreign=b,feasible=trace['feasible'])
  if not trace['feasible']:row.update(conflict(packet+b))
  boundaries.append(row)
assert sum(r['feasible']for r in boundaries)==5
assert {(r['last_actual_G8_packet'],r['next_foreign'])for r in boundaries if r['feasible']}=={('V','F'),('V','Q'),('U','F'),('U','Q'),('U','B')}
# An empty ordinary interval is NOT excluded. QF/BF are full prepared
# positive controls, even though their immediate U prepends fail.
empty=[]
for a in'FQB':
 for b in'FQB':
  trace=l.trace(W[a]+W[b]+l.M)
  row=dict(packet=a+b,feasible=trace['feasible'])
  if not trace['feasible']:row.update(conflict(a+b))
  empty.append(row)
assert {r['packet']for r in empty if r['feasible']}=={'QF','BF'}
positives=[control('QF',34),control('BF',37),control('CF',19),control('CQ',20),control('CB',23)]
u_prepend=[conflict('UQF'),conflict('UBF')]
assert[(r['immutable_conflict']['conflict_read'],r['immutable_conflict']['previous_read'])for r in u_prepend]==[(110,2),(145,1)]
D=['ordinary_RAW_G8_base_cut_bridge_2026-10-24/manifest.json','audits/check_RAW_G8_base_cut_bridge_independent.json','ordinary_RAW_G8_base_cut_bridge_2026-10-24/nonterminal_cut_manifest.json','audits/check_RAW_G8_nonterminal_cut_independent.json','seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json','audits/check_complete8_foreign_adjacency_independent.json','word_stabilization/check_foreign_return_interfaces.py','literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
result=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Any actual complete foreign A, then an ordinary RAW word z over D/C/V/U, then a next actual complete foreign B with its real following M11. If z is nonempty, it contains a base and its actual last atom is plain V or U; the only possible last-packet/foreign boundaries are VF,VQ,UF,UQ,UB. If z is empty, QF/BF remain literal possibilities. No U-entry, initial-WHITE, simplicity, first-foreign or length-bound premise.',all18_no_base_one_two_C_interval_conflicts=leading,all3_leading_triple_C_conflicts=triple,all24_actual_G8_last_packet_foreign_pairs=boundaries,all9_empty_interval_pairs=empty,all5_prepared_full_field_scope_controls=positives,all2_immediate_U_prepend_conflicts_not_general_ancestry=u_prepend,
 all_length_parse_argument='If z has no D/V/U base, it is C^r. The actual A CCC+M conflicts exclude r>=3: the next actual word supplies M11, including D10 spill when relevant. The eighteen ACB/ACCB words exclude r=1,2. Thus a nonempty z has a first base. Take the SAME actual ordinary factor from that first base to the last atom of z. Its first D, if any, has an actual preceding seven-atom RAW: a leading C or A. Its terminal cut admits the actual next B RAW+M11. Signed8a plus signed7ae therefore parse this whole selected factor into genuine G8 packets, retaining own C tails and their physical contexts. Signed735 (literally rebuilt here) leaves only five last-packet boundaries, all plain V/U. No complete packet is invented at an internal C cut.',
 no_preceding_C_corollary='In particular, a foreign that has an earlier foreign in an actual G7 factor is never immediately preceded by C. In a factor beginning at an actual RAW U, the ordinary prefix before the first foreign also parses by the same nonterminal bridge, so that first boundary is one of the five allowed pairs too. Therefore no foreign in that actual U-entry G7 factor has immediate previous-C bit1. This is an exact restricted-word grammar consequence, not a new geometric induction or language-coverage theorem.',
 scope_controls='Prepared CF/CQ/CB remain legal without an earlier actual foreign/base history. Empty prepared QF/BF remain legal and are not assigned an ordinary predecessor. The failures of immediate UQF/UBF exclude only those fixed prepends, not every possible earlier U-entry ancestry.',
 not_claimed=['No foreign-pair or tag-state theorem is iterated.','No tangent-clock bound, global proxy simplicity, ant-trajectory coverage, capture or finite-state conclusion.','No exclusion of every genuine QF/BF ancestry.','A supplied M11 is an actual physical prefix, not a fabricated complete next packet.'],dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in D})
(HERE/'foreign_interval_grammar.json').write_text(json.dumps(result,indent=2)+'\n')
print('Foreign intervals:18 ACB/ACCB conflicts+3 leadingCCC; arbitrary nonempty intervals end plainV/U via actual G8 parse;5 allowed packet boundaries. EmptyQF/BF and rawCF/CQ/CB controls retained. No C before foreign in an actual U-entry G7 factor.')
