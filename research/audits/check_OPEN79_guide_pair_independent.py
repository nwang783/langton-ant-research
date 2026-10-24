from pathlib import Path
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'OPEN79_MANDATORY_GUIDE_PAIR_AND_UNIT_RETURN.md';assert sha(P)=='5f8af474fe7af30a6791b20bb9521ade93a27b76cae4ba6f004db76a14a7a76d';assert sha(D/'certify_open79_mandatory_guide_pair.py')=='0cb6d380243ebfa88e141cbd827c615f8377cdf9e791721ff4b31c71d3b5d329';assert sha(D/'open79_mandatory_guide_pair_certificate.json')=='0dcf5941010e24ac896a9adb730b31ba231df078a72bce2c35fcde1d137e816c'
J=json.loads((D/'open79_mandatory_guide_pair_certificate.json').read_text())
for f,h in J['dependency_hashes'].items():assert sha(D/f)==h
ns={'__file__':str(S.with_name('check_physical_return_debt_independent.py'))};exec(Path(ns['__file__']).read_text().split('out=dict(')[0],ns);chains,H,outs=ns['chains'],ns['H'],ns['outs'];vec=[1j,1,-1j,-1];letters='NESW';xy=lambda q:[int(q.real),int(q.imag)];X=2+1j;Q=1+1j;A=1+0j;B=0j;U=1j;V=-1+1j;C=-1+0j;Z=2+0j
ch=next(ch for ch in chains if ch[0]==((12,11),0));assert len(ch)==35;path=[]
for offset,((i,r),k)in enumerate(ch):
 p=11-i+k*(3+1j);row=dict(offset=offset,position=xy(p),**{'class':i},rank=r,lift=k,incoming=letters[H[i][r]],turn='RL'[r%2]);path.append(row)
assert path==J['locked_named_chain']
for offset,p,r in [(0,C,11),(25,Z,0),(26,X,2),(29,Z,1),(33,Z,2),(34,X,3)]:assert path[offset]['position']==xy(p)and path[offset]['rank']==r
for a,b in zip(path,path[1:]):
 h=(letters.index(a['incoming'])+(1 if a['turn']=='R'else-1))%4;assert complex(*b['position'])==complex(*a['position'])+vec[h]and b['incoming']==letters[h]
assert [r for r in range(3)if outs[12,r]==3]==[0];assert H[12][1]==2 and outs[12,1]==1
assert H[10][3]==2 and outs[10,3]==1 and [r for r,h in enumerate(H[9])if h==1]==[3]
assert H[11][9]==1 and B-vec[1]==C
noU=[(C,2,'L'),(B,1,'L'),(U,0,'R'),(Q,1,'R'),(A,2,'L'),(Z,1,'L')];assert [[xy(p),h,c]for p,h,c in noU]==J['no_U_forced_tail']
for(p,h,c),(q,k,ch0)in zip(noU,noU[1:]):hh=(h+(1 if c=='R'else-1))%4;assert q==p+vec[hh]and hh==k
assert 8+25+12-5==J['explicit_no_U_clock_contradiction']['positive_cycle_constant']==40
controls=[]
for name in ['genuine_finite_pair_restoration_control','standalone_higher_return_control','genuine_finite_four_black_consumption_square']:
 r=J[name];black={complex(*q)for q in r['initial_black']};p=complex(*r['initial_position']);h=r['initial_heading'];ev=[]
 for t,c in enumerate(r['word']):
  assert(c=='L')==(p in black);ev.append(dict(time=t,position=xy(p),incoming_heading=h,turn=c));black.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=vec[h]
 assert ev==r['events']and sorted(map(xy,black))==r['final_black']and(xy(p),h)==(r['final_position'],r['final_heading']);controls.append(dict(name=name,reads=len(ev),initial_mass=len(r['initial_black']),final_mass=len(black)))
 if name.startswith('genuine_finite_pair'):assert[(e['position'],e['incoming_heading'],e['turn'])for e in ev[-2:]]==[(xy(U),2,'R'),(xy(V),3,'R')]
 elif name.startswith('standalone_higher'):
  assert [(e['time'],e['incoming_heading'],e['turn'])for e in ev if e['position']==xy(V)]==[(0,3,'R'),(4,1,'L'),(20,1,'R')];assert all(e['position']!=xy(U)and 3*e['position'][1]-e['position'][0]+11>=13 for e in ev);assert(p,h)==(C,2)
 else:assert [e['position']for e in ev]==list(map(xy,[C,B,U,V,C]))and black=={C}
# Independent literal obstruction to concatenating the two supplied prepared factors.
w=J['genuine_finite_pair_restoration_control']['word'][:-1]+J['standalone_higher_return_control']['word'];p=X;h=2;last={};conflict=None
for t,c in enumerate(w):
 if p in last and last[p][1]==c:conflict=dict(position=xy(p),earlier=list(last[p]),later=[t,c]);break
 last[p]=(t,c);h=(h+(1 if c=='R'else-1))%4;p+=vec[h]
assert conflict==J['standalone_control_non_gluing_witness']
out=dict(status='PASS conditional all-length unique U restoration, three V reads and exact C9->C10 square',proof=sha(P),script=sha(S),certificate=sha(D/'open79_mandatory_guide_pair_certificate.json'),independent_locked_chain=path,positive_no_U_cycle=40,full_controls=controls,non_gluing=conflict,analytic_review=['The independent79-event graph reconstruction gives the physical35-read chain C11->Z0 at+25,X2+26,Z1+29,Z2+33,X3+34 with every full lift. Since C11>C9, Z has no earlier physicalread and X rank2/3 are later. X only available W departure is alreadyusedrank0, while A nextS/L departs to locked Z E/L rank3 and is also later. No ordinal phase reduction or exterior multiplicity cap is used.','Inside the open C8->C9 excursion, B nextE requires the precedingC read, impossible before its endpoint. If U untouched then neither X norU can reachQ; A is untouched. The forced post-C9 tail reachesZ3 atC9+5, whereas Z3>=C11+25+12>=C9+45, yielding positive40. Thus U must firstarriveS/R fromnorth, restoring its previouslyL-erased cell.','Before a secondU, Q remains untouched: firstU S/R departsW toV, X has no availableW, and B remains inaccessible. SecondU S/L would forceQ E/R then lockedA S/L andZ E/L before Creturn. Thus U is read exactlyonce. This is a chronological first-second-read argument, not finite excursion enumeration.','Before Urestoration, any V reimport fromwest E/R would immediately reachC and end theexcursion without mandatoryU. Therefore U reaches untouchedV W/R. LaterW arrivals require anotherU, forbidden; nexttwo V arrivals mustE/L thenE/R, the latter giving C9. These are consecutive reads OF V, not necessarily consecutive globalupdates. Their two higher excursions are unbounded.','C9,B9,U,V are allBLACK with their exact prefix/restoration identities, so fouractualL moves returntoC10R in4steps. Full18/21/5 prepared controls are separately literal and do not glue; retained repeated-turn conflict proves that specific attemptedcompositionfails. No controllercompletion, repeatedstock sign, ageupperbound or growth exclusion follows.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
