from pathlib import Path
from itertools import product
from collections import Counter,defaultdict
import json,hashlib
S=Path(__file__);R=S.parents[1];P=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
proof=P/'mixed_LL_zero_chord_bridges_and_critical_last_LEFT_gate.md';assert sha(proof)=='dba869f472061078537c45b980381287271cea9aeb6fcde55b56d9555b2d5a07'
# Reuse our previously independent generic port/next-return/max-plus engine, with NO global-height cutoff.
src=(S.parent/'check_odd_eight_return_interface_independent.py').read_text().split('count=Counter();opens=[]')[0]
src=src.replace(" if any(z>0 for p,z in val.items()if(int(p.real)+int(p.imag))%2):return'global_C_max',None",' # No outside/global C maximum is imposed here.')
ns={'__file__':str(S.parent/'check_odd_eight_return_interface_independent.py')};exec(src,ns)
check=ns['check'];out=ns['out'];ranks=ns['ranks'];V=ns['V'];xy=ns['xy']
pos=dict(Z=0j,A=1+0j,B=1+1j,Y=1j);inv={v:k for k,v in pos.items()}
allw=lambda axis:[''.join(x)for n in range(1,5)for x in product(axis,repeat=n)]
a={
'Z':[h for h in allw('NS')if h[0]=='N'and h.count('S')==2 and out(h).count('E')==2],
'Y':[h for h in allw('EW')if h[0]=='E'and h.count('W')==2 and out(h).count('S')==2],
'A':[h for h in allw('EW')if h[0]=='E'and h.count('E')==2 and out(h).count('S')>=2],
'B':[h for h in allw('NS')if h[0]=='S'and out(h).count('W')==2 and h.count('S')>=2]}
assert set(a['Z'])=={'NSS','NNSS','NSSN'}and set(a['Y'])=={'EWW','EEWW','EWWE'}
assert set(a['A'])=={'EEWW','EWWE','EWE','EWEW'}and set(a['B'])=={'SSNN','SNNS','SSS','SSSS'}
J=json.loads((P/'check_mixed_LL_zero_chord_interface.json').read_text());counts=Counter();good=[]
for hs0 in product(*(a[u]for u in pos)):
 hs=dict(zip(pos,hs0));raw={pos[u]:h for u,h in hs.items()};why,succ=check(raw);counts[why]+=1
 if why!='open':continue
 rec=next(r for r in J['necessary_open_rows']if r['histories']==hs);good.append(hs)
 edges=[];ing=[];eg=[]
 for u,h in hs.items():
  p=pos[u]
  for dr,v in V.items():
   q=p+v
   if q in inv:
    target=inv[q]
    for j,(r,s)in enumerate(zip(ranks(h,dr,'out'),ranks(hs[target],dr)),1):edges.append([u,r,target,s,dr,j])
   else:
    for j,r in enumerate(ranks(h,dr,'out'),1):eg.append([u,r,xy(q),dr,j])
   q=p-v
   if q not in inv:
    for j,r in enumerate(ranks(h,dr),1):ing.append([xy(q),u,r,dr,j])
 canon=lambda x:sorted(json.dumps(y,sort_keys=True)for y in x)
 assert canon(edges)==canon(rec['edges'])and canon(ing)==canon(rec['ingresses'])and canon(eg)==canon(rec['egresses'])
 channels=[]
 for entry in ing:
  at=pos[entry[1]],entry[2];route=[at]
  while at in succ:at=succ[at];assert at not in route;route.append(at)
  egress=next(e for e in eg if e[:2]==[inv[at[0]],at[1]])
  channels.append(dict(ingress=entry,route=[[inv[p],r]for p,r in route],egress=egress,physical_steps=len(route)+1))
 assert canon(channels)==canon(rec['channels'])
 # Independent face-jump construction. Normalize selected C face (-1,0) to c=0.
 eq={};adj=defaultdict(list)
 for p,h in raw.items():
  ia='NS'if(int(p.real)+int(p.imag))%2==0 else'EW';oa='EW'if ia=='NS'else'NS'
  for d in oa:eq[p,d]=out(h).count(d)
  for d in ia:eq[p-V[d],d]=h.count(d)
 for(p,d),f in eq.items():
  c,l={'E':(p-1j,p),'W':(p-1,p-1-1j),'N':(p,p-1),'S':(p-1-1j,p-1j)}[d]
  adj[l].append((c,f));adj[c].append((l,-f))
 val={-1+0j:0};todo=[-1+0j]
 while todo:
  x=todo.pop()
  for y,k in adj[x]:
   if y in val:assert val[y]==val[x]+k
   else:val[y]=val[x]+k;todo.append(y)
 chord=out(hs['A']).count('N');assert chord==hs['B'].count('N')
 assert val[0]==-2 and val[1]==chord-2
 mixed=chord==0;assert mixed==rec['zero_chord_mixed']
 if hs['Y']in('EWW','EWWE')and hs['Z']=='NNSS':
  at=(1j,1);route=[at]
  for _ in range(2):at=succ[at];route.append(at)
  assert route==[(1j,1),(0j,3),(1+0j,2 if mixed else 1)]
