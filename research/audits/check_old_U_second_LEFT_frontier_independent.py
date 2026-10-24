from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import hashlib,json,math
S=Path(__file__).resolve();R=S.parents[1];D=R/'second_ordinary_after_first_foreign_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();man=D/'old_U_second_contact_LEFT_frontier_manifest.json';assert sha(man)=='474b53816c006efac6230d5e5e77f6ffda65ac384df7dedc483d8d6f4be0677f';mf=json.loads(man.read_text())
for p,h in mf['files'].items():assert sha(D/p)==h
for p,h in mf['dependencies'].items():assert sha(R/p)==h
ref=json.loads((D/'old_U_second_contact_LEFT_frontier.json').read_text())
ns={'__file__':str(S.with_name('check_second_ordinary_small_interface_independent.py'))};exec(Path(ns['__file__']).read_text().split('triples=[]')[0],ns);W,M,walk,center,xy,meet,cross,minus,pose,chord,pieces=[ns[k]for k in['W','M','walk','center','xy','meet','cross','minus','pose','chord','pieces']]
LEFT={0j,1j};STAR=LEFT|{1+0j,1+1j};K={-1-1j,-1,-1j,0j,1};old=chord('U');u=minus(old[1],old[0]);rows=[];startbad=[];boundsrows=[];gc=Counter()
for b in'DVU':
 full=walk(W[b]+M);first={}
 for t,(q,h,c)in enumerate(full['reads']):first.setdefault(q,(t,c))
 for N in range(1,4 if b=='U' else 5):
  h=(2-N)%4;r=(-1j)**h;seg=chord(b,0j,h);v=minus(seg[1],seg[0]);den=cross(u,v)
  cor=[tuple(F(old[0][k]+s*u[k]-seg[0][k]-t*v[k],2)for k in(0,1))for s in(0,1)for t in(0,1)];box=[(math.floor(min(z[k]for z in cor)),math.ceil(max(z[k]for z in cor)))for k in(0,1)];boundsrows.append((b,N,cor,box))
  for x in range(box[0][0],box[0][1]+1):
   for y in range(box[1][0],box[1][1]+1):
    if(x+y-N)%2:continue
    p=complex(x,y);ss=chord(b,p,h)
    if den:
     hit=meet(*old,*ss)
     if hit is None or not(0<=hit[0]<1 and 0<hit[1]<=1):continue
     s,t=hit[:2]
    else:
     assert b=='U'and N==2 and v==u
     z=minus(ss[0],old[0])
     if cross(z,u):continue
     s0=F(z[1],u[1]);assert x==0
     if 0<=s0<1:startbad.append((x,y,h));continue
     s=F(0);t=-s0
     if not(0<t<=1):continue
    if any((q-p)/r in K or first.get((q-p)/r,(None,None))[1]=='R'for q in LEFT):reason='LEFT_current_core_or_WHITE'
    elif any(first.get((q-p)/r,(None,None))[1]=='R'for q in STAR-LEFT):reason='other_original_physically_BLACK_but_before_WHITE'
    else:reason='LEFT_and_all_original_BLACK_compatible'
    row=dict(second=b,effective_N=N,second_pose=[x,y,h],classification=reason,source_s=[s.numerator,s.denominator],second_t=[t.numerator,t.denominator]);rows.append(row);gc[reason]+=1
    rr=next(z for z in ref['exact42_outgoing_owned_contact_poses']if z['second']==b and z['effective_N']==N and z['second_pose']==[x,y,h]);assert all(rr[k]==v for k,v in row.items())
    for st in rr['all_original_ID_before_locations']:
     q=complex(*st['original_U_cell']);l=(q-p)/r;assert xy(l)==tuple(st['second_local_cell'])and st['lies_in_actual_entry_K']==(l in K)
     f=first.get(l);o=st['first_read'];assert(o is None)==(f is None)
     if f:
      tick,c=f;assert o['context_tick0']==tick and o['turn']==c
      if tick>=len(W[b]):assert o['next_word_tick0']==tick-len(W[b])and o['next_word_read_number1']==tick-len(W[b])+1
assert len(rows)==42 and len(boundsrows)==11 and sorted(startbad)==[(0,0,0),(0,2,0)]and gc==ref['geometry_classification_counts']
assert Counter(z['second']for z in rows)=={'D':8,'V':16,'U':18}
other=[z for z in rows if z['classification']=='other_original_physically_BLACK_but_before_WHITE'];assert[(z['second'],z['second_pose'])for z in other]==[('U',[-2,-1,1]),('U',[0,-2,0]),('U',[2,1,3])]
compatible=[z for z in rows if z['classification']=='LEFT_and_all_original_BLACK_compatible'];seven=[z for z in compatible if z['second_pose'][2]!=1];assert len(seven)==7
east=[z for z in compatible if z['second_pose'][2]==1];assert[(z['second'],z['second_pose'])for z in east]==[('D',[-1,0,1]),('V',[-3,0,1]),('U',[-4,-1,1])]
yheads=[]
for A in'FQB':
 for b1 in'DVU':
  z=walk(W[A]+W[b1]);assert z['feasible'];p2=-4-1j;ap=p2-z['p']*(-1j)**3;assert ap.imag<=4;yheads.append([A,b1,*xy(ap),3])
