from pathlib import Path
from itertools import product
from collections import Counter,defaultdict
import json,hashlib
S=Path(__file__);R=S.parents[1];P=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();proof=P/'odd_eight_step_returns_keep_a_mixed_open_stock_transfer.md';assert sha(proof)=='2dd610223aefd981ecfd4f41a2741346f8c5c350f88ef681813171d9acc0e8b7'
J=json.loads((P/'check_odd_eight_return_open_interface.json').read_text());V={'N':1j,'E':1,'S':-1j,'W':-1};I={v:k for k,v in V.items()};out=lambda w:[I[V[h]*(-1j if r%2==0 else 1j)]for r,h in enumerate(w)];ranks=lambda w,h,kind='in':[r for r,c in enumerate(out(w)if kind=='out'else w)if c==h]
xy=lambda p:[int(p.real),int(p.imag)];words=lambda axis:[''.join(w)for n in range(1,5)for w in product(axis,repeat=n)]
def literal(w,board=None):
 p=0j;h=1;last={};trace=[];early=False;bad=False;B=None if board is None else set(board)
 for i,c in enumerate(w):
  trace.append((p,h,c));early|=i>0 and p==0
  if p in last and last[p]==c:bad=True
  last[p]=c
  if B is not None:assert(p in B)==(c=='L');B.symmetric_difference_update({p})
  h*=(-1j if c=='R'else 1j);p+=h
 return p,h,early,bad,trace,B
raw=[];legal=[]
for w in product('RL',repeat=7):
 w='L'+''.join(w);p,h,early,bad,trace,B=literal(w)
 if p==0 and h==1 and not early:
  raw.append(w)
  if not bad:legal.append(w)
assert raw==J['eight_step_raw_full_pose_words']and legal==['LLRRRRLL','LLLRRRRL']
assert literal('LLLRRRRL')[4][3][0]==-1 and literal('LLLRRRRL')[4][3][2]=='R'
seed={0,1j,-1};p,h,early,bad,trace,B=literal('LLRRRRLL',seed);assert B=={1j,-1+2j,2j}and len(B)==3 and 0 not in B
for r,(p,h,c)in zip(J['literal_prepared_transfer']['trace'],trace):assert r['cell']==xy(p)and r['incoming']==I[h]and r['turn']==c
# Independent full internal rank graph, max-plus closure, and every physical edge's face jump.
def check(hs,details=False):
 nodes=[(p,r)for p,w in hs.items()for r in range(len(w))];succ={};eq={};eds=[]
 def pute(p,d,m):
  key=(p,d)
  if key in eq and eq[key]!=m:return False
  eq[key]=m;return True
 for p,w in hs.items():
  eds.extend(((p,r),(p,r+1),4)for r in range(len(w)-1))
  ia='NS'if(int(p.real)+int(p.imag))%2==0 else'EW';oa='EW'if ia=='NS'else'NS'
  for d in oa:
   if not pute(p,d,len(ranks(w,d,'out'))):return'port',None
  for d in ia:
   if not pute(p-V[d],d,len(ranks(w,d))):return'port',None
  for d in V:
   q=p+V[d]
   if q not in hs:continue
   a=ranks(w,d,'out');b=ranks(hs[q],d)
   if len(a)!=len(b):return'port',None
   for r,t in zip(a,b):succ[p,r]=(q,t);eds.extend([((p,r),(q,t),1),((q,t),(p,r),-1)])
 for start in nodes:
  at=start;seen={at}
  while at in succ:
   at=succ[at]
   if at[0]==start[0]:
    if at[1]!=start[1]+1:return'skipped_rank',None
    break
   if at in seen:return'event_cycle',None
   seen.add(at)
 # All-pairs max-plus, independent of the author's Bellman relaxation order.
 ids={n:k for k,n in enumerate(nodes)};n=len(nodes);dd=[[-10**7]*n for _ in range(n)]
 for k in range(n):dd[k][k]=0
 for a,b,w in eds:dd[ids[a]][ids[b]]=max(dd[ids[a]][ids[b]],w)
 for k in range(n):
  for i in range(n):
   if dd[i][k]<-10**6:continue
   for j in range(n):dd[i][j]=max(dd[i][j],dd[i][k]+dd[k][j])
 if any(dd[i][i]>0 for i in range(n)):return'clock_cycle',None
 adj=defaultdict(list)
 for(p,d),f in eq.items():
  # C face on right of directed primal edge, L face on left.
  c,l={'E':(p-1j,p),'W':(p-1,p-1-1j),'N':(p,p-1),'S':(p-1-1j,p-1j)}[d]
  adj[l].append((c,f));adj[c].append((l,-f))
 val={1j:0};todo=[1j]
 while todo:
  p=todo.pop()
  for q,w in adj[p]:
   if q in val:
    if val[q]!=val[p]+w:return'height_cycle',None
   else:val[q]=val[p]+w;todo.append(q)
 assert len(val)==len(adj)
 if any(z>0 for p,z in val.items()if(int(p.real)+int(p.imag))%2):return'global_C_max',None
 return'open',succ
