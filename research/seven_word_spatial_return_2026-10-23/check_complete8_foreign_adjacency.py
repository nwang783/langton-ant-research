"""All 24 literal complete-eight -> F/Q/B adjacency contracts.
A finite prescribed pair table, not a trajectory-prefix search.
"""
from pathlib import Path
from collections import Counter
import hashlib,json
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';WP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
G=json.loads(GP.read_text())['geometry'];G7=json.loads(WP.read_text())['macro_words'];M=G[0]['marker'];V=((0,1),(1,0),(0,-1),(-1,0));K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}
C=G7[1]['word'];assert C==G[1]['word'][len(G[0]['word']):]
for a,base,tails in((0,0,0),(1,0,1),(4,2,0),(5,2,1),(6,2,2),(7,3,0),(8,3,1),(9,3,2)):
 assert G[a]['word']==G7[base]['word']+tails*C
rows=[]
for a in(0,1,4,5,6,7,8,9):
 for f in(4,5,6):
  source=G[a]['word'];fw=G7[f]['word'];word=source+fw+M;p=(0,0);h=0;par=set();req={};reads={};conflict=None;rawforeignexit=None
  for t,ch in enumerate(word):
   bit=(ch=='L')^(p in par)
   if p in req and req[p]!=bit:
    actual=req[p]^(p in par)
    conflict=dict(global_tick=t,foreign_phase=t-len(source),cell=p,proposed_turn=ch,forced_actual_turn='L'if actual else'R',previous_reads=reads[p],first_initial_color=req[p],conflicting_initial_color=bit)
    break
   req[p]=bit;reads.setdefault(p,[]).append((t,ch));par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=p[0]+V[h][0],p[1]+V[h][1]
   if t+1==len(source)+len(fw):rawforeignexit=dict(head=p,heading=h)
  row=dict(source=G[a]['name'],foreign='FQB'[f-4],source_RAW_length=len(source),foreign_RAW_length=len(fw),status='IMPOSSIBLE_LITERAL_PAIR'if conflict else'PREPARED_FINITE_PAIR_ATTAINED',conflict=conflict)
  if conflict:
   assert 0<=conflict['foreign_phase']<len(fw), 'Every rejection occurs in actual foreign RAW, not speculative marker ownership.'
  else:
   seed={q for q,b in req.items()if b};assert K<=seed
   board=set(seed);q=(0,0);hh=0
   for tick,ch in enumerate(word):
    assert(ch=='L')==(q in board);board.symmetric_difference_update({q});hh=(hh+(-1 if ch=='L'else 1))%4;q=q[0]+V[hh][0],q[1]+V[hh][1]
   assert q==p and hh==h
   row.update(prepared_seed=sorted(seed),seed_mass=len(seed),raw_foreign_exit=rawforeignexit,scope='Actual finite source+foreign+true M11 pair only; arbitrary incoming source history or graph class not certified.')
  rows.append(row)
legal=[(r['source'],r['foreign'])for r in rows if r['conflict']is None]
assert legal==[('V','F'),('V','Q'),('U','F'),('U','Q'),('U','B')]
expected={'D':43,'DC':16,'VC':37,'VCC':12,'UC':38,'UCC':12}
for row in rows:
 if row['source']in expected:assert row['conflict']['foreign_phase']==expected[row['source']]
 if row['source']=='V'and row['foreign']=='B':assert row['conflict']['foreign_phase']==59
D=[GP,WP,H/'foreign_kinked_barrier_manifest.json',R/'foreign_U_port_interfaces_2026-10-23/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_AUDIT',scope='Exact local adjacency of every complete-eight packet and each F/Q/B, with true M11 supplied. Every rejected pair has an immutable contradiction in foreign RAW. A first foreign after a complete-eight interval can only follow plain V(F/Q) or plain U(F/Q/B), hence never follows an atomic C. No arbitrary raw CF exclusion or global language coverage.',rows=rows,locally_attained_pairs=legal,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'complete8_foreign_adjacency.json').write_text(json.dumps(o,indent=2)+'\n')
print('24 exact pairs: 19 impossible in foreign RAW; only V->F/Q and U->F/Q/B locally attained. First foreign after complete8 always has previous-C bit zero.')
