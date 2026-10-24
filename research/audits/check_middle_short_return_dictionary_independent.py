from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'MIDDLE_SHORT_RETURN_INTERFACE_AND_STANDARD_DICTIONARY_OBSTRUCTION.md';JF=D/'middle_short_return_dictionary_certificate.json';assert sha(P)=='b0dc91d29d6c480ea67a954a01e16eeaeccd06780dd07cae319f04e038a5a6fb'and sha(JF)=='965f35fd0693c881d28a146e2aa1ce4404d1d2cec7035d77b7a71740ab9b4de6'and sha(D/'certify_middle_short_return_dictionary.py')=='606c3428234dcfbbccdea5357974e58d0cac3a3c9339e4b00d4a9b9133854206';J=json.loads(JF.read_text())
for f,h in J['dependencies'].items():assert sha(D/f)==h
Q=json.loads((S.parent/'check_middle_short_coincident_C_independent.json').read_text());assert sha(S.parent/'check_middle_short_C_core_ports_independent.json')=='56b2df29e1b9e2134fcfaf39b0edd1b3851c2b35354c29e593e27ba2d7029397'
N={};exec((S.parent/'check_drift31_refined_top_gap_independent.py').read_text().split("for line in(P/'DRIFT31_REFINED_TOP_ODD_GAP_SHA256SUMS')")[0],N);graph=N['graph'];V=[1j,1,-1j,-1];off=[-1j,-1-1j,-1,0j];lev=lambda p:int(3*p.imag-p.real);xy=lambda p:[int(p.real),int(p.imag)];ROOT=-8+0j;Kword='LRLRRRRLRRRRLLLLRL'
def literal(w,h=0,p=ROOT):
 events=[];last={};first={};bad=None
 for t,c in enumerate(w):
  hi=h;h=(h+(1 if c=='R'else-1))%4;e=dict(t=t,p=xy(p),hi=hi,ho=h,c=c);events.append(e);first.setdefault(p,(c,t))
  if bad is None and p in last and last[p]['c']==c:bad=(last[p],e)
  last[p]=e;p+=V[h]
 if bad:
  a,b=bad;return dict(legal=False,word=w,earlier=a,later=b,intervening_positions=[z['p']for z in events[a['t']+1:b['t']]],start_position=xy(ROOT),start_heading=0)
 seed={q for q,(c,t)in first.items()if c=='L'};B=set(seed)
 for e in events:q=complex(*e['p']);assert(q in B)==(e['c']=='L');B.symmetric_difference_update({q})
 return dict(legal=True,word=w,start_position=xy(ROOT),start_heading=0,full_minimal_initial_black=sorted(map(xy,seed)),full_final_black=sorted(map(xy,B)),final_position=xy(p),final_heading=h,events=events)
# Literal physical D/O/K and G/F initial channels for every complete core.
interfaces=[]
for ii,hs in enumerate(Q['six_survivors']):
 H={int(t):['NESW'.index(c)for c in w]for t,w in hs.items()};su,ev,*_=graph(H);core={(t,r)for t,r in ev if lev(-t+off[H[t][r]])in[1,3,5]};assert len(core)==24;thirdN=3 if H[8][3]==0 else 5;mode='A'if thirdN==3 else'B';ar=J['six_exact_lower_return_interfaces'][ii]
 def trace(st,steps):
  e=st;k=0;z=[]
  for j in range(steps+1):
   t,r=e;p=-t+k*(3+1j);z.append(dict(node=list(e),lift=k,position=xy(p),heading=H[t][r],turn='R'if r%2==0 else'L'))
   if j<steps:e,dk=su[e];k+=dk
  return z
 d=trace((8,0),4);o=trace((8,thirdN-1),4);k=trace((8,7),18);assert o==ar['opposite_return_five_events'];assert[(e['node'],e['lift'])for e in o]==[([8,thirdN-1],0),([9,1 if mode=='A'else 3],0),([6,3],-1),([5,3],-1),([8,thirdN],0)]
 assert ''.join(e['turn']for e in d[:-1])=='RRRR'and d[-1]['node']==[8,1]and d[-1]['lift']==0;assert ''.join(e['turn']for e in o[:-1])=='RLLL';assert ''.join(e['turn']for e in k[:-1])==Kword and k[-1]['node']==[8,0]and k[-1]['lift']==1
 fstarts=[1,thirdN];same=[r for r in[2,4,6]if H[8][r:r+2]==[2,2]];assert len(same)==2;gstart=same[0]+1;fs=[trace((8,r),1)for r in fstarts];g=trace((8,gstart),2);assert all(''.join(e['turn']for e in z[:2])=='LR'for z in fs)and ''.join(e['turn']for e in g[:3])=='LLL'and g[1]['node']==[7,1]
 # These disjoint pieces exhaust all 24 complete core event classes. The
 # same-cell T8 rank order places each piece inside one actual full P interval.
 pieces=[d[:-1],o[:-1],k[:-1],[z[0]for z in fs],g[:3]];hit=[];parts=[]
 for z in pieces:
  hh=[tuple(e['node'])for e in z if tuple(e['node'])in core];hit+=hh;parts.append(hh)
 assert len(hit)==24 and set(hit)==core and len(set(hit))==24
 assert [len(x)for x in parts]==[4,1,16,2,1]
 assert all(lev(complex(*e['position'])+off[e['heading']])>=7 for z in fs for e in z[1:]);assert all(lev(complex(*e['position'])+off[e['heading']])>=7 for j,e in enumerate(g[:3])if j!=1)
 interfaces.append(dict(mode=mode,D=d,O=o,K=k,F_initial=fs,G_initial=g,all24_core_assignment=[list(e)for e in hit],same_heading_pairs=[[r,r+1]for r in same]))
