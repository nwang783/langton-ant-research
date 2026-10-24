from pathlib import Path
from itertools import product
import json,hashlib
S=Path(__file__).resolve(); R=S.parents[1];D=R/'actual_G7_all_actor_clock_window_2026-10-24'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(D/'manifest.json')=='8a42ec220d1f69a61d5d5ad808be76207669ec99fa6d20ab86e6ed29cd06e123'
m=json.loads((D/'manifest.json').read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
q=R/'audits/check_one_foreign_contact_C_window_independent.py';ns={'__file__':str(q)};exec(q.read_text().split('def inside')[0],ns)
W,M,walk,center,xy,principal,plus,minus=[ns[k]for k in('W','M','walk','center','xy','principal','plus','minus')]
J=json.loads((D/'all_actor_window.json').read_text()); A={'D':(1,0),'C':(1,0),'V':(2,-1),'U':(2,0),'F_prefix':(4,1),'Q_tail':(2,0),'B_tail':(2,1)}
rot=lambda h:(-1j)**h
pieces={}; exits={}
for w in 'DCVUFQB':
 z=walk(W[w]);exits[w]=(z['p'],z['h']);p=[center(0j,0)]
 if w in 'QB':t=walk(W['F']);p.append(center(t['p'],t['h']))
 p.append(center(z['p'],z['h']));kinds=[w]if w in'DCVU'else ['F_prefix']+([w+'_tail']if w in'QB'else[])
 pieces[w]=list(zip(kinds,[v-u for u,v in zip(p,p[1:])]))
# Infer each local principal join directly from literal endpoint-vector rays.
def infer(u,v):
 ans=[]
 for a,b in product(range(-4,5),range(-2,3)):
  try:principal(xy(u),xy(v),(a,b));ans.append((a,b))
  except AssertionError:pass
 assert len(ans)==1,(u,v,ans)
 return ans[0]
local=[]
for a,b in product('DCVUFQB',repeat=2):
 x,u=pieces[a][-1];y,v=pieces[b][0];v*=rot(exits[a][1])
 if x==y=='F_prefix':assert not walk(W[a]+W[b])['feasible'];continue
 c=infer(u,v);inc=2*(a=='C')+4*(x=='F_prefix')-8*(a=='C'and b in'FQB')
 assert c==plus((inc,0),minus(A[y],A[x]));local.append([a,b,c])
for w in'QB':
 (x,u),(y,v)=pieces[w];c=infer(u,v);assert c==plus((4,0),minus(A[y],A[x]));local.append([w,'internal_F56',c])
# Source/actor realization is only a tangent control, not a physical-word claim.
# U separators avoid reversing F->F and the prohibited C->FOREIGN wrap.
def actual_partial(src,tgt,middle):
 sw={'F_prefix':'Q','Q_tail':'Q','B_tail':'B'}.get(src,src)
 tw={'F_prefix':'Q','Q_tail':'Q','B_tail':'B'}.get(tgt,tgt)
 words=[sw,'U']+middle+['U',tw]; allp=[];h=0
 for wi,w in enumerate(words):
  allp += [(wi,k,v*rot(h))for k,v in pieces[w]];h=(h+exits[w][1])%4
 start=next(i for i,(wi,k,v)in enumerate(allp)if wi==0 and k==src)
 end=next(i for i,(wi,k,v)in enumerate(allp)if wi==len(words)-1 and k==tgt)
 total=(0,0)
 for (_,_,u),(_,_,v)in zip(allp[start:end],allp[start+1:end+1]):total=plus(total,infer(u,v))
 K=sum(w=='C'for w in words[:-1]); f=sum(w in'FQB'for w in words[1:-1])
 return words,total,K,f

def form(src,tgt,L):return plus((2*L+4*(src=='F_prefix')+4*(tgt in('Q_tail','B_tail')),0),minus(A[tgt],A[src]))
def inside(c):
 lo,hi=sorted((c[0],sum(c)))
 if lo>=4 and hi<=12 and not(c[1]==0 and c[0]in(4,12)):return True
 assert hi<=4 or lo>=12
 return False
rows=[]; controls=[]
for src,tgt in product(A,repeat=2):
 offset=form(src,tgt,0);assert min(offset[0],sum(offset))>=-2 and not(offset[1]==0 and offset[0]<=-2)
 allow=[L for L in range(8)if inside(form(src,tgt,L))];assert min(form(src,tgt,8)[0],sum(form(src,tgt,8)))>12
 pairs=[]
 for L in allow:
  for f in range(L//2+1):
   K=L-2*f
   if src=='C'and K==0:continue
   pairs.append(dict(L=L,actual_C_count_K=K,strictly_intervening_complete_foreigns_f=f,foreign_Fprefix_pieces_touched=f+(src=='F_prefix')+(tgt not in'DCVU'),foreign_WORDS_touched=f+(src not in'DCVU')+(tgt not in'DCVU'),max_ordinary_monotone_epochs=K+f+1))
 au=next(z for z in J['all49_source_actor_windows']if(z['source_piece'],z['actor_piece'])==(src,tgt))
 assert au['allowed_L']==allow and au['all_necessary_K_f_pairs']==pairs
 for z in au['all8_exact_angle_bounds']:
  assert tuple((z['T_coeff_pi_over4'],z['T_coeff_beta']))==form(src,tgt,z['L'])and z['in_strict_Jordan_window']==inside(form(src,tgt,z['L']))
 for middle in([],['C','U'],['Q','U'],['C','U','B','U','C','U','Q','U']):
  words,c,K,f=actual_partial(src,tgt,middle);assert c==form(src,tgt,K+2*f);controls.append(dict(source=src,actor=tgt,words=words,turn=c,K=K,f=f))
 rows.append(dict(source=src,actor=tgt,offset=offset,allowed_L=allow,K_f_pairs=pairs))
old=json.loads((R/'actual_G7_positive_clock_contact_window_2026-10-24/positive_clock_window.json').read_text())
assert {(z['source'],z['actor']):z['allowed_L']for z in rows if z['actor']in'DCVU'}=={(z['source'],z['ordinary_contact_actor']):z['allowed_effective_L']for z in old['all28_source_ordinary_actor_windows']}
flat=[p for z in rows for p in z['K_f_pairs']]
assert max(p['foreign_Fprefix_pieces_touched']for p in flat)==3 and max(p['foreign_WORDS_touched']for p in flat)==4 and max(p['max_ordinary_monotone_epochs']for p in flat)==7
assert max(p['strictly_intervening_complete_foreigns_f']for z in rows if z['actor']not in'DCVU'for p in z['K_f_pairs'])==2
review=[
'Literal corrected-center rays independently infer all nonreversing adjacent principal turns and both genuine F56 internal kinks. Their local identities telescope at arbitrary length. Signed actual U-entry grammar sets C-toFOREIGN wrap count to zero. Formal F-toF-prefix reversals fail literal FF, including macro FQ/FB; QF/BF remain allowed.',
'The retained open subarc starts on the actual source piece and stops on the actual new actor piece. A source F-prefix contributes its own +4 quarter-turn clock units, while a source tail omits its already traversed prefix. A new F-prefix is terminal and contributes no own clock; a new Q/B tail retains its just-traversed F56 +4 quarter units. This gives exactly the displayed two-indicator formula. All196 independent physical-tangent controls check these partial endpoint conventions; they are not claimed actual legal wholewords.',
'K includes a source C and excludes target C, while f excludes both source and actor foreign words. The two pieces of one Q/B path are internally injective and meet only at their legitimate adjacent singleton join, so distinct foreign source and actor owners belong to distinct words.',
'GLOBAL-first stopping supplies a simple earlier proxy without mixed-language induction. Assign old vertices to outgoing pieces, but a new F-prefix END contact to that earliest prefix, not a zero-parameter new tail. The resulting positive-parameter tail actor had no earlier prefix contact. The intervening subarc and partial actor form a Jordan loop; opposite closing tangents would overlap earlier, while same-direction collinear onset and endpoints remain. Thus the closing angle is strictly between -pi and pi.',
'Every symbolic source/actor internal turn is greater than -pi/2 at nonnegative K,f. Negative Jordan orientation is impossible, hence the strict window pi<T<3pi. Exact coefficient intervals for beta/(pi/4) in(0,1) give all49 rows, with L>=8 uniformly above the upper window. This is not a finite-depth word search.',
'All28 ordinary-actor rows equal the signed prior windows exactly. The21 foreign-actor rows have f<=2. Prefix PIECES touched are at most3, whereas source-tail ownership permits4 FOREIGN WORDS. K+f+1<=7 bounds ordinary heading epochs only; their lengths, fields and dormant identities remain unbounded.',
'No contact is excluded by this angular necessity; no source age, SAME-current survival through FOREIGN, arbitrary-tail simplicity, global language coverage or capture is inferred. The actual final marker premise is retained and no terminal fine kink becomes a producer/core.'
]
out=dict(status='PASS necessary all-actor GLOBAL-first-contact clock window in actual U-entry G7',manifest=sha(D/'manifest.json'),dependencies=m['dependencies'],all_local_principal_joins=local,all49_windows=rows,partial_tangent_controls196=controls,analytic_review=review,scope=m['scope'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(sha(S.with_suffix('.json')))
