from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(D/'OPEN79_ALL_LENGTH_TWO_PORT_REIMPORT.md')=='9287061e1444cbcee14fbaafaaaa6d50069b37da26326027b1c686a83208514d';assert sha(D/'certify_open79_cluster_reimport.py')=='a55e51bcf117d1e1e2b29fe5110c771a0111c93786fbbcf7286f632e7bf04bdd';assert sha(D/'open79_cluster_reimport_certificate.json')=='fd01e7c72045321f6496e338d10d255ad2e702db7da17a4ce829d9dd9f9b74db'
J=json.loads((D/'open79_cluster_reimport_certificate.json').read_text())
for f,h in J['dependency_hashes'].items():assert sha(D/f)==h
P=json.loads((D/'physical_return_debt_certificate.json').read_text());hist=next(r for r in P['specified_open_debt_interface']if r['open_graph']['event_count']==79)['named_histories'];H='NESW';assert ''.join(H[v]for v in hist['9'])=='WWWEWW';assert ''.join(H[v]for v in hist['10'])=='SNSSSN';assert ''.join(H[v]for v in hist['11'])=='WEEEEEEWWEEEWEWE'
assert hist['10'][2:4]==[2,2]and hist['11'][8:10]==[3,1];assert hist['12'][0:4]==[2,2,0,0]and hist['12'][8:11]==[2,2,2]
X=2+1j;U=1j;Q=1+1j;A=1+0j;B=0j;C=-1+0j;Z=2+0j;CL={X,U,Q,A};vec=[1j,1,-1j,-1];xy=lambda q:[int(q.real),int(q.imag)];level=lambda q:int(3*q.imag-q.real+11)
# Independent deterministic tail when no cluster read occurs in the C excursion.
tail=[(C,2,'L'),(B,1,'L'),(U,0,'R'),(Q,1,'R'),(A,2,'L'),(Z,1,'L'),(X,0,'L')]
assert [[xy(p),h,c]for p,h,c in tail]==J['forced_tail_if_cluster_avoided']
for (p,h,c),(q,k,d)in zip(tail,tail[1:]):nh=(h+(1 if c=='R'else-1))%4;assert nh==k and p+vec[nh]==q
assert [i for i,v in enumerate(hist['9'])if v==1]==[3]
# First-contact geometry, preserving each cell's invariant incoming axis.
assert Q-vec[1]==U and Q-vec[3]==X and A-vec[2]==Q and U-vec[0]==B and B-vec[1]==C
assert X-vec[2]==2+2j and U-vec[2]==2j and(level(2j),level(2+2j))==(17,15)
controls=[]
for f in J['positive_finite_controls']:
 black={complex(*q)for q in f['initial_black']};p=complex(*f['initial_position']);h=f['initial_heading'];assert(p,h)==(X,2);ev=[]
 for t,c in enumerate(f['word']):
  assert(c=='L')==(p in black);ev.append(dict(time=t,position=xy(p),incoming_heading=h,turn=c));black.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=vec[h]
 assert ev==f['events']and sorted(map(xy,black))==f['complete_final_black']and(xy(p),h)==(f['final_position'],f['final_heading']);assert ev[6]['position']==xy(C)
 assert all(complex(*z['position'])not in CL|{C} and level(complex(*z['position']))>=13 for z in ev[7:-1]);assert ev[-1]['position']==f['contact_position']and ev[-1]['incoming_heading']==2
 target=complex(*f['contact_position']);assert target in(U,X)and ev[-1]['turn']==('R'if target==U else'L');assert len(ev)==(17 if target==U else 21)
 black={complex(*q)for q in f['initial_black']};p=X;h=2;reads=[];ct=[]
 for t in range(200):
  c='L'if p in black else'R';reads.append((t,p,h,c))
  if p==C:ct.append((t,h,c))
  if len(ct)==2:break
  black.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=vec[h]
 if target==U:assert ct[-1]==(142,0,'L');failure=dict(time=142,cell=xy(C),actual_incoming='N',required_next_incoming='S',owned_rank=9)
 else:assert [e for e in reads if e[1]==X][3]==(32,X,2,'L');failure=dict(time=32,cell=xy(X),actual_incoming='S',required_next_incoming='N',owned_rank=3)
 row=next(z for z in J['specific_seed_continuation_diagnostics']if z['contact_branch']==xy(target));assert row['next_C_return']==list(ct[-1])and row['specific_supplied_history_failure']==failure
 controls.append(dict(word=f['word'],initial_black=f['initial_black'],complete_final_black=f['complete_final_black'],first_cluster_read=ev[-1],specific_seed_failure=failure))
out=dict(status='PASS all-length two-port cluster reimport conditional on supplied OPEN79 gap3 history',proof=sha(D/'OPEN79_ALL_LENGTH_TWO_PORT_REIMPORT.md'),certificate=sha(D/'open79_cluster_reimport_certificate.json'),script=sha(S),controls=controls,analytic_review=['Complete named T9/T10/T11/T12 histories are independently bound. B next E arrival necessarily comes from C, so B cannot be read during the open first C excursion. Assuming noK contact fixes U/Q WHITE and A/X BLACK; after C L the literal forced tail C,B,U,Q,A,Z,X reaches X fromN instead of owned rank1S. An earlier Z E/L use only makes the contradiction earlier; no unknown Z turn is allowed.','At firstK contact, Q horizontal arrivals both require earlierU orX; A ownedS requires earlierQ. U invariant vertical axis leavesN fromforbiddenB orS fromnorth. X owned nextS comesfromnorth. Actual colors giveU R restoration versusX L consumption. This is actual first physical contact, not canonical clock/phase ordering.','Both prepared17/21 branches replay on complete6/8-black finite inputs with full final fields. They stop at firstreimport, not a completedC return or OPEN79/controller. Their exact-seed later heading failures do not exclude arbitrary exterior completions. No finite length bound, stock monotonicity or recursive debt amplification is inferred.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