assert dict(counts)==J['all144_counts']and len(good)==39
assert sum(h['A']in('EWE','EWEW')for h in good)==36
assert sum(h['Z']=='NNSS'for h in good)==15
# Critical last-LEFT ordinal identities for all eligible incoming/outgoing flow types.
left=['WWE','WWEW','WEE','WEEW','WWEE','WEEE'];ordinal=[]
for h in left:
 incoming=ranks(h,'E');outgoing=ranks(h,'N','out')
 assert len(incoming)==len(outgoing)
 if h in('WEE','WEEW','WEEE'):assert incoming[0]==1 and outgoing[0]==0
 # Rotate predecessor by quarter-turn so its first output feeds successor's incoming cycle port.
 # Only indices, not heading letters, enter this argument.
 if h in('WEE','WEEW','WEEE'):assert outgoing[:2]==[0,1]
 if h=='WWEE':assert outgoing==[0,3]
 ordinal.append(dict(history=h,cycle_arrivals=incoming,cycle_departures=outgoing))
obj=dict(status='PASS complete mixed LL inventory and conditional critical last-LEFT gate',proof=sha(proof),author_checker=sha(P/'check_mixed_LL_zero_chord_interface.py'),author_certificate=sha(P/'check_mixed_LL_zero_chord_interface.json'),independent_engine=sha(S.parent/'check_odd_eight_return_interface_independent.py'),derived_alphabets=a,counts=dict(counts),open39=good,critical_remaining15=[h for h in good if h['Z']=='NNSS'],left_ordinal_profiles=ordinal,analytic_review=[
'All144 complete WHITE cap4 profiles derived from first-R output and exact boundary port counts; no global exterior-height bound used. Full internal edges, zero ports, max-plus rank inequalities, next-read returns, all exterior ingresses/egresses and every complete local channel independently agree.',
'With selected C normalized0, intervening L is -2 and right C is chord_flow-2. Thus mixed zero-flow chord has both heights -2; old flat chord has C0. All36 mixed and3 old rows retained.',
'For a second-LEFT crossing v, preceding crossing u gives T1v=T0u+1<T1u<T2v=T1u+1<T2u. Critical same-PHYSICAL-return intervals cannot overlap. If preceding u is V, interval(T0u+1,T3u+1) contains RIGHT events uL1/uR2. Flow1 cannot supply the required2/3 port; no other LEFT profile remains.',
'Therefore Z=V leaves15 necessary interfaces. First-LL O/U sends actual L1->ZL3->AR2 in the zero-chord case. Its first three turns LLR preclude a4-step same-heading return, so at least8; no old-stock/fresh-fuel claim.',
'No full-board factor, global one-event orbit, completion, indefinite repetition or front existence is inferred. Constant-two singleton-U nesting exclusion is NOT imported into mixed LL geometry.'
]);S.with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print(obj['status']);print(sha(S.with_suffix('.json')))
