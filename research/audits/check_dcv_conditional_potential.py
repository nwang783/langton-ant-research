"""Independent exact arithmetic only. No claimed proof of the149 transfer exclusions."""
import json,pathlib,hashlib,itertools
P=pathlib.Path('/workspace/shared/langton');A=P/'audits';S=P/'word_stabilization'
W={'D':'LLLLRLRRRR','C':'LLLLRLRRRRLRRRR','V':'LLLLRLRRRRLRRLRRRR'};M='LLLLRLRRRRL';names=['D','DC','DCC','DCCC','V','VC','VCC'];keep=[0,1,4,5,6]
def rotate(q,h):
 x,y=q
 for _ in range(h%4):x,y=y,-x
 return x,y
def walk(word):
 x=y=h=0;first={};last={};odd=set()
 for c in word:
  q=(x,y)
  if last.get(q)==c:return None
  first.setdefault(q,c);last[q]=c;odd.symmetric_difference_update({q});h=(h+(1 if c=='R' else -1))%4;dx,dy=((0,1),(1,0),(0,-1),(-1,0))[h];x+=dx;y+=dy
 return (x,y,h),first,last,odd
words=[''.join(W[c]for c in s)for s in names];K={q for q,c in walk(M)[1].items()if c=='L'};G=[]
for w in words:
 e,f,l,o=walk(w);seed={q for q,c in walk(w+M)[1].items()if c=='L'};newK={(e[0]+rotate(q,e[2])[0],e[1]+rotate(q,e[2])[1])for q in K};G.append((e,sorted(seed-K),sorted((seed^o)-newK)))
# Exact packet cutoff and boundary exceptions.
assert walk(W['C']*4+M) is None
assert walk(W['D']+W['C']*4+M) is None
assert walk(W['V']+W['C']*3+M) is None
assert all(walk(words[2]+w+M)is None for w in words)
assert all(walk(w+words[3]+M)is None for w in words)
V=json.loads((S/'dcv_packet_maxplus_optimized.json').read_text())['values'];checks=0
for a in keep:
 e,ins,outs=G[a]
 for h in range(4):
  lower=[rotate((-1,1),h)[1]+V[f'c{h}']]+[2*rotate(q,h)[1]+V[f'u_{a}_{j}_{h}']for j,q in enumerate(ins)]
  upper=[2*rotate(e[:2],h)[1]+rotate((-1,1),h+e[2])[1]+V[f'c{(h+e[2])%4}']]+[2*rotate(q,h)[1]+V[f'w_{a}_{j}_{h}']for j,q in enumerate(outs)]
  assert max(upper)<=max(lower);checks+=len(upper)
ordinary={tuple(map(int,l.split()[:5]))for l in (S/'seven_sub_dcv_star4_kernel.tsv').read_text().splitlines()};potential_edges=[];bad=[]
for a in keep:
 for ai,q in enumerate(G[a][2]):
  for b in keep:
   for bi,z in enumerate(G[b][1]):
    poses=[]
    for h in range(4):
     zz=rotate(z,h);p=(q[0]-zz[0],q[1]-zz[1])
     if (sum(p)-h)%2 or (a,b,*p,h)in ordinary:continue
     poses.append([*p,h]);viol=[g for g in range(4)if V[f'w_{a}_{ai}_{g}']<V[f'u_{b}_{bi}_{(g+h)%4}']]
     if viol:bad.append((a,q,b,z,(*p,h),tuple(viol)))
    if poses:potential_edges.append({'producer':[a,ai],'consumer':[b,bi],'poses':poses})
assert potential_edges==json.loads((S/'dcv_residual_core_resources.json').read_text())['transfer_edges']
R=json.loads((S/'dcv_conditional_confinement_optimized.json').read_text())
def norm(r):return(r['source_packet'],tuple(r['source_output']),r['target_packet'],tuple(r['target_input']),tuple(r['target_pose']),tuple(r['violating_global_headings']))
assert set(bad)=={norm(r)for r in R['protected_relation_excludes']+R['unproved_bad_transfers']}
protected={tuple(map(int,l.split()[:7]))for l in (S/'dcv_protected_patch2_kernel.tsv').read_text().splitlines()}
assert {v for v in bad if (v[0],v[2],*v[4],*v[1])in protected}=={norm(r)for r in R['protected_relation_excludes']}
pose_count=excluded_count=0
for e in potential_edges:
 a,ai=e['producer'];b,bi=e['consumer'];q=G[a][2][ai]
 for pose in e['poses']:
  pose_count+=1;excluded_count+=int((a,b,*pose,*q)in protected)
assert (pose_count,excluded_count)==(324,103)
I=max(v for k,v in V.items()if k.startswith('u_'));offsets=[rotate((-1,1),h)[1]+V[f'c{h}']for h in range(4)];init=max(I,*offsets);minweight=min(I,*(v for k,v in V.items()if k.startswith('w_')))
assert (checks,I,init,(init-min(offsets)+1)//2,(init-minweight+1)//2)==(148,17,17,9,13)
res={'status':'PASS conditional arithmetic only','local_inequalities':checks,'ordinary_forbidden_pairs':len(ordinary),'transfer_edge_families':len(potential_edges),'all_bad_transfer_poses':len(bad),'required_unproved_bad_transfer_poses':len(R['unproved_bad_transfers']),'protected_transfer_exclusions':excluded_count,'provisional_split':[len(R['unproved_bad_transfers']),len(R['protected_relation_excludes'])],'head_margin':9,'residual_margin':13,'hashes':{str(f.relative_to(P)):hashlib.sha256(f.read_bytes()).hexdigest()for f in [S/'dcv_packet_maxplus_optimized.json',S/'dcv_residual_core_resources.json',S/'seven_sub_dcv_star4_kernel.tsv']}}
(A/'dcv_conditional_potential_independent.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res))
