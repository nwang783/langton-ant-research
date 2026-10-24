from pathlib import Path
from itertools import product
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();files={'negative_L3_transport_has_a_quotient_safe_span_and_owner_gate.md':'4c6aeac8ca663c6d4e5a22e712776f6321d23f86955e63c07dc5ca75303499a9','check_negative_L3_span_owner_gate.py':'54284d8d4c3f3a7e7ebdc68804b5a0972e947790af7cc2fa269350864dc3295a','check_negative_L3_span_owner_gate.json':'39d73c17533fb56aeb957f134066a4987b4106bc1c441ca12cecc2c1eaecc65f'}
for f,h in files.items():assert sha(D/f)==h
DEPS=['check_mixed_first_track_pipeline_independent.json','check_mixed_LL_gate_independent.json','check_mixed_flow2_flat_islands_independent.json'];deps={f:sha(S.with_name(f))for f in DEPS}
for f in DEPS:assert json.loads(S.with_name(f).read_text())['status'].startswith('PASS')
J=json.loads((D/'check_negative_L3_span_owner_gate.json').read_text());V={'N':1j,'E':1,'S':-1j,'W':-1};letter={v:k for k,v in V.items()};xy=lambda p:[int(p.real),int(p.imag)];X=1+0j;Y=1+1j;DD=2+1j;RR=2+0j
outvec=lambda word,i:V[word[i]]*(-1j if i%2==0 else 1j)
# Count match every known physical directed port, then derive actual ordinal successor edges.
for row in J['negative_channels']:
 for rootword in['EWW','EWWE']:
  H={0j:'NNSS',1j:rootword,X:'EEWW',Y:'SNNS',DD:row['D'],RR:row['R']};succ={}
  for p,w in H.items():
   for v in V.values():
    if p+v not in H:continue
    outgoing=[i for i in range(len(w))if outvec(w,i)==v];incoming=[i for i,c in enumerate(H[p+v])if V[c]==v];assert len(outgoing)==len(incoming)
    for a,b in zip(outgoing,incoming):succ[(p,a)]=(p+v,b)
  expected=[[(RR,1),(X,2),(Y,2),(DD,1)],[(Y,3),(DD,2),(RR,2),(X,3)]]
  assert row['paths']==[[[xy(p),i]for p,i in path]for path in expected]
  for path in expected:assert all(succ[a]==b for a,b in zip(path,path[1:]))and ''.join('R'if i%2==0 else'L'for p,i in path)=='LRRL'
  # Physical b geometry rules out supplier LEFT-contact roles, not all Gamma membership.
  assert outvec(H[Y],0)==-1 and outvec(H[DD],0)==1j
  assert outvec(H[DD],0)==1j and outvec(H[RR],0)==1
  assert outvec(H[X],0)==-1j and sum(outvec(H[X],i)==-1j for i in range(4))==2
# Independent all small closed-pose paths and the unique four-step Y2->Y3 geometry.
def walk(word,p,v):
 trace=[];origin=p;early=[]
 for t,c in enumerate(word):
  trace.append([xy(p),letter[v],c]);v*=1j if c=='L'else-1j;p+=v
  if p==origin and t+1<len(word):early.append(t+1)
 return p,v,trace,early
short={}
for n in[4,8]:
 good=[]
 for chars in product('LR',repeat=n):
  if chars[0]!='L':continue
  w=''.join(chars);p,v,tr,early=walk(w,0j,1)
  if p==0j and v==1 and not early:good.append(w)
 assert good==J['raw_short_returns'][str(n)]and all('LRRL'not in w for w in good);short[n]=good
square=[]
for chars in product('LR',repeat=3):
 w='R'+''.join(chars);p,v,tr,early=walk(w,Y,1j)
 if p==Y and v==-1j and not early:square.append((w,tr))
assert len(square)==1 and square[0][0]=='RLLL'and [r[0]for r in square[0][1]]==[xy(Y),xy(DD),[2,2],[1,2]]
body='LRRLLLLRRL';p,v,tr,_=walk(body,RR,1j);assert(p,v)==(1-1j,-1j)and body==J['fused_ten_word']
frames=[]
for prelen in[1,2]:
 for cs in product('LR',repeat=2):
  pre=''.join(cs[:prelen]);post=''.join(cs[prelen:])
  if pre[0]!='L':continue
  for hi in V.values():
   d,vv,_,_=walk(pre,0j,hi)
   if vv!=1j:continue
   root=RR-d;word=pre+body+post;p,vv,trace,early=walk(word,root,hi)
   if p==root and vv==hi and not early:frames.append(dict(root=xy(root),incoming=letter[hi],prefix=pre,word=word,trace=trace))
assert frames==J['only_twelve_frames']and {(tuple(z['root']),z['incoming'])for z in frames}=={((2,-1),'E'),((1,-1),'S')}
# Each frame's physical b incoming/outgoing forces the stated critical gate.
B=1-1j;H=2-1j
assert X-1j==B
# Frame1 owner H receives its LEFT b-edge from B and sends N; B receives S from X and sends E.
assert B+1==H and H+1j==RR
# Frame2 owner B receives the TWO-use S edge from X; this is flow2 O/U after flat X, not a high3 root.
assert sum(outvec('EEWW',i)==-1j for i in range(4))==2
out=dict(status='PASS exact negative-supplier span transport and conditional physical owner>=12 / fused>=16 gate',script=sha(S),bindings=files,dependencies=deps,short_returns=short,twelve_frames=frames,analytic_review=[
'Both complete matched supplier alternatives WEE/NNS and WEEW/NNSS, for both real LL-rootO/U histories, retain all internal count/ordinal edges. They force two actual LRRL channels, T2Y=T2X+1 and T3X=T3Y+3, hence A23X=A23Y+4. A23 is invariant under every full-drift translate; a genuinely closed quotient cycle of positive increment is impossible, but no recurrence/coverage of these transport edges is proved.',
'D cannot be a LEFTGamma contact because its required b-predecessorY firstR pointsW, notE. R cannot be LEFTGamma because the required D firstR pointsN, notS. RIGHTGamma L1/R2 ports are LEFT; an offGamma vertex cannot cross the embeddedboundary. Both displayed channels therefore stayLEFT and belong to physical critical same-contact returns. Exhaustive4/8 firstreturns with initialL contain no LRRL, yielding owner span>=12. Owners may coincide or be different translates; no budgets are added.',
'If actual A23Y=4, exact four-step return with incomingN toincomingS is uniquelyRLLL through D,T,U. Those two intermediate visits are actualL, independent of their unspecified complete histories. Since exitLEFT->RIGHT requires an R2 event, they cannot split the enclosing LEFT excursion. The fused ten-read actual channel has a single owner; this uses critical same-contact topology, not a repaired or hypothetical word.',
'R is not a crossing root, so a span12 owner has1or2 turns before the ten-read channel and0or1 after. Full pose and firstreturn reconstruction leaves exactly LL extra turns in the two recorded physical frames. Root(2,-1)E is secondLEFT after X->(1,-1), excluded by mixed lastLEFTgate. Root(1,-1)S receives exactly two physical uses from flatX, so is a flow2O/U crossing afterX, excluded by signed GLOBALM flat-island theorem. No guessed T/U full history, canonical sheet, exterior period or age upperbound is used.',
'CompleteWHITE/cap4, criticalGLOBALM and no-one-use hypotheses remain for owner/gate conclusions. Fixed8a0f controls are not reinstated onGamma. No actual fullfactor/front, iteratedspanincrease, ownerinjection, fuelbound or globalexclusion is claimed.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
