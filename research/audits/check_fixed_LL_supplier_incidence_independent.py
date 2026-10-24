from pathlib import Path
import ast,json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();files={'fixed_LL_supplier_controls_cannot_put_Y_on_a_b_cycle.md':'c78ff9a789c643535d8052b30306279ee8872705c8e6e6bb4d358382f76dd079','check_fixed_LL_supplier_b_incidence.py':'805a3d643d6c7433cc8bf695ba6dcda535e4097f7d0226397aac510003fb9b18','check_fixed_LL_supplier_b_incidence.json':'2b6b0ce442fb2cfbeab86c42f7f630c07ab73e5af30bebd552a1b828da232fd7','check_fixed_LL_L3_supplier_controls.json':'0d78caa060dfa639958fa1a6413003ddf4384b4486c2f950a945402bba985a2e'}
for f,h in files.items():assert sha(D/f)==h
assert sha(S.with_name('check_LL_supplier_signs_independent.json'))=='7aa261080a34b8ae6bd96c1820216585e29ddb46a41c209bbcf18f72f35567f6'
J=json.loads((D/'check_fixed_LL_L3_supplier_controls.json').read_text());ref=json.loads((D/'check_fixed_LL_supplier_b_incidence.json').read_text());V={'N':1j,'E':1,'S':-1j,'W':-1};xy=lambda q:[int(q.real),int(q.imag)];U=1+2j;Y=1+1j;records=[]
for r in J['rows']:
 hist={complex(*ast.literal_eval(p)):w for p,w in r['histories'].items()};assert hist[U]=='EEE'and hist[2j]=='SSNS'and hist[2+2j]in{'N','NSN'}and hist[Y]=='SNNS'and hist[1]=='EEWW'
 dest=lambda q:q-1j*V[hist[q][0]]
 pred={}
 for target in[U,Y]:
  candidates=[]
  for step in[1,1j,-1,-1j]:
   q=target-step;incomingaxis={1j,-1j}if int(q.real+q.imag)%2==0 else{1,-1};outaxis={-1j*v for v in incomingaxis}
   if step not in outaxis:continue
   assert q in hist
   if dest(q)==target:candidates.append(q)
  pred[target]=candidates
 assert pred[U]==[]and pred[Y]==[U]and dest(U)==Y
 rr=next(z for z in ref['rows']if z['kind']==r['kind']);assert rr['U_indegree']==0 and rr['Y_unique_predecessor']==xy(U)
 records.append(dict(kind=r['kind'],U_predecessors=[],Y_predecessors=[xy(U)],fixed_departures=[dict(cell=xy(q),first_heading=hist[q][0],destination=xy(dest(q)))for q in[2j,2+2j,U,1+0j]]))
# Other exact histories genuinely defeat this PARTICULAR incidence obstruction.
assert (2+2j)-1j*V['S']==U and U-1j*V['E']==Y
out=dict(status='PASS mandatory fixed-LL-controls b-incidence obstruction; prior conditional cycle-owner continuation counterfactual',script=sha(S),bindings=files,controls=records,analytic_review=[
'Fixed Manhattan sector is determined by actual step/turn parity, not an exterior cap or WHITE assumption. AtU only the horizontal physicalneighbors can depart towardit; both are fixed and firstR goesaway. AtY only verticalneighbors can feedit; the sole actual predecessor isU. ThusU has zero bindegree andY cannot be cyclic.',
'Every edge of a full-drift quotient cycle lifts to a physical edge into an actual translate. Translation preserves all complete firstR histories; the same missing incomingedge holds at every U copy. A quotient wrap cannot supply another neighbor or rotate an assigned first heading.',
'This makes the prior conditional global distinct-long-owner consequence in8a0f/Stage37 counterfactual for these TWO FIXED inventories. Their complete local port equations, stream heights, injective clocks and positive45/negative-3 late tails remain validOPEN local networks; possible off-cycle b-tree/factor roles are not excluded.',
'No exclusion of every negative supplier profile. The other modes U=EEWW,T=SSNN do giveT->U->Y and require separate analysis. No exterior-cap,criticalheight,age,fuel,globalfront or attraction theorem is inferred.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
