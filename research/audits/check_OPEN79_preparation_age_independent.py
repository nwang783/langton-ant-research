from pathlib import Path
from itertools import product
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for row in(D/'OPEN79_PREPARATION_FORK_SHA256SUMS').read_text().splitlines():h,f=row.split();assert sha(D/f)==h
J=json.loads((D/'open79_preparation_fork_certificate.json').read_text())
for f,h in J['dependency_hashes'].items():assert sha(D/f)==h
assert sha(S.with_name('check_OPEN79_age_independent.json'))=='015a698f2edcda92746c5f3fe50e64f6d43fffdbf4075564ecf97338224d798a'
H='NESW';V=[1j,1,-1j,-1];turn=lambda h,c:(h+(1 if c=='R'else-1))%4;h11='WEEEEEEWWEEEWEWE';h12='SSNNNSNSSSSSSSSSSS';outs=lambda w:[turn(H.index(h),'RL'[r%2])for r,h in enumerate(w)]
assert list(map(H.index,h11))==J['complete_named_histories']['T11']and list(map(H.index,h12))==J['complete_named_histories']['T12']
A=1+0j;B=0j;C=-1+0j;U=1j;VV=-1+1j;Q=1+1j;X=2+1j;drift=3+1j
# Exhaust all kinematic routes shorter than7 from B.R8 to C incomingS.
routes=[]
for length in range(1,7):
 for ss in product('RL',repeat=length-1):
  word='R'+''.join(ss);p=B;h=3;vis=[]
  for ch in word:vis.append((p,h,ch));h=turn(h,ch);p+=V[h]
  if(p,h)==(C,2):routes.append((word,vis))
assert[r[0]for r in routes]==['RLL'];assert routes[0][1]==[(B,3,'R'),(U,0,'L'),(VV,3,'L')]
# Complete immediate predecessor fork: Q must departS, so W/L orE/R.
predecessors=[]
for qh,ch in product((1,3),'RL'):
 if turn(qh,ch)!=2:continue
 prev=Q-V[qh]
 for uh,uc in product((0,2),'RL'):
  if turn(uh,uc)!=qh:continue
  predecessors.append((prev,uh,uc,qh,ch))
assert len(predecessors)==4
for prev,uh,uc,qh,ch in predecessors:
 if prev==X:assert qh==3 and ch=='L'and(uh,uc)in((0,'L'),(2,'R'))
 else:
  assert prev==U and qh==1 and ch=='R'
  if uh==2:assert uc=='L' # U would be L at-2 and+2 with onlyQ,A,B between.
  else:
   assert uh==0 and uc=='R'and U-V[uh]==B
   assert h11[7]=='W'and outs(h11)[7]==2 # actual previousB mustrank7 and departS, notN.
allowed=[r for r in range(8)if outs(h12)[r]==3];assert allowed==[0,3]and X==C+drift
# X at tau-2 equals canonical rankk+P; C.rank8 at tau+4, so t8-tk=P+6.
# signed chain: t11-t3=P-34. k3 would force t8-t11=40 against 3 rank gaps>=4.
cycle=J['rejected_rank3_positive_clock_cycle'];assert [(r['source'],r['target'],r['constant'],r['P'])for r in cycle]==[(8,9,4,0),(9,10,4,0),(10,11,4,0),(11,8,40,0)]and sum(r['constant']for r in cycle)==52
sarr=[r for r,h in enumerate(h12)if h=='S'];assert sarr.index(0)==0 and sarr.index(8)==4
assert C+1j==VV and (-15+0j)+drift==-12+1j # physical source T15+d to canonicalT12.
ctl=J['prepared_seven_control'];p=complex(*ctl['initial_position']);h=ctl['initial_heading'];black={complex(*q)for q in ctl['initial_black']};assert(p,h,black)==(X,2,{Q,U,VV});events=[]
for t,ch in enumerate(ctl['word']):
 assert(ch=='L')==(p in black);events.append(dict(time=t,position=[int(p.real),int(p.imag)],incoming_heading=h,turn=ch));black.symmetric_difference_update({p});h=turn(h,ch);p+=V[h]
assert events==ctl['events']and events[-1]['position']==[-1,0]and[int(p.real),int(p.imag)]==ctl['final_position']and h==ctl['final_heading']and sorted([[int(q.real),int(q.imag)]for q in black])==ctl['complete_final_black']
out=dict(status='PASS conditional OPEN79 gap3 forces exact P+6 preparation age and future S0-to-S4 debt',proof_sha256=sha(D/'OPEN79_SHORT_GAP_FORCES_PREPARATION_AGE.md'),certificate_sha256=sha(D/'open79_preparation_fork_certificate.json'),signed_chain_report=sha(S.with_name('check_OPEN79_age_independent.json')),all_routes_shorter_than7=[r[0]for r in routes],upper_departure_ranks=allowed,positive_rank3_cycle_weight=52,prepared_control_reads=len(events),analytic_review=['The conditional canonical gap is the physical B-to-C gap because their representatives lie on the same y0 lift. Exhaustive short kinematics forces U.N/L,V.W/L. Q predecessor has exactly four heading/turn options; two atX are the owned rank0/3 alternatives, while the two viaU fail no-intervening-read color or B complete rank7 heading. No exterior field is set WHITE.','X=C+d makes its actual time t12,k+P. Therefore t12,8-t12,k=P+6 and k<8. Complete named T12 history leaves only W departures0/3. Signed chain ageP-34 plus actual rank ordering rejects3 by a zero-voltage positive52 cycle, leavingrank0.','S arrivals at named ranks0/8 are exact ordinals0/4. Their physical sources are the same T15+d, so subtracting both source clock equations preservesP+6. Later source is actualV.W/L; earlier source is not claimed to be first read.','Prepared7 control is a genuine full-board finite factor with three BLACK helpers, not the entire OPEN79 history or autonomous controller. Rank0 age branch and all longer gaps remain OPEN; no debt growth or new front exclusion follows.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
