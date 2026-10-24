from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib,math
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((D/'DROUGHT_BOUNDARY_PINNING_MANIFEST.json').read_text());assert sha(D/'DROUGHT_BOUNDARY_PINNING_MANIFEST.json')=='f0d24e49e0ceef9fef4e887a1941ab3c7a094470d77930d1991604c9a876d824'
for kind in('files','dependencies'):
 for f,h in m[kind].items():assert sha(D/f)==h
J=json.loads((D/'DROUGHT_BOUNDARY_PINNING_CHECKED.json').read_text())
q=R/'audits/check_phase13_double_scatter_independent.py';ns={'__file__':str(q)};exec(q.read_text().split('# Canonical source')[0],ns);K,xy,geometry,sim,cert,future,key=[ns[k]for k in('K','xy','geometry','sim','cert','future','key')];V=(1j,1,-1j,-1)
# Independent full3x3 state cover, including arbitrary endpoint initial poses.
cells=[complex(x,y)for x in range(3)for y in range(3)];corners={0j,2+0j,2j,2+2j};inside=lambda p:0<=p.real<=2 and 0<=p.imag<=2;inner=lambda p:p==1+1j
sides=[[1+2j],[2+1j],[1+0j],[1j]];summary=[];partial=0
for mask in range(512):
 seed={p for j,p in enumerate(cells)if(mask>>j)&1}
 for h0 in range(4):
  B=set(seed);p=1+1j;h=h0;pts=[p];turns=[];boards=[set(B)];head=[h]
  for _ in range(50):
   c='L'if p in B else'R';B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=V[h];turns.append(c);pts.append(p);boards.append(set(B));head.append(h)
   if not inside(p):break
  assert not inside(p);end=max(t for t,p in enumerate(pts)if inner(p));sig=((int(pts[0].real+pts[0].imag))%2)^(h0%2)
  def phi(side,board):
   ans=0
   for j,p in enumerate(sides[side]):
    vertical=((int(p.real+p.imag)%2)^sig)==0;normal=(side%2==0)==vertical
    eta=int(p in board)if normal else int(p not in board);ans+=(j+1)*eta
   return ans
  cornerseen=set();dom=[0]*4;pert=[0]*4;eps=[];t=0
  while t<end:
   if inner(pts[t]):t+=1;continue
   start=t
   while t<end and not inner(pts[t]):t+=1
   block=pts[start:t];w=''.join(turns[start:t]);co=set(block)&corners
   assert len(block)in(2,3)and w in('RR','LL','RRR','LLL')and len(co)==len(block)-2
   assert not co&cornerseen;cornerseen|=co
   for side in range(4):
    nh=sum(p in sides[side]for p in block);delta=phi(side,boards[t])-phi(side,boards[start])
    if co and nh:assert nh==1 and abs(delta)<=len(sides[side]);pert[side]+=delta
    elif nh:assert nh==2 and delta==-1;dom[side]+=1
    else:assert delta==0
   eps.append((start,t,w))
  for side in range(4):assert dom[side]==phi(side,boards[0])-phi(side,boards[end])+pert[side]
  reads=sum(b-a for a,b,w in eps);assert reads<=36
  summary.append(dict(exit=len(turns),interior_end=end,boundary_reads=reads,corner_reads=len(cornerseen),dominos=dom,bound=36))
  for start in cells:
   if inner(start):continue
   B=set(seed);p=start;h=h0
   for t in range(4):
    if not inside(p)or inner(p):break
    c=p in B;B.symmetric_difference_update({p});h=(h+(-1 if c else 1))%4;p+=V[h]
   assert not inside(p)or inner(p);assert t<=3;partial+=1
au=J['three_by_three_complete_exhaustion'];assert len(summary)==au['states']==2048 and max(z['exit']for z in summary)==au['max_exit']and max(z['boundary_reads']for z in summary)==au['max_boundary_reads']and max(z['corner_reads']for z in summary)==au['max_corner_reads']
assert hashlib.sha256(json.dumps(summary,separators=(',',':')).encode()).hexdigest()==au['results_sha256']
# Independent local straight/corner episodes in both sectors and nontrivial sides.
local_episodes=[]
for width,height in product([3,4,5,7],repeat=2):
 inside2=lambda p:0<=p.real<width and 0<=p.imag<height
 inner2=lambda p:0<p.real<width-1 and 0<p.imag<height-1
 corners2={0j,width-1+0j,(height-1)*1j,width-1+(height-1)*1j}
 sides2=[[x+(height-1)*1j for x in range(1,width-1)],[width-1+y*1j for y in range(height-2,0,-1)],[x+0j for x in range(width-2,0,-1)],[y*1j for y in range(1,height-1)]]
 for x,y,h0 in product(range(width),range(height),range(4)):
  start=complex(x,y)
  if inner2(start)or not inner2(start-V[h0]):continue
  sig=(x+y)%2^(h0%2)
  def moment(side,board):
   return sum((j+1)*(int(p in board)if ((int(p.real+p.imag)%2)^sig==0)==(side%2==0)else int(p not in board))for j,p in enumerate(sides2[side]))
  for c in'RL':
   p=start;h=h0;cells2=[]
   for n in range(3):
    assert inside2(p)and not inner2(p);cells2.append(p);h=(h+(1 if c=='R'else-1))%4;p+=V[h]
    if not inside2(p)or inner2(p):break
   if not inside2(p):continue
   assert inner2(p)and len(cells2)in(2,3)and len(set(cells2))==len(cells2)
   before=set(cells2)if c=='L'else set();after=before^set(cells2);cornerset=set(cells2)&corners2
   assert len(cornerset)==len(cells2)-2
   for side in range(4):
    hits=sum(q in sides2[side]for q in cells2);delta=moment(side,after)-moment(side,before)
    if not cornerset and hits:assert hits==2 and delta==-1
    elif cornerset and hits:assert hits==1 and abs(delta)<=len(sides2[side])
    else:assert delta==0
   local_episodes.append((width,height,x,y,h0,c,len(cells2)))
