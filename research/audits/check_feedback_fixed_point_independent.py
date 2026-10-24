from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'OPPOSITE_FEEDBACK_FIXED_POINT_MANIFEST.json';assert sha(MF)=='72a19c30ae323f04b3cabd39033fb96a80071d268b0a5d642ac8f943867c4497'
for f,h in json.loads(MF.read_text())['files'].items():assert sha(D/f)==h
ref=json.loads((D/'OPPOSITE_FEEDBACK_FIXED_POINT_CHECKED.json').read_text())
for f,h in ref['source_hashes'].items():assert sha(D/f)==h
lib=S.with_name('check_phase13_double_scatter_independent.py');ns={'__file__':str(lib)};exec(lib.read_text().split('# Canonical source')[0],ns);sim,geometry,future,phases,xy=[ns[k]for k in('sim','geometry','future','phases','xy')]
seed={complex(*p)for p in ref['initial_black']};N=ref['actual_physical_reads'];s,t=ref['contact_start'],ref['contact_end'];cuts=[z['cut']for z in ref['actual_full_snapshots']];z=sim(seed,N,expected=ref['actual_full_word'],cuts=cuts);z['snap'][N]=(dict(z['B']),z['p'],z['h']);tail,dr,fdead,tests=future(z['B'],z['p'],z['h']);assert tail==ref['actual_infinite_tail_word']and tail in phases and xy(dr)==ref['actual_tail_drift'];z['dead'].update({i:N+u for i,u in fdead.items()})
for rr in ref['actual_full_snapshots']:
 B,p,h=z['snap'][rr['cut']];assert[xy(p),h]==rr['pose'];full=[dict(cell=xy(q),lifetime=i,death=z['dead'].get(i))for q,i in sorted(B.items(),key=lambda a:(a[0].real,a[0].imag))];assert full==rr['full_black'];assert sorted(xy(q)for q,i in B.items()if i in z['dead'])==rr['whole_actual_relevant']
W=z['word'][s:t];P=len(W);Q,HH,d,hh=geometry(0j,0,W);assert W==ref['loop_word']and P==5812 and(d,hh)==(-68+72j,0)
B0,p0,h0=z['snap'][s];B1,p1,h1=z['snap'][t];assert(p0,h0,p1,h1)==(112+105j,0,44+177j,0)
C0={q for q,i in B0.items()if i in z['dead']};C1={q for q,i in B1.items()if i in z['dead']};old={q for q in C1 if B1[q]<s};new=C1-old;translated={q+d for q in C0};rcomp=ref['actual_relevant_comparison'];assert(len(C0),len(C1),len(old),len(new))==(234,144,90,54)
for name,ss in [('old_survivors',old),('new_relevant',new),('missing_translated_entry',translated-C1),('extra_current_relevant',C1-translated)]:assert sorted(map(xy,ss))==rcomp[name]
assert sum(s<=z['dead'].get(i,10**20)<t for i in B0.values())==144
first={};toggle=set();orbits=defaultdict(list)
def cl(q):
 x,y=int(q.real),int(q.imag);r=x%68;k=(x-r)//-68;return complex(r,y-72*k),k
for i,q in enumerate(Q):
 first.setdefault(q,(i,W[i]));toggle.symmetric_difference_update({q});r,k=cl(q);orbits[r].append((k,i,W[i]))
assert len(first)==1210 and len(toggle)==654 and len(orbits)==1160
bad=[]
for q,(i,c)in sorted(first.items(),key=lambda z:z[1][0]):
 actual='L'if p1+q in B1 else'R'
 if c!=actual:bad.append(dict(offset=i,cell=xy(p1+q),required=c,current=actual,current_lifetime=B1.get(p1+q)))
assert bad==ref['desired_next_full_field_port_disagreements']and Counter(r['required']for r in bad)==dict(L=61,R=66)
assert next(i for i,(a,b)in enumerate(zip(W,z['word'][t:]))if a!=b)==2
v=43+178j;vis=[[i,z['word'][i],z['events'][i]]for i,q in enumerate(z['pts'])if q==v];assert vis==ref['actual_fixed_preparation_port']['visits']and vis[:6]==[[18835,'R',None],[18843,'L',18835],[18847,'R',None],[18955,'L',18847],[18963,'R',None],[18971,'L',18963]];assert vis[6][0]==55543
# Solve every finite renewal equation by spatial suffix parity, independently.
S0=set();equations=[];leading=[];intrinsic=[];lo={}
for r,rs in sorted(orbits.items(),key=lambda a:(a[0].real,a[0].imag)):
 parity=Counter(k for k,i,c in rs);l=min(parity);hi=max(parity);lo[r]=l;bit=0
 for k in range(hi,l-1,-1):
  assert bit==sum(v for j,v in parity.items()if j>k)%2
  if bit:S0.add(r+k*d)
  equations.append(dict(rep=xy(r),index=k,visit_parity=parity[k]%2,entry_bit=bit));bit^=parity[k]%2
 ordered=sorted(rs,key=lambda a:a[1]-P*a[0])
 if ordered[0][2]=='L':leading.append(dict(rep=xy(r),phase=ordered[0][1],index=ordered[0][0]))
 for a,b in zip(ordered,ordered[1:]):
  if a[2]==b[2]:intrinsic.append(dict(rep=xy(r),earlier=list(a),later=list(b)))
