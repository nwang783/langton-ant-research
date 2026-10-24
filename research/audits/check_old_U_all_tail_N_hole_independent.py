from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib,math
S=Path(__file__);R=S.parents[1];D=R/'old_U_all_tail_N_hole_guard_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'manifest.json';assert sha(mf)=='2df21fefa60d24fcdeec3f1389b6bfb79810245097a652e9f9bd252be9c62719';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'N_hole.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,center,xy,meet,cross=[ns[k]for k in('W','M','K','tr','rot','center','xy','meet','cross')];G={a:tr(W[a])for a in W};left={0j,1j};g=-1+0j;target=-2j
angles=json.loads((R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json').read_text())['all44_exact_source_target_C_window_rows']
for a in'DCVU':
 ar=next(z for z in angles if z['source_class']=='preFOREIGN_ordinary'and z['source_atom']=='U'and z['contact_atom']==a);assert[k for k in ar['allowed_C_counts_before_contact_ENTRY']if(2-k)%4==0]==[2]
source=(center(0j,0),center(G['U']['p'],0));geom=[];keep=[]
for a in'DCVU':
 z=tr(W[a]+M);start=center(0j,0);end=center(G[a]['p'],G[a]['h']);corners=[(s-t)/2 for s in source for t in(start,end)]
 for x in range(math.floor(min(p.real for p in corners)),math.ceil(max(p.real for p in corners))+1):
  for y in range(math.floor(min(p.imag for p in corners)),math.ceil(max(p.imag for p in corners))+1):
   if(x+y)%2:continue
   p=complex(x,y);c=start+2*p;d=end+2*p;u=source[1]-source[0];v=d-c
   if cross(u,v):hit=meet(*source,c,d)
   else:
    if cross(c-source[0],u):continue
    q=source[0]-c;den=v.real if v.real else v.imag;t=F(int(q.real if v.real else q.imag),int(den));hit=(F(0),t)if q==t*v else None
   if hit is None or not(0<=hit[0]<1 and 0<hit[1]<=1):continue
   bad={q for q in left if q-p in K or z['req'].get(q-p)is False};au=next(r for r in J['all8_exact_outgoing_owned_N_geometries']if r['actor']==a and r['ENTRY']==[x,y,0]);assert{tuple(xy(q))for q in bad}=={tuple(r['SAME_LEFT'])for r in au['SAME_LEFT_contradictions']};assert[str(hit[0]),str(hit[1])]==[au['old_U_first_contact_parameter'],au['new_positive_first_contact_parameter']];geom.append((a,x,y,str(hit[0]),str(hit[1]),len(bad)))
   if not bad:keep.append((a,p))
assert len(geom)==8 and keep==[('U',target)]and G['U']['last'][g]==('L',1);assert G['U']['reads'][13][0]==g-target and G['U']['reads'][13][2]=='L'
RR={}
for a,z in G.items():
 ec={z['p']+rot(z['h'])*q for q in K};rr=[]
 for q,(c,t)in z['last'].items():
  if c!='R':continue
  first=next((cc,i)for i,(qq,hh,cc)in enumerate(z['reads'])if qq==q);row=dict(slot=xy(q),last_R_tick0=t,last_R_read1=t+1,first_physical_read=list(first),actual_RAW_EXIT_CORE=q in ec);rr.append(row)
 assert rr==J['all_physical_RAW_final_R_slots_including_CORE'][a];RR[a]=rr
counts=Counter();surv={h:[]for h in range(4)};marker_inputs=0
for h in range(4):
 for a in'DCVU':
  z=G[a];ctx=tr(W[a]+M)
  for rr in RR[a]:
   q=complex(*rr['slot']);p=g-rot(h)*q;ep=p+rot(h)*z['p'];eh=(h+z['h'])%4;au=next(r for r in J['all144_earlier_ordinary_first_BLACK_cut_writer_roles']if r['hypothetical_STRICTLY_EARLIER_writer_RAW']==a and r['writer_ENTRY']==[*xy(p),h]and r['physical_final_R']==rr);assert au['writer_RAW_EXIT']==[*xy(ep),eh]
   if(int(p.real+p.imag)+h)%2:why='wrong_actual_marked_sector'
   elif rr['first_physical_read'][0]=='L':why='first_hole_read_L_requires_BLACK_at_an_earlier_actual_RAW_cut'
   else:
    touched=[]
    for tag in sorted(left,key=lambda q:(q.real,q.imag)):
     local=(tag-p)/rot(h);fr=next(([c,i]for i,(qq,hh,c)in enumerate(ctx['reads'])if qq==local),None)
     if local not in K and fr is None:continue
     if local in K:how='CURRENT_anchor_cannot_be_in_writer_ENTRY_CORE'
     elif fr[0]=='R':how='SAME_BLACK_anchor_conflicts_with_first_WHITE'
     else:
      how='TRUE_anchor_input_would_lose_CURRENT_by_writer_RAW_EXIT_including_marker_CORE_capture'
      if fr[1]>=len(W[a]):assert local in{z['p']+rot(z['h'])*k for k in K};marker_inputs+=1
     touched.append((xy(tag),xy(local),fr,how))
    if touched:
     assert touched==[(r['SAME_LEFT_anchor'],r['local'],r['actual_first'],r['exact_contradiction'])for r in au['independently_CURRENT_before_and_after_earlier_writer_LEFT_contacts']];why='earlier_writer_touches_independently_CURRENT_SAME_LEFT'
    else:why='necessary_earliest_BLACK_cut_origin_after_sector_and_LEFT_and_priorBLACK_filters';surv[h].append((a,p,ep,eh,rr['last_R_tick0'],rr['actual_RAW_EXIT_CORE']))
   assert why==au['route'];counts[why]+=1
assert sum(counts.values())==144 and {str(h):len(v)for h,v in surv.items()}==J['exact_surviving_first_BLACK_origin_counts']=={'0':5,'1':3,'2':0,'3':4}
assert{(a,p)for a,p,*_ in surv[3]}=={(a,-1-2j)for a in'DCVU'}and all(p.imag<4 for a,p,*_ in surv[0])
assert{(a,p)for a,p,*_ in surv[1]}=={('D',-2+1j),('V',-4+1j),('U',-5+0j)}and all(ep==-1 and eh==1 for a,p,ep,eh,*_ in surv[1])
for a,p,ep,eh,*_ in surv[0]:assert(a=='C'and eh==3)or(a!='C'and eh==0 and ep.imag>=2)
fore=[]
for a in'FQB':
 ep=G[a]['p'];assert G[a]['h']==2
 for rr in RR[a]:
  q=complex(*rr['slot']);X=int((g-q).real);Y=int((g-q).imag)-4;models=[]
  for v in range(max(X+1,0)):
   d=X-v;u=(Y-d-3*v)//4
   if u>=0 and d+3*v+4*u==Y:models.append((d,v,u))
  assert not models
  post=g+q-ep;assert post.imag>=0>target.imag
  au=next(z for z in J['all73_n0_FOREIGN_physical_CORE_inclusive_R_origin_queries']if z['FOREIGN']==a and z['physical_final_R']==rr);assert au['exact_N_zero_run_X']==X and au['exact_N_zero_run_Y']==Y and not au['all_nonnegative_N_count_models']
  au=next(z for z in J['all73_n2_FOREIGN_physical_CORE_inclusive_R_endpoint_cuts']if z['FOREIGN']==a and z['physical_final_R']==rr);assert au['actual_S_FOREIGN_ENTRY']==xy(g+q)and au['actual_N_FOREIGN_RAW_EXIT']==[*xy(post),0]
  fore.append((a,rr['slot'],rr['last_R_tick0'],rr['actual_RAW_EXIT_CORE'],X,Y,xy(post)))
 assert min(q['slot'][0]for q in RR[a])>=-5
assert len(fore)==73 and tr(W['C']+W['U'])['bad']
# All source own-C cuts preserve the four SAME star identities outside actual K.
star={0j,1j,1+0j,1+1j}
for seq in['U','UC','UCC']:
 z=tr(''.join(W[a]for a in seq));assert all(z['last'][q]==G['U']['last'][q]for q in star)and not star&{z['p']+rot(z['h'])*k for k in K}
O=dict(status='PASS old-U arbitrary ordinary-tail N-facing GLOBAL-first-contact exclusion, total-C2 only',manifest=sha(mf),script=sha(S),all8_geometry=geom,ordinary_counts=counts,marker_true_inputs_independently_verified_in_exit_CORE=marker_inputs,surviving_ordinary_origins={h:[[a,xy(p),xy(ep),eh,t,core]for a,p,ep,eh,t,core in v]for h,v in surv.items()},all73_foreign_origins=fore,analytic_review=[
'Signed exact angle plus heading gives TOTAL K2, true preFOREIGN n0/1/2. The complete first-FOREIGN star-MISS effect and GLOBAL-first stopping supply SAME LEFT CURRENT at candidateENTRY and every strictly earlier ordinary cut, never through the contact actor. Actual source UC/UCC tails preserve the same stars, including their intermediate C cut.',
'Earliest RAW-exit BLACK restoration is chosen after actual sourceU erased g by L1; CORE BLACK counts. An unread writer or first-L writer would already require BLACK at its previous actual cut. Every possible writer therefore has a physical finalR and firstR at g. The earlier-ordinary anchor filter uses independent before/after CURRENT: firstR conflicts, ownL loses original identity, marker firstL means actual exitCORE capture. These marker cases were independently checked against K, not called immediate color contradictions.',
'The full144 physical/CORE origin cover leaves N5/W4/E3/S0. PreFORE N heads y>=4 and W y>=5 exclude all surviving preFORE ordinary writers. Source ownC tails are actual RAWs, not invented completed packets. S supplies no earliest restoration.',
'All73 FOREIGN finalR origins retained. n0 exact nonnegative N displacement equations have no model. n1 UC startsW y5 and actual nonempty W beginsD/V, henceFOREheady>=6; plainU requires later producer-ownC and hasFOREheady>=7. LocalR x>=-5 forbids writingg y0. n2 S-oriented FOREIGN rewritingg would exitN y>=0 and cannot reach targety-2 by zeroC N motion. No postFORE age law used.',
'PostFORE phases are S/E/N only. E survivors exit(-1,0,E); the sole E-toN C addsx1, so reachingtargetx0 forces no Ebase and only zero-x NU afterward, leaving y>=0. N C would exceed targetclock; Nbase survivors exity>=2. This excludes every earlier funding origin at arbitrary tail length.',
'Conclusion closes exactly eight old outgoing-U-owned N headings at GLOBAL first contact after FIRST foreign, with TOTAL ordinaryC2. No intermediate fine-time WHITE permanence, through-contact LEFT guard, other old source/heading, secondFOREIGN or full-tail simplicity is inferred.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(counts);print(sha(S.with_suffix('.json')))
