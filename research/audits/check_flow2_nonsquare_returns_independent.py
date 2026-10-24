import itertools,json,hashlib,collections
from pathlib import Path
R=Path('/workspace/shared/langton');P=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
proofs=['global_max_singleton_LEFT_even_resets_need_longer_returns.md','single_LEFT_four_L_auxiliary_corner_scope_clarification.md','critical_global_max_flow2_circles_need_nonsquare_LEFT_returns.md']
assert[sha(P/f)for f in proofs]==['84e543c3c20f6d7c26df542829d490c469fe1e9d4635a3dbeea305ca01e131f7','0a2bb57a9c3d501f578eb4755af9b6acacd6ca719f0ca041f5bde3fd823e017c','728ad41f050840e9723fd80ea33625985d9239b9bb14970bd8c9bae810537f50']
V={'N':1j,'E':1,'S':-1j,'W':-1};I={v:k for k,v in V.items()};out=lambda w:[I[V[h]*(-1j if r%2==0 else 1j)]for r,h in enumerate(w)];ranks=lambda w,h,o=False:[r for r,c in enumerate(out(w)if o else w)if c==h]
pos={'Y':1j,'A':2j,'B':-1+2j,'C':-1+1j};inv={p:k for k,p in pos.items()};counts=collections.Counter();opens=[]
J=json.loads((P/'check_single_LEFT_four_L_return_square.json').read_text());E=json.loads((P/'singleton_four_L_boundary_coverage_control.json').read_text())
for y,a,c,n in itertools.product(['WEE','WEEW'],['NNSS','NSSN'],['NNSS','NSSN'],range(1,5)):
 for bs in itertools.product('EW',repeat=n):
  hs=dict(Y=y,A=a,B=''.join(bs),C=c);nodes=[(u,r)for u,w in hs.items()for r in range(len(w))];idx={x:i for i,x in enumerate(nodes)};succ={};eds=[];bad=False
  for u,w in hs.items():
   eds.extend(((u,r),(u,r+1),4)for r in range(len(w)-1))
   for h in V:
    dest=inv.get(pos[u]+V[h])
    if dest is None:continue
    rr=ranks(w,h,True);tt=ranks(hs[dest],h)
    if len(rr)!=len(tt):bad=True;break
    for r,t in zip(rr,tt):succ[u,r]=(dest,t);eds.extend([((u,r),(dest,t),1),((dest,t),(u,r),-1)])
   if bad:break
  if bad:counts['port']+=1;continue
  skip=False
  for st in nodes:
   at=st;seen={st}
   while at in succ:
    at=succ[at]
    if at[0]==st[0]:
     if at[1]!=st[1]+1:skip=True
     break
    assert at not in seen;seen.add(at)
   if skip:break
  if skip:counts['skipped rank']+=1;continue
  m=len(nodes);D=[[-10**8]*m for _ in range(m)]
  for i in range(m):D[i][i]=0
  for x,z,vv in eds:D[idx[x]][idx[z]]=max(D[idx[x]][idx[z]],vv)
  for k in range(m):
   for i in range(m):
    for j in range(m):D[i][j]=max(D[i][j],D[i][k]+D[k][j])
  if any(D[i][i]>0 for i in range(m)):counts['positive clock cycle']+=1;continue
  path=[('Y',1)]
  for _ in range(4):
   if path[-1]not in succ:break
   path.append(succ[path[-1]])
  if len(path)!=5 or path[-1]!=('Y',2)or any(r%2!=1 for _,r in path[:-1]):counts['not the prescribed four-L return']+=1;continue
  counts['open']+=1;opens.append(hs)
  assert path==[('Y',1),('A',3),('B',1),('C',1),('Y',2)]
  ar=next(r for r in J['necessary_open_rows']if r['histories']==hs);assert path==list(map(tuple,ar['route']))
  assert set(succ.items())=={((a,r),(b,s))for a,r,b,s,*_ in ar['edges']}
  er=next(r for r in E['rows']if r['histories']==hs)
  for i,rr in enumerate(er['actual_edge_partition']):
   (u,r),(z,s)=path[i:i+2];h=out(hs[u])[r];assert rr['source']==[u,r]and rr['target']==[z,s]and rr['heading']==h
   is_gamma=h==out(hs[u])[0];assert is_gamma==rr['is_gamma']==(i in[0,3])
assert dict(counts)==J['classification']and sum(counts.values())==240
assert set(tuple(h[u]for u in'YABC')for h in opens)=={(y,'NSSN',b,'NSSN')for y in['WEE','WEEW']for b in['WWE','WWEE']}
S=json.loads((R/'audits/check_global_max_flow2_staircase_independent.json').read_text());ww=[r['word']for r in S['open_words']if r['open']];assert len(ww)==8
assert all(w[3]=='X'for w in ww if w[2]=='U')
assert[w for w in ww if w[2]=='O'and w[1]==w[3]=='Y']==[['V','Y','O','Y','V']]
report={'status':'PASS with auxiliary-corner clarification; critical global-max constant-flow2 circle requires singleton LEFT return at least8','proof_sha256':{f:sha(P/f)for f in proofs},'script_sha256':sha(Path(__file__)),'complete_local_counts':dict(counts),'open_profiles':opens,'analytic_checks':['All auxiliary B membership unconstrained, so local cover is a necessary overapproximation even with distant gamma aliases. No off-curve claim is needed.','Each prescribed four-L square uses exactly two gamma second occurrences: Y->A and C->Y. The other physical ports contradict their source first-R departure, which remains true under any full-drift identification.','Global-M signed five-contact cover gives U following RIGHT X while four-L needs Y, so U length4 impossible. O length4 requires V,Y,O,Y,V.','Signed critical actual LEFT-return partition covers each gamma second occurrence once. If all returns short, ell=3q+2p whereas zero turning and disjoint LL pairs implyell>=4q+2p. Thusq=0 and all geometric LEFT are singletonO, contrary to required V caps.','A same-cell same-incoming-heading return has positive length divisibleby4. All doubleLL resets are fixed fourL, so the necessary long return is singletonO/U, length>=8. Long returns reserve remainingell-3q-2p4>=q+2p_long gamma occurrences, not original fuel.'],'not_claimed':['long-return exterior impossible','general one-use','global cap4 front exclusion','fuel or age bound','non-global or noncritical extension']}
p=R/'audits/flow2_nonsquare_returns_independent.json';p.write_text(json.dumps(report,indent=2)+'\n');print(sha(p));print(report['status'])
