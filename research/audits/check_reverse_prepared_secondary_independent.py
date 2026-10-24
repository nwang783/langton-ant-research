from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23';vec=dict(N=1j,E=1,S=-1j,W=-1);ch={v:k for k,v in vec.items()};rows={'O':[],'E':[]}
for which,axis in [('O','EW'),('E','NS')]:
 for n in range(1,5):
  black=n%2==1
  for hs in product(axis,repeat=n):
   h=''.join(hs);turn=['L'if(k%2==0)==black else'R'for k in range(n)];out=''.join(ch[vec[c]*(1j if t=='L'else-1j)]for c,t in zip(h,turn));rr=Counter(c for c,t in zip(h,turn)if t=='R');ll=Counter(c for c,t in zip(h,turn)if t=='L')
   if which=='O':
    if h.count('W')!=1:continue
    a=-2-rr['W'];C={'NE':-2,'SW':a+rr['E']};L={'NW':a-ll['E'],'SE':a-ll['W']};eta=C['SW']
   else:
    if out.count('E')!=1:continue
    a=-2-rr['N'];C={'SE':-2,'NW':a+rr['S']};L={'NE':a-ll['S'],'SW':a-ll['N']};eta=C['NW']
   if min(L.values()) < -3:continue
   # Exact read-event reversal: original incoming is negative reverse outgoing, in reverse rank order.
   orig=''.join(ch[-vec[c]]for c in out[::-1]);origturn=''.join('R'if t=='L'else'L'for t in turn[::-1]);assert origturn[0]=='R'
   rows[which].append({'h':h,'black':black,'out':out,'C':C,'L':L,'eta':eta,'original_h':orig,'original_turns':origturn,'original_C':{k:-v for k,v in L.items()},'original_L':{k:-v for k,v in C.items()}})
assert{r['h']for r in rows['O']}=={'W','EW','WEE','EEW','EEEW','EWEE'}and{r['h']for r in rows['E']}=={'S','SS','NSS','SSN','SSSN','SNSS'}
pairs=[]
for o,e in product(rows['O'],rows['E']):
 if o['eta']!=e['eta']:continue
 so=[k for k,c in enumerate(o['out'])if c=='S'];si=[k for k,c in enumerate(e['h'])if c=='S']
 if len(so)!=len(si):continue
 nodes=[(a,k)for a,r in [('O',o),('E',e)]for k in range(len(r['h']))];edges=[]
 for a,r in [('O',o),('E',e)]:edges.extend(((a,k),(a,k+1),4)for k in range(len(r['h'])-1))
 for a,b in zip(so,si):edges.extend([(('O',a),('E',b),1),(('E',b),('O',a),-1)])
 edges.append((('O',o['h'].index('W')),('E',e['out'].index('E')),1));t={a:0 for a in nodes}
 for _ in nodes:
  change=False
  for a,b,k in edges:
   if t[b]<t[a]+k:t[b]=t[a]+k;change=True
  if not change:break
 else:continue
 nout=o['out'].count('N');nin=e['h'].count('N');b3o=o['black']and len(o['h'])==3;b3e=e['black']and len(e['h'])==3;assert nout-nin==int(b3o)-int(b3e)
 pairs.append((o['h'],e['h'],o['eta'],nout,nin))
A=json.loads((D/'reverse_locked_rail_secondary_prepared_ports.json').read_text());assert len(pairs)==11 and set(pairs)=={(z['O']['headings'],z['E']['headings'],z['O']['other'],z['next_N_outputs'],z['previous_N_inputs'])for z in A['pairs']}
for which in rows:
 for r in rows[which]:
  if r['black']and len(r['h'])==1:
   assert r['eta']==-2 and set(r['original_C'].values())=={2,3}and set(r['original_L'].values())=={2}
  if r['black']and len(r['h'])==3:
   assert r['eta']==-1 and set(r['original_C'].values())=={3}and set(r['original_L'].values())=={1,2}and r['original_h'][0]!=r['original_h'][2]
