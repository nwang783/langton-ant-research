from pathlib import Path
from collections import Counter
import json,hashlib
P=Path(__file__);R=P.parent.parent;D=R/'two_track_UCC_F_return_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'plain_rail_extension_manifest.json';assert sha(mf)=='6d9a85d89ffbf04d4b6c10441a1d2304a5fd663686f05eff8a6d970fd18b3b7d';m=json.loads(mf.read_text())
for n,h in m['files'].items():assert sha(D/n)==h
for n,h in m['dependencies'].items():assert sha(R/n)==h
ref=json.loads((D/'plain_rail_extension.json').read_text());ns={'__file__':str(P.with_name('check_two_track_UCC_F_guard_independent.py'))};exec(Path(ns['__file__']).read_text().split('src,sk,so=')[0],ns);W,M,K,trace,field_geom,xy=[ns[k]for k in('W','M','K','trace','field_geom','xy')];g=-1+0j;raw=lambda z:''.join(W[a]for a in z);source,ek,oo=field_geom(raw('UCC'));assert(source['p'],source['h'])==(-1+5j,2)and source['last'][g]==('L',1)and g not in ek|oo
geom={};south=[];north=[];why=Counter()
for a in'DVU':
 t,k,O=field_geom(W[a]);geom[a]=(t,k,O);assert {p for p,h,c in t['reads'][:6]}==K and all(next(c for p,h,c in t['reads']if p==z)=='L'for z in K);assert sorted(map(xy,O))==list(map(tuple,ref['all_plain_full_geometries'][a]['outputs']))
 for o in sorted(O,key=lambda z:xy(z)):
  ps=g+o;solutions=[]
  if o.real>0:reason='requires_head_right_of_all_S_rail_heads'
  else:
   for v in range(int(-o.real)+1):
    d=int(-o.real)-v;num=5-d-3*v-int(ps.imag)
    if num>=0 and num%4==0:solutions.append(dict(d=d,v=v,u=num//4))
   if not solutions:reason='no_nonnegative_prefix_count_solution'
   elif solutions==[dict(d=0,v=0,u=1)]:reason='unique_prefix_U_contains_forbidden_UCCU'
   else:assert(a,o,solutions)==('U',-1+2j,[dict(d=0,v=1,u=0)]);reason='unique_prefix_V_contains_forbidden_UCCVU'
  why[reason]+=1;south.append(dict(full_plain_source=a,fresh_O_slot=list(xy(o)),required_S_entry=list(xy(ps)),all_possible_prior_rail_count_solutions=solutions,exclusion=reason));pn=g-o;en=pn+t['p'];assert en.imag>=1
  north.append(dict(full_plain_source=a,fresh_O_slot=list(xy(o)),required_N_entry=list(xy(pn)),genuine_full_exit=[*xy(en),t['h']],exit_Y_minus_target_Y=int(en.imag+2)))
assert len(south)==len(north)==16 and south==ref['all16_regenerated_S_residual_origin_rows']and north==ref['all16_N_residual_origins_exit_too_high']
assert sorted(why.values())==[1,2,2,11]
short=[]
for seq,ix in [('UCCU',(70,30)),('UCCVU',(89,1))]:
 t=trace(raw(seq)+M);assert t['conflict'][:2]==ix;short.append([seq,*ix,xy(t['conflict'][2])])
 if seq=='UCCVU':assert t['conflict'][2]==g
# Exact affine coefficient algebra, no finite run bound: deltaD+deltaV=-3; deltaD+3deltaV+4deltaU=-9.
assert all((geom[a][0]['p'],geom[a][0]['h'])==(z,0)for a,z in [('D',1+1j),('V',1+3j),('U',4j)])
ft,ekf,of=field_geom(W['F']);assert(ft['p'],ft['h'])==(-4-2j,2)and min(p.imag for p,h,c in ft['reads'])==-2 and max(z.imag for z in K)<2
# For arbitrary deltaU=u, substitution proves both endpoint equations identically (coefficient and constant).
for u in(0,1):
 dd,dv=2*u,-3-2*u;assert dd+dv==-3 and dd+3*dv+4*u==-9
controls=[]
for z in ref['actual_complete_finite_prefix_controls_with_rail_U']:
 X,Y=z['X'],z['Y'];dd=Y.count('D')-X.count('D');dv=Y.count('V')-X.count('V');du=Y.count('U')-X.count('U');assert dd==2*du and dv==-3-2*du
 drop=lambda w:w.count('D')+3*w.count('V')+4*w.count('U');assert drop(X)==9+drop(Y)>=9
 seq='UCC'+X+'F'+Y;word=raw(seq);pre=trace(word);assert(pre['p'],pre['h'])==(-2j,0);part=trace(word+W['U'][:13]);assert part['conflict']is None
 B={complex(*p)for p in z['complete_initial_black']};assert B=={p for p,b in part['req'].items()if b};B0=set(B);reads_g=[]
 for i,(p,h,c)in enumerate(part['reads']):
  assert(p in B)==(c=='L');B.symmetric_difference_update({p})
  if p==g:reads_g.append((i,c))
 assert reads_g==[(1,'L')]and g not in B and(part['p'],part['h'])==(g,3);full=trace(word+W['U']+M);assert full['conflict']==(len(word)+13,1,g,'L')
 bad={a:next(i for i,c in enumerate(W['U'][:13]+'R')if(W[a]+M)[i]!=c)for a in'DCVUFQB'};assert bad==z['all_seven_impossible_by_current_actual_prefix']and len(part['reads'])==z['successful_actual_reads']
 controls.append(dict(X=X,Y=Y,deltaU=du,seed_mass=len(B0),successful_reads=len(part['reads']),next_actual_R_cell=xy(g),next_board_mass=len(B),all7_conflict_ticks=bad))
assert len(controls)==5 and{z['deltaU']for z in controls}=={-1,0,1}and sum('U'in z['X']and'U'in z['Y']for z in controls)==3
out=dict(status='PASS exact UCC/plain-DVU south/F/plain-DVU north/attempted-U two-track family impossible through targetU13',manifest_sha256=sha(mf),dependencies=m['dependencies'],south16=south,north16=north,south_reason_counts=dict(why),immutable_short_prefixes=short,complete_prefix_controls=controls,analytic_review=['Endpoint equations give deltaD=2deltaU,deltaV=-3-2deltaU and dropX=9+dropY>=9, not the narrower equal-D/V-offset assumption. All orders and unbounded nonnegative counts are covered.','All16 genuine full-output roles regenerated independently. S heads have d+v=-outputx; this exactly bounds the predecessor counts. Unique singleton U or V count vectors force the literal first prefix itself, not merely a chosen ordering. The recycled U q role needs original hole BLACK before R21 and fails UCCVU at89 versus1. V(0,1) is excluded through unique preceding U, not old DV-only first-entry reasoning.','At foreign entry the hole is localy<=-4 below every F RAW read, and at exit its relativey>=2 lies outsideK. N origins all exit at leasty1 and remaining N motion strictly increasesy, so cannot reach targety-2.','Full residual export remains exhaustive: every final-R cell outside exitK is in the enumerated true O; entryK identities are actually deleted in first6 reads of each next fullpacket. No untested core-carried identity can become final external BLACK. No intermediate whiteness or postforeign age law is assumed.','Five actual finite boards including U in both rails and deltaU=-1,0,1 replay completely through targetticks0..12; nextactualR at deleted hole rejects all seven continuations. No completed targetU, proxycontact, otherconnector or general FSA/decidability claim.'])
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(controls)
