from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'foreign_three_C_NE_reserve_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'manifest.json';assert sha(mf)=='f24ab1025b88752f6cf5c27f02c9939fb67a9be69e2b920e091e174ae55c5b77'
m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy=[ns[k]for k in ('W','M','K','tr','rot','xy')];J=json.loads((D/'three_C_NE_reserve.json').read_text())
G={a:tr(W[a])for a in W};CT={a:tr(W[a]+M)for a in W};I={a:{q for q,b in CT[a]['req'].items()if b and q not in K}for a in W};O={a:{q for q,(c,t)in G[a]['last'].items()if c=='R'and q not in {G[a]['p']+rot(G[a]['h'])*x for x in K}}for a in W}
NE={-1-1j,-1+0j,-1+1j,0j,1j,1+0j,1+1j,1+2j,2+0j,2+1j};FIELD=NE|{-2-1j};hole=2j
assert not I['C']and sum(len(I[a])for a in 'DVU')==8
for a in 'FQB':
 assert FIELD<=O[a]and G[a]['last'][hole]==('L',28)and G[a]['last'][-2-1j]==('R',47)and G[a]['last'][-1-1j]==('R',46)
 assert G[a]['h']==2 and G[a]['p'].imag<=-2
# Whole S/E epochs from actual exit. Complete R and true-input coordinate bounds.
for a in 'DVU':
 assert all(q.imag>=1 and q.real>=-1 for q in I[a])
 assert G[a]['p'].imag>0 and G[a]['p'].real>=0
for a in 'DCVU':
 rr=[q for q,h,c in G[a]['reads']if c=='R'];assert min(q.imag for q in rr)>=0 and min(q.real for q in rr)>=-1
# S head y<=-2 => inputs<=-3 and physicalR<=-2. E follows S-C,
# so head y<=-3 => inputs/R<=-2. Neither writes h2 or loses FIELD y>=-1.
rows=[];counts={};gates=[]
au={(z['heading'],tuple(z['original']),z['consumer'],tuple(z['true_input'])):z for z in J['all176_joint_first_loss_roles']}
for h in (0,3):
 counts[h]=Counter()
 for tag in FIELD:
  for a in 'DVU':
   for q in I[a]:
    p=tag-rot(h)*q;k=(h,tuple(xy(tag)),a,tuple(xy(q)));ar=au[k];assert ar['ENTRY']==[*xy(p),h]
    if(int(p.real+p.imag)+h)%2:route='sector'
    else:
     bad={v for v in FIELD if(v-p)/rot(h)in K or CT[a]['req'].get((v-p)/rot(h))is False}
     route='held_field'if bad else'first_loss_gate'
     assert bad=={complex(*x['original'])for x in ar['conflicts']}
    assert route==ar['route'];counts[h][route]+=1;rows.append((k,[*xy(p),h],route))
    if route=='first_loss_gate':gates.append((h,a,p,tag))
assert counts[0]=={'sector':42,'held_field':44,'first_loss_gate':2}and counts[3]=={'sector':46,'held_field':41,'first_loss_gate':1}
assert set(gates)=={(0,'U',3-1j,2+0j),(0,'U',3-1j,2+1j),(3,'U',2+3j,1+2j)}
wg=2+3j;slot=(hole-wg)/rot(3);assert slot==-1+2j and next((i,c)for i,(q,h,c)in enumerate(CT['U']['reads'])if q==slot)==(13,'L')
fund=[]
for a in 'DVU':
 for q,(c,t)in G[a]['last'].items():
  if c!='R':continue
  p=hole-q
  if int(p.real+p.imag)%2:continue
  if any(v-p in K or CT[a]['req'].get(v-p)is False for v in NE):continue
  fund.append((a,[*xy(p),0],t,[*xy(p+G[a]['p']),0]));assert p+G[a]['p'] in(-1+3j,-1+5j,-2+6j)
assert set((a,tuple(p),t,tuple(e))for a,p,t,e in fund)=={(z['producer'],tuple(z['ENTRY']),z['actual_R_own_tick0'],tuple(z['RAW_EXIT']))for z in J['all3_N2_CORE_inclusive_hole_funders']}
assert len(fund)==3 and all(e[1]+1>3 for a,p,t,e in fund)
bounds=[]
for a in 'DCVU':
 for t,(q,hh,c)in enumerate(G[a]['reads']):
  if c!='R':continue
  if a=='C':
   assert q.real>=0;p=hole-q;h=0;ep=p+G[a]['p'];assert ep.real<=0
  else:
   assert q.imag<=G[a]['p'].imag;p=hole-rot(3)*q;h=3;ep=p+rot(3)*G[a]['p'];assert ep.real<=0
  bounds.append((a,t,xy(q),[*xy(p),h],[*xy(ep),(h+G[a]['h'])%4]))
AB=[(z['atom'],r['own_tick0'],r['physical_R_local'],r['producer_ENTRY'],r['actual_RAW_EXIT'])for z in J['all_actual_physical_R_bounds_for_C3_and_W']for r in z['all_actual_R_supports']];assert bounds==AB
ng=3-1j;new={ng+q for q in O['U']};old=FIELD-{2+0j,2+1j};assert len(new)==len(old)==9 and not(new&old)and max(q.imag for q in new|old)==2
assert ng+G['U']['p']==3+3j and all(q-ng not in CT['U']['req']for q in old)
assert sorted(map(xy,old))==J['transfer_dichotomy']['nine_retained_originals']and sorted(map(xy,new))==J['transfer_dichotomy']['nine_new_U_outputs']
# Every later N input >=headY+1>=4; C givesW headY>=4 and its
# W inputs >=headY-1>=3, above all18 retained/new identities.
for a in 'DVU':assert min(q.imag for q in I[a])>=1 and min((rot(3)*q).imag for q in I[a])>=-1 and(rot(3)*G[a]['p']).imag>=0
out=dict(status='PASS genuine foreign eleven-tag reserve through ordinary C3 only',manifest=sha(mf),script=sha(S),role_counts=counts,all176_roles=rows,N_funders=fund,all_physical_R_bounds=bounds,retained9=sorted(map(xy,old)),new9=sorted(map(xy,new)),analytic_review=['S0/E1 cones are sourceENTRY-normalized and use actual F/Q/B EXIT y<=-2; no earlier history/U/simple premise. All physicalR slots and marker-inclusive true inputs are retained. C has no external input, so cannot silently absorb a CURRENT tag into CORE.','At earliest loss all11 are genuinelyCURRENT. The N paired gate consumes twoTRUE simultaneous inputs, not a false field contradiction. Its nine surviving source IDs and nine NEW U outputs lie below every remaining N/C/W input cone. Original q is dead; newq is a distinctR identity.','If NE is still unspent at W3, sourceL28 hole remainsWHITE unless an actual prior RAW R repairs it. All28 CORE-inclusive N lastR candidates reduce to three exits toohigh before C3; all physical C3/W R writers exitx<=0, so W monotonicity cannot reach gatex2. Whole actualRAW packets do not overlap, and the gate itself firstreads h atL13 with no earlier repair.','Therefore sourceR46/R47 survive CURRENT through these ordinary cuts. No survival through any subsequent FOREIGN or afterC3 is imported.'],scope=m['scope'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(sha(S.with_suffix('.json')))