# Exact physical five-read singleton route and time conjugacy, no free reset.
reverse_events=[(1j,'L','N'),(-1+1j,'L','W'),(-1,'L','S'),(0j,'L','E'),(1j,'R','N')]
for (p,t,h),(q,_,hi)in zip(reverse_events,reverse_events[1:]):
 out=vec[h]*(1j if t=='L'else-1j);assert p+out==q and out==vec[hi]
forward_events=[(p,'R'if t=='L'else'L',ch[-vec[h]*(1j if t=='L'else-1j)])for p,t,h in reverse_events[::-1]];assert ''.join(t for p,t,h in forward_events)=='LRRRR'
# F_k < S_(k+1): Zk.L3 ->Yk.R2, then Yk.L3 later by at least4, followed by the exact five-port chain to O(k+1).W.
main={0:'WWWE',1j:'NNNS',1:'NNSN',1+1j:'EEWE',2j:'WWWE',3j:'NNNS',1+2j:'NNSN'}
route=[(0,3),(1j,2),(1j,3),(1+1j,3),(1+2j,3),(2j,2),(3j,1)]
for (p,k),(q,j)in zip(route,route[1:]):
 if p==q:
  assert (k,j)==(2,3);continue
 out=vec[main[p][k]]*(-1j if k%2==0 else 1j);assert p+out==q and out==vec[main[q][j]]
files=['reverse_locked_rail_prepared_secondary_interfaces.md','reverse_locked_rail_secondary_prepared_ports.py','reverse_locked_rail_secondary_prepared_ports.json'];hashes={f:hashlib.sha256((D/f).read_bytes()).hexdigest()for f in files};assert hashes[files[0]]=='c39497b8456f8ebe9b1b1e4bef96b27ce05c8e998524b227130c175214a8f356'
out={'status':'PASS conditional prepared locked-rail secondary interfaces and exact full-period count','source_hashes':hashes,'fresh_profiles':rows,'eleven_same_eta_pairs':pairs,'reverse_singleton_route':[(str(p),t,h)for p,t,h in reverse_events],'original_reverse_event_route':[(str(p),t,h)for p,t,h in forward_events],'main_F_to_nextS_edges':[(str(p),k)for p,k in route],'analytic_review':[
'All reverse histories are classified by actual original WHITE reversal: WHITEeven2or4 and BLACKodd1or3. Imposing exactly one W input atO or one E output atE, the genuine baselineC=-2 and globalLfloor-3 gives precisely six histories each. No other off-Q cell is assumed WHITE; black singleton and blackLRL suppliers are necessary retained possibilities.',
'Independent complete same-pair S ordinal matching, actual rank gaps4 and strictS<F leave exactly11 pairs. The main locked port chain separately verifiesF<Snext (the exact Z3-to-Y2 port, later Y3, and successive B3/A_next3/Z_next2/Y_next1 ports give strict ordering). The secondaryN and farther external ports are not presumed solved.',
'At eta-2 the unique BLACK singletons force the literal reverse five-event LLLLR path, each arrow one physical update. Read-event conjugacy, not an unshifted heading reversal, gives original LRRRR. Both original singleton outputs are topC=M/M-1 and L=M-1. At eta-1 BLACK3 endpoints reverse to opposite-R three-read outputs with originalC=M/M and originalL=M-1/M-2, so they are shallow and not roots ofM-3.',
'For each same-eta pair, Nout(O)-Nin(E)=indicatorBLACK3O-indicatorBLACK3E. Summing complete physical N edges in the actual full vertical quotient gives equal BLACK3 counts. Eta0 white4 counts cancel pairwise. Eta-2 contributes two singletons, and checker parity preventsO/E aliasing because full drift is(0,2a). Thus exactly2(B1+B3) distinct secondary odd classes are registered, but they may overlap other output reservations.',
'Eta0 identifies another same-height reverseC face separated fromQ by the low row, not automatically the same plateau, root-free, or locally maximal. Deeper or odd-rooted suppliers, exterior realization and full rail composition remain open. No seed fuel or additional disjoint output budget is inferred.'
]}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(pairs)
