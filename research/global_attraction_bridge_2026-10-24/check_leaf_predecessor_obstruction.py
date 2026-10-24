"""Exact first-step injection and literal failure of terminal input/output charging."""
from pathlib import Path
from collections import Counter
import hashlib,json
P=Path(__file__).parent;D=[(0,1),(1,0),(0,-1),(-1,0)]
SRC=json.loads((P/'WHOLE_LAST_EXIT_RENEWAL_CHECKED.json').read_text())

def run(case_name,start,end,selected):
 source=next(c for c in SRC['cases']if c['name']==case_name);it=next(z for z in source['intervals']if z['start']==start and z['end']==end);cut=it['whole_tree_cuts'][0];B={tuple(q):i for q,i in cut['full_black']};initial=dict(B);p,h=tuple(cut['pose'][0]),cut['pose'][1];events=[];last={};visits={}
 for t in range(start,end):
  q=p;old=B.pop(q,None);c='R'if old is None else'L'
  if old is None:B[q]=t;h=(h+1)%4
  else:h=(h-1)%4
  p=(q[0]+D[h][0],q[1]+D[h][1]);events.append(dict(time=t,cell=q,turn=c,consumed=old,next=p));last[q]=(t,p);visits.setdefault(q,[]).append((t,c))
 assert B=={tuple(q):i for q,i in it['whole_tree_cuts'][1]['full_black']}and p not in last
 tree={q:r for q,(t,r)in last.items()};ind=Counter(tree.values());leaves={q for q in last if not ind[q]};C=set(initial)&set(last);O=set(B)&set(last);marked=C|O;f={}
 for q,(t,r)in last.items():
  if t==start:continue
  u=tuple(events[t-start-1]['cell'])
  if last[u][0]>t:f[q]=u
 assert len(set(f.values()))==len(f)
 assert all(v in f or last[v][0]==start for v in leaves)
 bad=[]
 for v in sorted(leaves-marked):
  q=v;chain=[]
  while q not in marked and q in f:chain.append(q);q=f[q]
  if q not in marked:bad.append(dict(start=v,chain=chain,terminal=q))
 examples=[]
 for v in selected:
  q=v;chain=[]
  while q not in marked and q in f:chain.append(q);q=f[q]
  assert q not in marked and v in leaves
  nodes=[]
  for z in chain+[q]:
   tt=last[z][0];u=tuple(events[tt-start-1]['cell'])if tt>start else None
   assert z not in initial and z not in B and visits[z][0][1]=='R'and visits[z][-1][1]=='L'
   nodes.append(dict(cell=z,is_tree_leaf=z in leaves,tree_indegree=ind[z],actual_reads=visits[z],last_predecessor=u,predecessor_last_read=last[u][0]if u is not None else None,last_tree_edge=tree[z]))
  examples.append(dict(start=v,nodes=nodes,terminal=q,terminal_last_arrival_is_tree_edge=(u is not None and tree[u]==q and last[u][0]==last[q][0]-1)))
 return dict(case=case_name,start=start,end=end,interval_tree_root=p,read_vertices=len(last),leaf_count=len(leaves),unmarked_leaves=len(leaves-marked),unmarked_leaf_starts_ending_unmarked=len(bad),inversion_map_size=len(f),inversion_map_injective=True,inversion_map_sha256=hashlib.sha256(json.dumps(sorted(f.items())).encode()).hexdigest(),selected_examples=examples,full_input_hash=hashlib.sha256(json.dumps(cut['full_black']).encode()).hexdigest(),full_output_hash=hashlib.sha256(json.dumps(sorted(B.items())).encode()).hexdigest())

cases=[run('empty',5710,6042,[(0,8)]),run('MT_100',40071,109168,[(432,449),(213,234)])]
assert cases[0]['unmarked_leaf_starts_ending_unmarked']==1 and cases[1]['unmarked_leaf_starts_ending_unmarked']==275
assert len(cases[1]['selected_examples'][1]['nodes'])==3 and sum(q['is_tree_leaf']for q in cases[1]['selected_examples'][1]['nodes'])==2
fs=['WHOLE_LAST_EXIT_RENEWAL_MANIFEST.json','WHOLE_LAST_EXIT_ENDPOINT_ADDENDUM.json','../audits/check_whole_last_exit_renewal_independent.json']
for f in fs:assert(P/f).exists(),f
out=dict(status='AUTHOR first-step injection and continuation countercontrols; independent audit pending',cases=cases,dependencies={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in fs},scope='Fresh-root interval trees only. First-step injection does not make terminal chains an injective charge to C/O. Gross leaf<=C+O+1 is neither proved nor disproved.')
(P/'LEAF_PREDECESSOR_OBSTRUCTION_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n');print([(c['case'],c['leaf_count'],c['unmarked_leaves'],c['unmarked_leaf_starts_ending_unmarked'])for c in cases])
