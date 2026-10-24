from pathlib import Path
from itertools import product
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'DISCONNECTED_C_LADDER_KINEMATIC_ATTEMPT.md';JF=D/'disconnected_C_ladder_attempt_certificate.json';assert sha(P)=='bfca6d57f60529bf02e3668435eff4bb1bf54e4ffbca012fcf51efaceef460d7'and sha(JF)=='b5beb093dd99d317bb2c73386bf6bcc3b07b58d29d88d721ef2f6e626974a505'and sha(D/'certify_disconnected_C_ladder_attempt.py')=='9df97d272c81a5c445cd29bc5c6e40b759f815fce6f158c77aa9e1bd4ea2745d';J=json.loads(JF.read_text())
for f,h in J['dependency_hashes'].items():assert sha(D/f)==h
C=[complex(*p)for p in J['C_lattice_path']];N=17;d=1+0j;physical=lambda q:complex(q.real-q.imag,q.real+q.imag-1);V=[1j,1,-1j,-1];off=[-1j,-1-1j,-1,0j];xy=lambda p:[int(p.real),int(p.imag)]
def face(t):
 k,i=divmod(t,N);return C[i]+k*d
assert len(C)==18 and C[-1]==C[0]+d and all(abs(b-a)==1 for a,b in zip(C,C[1:]))and all(face(t-1)!=face(t+1)for t in range(N))
assert [xy(physical(q))for q in C]==J['physical_C_faces'];rows={}
for y in sorted(set(int(q.imag)for q in C[:-1])):
 times=sorted(t-N*int(q.real)for t,q in enumerate(C[:-1])if q.imag==y);a,b=times[0],times[-1];u=face(a-1);v=face(b+1);assert face(a)==face(b)==y*1j
 row=dict(row=y,first_C_index=a,last_C_index=b,first_occurrence_phase=a%N,last_occurrence_phase=b%N,first_parent_row=int(u.imag),first_parent_voltage=int(u.real),last_successor_row=int(v.imag),last_successor_voltage=int(v.real));assert row==next(r for r in J['abstract_first_last_forests']if r['row']==y);rows[y]=row
edges={y:set()for y in rows}
for y,r in rows.items():
 for v in[r['first_parent_row'],r['last_successor_row']]:edges[y].add(v);edges[v].add(y)
seen=set();comp=[]
for y in sorted(rows):
 if y in seen:continue
 stack=[y];c=set()
 while stack:
  v=stack.pop()
  if v in c:continue
  c.add(v);stack.extend(edges[v]-c)
 seen|=c;comp.append(sorted(c))
assert comp==J['abstract_union_components']==[[-1,0],[1,2]]
p=1+0j;h=1;ks=[]
for q0,q1 in zip(C,C[1:]):
 assert p+off[h]==physical(q0);k=0
 while True:
  hh=(h-1)%4;pp=p+V[hh]
  if pp+off[hh]==physical(q1):break
  h=(h+1)%4;p+=V[h];k+=1;assert k<=3
 ks.append(k);p,h=pp,hh
assert ks==J['minimal_R_exponents']and(p,h)==(2+1j,1);opt=[i for i,k in enumerate(ks)if k==0];assert opt==J['optional_four_R_blocks']and len(opt)==9 and sum(ks)+17==30
leaves=J['six_leaf_complete_color_cover'];prefixes=[r['bit_prefix']for r in leaves];assert prefixes==[[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],[0,1],[1]]
for row in leaves:
 ev=row['all_legal_prefix_reads'];seed={complex(*e['position'])for j,e in enumerate(ev)if e['turn']=='L'and all(f['position']!=e['position']for f in ev[:j])};assert sorted(map(xy,seed))==row['full_minimal_initial_BLACK'];B=set(seed);p=1+0j;h=1;last={}
 for t,e in enumerate(ev):
  assert e['time']==t and e['position']==xy(p)and e['heading']==h;actual='L'if p in B else'R';assert e['turn']==actual;last[p]=e;B.symmetric_difference_update({p});h=(h+(1 if actual=='R'else-1))%4;p+=V[h]
 earlier,bad=row['consecutive_same_turn_witness'];assert last[p]==earlier and bad['position']==xy(p)and bad['time']==len(ev)and bad['turn']==earlier['turn'];assert row['actual_required_turn']==('L'if p in B else'R')!=bad['turn']and row['head_at_failure']==xy(p)and row['heading_at_failure']==h and row['full_BLACK_at_failure']==sorted(map(xy,B));assert row['covered_full_choices']==2**(9-len(row['bit_prefix']))
for bits in product([0,1],repeat=9):
 row=next(r for r in leaves if list(bits[:len(r['bit_prefix'])])==r['bit_prefix']);assert sum(list(bits[:len(r['bit_prefix'])])==r['bit_prefix']for r in leaves)==1;ex=ks[:]
 for i,b in zip(opt,bits):ex[i]=4*b
 p=1+0j;h=1;rr=[];last={};firstbad=None
 for i,k in enumerate(ex):
  for c in'R'*k+'L':
   assert p+off[h]==physical(C[i]);t=len(rr);e=dict(time=t,position=xy(p),heading=h,turn=c,C_step_block=i)
   if p in last and last[p]['turn']==c and firstbad is None:firstbad=(last[p],e)
   last[p]=e;rr.append(e);h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 assert(p,h)==(2+1j,1)and len(rr)==30+4*sum(bits);assert list(firstbad)==row['consecutive_same_turn_witness'];assert rr[:firstbad[1]['time']]==row['all_legal_prefix_reads']
O=dict(status='PASS geometric disconnected-union countermodel and complete color exclusion of ONE fixed17-C-step realization family; NOT an actual ant counterexample',proof=sha(P),certificate=sha(JF),script=sha(S),abstract_components=comp,minimal_R_counts=ks,optional_laps=opt,complete_choices=512,six_prefixes=prefixes,analytic_review=[
'The embedded four-row C-lattice walk and seam are nearest-neighbor/nonbacktracking. Exact FULL drift(1,1) first/last occurrence arrays reconstruct two disconnected extremal-forest components. These times are C-transition indices, not ant clocks; pureR stays preserve vertex order but change the period.',
'The specified incoming C edge uniquely fixes the actual head/heading after its L, including the seam. R stays cycle four corners; each desired next C move therefore allows a fixed R count modulo4. Five consecutiveR are impossible on any board because the fourth restores headpose after flipping its initialcellBLACK. Hence each positive minimal count1/2 is forced and each zero permits only0/4. This exhausts exactly512 expansions of this one geometry, with periods30+4b, not a bounded arbitrary-word search.',
'Fresh independent replay confirms all512 kinematic words and their exact first immutable same-cell repeated-turn failures, covered by six disjoint prefix leaves. Every leaf legalprefix has its complete finite minimal seed and entire field at failure reconstructed; unread outside bits cannot repair a repeated read. Thus no expansion is even an actual finite ant factor.',
'Planarity, nonbacktracking and cursor geometry alone do not force unionconnectivity. Actual ant colors reject this particular attempt, not every disconnected pattern. No actual disconnected-front counterexample, general connectivity theorem, controller module forcing, WHITE lifetimeS1 or capture follows.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
