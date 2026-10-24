from pathlib import Path
from collections import defaultdict
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'MIDDLE_SHORT_FORCED_THREE_C_DISCOVERY_CYCLE.md';JF=D/'middle_short_three_C_cycle_certificate.json';assert sha(P).startswith('50990252')and sha(JF).startswith('9b96cc89')and sha(D/'certify_middle_short_three_C_cycle.py').startswith('6536864d');J=json.loads(JF.read_text())
for f,h in J['dependencies'].items():assert sha(D/f)==h
prior=R/'audits/check_C_permanent_pair_channel_independent.json';assert sha(prior)=='01e4725119addc4817f2138f8dacb575bd9a03a2982d87aab306e2fa0d920224';Q=json.loads(prior.read_text());H='NESW';V=[1j,1,-1j,-1];off=[-1j,-1-1j,-1,0j];words=['S','W','S','EEWE','SSNS','EEWE','NNNSS','EEEWW'];xy=lambda p:[int(p.real),int(p.imag)];out=lambda w,r:H[(H.index(w[r])+(1 if r%2==0 else-1))%4];cs=Q['all25_named_chains'];allchannels=[]
for chain in cs:
 ee=[]
 for(t,r),k in chain:
  p=-t+k*(3+1j);h=H.index(words[t][r]);ee.append(dict(level=t,rank=r,lift=k,position=xy(p),heading=h,turn='R'if r%2==0 else'L',C_face=xy(p+off[h])))
 allchannels.append(ee)
canon=lambda a:json.dumps(a,sort_keys=True);assert set(map(canon,allchannels))==set(map(canon,J['all_named_channels']))
pre=next(c for c in allchannels if len(c)==3);assert[(r['level'],r['rank'])for r in pre]==[(7,0),(4,0),(5,2)]and all(r['C_face']==[-8,-1]for r in pre)
Nport=[r for r in range(len(words[5]))if out(words[5],r)=='N'];assert Nport==[1,2,3]
supply=[dict(source_T5_rank=r,target_T8_N_ordinal=i,source_position=[-8,-1],target_position=[-8,0])for i,r in enumerate(Nport)];assert supply==J['complete_N_port_and_ordinals']
# The secondN is exactly the next read after this complete three-R prelude.
assert complex(*pre[-1]['position'])+V[0]==-8+0j
assert all(complex(*r['position'])!=-8+0j for r in pre)
# Rebuild EVERY incident active sector of physical C5, no hidden upper reads.
F5=-8-1j;known=[]
for p,h in[(-7-1j,2),(-8-1j,3),(-7+0j,1)]:
 t=int(3*p.imag-p.real);ranks=[r for r,c in enumerate(words[t])if H.index(c)==h];assert p+off[h]==F5;known.append(dict(cell=xy(p),level=t,heading=h,ranks=ranks))
assert [(r['level'],r['ranks'])for r in known]==[(4,[0,1,3]),(5,[2]),(7,[0,1,2])]
# All named C5 reads are at/after T7R0 by these exact complete ranks.
assert pre[1]['rank']==known[0]['ranks'][0]and pre[2]['rank']==known[1]['ranks'][0]and pre[0]['rank']==known[2]['ranks'][0]
assert(-8+0j)+off[0]==F5
# Remaining C5 corner has only its exactly THREE N arrivals active there;
# arbitrary S arrivals belong to its other active C face and are retained.
assert(-8+0j)+off[2]!=F5
assert sum(len(r['ranks'])for r in known)+len(Nport)==10
invent=defaultdict(list)
for t,w in enumerate(words):
 for r,c in enumerate(w):
  h=H.index(c);f=-t+off[h];lev=int(3*f.imag-f.real)
  if lev in[1,3,5]:invent[lev].append(dict(cell_level=t,rank=r,heading=h,turn='R'if r%2==0 else'L',physical_C=xy(f)))
assert dict(invent)=={int(k):v for k,v in J['complete_known_sector_inventories'].items()};assert[len(invent[t])for t in[1,3,5]]==[6,8,7]
main=next(c for c in allchannels if len(c)==17);assert[main[i]['C_face']for i in[2,7]]==[[-7,-2],[-6,-1]];last=main[-1];assert(last['level'],last['rank'])==(5,1);lp=complex(*last['position']);lh=(last['heading']-1)%4;nf=lp+V[lh]+off[lh];assert nf==-5+0j
steps=[(-8-1j,-7-2j),(-7-2j,-6-1j),(-6-1j,-5+0j)];assert[[xy(a),xy(b)]for a,b in steps]==J['cycle_steps']and steps[-1][1]-steps[0][0]==3+1j
assert len({int(3*a.imag-a.real)for a,b in steps})==3
assert ''.join(r['turn']for r in main[2:7])=='RRRRL'and ''.join(r['turn']for r in main[7:17])=='RRRRLLLLRL'
O=dict(status='PASS exact middle-short core forces genuine three-face WHITE C-discovery cycle; no branch exclusion',proof=sha(P),certificate=sha(JF),script=sha(S),prior_weak_interface=sha(prior),three_R_prelude=pre,exact_T5_N_port=supply,complete_C5_named_sector_reads=known,complete_C_counts={'C1':6,'C3':8,'C5':10},actual_cycle_steps=[[xy(a),xy(b)]for a,b in steps],activation_times_from_T7_R2={'C5':'17-P','C1':2,'C3':7,'C5+d':17},exact_interval_words=['unrestricted P-15','RRRRL','RRRRLLLLRL'],analytic_review=[
'The physical T5 complete N-departure ranks are1,2,3; they supply T8 N arrivals in exactly that order. The fixed T7R0->T4R0->T5R2 prelude therefore ends just before SECOND N arrival, not first. First N must be earlier, and none of the three preceding literal reads is T8, so it precedes the ENTIRE prelude.',
'Every possible active C5 read is independently inventoried: T4 S ranks0/1/3, T5 W rank2, T7 E ranks0/1/2, and exactly three T8 N arrivals. All seven named reads are at/after T7R0; all later T8 N arrivals are after its first. Thus the very first C5 activation is firstT8N, supplied immediately by actualT5.L1 on C3-d. Arbitrarily many T8 S reads remain allowed but are on its other activeface.',
'This eliminates the weak upper C5 first-parent alternative without an upper multiplicity cap, initialT8heading assumption, optional-lap identification or guessed temporal order. The prior weak alternatives remain valid statements. C7 alternatives are unchanged.',
'Combined with independently signed C1/C3 first entries, the distinct full-drift faceclasses give actual C5->C1->C3->C5+d. The literal17-read channel fixes activations at s+2,s+7,s+17; hence full forward winding+1 and exact gapsP-15,5,10. Its fixed latter words are five-readRRRRL and ten-readRRRRLLLLRL; the entire third interval remains open.',
'Completeactiveface counts10/6/8 do not bound exterior excursions, T8other-sector reads, period or globalstock. Selected firstL cells retain their real R0owners. No removablemodule, fullfixedCtrace, controllercompletion, odd/fuelpayment, four-typeexclusion, WHITE S1 or universalcapture theorem follows.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
