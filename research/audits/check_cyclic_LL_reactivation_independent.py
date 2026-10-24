from pathlib import Path
from collections import Counter,deque
from itertools import product
import ast,json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'cyclic_LL_roots_have_only_four_or_eight_step_X_reactivation.md';F=D/'check_LL_cyclic_supplier_reactivation_modes.json';assert sha(P).startswith('7a4d0c56')and sha(F).startswith('f3a9ddad')and sha(D/'check_LL_cyclic_supplier_reactivation_modes.py').startswith('3a5e2fe4');J=json.loads(F.read_text())
ns={'__file__':str(S.with_name('check_global_max_flow2_staircase_independent.py'))};exec(Path(ns['__file__']).read_text().split('rows=[];stats=Counter()')[0],ns);H,V,out,cv,string,NS,EW,cin,cout,test=[ns[k]for k in('H','V','out','cv','string','NS','EW','cin','cout','test')];xy=lambda p:[int(p.real),int(p.imag)]
pts=[complex(x,y)for x,y in product(range(3),repeat=2)];adj={p:[(p+v,h)for h,v in enumerate(V)if p+v in pts]for p in pts}
def port(w,p,h):return cout(w,h)if h%2!=int(p.real+p.imag)%2 else cin(w,(h+2)%4)
def reduce(ds):
 queue=deque(ds)
 while queue:
  p=queue.popleft()
  for q,h in adj[p]:
   vals={port(w,p,h)for w in ds[p]};keep=[w for w in ds[q]if port(w,q,(h+2)%4)in vals]
   if not keep:return
   if len(keep)<len(ds[q]):ds[q]=keep;queue.append(q)
 return ds
mapped={'skipped':'skipped_rank','clock':'clock_cycle','global_max':'global_C_max','open':'open','port':'port','height_cycle':'height_cycle','event_cycle':'event_cycle'};total=Counter();survivors=[];placements=0
for root in('EWW','EWWE'):
 fixed={0j:cv('NNSS'),1j:cv(root),1:cv('EEWW'),1+1j:cv('SNNS')};ds={p:[fixed[p]]if p in fixed else(NS[:]if int(p.real+p.imag)%2==0 else EW[:])for p in pts};counts=Counter();local=[]
 def search(ds):
  ds=reduce(ds)
  if ds is None:return
  und=[p for p in pts if len(ds[p])>1]
  if und:
   p=min(und,key=lambda p:len(ds[p]))
   for w in ds[p]:search(ds|{p:[w]})
   return
  hs={p:v[0]for p,v in ds.items()};res,wit=test(hs);counts[mapped[res]]+=1
  if res=='open':local.append(hs)
 search(ds);row=next(r for r in J['roots']if r['root']==root);assert dict(counts)==row['full_count_compatible_rejections']and len(local)==row['open_local_profiles'];total.update(counts)
 necessary=[hs for hs in local if string(hs[1+2j])=='EEWW'and string(hs[2+2j])in('SNNS','SSNN')];assert len(necessary)==3
 refs={tuple(sorted(r['histories'].items())):r for r in row['cyclic_necessary_profiles']};seen=set()
 for hs in necessary:
  sh={str((int(p.real),int(p.imag))):string(w)for p,w in hs.items()};key=tuple(sorted(sh.items()));seen.add(key);r=refs[key];assert string(hs[2j])==('SSN'if root=='EWW'else'SSNN')
  tw,dw,rw=[string(hs[q])for q in(2+2j,2+1j,2+0j)]
  if tw=='SNNS':assert(dw,rw)==('EWWE','NNSS');kind='P';tags=['T_RIGHT_Y_with_preceding_flat_RR']
  else:
   assert(dw,rw)in[('WEE','NNS'),('WEEW','NNSS')];kind='N';tags=['T_RIGHT_X_with_preceding_flat_RR']
   if dw=='WEEW':tags+=['T_LEFT_V_with_D_RIGHT_Y']
  assert r['kind']==kind and r['placement_tags']==tags;placements+=len(tags)
  succ={}
  for p,w in hs.items():
   for h,v in enumerate(V):
    if p+v not in hs:continue
    a=[i for i in range(len(w))if out(w,i)==h];b=[i for i,c in enumerate(hs[p+v])if c==h];assert len(a)==len(b);succ.update({(p,i):(p+v,j)for i,j in zip(a,b)})
  path=[(2+0j,1)]
  while path[-1]!=(1+0j,3):assert len(path)<20 and path[-1]in succ;path.append(succ[path[-1]])
  word=''.join('R'if i%2==0 else'L'for p,i in path);assert word==('LRRRRL'if kind=='P'else'LRRLLLLRRL')==r['word']and [[xy(p),i]for p,i in path]==r['actual_reactivation_channel']
  assert len(path)-1-path.index((1+0j,2))==r['X_age23']==(4 if kind=='P'else 8)
  if kind=='N':assert path.index((1+1j,3))-path.index((1+1j,2))==4 and path.index((1+1j,3))-path.index((1+0j,3))==-3
  survivors.append(dict(root=root,kind=kind,histories=sh,placements=tags,channel=word))
 assert seen==set(refs)
