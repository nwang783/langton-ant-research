"""Independent literal geometry and exact integer max-potential verification.

The result is a conditional reduction, never a proof of its remaining transfers.
"""
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parents[1];S=P/'word_stabilization'
manifest=json.loads((S/'dcv_directional25_manifest.json').read_text())
for f,h in manifest['files'].items():assert hashlib.sha256((S/f).read_bytes()).hexdigest()==h,f
words={'D':'LLLLRLRRRR','C':'LLLLRLRRRRLRRRR','V':'LLLLRLRRRRLRRLRRRR'};marker='LLLLRLRRRRL';names=['D','DC','DCC','DCCC','V','VC','VCC'];keep=[0,1,4,5,6]
def rotate(p,h):
 x,y=p
 for _ in range(h%4):x,y=y,-x
 return x,y
def walk(w):
 p=(0,0);h=0;first={};current={};flip=set()
 for t in w:
  bit=t=='L'
  if p in current:assert current[p]==bit
  else:first[p]=bit
  current[p]=not bit;flip.symmetric_difference_update({p});h=(h+(1 if t=='R'else-1))%4;dx,dy=((0,1),(1,0),(0,-1),(-1,0))[h];p=(p[0]+dx,p[1]+dy)
 return (*p,h),first,flip
core={q for q,b in walk(marker)[1].items()if b};G=[]
for name in names:
 w=''.join(words[c]for c in name);e,_,flip=walk(w);entry={q for q,b in walk(w+marker)[1].items()if b};newcore={(e[0]+rotate(q,e[2])[0],e[1]+rotate(q,e[2])[1])for q in core}
 G.append((e,sorted(entry-core),sorted((entry^flip)-newcore)))
V=json.loads((S/'dcv_free_direction_family102.json').read_text())['values'];assert(V['ax'],V['ay'])==(1,3)
L=lambda p:p[0]+3*p[1];checks=[]
for a in keep:
 e,ins,outs=G[a]
 for h in range(4):
  lower=[L(rotate((-1,1),h))+V[f'c{h}']]+[2*L(rotate(q,h))+V[f'u_{a}_{j}_{h}']for j,q in enumerate(ins)]
  upper=[2*L(rotate(e[:2],h))+L(rotate((-1,1),h+e[2]))+V[f'c{(h+e[2])%4}']]+[2*L(rotate(q,h))+V[f'w_{a}_{j}_{h}']for j,q in enumerate(outs)]
  assert max(upper)<=max(lower)
  checks.extend({'packet':a,'heading':h,'output':j,'value':v,'ceiling':max(lower)}for j,v in enumerate(upper))
assert len(checks)==148
def rel(file,width):return {tuple(map(int,line.split()[:width]))for line in(S/file).read_text().splitlines()}
ordinary=rel('seven_sub_dcv_star4_kernel.tsv',5);protected=rel('dcv_protected_patch2_kernel.tsv',7);signed=rel('dcv_companion_closed_family.tsv',7)
assert len(ordinary)==3873 and len(protected)==102122 and len(signed)==102
assert hashlib.sha256((S/'dcv_companion_closed_family.tsv').read_bytes()).hexdigest()=='8da1a5e5fc5c1162c1938890c836602ffd7ea4fa8d91831d0510425bcc16368e'
allposes=[];remaining=[];base=[];extra=[];edges=[]
for a in keep:
 for ai,q in enumerate(G[a][2]):
  for b in keep:
   for bi,z in enumerate(G[b][1]):
    poses=[]
    for h in range(4):
     rz=rotate(z,h);p=(q[0]-rz[0],q[1]-rz[1]);row=(a,b,*p,h,*q)
     if(sum(p)-h)%2 or row[:5]in ordinary:continue
     poses.append([*p,h]);allposes.append(row)
     bad=[g for g in range(4)if V[f'u_{b}_{bi}_{(g+h)%4}']>V[f'w_{a}_{ai}_{g}']]
     if bad:
      r={'tuple':list(row),'violating_global_headings':bad}
      (base if row in protected else extra if row in signed else remaining).append(r)
    if poses:edges.append({'producer':[a,ai],'consumer':[b,bi],'poses':poses})
resource=json.loads((S/'dcv_residual_core_resources.json').read_text());assert resource['transfer_edges']==edges
for a,g in enumerate(resource['geometry']):assert (g['endpoint'],g['inputs'],g['outputs'])==(list(G[a][0]),[list(p)for p in G[a][1]],[list(p)for p in G[a][2]])
saved=json.loads((S/'dcv_conditional_free_direction_family102.json').read_text())
assert remaining==saved['unproved_bad_transfers'] and extra==saved['given_relation_exclusions'] and base==saved['original_protected_exclusions'] and V==saved['integer_weights']
assert rel('dcv_directional25_targets.tsv',7)=={tuple(r['tuple'])for r in remaining} and len(remaining)==25
observed=rel('dcv_companion_observed19.tsv',7)
assert not observed&{tuple(r['tuple'])for r in remaining+extra+base}
old=json.loads((S/'dcv_conditional_confinement_optimized.json').read_text())['unproved_bad_transfers'];oldrows=[(r['source_packet'],r['target_packet'],*r['target_pose'],*r['source_output'])for r in old]
shared=[i for i,r in enumerate(oldrows,1)if r in{tuple(r['tuple'])for r in remaining}];new=sorted({tuple(r['tuple'])for r in remaining}-set(oldrows))
assert shared==[1,2,3,4,5,15,16,17,18,19,20,22,23,24,31,35,36,39,41,42,43,44]
assert new==[(0,4,4,-1,3,2,0),(1,4,5,0,3,3,1),(4,4,4,1,3,2,2)]
I=max(v for k,v in V.items()if k.startswith('u_'));minweight=min([I]+[v for k,v in V.items()if k.startswith('w_')]);offsets=[L(rotate((-1,1),h))+V[f'c{h}']for h in range(4)]
result={'status':'PASS conditional directional confinement reduction ONLY; all25 residual obligations remain unproved','direction':[1,3],'local_inequalities':len(checks),'possible_transfer_poses':len(allposes),'original_protected_bad_exclusions':len(base),'signed102_bad_exclusions':len(extra),'remaining_obligations':len(remaining),'shared_original69_indices':shared,'new_tuples':new,'initial_weight':I,'minimum_token_weight':minweight,'core_offsets':offsets,'independent_checks':checks,'source_manifest_sha256':hashlib.sha256((S/'dcv_directional25_manifest.json').read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k!='independent_checks'}))
