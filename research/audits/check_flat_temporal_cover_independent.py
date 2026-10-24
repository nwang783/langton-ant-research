from pathlib import Path
from itertools import product
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'critical_flat_ages_have_an_exact_pointwise_temporal_cover.md';J=json.loads((D/'check_temporal_flat_cover_cochain.json').read_text());H='NESW';modes={'X':'EEWW','Y':'EWWE','source3':'EWE','sink3':'EEE','source4':'EWEW','sink4':'EEEE','O':'WEE','U':'WEEW','V':'WWEE','left3':'WEEE'};ports=[]
for name,w0 in modes.items():
 for turn in range(4):
  w=''.join(H[(H.index(c)+turn)%4]for c in w0);ci=(1+turn)%4;co=(H.index(w[0])+1)%4;arr=[i for i,c in enumerate(w)if H.index(c)==ci];out=[i for i,c in enumerate(w)if(H.index(c)+(1 if i%2==0 else-1))%4==co];f,g=len(arr),len(out);assert f>=2 and g>=2;ri=arr[1 if f==2 else 2];ro=out[1 if g==2 else 2];assert ri!=arr[0]and ro!=out[0]
  expected=(1,3)if name=='X'else(3,1)if name=='Y'else(2,1)if name in('O','U')else(2,2)if name in('source3','sink3','source4','sink4')else(3,3)
  assert(ri,ro)==expected;ports.append(dict(mode=name,rotation=turn,history=w,in_flow=f,out_flow=g,selected_in_rank=ri,selected_out_rank=ro))
rows=[];times=0
for n in range(2,6):
 for kinds in product('XYO',repeat=n):
  jumps=[{'X':8,'Y':-12,'O':-4}[c]for c in kinds];period=-(n+sum(jumps))
  if period<=0:continue
  cur=0;parts=[];edge=[]
  for c,delta in zip(kinds,jumps):
   nxt=cur+delta;parts.append((cur,nxt,c));parts.append((nxt,nxt+1,'B'));edge.append(nxt);cur=nxt+1
  assert cur==-period
  for t2 in range(1,2*period,2):
   covers={c:0 for c in'XYOB'}
   for a,b,c in parts:
    signed=(t2-2*a)//(2*period)-(t2-2*b)//(2*period);covers[c]+=abs(signed)
   assert covers['B']+covers['X']-covers['Y']-covers['O']==-1;assert covers['Y']-covers['X']==1+covers['B']-covers['O'];times+=1
  rows.append(dict(kinds=''.join(kinds),P=period,selected_event_phases_distinct=len({a%period for a in edge})==n))
assert rows==J['rows']and len(rows)==225 and sum(r['selected_event_phases_distinct']for r in rows)==175
# No actual critical side assumption is imposed on those algebraic examples.
for right,I2,I3 in[(1,0,0),(0,1,0),(0,0,1)]:
 for B in(0,1):
  if B and right:continue
  d=1+B-I2;assert d==B+right+I3 and 0<=d<=2
out=dict(status='PASS exact pointwise signed temporal cover under critical global-M no-one-use hypotheses',proof=sha(P),algebra_certificate=sha(D/'check_temporal_flat_cover_cochain.json'),script=sha(S),all_rotated_selected_ports=ports,algebra_controls=225,regular_cut_checks=times,analytic_review=['The signed exhaustive global-M no-one-use macro cover leaves exactly the ten rotated boundary roles reconstructed here. Every gamma edge selects ordinal2 ifflow2 and ordinal3 ifflow3/4. At all through roles the same actual rank is selected; only X1->3,Y3->1,O/U2->1 are temporal jumps. No other full rank or third/fourth copy is erased.','Each selected outgoing event is at a different embedded gamma vertex class, hence has a distinct phase in the ONE actual P-event orbit. Its physical edge occurrence is notfirst, so strictly LEFT in the signed first-track split. Thus B is an indicator and B*R=0. These geometric/chronological premises are analytic; the225 cochains are only arithmetic controls, some deliberately lack distinct phases.','For a regular cut t, oriented all-translate multiplicity of[a,b] is floor((t-a)/P)-floor((t-b)/P). Summing around the lifted selected polygon telescopes fromT toT-P and equals-1 exactly. This proves B+nX-nY-I2=-1 pointwise, retaining every translated physical age even aboveP, rather than inferring it from its average.','Critical first-track chronology partitions every actual unit edge into RIGHT or one disjoint physical flow2/flow3 L1->R2 excursion. Thus R+I2+I3=1 and nY-nX=B+R+I3. The exact signed DIFFERENCE is0..2; neither nX nor nY separately is bounded.','An interval after leaving the selected lane and before its next actual entry contains no selected unit edge. Every flatL1/L3 is a selected incoming or outgoing endpoint, so no such endpoint lies strictly inside this interval; the signed potential is constant. It may contain other complete flow3 excursions and RIGHT factors, and no fixed exterior root owner or embeddedness is inferred.','Integrating gives sumYage-sumXage=P+ell-sumflow2Delta. The unique RIGHT circuit clock substitutesP=L_RIGHT+sumflow2Delta+sumflow3Delta, yielding ell+L_RIGHT+sumflow3Delta. Flow2 waits cancel exactly and must not be charged again. Yexists, but no initial fuel, individual lifespan, number of old copies, K>=2 exclusion or completed exterior is proved.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