# Independently obtain every complete standard full-drift read history.
lib=S.parent/'check_active_C_entry_exit_independent.py';ns={'__file__':str(lib)};src=lib.read_text().split('base={};summary={}')[0].replace(' return sig',' return dict(E=E,d=d,H=H,F=F,ev=ev)');exec(src,ns);az=json.loads((D/'active_C_entry_exit_forests_certificate.json').read_text())['base_controls']['S104'];z=ns['analyze'](az['word'],author=az);w=az['word'];P0=len(w);pal={x:{}for x in'EFG'}
for cl,rs in sorted(z['H'].items(),key=lambda a:(a[0].real,a[0].imag)):
 for (a,e),(b,f)in zip(rs,rs[1:]):
  typ=None
  if e['c']=='R'and e['hi']==f['hi']:typ='E';hh=2
  elif e['c']=='L'and(f['hi']-e['hi'])%4==2:typ='F';hh=0
  elif e['c']=='L'and e['hi']==f['hi']:typ='G';hh=2
  if typ is None:continue
  ww=''.join(w[t%P0]for t in range(a,b));q=ROOT;h=hh;levels=[];poss=[]
  for c in ww:poss.append(q);levels.append(lev(q+off[h]));h=(h+(1 if c=='R'else-1))%4;q+=V[h]
  assert q==ROOT and ROOT not in poss[1:]
  good=min(levels)>=7 if typ=='E'else(levels[0]==5 and min(levels[1:])>=7 and ww[:2]=='LR')if typ=='F'else(ww[:3]=='LLL'and levels[1]==5 and min(levels[:1]+levels[2:])>=7)
  if good:pal[typ].setdefault(ww,dict(word=ww,standard_start_phase=a%P0,standard_length=b-a,standard_read_class=xy(cl),normalized_heading=hh,normalized_C_levels=levels))
ps={t:sorted(pal[t],key=lambda w:(len(w),w))for t in'EFG'};assert {t:len(x)for t,x in ps.items()}=={'E':5,'F':7,'G':3}
for typ in'EFG':
 assert ps[typ]==[a['word']for a in J['standard_return_dictionaries'][typ]]
 for ar in J['standard_return_dictionaries'][typ]:
  rr=pal[typ][ar['word']];assert all(ar[k]==v for k,v in rr.items())
# Prefix-tree cover, with no restrictions at all after its finite bad leaves.
leaves=[];stages=[];positive=None
for mode in'AB':
 seq=[('D',['RRRR']),('F1',ps['F'])]+([('O',['RLLL']),('F2',ps['F']),('E1',ps['E'])]if mode=='A'else[('E1',ps['E'])]);live=[('',[])]
 for name,choices in seq:
  nxt=[]
  for pre,labs in live:
   for j,ww in enumerate(choices):
    v=literal(pre+ww);lab=labs+[[name,j]]
    if v['legal']:
     nxt.append((pre+ww,lab))
     if mode=='A'and name=='F2':assert positive is None;positive=v
    else:leaves.append(dict(mode=mode,last_block=name,block_choices=lab,literal_consecutive_same_turn_witness=v))
  stages.append(dict(mode=mode,block=name,attempts=len(live)*len(choices),surviving_prefixes=len(nxt)));live=nxt
 assert not live
assert leaves==J['arbitrary_suffix_prefix_cover']['all64_terminal_witnesses']and stages==J['arbitrary_suffix_prefix_cover']['complete_prefix_tree_stages'];assert len(leaves)==64 and positive==J['arbitrary_suffix_prefix_cover']['unique_32_read_prepared_survivor_before_E1'];assert(len(positive['word']),len(positive['full_minimal_initial_black']),len(positive['full_final_black']),positive['final_heading'])==(32,3,9,2)
# Materialize all fifteen positive factors from one complete blank orbit,
# retaining every original board cell and every actual L owner.
lib=S.parent/'check_phase13_double_scatter_independent.py';n={'__file__':str(lib)};exec(lib.read_text().split('# Canonical source')[0],n);sim,future=n['sim'],n['future'];cuts={9977}
for ls in J['standard_return_dictionaries'].values():
 for a in ls:cuts|={a['blank_start'],a['blank_end']}