count=Counter();opens=[]
for b,d,e,p,q in product(['WWE','WWEE'],words('NS'),words('EW'),['NNSS','NSSN'],['EEWW','EWWE']):
 hs={1j:'WEE',2j:'NNSS',-1+1j:'NSSN',-1+2j:b,-1+3j:d,3j:e,1+2j:'WWEE',1+3j:p,2+3j:q,2+2j:'NNSS'}
 why,succ=check(hs);count[why]+=1
 if why!='open':continue
 record=next(r for r in J['necessary_open_rows']if r['variable_profiles']==dict(B=b,D=d,E=e,P=p,Q=q));opens.append((b,d,e,p,q))
 path=[(1j,1)]
 for _ in range(8):path.append(succ[path[-1]])
 assert path[-1]==(1j,2)and ''.join('RL'[r%2]for _,r in path[:-1])=='LLRRRRLL'
 assert path[3]==(-1+3j,0)and path[4]==(3j,0)
 assert path==[(complex(*p),r)for p,r in record['eight_step_actual_route']]
 assert set(succ.items())=={((complex(*r['source']),r['source_rank']),(complex(*r['target']),r['target_rank']))for r in record['all_internal_ordinal_edges']}
 # Build every external-to-external named channel, including notional zero ports in helper domains.
 starts=[];ends={};ext=set();channels=[]
 for pos,w in hs.items():
  for hh in V:
   a=pos-V[hh];z=pos+V[hh]
   if a not in hs:
    ext.add(a)
    for ord,r in enumerate(ranks(w,hh)):starts.append((a,hh,ord,(pos,r)))
   if z not in hs:
    ext.add(z)
    for ord,r in enumerate(ranks(w,hh,'out')):ends[pos,r]=(z,hh,ord)
 for a,hh,ord,at in starts:
  route=[at]
  while route[-1]in succ:route.append(succ[route[-1]]);assert len(route)==len(set(route))
  z,di,jj=ends[route[-1]];channels.append((a,hh,ord,z,di,jj,route))
 loops=[l for l in channels if l[0]==l[3]];assert len(loops)==1
 a,hh,ord,z,di,jj,route=loops[0];assert(a,hh,ord,di,jj,len(route)+1)==(1+1j,'W',0,'S',1,4)
 assert route==[(1j,0),(2j,0),(1+2j,2)]
 for x in ext:
  axis='NS'if(int(x.real)+int(x.imag))%2==0 else'EW';candidates=[]
  for hw in words(axis):
   valid=True
   for hh in V:
    if x+V[hh]in hs:valid&=len(ranks(hw,hh,'out'))==len(ranks(hs[x+V[hh]],hh))
    if x-V[hh]in hs:valid&=len(ranks(hw,hh))==len(ranks(hs[x-V[hh]],hh,'out'))
   if not valid:continue
   for a,hh,ord,z,di,jj,route in loops:
    if a==x:valid&=ranks(hw,di)[jj]==ranks(hw,hh,'out')[ord]+1
   if valid:candidates.append(hw)
  ref=next(r for r in record['all_unfilled_external_helpers']if r['cell']==xy(x));assert candidates==ref['complete_WHITE_histories']and candidates
  if x==1+1j:
   assert set(candidates)=={'SS','SSN'}
   for hw in candidates:assert check(hs|{x:hw})[0]=='open'
assert dict(count)==J['complete_neighbor_cover_counts']and len(opens)==14
expected=[('WWE','N','EWW'),('WWE','NS','EWWE'),('WWE','NSS','EWWE'),('WWEE','NN','EWW'),('WWEE','NNS','EWW'),('WWEE','NNSS','EWWE'),('WWEE','NSSN','EWWE')]
assert set(opens)=={(b,d,e,'NSSN',q)for b,d,e in expected for q in('EEWW','EWWE')}
# Signed five-contact language and actual LL restriction establish the chosen RR junction.
lang=json.loads((P/'flat_flow2_symbolic_row_with_odd_left.json').read_text());ww=[tuple(r[k]for k in('Bprev','A','B','Anext','Bnext'))for r in lang['rows']if r['open_completions']]
assert[w for w in ww if w[2]=='O'and w[1]=='Y'and w[3]=='X']==[('V','Y','O','X','V')]
assert not any(w[2]=='V'for w in ww)
outobj=dict(status='PASS necessary odd-eight mixed open interface and separate prepared finite transfer',proof=sha(proof),author_checker=sha(P/'check_odd_eight_return_open_interface.py'),author_certificate=sha(P/'check_odd_eight_return_open_interface.json'),all128_firstL_return_words_checked=True,fullpose_first_returns=raw,letter_legal=legal,complete_7200_cover=dict(count),all14_open_profiles=opens,prepared_factor_initial=[xy(p)for p in seed],prepared_factor_final=[xy(p)for p in B],analytic_review=[
'LLLRRRRL visits predecessor C with R four steps after its forced R0 feeding first E arrival at rootL1. A distinct second R needs intervening L and two >=4 same-cell gaps, so impossible. No old stock exclusion is needed.',
'The surviving root and adjacent RIGHT profiles give globalM V,Y,O,X,V caps. Next V cannot start LL because its preceding RIGHT is X, whereas signed LL cover requires Y. If next RIGHT singleton the next staircase has forbidden middle V, forcing RR. This is a mixed junction, not homogeneous repetition.',
'All complete WHITE length1..4 D/E histories admitted before classification. Every named physical ordinal port, zero-port face jump, actual next-read return and max-plus rank constraint independently reconstructed. Only the14 necessary networks survive and then force the two displayed R0 reads.',
'All external named channels/helper port domains reconstructed. K firstW-to-secondS four-step first return admits SS/SSN and both remain locally clock/height compatible. No complete period phases, single physical event orbit or outer-field realization inferred.',
'The separate explicit three-black8-turn board factor is genuine, mass3->3, returns same head/heading and leaves root WHITE. It cannot immediately repeat and is not a full WHITE front or renewable stock source.'
]);S.with_suffix('.json').write_text(json.dumps(outobj,indent=2)+'\n');print(outobj['status']);print(sha(S.with_suffix('.json')))
