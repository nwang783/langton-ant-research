"""Finite inductive empty-origin sets, not reachability or literal support paths."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;gp=R/'chronology_dcuv/literal_residual_geometry.json';ip=R/'chronology_dcuv/u_middle_input_origin_order.json';GG=json.loads(gp.read_text());G=GG['geometry'];K={tuple(q)for q in GG['core']};T=json.loads(ip.read_text())['four_cohort_templates'];IDS=(0,1,4,5,6,7,8,9)
def rot(q,h):x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return(p[0]+q[0],p[1]+q[1])
def sub(p,q):return(p[0]-q[0],p[1]-q[1])
results=[]
for ti,t in enumerate(T):
 b=t['source_packet'];O={tuple(q)for q in G[b]['outputs']};P={tuple(q)for q in t['matched_source_outputs']};D={tuple(q[:2]):q[2]for q in G[b]['requirements']};odd={tuple(q)for q in G[b]['raw_odd']};end=G[b]['endpoint'];EC={add(end[:2],rot(q,end[2]))for q in K};known_post={q:v^(q in odd)for q,v in D.items()};assert{q for q,v in known_post.items()if v and q not in EC}==O
 N0=set(D)-O;ops={};allcounts={}
 for q in N0:
  ops[q]=[];allcounts[q]=0
  for a in IDS:
   for h in range(4):
    for oi,z in enumerate(G[a]['outputs']):
     p=sub(q,rot(z,h))
     if(sum(p)-h)%2:continue
     allcounts[q]+=1;C={add(p,rot(z[:2],h))for z in G[a]['requirements']}
     if C&P:continue
     I={add(p,rot(z,h))for z in G[a]['inputs']};ops[q].append({'packet':a,'pose':[*p,h],'output_index':oi,'inputs':sorted(I)})
  assert allcounts[q]==136
 N=set(N0);rounds=[];deleted=[]
 while True:
  remove=[]
  for q in sorted(N):
   witness=next((op for op in ops[q]if not({tuple(p)for p in op['inputs']}&N)),None)
   if witness is not None:remove.append(q);deleted.append({'cell':q,'round':len(rounds),'witness':witness})
  rounds.append(remove)
  if not remove:break
  N-=set(remove)
 closure=[]
 for q in sorted(N):
  for op in ops[q]:
   intersection={tuple(z)for z in op['inputs']}&N;assert intersection;closure.append({'cell':q,'operation':op,'input_in_invariant':min(intersection)})
 direct={q for q in N0 if not ops[q]};missing=tuple(t['missing_input']);result={'template_index':ti,'source_packet':b,'consumer_pose':t['consumer_pose'],'protected_outputs':sorted(P),'missing_input':missing,'old_outcome':t['outcome'],'known_initial_nonresidual_cells':sorted(N0),'direct_shadow_cells':sorted(direct),'fixedpoint_empty_origin_cells':sorted(N),'new_indirect_cells':sorted(N-direct),'deletion_rounds':rounds,'deletion_witnesses':deleted,'closure_operations':closure,'excludes_missing_input':missing in N,'all_known_cell_exporters':sum(allcounts.values())}
 results.append(result)
summary={'templates':len(results),'excludes_missing':sum(t['excludes_missing_input']for t in results),'newly_excluded':sum(t['excludes_missing_input']and t['old_outcome']!='excluded_all_ages'for t in results),'templates_with_indirect_cells':sum(bool(t['new_indirect_cells'])for t in results),'new_indirect_cells':sum(len(t['new_indirect_cells'])for t in results),'enumerated_cell_exporter_placements':sum(t['all_known_cell_exporters']for t in results)}
J={'status':'AUTHOR_FINITE_EMPTY_ORIGIN_FIXEDPOINT_PASS','scope':'Retained protected identities and exact residual-origin implications only; no continuous head, ages, counts, or realizability. Greatest fixedpoint inside the stated known postsource nonresidual domain, not a strongest invariant claim.','summary':summary,'templates':results,'dependencies':{str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in(gp,ip)}}
(R/'chronology_dcuv/protected_origin_siphons.json').write_text(json.dumps(J,indent=2)+'\n');print(summary)
for t in results:
 if t['new_indirect_cells']:print(t['template_index'],t['source_packet'],t['consumer_pose'],'added',t['new_indirect_cells'],'miss',t['missing_input'],'excludes',t['excludes_missing_input'])
