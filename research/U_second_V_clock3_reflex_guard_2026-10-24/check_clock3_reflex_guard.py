"""Two exact first-contact loops; strict old-U half-chord confinement."""
from pathlib import Path
from fractions import Fraction
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent;BP=R/'U_star_one_foreign_return_transfer_2026-10-24/check_U_star_corner_transfer.py';n={'__file__':str(BP)};exec(BP.read_text().split('# Exactly twelve constant local suffixes.')[0],n)
W=n['W'];mp=n['mp'];M=n['M'];rot=n['rot'];at=n['at'];add=n['add'];literal=n['literal'];center=n['center'];meet=n['meet'];sub=n['sub'];B=(-1,3);Ustart=(-1,-1);Uend=(-1,7)
# Symbolic quarter-turn lift: N_beforeA=3 plus FIRST rawC1 =>4.
# open=6*pi/2-beta, close=-pi+beta, hence+2*pi. beta in(0,pi/4).
# At B outgoingU=(0,1), reversed incomingV=(1,3); their cross<0 gives
# reflex CCW inside. Reverse oldU ray(0,-1) lies strictly in that sector.
outgoing=(0,1);reverse_incoming=(1,3);old_reverse=(0,-1);cross=lambda a,b:a[0]*b[1]-a[1]*b[0]
assert cross(outgoing,reverse_incoming)<0 and old_reverse[1]<0 and reverse_incoming[1]>0
cases=[]
for a,p in(('Q',(5,0)),('B',(6,1))):
 h=1;aa=n['walk'](a+'CV');pieces=[]
 for atom in aa:
  z0=at(atom['start'],(2*p[0],2*p[1]),h);z1=at(atom['end'],(2*p[0],2*p[1]),h)
  if atom['atom']in'QB':
   zz=at(add((2*atom['entry'][0],2*atom['entry'][1]),rot((-7,-3),atom['entry'][2])),(2*p[0],2*p[1]),h);pieces.extend([(z0,zz),(zz,z1)])
  else:pieces.append((z0,z1))
 assert pieces[-1]==((1,9),B)and pieces[-2]==((3,7),(1,9))
 assert meet(Ustart,Uend,*pieces[-1])==(Fraction(1,2),Fraction(1))
 for z0,z1 in pieces[:-1]:assert meet(Ustart,Uend,z0,z1)is None
 targetmin=2*p[1]+1;assert targetmin in(1,3)
 assert min(q[1]for seg in pieces for q in seg)==targetmin
 # Independent exact component endpoint inequalities; segment minima are
 # endpoint minima. All possible zero-C D/V/U increments are literal.
 increments={}
 for h0 in range(4):
  increments[h0]={b:rot(tuple(literal(W[mp[b]]['word'])['endpoint'][:2]),h0)for b in'DVU'}
 assert all(v[1]>=0 for v in increments[0].values())
 assert all(v[1]>=0 for v in increments[3].values())
 assert all(v[1]<=0 for v in increments[2].values())
 assert all(v[1]<=0 for v in increments[1].values())
 # For C in S, y goes down1; for C in E, nextclock4, excluded by Aclock3.
 cend=literal(W[mp['C']]['word'])['endpoint'];assert rot(tuple(cend[:2]),2)==(0,-1)
 minimum=min(3,targetmin);assert Ustart[1]<minimum
 cases.append(dict(foreign=a,foreign_pose=[*p,h],true_preforeign_C_clock=3,FIRST_atom='C',SECOND_atom='V',SECOND_pose=[0,4,2],foreign_plus_first_and_second_pieces=pieces,first_old_U_contact=dict(source_parameter='1/2',second_parameter='1',point=B),loop_orientation='CCW',corner_inside_reflex_angle='2*pi-beta, beta=atan(1/3)',reverse_incoming_old_U_half_strictly_inside=True,phase_support=dict(source_U_remainder_min_y2=3,N_clock0_after_U_head_y_at_least4=True,N_clock0_corrected_y_at_least7=True,W_clock1_head_y_at_least5=True,W_clock1_corrected_y_at_least9=True,S_clock2_and_C3_minimum_reduced_to_E3=True,E_clock3_head_y_at_least_foreign_y=p[1],E_clock3_corrected_y_at_least=targetmin,foreign_repaired_piece_min_y2=targetmin,FIRST_C_and_SECOND_V_min_y2=3),whole_loop_min_y2=minimum,actual_old_U_start=Ustart,old_start_strictly_below_entire_loop=True))
D=[BP,R/'seven_word_spatial_return_2026-10-23/foreign_kinked_barrier_manifest.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'second_ordinary_after_first_foreign_2026-10-24/old_U_second_contact_LEFT_frontier_manifest.json',R/'U_second_V_original_q_frontier_2026-10-24/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='Only the two necessary old-outgoing-U chronological FIRST new-contact cases Q5,0E+C+V0,4S and B6,1E+C+V0,4S at true preforeign clock3 are excluded. Earlier sourceU half is rigorously inside the simple first-contact loop, but below the whole loop support. No earlier/later arbitrary contacts or unconditional enclosure contradiction.',cases=cases,topological_analytic_obligation='First contact at old-U strict midpoint closes B-to-B future subarc into a Jordan loop. Signed one-foreign tangent lift gives CCW orientation. The reverse incoming old-U half lies in the reflex interior; it cannot leave without another old/new intersection, forbidden by old simplicity and the chronological FIRST-contact premise. Hence oldUstart is strictly inside. A loop contained in y>=minimum has its bounded region there; oldUstart_y=-1 contradicts minimum1/3.',no_age_or_identity_rule_used=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'clock3_reflex_guard.json').write_text(json.dumps(o,indent=2)+'\n');print('Two clock3 Q/B+C+V first contacts excluded: reflex old-U half confined inside loop, whole-loop y2>=1/3 but oldUstart_y2=-1.')
