from pathlib import Path
from itertools import product
import hashlib,json
S=Path(__file__).resolve();R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();note=D/'G8_CYCLE_THREE_OUTER_MODES.md';assert sha(note)=='fe06a08d38f43886cf33697d65fbd4d04a0b65fa55761ceac345d2ea787ca23e'
V={'N':1j,'E':1,'S':-1j,'W':-1};H='NESW';out=lambda h,i:H[(H.index(h)+(1 if i%2==0 else-1))%4];count=[];surv=[]
for n in (4,5,8,9):
 for hs in product('EW',repeat=n):
  if hs.count('E')!=2:continue
  oo=[out(h,i)for i,h in enumerate(hs)];er=[i for i,h in enumerate(hs)if h=='E'];sr=[i for i,h in enumerate(oo)if h=='S']
  if len(sr)!=2:continue
  a=sum(hs[i]=='E'for i in range(0,n,2));assert n//2+2*a==4
  row=dict(word=''.join(hs),E_ranks=er,S_ranks=sr);count.append(row)
  if er[1]==sr[0]+1:surv.append(row)
assert len(count)==22 and {z['word']for z in surv}=={'EEWW','EEWWW','WEWWE'}
# Actual directed ordinal path, not a repaired transition or static adjacency.
paths=[]
for x in(-3,0,1,8):
 A=complex(x,1-x);B=A-1j;T=B-1;Bp=T+1j;assert Bp+1==A;assert len({A,B,T,Bp})==4
 # A first S -> B first S/R0; B first W -> T sole W/R0;
 # T sole N -> B' last N/R2; B' second E -> A second E.
 assert out('S',0)=='W'and out('W',0)=='N'and out('N',2)=='E'
 paths.append([[int(q.real),int(q.imag)]for q in(A,B,T,Bp,A)])
qrows={}
for I,J in((2,2),(3,3),(2,3),(3,2)):
 totals=[]
 for n in range(2,30,2):
  for X in range(I+1):
   counts=(X,I-X,n//2-X,n-I-n//2+X)
   if min(counts)>=0 and I+n//2-2*X==J:totals.append(n)
 qrows[f'{I},{J}']=sorted(set(totals))
assert qrows=={'2,2':[4,8],'3,3':[4,8,12],'2,3':[6,10],'3,2':[6,10]}
patch=json.loads((D/'check_g8_extremal_boundary_interface.json').read_text());upper=[z for z in patch['complete_histories_on_six_named_classes']if sum(z['cell'])==1];assert {''.join(H[e['h']]for e in z['events'])for z in upper}=={'EEWW','EEWWW'}
for z in upper:
 es=z['events'];sr=[e for e in es if H[e['out']]=='S'];er=[e for e in es if H[e['h']]=='E'];assert er[1]['rank']==sr[0]['rank']+1 and er[1]['clock']==sr[0]['clock']+4
outp={'status':'PASS forced four-step return and three necessary upper modes at E4 boundary','note':sha(note),'all22_count_compatible':count,'three_modes':surv,'fourstep_paths':paths,'next_even_row_count_options':qrows,'analytic_review':[
'The first S departure from A enters its lower SSN neighbor at that neighbor first S/R0 by complete physical port ordinal matching. It goes W to the singleton W/R0, then N to the adjacent SSN last N/R2, then E to A second E arrival. The four physical vertices are distinct until the exact return to A. No unknown upper cell is visited. Hence e1=s0+1 as actual consecutive reads, and clock gap4, without assuming the departure itself is R.',
'Exactly two E arrivals and S departures give floor(n/2)+2a=4. The a2 option lacks two arrivals; a0 forces both E ranks and S ranks odd, contradicting e1=s0+1. Thus n4/5. If firstS even it is e0 and must occur at0, yielding EEWW/EEWWW; if odd it must occur at3 with E ranks1,4, yielding WEWWE. The22-word check is exhaustive only because this count identity gives the multiplicity bound.',
'All four actual physical ports then have multiplicities2 or3. Signed extremal single-use lemma excludes every firstR-to-lastread E edge incident to A. This is E-isolation, not absence of ordinary interactions or an extra output charge.',
'Under g8, next level2 has even histories. Its lower incoming/outgoing counts I,J are2or3; n=2(J-I+2X)<=2(I+J)<=12. Fresh nonnegative inventory equations give4/8 for2,2;4/8/12 for3,3;6/10 for mixed. No uniform bound at higher levels or arbitrary controller follows. The signed open17-event interface uses Y/X and satisfies exact fourstep clocks, so it remains nonempty and uncompleted.'
]}
S.with_suffix('.json').write_text(json.dumps(outp,indent=2)+'\n');print(outp['status'])