assert[(xy(walk(W[b])['p']),walk(W[b])['h'])for b in'DVU']==[((1,1),0),((1,3),0),((0,4),0)]
cu=walk(W['C']+W['U']+M);assert not cu['feasible']and(cu['i'],cu['first'])==(29,1)
# Derive typed labels directly from N and b1, then invert actual A+b1 endpoints.
typed=[];counts=Counter()
for g in seven:
 b2,N=g['second'],g['effective_N'];p2=complex(*g['second_pose'][:2]);h2=g['second_pose'][2]
 for b1 in'DCVU':
  n=N-(b1=='C');ha=(-n)%4;rot=(-1j)**ha
  for A in'FQB':
   pre=walk(W[A]+W[b1]);assert pre['feasible']and(ha+pre['h'])%4==h2;ap=p2-rot*pre['p'];full=walk(W[A]+W[b1]+W[b2]+M);ac=walk(W[A]+M);hits=[q for q in STAR if(q-ap)/rot in ac['req']];pc,aend,_=pieces(A,ap,ha);prior=any(meet(*old,*seg)is not None for seg in pc+[chord(b1,*aend)])
   if not full['feasible']:why='immutable_local_RAW_context_conflict'
   elif hits:why='FOREIGN_complete_context_hits_original_star_below_age5'
   elif prior:why='already_signed_simple_prior_proxy_contacts_old_U'
   else:why='necessary_only_unresolved'
   row=dict(second=b2,effective_N=N,true_preforeign_age=n,foreign=A,foreign_pose=[*xy(ap),ha],first=b1,second_pose=g['second_pose'],classification=why);typed.append(row);counts[why]+=1
   rr=next(z for z in ref['all84_foreign_first_second_typed_alignments']if all(z[k]==row[k]for k in('second','effective_N','foreign','first','second_pose')));assert all(rr[k]==v for k,v in row.items())
assert len(typed)==84 and counts==ref['disjoint_typed_classification_counts'];remain=[z for z in typed if z['classification']=='necessary_only_unresolved'];assert len(remain)==60
assert Counter(z['true_preforeign_age']for z in remain)=={3:42,4:18};assert Counter(z['second']for z in remain)=={'D':9,'V':27,'U':24}
assert any(z['foreign_pose']==[4,-3,1]and z['foreign']=='F'and z['first']=='D'and z['second']=='U'and z['second_pose']==[1,2,3]for z in remain)
out={'status':'PASS exact necessary old-U second D/V/U LEFT frontier; not attainment or second simplicity','manifest':sha(man),'geometry_counts':dict(gc),'poses':rows,'CUT2_already_old_starts':startbad,'east_U_inverse_heads':yheads,'typed_counts':dict(counts),'remaining':remain,'analytic_review':[
'Signed angles give true n<=4 and effective N=n+C(b1), with actual U-family source full entry equal to its U-base entry and real C tails included. Preforeign star-effect>=5 implies complete-context MISS; exact signed CUT2 transfer then gives LEFT same-ID CURRENT and ALLfour physicallyaliveBLACK. The right column may be CORE and is not declared CURRENT.',
'Exact closed head parallelograms and active parity exhaust eleven boxes,42 outgoing-old/positive-new contact poses. The sole parallel case is same-direction U,N2. Starts y0/y2 already lie on old source before the second read and are excluded by signed OPEN simplicity. y4 starts at oldEND and moves away. y-4/y-2 are retained first positive onsets at oldSTART, new1/1/2. No zero determinant silently removes a candidate.',
'Actual second RAW+nextM masks cut29 by heldLEFT core/WHITE and three additional U poses only by physical BLACK right-column firstR. At rightCORE firstL no false exclusion is made. Ten compatible poses remain. East D/V use signed endpoint law; east U inverse nineforeignheads all y<=4, whereas arbitrary one-C N/W history from genuineU has y>=5. b1C is the separate actualCU conflict, not assigned the true-one-C equation.',
'Seven poses expand to84 actual A/b1/b2 contexts with true n. Nine local literal conflicts,15 prohibited foreignstarhits,60 necessary residues match exactly; any prior oldU contact is already in a cut class. Remaining ages3/4 only. Foreign Q/B pieces use true F56 cut without a fictitious internalK.',
'All marker owners were regenerated from RAW length and absolute zero-based tick. D context11 and V19 are next-wordtick1/read2, not a physical deletion during the secondRAW. The F(4,-3,E),D,U(1,2,W) prepared target remains necessary with rightCORE, not a genuine U-ancestry witness. No postforeign maturation, third-atom iteration, secondsimplicity or decreasingresource follows.'
]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(gc,counts)
