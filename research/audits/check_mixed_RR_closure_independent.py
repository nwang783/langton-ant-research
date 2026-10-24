from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();F=D/'mixed_RR_boundary_closure_and_required_flat_RIGHT_exits.md';assert sha(F)=='f008184db7e904542e3a674c0225248cc70a0b572578a440a963fb290c14e4a9'
V={'N':1j,'E':1,'S':-1j,'W':-1};I={v:k for k,v in V.items()};out=lambda h:[I[V[c]*(-1j if r%2==0 else 1j)]for r,c in enumerate(h)];rank=lambda h,d,kind:[r for r,c in enumerate(h if kind=='in'else out(h))if c==d]
words=lambda axis:[''.join(q)for n in range(1,5)for q in product(axis,repeat=n)]
zwords=[h for h in words('NS')if h[0]=='N'and h.count('S')==out(h).count('E')>0];ywords=[h for h in words('EW')if h[0]=='E'and h.count('W')==out(h).count('S')>0]
rights=[h for h in words('EW')if h[0]=='E'];bs=[h for h in words('NS')if h[0]=='S'];assert(len(zwords),len(ywords),len(rights),len(bs))==(6,6,15,15)
J=json.loads((D/'check_general_mixed_RR_square_gate.json').read_text());counts=Counter();pairs=set();no1=set();survivors=[]
for z,a,b,y in product(zwords,rights,bs,ywords):
 hs=[z,a,b,y];dirs=['E','S','W','N'];source=[rank(hs[k],d,'out')for k,d in enumerate(dirs)];target=[rank(hs[(k+1)%4],d,'in')for k,d in enumerate(dirs)]
 if any(len(s)!=len(t)or not s for s,t in zip(source,target)):counts['port mismatch']+=1;continue
 arrivals=[target[(k-1)%4][0]for k in range(4)];departs=[s[0]for s in source];assert arrivals[:3]==departs[:3]==[0]*3
 # Consecutive physical unit-square edges imply T_in(Y)=T_out(Y)+4.
 assert arrivals[3]in(1,2)and departs[3]==3-arrivals[3]
 if arrivals[3]<departs[3]:counts['positive first-ordinal clock']+=1;continue
 assert(arrivals[3],departs[3])==(2,1)
 assert source[3][:2]==[1,2]and len(target[3])>=2
 if target[3][1]!=1:assert target[3][1]==3;counts['Z first-to-rank3 gap forced4']+=1;continue
 counts['necessary first-ordinal survivors']+=1;pairs.add((z,y));survivors.append(hs)
 if min(len(s)for s in source[:3])>=2:assert(z,y)==('NNSS','EEWW');no1.add((a,b,len(source[1])))
assert dict(counts)==J['all8100_counts']and sum(counts.values())==8100
assert pairs=={(r['Z'],r['Y'])for r in J['necessary_LEFT_endpoint_pairs']}
assert no1=={(r['A'],r['B'],r['internal_flow'])for r in J['no_one_use_RIGHT_pairs']}
assert len(pairs)==5 and len(no1)==6
# Geometric extension of every forbidden longer max-flow3 template: a neighboring RR run has LEFT on each side.
for tw in('RLRR','RRLR','RRLRR'):
 # Complete potential adjacent turns, imposing no3same on the embedded essential b curve.
 extensions=[l+tw+r for l,r in product('LR',repeat=2)if'RRR'not in l+tw+r and'LLL'not in l+tw+r]
 assert extensions
 for ext in extensions:
  windows=[ext[k:k+4]for k in range(len(ext)-3)];assert'LRRL'in windows
  # At least one LEFT in that LRRL lies internally in the flow3 macro, hence has physical flow3.
  assert any(ext[k:k+4]=='LRRL'and any(1<=j<=len(tw)and tw[j-1]=='L'for j in(k,k+3))for k in range(len(ext)-3))
M=json.loads((R/'audits/check_mixed_second_lane_independent.json').read_text());assert all(r['second_lane']['kind']=='THROUGH'for r in M['all10_flow3_scatterings']if r['flow3_turn_word']in('RR','RLR'));assert M['flow4']['second_lane']['kind']=='THROUGH'
outobj=dict(status='PASS mixed RR boundary closure and conditional critical flat-RIGHT exit reservation',proof=sha(F),author_checker=sha(D/'check_general_mixed_RR_square_gate.py'),author_certificate=sha(D/'check_general_mixed_RR_square_gate.json'),independent_alphabets={'Z':zwords,'Y':ywords,'A':rights,'B':bs},all8100_counts=dict(counts),necessary_endpoint_pairs=sorted(pairs),no_one_use_RIGHT_pairs=sorted(no1),analytic_review=[
'The closing physical N edge Y->Z is NOT another b edge. All its copies are nevertheless fixed by complete endpoint histories. Unit-square first ordinal gives T_inY=T_outY+4. O/U/flow3 would have L1 before R2 and forces positive4+Delta=0. Flow1/V instead have R2 arrival and L1 departure, fixing Delta12Y=4.',
'The first2 N departures at Y are L1/R2, so first2 N arrivals at Z are4apart. Their first is R0 and second cannot be L3 across3same-cell gaps>=12. Independent full8100 product leaves exactly5endpoint pairs, none O/U/flow3. No exterior profile/period bound is imposed.',
'On an embedded essential actual b-circle,3consecutiveRIGHT turns repeat the prior physical vertex and are impossible. Thus anyRRrun hasLEFTneighbors. Every longer maximal3 template RLRR/RRLR/RRLRR has such an actual LRRL window with an INTERNAL flow3 LEFT endpoint, contradicting the local gate. The external LEFT may have flow1, fully retained in the6-profile cover. Maximum-level dependency only enters the earlier5-template list.',
'At GLOBALM, maximal3 is consequently RR or RLR; with nooneuse both are exact source/sink transparent actual second-lane macros. Isolated4 and flow2LEFTV are transparent too. Remaining exits are flat2RIGHT toLEFT or flow2LEFT O/U R2 toRIGHT.',
'At criticalM=c_right+1 every flow2 O/U root L1, whether singleton or LL-first, launches that actual second lane. Wrong physical RIGHT endpoint and full negative lap are forbidden. First hit is a flatRIGHT exit; no through path contains another rootL1. Full-P permutation backward uniqueness injects these root classes into flatRIGHT exit events. If no roots and noflat, the closed negative lane itself contradicts actualtime.',
'A flat2RIGHT junction is mandatory, not impossible. Its exterior continuation, old stock, odd roots and arbitrary numbers of such junctions remain OPEN; no general oneuse/front/capture or fuel theorem follows.'
],dependencies={str(p.relative_to(R)):sha(p)for p in[R/'audits/check_flow3_double_LEFT_independent.json',R/'audits/check_mixed_second_lane_independent.json',R/'audits/check_mixed_LL_gate_independent.json',R/'audits/check_critical_mixed_LL_exits_independent.json']})
S.with_suffix('.json').write_text(json.dumps(outobj,indent=2)+'\n');print(outobj['status']);print(sha(S.with_suffix('.json')))
