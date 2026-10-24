from pathlib import Path
from itertools import product
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
proof=D/'mixed_departure_second_lane_forces_an_open_junction.md';code=D/'check_mixed_departure_second_lane_junctions.py';cert=code.with_suffix('.json')
assert sha(proof)=='a37a9d330a347d07b3108e8b24a6f8ec9be5f7e37a78396f7892b32e0a011915'
J=json.loads(cert.read_text());H='NESW';v=(1j,1,-1j,-1)
out=lambda hist,k:(H.index(hist[k])+(1 if k%2==0 else -1))%4
ports=lambda hist,head,io:[k for k in range(len(hist)) if (H.index(hist[k]) if io=='in' else out(hist,k))==head]
rot=lambda hist,h:''.join(H[(H.index(x)+h)%4] for x in hist)
xy=lambda z:[int(z.real),int(z.imag)]
def nodes(tw,bits,st='EWE',en='EEE'):
 p=1j;ci=1;bb=iter(bits);res=[]
 for k,turn in enumerate(tw):
  hist=st if k==0 else en if k==len(tw)-1 else next(bb) if turn=='R' else 'WEEE'
  hist=rot(hist,ci-1);co=(ci+(1 if turn=='R' else -1))%4
  res.append(dict(cell=xy(p),turn=turn,history=hist,cycle_incoming=H[ci],cycle_outgoing=H[co]));p+=v[co];ci=co
 return res
def scatter(ns):
 n=ns[0];rank=ports(n['history'],H.index(n['cycle_incoming']),'in')[1];route=[]
 for i,n in enumerate(ns):
  hist=n['history'];co=H.index(n['cycle_outgoing']);hh=out(hist,rank)
  route.append(dict(vertex=i,cell=n['cell'],rank=rank,incoming=hist[rank],outgoing=H[hh]))
  if hh!=co:
   # Physical side at an L/R square corner, independent of macro label.
   ci=H.index(n['cycle_incoming']);assert hh==(ci+(1 if n['turn']=='L' else -1))%4
   return dict(kind='EXIT',side='RIGHT' if n['turn']=='L' else 'LEFT',at_vertex=i,at_rank=rank,physical_target=xy(complex(*n['cell'])+v[hh]),heading=H[hh],route=route)
  ordinal=ports(hist,co,'out').index(rank)
  if i+1==len(ns):assert ordinal==1;return dict(kind='THROUGH',output_ordinal=2,route=route)
  nxt=ns[i+1];assert complex(*nxt['cell'])==complex(*n['cell'])+v[co]
  incoming=ports(nxt['history'],co,'in');assert len(incoming)==len(ports(hist,co,'out'))
  rank=incoming[ordinal]
 raise AssertionError
macros=[]
for tw in ('RR','RLR','RLRR','RRLR','RRLRR'):
 for bits in product(('EEEW','EWEE'),repeat=tw.count('R')-2):
  ns=nodes(tw,bits);sc=scatter(ns);assert(sc['kind']=='THROUGH')==(tw in ('RR','RLR'))
  macros.append(dict(flow3_turn_word=tw,internal_RIGHT_histories=list(bits),complete_nodes=ns,second_lane=sc))
assert macros==J['flow3_macros'] and len(macros)==10
f4=nodes('RR',(),st='EWEW',en='EEEE');ff=dict(nodes=f4,second_lane=scatter(f4));assert ff==J['flow4_macro']
assert [r['rank'] for r in ff['second_lane']['route']]==[2,2]
# Reconstruct complete constant-two local alphabet, not only supplied rows.
alphabet={}
for turn,start,ci,co in [('R','E',1,2),('L','W',1,0)]:
 allowed=[]
 for n in range(1,5):
  for tail in product('EW',repeat=n-1):
   hist=start+''.join(tail)
   if len(ports(hist,ci,'in'))==len(ports(hist,co,'out'))==2:allowed.append(hist)
 alphabet[turn]=allowed
