from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();proof=D/'flow3_double_LEFT_rank_collision_and_staircase_normal_form.md';assert sha(proof)=='a5d8cd2a5692d6673c9a80fd440a40d70f27c2c22718d275497d48138bd19ad4'
J=json.loads((D/'check_flow3_double_LEFT_rank_collision.json').read_text());V={'N':1j,'E':1,'S':-1j,'W':-1};I={v:k for k,v in V.items()};out=lambda w:[I[V[h]*(-1j if r%2==0 else 1j)]for r,h in enumerate(w)];p={'A':1j,'Z':0j,'Y':1,'B':1+1j};pinv={v:k for k,v in p.items()};rows=[];counts=Counter()
# Derive endpoints directly from all complete WHITE cap4 RIGHT profiles.
prev=[];nxt=[]
for n in range(1,5):
 for tt in product('EW',repeat=n-1):
  w='E'+''.join(tt)
  if out(w).count('S')==3:prev.append(w)
 for tt in product('NS',repeat=n-1):
  w='N'+''.join(tt)
  if w.count('N')==3:nxt.append(w)
assert set(prev)=={'EWE','EWWW','EEEW','EWEE'}and set(nxt)=={'NNN','NNSN','NNNS','NSNN'}
for a,b in product(prev,nxt):
 hs=dict(A=a,Z='NSSS',Y='WEEE',B=b);succ={};bad=False
 for name,w in hs.items():
  for d in V:
   dest=pinv.get(p[name]+V[d])
   if dest is None:continue
   sr=[r for r,c in enumerate(out(w))if c==d];rr=[r for r,c in enumerate(hs[dest])if c==d]
   if len(sr)!=len(rr):bad=True;break
   for r,t in zip(sr,rr):succ[name,r]=(dest,t)
  if bad:break
 if bad:counts['port']+=1;rows.append((a,b,'port',[]));continue
 witnesses=[]
 for r in range(4):
  route=[('Z',r)]
  while route[-1]in succ:
   route.append(succ[route[-1]])
   if route[-1][0]=='Z':
    if route[-1][1]!=r+1:witnesses.append(route)
    break
   assert len(route)==len(set(route))
 assert witnesses and all(len(w)==5 for w in witnesses)
 counts['rank']+=1;rows.append((a,b,'rank',witnesses))
assert counts=={'port':6,'rank':10}
# Verify every author-provided return against independent physical successor.
assert J['complete_counts']=={'port mismatch':6,'literal rank collision':10}
for a,b,kind,witnesses in rows:
 ref=next(z for z in J['rows']if(z['A'],z['B'])==(a,b))
 if kind=='rank':
  assert ref['result']=='literal rank collision'and list(map(tuple,ref['actual_return']))in witnesses
  hs=dict(A=a,Z='NSSS',Y='WEEE',B=b)
  for u,r,v,t,d,j in ref['all_internal_edges']:
   sr=[q for q,h in enumerate(out(hs[u]))if h==d];rr=[q for q,h in enumerate(hs[v])if h==d]
   assert p[u]+V[d]==p[v]and sr[j-1]==r and rr[j-1]==t
 else:
  assert ref['result']=='port mismatch';z=ref['witness'];hs=dict(A=a,Z='NSSS',Y='WEEE',B=b)
  sr=[q for q,h in enumerate(out(hs[z['source']]))if h==z['heading']];rr=[q for q,h in enumerate(hs[z['target']])if h==z['heading']]
  assert len(sr)!=len(rr)and sr==z['departures']and rr==z['arrivals']
outj=dict(status='PASS no consecutive LEFT in any constant-flow3 b-segment; local-max length at most4 edges',proof_sha256=sha(proof),control_sha256=sha(D/'check_flow3_double_LEFT_rank_collision.json'),all16_independent_rows=rows,counts=dict(counts),analytic_review=[
'Any consecutive LEFT pair on an embedded essential b-circle has RIGHT predecessor/successor: a third same turn would close a physical unit square. Their incident flow3 ports derive exactly four complete predecessor/four successor histories, including odd endpoints and one-use reroutes.',
'All16 actual square port networks independently regenerated. Six mismatch; each of ten compatible rows has a four-step actual return to Z that skips/reverses a rank or returns to the same actual event. Unknown exterior cannot insert a missing Z read inside these consecutive four moves.',
'The obstruction requires constant selected C/cap4 WHITE alphabet but no height maximum. Together signed any-height LRRL obstruction and no three equal turns, every nonclosed flow3 segment has alternating LR body and one/two RIGHT endpoint caps. No finite length bound at arbitrary c.',
'At locally maximal selected C, signed LRL excludes two LEFT contacts, leaving RR,RLR,RLRR,RRLR,RRLRR and at mostfour edges. This strengthens signed five-edge bound without changing its source hypotheses. Number of segments, waits, period and all outside support remain open.'
]);S.with_suffix('.json').write_text(json.dumps(outj,indent=2)+'\n');print(outj['status']);print(sha(S.with_suffix('.json')))
