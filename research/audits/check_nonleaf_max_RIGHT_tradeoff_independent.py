from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23';v={'E':1+0j,'W':-1+0j,'N':1j,'S':-1j};name={z:k for k,z in v.items()};allrows=[];rights=[];triples=[]
for n in range(1,5):
 for word in product('EW',repeat=n):
  h=''.join(word);rs=Counter(h[::2]);shift=-max(rs['E'],rs['W']);csw=rs['E']+shift;cne=rs['W']+shift;inc=Counter();out=Counter();events=[]
  for i,z in enumerate(h):
   o=name[v[z]*(-1j if i%2==0 else 1j)];inc[z]+=1;out[o]+=1
   il=(csw if z=='E'else cne)-inc[z]+1;ol=(csw if o=='S'else cne)-out[o]+1
   events.append({'rank':i,'in':z,'out':o,'in_ordinal':inc[z],'out_ordinal':out[o],'in_level':il,'out_level':ol})
  for i,e in enumerate(events):
   partner=3-i if n>=3 and i in(1,2)else i
   assert e['in_level']==events[partner]['out_level']
  if n>=3 and h[0]==h[2]:
   ei=next(e for e in events if e['in_level']==-1);eo=next(e for e in events if e['out_level']==-1);assert{ei['rank'],eo['rank']}=={1,2}
   ports=[('in',z,c)for z,c in inc.items()if c>=3]+[('out',z,c)for z,c in out.items()if c>=3];assert ports
   assert any((ei['in']==z and ei['in_ordinal']==2)if side=='in'else(eo['out']==z and eo['out_ordinal']==2)for side,z,c in ports)
   rights.append({'word':h,'middle_in':ei,'middle_out':eo,'high_ports':ports})
  ii=next((z for z,c in inc.items()if c==3),None);oo=next((z for z,c in out.items()if c==3),None)
  if ii or oo:
   ei=next((e for e in events if e['in']==ii and e['in_ordinal']==2),None);eo=next((e for e in events if e['out']==oo and e['out_ordinal']==2),None)
   if ei and eo:assert ei['rank']+eo['rank']==3 and ei['in_level']==eo['out_level']==-1;kind='internal'
   elif ei:
    e=events[3-ei['rank']];assert ei['in_level']==e['out_level']==-1 and out[e['out']]==2 and e['out_ordinal']==2;kind='sink'
   else:
    e=events[3-eo['rank']];assert eo['out_level']==e['in_level']==-1 and inc[e['in']]==2 and e['in_ordinal']==2;kind='source'
   triples.append({'word':h,'type':kind,'middle_input_rank':ei['rank']if ei else None,'middle_output_rank':eo['rank']if eo else None})
  assert sum(c==4 for c in inc.values())+sum(c==4 for c in out.values())<=1
  allrows.append((h,events,inc,out))
assert len(rights)==12 and len(triples)==12
source=next(e for h,e,ic,oc in allrows if h=='EWEW');targetE=next(e for h,e,ic,oc in allrows if h=='EEEE')
# Quarter rotate target EEEE to actual SSSS. Levels and ranks do not change.
for r in range(4):assert source[r]['out']=='S'and source[r]['out_level']==targetE[r]['in_level']==-r
assert source[1]['out_level']==targetE[2]['out_level']==-1 and source[2]['out_level']==targetE[1]['out_level']==-2
saved=json.loads((D/'max_RIGHT_nonleaf_triple_or_quadruple_control.json').read_text());assert [z['word']for z in rights]==[z['headings']for z in saved['right_rows']]and[z['word']for z in triples]==[z['headings']for z in saved['triple_rows']]
files=['max_RIGHT_nonleaf_stock_holes_require_outputs_or_parallel_exchanges_v2.md','max_RIGHT_nonleaf_triple_or_quadruple_control.py','max_RIGHT_nonleaf_triple_or_quadruple_control.json'];hashes={f:hashlib.sha256((D/f).read_bytes()).hexdigest()for f in files};assert hashes[files[0]]=='160ea8de41b0b7e1d56eb7d7a1fc1748af72170ce547f624e7ce67f12d8ff1c2'
prior=R/'audits/check_G3_contractibility_and_max_leaf_independent.json';assert hashlib.sha256(prior.read_bytes()).hexdigest()=='5f41b889a8d9dd2686ed419f3838a5bba132b3f3fbbbdc26847f3958416976f1'
out={'status':'PASS distinct contractible max-RIGHT middle-node output/parallel-exchange tradeoff','source_hashes':hashes,'fresh_twelve_max_RIGHT_histories':rights,'fresh_twelve_G3_middle_connections':triples,'flow4_source_events':source,'flow4_target_E_normalized_events':targetE,'analytic':['Every selected max-RIGHT middle transition has a physical flow3 or4 ordinal-two occurrence on sheet M-1. Complete same-R RLR/RLRL cases and both possible L3 headings are retained.','At all G3 internal cells, ordinal-two incoming and outgoing occurrences are exactly the L1/R2 repaired partners on c-1. At endpoints the other partner is ordinal two of a flow-two port. Thus the WHOLE source-sink path belongs to one canonical middle node, and a cyclic G3 component is an entire canonical node, not merely a subpath.','A G3 cyclic component is essential by the independently signed first/last crossing theorem. It therefore cannot be the chosen contractible canonical node. Every contractible node with a middle G3 edge contains a source-sink path; different nodes cannot share any such path because canonical edge occurrences partition. This gives h3<=J without assigning new original fuel.','A flow4 edge saturates every read at each endpoint: source EWEW sends SSSS, target SSSS receives those same four physical ordinal occurrences. Both exchanges join the SAME c-1 and c-2 canonical nodes, as shown by direct labels and L1/R2 swap. Those nodes are on distinct sheets. Physical neighboring endpoint cells have opposite checker parity and cannot alias under a full heading-restoring drift.','A complete cap4 cell has at most one saturated input-or-output port, as the fresh30-history enumeration confirms. Hence different physical flow4 quotient edges use DISJOINT pairs of exchange edges. Removing one edge per pair leaves its retained parallel alternative, so the connected canonical graph stays connected and beta>=F4. Existing even-beta parity supplies the even rounding; no primitivity assumption is used.','A remaining contractible node without G3 must have a flow4 ordinal-two edge at a chosen max-RIGHT corner. Each such edge has exactly one upper canonical node, so distinct nodes choose distinct flow4 edges. Consequently h<=J+F4<=J+beta. Under zero output J0, every such node uses a nonbridge parallel pair; h>0 forces beta>=2. This does not bound beta or count renewals.'],'scope':'Complete WHITE cap4 actual full-drift front. H counts distinct contractible M-1 canonical nodes having max-RIGHT corners. No K1 required, no global-front exclusion, no fuel or extra additive period budget.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