assert alphabet=={'R':['EEWW','EWWE'],'L':['WEE','WEEW','WWEE']}
loc=[]
for turn,hist,ci,co in [('L','WWEE',1,0),('L','WEE',1,0),('L','WEEW',1,0),('R','EEWW',1,2),('R','EWWE',1,2)]:
 ns=[dict(cell=[0,1],turn=turn,history=hist,cycle_incoming=H[ci],cycle_outgoing=H[co])];ss=scatter(ns)
 assert(ss['kind']=='THROUGH')==(hist=='WWEE');loc.append(dict(turn=turn,history=hist,second_lane=ss))
assert loc==J['flow2_internal_contacts']
report=dict(status='PASS mixed no-one-use global-max cap4 departure circle requires a listed actual second-lane exit',proof_sha256=sha(proof),checker_sha256=sha(code),certificate_sha256=sha(cert),independent_checker_sha256=sha(S),all10_flow3_scatterings=macros,flow4=ff,complete_constant2_alphabet=alphabet,flow2=loc,analytic_scope=['Signed maximal3 templates include their true2-to3 source and3-to2 sink under no-one-use; signed isolated4 pair retained. All short macro transitions here are uninterrupted ACTUAL same-rank successor edges, not repaired exchanges or waiting gaps.','If no listed exit occurs, second ordinal between macros becomes third inside short3/4 and returns to second. One selected real read per boundary vertex follows every gamma edge once, including seam lift. Gamma winding -1 would force the same rank at v-d after positive ell updates, while full-front equivariance gives time difference -P. Contradiction.','Nonlocal chord exits remain real open junctions, not absent exterior or fuel. No critical K1 hypothesis, period/count bound, attainable full front, or universal one-use follows.'])
S.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print('PASS',sha(S.with_suffix('.json')))
# Separate analytic scope addendum.
bp=D/'boundary_local_cap4_first_track_extension_and_single_use_level.md';assert sha(bp)=='3eee26b9785a7af4b759bca2e0c3c96c5018d65a4d0b1c1aff8b60613194b789'
deps=[R/'audits/check_mixed_first_track_pipeline_independent.json',R/'audits/check_single_used_first_circle_independent.json',R/'periodic_classification_new/cap_three_shifted_stream_height.md']
br=dict(status='PASS boundary-local cap4 extension and cap-free single-used boundary level only',proof_sha256=sha(bp),dependencies={str(p.relative_to(R)):sha(p) for p in deps},argument=['Only b-circle vertices require the complete WHITE cap4 inventory for local first-R C-maximum and m(b(v))>=m(v); finiteness of the full-drift b-cycle forces equality and constant selected c. Exterior stream integration, current partition and actual chronology need no exterior cap.','For a physical single-used outgoing first-R port, later heading ranks force A,A,-A,A,-A,... . Single-used incoming cycle port then forces singleton at RIGHT, and exactly3/4 reads at LEFT. Thus the required boundary inventory is derived without global cap. This is the signed29cce94f setting, not a new all-cap first-R maximum claim.','Single-used boundary has no LEFT copy or crossing; nonempty separated LEFT events would be successor-invariant, contradicting the one actual full-P event orbit. Entire actual support is geometric RIGHT.','Unrestricted stream integration/homology is Section1 of cap_three_shifted_stream_height, independent of its later cap3 premises. For winding -1 gamma, geometric RIGHT is global LEFT exterior; W_R=c-1-c_left=c-c_right. Entire actual current has winding1, so c=c_left+2=c_right+1. For d3,1, increasing3y-x is LEFT of+d and RIGHT of gamma.'],not_claimed=['any outside multiplicity or stream-height bound','all-cap first-R maximum','bound on aggregate voltageK','controller existence or capture'])
q=R/'audits/boundary_local_first_track_independent.json';q.write_text(json.dumps(br,indent=2)+'\n');print('BOUNDARY PASS',sha(q))
