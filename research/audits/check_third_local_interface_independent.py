from pathlib import Path
from fractions import Fraction
import json,hashlib,itertools,collections
R=Path('/workspace/shared/langton');P=R/'third_ordinary_local_interface_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=P/'manifest.json';assert sha(mf)=='84c0fe1e65ccb75304f8ba4003e8f56b5b45d78a01eb22507235515a6155c0ad';MNF=json.loads(mf.read_text())
for f,h in MNF['files'].items():assert sha(P/f)==h
for f,h in MNF['dependencies'].items():assert sha(R/f)==h
p=R/'audits/check_old_V_second_age1_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('# Universal')[0],ns)
W,M,tr,pieces,meet,xy=[ns[k]for k in ['W','M','tr','pieces','meet','xy']];J=json.loads((P/'third_local_interface.json').read_text());contacts=[]
for a in'FQB':
 for ts in itertools.product('DCVU',repeat=3):
  tokens=a+''.join(ts);seg=pieces(tokens);row=next(r for r in J['all192_exact_foreign_b1_b2_b3_local_geometries']if r['tokens']==tokens);assert [xy(seg[0][0])]+[xy(d)for c,d in seg]==row['true_foreign_piece_and_ordinary_doubled_vertices']
  hits=[]
  for i,s in enumerate(seg[:-1]):
   h=meet(*s,*seg[-1])
   if h is None:continue
   if h[0]=='OVERLAP':
    c,d=seg[-1];u=d-c;co=lambda z:int(z.real)if u.real else int(z.imag)
    l,r=sorted((Fraction(co(s[0]-c),co(u)),Fraction(co(s[1]-c),co(u))));new=max(Fraction(0),l);assert new<=min(1,r);pt=c+new*u;v=s[1]-s[0];old=Fraction(int((pt-s[0]).real),int(v.real))if v.real else Fraction(int((pt-s[0]).imag),int(v.imag))
    assert tokens=='QCCU'and i==1 and new==Fraction(1,2)and old==1
   else:old,new=h
   if new>0:hits.append((new,i,old))
  if not hits:assert 'first_local_owner'not in row;continue
  t=min(z[0]for z in hits);own={i+1 if old==1 else i for tt,i,old in hits if tt==t};assert len(own)==1;owner=own.pop();assert owner==row['first_old_owned_piece_index0']and [t.numerator,t.denominator]==row['first_new_t']and owner<len(seg)-2
  rr=tr(''.join(W[b]for b in tokens)+M);fail,prev,q,ch=rr['bad'];start=sum(len(W[b])for b in tokens[:-1]);assert fail<start+len(W[tokens[-1]])
  if tokens=='FCCV':assert owner==0 and t==Fraction(3,4)and (fail,prev,q,ch)==(101,45,-1+0j,'R')
  else:assert tokens in['FCCU','QCCU','BCCU']and row['first_local_owner']=='b1:C'and t==Fraction(1,2)and (fail-len(W[a]),prev-len(W[a]),ch)==(42,2,'L')and fail-start==12
  oc=row['later_conflicting_actual_read_owner'];assert oc['actual_atom']==tokens[-1]and oc['canonical']['context_tick0']==fail-start and oc['canonical']['owner_read_number1']==fail-start+1
  contacts.append(tokens)
assert contacts==['FCCV','FCCU','QCCU','BCCU']
for b in'DCVU':assert(W[b]+M)[:11]==M
# Direct specialization of signed source-relative turn window. True age and two returned C increments remain separate.
rk={'U':0,'V':1,'D':2,'C':2};angles=[]
for b1,b2,old,b3 in itertools.product('DCVU',repeat=4):
 for n in range(5):
  N=n+(b1=='C')+(b2=='C')
  if old=='C'and n==0:continue
  # Strict endpoint form 0< N + (source tangent-target tangent)/pi/2 <4.
  # Equal D/C tangent rank is retained explicitly.
  if N<0 or N>4 or(N==0 and rk[old]<=rk[b3])or(N==4 and rk[old]>=rk[b3]):continue
  angles.append(dict(old_source=old,first=b1,second=b2,third=b3,true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age=n,first_returned_C_indicator=int(b1=='C'),second_returned_C_indicator=int(b2=='C'),total_ordinary_C_before_third=N,true_FOREIGN_heading_relative_old=(-n)%4,third_heading_relative_old=(2-N)%4))
key=lambda x:json.dumps(x,sort_keys=True);assert len(angles)==831 and set(map(key,angles))==set(map(key,J['all831_conditional_preFOREIGN_old_source_angle_interfaces']));cnt=dict(collections.Counter(r['old_source']for r in angles));assert cnt=={'D':206,'C':160,'V':229,'U':236}
report={'status':'PASS local third-RAW foreign/b1 source split and necessary831 older-source angles only','manifest_sha256':sha(mf),'script_sha256':sha(Path(__file__)),'all_closed_local_geometries':192,'RAW_impossible_contacts':contacts,'necessary_older_source_angle_counts':cnt,'analytic_checks':['Signed two-RAW simple prefix remains actually recognized because thirdRAW plus actualfinalM supplies priorM11, with D10 spilling exactlyone actual finalread.','All foreignpieces use actualF56bend; every closed segment intersection, including starts/ends and collinearity, recomputed before outgoing ownership. QCCU has a true collinear overlap with Qtail beginning at newparameter1/2 and oldterminal; earliest endpoint is assigned next outgoingb1C, not foreignterminal. All closed/collinear cases retained.','OnlyFCCVproperforeigncross andthreeACC U foreignexit/b1C contacts survivegeometry; all failinsideactualthirdRAW. b2/b3 are trueadjacencyonly by signed ordinaryjoin.','831 angles are a specialization of the signed arbitrary-tail Jordan source-window, not a new position catalogue. True preforeignn is separate fromboth returnedCindicators, sourceC requiresn>=1, foreignheading-n andthirdheading2-N retain fullCclock.','Immediate lastoldV/U remains allowed in older-source scope. No new lifetime law, fullproducer relabeling, thirdsimplicity or arbitrarytail inference.']}
p=R/'audits/third_local_interface_independent.json';p.write_text(json.dumps(report,indent=2)+'\n');print(sha(p));print(report['status'])
