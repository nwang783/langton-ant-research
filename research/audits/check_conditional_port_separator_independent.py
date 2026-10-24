from pathlib import Path
import json,hashlib,collections
R=Path('/workspace/shared/langton');P=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();m=P/'CONDITIONAL_PORT_SEPARATOR_MANIFEST.json';assert sha(m)=='ecccb2270c835df0fa330d8819eecea68716dfb3a76f444e3e0a86573476c090';mf=json.loads(m.read_text())
for f,h in mf['files'].items():assert sha(P/f)==h
for f,h in mf['independent_dependencies'].items():assert sha(R/'audits'/f)==h
base=R/'audits/check_minimal_cohort_restart_independent.py';ns={'__file__':str(base)};exec(base.read_text().split('report=')[0],ns)
seed,states,poses,head,reads,cp,xy,v=[ns[k]for k in['seed','states','poses','head','reads','cp','xy','v']]
J=json.loads((P/'CONDITIONAL_PORT_SEPARATOR_CHECKED.json').read_text());B=set(states[262]);p=poses[262];h=head[262];n=lambda q:int(q.real-q.imag);assert(p,h,len(B))==(-1-1j,1,46)and sorted(map(xy,B))==J['white_branch_full_terminal_black']
word=J['white_branch_terminal_word'];assert len(word)==104;Q=[];pp=p;hh=h
for ch in word:Q.append(pp);hh=(hh+(1 if ch=='R'else-1))%4;pp+=v[hh]
assert pp-p==2-2j and hh==h and min(map(n,Q))==0
multiple=ns['multiple'];tests=0
for i,q in enumerate(Q):
 hits=[k for z in B if(k:=multiple(z-q))is not None and k>=0];th=[k for j,z in enumerate(Q)if(k:=multiple(z-q))is not None and(k>0 or k==0 and j<i)];cuts=sorted({0,*hits,*[k+1 for k in hits],*th});row=J['white_branch_terminal_ray_parity'][i]
 assert sorted(hits)==sorted(row['initial_hits'])and sorted(th)==sorted(row['prior_thresholds'])and cuts==row['tests']and row['point']==xy(q)
 for k in cuts:assert(sum(a==k for a in hits)+sum(a<=k for a in th))%2==(word[i]=='L');tests+=1
assert tests==171 and ''.join(reads[:262])==J['white_branch_prefix'];first={}
for t in range(262):first.setdefault(poses[t],t)
E={q for q in first if n(q)<0};assert sorted(map(xy,E))==J['old_side_exposure_white_branch']and max(t for t in range(262)if n(poses[t])<0)==261
white=set(map(cp,J['common_required_white']));hole=cp(J['released_bit']);assert hole==-3-2j and seed==set(map(cp,J['common_required_black']))and white=={-3+1j,-3+2j,-2+0j,-1+0j}
G=seed|{hole}|white;ports=E-G;assert len(G)==19 and len(E)==38 and len(ports)==19 and sorted(map(xy,ports))==J['conditional_required_white']and not ports&seed
assert sorted([first[q],xy(q)]for q in ports)==J['port_first_reads']and sorted(first[q]for q in ports)==[72,73,169,174,175,176,184,185,186,189,190,191,212,225,226,227,235,236,237]
# Independently replay every perturbed fullboard up to exact discrepancy.
def replay(B,T):
 B=set(B);p=0j;h=1;rr=[]
 for t in range(T):
  ch='L'if p in B else'R';rr.append((p,h,ch));B.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=v[h]
 return B,p,h,rr
for row in J['port_single_flip_controls']:
 q=cp(row['port']);t=first[q];BB,pp,hh,rr=replay(seed|{q},t+1);assert sorted(map(xy,seed|{q}))==row['initial_black']and t==row['first_disagreement']
 assert all((p,h,ch)==(poses[i],head[i],reads[i])for i,(p,h,ch)in enumerate(rr[:t]));assert rr[t][0]==q and rr[t][2]=='L'and reads[t]=='R'