assert equations==ref['finite_renewal_equations']and leading==ref['stable_first_L_orbits']and intrinsic==ref['bulk_alternation_conflicts'];assert(len(S0),len(leading),len(intrinsic))==(35,115,30)
def exposed(q,shift):r,k=cl(q);return r in lo and k>=lo[r]+shift
after=S0^toggle;nextS={q+d for q in S0};assert{q for q in after if exposed(q,1)}==nextS and all(exposed(q,0)for q in S0);discard=after-nextS
assert sorted(map(xy,S0))==ref['unique_candidate_relevant']and sorted(map(xy,discard))==ref['candidate_permanent_output']and len(discard)==620;assert 0j not in S0 and W[0]=='L'
assert orbits[0j]==[(0,0,'L')];assert B0[p0]==5605 and B0[p1]==B1[p1]==18845 and p0+2*d not in B0 and p0+2*d not in B1
# W^2 is geometry only. Its first intrinsic same-cell alternation failure.
QQ,_,_,_=geometry(0j,0,W*2);last={};failure=None
for i,q in enumerate(QQ):
 c=(W*2)[i]
 if q in last and last[q][1]==c:failure=dict(cell=xy(q),earlier_tick=last[q][0],later_tick=i,earlier_turn=c,later_turn=c);break
 last[q]=(i,c)
assert failure==ref['earliest_two_copy_conflict']and failure==dict(cell=[-69,68],earlier_tick=5733,later_tick=6745,earlier_turn='R',later_turn='R');assert all(q!=-69+68j for q in QQ[5734:6745]);assert(z['pts'][s+5733],z['word'][s+5733])==(43+173j,'R')
out=dict(status='PASS exact5812 feedback-word fixed-point obstruction, not arbitrary feedback',manifest=sha(MF),full_actual_reads=N,actual_tail_tests=tests,actual_entire_relevance=[234,144],old_new_survivors=[90,54],counterfactual_footprint=dict(cells=1210,full_drift_classes=1160,odd_toggles=654,unique_finite_candidate=35,discarded_parity_output=620),first_intrinsic_two_copy_failure=failure,actual_second_word_first_failure=2,full_board_port_disagreements=dict(BLACK_missing=61,BLACK_interference=66),analytic_review=[
'The actual entire contact-to-contact word restores N with drift(-68,72), so no freely inserted quarter-rotation is part of this fixed recurrence. All57885 physical reads, every meaningful full identity board, lifetime fate and exact infinite canonical tail reconstruct.',
'The full counterfactual W^2 geometry has consecutive R5733/R6745 at the same physical(-69,68) and no intermediate visit. It is the first intrinsic alternation failure and rules out TWO copies on any initial board, even infinite support. The later prescribed read is not asserted to occur in the actual orbit.',
'For each full Zd orbit, ell is the minimum SPATIAL layer. The prescribed future footprint is k>=ell, shifted future k>=ell+1. Therefore finite recurring pruning must satisfy s(k-1)=s(k) XOR t(k) only for k>=ell+1, with zero large-k boundary. The unique suffix-XOR solution is necessary only; layerell may leave exposure. Unread archive outside the entire footprint cannot alter it.',
'All1160 orbit equations produce35 BLACK cells and620 discarded parity outputs, but head is WHITE against the first required L. These are counterfactual algebraic sets, never the actual234/144 pruning or an attained ant board.',
'The marker orbit has only phase0L: the second actual marker is old R18845, not output of the5812 loop. The third marker is absent from both entire actual boards. The115 stable first-L diagnostic is old-at-entry fuel only and subordinate to the stronger intrinsic contradiction.',
'The actual first repetition failure at offset2 is fixed WHITE by the earlier18971L with no intervening visit. Its127 whole-board port discrepancies use ALL black archive, not a C* crop. Preserving the entire preparation cannot fix that read through unread seed edits.',
'Only this exact word/pose recurrence is excluded. Other connecting words, longer feedback cycles, new preparations and universal attraction remain open.'
],source_hashes=ref['source_hashes'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
