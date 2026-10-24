from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'MIDDLE_SHORT_C_CORE_FOUR_CHANNEL_OWNER_INTERFACE.md';A=D/'middle_short_C_core_ports_certificate.json';assert sha(P)=='22ecb8ce96b2ecab8d42a72794908541ee9de4b46fcd92f3e70835cadf6ccb56';assert sha(A)=='347a3a50a608166da1ae13386e05e2404cc8358f4e741e3cc38068304fa51c7a';assert sha(D/'certify_middle_short_C_core_ports.py')=='7d5ec41d00444551ea216b0b947b4b650461eec3ae222bbcd22bb93ce9009a7e';J=json.loads(A.read_text())
for f,h in J['dependencies'].items():assert sha(D/f)==h
prior=S.parent/'check_middle_short_coincident_C_independent.json';assert sha(prior)=='9f0a6ffabae1161c317bc838cff444609fd74740978e5ef0917b0d08ab5a07e0';Q=json.loads(prior.read_text());N={};exec((S.parent/'check_drift31_refined_top_gap_independent.py').read_text().split("for line in(P/'DRIFT31_REFINED_TOP_ODD_GAP_SHA256SUMS')")[0],N);graph,rk,oh=[N[x]for x in('graph','rk','o')];off=[-1j,-1-1j,-1,0j];T=lambda p:int(3*p.imag-p.real);xy=lambda p:[int(p.real),int(p.imag)];V=[1j,1,-1j,-1];rows=[]
for ii,hs in enumerate(Q['six_survivors']):
 H={int(t):['NESW'.index(h)for h in w]for t,w in hs.items()};ar=J['six_named_interface_checks'][ii];su,ev,chains,seen,lev=graph(H);inc={f:(e,k)for e,(f,k)in su.items()};core={(t,r)for t,r in ev if T(-t+off[H[t][r]])in[1,3,5]};assert len(core)==24 and sum(r%2==0 for t,r in core)==14;assert sorted([list(e)for e in core])==ar['all24_core_events'];starts=sorted(e for e in core if e not in inc or inc[e][0]not in core);assert set(starts)=={(7,2),(4,3),(7,1),(5,3)};covered=set();cc=[]
 for st in starts:
  e=st;k=0;seq=[]
  while True:
   assert e not in covered;covered.add(e);t,r=e;p=-t+k*(3+1j);h=H[t][r];seq.append(dict(node=list(e),lift=k,position=xy(p),heading=h,turn='R'if r%2==0 else'L',C_face=xy(p+off[h])))
   f,l=su[e]
   if f not in core:break
   e=f;k+=l
  before,nu=inc[st];after,dnu=su[e];z=dict(start=list(st),events=seq,word=''.join(e['turn']for e in seq),incoming_outside_node=list(before),incoming_edge_voltage=nu,outgoing_outside_node=list(after),outgoing_edge_voltage=dnu,last_lift=k);assert z==next(c for c in ar['four_actual_core_channels']if c['start']==list(st));cc.append(z)
 assert covered==core
 assert{tuple(z['start']):(z['word'],len(z['events']))for z in cc}=={(7,2):('RLRRRRLRRRRL',12),(4,3):('LLRLRRRRL',9),(7,1):('L',1),(5,3):('LL',2)}
 intern=[];exp=[];imp=[];perm=[]
 for t,w in sorted(H.items()):
  for r in range(0,len(w)-1,2):
   z=dict(R_node=[t,r],L_node=[t,r+1],same_physical_position=[-t,0],R_heading=w[r],L_heading=w[r+1]);src=(t,r)in core;dst=(t,r+1)in core
   if src and dst:intern.append(z)
   elif src:exp.append(z)
   elif dst:imp.append(z)
  if len(w)%2 and(t,len(w)-1)in core:perm.append([t,len(w)-1])
 assert(intern,exp,imp,perm)==(ar['nine_internal_lifetimes'],ar['two_exported_lifetimes'],ar['one_imported_lifetime'],ar['three_core_permanent_outputs']);assert(len(intern),len(exp),len(imp),len(perm))==(9,2,1,3);assert 14-10==3+2-1
 x=next(z for z in cc if z['start']==[7,2]);y=next(z for z in cc if z['start']==[4,3]);assert x['outgoing_outside_node']==y['incoming_outside_node']==[7,3];assert su[7,3][0]==(4,3)
 # No period/lifetime identification: the outside L3 is the actual next step
 # after the twelve contiguous X reads at its SAME physical T7 cell.
 last=x['events'][-1];e=tuple(last['node']);k=last['lift'];f,dk=su[e];assert f==(7,3)and k+dk==0
 t8=H[8];thirdN=rk(t8,0)[2];Eports=rk(t8,1,True);assert Eports[0]==0 and Eports[-1]==7 and len(Eports)==3;zrank=Eports[1];assert zrank in[3,5]and thirdN in[3,5]and zrank!=thirdN;order='Y,W,Z,X,Y'if thirdN<zrank else'Y,Z,W,X,Y';assert order==ar['cyclic_core_order'];assert thirdN==imp[0]['L_node'][1]and imp[0]['R_node'][1]==thirdN-1
 assert T(-8+off[t8[thirdN-1]])==9 and T(-8+off[t8[thirdN]])==5
 for e in exp:assert T(-e['L_node'][0]+off[e['L_heading']])==7
 # Every surviving T10 startsSN, so the signed upper SS first-parent
 # alternative is unavailable. Rebuild the actual entering edge and priorR.
 assert H[10][:2]==[2,0];assert su[7,1]==((10,1),1);p=-10+(3+1j);assert p==-7+1j;assert p+off[0]==-7+0j and T(p+off[0])==7;assert p+off[2]==-8+1j and T(p+off[2])==11
 rows.append(dict(T8=''.join('NESW'[h]for h in t8),core=sorted([list(e)for e in core]),channels=cc,internal=intern,exports=exp,imports=imp,permanent=perm,cyclic_order=order,third_N_rank=thirdN,Z_supplier_S_rank=zrank,C7_first_parent_event=[7,1],C7_first_read=[10,1],actual_prior_R0_on_C11=[10,0]))
