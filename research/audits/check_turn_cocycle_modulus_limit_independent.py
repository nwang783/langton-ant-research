from pathlib import Path
import hashlib,json
S=Path(__file__);P=S.parents[1]/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();F=P/'TURN_POSITION_COCYCLE_MODULUS_LIMIT.md';assert sha(F)=='f55830eca216ada2c76af18faa421a7ca6e04b3e37b128071fdd853edc6345b8'
# Coefficients [A,B,E/W successor1, successor2,w,constant].
even=[[ -1,0,1,0,-1,0],[-1,0,0,1,1,0],[0,-1,0,1,-1,0],[0,-1,1,0,1,0]]
odd=[[-1,0,1,0,-1,-1],[-1,0,0,1,1,1],[0,-1,0,1,-1,1],[0,-1,1,0,1,-1]]
for rows in(even,odd):
 q=[sum(a*x for a,x in zip([1,-1,1,-1],col))for col in zip(*rows)];assert q==[0,0,0,0,-4,0]
p=0j;h=1j;trace=[]
for c in'RLRRLL':
 trace.append([int(p.real),int(p.imag),int(3*p.imag-p.real),c]);h*=(-1j if c=='R'else 1j);p+=h
assert p==3+1j and h==1j
out=dict(status='PASS analytic sharp modulus limit for the stated universal linear position/turn unit-winding ansatz',proof=sha(F),local_four_equation_elimination={'even':even,'odd':odd,'combination':[1,-1,1,-1],'result':'4*w(T)=0 at every allowed vertex'},six_step_path=trace,endpoint=[3,1,'N'],analytic_review=[
'Even incoming N/S and odd incoming E/W use identical successor states under the opposite choices. Correct vertical displacement signs in odd equations eliminate to4w=0 without dividing by2 or assuming m odd.',
'The geometric RLRRLL path restores heading and has exact full displacement(3,1), so T=3y-x returns unchanged. The summed universal move identity gives signed weight sum1 in Z/m. Multiplying by4 forces4=0 and hence m divides4.',
'The same reasoning permits arbitrary position-dependent weights/potentials provided the potential is periodic under FULL(3,1). No additional T period or board legality is required. The already signed24-state mod4 table attains the limit.',
'Only this universal linear signed-turn coefficient with unit dy winding is bounded. Chronological, nonlinear, local-rank, board-dependent, or multiplicity-retaining invariants and nonprimitive/nonunit winding are outside scope. No new front or parameter exclusion follows.'
],attaining_mod4_report=sha(S.parent/'check_drift31_mod4_cocycle_independent.json'))
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
