from pathlib import Path
import json,hashlib
files=['staged_two_cell_singletons.md','staged_two_cell_periodic_certificates.json','certify_staged_periodic_tails.py','direct_monochromatic_returns.cpp','analyze_direct_macro_histories.py','build_marker_context_quotient.py','prepare_marker_quotient_kernel.py','build_pruned_context_component.py','prune_charged_context_graph.py','generic_patch2_spatial_kernel.cpp','multi_cell_spatial_inference.md','extract_patch2_dependency_cone.cpp','minimize_charged_contexts.py',__file__]
files += ['../audits/replay_staged_singleton_clauses_independent.py','../audits/check_staged_singleton_bridges_independent.py','../audits/check_literal_spatial_clauses.cpp','staged_two_cell_snapshots/audited_manifest_input.json']
config=[]
def scc(n,E,removed):
 A=[[]for _ in range(n)];R=[[]for _ in range(n)]
 for a,b in E:
  if a not in removed and b not in removed:A[a].append(b);R[b].append(a)
 seen=set();order=[]
 def dfs(a):
  seen.add(a)
  for b in A[a]:
   if b not in seen:dfs(b)
  order.append(a)
 for a in range(n):
  if a not in removed and a not in seen:dfs(a)
 seen=set();S=[]
 for a in reversed(order):
  if a in seen:continue
  seen.add(a);todo=[a];part=[]
  while todo:
   u=todo.pop();part.append(u)
   for v in R[u]:
    if v not in seen:seen.add(v);todo.append(v)
  if len(part)>1 or a in A[a]:S.append(sorted(part))
 return S
for lab,depth in [('lrrlrrrrlrl',2),('rrrlrllrrrr',1)]:
 b='direct_mono_'+lab;p=b+'_history4_scc0_context2';snap='staged_two_cell_snapshots/'+lab
 files += [b+'.returns.tsv',snap+'.returns.tsv',snap+'_history4_words.json',snap+'_history4_summary.json',snap+'_history4_scc0_port_quotient.json',b+'_history4_scc0_port_quotient.json',snap+'.log']
 old=json.load(open(b+'_history4_scc0_port_quotient.json'));new=json.load(open(snap+'_history4_scc0_port_quotient.json'))
 assert all(old[k]==new[k]for k in old)
 files += [p+'_patch2_cone.tsv',p+'_selected_marks.tsv',p+'_selected_charges.json']
 stages=[]
 for i in range(depth+1):
  s=p+'_residual0'*i;Q=json.load(open(s+'_port_quotient.json'));G=json.load(open(s+'_grammar.json'))
  for suffix in ['_port_quotient.json','_grammar.json','_kernel.input','_patch2_kernel.summary.json','_patch2_pruned_graph.json','_patch2_kernel.fresh.tsv']:
   files.append(s+suffix)
  if i:
   files.append(s+'_patch2_kernel.tsv');marks={}
   for l in open(s+'_patch2_kernel.fresh.tsv'):
    a,x,y,t=map(int,l.split())
    if t<len(Q['macro_words'][a]['word']):marks.setdefault(a,(x,y,t))
   mp=s+'_raw_marks.tsv';Path(mp).write_text(''.join(f'{a} {x} {y} {t}\n'for a,(x,y,t)in sorted(marks.items())))
   files.append(mp);removed=set(marks)
  else:mp=s+'_selected_marks.tsv';removed=set(json.load(open(s+'_selected_charges.json'))['selected'])
  S=scc(len(Q['macro_words']),G['pairs'],removed)
  if i==0:assert not(set(sum(S,[]))&set(json.load(open(s+'_selected_charges.json'))['all_charged']))
  stages.append({'prefix':s,'certificate':s+('_patch2_cone.tsv'if i==0 else'_patch2_kernel.tsv'),'marks':mp,'marked_types':sorted(removed),'recurrent_components_after_selected_marks':S})
 config.append({'label':lab.upper(),'snapshot_prefix':snap,'stages':stages})
W='LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLLRRRRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRRLLLLRLRRRRLRRRR'
Path('staged_two_cell_singletons_manifest.json').write_text(json.dumps({'status':'independently verified end to end; separate singleton theorems only','canonical_W104':W,'canonical_W_sha256':hashlib.sha256(W.encode()).hexdigest(),'claims':config,'files':{f:hashlib.sha256(Path(f).read_bytes()).hexdigest()for f in sorted(set(files))}},indent=2))
print('FROZEN files',len(set(files)))
