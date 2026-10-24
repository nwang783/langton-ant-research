import itertools,json,hashlib,collections
from pathlib import Path
R=Path('/workspace/shared/langton');P=R/'first_departure_multiplicity_2026-10-24'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
proofs={'wall':'constant_flow2_departure_circles_need_actual_LEFT_resets.md','square':'flow2_double_LEFT_reset_has_three_complete_profiles.md','critical':'critical_flow2_departure_circles_have_same_contact_LEFT_returns.md'}
expect=['b019b6d35f033cc38cd1435f6e91f16852b883b744feaa6830d4c5951d91aa1e','c3f16bb34cbd92235eb6740f82f6b57cce6f809822e7131ff854e1a99775fb02','f7297c7b6beaeb864ae3e3827de7f60f7925ca1b8b365177c5a955d34db89f31']
assert [sha(P/f)for f in proofs.values()]==expect
V={'N':1j,'E':1,'S':-1j,'W':-1};I={v:k for k,v in V.items()}
def out(w):return [I[V[h]*(-1j if r%2==0 else 1j)]for r,h in enumerate(w)]
def ranks(w,h,o=False):return [r for r,c in enumerate(out(w)if o else w)if c==h]
alph={};tables={}
for typ,first,depart in [('RIGHT','E','S'),('LEFT','W','N')]:
 a=[]
 for n in range(1,5):
  for tail in itertools.product([first,I[-V[first]]],repeat=n-1):
   w=first+''.join(tail)
   if typ=='LEFT'and(n<3 or w[2]!='E'):continue
   if len(ranks(w,'E'))==len(ranks(w,depart,True))==2:a.append(w)
 alph[typ]=sorted(a)
 for w in a:
  ins=ranks(w,'E');outs=ranks(w,depart,True);ex='LEFT'if typ=='RIGHT'else'RIGHT'
  tab=[]
  for r in range(len(w)):
   li=('RIGHT'if ins.index(r)==0 else'LEFT')if r in ins else ex
   lo=('RIGHT'if outs.index(r)==0 else'LEFT')if r in outs else ex
   tab.append([r,w[r],out(w)[r],li,lo])
  dif=[r for r,*_,li,lo in tab if li!=lo]
  assert dif==([1,2]if w in('WEE','WEEW')else[])
  if dif:assert tab[1][-2:]==['RIGHT','LEFT']and tab[2][-2:]==['LEFT','RIGHT']
  # Every other local port is on the asserted geometric side, for all rotations.
  for z in [1,1j,-1,-1j]:
   for r,h in enumerate(w):
    if r not in ins:assert -V[h]*z==1*z
   for r,h in enumerate(out(w)):
    if r not in outs:assert V[h]*z==(-V[depart])*z
  tables[w]=tab
assert alph=={'RIGHT':['EEWW','EWWE'],'LEFT':['WEE','WEEW','WWEE']}
J=json.loads((P/'check_flow2_LL_reset_square.json').read_text());pos={'Z':0j,'A':1+0j,'B':1+1j,'Y':1j};inv={p:k for k,p in pos.items()}
# Derive rotated alphabet at each actual cycle contact, not a supplied finite list.
roles={}
for k,first,arr,dep,left in [('Z','N','S','E',1),('A','E','E','S',0),('B','S','S','W',0),('Y','E','W','S',1)]:
 a=[]
 for n in range(1,5):
  for tail in itertools.product([first,I[-V[first]]],repeat=n-1):
   w=first+''.join(tail)
   if left and(n<3 or w[2]!=arr):continue
   if len(ranks(w,arr))==len(ranks(w,dep,True))==2:a.append(w)
 roles[k]=sorted(a)