assert any(z[-1]==2 for z in local_episodes)and any(z[-1]==3 for z in local_episodes)
orientation=D/'DROUGHT_BOUNDARY_ORIENTATION_ADDENDUM.json'
assert sha(orientation)=='9a2524e996f887b54e7780e682790918f336af7ba9ff485c3f40209d8da4c728'
for fn,h in json.loads(orientation.read_text())['files'].items():assert sha(D/fn)==h

# Fresh complete original-field controls and all-n phase inequalities.
A=json.loads((D/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());M=json.loads((D/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());W=sim(K,104)['word'];assert W==M['W'];d=2+2j;qm=202+201j
pre=W*100+W[:13]+M['modes']['M']['recovery_word'];P,PH,pe,ph=geometry(0j,1,pre);assert(pe,ph)==(228+229j,0)
fw=W[41:]+W[:41];F,FH,_,_=geometry(pe,ph,fw);T,TH,te,th=geometry(0j,0,A['T_recovery']);SW,SH,_,_=geometry(te,th,A['T_tail_word']);post,postH,postend,posth=geometry(207+229j,1,A['postcollision_word']);NW=A['controls'][0]['complete_future_certificate']['tail_word'];NQ,NH,nend,nh=geometry(postend,posth,NW)
assert postend==155+215j and posth==1 and nend-postend==-2+2j
# Exact pin births, no later T-prefix read, then all future phase separation.
assert T[6452]==20+8j and T[8494]==1+33j and A['T_recovery'][6452]==A['T_recovery'][8494]=='R'
for p,t in [(20+8j,6452),(1+33j,8494)]:assert max(i for i,q in enumerate(T)if q==p)==t
assert max(p.real for p in SW)<20 and max(p.imag for p in SW)<33
assert max(p.real for p in post+NQ+[postend])<=240 and min(p.imag for p in post+NQ+[postend])>0
first=sim(K,104);assert first['B'][0j]==20 and min(p.real for p in first['B'])==min(p.imag for p in first['B'])==0
assert min(p.real for p in P[104:])>0 and min(p.imag for p in P[104:])>0
checks=Counter()
def bound(p,ax,ay,label,strict=False):
 x,y=int(p.real),int(p.imag);lo=1 if strict else 0
 for a,b in[(ax,x-lo),(2-ax,250-lo-x),(ay,y-lo),(2-ay,262-lo-y)]:assert a>=0 and 100*a+b>=0;checks[label]+=1
# Full initial board and all reads after firstperiod lie in Q_n, all n>=100.
for p in set(first['B'])|{qm+a*d for a in(0,1,6,8)}:bound(p,0,0,'initial_after104')
for a in(0,1,3,5,6):bound(qm+14*d+a*d,2,2,'T_seed')
for p in P[104:]:bound(p,0,0,'prefix')
for p in F:bound(p,0,0,'flight_first');bound(p-d,2,2,'flight_last')
for p in F[:77]:bound(p,2,2,'flight_partial')
for p in T+[te]:bound(230+229j+p,2,2,'T_prefix')
# Every SW period is affine between first and last fullperiod, then partial.
for p in SW:bound(230+229j+p,2,2,'SW_first',True);bound(246+245j+p,0,0,'SW_last',True)
for p in SW[:101]:bound(244+243j+p,0,0,'SW_partial',True)
for p in post+[postend]:bound(p,0,0,'post',True)
# Alln local pruning follows canonical SW first-hit inventory, then fixed remote786.
B_T={complex(*q):i for i,q in enumerate(A['T_output_black'])};tail,drift,dead,tests=future(B_T,te,th);assert tail==A['T_tail_word']and drift==-d and len(dead)==21 and max(dead.values())<104*100-628
remote={complex(*q)for q in A['exact_entry_pruning']['remote']};local={p for p,i in B_T.items()if i in dead};assert len(remote)==786 and min((430+429j+p).real for p in local)>max(p.real for p in remote)
controls=[];reads=0
for au in J['controls']:
 n=au['n'];qt=qm+(n+14)*d;seed=K|{qm+a*d for a in(0,1,6,8)}|{qt+a*d for a in(0,1,3,5,6)};assert len(seed)==22
 start=32433+104*n;end=80270+208*n;s=29671+104*n
 word=pre+fw*n+fw[:76]+A['T_recovery']+A['T_tail_word']*(n-7)+A['T_tail_word'][:100]+'L'+A['postcollision_word'];assert len(word)==end
 z=cert(sim(seed,end,expected=word,cuts={start,s}),NW);Bs,ps,hs=z['snap'][start];pins={0j:20,2*n+250+(2*n+237)*1j:27653+104*n,2*n+231+(2*n+262)*1j:29695+104*n}
 assert max(z['dead'][i]for i in range(-22,0))==27201+104*n
 assert all(Bs[p]==iid and z['B'][p]==iid and iid not in z['dead']for p,iid in pins.items())
 assert(min(p.real for p in Bs),max(p.real for p in Bs),min(p.imag for p in Bs),max(p.imag for p in Bs))==(0,2*n+250,0,2*n+262)
 assert all(0<p.real<2*n+250 and 0<p.imag<2*n+262 for p in z['pts'][start:]+[z['p']])
 enc=lambda B:sorted([[xy(p),i]for p,i in B.items()]);assert enc(Bs)==au['whole_start_black']and enc(z['B'])==au['whole_end_black']
 C={p for p,i in Bs.items()if i in z['dead']};assert len(C)==807 and sorted(map(xy,C))==au['whole_start_relevant'];assert C=={qt+p for p in local}|remote
 assert z['tests']==au['infinite_parity_tests']and[xy(ps),hs]==[list(au['pose_start'][0]),au['pose_start'][1]]
 reads+=end-s;controls.append(dict(n=n,fresh_full_reads=end,reported_suffix_reads=end-s,duration=end-start,relevant=len(C),pins=[dict(cell=xy(p),birth=i)for p,i in pins.items()],parity_tests=z['tests']))
assert reads==228445
review=[
'For strict-interior endpoint cuts, a confined corner has one permitted incoming directed edge and one permitted outgoing edge in the fixed checkerboard sector. Every corner read would have the same turn, so it occurs at most once. Every complete boundary episode is exactly two noncorner reads RR/LL or three reads RRR/LLL through one corner.',
'Use the explicit side order topE/rightS/bottomW/leftN, the R turn from the OUTWARD normal (arrival from interior). Complement non-normal-arrival sites. Both straight color patterns become01to10, lowering weighted first moment by1; each corner changes one endpointbit on each adjacent side, at most2 perturbations per side. Thus side dominos<=L(L+1)/2+2L and boundaryreads<=2W²+2H²+2W+2H-12. Mandatory orientation clarification9a2524e9 is explicitly bound; the original prose remains immutable.',
'Boundary updates plus entry moves cost at most2B. At mostB+1 retained inner HEAD-cut intervals therefore have total duration>=D-2B; one has duration>=max(0,ceil((D-2B)/(B+1))). All their endpoint heads are actually inner. Arbitrary endpoint boundary runs trim<=3 each; fresh16384 arbitrary boundary starts test this endpoint statement. Iteration retains every unread exterior bit and makes no BLACK-hull descent claim.',
'Alln pinning uses the signed complete MT future plus fresh full-field replay. After actual first104, fullBLACK is nonnegative and R20 at0 persists. Every subsequent prefix/flight/T cell is insideQn; exact T lastR6452/8494 attain east/north. The complete following SW train/partial/actualcollision/recovery head path is strictlyinsideQn by affine endpoint bounds atn100 with nonnegative coefficients, hence alln>=100. No boundary color changes. Infinite SW separation and fixed postcollision/NW x<=240,y>0 prove allthree SAME R identities permanently unread.',
'At T-end starta_n, canonical SW first-hit inventory gives21 local current inputs, all consumed before firstoldMcollision, plus the independently signed fixed786 old inputs. The entire later varying field lies beyond the fixed recovery reach, so no other current lifetime is omitted. Thus807 is whole actualC*, not a cropped population or sample maximum.',
'The22-cell family offers arbitrarily many prescribed reset subwindows inside ONE completed global drought, not arbitrarily many completed droughts or one noncapturing orbit. Constant fullBLACK hull can be permanently pinned while head intervals peel inward. Universal record-window occurrence, a global resource decrease and canonical uniqueness remain open.'
]
out=dict(status='PASS finite boundary budget, head-interval peeling and all-n full-field pinned hull with mandatory orientation correction',manifest=sha(D/'DROUGHT_BOUNDARY_PINNING_MANIFEST.json'),script=sha(S),dependencies=m['dependencies'],orientation_addendum_sha256=sha(orientation),local_straight_corner_episodes=len(local_episodes),small_states=len(summary),arbitrary_boundary_start_checks=partial,small_summary=au,all_n_affine_checks=sum(checks.values()),affine_stages=checks,controls=controls,reported_suffix_reads=reads,analytic_review=review)
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(sha(S.with_suffix('.json')))