end=max(cuts);actual=sim(set(),end,h=0,cuts=cuts);actual['snap'][end]=(dict(actual['B']),actual['p'],actual['h']);actual['pts'].append(actual['p']);cap=actual['snap'][9977];fw,dr,dead,nt=future(*cap);assert fw==w;assert J['full_standard_capture']==dict(time=9977,full_black_field=sorted(map(xy,cap[0])),head=xy(cap[1]),heading=cap[2])
positive_rows=[]
for typ,ls in J['standard_return_dictionaries'].items():
 for ar in ls:
  a,b=ar['blank_start'],ar['blank_end'];assert a==9977+3*104+ar['standard_start_phase']and b-a==len(ar['word'])and actual['word'][a:b]==ar['word'];assert actual['pts'][a]==actual['pts'][b]and actual['pts'][a]not in actual['pts'][a+1:b]
  for tick,label in[(a,'source_full_initial_state'),(b,'source_full_final_state')]:
   bb,p,h=actual['snap'][tick];assert ar[label]==dict(time=tick,full_black_field=sorted(map(xy,bb)),head=xy(p),heading=h)
  events=[]
  for t in range(a,b):
   e=dict(time=t,position=xy(actual['pts'][t]),heading=actual['heads'][t],turn=actual['word'][t])
   if actual['word'][t]=='L':birth=actual['events'][t];assert birth>=0 and actual['pts'][birth]==actual['pts'][t]and actual['word'][birth]=='R';e['actual_R_owner']=birth
   events.append(e)
  assert events==ar['source_events_and_actual_owners'];positive_rows.append(dict(type=typ,word=ar['word'],interval=[a,b],full_initial_size=len(actual['snap'][a][0]),full_final_size=len(actual['snap'][b][0]),actual_owners=[e.get('actual_R_owner')for e in events]))
O=dict(status='PASS five arbitrary-return semantics and conditional standard-return dictionary prefix obstruction ONLY',proof=sha(P),certificate=sha(JF),script=sha(S),signed_core_report=sha(S.parent/'check_middle_short_C_core_ports_independent.json'),dependencies=J['dependencies'],six_physical_return_interfaces=interfaces,full_standard_return_dictionaries=ps,all64_bad_prefix_witnesses=leaves,prefix_stages=stages,prepared32_full_factor=positive,all15_positive_standard_factors=positive_rows,blank_full_reads=end,full_capture_parity_tests=nt,analytic_review=[
'The exact physical T8 history has eight reads within a span P-18<P. Consecutive same-cell ranks, not quotient adjacency alone, define the five free words. Actual successor reconstruction in all six interfaces gives D=RRRR, O=RLLL and the18-read K ending at z+d,N, with full lifts retained. In particular the O return uses T6.L3 and T5.L3 on lift-1, while both T8 endpoints are on lift0.',
'The fixed D/O/K pieces contribute4/1/16 complete core event classes; the first events of F1/F2 contribute2, and the second event of G is the remaining Z class. These24 roles are distinct and exhaust every complete C1/C3/C5 event class within the same full-P interval. Since T=3y-x is invariant under d, no other physical translate of any core face can occur inside either E excursion or the omitted parts of F/G. This is exact complete-history exhaustion, not an unread-mask inference.',
'Each E is an arbitrary first return S/R to same-position S/L, with endpoints excluding the latter read, hence closed head pose and length divisible4. F goes N/L to S/R and beginsLR; only its first event is onC5. G goes S/L to S/R, beginsLLL and contains only the one-event Z core channel. All other active-face classes are>=7 by the complete lower support/core inventory. No bound on length, exterior stock, mass change or physical read multiplicity follows.',
'Independent complete full-drift standard histories give exactly5 E,7 F,3 G words under those physical endpoint and active-face exclusions. All15 are materialized from a single literal blank-origin certified standard future, with complete source/end boards and every actual earlier R owner. Rotation to a normalized root does not erase their prepared inputs or establish compatible joins.',
'The exact prefix tree has64 first same-cell/same-turn failures: A gives4 atO,20 atF2,5 atE1; B gives35 atE1. Every pair is consecutive at that physical cell and every intervening position is retained. Thus suffixes after those bad prefixes may be arbitrary. The sole32-read A prefix is genuinely legal from its full3-cell input and ends with9 cells, but none of the5 specified E words can follow.',
'Only modeA F1/F2/E1 and modeB F1/E1 are restricted to the finite dictionary. Neither whole core order, arbitrary E/F/G returns, the four open lifetime-boundary types, a finite macro alphabet, WHITE winding or universal capture is excluded. The7350 full product size is bookkeeping, not a bounded period premise.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