assert roles=={k:sorted(v)for k,v in J['alphabets'].items()}
counts=collections.Counter();openrows=[];witnesses=[]
for val in itertools.product(*(roles[k]for k in 'ZABY')):
 hs=dict(zip('ZABY',val));nodes=[(u,r)for u,w in hs.items()for r in range(len(w))];idx={v:i for i,v in enumerate(nodes)};succ={};eds=[];ing=[];eg=[]
 for u,w in hs.items():
  for r in range(len(w)-1):eds.append(((u,r),(u,r+1),4))
  for h in V:
   dest=inv.get(pos[u]+V[h]);rr=ranks(w,h,True)
   if dest is not None:
    tt=ranks(hs[dest],h);assert len(rr)==len(tt)
    for r,t in zip(rr,tt):succ[u,r]=(dest,t);eds.extend([((u,r),(dest,t),1),((dest,t),(u,r),-1)])
   else:eg.extend((u,r,h)for r in rr)
   if pos[u]-V[h]not in inv:ing.extend((u,r,h)for r in ranks(w,h))
 skip=None
 for st in nodes:
  cur=st;path=[cur];seen={cur}
  while cur in succ:
   cur=succ[cur];path.append(cur)
   if cur[0]==st[0]:
    if cur[1]!=st[1]+1:skip=path
    break
   if cur in seen:raise AssertionError('unexpected disjoint closed component')
   seen.add(cur)
  if skip:break
 if skip:counts['skipped rank']+=1;witnesses.append([hs,'skipped',skip]);continue
 # All-pairs max-plus, a different exact clock feasibility check.
 n=len(nodes);D=[[-10**9]*n for _ in range(n)]
 for i in range(n):D[i][i]=0
 for a,b,c in eds:D[idx[a]][idx[b]]=max(D[idx[a]][idx[b]],c)
 for k in range(n):
  for i in range(n):
   if D[i][k]>-10**8:
    for j in range(n):
     if D[k][j]>-10**8:D[i][j]=max(D[i][j],D[i][k]+D[k][j])
 if any(D[i][i]>0 for i in range(n)):counts['positive clock cycle']+=1;continue
 counts['open']+=1;openrows.append(hs)
 # All supplied channels, every ingress/egress and internal ordinal edge are reconstructed.
 ar=next(r for r in J['necessary_open_rows']if r['histories']==hs)
 assert {(u,r,v,t)for (u,r),(v,t)in succ.items()}=={tuple(e[:4])for e in ar['edges']}
 assert set(ing)=={(e[1],e[2],e[3])for e in ar['ingresses']}
 assert set(eg)=={(e[0],e[1],e[3])for e in ar['egresses']}
assert dict(counts)==J['rejections']and len(openrows)==3
report={'status':'PASS scoped wall, 36-square cover, and conditional critical-level actual same-contact return theorem','proofs':{k:sha(P/v)for k,v in proofs.items()},'script_sha256':sha(Path(__file__)),'complete_alphabets':alph,'local_side_tables':tables,'square_counts':dict(counts),'square_open_rows':openrows,'analytic_checks':['Embedded physical essential b-circle separates the full drift cylinder; every off-circle grid edge and nonlocal chord has one side, and its endpoint exterior port labels agree. Full drift preserves labels; all-V yields two actual successor-invariant nonempty event sets.','O/U repairs pair right incoming L1 with outgoing R2 and left incoming R2 with outgoing L1. All other physical occurrences and actual pairings retained.','For winding-minus-one b-circle, geometric RIGHT contains global LEFT. Piecewise stream h-(c-1) gives right homology c-c_right. Positive actual-edge lengths plus positive T2-T1 imply every right circuit has positive integer time winding; no untouched proper actual orbit.','At c=c_right+1, unique right circuit has winding one and covers every O/U class exactly once. Lifted physical contact sequence gives disjoint ordered intervals T1_i<T2_i<T1_next, repeated by exactly P. This exhausts all crossing events, proving the next actual left excursion returns to the same physical contact, not just quotient class.','Partial graph only is a star; no full canonical graph, geometric simplicity, bounded age or fuel consequence.'],'not_claimed':['general one-use','all constant-flow-two circles excluded','complete realization of open square profiles','full exchange graph beta bound']}
p=R/'audits/flow2_resets_independent.json';p.write_text(json.dumps(report,indent=2)+'\n');print(sha(p));print(report['status'])
