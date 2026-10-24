from pathlib import Path
from collections import Counter,defaultdict
from functools import lru_cache
from itertools import product
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'second_foreign_short_clock_transfer_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='edb2b9cb824041498035756583408e31b773a2142797cf8ce901b667a3a85087';mf=json.loads(MF.read_text())
for k,b in [('files',D),('dependencies',R)]:
 for f,h in mf[k].items():assert sha(b/f)==h
J=json.loads((D/'second_foreign_transfer.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy,center,meet,pieces=[ns[k]for k in('W','M','K','tr','rot','xy','center','meet','pieces')]
raw={a:tr(W[a])for a in'DCVUFQB'};ctx={a:tr(W[a]+M)for a in'FQB'};first=lambda z,q:next((c,t)for t,(p,h,c)in enumerate(z['reads'])if p==q);spell=lambda word:''.join(W[a]for a in word)
STAR={0j,1j,1+0j,1+1j};HK={'F':{-3-1j,-2-1j},'Q':{-3-3j,-2-3j,-1-3j,-1-2j},'B':{-2-4j,-1-4j,-4j,-3j}};ids={};start={}
for A in'FQB':
 p=4j+raw[A]['p'];h=raw[A]['h'];assert(p,h)==({'F':-4+2j,'Q':-4+0j,'B':-3-1j}[A],2);start[A]=(p,h);idc={q:raw['U']['last'][q][1]for q in STAR}
 for tag in HK[A]:
  cell=p+rot(h)*tag;local=cell-4j;ch,t=raw[A]['last'][local];assert ch=='R'and(local-raw[A]['p'])/rot(h)not in K;idc[cell]=28+t
 assert len(idc)==len(STAR)+len(HK[A]);ids[A]=idc
 for name,r in J['selected_id_definitions'][A].items():q=complex(*r['cell']);assert idc[q]==r['birth_tick0']and r['own_R_tick0']==idc[q]-(28 if name.startswith('first_foreign')else 0)
# Complete external-to-CORE loss coverage, including untouched RAW cells.
for r in J['all15_foreign_EXIT_CORE_capture_checks']:
 a=r['foreign'];q=complex(*r['actual_EXIT_CORE_cell']);assert(q-raw[a]['p'])/rot(raw[a]['h'])in K and r['in_ENTRY_CORE']==(q in K)
 assert r['actual_RAW_last_read']==(list(raw[a]['last'][q])if q in raw[a]['last']else None)
 assert r['actual_complete_first_requirement']==(list(first(ctx[a],q))if q in ctx[a]['req']else None)
 if q not in K and q not in raw[a]['last']:assert ctx[a]['req'][q]is True
assert len(J['all15_foreign_EXIT_CORE_capture_checks'])==15
@lru_cache(None)
def perm(t):
 if sum(t)==0:return ('',)
 ans=[]
 for i,a in enumerate('DVU'):
  if t[i]:z=list(t);z[i]-=1;ans +=[a+s for s in perm(tuple(z))]
 return tuple(ans)
def comps(weights,n):
 if not weights:
  if n==0:yield ()
  return
 for i in range(n//weights[0]+1):
  for z in comps(weights[1:],n-i*weights[0]):yield(i,)+z
allwords={0:{},1:{}};alltuples=set();goals={};counts={}
for c in(0,1):
 for A in'FQB':
  p1,h1=start[A];h=(h1-c)%4;gg=defaultdict(list)
  for A2 in'FQB':
   for q in ids[A]:
    for slot,b in ctx[A2]['req'].items():
     if not b:continue
     p=q-rot(h)*slot
     if int(p.real+p.imag+h)%2==0:gg[(A2,p)].append((q,slot))
  ref=next(r for r in J['all_necessary_second_FOREIGN_FIRST_L_goals']if r['C_count']==c and r['first_foreign']==A);assert len(gg)==ref['goal_count']==len(ref['all_exact_goals']);seen=set()
  for r in ref['all_exact_goals']:
   A2=r['second_foreign'];p=complex(*r['entry'][:2]);assert r['entry'][2]==h;seen.add((A2,p));assert set(gg[A2,p])=={(complex(*q['physical_cell']),complex(*q['second_foreign_first_L_local']))for q in r['witnesses']}
   for q in r['witnesses']:
    slot=complex(*q['second_foreign_first_L_local']);f=first(ctx[A2],slot);assert q['is_ENTRY_CORE']==(slot in K)and q['actual_first_L_owner']['context_tick0']==f[1]and f[0]=='L'
  assert seen==set(gg);nword=0
  for(A2,p)in gg:
   if c==0:
    dx,dy=int(p1.real-p.real),int(p1.imag-p.imag)
    if min(dx,dy)<0:continue
    for s in comps((1,3,4),dy):
     if s[0]+s[1]!=dx:continue
     alltuples.add((c,A,A2,*xy(p),h,*s));
     for pre in perm(s):allwords[c]['U'+A+pre+A2]=(A,A2,p,h,pre,'');nword+=1
   else:
    budget=int(p1.imag-1-p.imag)
    if budget<0:continue
    for ds,vs,us,de,ve in comps((1,3,4,1,1),budget):
     v=int(p.real-p1.real)+ds+vs-de-3*ve
     if v<0 or v%4:continue
     ue=v//4;s=(ds,vs,us);e=(de,ve,ue);alltuples.add((c,A,A2,*xy(p),h,*s,*e))
     for pre,post in product(perm(s),perm(e)):allwords[c]['U'+A+pre+'C'+post+A2]=(A,A2,p,h,pre,post);nword+=1
  counts[c,A]=(len(gg),nword)
assert[ counts[c,A]for c in(0,1)for A in'FQB']==[(97,11),(112,8),(112,6),(102,948),(117,240),(117,90)]
assert alltuples=={(r['C_count'],r['first_foreign'],r['second_foreign'],*r['second_entry'],*r['S_counts'],*r.get('E_counts',[]))for r in J['all_exact_nonnegative_count_tuples']}
def owner(word,t):
 for i,a in enumerate(word):
  if t<len(W[a]):return dict(atom_index0=i,atom=a,own_tick0=t,own_read_number1=t+1,turn=W[a][t])
  t-=len(W[a])
 return dict(owner='actual following word supplied by M11',next_word_tick0=t,next_word_read_number1=t+1,turn=M[t])
for c,field in[(0,'all25_zero_C_immutable_words'),(1,'all1278_one_C_immutable_words')]:
 refs={r['word']:r for r in J[field]};assert len(refs)==len(J[field])==len(allwords[c])and set(refs)==set(allwords[c])
 for word,(A,A2,p,h,pre,post)in allwords[c].items():
  r=refs[word];z=tr(spell(word[:-1]));assert(z['p'],z['h'])==(p,h);z=tr(spell(word)+M);assert z['bad'];later,earlier,cell,ch=z['bad'];assert r['previous_owner']==owner(word,earlier)and r['conflicting_owner']==owner(word,later);assert r['immutable_conflict']['previous_read']==earlier and r['immutable_conflict']['conflict_read']==later
  assert r['endpoint_data']['S_rail']==pre and r['endpoint_data']['E_rail']==post
# Independent full prepared boards and SAME physical identities at every true cut.
positives=[];minrefs={r['word']:r for r in J['all15_prescribed_minimal_nonempty_zero_C_controls']}
for A in'FQB':
 for b,targets in [('V','FQ'),('U','FQB')]:
  for A2 in targets:
   word='U'+A+b+A2;z=tr(spell(word)+M);assert(not bool(z['bad']))==minrefs[word]['feasible']
   if z['bad']:continue
   r=next(r for r in J['all3_genuine_complete_two_FOREIGN_positive_controls']if r['word']==word);seed={q for q,b in z['req'].items()if b};assert sorted(map(xy,seed))==r['complete_seed']and len(seed)==r['seed_mass'];B={q:None for q in seed};p=0j;h=0;t=0;cuts=[];segments=[];idreads=defaultdict(list)
   named={name:complex(*q['cell'])for name,q in J['selected_id_definitions'][A].items()}
   for i,a in enumerate(word):
    for x,y in pieces(a):segments.append((2*p+rot(h)*x,2*p+rot(h)*y))
    for k,ch in enumerate(W[a]):
     assert(p in B)==(ch=='L')
     for name,q in named.items():
      if p==q:idreads[name].append(dict(global_tick0=t,atom_index0=i,atom=a,own_tick0=k,turn=ch,SAME_original_before_read=B.get(p)==ids[A][p]))
     if ch=='L':del B[p];h=(h-1)%4
     else:B[p]=t;h=(h+1)%4
     p+=rot(h)*1j;t+=1
    if i>=1:
     ck={p+rot(h)*q for q in K};rr=next(q for q in r['RAW_cuts']if q['after_atom_index0']==i);assert rr['RAW_cut_tick0']==t and rr['actual_head']==xy(p)+[h]
     for q,born in ids[A].items():assert B.get(q)==born and q not in ck
     for q in rr['selected_ID_state']:assert q['CURRENT']and q['same_physically_BLACK']and not q['alive_CORE']and ids[A][complex(*q['cell'])]==q['birth_tick0']
   for k,ch in enumerate(M):
    assert(p in B)==(ch=='L')
    for name,q in named.items():
     if p==q:idreads[name].append(dict(global_tick0=t,owner='actual following word via M11',next_tick0=k,next_read_number1=k+1,turn=ch,SAME_original_before_read=B.get(p)==ids[A][p]))
    if ch=='L':del B[p];h=(h-1)%4
    else:B[p]=t;h=(h+1)%4
    p+=rot(h)*1j;t+=1
   assert t==r['all_physical_reads']and all(B.get(q)==born for q,born in ids[A].items())and dict(idreads)==r['all_selected_identity_reads']
   for j,bseg in enumerate(segments):
    assert r['actual_repaired_proxy_pieces'][j]['start']==xy(bseg[0])and r['actual_repaired_proxy_pieces'][j]['end']==xy(bseg[1])
    for i,aseg in enumerate(segments[:j]):
     m=meet(*aseg,*bseg)
     if j==i+1:assert aseg[1]==bseg[0]and m==(1,0)
     else:assert m is None
   positives.append((word,len(seed),t))
assert positives==[('UQUF',44,187),('UBVF',44,187),('UBUF',47,197)]
out=dict(status='PASS exact second-foreign C0/C1 selected-identity non-loss and three full positive controls',manifest=sha(MF),script=sha(S),goal_and_word_counts={f'C{c}_{A}':list(v)for(c,A),v in counts.items()},count_tuples=len(alltuples),immutable_words=[len(allwords[c])for c in(0,1)],positive_controls=positives,analytic_review=['Actual plainU immediately before firstF/Q/B fixes the S-facing start. Every selected actual originalR cell is aligned to EVERY secondforeign+actualM11 firstL slot, including entryCORE and marker-only inputs. This deliberately overapproximates survival-to-entry, so no assumed old currentness is used to eliminate a candidate.','ZeroC monotone S drift yields exact nonnegative x/y budgets. OneC has S rail,C step0,-1, thenE rail; the vertical budget bounds allfive independent counts and the horizontal equation fixes U_E. An independent weighted-composition generator reconstructs every tuple and every ordering, including empty rails and C immediately beside a foreign. All25+1278 complete words have literal same-cell contradictions with actual owners. No depth or rail cap is imposed.','Any SAME BLACK identity physically consumed in the secondRAW/M has a firstL there. All15 actual foreign exitCORE roles show that a previously external original silently absorbed atRAWexit would be readL by the real nextM11. Thus selected SAME identities cannot suffer that completed second-interval loss at clocks0/1. An original already dead/reborn earlier is not protected as SAME; physically aliveCORE is never confused with physical death.','The three complete prepared44/44/47 boards realize genuineU births and both foreigners. All selected original identities are CURRENT at each markedRAWcut and physically BLACK after suppliedM; that final finecut is not declared a markedCOREcut. The directly reconstructed repaired finite proxies are simple, with realF56 split and no auxiliaryM chord. These are finite positive controls, not a twoforeign simplicity induction.','Scope remains exact plainU, immediatefirstforeign, zero/one ordinaryC, secondforeign withactualM. AtleasttwoCs is a necessary loss obligation only; oppositeS/N rails atC2 remain unbounded. No arbitrary initialUC/UCC, earlierforeignprefix, generalhookseal, foreign-countfuel or capture.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