assert dict(total)==J['all_stock_count_compatible_counts']and sum(total.values())==6102 and total['open']==46 and placements==8
# Exact owner-length possibilities are full physical first returns.
def walk(w,p,h):
 q=p;early=False
 for t,c in enumerate(w):h=(h+(1 if c=='R'else-1))%4;p+=V[h];early|=(p==q and t+1<len(w))
 return p,h,early
frames=[]
for body in('LRRRRL','LRRLLLLRRL'):
 ff=[]
 for k in(1,2):
  for extras in product('LR',repeat=2):
   pre=''.join(extras[:k]);post=''.join(extras[k:])
   if pre[0]!='L':continue
   for h in range(4):
    p,hh,_=walk(pre,0j,h)
    if hh!=0:continue
    root=2-p;w=pre+body+post;p,hh,early=walk(w,root,h)
    if(p,hh,early)==(root,h,False):ff.append(dict(root=xy(root),incoming=H[h],word=w))
  # k enumeration does not assume individual ages belowP.
 r=next(r for r in J['owner_frames']if r['channel']==body);assert ff==r['only_frames']and r['excluded_minimum_owner_span']==len(body)+2 and r['required_owner_span_at_least']==len(body)+6;frames.append(r)
# Bind the signed physical/topological gates, no off-cycle positive controls.
reports=['check_mixed_RR_closure_independent.json','check_mixed_LL_gate_independent.json','check_mixed_flow2_flat_islands_independent.json','check_global_max_flow2_staircase_independent.json','check_negative_L3_span_owner_independent.json','check_fixed_LL_supplier_incidence_independent.json']
for f in reports:assert json.loads(S.with_name(f).read_text())['status'].startswith('PASS')
O=dict(status='PASS six necessary cyclic LL-root supplier inventories, eight placements, exact X reactivation4/8 and owner gates',proof=sha(P),certificate=sha(F),script=sha(S),signed_dependencies={f:sha(S.with_name(f))for f in reports},complete_patch_counts=dict(total),necessary_inventories=survivors,owner_frames=frames,analytic_review=[
'All empty and completeWHITE1..4 histories at every unknown3x3 cell are retained. Exact zero/nonzero radial port matching and exhaustive domain recursion reconstruct6102 patches; independently implemented physical successor ranks, positive-clock cycle extraction, and all dual-face equations at GLOBALM leave46. No period, exterior age or guessed supplier first-heading bound is imposed.',
'For a true cyclic LLroot, Y incomingS forces U as predecessor. RIGHTU would put RR immediately before crossingrootr, forbidden by generalRR closure; crossingLEFTU violates either secondLEFT or singleton-island outerV. Thus U is passiveV=EEWW. Its predecessorT startsS. SNN is forbidden asRIGHT by one-use input or asLEFTO by followingY instead of requiredX. SNNS can only RIGHTY; SSNN is RIGHTX or LEFTV. Exactlysix complete inventories survive. This explicitly excludes the formerly off-cycle8a controls, not reinstates them.',
'For RIGHTT, precedingQ must RIGHT because LEFTQ gives the actual complete five-corner window Q,T,U,Y,r with forbidden passive middleU. GeneralRR then makesQ flat. For LEFTT, N3 D=WEE has a one-use incoming selected edge; onlyN4 D=WEEW permits cyclic RIGHTY. These are eight necessary placement tags, with exteriorQ and all other stock still unknown.',
'All internal physical ordinal edges regenerate actual LRRRRL inP and LRRLLLLRRL inN. Xage23 is exactly4/8; N Yage23=4 and signedL3tail=-3. P tail=A23Y-3>0 retains arbitrary oldY stock. These are conditional literal channels, not phase-remainder arithmetic or attained prepared factors.',
'P-side detail: Y.R2 has a LEFT off-boundary output. Its successor D.R0 would be RIGHT for EITHER possible Gamma role, RIGHT contact or LEFTU. Thus D is necessarily offGamma in this side argument, not only excluded asLEFTU. R cannot LEFTV because its L1 would beRIGHT while its edge enters X.R2 LEFT; if RIGHT its L1/R2 areLEFT. Therefore the whole P channel staysLEFT. N uses independently signed generic negative-channel side proof. No unrecorded contact crossing splits either channel.',
'Each owner contains the known six/ten events, with at least one earlier rootL1 and later returnR2. A minimal8/12 owner has exactly the two enumerated full-pose frames. The2,-1E frame is forbidden secondLEFT; the1,-1S frame receives the actual two-use edge from flatX and is an excluded f2root afterX. Owner span must therefore>=12/16. Owners may coincide or be translates; no injection or fuel addition is claimed.',
'Full completeWHITEcap4, GLOBALcriticalM,no-one-use and genuine LLfirstO/U scope remain. PassiveVV notches, six-profile realizability, fullfront exclusion and iterative stock bounds remain open.'
]);S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
