from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23';vec={'E':1+0j,'W':-1+0j,'N':1j,'S':-1j};nm={v:k for k,v in vec.items()};rows=[];roots=[];targets=[]
for n in range(1,5):
 for hs in product('EW',repeat=n):
  hs=''.join(hs);ins=[vec[h]for h in hs];outs=[v*(-1j if i%2==0 else 1j)for i,v in enumerate(ins)];ci=Counter(ins);co=Counter(outs)
  rE=hs[::2].count('E');rW=hs[::2].count('W');a=-max(rE,rW);C={'N':rW+a,'S':rE+a}
  if 3 in ci.values()and 3 in co.values():
   hi=next(v for v,c in ci.items()if c==3);ho=next(v for v,c in co.items()if c==3);ti=[i for i,v in enumerate(ins)if v==hi];to=[i for i,v in enumerate(outs)if v==ho];si=[i for i in range(n)if i not in ti];so=[i for i in range(n)if i not in to];assert n==4 and len(si)==len(so)==1
   turn='LEFT'if ho==1j*hi else'RIGHT';assert ho in(1j*hi,-1j*hi)
   first=[i for i in si if i in to and i==min(to)];last=[i for i in so if i in ti and i==max(ti)]
   assert 0 in ti or 0 in to;assert 3 in ti or 3 in to
   # Relative incoming E normal form: the two non-cycle ports are E plus
   # the opposite outgoing direction, both in the same open side component.
   unused={-ins[si[0]]/hi,outs[so[0]]/hi}
   assert unused==({1,-1j}if turn=='LEFT'else{1,1j})
   if first:assert first==[0]and turn=='LEFT'and hs[0]!=hs[1]==hs[2]==hs[3]
   if last:assert last==[3]and turn=='RIGHT'and hs[0]==hs[2]==hs[3]!=hs[1]
   rows.append(dict(headings=hs,triple_input=nm[hi],triple_output=nm[ho],turn=turn,input_ranks=ti,output_ranks=to,single_input=si,single_output=so,single_side='RIGHT'if turn=='LEFT'else'LEFT',eligible_first=first,eligible_last=last))
  if n>=3 and hs[0]==hs[2]:
   ordinal=sum(v==outs[1]for v in outs[:2]);label=C[nm[outs[1]]]-ordinal+1
   if label==-1:
    assert hs[1]!=hs[0]and ordinal==2 and outs[0]==outs[1]==outs[2]and co[outs[1]]in(3,4)
    roots.append(dict(headings=hs,L1_output=nm[outs[1]],ordinal=ordinal,port_count=co[outs[1]],sheet_relative_M=label))
  if ci[1]>=3:
   rank=[i for i,v in enumerate(ins)if v==1][1];assert rank in(1,2);targets.append(dict(headings=hs,port_count=ci[1],second_rank=rank))
assert len(rows)==8 and sum(bool(r['eligible_first'])for r in rows)==2 and sum(bool(r['eligible_last'])for r in rows)==2 and len(roots)==len(targets)==6
# Compare freshly generated physical data, without importing saved local rows.
a=json.loads((D/'triple_use_cycle_first_last_crossing_table.json').read_text())['rows']
for r,s in zip(rows,a):
 assert(r['headings'],r['input_ranks'],r['output_ranks'],r['eligible_first'],r['eligible_last'])==(s['headings'],s['triple_input_ranks'],s['triple_output_ranks'],s['eligible_first_edge_departure'],s['eligible_last_edge_arrival'])
b=json.loads((D/'max_RIGHT_penultimate_leaf_second_exchange.json').read_text());assert [r['headings']for r in roots]==[r['headings']for r in b['roots']]and[r['headings']for r in targets]==[r['headings']for r in b['targets']]
files=['triple_use_cycles_cannot_be_contractible.md','triple_use_cycle_first_last_crossing_table.py','triple_use_cycle_first_last_crossing_table.json','max_RIGHT_penultimate_graph_leaves_are_impossible.md','max_RIGHT_penultimate_leaf_second_exchange.py','max_RIGHT_penultimate_leaf_second_exchange.json','triple_use_current_pairs_top_same_R_outputs.md','max_turn_leaf_stock_balance.md','penultimate_leaf_top_R0_supplier_capacity.md'];hashes={f:hashlib.sha256((D/f).read_bytes()).hexdigest()for f in files};assert hashes[files[0]].startswith('5036e7c2')and hashes[files[3]].startswith('b1ae9995')
out={'status':'PASS no finite physical G3 cycle and independent restricted max-RIGHT penultimate graph-leaf obstruction','source_hashes':hashes,'fresh_eight_G3_internal_histories':rows,'six_root_histories':roots,'six_target_histories':targets,'G3_analytic':['Complete WHITE cap4 at each cell gives one fixed incoming axis; physical edges have one possible traversal direction by the checker/heading-axis invariant. Each internal G3 vertex has two distinct adjacent ports, one triple input and one triple output. A finite directed component cycle is a simple embedded unit-square-lattice Jordan curve, not a chronological itinerary.','At the earliest cycle-edge departure the source read must use the single input and have no earlier triple output. Fresh full inventory leaves only LEFT WEEE R0 (and rotations), arriving from the open RIGHT side. Every boundary R0 uses a cycle edge, so there can be no strictly earlier boundary read, including at the other end of an unused chord. The past path cannot cross a unit edge interior.','At the last cycle-edge arrival the target read must use the single output and have no later triple input. Only RIGHT EWEE L3 survives; it departs into the open LEFT side. Every boundary L3 uses a cycle edge, so no later boundary read is possible; unused chords cannot escape the condition. The actual arrival read is one update after the latest edge departure, and the subsequent single-edge departure is not mislabeled as a cycle traversal.','A clockwise finite cycle would force the complete past to remain in its bounded RIGHT interior; a counterclockwise cycle would trap the complete future in its bounded LEFT interior. Bi-infinite nonzero translation excludes both. Essential quotient cycles have infinite lifts and no global first/last traversal, so are retained.'],'leaf_analytic':['The old restricted premise is a CONTRACTIBLE repaired sheet M-1 GRAPH LEAF, with multiedge incidence retained, sole root a max-C RIGHT corner with same R headings. The independently signed bridge clock ell±Delta=0 forces the outgoing-L1 side; no generic leaf or nonleaf stock hole is included.','Fresh same-R local sheet labels show every outgoing L1 at M-1 is the second departure on a physical port used three or four times. Literal chronological matching makes its arrival at the neighbor the second use of that input port. With at most four complete WHITE reads and at least three same-heading inputs, this is rank1 or2, never rank0 or3.','The repaired cycle containing that incoming occurrence is genuinely incident to the neighbor L1/R2 transposition: both ranks are precisely the two exchanged arrivals; their canonical outputs lie on adjacent distinct sheets. It is not an unchanged R0/L3 corner or an exchange self-loop.','The root and neighbor are physical nearest neighbors of opposite checker parity. Full heading-restoring period has even P, hence drift parity even; they cannot represent the same full-quotient cell class. Their exchange edges are distinct even if they connect the same pair of canonical cycles. Thus degree at least2 contradicts the graph-leaf premise.','This leaf proof is independent of the G3 contractibility result and needs no K1 or zero-output assumption. Earlier restricted leaf capacity bounds remain true but vacuous. It does not remove general contractible sheet cycles or nonleaf stock holes.'],'scope':'Complete WHITE cap4 translating fronts with actual full period/drift. No initial-fuel charge, new period cost, whole-front exclusion, standard classification or universal capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
