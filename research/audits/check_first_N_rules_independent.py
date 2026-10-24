from pathlib import Path
from collections import Counter
import hashlib,json
S=Path(__file__).resolve();R=S.parents[1];P=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();bind={'FIRST_N_RETURN_RULES_DIAGONAL_REDUCTION.md':'961b19e632cae7084d29cae71bdc9aa3400bbe655694cd69b3b10fd776c66c00','certify_first_N_return_rules.py':'244d67e81a3c69bd0ad2c92c1c0a41a80b1a146d6b23c96b6869dc07abedd81d','first_N_return_rules_certificate.json':'948b8dcb5b36bcc70ea1da36d2bac51c47ee54528582bbfb19c808944369dfa9'}
for f,h in bind.items():assert sha(P/f)==h
ref=json.loads((P/'first_N_return_rules_certificate.json').read_text());dp=P/'certify_diagonal_read_minimum.json';assert sha(dp)==ref['signed_lower_domain_sha256']=='a4de122acffd766aee76c6676bb247f02c8754fc9ecfd5949cd20c5478929c7f';dom=json.loads(dp.read_text());ns={'__file__':str(S.with_name('check_g8_two_row_covers_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Independent binary-position domain')[0],ns);graph,rot,V,quotient,xy=[ns[k]for k in('graph','rot','V','quotient','xy')];dr=2-2j
rej={(r['lower_case'],tuple(r['A_indices'])):r for r in ref['rejections']};assert len(rej)==len(ref['rejections'])==68
allids=set();newids=set();certs=[];families=Counter();tags=Counter();finaltypes=Counter()
def canreject(J,rels):
 out=[]
 for first in rels:
  a=first['W_ordinal']
  if first['N_ordinal']!=0:continue
  if J<=a+1:out.append(('A',a))
  for second in rels:
   c,b=second['W_ordinal'],second['N_ordinal']
   if c==a+1 and b!=1:out.append(('B',a,b))
   if c==a+2 and b==2 and J==a+3:out.append(('C',a))
 return out
for c in dom['cases']:
 for s in c.get('survivors',[]):
  key=(c['case'],tuple(s['A_indices']));assert key not in allids;allids.add(key);H=list(map(tuple,c['lower_headings']+s['A_headings']));pts,su,pr,oo,oi=graph(H);rels=[[],[]];used=set();counts=[dict(incoming_N=0,outgoing_W=0)for _ in(0,1)]
  for root,(sr,sk,h)in oi.items():assert h==3 and sr.real+sr.imag==2;counts[int(sr.real)]['outgoing_W']+=1
  for node,(tr,tk,h,o)in oo.items():assert h==0 and tr.real+tr.imag==2;counts[int(tr.real)]['incoming_N']+=1
  for root in sorted(oi):
   sr,sk,hi=oi[root];source=sr+sk*dr;lane=int(sr.real);a=[j for j,h in enumerate(H[root[0]])if h==hi].index(root[1]);node=root;k=0;path=[]
   while True:
    assert node not in used;used.add(node);p=pts[node[0]]+k*dr;assert p.real+p.imag<=1 and p!=source;path.append(dict(physical_cell=list(xy(p)),class_index=node[0],complete_rank=node[1],voltage=k,heading=H[node[0]][node[1]],turn='R'if node[1]%2==0 else'L'))
    if node not in su:break
    node,dk=su[node];k+=dk
   tr,tk,ho,b=oo[node];target=tr+(k+tk)*dr
   if source==target:rels[lane].append(dict(W_ordinal=a,N_ordinal=b,duration=len(path)+1,physical_base=list(xy(source)),internal_events=path))
  assert len(used)==sum(map(len,H))
  possible=[canreject(counts[lane]['outgoing_W'],rels[lane])for lane in(0,1)]
  assert any(possible)==(key in rej)
  if key in rej:
   z=rej[key];assert list(map(list,H))==z['complete_named_histories']and counts==z['next_Q_counts']
   # Order-independent exact path coverage, then validate the author's selected indexed witness.
   for lane in(0,1):assert {json.dumps(v,sort_keys=True)for v in rels[lane]}=={json.dumps(v,sort_keys=True)for v in z['actual_first_return_paths'][lane]}
   lane=z['contradictory_lane'];w=z['witness'];rr=z['actual_first_return_paths'][lane];f=rr[w['first_relation']];a=f['W_ordinal'];J=counts[lane]['outgoing_W'];assert f['N_ordinal']==0 and w['a']==a
   if w['rule'].startswith('A_'):assert J<=a+1 and w['total_W']==J
   elif w['rule'].startswith('B_'):
    sec=rr[w['second_relation']];assert sec['W_ordinal']==a+1 and sec['N_ordinal']==w['b']and w['b']in(2,3)
   else:
    assert w['rule']=='C_consecutive_LN_events';sec=rr[w['second_relation']];assert J==w['total_W']==a+3 and(sec['W_ordinal'],sec['N_ordinal'])==(a+2,2)
   newids.add(key);families[key[0]]+=1;tags[w['rule']]+=1;certs.append(dict(id=key,rule=w['rule'],lane=lane,counts=counts,relations=rels))
cyclic={k for k in allids if k[0]==4};skipped={(3,(1,0)),(3,(1,1))};assert len(allids)==227 and len(cyclic)==9 and skipped<=allids and not(skipped&newids)and len(cyclic&newids)==7
final=allids-cyclic-skipped-newids;prior216=allids-cyclic-skipped;assert len(prior216)==216 and len(prior216&newids)==61 and len(final)==155 and len(allids-newids-skipped)==157
serial=lambda ss:[[a,list(b)]for a,b in sorted(ss)]
expected={'all_nine_prior_cyclic_E_ids':serial(cyclic),'both_prior_skipped_middle_ids':serial(skipped),'new_68_intersection_cyclic_E':serial(newids&cyclic),'new_68_intersection_skipped_middle':serial(newids&skipped),'new_61_ids_relative_to_prior216':serial(prior216&newids),'exact_final155_ids':serial(final)};assert expected==ref['explicit_set_difference'];assert dict(tags)==ref['rule_counts']and {str(k):v for k,v in families.items()}==ref['rejected_by_lower_family']
for c in dom['cases']:
 for s in c.get('survivors',[]):
  if(c['case'],tuple(s['A_indices']))not in final:continue
  low=c['lower_headings'];category='one_singleton'if not low[1]else'mixed_N_first'if any(w[0]==0 for w in low[2:])else'one_quadruple'if sum(len(w)==4 for w in low[2:])==1 else'two_quadruple';finaltypes[category]+=1
assert finaltypes=={'one_singleton':4,'mixed_N_first':12,'one_quadruple':30,'two_quadruple':109}
out=dict(status='PASS all-cap first-N return rules exclude68 of227; signed g8 diagonal remainder155 necessary OPEN interfaces',bindings=bind,independent_cover_report=sha(S.with_name('check_diagonal_read_minimum_cover_independent.json')),rule_counts=dict(tags),families=dict(families),all68_independent_return_certificates=certs,exact_set_differences=expected,final_g8_classes=dict(finaltypes),analytic_review=[
'For a vertical incoming-axis cell, W departures are exactly S/R orN/L. A SAME-PHYSICAL-cell first return n0=w_a+1 makes firstN turnL and equal the next W departure w_(a+1), independent of initial color. RuleA contradicts the total W count. RuleB contradicts consecutive N ordinals. RuleC uses lastW to make n2R and its previous read n1L/W, so consecutive n0/n1 are also consecutive W departures; an intervening required R must add another N orW and contradicts one list.',
'All227 signed complete lower interfaces are rebuilt through the independent port graph. Exact complete neighbor histories fix TOTAL Q N andW counts. Each open-root chain is lifted using full d=(2,-2); only equal physical source/target Q returns are used, with all intermediate levels<=1. Every chain edge and rank is exact, with no invented upper history, outside port routing, phase assignment or multiplicity bound.',
'All actual return paths, not merely the selected witness, are independently reconstructed and compared. Every selected RuleA26/RuleB32/RuleC10 application is checked. The complement159 is exactly where none of these three tests applies; it is not asserted feasible or exhaustive of all possible obstruction types.',
'The two signed skipped-middle IDs are disjoint from the68. Seven of the nine cyclic-E IDs overlap, so61 newly excluded IDs relative to prior216 leave155. Exact sets, not marginal counts, are checked. All-growth necessary remainder is157; g8 additionally removes the two cyclic-E leftovers. Final split4 one-singleton/12 mixed/30 one-quad/109 two-quad.',
'This is a finite necessary boundary reduction with all higher support, period and unbounded next-cell history retained. It does not imply155 physical completions, a visit/width bound, all growth-eight exclusion or attraction.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(tags,finaltypes)
