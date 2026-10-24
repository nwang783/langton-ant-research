from pathlib import Path
from collections import Counter
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'foreign_C4_joint_hook_reserve_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'manifest.json';assert sha(mf)=='826a3f54e7584cf2eae5de1144ed30fd50874f1c83da61f6a29819e366e68c17';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'C4_joint_hook.json').read_text());N={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(N['__file__']).read_text().split('# Universal')[0],N);W,M,K,tr,rot,xy=[N[k]for k in('W','M','K','tr','rot','xy')];G={a:tr(W[a])for a in W};C={a:tr(W[a]+M)for a in W};I={a:{q for q,b in C[a]['req'].items()if b and q not in K}for a in W};pose=lambda p,h:[*xy(p),h];ff=lambda a,q:next(([c,i]for i,(v,h,c)in enumerate(C[a]['reads'])if v==q),None);sort=lambda s:sorted(s,key=lambda q:(q.real,q.imag))
F15={-1-1j,-1+0j,-1+1j,0j,1j,1+0j,1+1j,1+2j,2+0j,2+1j,-4+1j,-4+2j,-3+2j,-2+1j,-2-1j};old13=F15-{2+0j,2+1j};HK={-1-1j,-2-1j,-3-1j,-3-2j};fields={'F_unspent':F15,'F_paired':old13,'QB_unspent':F15|HK,'QB_paired':old13|HK};a=-3+3j;r=-4+3j
for source in'FQB':
 assert G[source]['last'][a]==('L',34)and G[source]['last'][r]==('L',35)
 ek={G[source]['p']+rot(G[source]['h'])*q for q in K};actual={q for q,(c,t)in G[source]['last'].items()if c=='R'}-ek;assert F15<=actual
 if source in'QB':assert HK<=actual
# Every CORE capture of an external SAME tag is covered by an actual external
# BLACK requirement in RAW+the real next M, or conflicts with a first R.
marker=[];core=[]
for atom in'DCVU':
 ek={G[atom]['p']+rot(G[atom]['h'])*q for q in K}
 for q in ek-K:assert q in C[atom]['req'];core.append(dict(atom=atom,local=xy(q),first=ff(atom,q)))
 for q in I[atom]:
  if q not in G[atom]['req']:assert q in ek;marker.append(dict(atom=atom,local=xy(q),first=ff(atom,q)))
assert not I['C']and sum(len(I[x])for x in'DVU')==8
assert all(q in K for q,b in C['C']['req'].items()if b)
reports=[];seen=0
for name,field in fields.items():
 au=next(z for z in J['all480_joint_first_S4_CURRENT_loss_rows']if z['field_name']==name);assert au['SAME_current_at_S4_start']==list(map(xy,sort(field)));rows=[];co=Counter();gates=[]
 for tag in sort(field):
  for atom in'DVU':
   for slot in sort(I[atom]):
    p=tag+slot;ar=next(z for z in au['all_first_CURRENT_loss_rows']if z['original']==xy(tag)and z['consumer']==atom and z['ENTRY']==pose(p,2));assert ar['true_input']==xy(slot)and ar['actual_L']['context_tick0']==ff(atom,slot)[1]
    if(int(p.real+p.imag)+2)%2:route='sector'
    else:
     bad=[]
     for g in sort(field):
      q=p-g;first=ff(atom,q)
      if q in K or first and first[0]=='R':bad.append(dict(SAME_original=xy(g),local=xy(q),first=first,reason='ENTRY_CORE'if q in K else'first_WHITE'))
     assert bad==ar['current_field_conflicts']
     if bad:route='held_field'
     else:
      assert atom=='U'and p in[-5+3j,-4+4j];hole,tick=(r,1)if p==-5+3j else(a,14);assert ff(atom,p-hole)==['L',tick]and tick<len(W[atom]);assert ar['WHITE_hole']==xy(hole)and ar['own_BLACK_request']['context_tick0']==tick;route='source_only_f01_WHITE_hole';gates.append(dict(tag=xy(tag),ENTRY=pose(p,2),hole=xy(hole),own_L=tick))
    assert route==ar['route'];co[route]+=1;rows.append(dict(original=xy(tag),consumer=atom,ENTRY=pose(p,2),input=xy(slot),route=route))
 assert len(rows)==len(au['all_first_CURRENT_loss_rows'])==8*len(field)and dict(co)==au['counts']and len(gates)==5;seen+=len(rows);reports.append(dict(name=name,counts=dict(co),all_rows=rows,five_labels_two_gates=gates))
