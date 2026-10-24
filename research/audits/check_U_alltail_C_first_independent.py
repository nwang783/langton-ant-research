from pathlib import Path
from fractions import Fraction
import json,hashlib,math
R=Path('/workspace/shared/langton');P=R/'old_U_arbitrary_tail_C_first_contact_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=P/'manifest.json';assert sha(mf)=='5b1b08308767de12c278289ca2c1c405dc22492bb6a6b22094a3b036a686520b'
for f,h in json.loads(mf.read_text())['files'].items():assert sha(P/f)==h
J=json.loads((P/'C_first_contact.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
p=R/'audits/check_old_V_second_age1_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('# Universal')[0],ns)
W,M,K,tr,rot,xy,center,cross=[ns[k]for k in ['W','M','K','tr','rot','xy','center','cross']]
angle=J['exact_signed_arbitrary_tail_angle_row'];assert angle['allowed_C_counts_before_contact_ENTRY']==[1,2,3,4]
u=tr(W['U']);a=center(0j,0);b=center(u['p'],u['h']);dv=b-a;cases=[]
for Cclock in range(1,5):
 h=(2-Cclock)%4;c=center(0j,h);zz=tr(W['C'],0j,h);d=center(zz['p'],zz['h']);nv=d-c;den=cross(dv,nv);assert den
 corners=[(a+s*dv-c-t*nv)/2 for s in[0,1]for t in[0,1]]
 for x in range(math.floor(min(p.real for p in corners)),math.ceil(max(p.real for p in corners))+1):
  for y in range(math.floor(min(p.imag for p in corners)),math.ceil(max(p.imag for p in corners))+1):
   if(x+y+h)%2:continue
   p=complex(x,y);q=2*p+c-a;s=Fraction(cross(q,nv),den);t=Fraction(cross(q,dv),den)
   if not(0<=s<1 and 0<t<=1):continue
   T=tr(W['C'],p,h);core={p+z*rot(h)for z in K};cuts=[]
   for z in[0j,1j]:
    if z in core:cuts.append((xy(z),'entryCORE'))
    elif T['req'].get(z)is False:cuts.append((xy(z),'firstRAW_R',next(i for i,(q,hh,ch)in enumerate(T['reads'])if q==z)))
   assert cuts and s in[0,Fraction(1,2)]and t==1;row=next(r for r in J['all8_outgoing_owned_contact_C_poses_and_actual_LEFT_contradictions']if r['total_actual_C_before_contact_ENTRY']==Cclock and r['contact_C_pose']==[x,y,h]);assert row['old_outgoing_s']==str(s)and row['new_positive_t']==str(t)
   assert{tuple(e[0])for e in cuts}=={tuple(e['SAME_original_LEFT_cell'])for e in row['actual_contradictions']}
   for z in row['actual_contradictions']:
    if not z['in_actual_entry_K']:assert z['first_physical_read']['context_tick0']<15 and z['first_physical_read']['turn']=='R'
   cases.append([Cclock,[x,y,h],str(s),str(t),cuts])
assert len(cases)==8
report={'status':'PASS arbitrary ordinary-tail oldU-source/global-FIRST-C contact exclusion','manifest_sha256':sha(mf),'script_sha256':sha(Path(__file__)),'exact8_outgoing_owned_poses':cases,'analytic_checks':['Signed arbitrary-tail Jordan clock gives TOTAL actualC countK1..4; true sourceU-entry tofirstFOREIGN age n is only a nonnegative subcountn<=K. Genuine sourceUC/UCC tails count inboth only when actuallypreceding; no falsefundingclock equality.','Signed genuine old8star permanence plus beforeFOREIGN RAW0..4 and marker/core first-effect bounds supply COMPLETEforeigncontextMISS at n<=4, not a postforeign maturity law.','Choose GLOBAL first proxycontact and stop at candidateCENTRY. Entire preceding completedordinaryprefix is simple bydefinition; actualnextCsupplies its M11. Signed bf1018 applies exactlythere and yields SAMELEFT CURRENT outsideentryK. No presumption through candidateC or iterativefinite-transfer use.','Exact four rational contactboxes/activeparity/outgoingold s<1/positive newt rebuilt. All8 Cposes have t1,s0or1/2 and actualentryCORE or ownRAW firstR contradiction withheldLEFT.','No foreignerosion branch, originalRIGHT/q/shadow persistence afterforeign, generaltail simplicity,otheroldsource orD/V/Utarget exclusion.']}
p=R/'audits/U_alltail_C_first_independent.json';p.write_text(json.dumps(report,indent=2)+'\n');print(sha(p));print(report['status'])
