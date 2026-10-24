"""Exact causal exclusion of FIRST foreign B at(3,0,E) after genuine U.
Two proofs: forced-renewal fresh-star core collision; four actual predecessors.
No prefix enumeration, prepared ancestry, or permanence across foreign words.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
QP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json';GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
G=json.loads(QP.read_text())['macro_words'];G8=json.loads(GP.read_text())['geometry'];M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};L={(0,0),(0,1),(1,0),(1,1)};Z={(1,0),(1,1),(2,0),(2,1)};E={(2,0),(2,1)};V=((0,1),(1,0),(0,-1),(-1,0))
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def place(q,p,h):return add(p,rot(q,h))
def derive(w):
 p=(0,0);h=0;par=set();req={};reads={}
 for t,ch in enumerate(w):
  b=(ch=='L')^(p in par);assert p not in req or req[p]==b;req[p]=b;reads.setdefault(p,[]).append((t,ch));par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,V[h])
 return req,par,p,h,reads
assert{q for q,b in derive(M)[0].items()if b}==K
bp=(3,0);bh=1;BK={place(q,bp,bh)for q in K};assert BK=={(2,0),(2,1),(3,-1),(3,0),(3,1)}
assert E<=BK and not L&BK
breaker=(3,-1);newL={place(q,breaker,0)for q in L};assert newL=={(3,-1),(3,0),(4,-1),(4,0)}
assert BK&newL=={(3,-1),(3,0)}
for a in(7,8,9):
 outs={place(q,breaker,0)for q in G8[a]['outputs']};assert newL<=outs
 req,_,_,_,reads=derive(G8[a]['word']);assert all(t<len(G[3]['word'])for q in L for t,ch in reads[q])
 assert all(reads[q][-1][1]=='R'for q in L)
# Actual RAW marker reads in B confirm core ownership, rather than treating
# these old cycle cells as residual inputs or claiming the context misses Z.
breq,_,_,_,br=derive(G[6]['word']+M);core_reads=[]
for q in sorted(BK):
 local=rot(sub(q,bp),-bh);assert local in K and breq[local]
 core_reads.append(dict(global_cell=q,B_local_cell=local,reads=br[local],is_original_east_cycle=q in E,is_forced_breaker_star=q in newL))
# Independently check each possible ACTUAL atom immediately before B entry.
rows=[]
for i,name in((0,'D'),(2,'V'),(3,'U'),(1,'C')):
 _,_,ep,dh,_=derive(G[i]['word']);h=(bh-dh)%4;p=sub(bp,rot(ep,h));core={place(q,p,h)for q in K};req,_,_,_,reads=derive(G[i]['word']+M);white={place(q,p,h)for q,b in req.items()if not b}
 row=dict(atom=name,pose=[*p,h],endpoint=[*bp,bh],old_star_core_hits=sorted(core&L),old_star_before_white_hits=sorted(white&L))
 if name in'DV':assert core&L;row['exclusion']='old original star in predecessor entry core'
 elif name=='U':
  assert(p,h)==((-1,0),1)
  a=add((2*p[0],2*p[1]),rot((-1,-1),h));b=add(a,rot((0,8),h));assert(a,b)==((-3,1),(5,1))
  z=(-1,1);assert z==add(a,(2,0));assert z==add((-1,-1),(0,2))
  row.update(exclusion='strict crossing with creating U chord inside preforeign simple-eight path',predecessor_chord=[a,b],creating_U_chord=[(-1,-1),(-1,7)],contact=z,source_parameter='1/4',predecessor_parameter='1/4')
 else:
  assert(p,h)==((3,1),2)
  for q,ph,local in(((1,0),7,(2,1)),((1,1),8,(2,0))):
   assert place(local,p,h)==q and req[local]is False and reads[local][0]==(ph,'R')
  assert{(1,0),(1,1)}<=white&L;row['exclusion']='predecessor C requires permanent original star WHITE'
 rows.append(row)
assert[(r['atom'],r['pose'])for r in rows]==[('D',[2,1,1]),('V',[0,1,1]),('U',[-1,0,1]),('C',[3,1,2])]
D=[QP,GP,Path(__file__).resolve()]+[R/'core_periodicity_new'/x/'manifest.json'for x in('causal_cycle_renewal_20261023_1841','U_left_star_permanence_frozen_20261023_1918','U_entry_simplicity_frozen_20261023_1616')]+[R/'seven_word_return_bridge_2026-10-23/manifest.json']
out=dict(status='AUTHOR_ALL_HISTORY_FIRST_FOREIGN_B_CORE_GUARD_PENDING_INDEPENDENT_AUDIT',scope='A genuine creating U/UC/UCC, followed by any uninterrupted retained-eight interval, cannot have its FIRST foreign word B enter at(3,0,E). All C ages, arbitrary finite-entry board, and actual creator birth tags covered. No permanence or simplicity is used after the first foreign begins. No global seven-word termination claim.',foreign_B_pose=[3,0,1],actual_B_entry_core=sorted(BK),original_U_east_ids=sorted(E),forced_genuine_first_breaker_pose=[3,-1,0],forced_breaker_fresh_star=sorted(newL),forced_breaker_star_core_collision=sorted(BK&newL),B_core_raw_reads=core_reads,immediate_predecessor_rows=rows,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'B_core_guard.json').write_text(json.dumps(out,indent=2)+'\n');print('Firstforeign B(3,0,E) excluded at ALL clocks: causal coreguard and4 predecessor cases')
