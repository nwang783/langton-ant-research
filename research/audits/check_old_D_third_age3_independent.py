from pathlib import Path
from itertools import product
from fractions import Fraction as F
from collections import Counter
import json,hashlib,math
S=Path(__file__);R=S.parents[1];D=R/'old_D_third_age3_beta_loss_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='be2ad76d4b0364f52fd73788079ef9a648f35a484ff801fe4aa3f87ea9c26982';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'D_third_age3_beta_loss.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,K,tr,G,rot,center,xy,meet,pieces,cross=[ns[k]for k in('W','M','K','tr','G','rot','center','xy','meet','pieces','cross')];raw=lambda seq:''.join(W[a]for a in seq);full=('D','DC','V','VC','VCC','U','UC','UCC')
def inv(s):
 z=tr(raw(s));ct=tr(raw(s)+M);ek={z['p']+rot(z['h'])*q for q in K};ii={q for q,b in ct['req'].items()if b and q not in K};oo={q for q,(c,t)in z['last'].items()if c=='R'and q not in ek}
 for q in ek-K:assert q in ct['req']and(q in ii or ct['req'][q]is False)
 return z,ct,ii,oo,ek
I={s:inv(s)for s in full};beta=1-1j;common=2;g=-1j
for s in ('D','DC'):
 assert beta not in I[s][1]['req'];assert I[s][1]['last'][g]==('L',3)and g not in I[s][3]|I[s][4]
for s in full:
 z=I[s][0];slot=z['p']+rot(z['h'])*beta;assert slot in I[s][3]and z['last'][slot]==('R',len(raw(s))-2)
 assert all(q.imag>=0 and I[s][0]['last'][q][0]=='R'for q in I[s][3])
assert I['DC'][3]=={2,2+3j,3+1j,3+2j}
# A cannot follow selected plainD directly; actual next FULL packet therefore exists before firstforeign.
assert all(tr(W['D']+W[a]+M)['bad']is not None for a in'FQB')
assert I['D'][0]['p']==1+1j and I['D'][0]['h']==0
assert all(I[a][0]['p'].imag>0 and I[a][0]['h']==0 for a in'DVU')
angles=[a for a in json.loads((R/'third_ordinary_local_interface_2026-10-24/third_local_interface.json').read_text())['all831_conditional_preFOREIGN_old_source_angle_interfaces']if a['old_source']=='D'and a['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age']==3];assert len(angles)==36
old=pieces('D')[0];u=old[1]-old[0];poses=0;cases={};counts=Counter();left={}
def key(r):return(r['source'],r['nextfull'],r['b1'],r['b2'],r['b3'],r['A'],tuple(r['pa']),tuple(r['p3']))
cert={key(r):r for r in J['typed_rows']};assert len(cert)==1458
for ag in angles:
 b1,b2,b3=ag['first'],ag['second'],ag['third'];KK=3+(b1+b2).count('C');h=(2-KK)%4;ha=1;assert(KK,h,ha)==(ag['total_ordinary_C_before_third'],ag['third_heading_relative_old'],ag['true_FOREIGN_heading_relative_old'])
 z=tr(W[b3],h=h);c=center(0,h);v=center(z['p'],z['h'])-c;den=cross(u,v);corners=[(old[0]+s*u-c-t*v)/2 for s,t in product((0,1),repeat=2)]
 for x in range(math.floor(min(q.real for q in corners)),math.ceil(max(q.real for q in corners))+1):
  for y in range(math.floor(min(q.imag for q in corners)),math.ceil(max(q.imag for q in corners))+1):
   if(x+y-KK)%2:continue
   p=x+y*1j;off=c+2*p-old[0]
   if den:ss,tt=F(cross(off,v),den),F(cross(off,u),den)
   else:
    if cross(off,u):continue
    mul=F(int(v.real),int(u.real));q=F(int(off.real),int(u.real));assert mul>0
    if q>=0:continue
    ss=F(0);tt=-q/mul
   if not(0<=ss<1 and 0<tt<=1):continue
   poses+=1
   for A in'FQB':
    dz=tr(raw(A+b1+b2),h=ha);pa=p-dz['p'];assert dz['h']==h;local=tr(raw(A+b1+b2+b3)+M);assert local['bad']is None
    # All earlier closed pieces, with F+Q/B tail split, miss this old source.
    ep=pa;hh=ha;verts=[center(ep,hh)];f=tr(W['F'],ep,hh);verts.append(center(f['p'],f['h']));a=tr(W[A],ep,hh);ep,hh=a['p'],a['h']
    if A!='F':verts.append(center(ep,hh))
    for atom in(b1,b2):z0=tr(W[atom],ep,hh);ep,hh=z0['p'],z0['h'];verts.append(center(ep,hh))
    assert not any(meet(*old,a,b)is not None for a,b in zip(verts,verts[1:]))
    for source,nxt in [('DC',None)]+[('D',s)for s in full]:
     facts={common}
     if source=='DC':facts|={2+3j,3+1j,3+2j}
     elif nxt[0]=='D':facts.add(3+1j)
     elif nxt[0]=='V':facts|={1+1j,2+1j,3+2j}
     else:
      facts|={1+1j,1+2j,2+1j,2+2j};fore=tr(W[A]+M);assert not any((q-pa)/rot(ha)in fore['req']for q in facts-{common})
     cuts={q for q in facts if(q-pa)/rot(ha)in K or local['req'].get((q-pa)/rot(ha))is False};why='CURRENT_cut'if cuts else'NECESSARY';kk=(source,nxt,b1,b2,b3,A,tuple(xy(pa)+[ha]),tuple(xy(p)+[h]));r=cert[kk];assert why==r['why']and cuts=={complex(*q)for q in r['cuts']};cases[kk]=why;counts[why]+=1
     if not cuts:
      assert b2=='D'and b3 in'DC'and p==-1j and h==3;qb=(beta-pa)/rot(ha);assert qb not in K and local['req'][qb]is False
      tick=next(i for i,(q,hh,ch)in enumerate(local['reads'])if q==qb);assert r['beta_first_required_turn_tick0']==['R',tick]and len(W[A])<=tick<len(W[A])+len(W[b1]);left[(A,b1,b2,b3,tuple(xy(pa)+[ha]))]=tick