assert len({json.dumps(r,sort_keys=True)for r in rows})==2
O=dict(status='PASS complete24-event four-channel middle-short C core and exact ownership/order interface',proof=sha(P),certificate=sha(A),script=sha(S),signed_local_cover=sha(prior),all6_interface_checks=rows,analytic_review=[
'Core membership is the active C-face class, not the physical boundary cell. All24 complete events of C1/C3/C5, including every physical lift, are selected; T8 S-sector reads remain outside. Independent ordinal graph extraction gives four open event-disjoint actual channels of12,9,1,2 reads, exhausting the core with14R/10L.',
'The sole fixed exterior interval is the actual T7.L3 immediately between X andY. It consumes X-start T7.R2 at the same physical point after12 updates. Other exterior intervals retain arbitrary lengths and old stock. The components are genuine contiguous successor channels, not repaired lifetime paths.',
'With C5 activation0, Y tail is0..4, X startsP-17 and nextY beginsP-4. W is the pair ending at T8 thirdN and Z follows the middle E-departure S/L of T8. Complete ranks3 versus5 put W beforeZ for NNSNSSSS and afterZ for NNSSSNSS. This derives two cyclic orders without selecting a period or discarding seams.',
'Actual R-to-nextL pairing gives9 internal lifetimes,2 exports T6R2/T7R2 to C7,1 opposite-heading import T8S/R2-or4 to its nextN/L3-or5 on C5, and3 permanent core outputs T0/T1/T2. The exact4=3+2-1 balance is bookkeeping, not input fuel. The exterior has the otherfive full odd outputs, with its own imbalance4; it is not a complete WHITE translating word.',
'Every one of the six complete T10 histories beginsSN. The signed upperSS C7 first-parent alternative is therefore impossible: actual T7.L1 onC5 enters T10.N/L1 onC7. Its earlier physical R0 is active atC11, so C11 was already active. No different-basin, first/last connectivity, monotone age or owner injection follows.',
'No whole exterior completion, finite-state controller, period/age bound, four lifetime-boundary type exclusion, universal WHITE S1 or capture is asserted. The two core cyclic orders are not identified with the four boundary matching types.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
