from pathlib import Path
from collections import Counter
from fractions import Fraction as F
import json,hashlib
R=Path('/workspace/shared/langton');P=R/'old_D_second_age3_common_beta_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=P/'manifest.json';assert sha(mf)=='66aa94a995745ebbe703ec226381c641efa8677070cb3045e3bde6afc095fcac';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(P/f)==h
J=json.loads((P/'D_age3_common_beta.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
base=R/'audits/check_old_V_second_age1_independent.py';ns={'__file__':str(base)};exec(base.read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy,center=[ns[k]for k in('W','M','K','tr','rot','xy','center')];raw=lambda s:''.join(W[a]for a in s)
D=R/'core_periodicity_new/chronology_dcuv';G=json.loads((D/'literal_residual_geometry.json').read_text())['geometry'];ids=(0,1,4,5,6,7,8,9);compact={i:j for j,i in enumerate(ids)};COUNT={tuple(map(int,l.split()[:8]))for l in(D/'critical_ucc_count5/frozen_20261023_0813/01_closure.tsv').read_text().splitlines()};I={}
for i in ids:
 ctx=tr(raw(G[i]['name'])+M);I[G[i]['name']]={q for q,b in ctx['req'].items()if b and q not in K};assert set(map(tuple,map(xy,I[G[i]['name']])))==set(map(tuple,G[i]['inputs']))
co=Counter();ports=[];qindex=0
for si in(0,1):
 name=G[si]['name'];t=tr(raw(name));assert [(j,ch)for j,(q,h,ch)in enumerate(t['reads'])if q==2]==[(8,'R')];assert all(q!=1-1j for q,h,ch in t['reads'])
 for age in range(4):
  h=(-age)%4
  for ci in ids:
   consumer=G[ci]['name']
   for slot,inp in enumerate(G[ci]['inputs']):
    p=2-complex(*inp)*rot(h);x,y=xy(p);key=(compact[si],compact[ci],x,y,h,2,0,age)
    if age<name.count('C'):why='full_source_not_yet_completed'
    elif age+consumer.count('C')>3:why='consumer_full_tail_cannot_complete_before_foreign3'
    elif age<3:why='signed1344_common_atomic_ENTRY_minimum3'
    elif(x+y+h)%2:why='sector'
    elif key in COUNT:why='signed_COUNT5'
    else:why='exact_E3_plain_port';ports.append((name,consumer,p,h))
    z=J['all184_common_first_loss_full_role_queries'][qindex];assert(z['actual_full_source'],z['consumer'],z['input_slot0'],z['input_cell'],z['pose'],z['true_full_source_ENTRY_age'],z['key'],z['reason'])==(name,consumer,slot,inp,[x,y,h],age,list(key),why);co[why]+=1;qindex+=1
assert qindex==184 and dict(co)==J['query_classification']and len(ports)==5
cr=lambda a,b:int(a.real*b.imag-a.imag*b.real)
def chord(a,p=0j,h=0):
 e=tr(W[a],p,h);return center(p,h),center(e['p'],e['h'])
def strict(a,b,c,d):
 s=F(cr(c-a,d-c),cr(b-a,d-c));t=F(cr(c-a,b-a),cr(b-a,d-c));assert 0<s<1 and 0<t<1;return s,t,a+float(s)*(b-a)
old=chord('D');nex=[]
for name,c,p,h in ports:
 if c=='D':assert p==1 and h==1 and center(p,h)==old[1]
 elif p==-1:assert strict(*old,*chord(c,p,h))[:2]==(F(1,2),F(1,2))
 else:
  assert c=='V'and p==1j and h==1
  for a in'DCVU':
   s,t,q=strict(*chord(c,p,h),*chord(a,1+1j,0));nex.append([a,str(s),str(t),[str(F(q.real).limit_denominator()),str(F(q.imag).limit_denominator())]])
assert len(nex)==8
for row in J['all8_actual_prior_full_EXIT_bud_roles']:
 full=row['actual_previous_full'];t=tr(raw(full));q=t['p']+(1-1j)*rot(t['h']);assert t['last'][q]==('R',len(raw(full))-2)and q not in{t['p']+z*rot(t['h'])for z in K};assert row['beta_in_actual_previous_full_frame']==xy(q)and row['previous_full_ENTRY_clock']==-full.count('C')and row['full_ENTRY_age_at_foreign']==3+full.count('C')and row['true_post_EXIT_age_at_foreign']==3
ob=json.loads((R/'second_contact_signed_obligations_2026-10-24/signed_current_obligations.json').read_text());bases=[r for r in ob['all267_foreign_typed_base_rows']if(r['old'],r['n'])==('D',3)];rows=J['all54_foreign_typed_masks'];key=lambda r:(r['A'],r['b1'],r['b2'],tuple(r['pa']),tuple(r['p2']));assert{(r['foreign'],r['first'],r['second'],tuple(r['foreign_pose']),tuple(r['second_pose']))for r in rows}==set(map(key,bases))and len(rows)==54
counts=Counter();endpointchecks=0
for r in rows:
 T=r['foreign']+r['first']+r['second'];tt=tr(raw(T)+M);p=complex(*r['foreign_pose'][:2]);h=r['foreign_pose'][2];first={}
 for tick,(q,hh,ch)in enumerate(tt['reads']):first.setdefault(q,(ch,tick))
 masks=[]
 for q,z in zip((2+0j,1-1j),r['tag_context'],strict=True):
  local=(q-p)/rot(h);fr=first.get(local);assert z['cell']==xy(q)and z['foreign_local']==xy(local)and z['in_foreign_ENTRY_core']==(local in K)and z['actual_first_read']==(list(fr)if fr else None);masks.append(local in K or(fr and fr[0]=='R'))
  if fr:
   owner=z['actual_owner'];lo=0
   for k,a in enumerate(T):
    if fr[1]<lo+len(W[a]):assert(owner['actual_atom_index0'],owner['actual_atom'],owner['canonical']['context_tick0'])==(k,a,fr[1]-lo);break
    lo+=len(W[a])
   else:assert owner['actual_atom']=='next actual word'and owner['next_word_tick0']==fr[1]-lo and owner['next_word_read_number1']==fr[1]-lo+1
 if masks[0]:why='excluded_by_same_original_common_CURRENT'
 elif masks[1]:
  why='excluded_by_incoming_beta_min3_and_final_E_endpoint_guard';assert(r['first'],r['second_pose'])==('D',[0,-1,3])and r['second']in'DC'
  endrows=r['all8_beta_E3_endpoints'];assert len(endrows)==8
  for z in endrows:
   c=z['consumer'];inp=complex(*z['input_cell']);assert inp in I[c];cp=1-1j-inp*rot(1);end=tr(W[c],cp,1);assert z['consumer_pose']==[*xy(cp),1]and z['consumer_RAW_exit']==[*xy(end['p']),end['h']];dx,dy=xy(p-end['p']);solutions=[];sector=(sum(xy(cp))+1)%2
   if not sector and dx>=0 and dy<=0:
    # Every later packet is plain E. These exact nonnegative equations exhaust all lengths.
    for v in range(-dy+1):
     d=-dy-v;rem=dx-d-3*v
     if rem<0 or rem%4:continue
     u=rem//4
     if d+v+u==0:ok=c=='U'or(c=='V'and r['foreign']in'FQ')
     else:ok=u>0 or(v>0 and r['foreign']in'FQ')
     if ok:solutions.append((d,v,u))
   assert not solutions and z['count_solutions']==[];endpointchecks+=1
 else:why='necessary_only_unresolved';assert r['first']in'VU'and r['second']in'VU'and r['second_pose']==[1,0,3]
 assert r['classification']==why;counts[why]+=1
assert dict(counts)==J['exact_disjoint_classification']and endpointchecks==48
report={'status':'PASS old-D age3 reduction42/54 per source D/DC role,12 necessary masks remain','manifest_sha256':sha(mf),'script_sha256':sha(Path(__file__)),'dependencies':J['dependencies'],'common_queries':dict(co),'surviving_plain_E_ports':[[a,b,*xy(p),h]for a,b,p,h in ports],'actual_next_N_atom_strict_crossings':nex[:4],'disjoint_masks':dict(counts),'beta_endpoint_equations':endpointchecks,'analytic_review':['Common sameR8 sourceD/DC tag preserved, first CURRENT loss includes all true full I slots/marker core capture; only five completed E3 alignments remain','Their entry is a nonadjacent oldD EXIT repeat or strict actual oldD/next N atom crossing. The next actual oldatom D/C/V/U necessarily exists because three C turns intervene before foreign','Incoming beta is genuine final atomic EXIT output of all8 previous full roles, not a reset full-entry age. True postEXIT3 permits only final E3 plain D/V/U consumers before the complete foreign boundary','All48 beta obligations exhaust arbitrary final E-run counts and actual lastV/U foreign adjacency, including empty continuation. No earlier-stage bound or postforeign maturation law','Twelve V/U,V/U masks retain common/beta BLACK requirements and remain necessary-only; fullDC stronger cohort proof is separate']}
f=R/'audits/old_D_age3_common_beta_independent.json';f.write_text(json.dumps(report,indent=2)+'\n');print(sha(f));print(report['status'])