assert poses==54 and len(cases)==1458 and counts==Counter(CURRENT_cut=1296,NECESSARY=162)and len(left)==18
ports=[]
for atom in'DVU':
 for inp in I[atom][2]:
  p=beta-rot(1)*inp;z=tr(W[atom],p,1);tc=(common-p)/rot(1)
  if(int(p.real+p.imag)+1)%2:why='sector'
  elif tc in I[atom][2]:why='takes_held_source_common'
  elif atom=='D':assert center(p,1)==center(0,0);why='repeats_source_D_ENTRY'
  elif(z['p'],z['h'])==(1-2j,1):assert center(z['p'],z['h'])==center(-1j,3);why='repeats_second_D_EXIT_before_third_ENTRY'
  else:assert(atom,inp,p,z['p'])==('U',-1+2j,-1-2j,3-2j)and p+rot(1)*(-1+1j)==g;why='deleted_source_core_cannot_fund_lower_a'
  ports.append((atom,tuple(xy(inp)),tuple(xy(p)+[1]),tuple(xy(z['p'])+[z['h']]),why))
assert set(ports)=={(r['atom'],tuple(r['input']),tuple(r['head']),tuple(r['raw_exit']),r['reason'])for r in J['first_beta_loss_ports']}
q=json.loads((R/'audits/dcuv_count5_replay/queries.json').read_text());assert all(q['slots'][f'{i}:(-1, 1)']['certified_minimum_C_age']==3 for i in(7,8,9))
out=dict(status='PASS scoped oldD THIRD true-prefage3 beta-loss closure',manifest=sha(MF),angles=36,poses=poses,typed_cases=len(cases),initial_partition=dict(counts),remaining_physical_targets=len(left),all8_beta_loss_ports=ports,analytic_review=[
'Exact36 angle domains/54 outgoing-owned heads/1458 source-nextFULL masks independently reconstructed. All local traces are feasible and earlier pieces miss oldD;1296 before-CURRENT contradictions and162typed/18physical beta-WHITE residues match. Actual sourceDC uses its signed full4-output cohort, not an invented next-base source.',
'For plainD, each D+A+M literal is impossible, so actual next complete8 packet beforeFOREIGN genuinely exists at1,1N clock0. All8 full types, ownC completion and true source clocks retained. Current Dcommon, nextV r/B/C and nextU star guards apply only preA3; no postA age.',
'Genuine previous full final-atomic EXIT beta exists because selectedD is noninitial in U-entry factor. All8 prior full freshR exits checked; D/DC plus marker never readbeta. Every remaining mask first requests beta WHITE in actualb1, never earlierFOREIGN, so physical retirement beforeA is necessary. Earliest CURRENT loss has clock3 and must finish as plainE D/V/U before completeA3.',
'All8 beta input ports include marker CORE capture:2sector,2take still-held common,1 repeatsoldDentry,2 repeat the ACTUAL b2 exit correctedcenter1,-3. Last pair uses already signed TWO-RAW simplicity, not assumed third simplicity. Its actual followingM is supplied by actualthirdRAW plus finalM including D10 spill.',
'LastU lowerq port needs true lower-a g0,-1 BLACK. ActualsourceD L3 deletesg and containingD/DC never rereads/exports/core-retains it. Any later residual identity must come from a completed genuine full producer; exact fullO consists of fresh lastR identities and covers core-to-residual export. Nonoverlapping packets exclude any earlier-starting later-finishing producer across the deleting containingpacket.',
'Every laterclock0 producer isN with heady>=1; all8 full outputs have localy>=0, including tails, so cannotexportg. Every entryclock>=1 producer has age<=2 at consumer3, below exactU/UC/UCC lower-a min3. This excludes funding, not permanentphysical whiteness. No unfinished consumer tail or postforeign age is used.',
'Only oldD truepreA3 GLOBAL-FIRST THIRD source slice closes. Younger D/V slices and overallTHIRD simplicity remain separate.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
