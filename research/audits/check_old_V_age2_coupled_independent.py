from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from itertools import product
import json,hashlib,math
S=Path(__file__).resolve();R=S.parents[1];D=R/'old_V_all_tail_foreign_age2_coupled_ports_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='0af992fdc785575d8682735d1e7fee5d3207a6506e525f8e0ed84e365d4ee4ba'
for f,h in json.loads(MF.read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'V_n2.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
# Reconstruct all rational source/actor geometry from independent word chords, not author heads.
lib=S.with_name('check_old_V_age3_horizon_independent.py');ns={'__file__':str(lib)};exec(lib.read_text().split('re={')[0],ns)
W,M,K,tr,rot,center,xy,cross,meet,pieces,G,C,I,ex,cut,geo=[ns[k]for k in('W','M','K','tr','rot','center','xy','cross','meet','pieces','G','C','I','ex','cut','geo')]
RES={0j,1+0j,2+1j,2+2j};B=1+0j;CC=2+1j;bud=2+2j
jr={(r['actor'],*r['ENTRY']):r for r in J['all15_exact_total3_geometries_with_TRUE_age2_not_copied_age3']}
for A,x,y,h,s,t,typ in geo:
 z=jr[A,x,y,h];assert z['true_preFOREIGN_age']==2 and z['TOTAL_ordinary_C']==3 and(z['old_outgoing_s'],z['new_positive_t'])==(s,t)
assert len(jr)==15
births=[]
for src in('V','VC','VCC'):
 zz=tr(''.join(W[a]for a in src));ek={zz['p']+rot(zz['h'])*k for k in K}
 for q in RES:assert zz['last'][q]==G['V']['last'][q]and zz['last'][q][0]=='R'and q not in ek
 births.append((src,[(xy(q),G['V']['last'][q])for q in sorted(RES,key=lambda q:(q.real,q.imag))]))
# Exact integer cone enumeration: split available height between the two rails;
# enumerate N D/V/U and W D/V by height; remaining W-U solved from horizontal displacement.
names=('N_D','N_V','N_U','W_D','W_V','W_U')
def endpoint(e,t):
 dh=int(t.imag-e.imag-1);dx=int(t.real-e.real)
 if dh<0:return []
 res=[]
 for hn in range(dh+1):
  for nd in range(hn+1):
   for nv in range(hn//3+1):
    rem=hn-nd-3*nv
    if rem<0 or rem%4:continue
    nu=rem//4;hw=dh-hn
    for wd in range(hw+1):
     wv=hw-wd;left=nd+nv-wd-3*wv-dx
     if left<0 or left%4:continue
     z=(nd,nv,nu,wd,wv,left//4);assert e+complex(nd+nv,nd+3*nv+4*nu)+1j+complex(-wd-3*wv-4*z[5],wd+wv)==t;res.append(z)
 return sorted(res)
model=lambda z:tuple(z[n]for n in names)
fore_ref={(tuple(r['SAME_original_source_tag']),r['FOREIGN'],tuple(r['true_input'])):r for r in J['all188_actual_FOREIGN_four_tag_input_exit_roles_and_all15_future_endpoint_cases']}
fore=[];short=[];fc=Counter()
for tag,A in product(sorted(RES,key=lambda q:(q.real,q.imag)),'FQB'):
 for slot in sorted(I[A],key=lambda q:(q.real,q.imag)):
  p=tag-rot(2)*slot;e,eh=ex(A,p,2);assert eh==0 and e.imag>=tag.imag
  z=fore_ref[tuple(xy(tag)),A,tuple(xy(slot))];assert z['ENTRY']==[*xy(p),2]and z['actual_N_RAW_EXIT']==[*xy(e),0]
  if(int(p.real+p.imag)+2)%2:assert z['route']=='sector';fc['sector']+=1
  else:
   fc['target_endpoint']+=1;cases={(r['actor'],*r['ENTRY']):r for r in z['all15_target_endpoint_cases']}
   for a,x,y,h,s,t,typ in geo:
    models=endpoint(e,complex(x,y));zr=cases[a,x,y,h];assert sorted(model(m['exact_count_model'])for m in zr['all_exact_count_models'])==models
    for m in models:
     assert sum(m)<=1 and m[1]==m[2]==m[4]==m[5]==0;idx=2+sum(m);short.append((xy(tag),A,xy(p),a,x,y,m,idx))
  fore.append((xy(tag),A,xy(slot),[*xy(p),2],[*xy(e),eh]))
assert len(fore)==len(fore_ref)==188
ss={(tuple(z['source_tag']),z['FOREIGN'],tuple(z['ENTRY']),z['target_actor'],tuple(z['target_ENTRY']),model(z['exact_count_model']),z['actual_contact_RAW_index_derived_not_assumed'])for z in J['all_derived_FOREIGN_consumption_RAW2_RAW3_horizons']}
assert ss=={(tuple(t),A,(*p,2),a,(x,y,3),m,idx)for t,A,p,a,x,y,m,idx in short}
# Every possible ordinary first CURRENT loss is a genuine D/V/U external TRUE input.
# Other simultaneous TRUE inputs are left in; only first-WHITE or ENTRY K is an immediate field cut.
jref={(tuple(z['first_lost_SOURCE_reserve_tag']),z['consumer'],tuple(z['ENTRY']),tuple(z['true_input'])):z for z in J['all128_ordinary_joint_first_CURRENT_loss_roles']};jc=Counter();kept=[];rows=[]
for tag,A,h in product(sorted(RES,key=lambda q:(q.real,q.imag)),'DVU',range(4)):
 for slot in sorted(I[A],key=lambda q:(q.real,q.imag)):
  p=tag-rot(h)*slot;e,eh=ex(A,p,h);z=jref[tuple(xy(tag)),A,(*xy(p),h),tuple(xy(slot))];assert z['actual_RAW_EXIT']==[*xy(e),eh]
  if h not in(0,3):why='not_in_actual_postFOREIGN_N2_or_W3_stages'
  elif(int(p.real+p.imag)+h)%2:why='sector'
  elif any(cut(A,p,h,q)for q in RES-{tag}):why='other_CURRENT_reserve_actual_ENTRY_CORE_or_firstWHITE'
  elif meet(*pieces('V')[0],center(p,h),center(e,eh))is not None:why='earlier_GLOBAL_proxy_contact_with_genuine_old_V_source_not_legitimate_adjacency'
  else:
   kept.append((tag,A,p,h,e,eh))
   if tag==B:assert h==eh==0 and e==2;why='first_B_loss_exact_N2_exit2_0'
   elif tag==CC:assert h==eh==0 and e==3+1j;why='first_C_loss_exact_N2_exit3_1'
   else:assert tag==bud and h==eh==3 and e==2+3j;why='first_bud_loss_W3_exit_y3_above_every_target_y_le2'
  assert why==z['route'];jc[why]+=1;rows.append((xy(tag),A,xy(p),h,why))
assert len(rows)==128 and len(kept)==8
kr={(tuple(z['first_lost_SOURCE_reserve_tag']),z['consumer'],tuple(z['ENTRY']))for z in J['all8_only_ordinary_firstloss_ports']};assert kr=={(tuple(xy(t)),a,(*xy(p),h))for t,a,p,h,e,eh in kept}
# C has no external true inputs. Exactly three external EXIT-K captures require first WHITE;
# the two others are already in incoming K and cannot be a fresh external CURRENT identity.
assert len(I['C'])==0
core=[]
for q in K:
 p=G['C']['p']+rot(G['C']['h'])*q
 if p in K:assert C['C']['req'][p];kind='already_ENTRY_CORE'
 else:assert C['C']['req'][p]is False;kind='external_first_WHITE'
 core.append((xy(p),kind))
assert Counter(z[1]for z in core)==dict(already_ENTRY_CORE=2,external_first_WHITE=3)
future=[];missC=[]
cu=tr(W['C']+W['U']+M);assert cu['bad']is not None
for tag,A,p,h,e,eh in kept:
 if tag==bud:assert e.imag==3>max(z[2]for z in geo);future.append((xy(tag),A,xy(p),'W_y_above_all_targets'));continue
 if tag==B:
  local=(CC-p)/rot(h);assert local not in C[A]['req']and local not in K and(CC-e)/rot(eh)not in K
  hits=[(i,c)for i,(q,hin,c)in enumerate(G['C']['reads'])if q==1j];assert hits[0]==(11,'R');missC.append((A,xy(p),xy(local),hits))
 for a,x,y,hh,s,t,typ in geo:
  for m in endpoint(e,complex(x,y)):
   if tag==CC:assert m==(0,0,0,0,0,0)and(a,x,y)==('U',3,2);why='C_U'
   elif m[0]:assert m==(1,0,0,0,0,0)and(a,x,y)==('U',3,2);why='D_C_U'
   else:assert m[0]==m[1]==m[2]==m[4]==m[5]==0 and m[3]in(0,1);why='real_next_C_own_R11'
   future.append((xy(tag),A,xy(p),a,x,y,m,why))
assert len(future)==20 and len(missC)==3
# Compare each author exact future, retaining unrestricted earlier loss index.
afuture=J['all20_exact_post_firstloss_future_obligations'];assert len(afuture)==20
fkeys=set()
for z in afuture:
 k=z['firstloss'];tag=tuple(k['first_lost_SOURCE_reserve_tag']);A=k['consumer'];p=tuple(k['ENTRY'][:2]);route=z['route']
 if 'all_later_W_heads_y_ge3'in z:fkeys.add((tag,A,p,'W_y_above_all_targets'))
 else:
  a=z['target_actor'];x,y,h=z['target_ENTRY'];why='D_C_U'if route.startswith('actual_D_C')else'C_U'if route.startswith('actual_C_then')else'real_next_C_own_R11';fkeys.add((tag,A,p,a,x,y,model(z['exact_remaining_N_C_W_model']),why))
assert fkeys=={tuple(tuple(v)if isinstance(v,list)else v for v in z)for z in future}
final=[]
for A,x,y,h,s,t,typ in geo:
 cuts=[xy(q)for q in RES if cut(A,complex(x,y),h,q)];assert cuts;final.append((A,x,y,h,cuts))
# Signed TWO/THREE statements cover precisely actual target-index 2/3 with actual final M.
two=json.loads((R/'first_foreign_two_ordinary_simplicity_2026-10-24/manifest.json').read_text());three=json.loads((R/'first_foreign_three_ordinary_simplicity_2026-10-24/manifest.json').read_text());assert 'exactly TWO'in two['theorem']and'THREE immediate ordinary RAW'in three['scope']
report=dict(status='PASS old-V true FIRST-FOREIGN age2/TOTAL ordinary contact3 coupled-port slice',manifest=sha(MF),geometries=geo,source_births=births,foreign_roles=fore,foreign_role_counts=dict(fc),derived_short_horizon_cases=short,joint_counts=dict(jc),all128_joint_classifications=rows,eight_firstloss_ports=[(xy(t),a,xy(p),h,xy(e),eh)for t,a,p,h,e,eh in kept],all20_future_obligations=future,three_B_loss_context_MISS_C=missC,C_capture_partition=core,actual_C_U_conflict=cu['bad'],all15_entry_cuts=final,analytic_review=[
'True age2 and TOTAL3 are independently distinguished: genuine source V/VC/VCC preforeign births r/B/C/bud remain CURRENT by the signed strictly-preforeign bounds and actual source tails. No n>=3 pair-transfer conclusion is imported afterFOREIGN.',
'All188 marker-inclusive foreign true-input placements and every target semigroup are rebuilt. Foreign S entry exits N with y>=the consumed tag; one remaining C and W target y<=2 imply zero or one total ordinary BASE before actor. W-U is solved from x exactly, not bounded by guessed word depth. This derives actual RAW2/RAW3, allowing precisely the respective signed TWO/THREE theorem with the real finalM.',
'If the foreign would read/capture one held tag, its actual short contact is already impossible. ENTRY CORE/first-WHITE cannot match original CURRENT funding. Consequently complete context-MISS is proved BEFORE any ordinary reserve; a recolored replacement is never substituted for the original identity.',
'All128 ordinary earliest-CURRENT-loss roles retain simultaneous true inputs. Other held-tag contradictions use only actual ENTRY CORE or their FIRST WHITE read. A closed oldV chord contact during an earlier loss atom is genuinely earlier, including old terminal: an entire foreign separates source and actor, so it is not legitimate adjacency.',
'The surviving eight ports are three B losses exiting(2,0,N), two C losses exiting(3,1,N), three bud losses exiting(2,3,W). Their index within the suffix is unrestricted. Exact future cones eliminate bud and force C/U conflict after C loss. All three B-loss full contexts genuinely MISS original C and leave it external; next required real C ownR11 at(0,1) demandsWHITE against SAME original C. The alternative D,C,U branch is literal CU; C is not assumed to survive its permitted D loss.',
'C itself cannot silently capture an external CURRENT identity: zero external inputs, three external exitCORE sites firstWHITE and two alreadyENTRYCORE sites. Marker currentness and later physical death remain distinct, and no through-target permanence is claimed.',
'Only the15 old outgoing V geometries at true firstFORE age2/TOTAL3 are closed. Other true ages, total clocks, preforeign source classes, arbitrary-tail global simplicity, produced-input ages, and a secondFOREIGN are outside this result. No false postforeign pair-K2 impossibility is inferred.'
],dependencies=J['dependencies'])
S.with_suffix('.json').write_text(json.dumps(report,indent=2,default=lambda z:xy(z) if isinstance(z,complex) else str(z))+'\n');print(report['status']);print(sha(S.with_suffix('.json')));print(fc,jc,Counter(z[-1]for z in future))