# Blackbranch entire old-side exposure, from separately signed all-future baseline.
K=json.loads((P/'PAIRED_WAKE_RETURN_CREDIT_CHECKED.json').read_text());baseword=K['baseline_word'];pp=0j;hh=1;old=set();last=-1
for i,ch in enumerate(baseword):
 nn=n(pp)
 for k in range(max(0,(-nn+3)//4)):
  q=pp+k*(2-2j);assert n(q)<0;old.add(q);last=max(last,104*k+i)
 hh=(hh+(1 if ch=='R'else-1))%4;pp+=v[hh]
assert old==G and last==161==J['black_branch_last_old_side_read']and sorted(map(xy,old))==J['black_branch_old_side_exposure']and not old&ports
archive={-1000000-999999j,999999999+1000000000j,-1000000000+5j,-7+0j};assert all(n(q)<0 for q in archive)and not archive&E
for row in J['huge_archive_controls']:
 S=seed|({hole}if row['hole_black']else set());BB,pp,hh,rr=replay(S|archive,262);b,p0,h0,ref=replay(S,262);assert rr==ref and BB==b|archive and pp==p0 and hh==h0
 assert sorted(map(xy,S|archive))==row['initial_black']and sorted(map(xy,BB))==row['full_final_black']and [xy(pp),hh]==row['final_pose']
# Preparation works for arbitrary admitted board, because both changedcells are fixed bycommon guard.
for S in[seed,seed|{hole},seed|archive,seed|{hole}|archive]:
 B0=(S-{-1+1j})|{-1+0j};q=-1+1j;h=1;prior=[]
 for ch in'RL':
  prior.append(q);assert(q in B0)==(ch=='L');B0.symmetric_difference_update({q});h=(h+(1 if ch=='R'else-1))%4;q+=v[h]
 assert B0==S and(q,h)==(0,1)and list(map(n,prior))==[-2,-1]and all(n(z)<0 for z in S)
report={'status':'PASS strictly broader conditional finite no-reentry capture class, not universal guard occurrence','manifest_sha256':sha(m),'script_sha256':sha(Path(__file__)),'whitebranch_prefix_length':262,'whitebranch_terminal_complete_mass':46,'whitebranch_infinite_parity_tests':tests,'black_white_oldside_exposure_sizes':[19,38],'black_white_last_oldside_reads':[161,261],'conditional_white_ports':19,'analytic_checks':['Actualpose0,E and ENTIRE CURRENT x-y>=0WHITE required. Common18bits AND(hBLACK OR19portsWHITE); blackbranch addsNOnewportconditions. Strictweakeningwitness isliteral14blackdefect.','Whitebranch complete262prefix/46blackstate andall171infinitephase-rayparitytests verified; everyfuturephaseprojection>=0 anddriftprojection4. Alloldsideexposureexact38 finitecells.','Arbitraryfiniteoldarchiveoutsidethe actualbranch exposure ispreserved byfirst-differenceinduction. No componentseparation, connectedwall orfinitehorizon assumption. Allfuturefreshsidereads agreefrominitialWHITEnessandthe sameactual toggles.','All19singleport flips causeexactfirstR-toL disagreementandhugearchiveregressions retaincompletefields. These ports are necessaryforTHISword,notnecessaryfor eventualcapturevia anotherroute.','Two-readRLpreparationusesfixedcommonblack(-1,1)andwhite(-1,0), restoringfulladmittedboard andstrictrecordagainstearlierheadprojections.','Tangentialtailcountercontrol isnotexcludedbyfreshness;its infiniteoldsideexposureviolates this finitecut mechanism. No universalrecordcover inferred.'],'not_claimed':['unconditional18-bitguard','everyseedhitsguard','globalcapture','connectedphysicalwall','permanentwakecreditbeforecertifiedcut']}
p=R/'audits/conditional_port_separator_independent.json';p.write_text(json.dumps(report,indent=2)+'\n');print(sha(p));print(report['status'])
