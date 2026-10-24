from pathlib import Path
from collections import Counter
import ast,json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
P=D/'even_reader_rails_expand_but_an_all_even_merge_resets_them.md';JF=D/'check_even_reader_rail_and_merge_reset.json'
assert sha(P).startswith('1df4856e') and sha(JF).startswith('a1acb1bb') and sha(D/'check_even_reader_rail_and_merge_reset.py').startswith('11e3b2dd')
J=json.loads(JF.read_text());ns={'__file__':str(S.with_name('check_global_max_flow2_staircase_independent.py'))};exec(Path(ns['__file__']).read_text().split('rows=[];stats=Counter()')[0],ns)
cv,V,out,test=[ns[x] for x in ('cv','V','out','test')]
encode=lambda e:[list(e[0]),e[1]]
rows=[]
for r in J['controls']:
 hs={complex(*ast.literal_eval(p)):cv(h) for p,h in r['histories'].items()};assert len(hs)==14 and all(len(h)==4 for h in hs.values());assert test(hs)[0]=='open'
 hs2={tuple(ast.literal_eval(p)):h for p,h in r['histories'].items()};times={ast.literal_eval(k):v for k,v in r['injective_mod4_calendar'].items()};su={};pre={}
 for p,w in hs.items():
  pt=(int(p.real),int(p.imag))
  for h,v in enumerate(V):
   if p+v not in hs:continue
   qt=(int((p+v).real),int((p+v).imag));aa=[i for i in range(4) if out(w,i)==h];bb=[i for i,z in enumerate(hs[p+v]) if z==h];assert len(aa)==len(bb)
   for a,b in zip(aa,bb):
    e,f=(pt,a),(qt,b);assert e not in su and f not in pre;su[e]=f;pre[f]=e
 assert len(times)==len(set(times.values()))==56
 for p,h in hs2.items():
  phase=2*(p[0]%2) if sum(p)%2==0 else 3-2*(p[0]%2)
  for i in range(4):
   assert times[p,i]%4==phase
   if i:assert times[p,i]-times[p,i-1]>=4
 for e,f in su.items():assert times[f]==times[e]+1
 # Rebuild the complete event-disjoint components, including every open endpoint.
 events={(p,i) for p in hs2 for i in range(4)};components=[];used=set()
 for e in sorted(events-set(pre)):
  chain=[];f=e
  while True:
   assert f not in used;used.add(f);chain.append(f)
   if f not in su:break
   f=su[f]
  components.append(chain)
 assert used==events
 assert [[[list(p),i] for p,i in c] for c in components]==r['components']
 intervals=[(times[c[0]],times[c[-1]]) for c in components];order=r['whole_component_order'];assert sorted(order)==list(range(len(components)))
 assert all(intervals[a][1]<intervals[b][0] for a,b in zip(order,order[1:]))
 for path in r['exact_paths']:
  pp=[(tuple(p),i) for p,i in path];assert all(su[a]==b for a,b in zip(pp,pp[1:]))
 C=(2,-1);H=(3,-2)
 if r['mode']=='expanding':
  assert times[H,1]==times[C,0]-2 and times[H,2]==times[C,3]+2
  assert times[H,2]-times[H,1]>=times[C,2]-times[C,1]+12
  assert hs2[(2,-2)]==hs2[(3,-1)]=='NNSS'
 else:
  assert hs2[(2,-2)]=='SSNN' and hs2[(3,-1)]=='SNNS'
  assert times[H,1]==times[C,3]+2
  pp=[(tuple(p),i) for p,i in r['exact_paths'][0]];assert ''.join('R' if i%2==0 else 'L' for p,i in pp[:-1])=='RLLL'
  assert hs2[H][0]=='W' and hs2[H][1]=='E'
 b={}
 for p,w in hs.items():
  q=p+V[out(w,0)];b[str((int(p.real),int(p.imag)))]=[int(q.real),int(q.imag)]
 assert b==r['firstR_edges']
 rows.append(dict(mode=r['mode'],events=56,components=len(components),internal_edges=len(su),all_complete_even=True,distinct_calendar=True))
O=dict(status='PASS exact expanding even rail and local all-even role-reset only',proof=sha(P),certificate=sha(JF),script=sha(S),controls=rows,analytic_review=[
'Exact complete four-read ordinal matching gives H.L1 to G.L1 to C.R0 and C.L3 to F.L3 to H.R2 in the NNSS/NNSS interface. Same-cell rank gaps at least four imply strict middle-span growth by twelve. The next chosen reader really is H=C+(1,-1) and the inherited helper G has the required NNSS role.',
'An infinite unchanged rail contradicts the finite FULL drift quotient: nonparallel drift makes infinitely many distinct classes; parallel nonzero integral drift identifies two rail cells and preserves both-rank time difference under the exact period voltage. No primitive period or spatial-descent assumption is used.',
'In the alternative SSNN/SNNS mode the actual RLLL channel is H.R0 to G.L1 to C.L3 to F.L1 to H.L1. It rotates heading by180 rather than returning full pose, and puts H.L1 after C.L3. The role required for nesting has changed. Actual b(H)=G,b(G)=C,b(C)=R are distinct from actual chronological successors using G.L1.',
'Both whole fourteen-cell inventories independently pass every port including zeros, literal next-rank return, positive-clock-cycle and global-C-height check. All56 event phases are distinct, every internal edge costs one, same-cell rank gaps are at least four, and all complete successor components and open endpoints partition the events with a disjoint mod-four calendar.',
'Neither local calendar supplies the missing physical connector paths, an actual prepared factor, full periodic field, or controller. The reset is an obstruction to an inference from this necessary abstraction only; it is not a physical counterexample to any complete-front odd-output theorem. No fresh-fuel charge or eventual global rail behavior follows.'
]);S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(rows);print(sha(S.with_suffix('.json')))
