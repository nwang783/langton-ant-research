from pathlib import Path
from fractions import Fraction as F
from math import floor,ceil
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'old_V_all_tail_total2_young_field_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='32b9144239d1e42e5630d5cd3de02b09dfe9afb70f995d9525dab3d9532f1987';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
ref=json.loads((D/'V_K2.json').read_text())
for f,h in ref['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,center,xy=[ns[k]for k in['W','M','K','tr','rot','center','xy']];G={a:tr(W[a])for a in W};CTX={a:tr(W[a]+M)for a in W};tags={0j,1+0j,2+1j,2+2j};det=lambda a,b:int(a.real*b.imag-a.imag*b.real)
def chord(a):return center(0j,0),center(G[a]['p'],G[a]['h'])
a,b=chord('V');u=b-a;geo=[]
for A in'DCVU':
 c,d=chord(A);v=d-c;dd=det(u,v);corners=[((F(int((a+ss*u-c-tt*v).real),2)),F(int((a+ss*u-c-tt*v).imag),2))for ss in[0,1]for tt in[0,1]];bounds=[(floor(min(p[k]for p in corners)),ceil(max(p[k]for p in corners)))for k in[0,1]]
 rr=next(z for z in ref['all4_exact_rational_source_target_boxes']if z['actor']==A);assert rr['rational_corners']==[[[q.numerator,q.denominator]for q in p]for p in corners]and rr['integer_bounds']==list(map(list,bounds))and rr['parallel']==(dd==0)
 for x in range(bounds[0][0],bounds[0][1]+1):
  for y in range(bounds[1][0],bounds[1][1]+1):
   if(x+y)%2:continue
   p=complex(x,y);q=c+2*p-a
   if dd:
    s,t=F(det(q,v),dd),F(det(q,u),dd)
    if not(0<=s<1 and 0<t<=1):continue
   else:
    if det(q,u):continue
    s=F(0);t=F(-int(q.real),int(v.real))if v.real else F(-int(q.imag),int(v.imag))
    if not(0<t<=1 and q+float(t)*v==0):continue
   cuts=[]
   for g in tags:
    z=g-p;ff=next(([e[2],j]for j,e in enumerate(CTX[A]['reads'])if e[0]==z),None)
    if z in K or ff and ff[0]=='R':cuts.append((xy(g),xy(z),z in K,ff))
   assert cuts and y<=-1
   row=next(z for z in ref['all5_outgoing_owned_TOTAL2_N_geometries_and_CURRENT_field_cuts']if z['actor']==A and z['ENTRY']==[x,y,0]);assert row['old_outgoing_s']==str(s)and row['new_positive_t']==str(t)
   assert {str(z)for z in cuts}=={str((v['SAME_CURRENT_tag'],v['local'],v['ENTRY_CORE'],v['actual_first']))for v in row['same_original_fourtag_ENTRY_cuts']}
   geo.append([A,x,y,str(s),str(t),cuts])
assert {(z[0],z[1],z[2])for z in geo}=={('D',-1,-1),('C',-1,-1),('V',-1,-3),('U',0,-4),('U',0,-2)}
fore=[]
for g in tags:
 for A in'FQB':
  for q,black in CTX[A]['req'].items():
   if not black or q in K:continue
   p=g+q;e=p-G[A]['p'];h=(2+G[A]['h'])%4;assert h==0 and e.imag>=g.imag>=0
   r=next(z for z in ref['all188_true_FOREIGN_age2_marker_inclusive_input_to_N_EXIT_y_bounds']if z['FOREIGN']==A and z['SAME_source_tag']==xy(g)and z['true_input']==xy(q));assert r['ENTRY']==[*xy(p),2]and r['actual_N_RAW_EXIT']==[*xy(e),h]
   tick=next(j for j,ev in enumerate(CTX[A]['reads'])if ev[0]==q);assert r['actual_owner']['context_tick0']==tick
   fore.append([A,xy(g),xy(q),[*xy(e),h],tick])
assert len(fore)==188
Y=json.loads((R/'old_V_young_FOREIGN_ports_total3_transfer_2026-10-24/young_ports.json').read_text());assert ref['all128_signed_generic_fourheading_firstloss_rows_copied_without_TOTAL3_conclusion']==Y['all128_full_four_heading_first_CURRENT_loss_roles'];loss=[]
for z in ref['all8_possible_firstloss_ports_and_TOTAL2_normal_cuts']:
 k=z['actual_firstloss'];assert k in Y['all8_firstloss_ports_set_equal_signed0af'];h=k['ENTRY'][2];e=k['RAW_EXIT'];assert h==3 or(h==0 and e[1]>=0);loss.append([k,z['route']])
assert len(loss)==8 and len([z for z in loss if z[0]['ENTRY'][2]==3])==3
c=G['C'];ek={c['p']+rot(c['h'])*k for k in K};assert len(ek-K)==3 and all(c['req'][p]is False for p in ek-K);assert len(ek&K)==2 and all(c['req'][p]is True for p in ek&K)
out=dict(status='PASS old-V TOTAL2 arbitrary ordinary suffix slice only, true FOREIGN ages0/1/2',manifest=sha(MF),script=sha(S),five_rational_geometries=geo,all188_true_FOREIGN_age2_exit_bounds=fore,all8_stopped_loss_ports=loss,analytic_review=[
'Four rational corrected-center parallelograms independently yield exactly five outgoing-owned N-facing targets, including the parallel V onset at the old start. Old terminal belongs to its next owner; new entry is not positive onset. Each target y is negative and at least one of the four SAME source tags is in ENTRY CORE or a first-WHITE demand.',
'Actual V/VC/VCC source completion and true FOREIGN ages are retained. Preforeign signed r5/B4/C-bud3 plus actual own-tail identity preservation supplies genuine CURRENT funding. The age0/1 import is only the no-TRUEinput coordinate theorem, not its TOTAL3 conclusion; CURRENT independently excludes CORE/WHITE touches, giving complete context MISS.',
'At true age2 the actual FOREIGN is S-facing and exits N. All188 real external BLACK input placements including marker-owned absorption have exit y>=tag y>=0. No C remains before TOTAL2, and every N base raises y. Therefore any such loss cannot precede any of the five negative-y targets. This is target-conditioned COMPLETE context MISS, not postforeign maturity.',
'The signed all128-heading table is intrinsic first-loss geometry, field and earlier-source contact logic. Its eight survivors and exclusions do not require TOTAL3 or true FOREIGN age2. After proven complete FOREIGN MISS, W-facing losses are clock3 and too late; five N2 losses exit y0/1 and cannot descend to the target. C has exactly three external first-WHITE exitCORE sites and two already ENTRYCORE sites, no silent external capture.',
'At GLOBAL first contact the earlier old-source chord contact alternatives are unavailable, including repeated old endpoints after the intervening FOREIGN. TRUE simultaneous inputs are not excluded merely for being BLACK. CURRENT loss can be marker capture before physical death; actual RAW exits, not delayed death cuts, control every endpoint argument.',
'No TOTAL3 conclusion, n>=3 pair reserve, old G8 age crossing FOREIGN, terminal-DCC parsing, fixed tail index, through-contact survival or complete arbitrary-tail simplicity is promoted. Only old outgoing V TOTAL2 is closed.'
],dependencies=ref['dependencies'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