assert seen==480
# Source-only lift: independently rebind the actual N/W/S frontier pieces,
# not the target-dependent final C5/E5 obstruction.
f01=json.loads((R/'audits/check_FOREIGN_C5_left_hole_independent.json').read_text());assert f01['manifest']==m['dependencies']['foreign_C5_left_hole_frontier_2026-10-24/manifest.json'];assert len(f01['all216_physical_final_R_roles'])==216
rr=f01['all216_physical_final_R_roles'];fund=lambda hole,h:[(atom,p,ep)for hh,eh,atom,p,ep,why in rr if hh==xy(hole)and eh==h and why=='possible_funder']
assert fund(a,2)==[]and fund(r,2)==[('U',[-4,4,2],[-4,0,2])];assert{tuple(p)for atom,p,ep in fund(r,3)}=={(-2,3,3),(-1,4,3)};assert all(ep==[-5,4,3]for atom,p,ep in fund(r,3));assert all(ep[0]<=-5 for atom,p,ep in fund(a,3))
for atom in'DCVU':assert[(i,c)for i,(q,h,c)in enumerate(G[atom]['reads'])if q==-1-1j]==[(2,'L')]
for atom in'DVU':
 for slot in I[atom]:assert slot.imag-G[atom]['p'].imag<=0
for atom in'DCVU':
 for q,(c,t)in G[atom]['last'].items():
  if c=='R':assert q.imag>=0
for atom in'DVU':assert(rot(3)*G[atom]['p']).real<=0 and(rot(2)*G[atom]['p']).real<=0
assert(rot(3)*G['C']['p']).real==-1
# Exact six branch interfaces are supplied by the prior signed three-C reserve.
B=json.loads((R/'C4_foreign_original_hook_loss_2026-10-24/C4_original_hook_loss.json').read_text())['theorem_B_all_C4_original_hook_loss'];bindings=[]
for source in'FQB':
 for branch in['unspent','paired']:
  name=('F_'if source=='F'else'QB_')+branch;field=fields[name];b=next(z for z in B['source_branch_cases']if z['source']==source and z['C3_state_branch']==('N2_paired'if branch=='paired'else branch));assert field<={complex(*q)for q in b['all_current_at_S4_start']}
  protected={-1-1j,-2-1j}if source=='F'else HK;au=next(z for z in J['all6_source_branch_bindings']if z['source']==source and z['C3_branch']==branch);assert au['joint_field']==name and au['protected_hook']==list(map(xy,sort(protected)));bindings.append(au)
O=dict(status='PASS source-only joint ordinary-C4 CURRENT reserve and one-next-FOREIGN Q/B hook transfer',manifest=sha(mf),script=sha(S),all480_rows=reports,all6_bindings=bindings,CORE_capture_support=core,marker_owned_true_inputs=marker,dependencies=m['dependencies'],analytic_review=[
'All source fields are genuine last-R external outputs of the actual F/Q/B source. The signed three-C theorem supplies old13 in both branches and all15 if unspent; Q/B hook maturity supplies the two additional originals. The fourth C is input-free and every external EXIT-CORE position has an actual first-read requirement, so it cannot silently absorb one of these current identities.',
'At the earliest joint loss during the S4 DVU rail, every other selected identity is still CURRENT at consumer ENTRY. All8 external BLACK roles per tag are reconstructed, including marker-owned CORE captures. Four distinct joint fields give480 rows: inactive sector, actual held-field ENTRY-CORE/first-R conflict, or precisely five labels at the two stated U heads. Simultaneous true inputs are allowed and are not falsely rejected as color conflicts.',
'The source-only f01 hole proof is independent of any final recipient: N2/C3 earliest BLACK funding is blocked; the two real W r repairs remain alive CORE until the next actually executed ordinary L2 deletes them; no later W/C4 repair is reachable. At every possible S4 hole producer head y>=3, earlier old13 loss would force a RAW EXIT y<=2 and cannot return north within this S rail. Thus the held old13 at the producer is independently recovered, not assumed from the new reserve.',
'No completed S4 a producer remains; the sole r producer U(-4,4,S) needs a at L14, but W a births exit x<=-5 and W/C4/S cannot increase x to that head. Consequently r is WHITE at completed S4 cuts and a is WHITE specifically at that U entry. The other gate U(-5,3,S) first needs r at L1. Both fail within RAW. A failed U may already have partially consumed another tag or written r; only completed marked cuts are asserted.',
'At Q/B next-FOREIGN ENTRY, allfour SAME hook originals are therefore unconditionally CURRENT under the stated actual language. The signed b961 first-physical-deletion exclusion and all15 exit-CORE checks may now be invoked ONCE, giving CURRENT at next RAW EXIT and physically SAME BLACK through its real supplied M. The prior conditional b961 result is unchanged; the new source-only lemma supplies exactly its missing ENTRY premise.',
'No persistence of the paired nine new outputs, arbitrary S/E continuation, E5 guarantee, further-FOREIGN iteration, whole-field equality, U ancestry, proxy simplicity, global first contact, rail-length bound, language coverage or capture is asserted. The actual subsequent completed context is required for marker ownership; no unexecuted marker is treated as a physical deletion.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print([(r['name'],r['counts'])for r in reports]);print(sha(S.with_suffix('.json')))
