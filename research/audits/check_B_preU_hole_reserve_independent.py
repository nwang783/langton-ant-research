from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'B_preU_WHITE_hole_shadow_reserve_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='694052de1c37e011b648f8c2bdde69e297b866f9ef69aabe7010ccfbcfe08f89'
for f,h in json.loads(MF.read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'B_ancestry_reserve.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy,center,meet,pieces=[ns[k]for k in('W','M','K','tr','rot','xy','center','meet','pieces')]
def chord(a,p=0j,h=0):z=tr(W[a],p,h);return center(p,h),center(z['p'],z['h'])
def first(a,q):return next((i,c)for i,(p,h,c)in enumerate(tr(W[a]+M)['reads'])if p==q)
I={a:{q for q,b in tr(W[a]+M)['req'].items()if b and q not in K}for a in'DCVU'};assert not I['C']and sum(map(len,I.values()))==8
support={ (r['atom'],tuple(r['actual_final_R_local']),r['R_tick0']):r for r in J['generic36_physical_final_R_support_rows']};seen=set()
for a in'DCVU':
 z=tr(W[a])
 for q,(c,t)in z['last'].items():
  if c!='R':continue
  ky=(a,tuple(xy(q)),t);seen.add(ky);r=support[ky];assert q.imag>=0 and q.real>=-1 and r['initial_N0_write_y_lower_bound']==q.imag and r['initial_W1_write_y_lower_bound']==1+q.real
  if a!='C':assert q.imag<=z['p'].imag and r['S2_RAW_EXIT_minus_write_y']==q.imag-z['p'].imag
  else:assert r['positive_C_atS2_cannot_complete_before_S2_reader']
assert seen==set(support)and len(seen)==36
for a in'DVU':z=tr(W[a]);assert z['h']==0 and z['p'].imag>0 and z['p'].real>=0
assert (tr(W['C'])['p'],tr(W['C'])['h'])==(1j,3)
# Genuine full predecessor grammar and the actual deleted core cell.
pre={}
for full in ['D','DC','V','VC','VCC','U','UC','UCC']:
 z=tr(''.join(W[a]for a in full+'B')+M);ok=z['bad']is None;pre[full]=ok;assert ok==next(r['feasible']for r in J['all8_actual_complete8_to_B_predecessor_queries']if r['full']==full)
assert [a for a,v in pre.items()if v]==['U']
ub=tr(W['U']+W['B']);hole_old=-1+0j;phole=(hole_old-ub['p'])/rot(ub['h']);assert phole==-2-1j and ub['last'][hole_old]==('L',1)
source=tr(W['B']);oldp=source['p']+rot(source['h'])*phole;assert oldp not in source['req']
g=-1-2j;hole=-2j;hook={-2-4j,-1-4j,-4j,-3j};fore=[((a-2*source['p'])/rot(source['h']),(b-2*source['p'])/rot(source['h']))for a,b in pieces('B')];assert fore==[(-5-9j,1-7j),(1-7j,-1-1j)]
assert source['last'][source['p']+rot(source['h'])*g]==('R',67)and source['last'][source['p']+rot(source['h'])*hole]==('L',66)and g not in K and hole not in K
rows={(r['consumer'],tuple(r['input']),r['pose'][2]):r for r in J['all32_B_original_g_first_CURRENT_loss_roles']};seen=set();counts=Counter();gates=[]
for a in'DCVU':
 ctx=tr(W[a]+M)
 for inp in I[a]:
  for h in range(4):
   p=g-rot(h)*inp;ky=(a,tuple(xy(inp)),h);seen.add(ky);r=rows[ky];assert r['pose']==xy(p)+[h]
   if(int(p.real+p.imag)+h)%2:why='sector'
   elif any((q-p)/rot(h)in K or(q-p)/rot(h)in ctx['req']for q in hook):why='would_touch_original_CURRENT_B_hook_before_target'
   elif any(meet(*f,*chord(a,p,h))is not None for f in fore):why='earlier_B_proxy_contact';assert(p,h)!=(0j,0)
   else:why='S2_g_loss_helper_requires_old_U_hole_BLACK';gates.append((a,p,h))
   assert why==r['classification'];counts[why]+=1
assert seen==set(rows)and len(seen)==32 and set(gates)=={('V',-1+1j,2),('U',-2+2j,2)}
for a,p,h in gates:
 assert p.imag>phole.imag and first(a,(phole-p)/rot(h))==(13 if a=='V'else 23,'L');assert first(a,(g-p)/rot(h))==(len(W[a])+1,'L');assert (g-tr(W[a],p,h)['p'])/rot(h)in K
# Full 208 physical R origins, CORE births included; compare both fresh and signed domains.
refs={(r['producer'],r['true_producer_ENTRY_C_clock'],tuple(r['actual_final_R_local'])):r for r in J['all208_B_h_last_R_origins_freshly_reconstructed_without_simplicity']};older=json.loads((R/'Q_B_hook_MISS_first_contact_2026-10-24/five_MISS.json').read_text());oldrefs={(r['producer'],r['true_producer_ENTRY_C_clock'],tuple(r['actual_final_R_local'])):r for r in older['all208_B_CORE_inclusive_last_R_origins']};seen=set();ct=Counter();surv=[];cuts=Counter()
for a in'DCVU':
 raw=tr(W[a]);ctx=tr(W[a]+M)
 for clock in range(6):
  if a=='C'and clock==5:continue
  h=(-clock)%4
  for slot,(c,t)in raw['last'].items():
   if c!='R':continue
   ky=(a,clock,tuple(xy(slot)));seen.add(ky);r=refs[ky];p=hole-rot(h)*slot;ep=tr(W[a],p,h);assert r['pose']==xy(p)+[h]and r['RAW_EXIT']==xy(ep['p'])+[ep['h']]and r['R_tick0']==t
   if(int(p.real+p.imag)+h)%2:why='sector'
   elif clock==0 and p.imag<0:why='initial_N0_head_below0'
   elif clock==1 and p.imag<1:why='initial_W1_head_below1'
   elif any((q-p)/rot(h)in K or(q-p)/rot(h)in ctx['req']for q in hook):why='would_touch_CURRENT_original_hook_before_target'
   elif any(meet(*f,*chord(a,p,h))is not None for f in fore):why='earlier_actual_FOREIGN_proxy_contact';assert(p,h)!=(0j,0)
   else:
    why='last_R_endpoint_obligation';loc=(g-p)/rot(h);assert loc in K or ctx['req'].get(loc)is False
    cut='CURRENT_g_in_producer_ENTRY_CORE'if loc in K else'SAME_BLACK_g_vs_producer_first_WHITE';cuts[cut]+=1;surv.append(ky)
    rr=next(rr for rr in J['all10_old_origin_residues_cut_by_new_g_field']if (rr['original_CORE_inclusive_R_origin']['producer'],rr['original_CORE_inclusive_R_origin']['true_producer_ENTRY_C_clock'],tuple(rr['original_CORE_inclusive_R_origin']['actual_final_R_local']))==ky);assert rr['cut']==cut and rr['producer_local_g']==xy(loc)
    if loc in ctx['req']:
     tt,ch=first(a,loc);assert rr['actual_first']==[ch,tt]and rr['actual_owner']['context_tick0']==tt
   assert why==r['classification']==oldrefs[ky]['classification'];ct[why]+=1
assert seen==set(refs)==set(oldrefs)and len(seen)==208 and len(surv)==10 and cuts=={'CURRENT_g_in_producer_ENTRY_CORE':4,'SAME_BLACK_g_vs_producer_first_WHITE':6}
targets=[]
for row in J['all4_proper_B_hook_MISS_entry_cuts']:
 t=row['owner_aware_target'];a=t['atom'];p=complex(*t['head']);h=t['h'];assert t['foreign']=='B'and t['actual_outgoing_owner']=='Btail'and t['heading_compatible_C_counts']==[5]
 assert all((q-p)/rot(h)not in K and(q-p)/rot(h)not in tr(W[a]+M)['req']for q in hook)
 witness=[]
 for tag,col in [(g,True),(hole,False)]:
  loc=(tag-p)/rot(h);ctx=tr(W[a]+M)
  if loc in K and not col or loc in ctx['req']and ctx['req'][loc]!=col:witness.append(tag)
 assert witness and set(map(tuple,[xy(q)for q in witness]))=={tuple(r['physical_guard'])for r in row['guard_contradictions']};targets.append([a,xy(p),h])
assert len(targets)==4
out=dict(status='PASS B genuine pre-U WHITE endpoint reserve, CURRENT g and WHITE h through C5 before CLOSED-B contact ENTRY',manifest=sha(MF),script=sha(S),physical_final_R_rows=36,predecessors=pre,g_loss_counts=dict(counts),h_origin_counts=dict(ct),new_g_cuts=dict(cuts),targets=targets,analytic_review=[
'Generic negative physical-WHITE endpoint reserve uses the LAST actual R needed to fund BLACK at an S2 reader ENTRY. All36 RAW final-R sites include active CORE births. N0/W1 support is nonnegativey; a completed S2 zero-C writer exits at or below the written site and remaining S motion cannot rise to the higher reader. A C at S2 cannot complete before another S2 entry. This is an endpoint-conditioned fact, not permanent whiteness or proxy simplicity.',
'All eight actual full-packet predecessors of FIRSTB rebuilt; only plainU can occur. Actual U L1 deletes its entry-core cell and both remaining U and B miss it. This gives physical WHITE p-2,-1 at B exit, independently of any initial color or residual-output interpretation.',
'All32 earliest g CURRENT-loss input/marker roles reconstructed. Hook entryCORE, WHITE and TRUE-input contacts are not ignored. Before first nonadjacent CLOSED-B contact the signed same-hook reserve excludes these; genuine closed contact includes the terminal vertex. No classified contact is legitimate initial B-to-b1 adjacency. The only remaining V/U S2 gates require p BLACK at ownL13/23. Throughclock5 S means2, so the generic endpoint reserve blocks them before g RAWexitCORE capture.',
'Every earlier h funding RAW is complete before the protected entry. Fresh208-role cover equals the signed cover exactly, retaining all CORE writes and Ccompletion deadlines. All10 survivors contradict the NEW independently protected g at producer entry: six firstWHITE, four entryCORE. Thus h is physicallyWHITE, while g is SAME CURRENT, at the protected entry. Earlier ordinary-ordinary selfcontacts are allowed; no fresh-donor age or global proxy simplicity is used.',
'Four properB hookMISS targets are excluded by their actual entry/first-read g/h requirements. The guards stop at first CLOSED-B contact ENTRY and C5. They do not assert through-contact CURRENT, indefinite WHITE, other foreign cases or arbitrary-tail simplicity. This is a stronger B-only alternate route, not a rewrite of signede329.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
