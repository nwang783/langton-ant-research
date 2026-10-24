from pathlib import Path
from collections import Counter
from fractions import Fraction
import json,hashlib,math
S=Path(__file__);R=S.parents[1];D=R/'firstpost_F_DC_proper_piece_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='210cc8f238c61f7018b4ae46d42a8f7f256c14f515695e944a4e957dfc86a802';mf=json.loads(MF.read_text())
for k,b in [('files',D),('dependencies',R)]:
 for f,h in mf[k].items():assert sha(b/f)==h
J=json.loads((D/'F_DC_piece.json').read_text());ns={'__file__':str(S.with_name('check_first_Q_B_DC_source_independent.py'))};exec(Path(ns['__file__']).read_text().split('oldD=R/')[0],ns)
W,M,K,tr,rot,xy,center,meet,pieces,raw,ctx,I,first,bad,bindbad=[ns[k]for k in('W','M','K','tr','rot','xy','center','meet','pieces','raw','ctx','I','first','bad','bindbad')]
F0,F1=-7-3j,-1-1j;common=2+0j;CO={2+0j,2+1j,1+2j};FT={-3-1j,-2-1j}
fraw=tr(W['F']);assert [(a-2*fraw['p'])/rot(fraw['h'])for ab in pieces('F')for a in ab]==[F0,F1]
def chord(a,p=0j,h=0):
 z=tr(W[a],p,h);return center(p,h),center(z['p'],z['h'])
det=lambda a,b:int(a.real*b.imag-a.imag*b.real)
def hit(a,b,c,d):
 u,v,w=b-a,d-c,c-a;den=det(u,v)
 if den:
  s,t=Fraction(det(w,v),den),Fraction(det(w,u),den)
  return(s,t)if 0<=s<=1 and 0<=t<=1 else None
 if det(w,u):return None
 axis=(lambda q:q.real)if v.real else(lambda q:q.imag)
 lo,hi=sorted([Fraction(int(axis(a-c)),int(axis(v))),Fraction(int(axis(b-c)),int(axis(v)))]);lo=max(Fraction(0),lo);hi=min(Fraction(1),hi)
 if lo>hi:return None
 p=c+float(lo)*v;ax=(lambda q:q.real)if u.real else(lambda q:q.imag);ss=Fraction(ax(p-a)).limit_denominator()/int(ax(u));return ss,lo,hi
windows=json.loads((R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json').read_text())['all44_exact_source_target_C_window_rows'];closed={};proper={};terminal={}
for a in'DCVU':
 for h in range(4):
  c,d=chord(a,h=h);corn=[(u-v)/2 for u in(F0,F1)for v in(c,d)]
  for x in range(math.floor(min(p.real for p in corn)),math.ceil(max(p.real for p in corn))+1):
   for y in range(math.floor(min(p.imag for p in corn)),math.ceil(max(p.imag for p in corn))+1):
    if(x+y+h)%2:continue
    hh=hit(F0,F1,c+2*complex(x,y),d+2*complex(x,y))
    if hh is None or hh[1]<=0:continue
    key=(a,x,y,h);closed[key]=hh
    if hh[0]==1:terminal[key]=hh
    else:
     kk=[k for w in windows if w['source_class']=='Fprefix'and w['contact_atom']==a for k in w['allowed_C_counts_before_contact_ENTRY']if(-k)%4==h];assert len(kk)==1;proper[key]=(kk[0],hh)
assert(len(closed),len(terminal),len(proper))==(62,20,42)
for field,domain in [('all62_closed_F_contact_geometries',closed),('all20_FORE_EXIT_owned_by_outgoing_b1_D_C',terminal),('all42_proper_F_owned_angle_geometries',proper)]:
 refs={(r['actor'],*r['pose']):r for r in J[field]};assert set(refs)==set(domain)
 for key,v in domain.items():
  hh=v[1]if field.startswith('all42')else v;r=refs[key];assert(r['actual_old_s'],r['actual_new_t'])==(str(hh[0]),str(hh[1]))and r['same_direction_parallel_interval']==([str(x)for x in hh[1:]]if len(hh)==3 else None)
  if field.startswith('all42'):assert r['actual_post_FOREIGN_C_clock']==v[0]
assert all(y<=-2 and x<=1 for(a,x,y,h),(k,_)in proper.items()if k==4)and all(y<=-1 for(a,x,y,h),(k,_)in proper.items()if k==5)
# Fresh regeneration of exactly the plain-BASE projection, never its old future-tail filter.
G=json.loads((R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];IDS=(0,1,4,5,6,7,8,9);ix={i:j for j,i in enumerate(IDS)};COUNT={tuple(map(int,l.split()[:8]))for l in(R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv').read_text().splitlines()};HB={tuple(map(int,l.split()[:7]))for l in(R/'core_periodicity_new/chronology_dcuv/protected_patch2.tsv').read_text().splitlines()}
refs={(r['actual_full_source'],r['consumer'],r['true_full_source_ENTRY_age'],tuple(r['input_cell'])):r for r in J['fresh_D_common_normal_reserve']['all64_source_D_DC_to_plain_BASE_common_queries']};seen=set();cc=Counter();ports=[]
for si in(0,1):
 name=G[si]['name'];z=tr(''.join(W[a]for a in name));assert z['last'][common]==('R',8)
 for age in range(4):
  h=(-age)%4
  for ci in(0,4,7):
   consumer=G[ci]['name'];assert consumer in'DVU'
   for slot,inp in enumerate(G[ci]['inputs']):
    p=common-rot(h)*complex(*inp);x,y=xy(p);key=(ix[si],ix[ci],x,y,h,2,0,age);r=refs[(name,consumer,age,tuple(inp))];seen.add((name,consumer,age,tuple(inp)))
    if age<name.count('C'):why='full_source_not_yet_completed'
    elif age<3:why='signed1344_common_atomic_ENTRY_minimum3'
    elif(x+y+h)%2:why='sector'
    elif key in COUNT:why='signed_COUNT5'
    else:why='exact_E3_plain_port';ports.append((name,consumer,p,h))
    assert r['reason']==why and r['pose']==[x,y,h]and r['key']==list(key)and r['input_slot0']==slot;cc[why]+=1
assert len(seen)==len(refs)==64 and len(ports)==5 and sum(cc.values())==64
for name,a,p,h in ports:
 if a=='D':assert name=='D'and center(p,h)==chord('D')[1]
 elif p==-1:assert hit(*chord('D'),*chord(a,p,h))==(Fraction(1,2),Fraction(1,2))
 else:
  assert(a,p,h)==('V',1j,1)
  for b in'DCVU':ss,tt=hit(*chord(a,p,h),*chord(b,1+1j,0));assert 0<ss<1 and 0<tt<1
norm={}
for a in'DVU':
 for slot in I[a]:
  for h in(0,3):
   p=common-rot(h)*slot;z=tr(W[a],p,h);assert z['p'].imag>=0
   if h==0:assert z['p'].real>=2
   norm[(a,tuple(xy(slot)),h)]=(p,z)
assert len(norm)==16
for r in J['fresh_D_common_normal_reserve']['all16_N4_W5_common_input_RAW_normal_bounds']:
 p,z=norm[(r['atom'],tuple(r['input']),r['h'])];assert r['pose']==xy(p)+[r['h']]and r['RAW_EXIT']==xy(z['p'])+[z['h']]
refs={(r['source'],tuple(r['SAME_F_tag']),r['consumer'],tuple(r['input']),tuple(r['pose'])):r for r in J['all128_coupled_F46_F47_roles_with_NO_beta_anchor']};seen=set();pc=Counter();esc=set()
for src,anchors in [('D',{common}),('C',CO)]:
 for tag in FT:
  for a in'DVU':
   for slot in I[a]:
    for h in range(4):
     p=tag-rot(h)*slot;z=tr(W[a],p,h);key=(src,tuple(xy(tag)),a,tuple(xy(slot)),tuple(xy(p)+[h]));seen.add(key);r=refs[key];assert r['RAW_EXIT']==xy(z['p'])+[z['h']]and r['owner']['context_tick0']==first(ctx[a],slot)[1]
     touch={q for q in anchors if(q-p)/rot(h)in ctx[a]['req']}
     if int(p.real+p.imag+h)%2:why='sector'
     elif touch:
      assert touch=={complex(*v['anchor'])for v in r['independently_CURRENT_anchor_touches']};why='would_touch_independent_same_source_reserve_before_target'
     elif bad(a,p,h,FT):why='SAME_other_F_tag_ENTRY_CORE_or_first_WHITE';bindbad(r['SAME_F_colour_conflicts'],bad(a,p,h,FT),a)
     elif hit(F0,F1,*chord(a,p,h))is not None or hit(*chord(src),*chord(a,p,h))is not None:why='earlier_actual_F_or_source_proxy_contact'
     else:assert h==0 and z['p']==-1-1j and(a,p)in{('D',-2-2j),('V',-2-4j),('U',-1-5j)};esc.add((a,tuple(xy(p))));why='N0_unreachable_or_N4_exit_y_minus1_cannot_reach_negative_y_N4_W5_target'
     assert why==r['route'];pc[why]+=1
assert seen==set(refs)and len(seen)==128 and len(esc)==3
# Genuine full source/output inventory, independently regenerated from actual words and finalK.
for i in IDS:
 name=G[i]['name'];z=tr(''.join(W[a]for a in name));exitK={z['p']+rot(z['h'])*q for q in K};outputs={q for q,(ch,t)in z['last'].items()if ch=='R'and q not in exitK};assert outputs=={complex(*p)for p in G[i]['outputs']}
upper=J['source_D_four_C_deleted_CORE_upper_guard'];g=-1+0j;target=-1-3j;assert(g-target)in I['U']and first(ctx['U'],g-target)==('L',23)
for src in('D','DC'):
 z=tr(''.join(W[a]for a in src));assert z['last'][g]==('L',1)and g not in{complex(*p)for p in G[0 if src=='D'else 1]['outputs']}
refs={(r['actual_full_producer'],tuple(r['output']),r['true_full_source_ENTRY_age']):r for r in upper['all340_existing_producer_specific_upper_age0_to4_exclusions']};seen=set();uc=Counter()
for i in IDS:
 for op in G[i]['outputs']:
  for age in range(5):
   h=(-age)%4;p=complex(*op)-3j*rot(h);x,y=xy(p);key=(ix[i],ix[7],x,y,h,*op,age);hb=(i,7,x,y,h,*op);r=refs[(G[i]['name'],tuple(op),age)];seen.add((G[i]['name'],tuple(op),age))
   if age<G[i]['name'].count('C'):why='producer_not_completed_before_TRUE_input'
   elif(x+y+h)%2:why='sector'
   elif hb in HB:why='signed_HB'
   else:assert key in COUNT;why='signed_COUNT5'
   assert r['route']==why and r['full_U_pose']==[x,y,h]and r['counted_key']==list(key)and r['HB_key']==list(hb);uc[why]+=1
assert seen==set(refs)and len(seen)==340
old=json.loads((R/'firstpostV_F_piece_first_contact_2026-10-24/F_piece_contact.json').read_text())['all5_proper_Fsource_lower_output_guards'];assert old==J['all5_existing_negative_y_FOREIGN_output_guards'];negative={}
for r in old:
 a=r['atom'];p=complex(*r['head']);h=r['h'];g=complex(*r['initial_SAME_FOREIGN_output_reserve']['postforeign_cell']);loc=(g-p)/rot(h);assert g.imag<0 and p.imag>g.imag and first(ctx[a],loc)[0]=='R'and first(ctx[a],loc)[1]<len(W[a]);negative[(a,*xy(p),h)]=r
beta=1-1j;assert(beta+1j)/rot(3)in K and W['U'][:11]==W['C'][:11]==M
refs={(r['first_ordinary_source'],r['actor'],*r['pose']):r for r in J['all84_first_D_C_proper_F_contact_exclusions']};seen=set();cl=Counter()
for src,held in [('D',{common}|FT),('C',CO|FT)]:
 for key,(k,hh)in proper.items():
  a,x,y,h=key;p=complex(x,y);r=refs[(src,*key)];seen.add((src,*key));assert r['actual_post_FOREIGN_C_clock']==k
  if bad(a,p,h,held):why='independent_source_reserve_and_SAME_F46_F47_CURRENT_colour';bindbad(r['guards'],bad(a,p,h,held),a)
  elif key in negative:why='existing_genuine_negative_y_FOREIGN_output_coordinate_guard';assert r['guard']==negative[key]
  elif(src,a,p,h,k)==('D','U',target,0,4):why='source_D_L1_deleted_CORE_upper_input_max_age4_below5';assert r['guard']==upper
  else:assert(a,p,h,k)==('U',-1j,3,5);why='same_pose_reader_independent_CURRENT_beta_inside_U_ENTRY_CORE';assert r['guard']==J['W5_same_ENTRY_U_reader_beta_lift']
  assert r['route']==why;cl[why]+=1
assert seen==set(refs)and len(seen)==84 and sorted(cl.values())==[1,2,10,71]
reports=['check_first_F_DC_source_independent.json','check_first_F_DC_terminal_C_qualification_independent.json','check_first_Q_B_DC_source_independent.json','check_firstpostV_F_piece_independent.json']
# The immutable manifest binds the original proper-piece report indirectly; only present exact reports below.
reports=[f for f in reports if S.with_name(f).exists()]
for f in reports:assert json.loads(S.with_name(f).read_text())['status'].startswith('PASS')
out=dict(status='PASS original proper F piece with first post-F D/C at GLOBAL first-contact entry',manifest=sha(MF),script=sha(S),geometry=dict(closed=62,outgoing_b1_terminal=20,proper=42),plain_BASE_queries=dict(cc),F_pair_roles=dict(pc),upper_funding_queries=dict(uc),closure_counts=dict(cl),signed_reports={f:sha(S.with_name(f))for f in reports},analytic_review=[
'The64 sourceD/DC-to-plainBASE projection is reconstructed without the old positive-C consumer completion-beforeFORE3 filter. Each hypothetical earlier firstCURRENT-loss BASE ends a real sourceD-to-consumer G8 factor with actual nextM, even if later C tails follow. InitialD has genuine precedingF. Five E3 ports are nonadjacent sourceEXIT/source/actualnextN contacts. No terminalC/DCC target is parsed.',
'SAME sourceD common currentness through3 is extended only by exact N4 x>=2/y>=0 and W5 y>=0 input-exit bounds to the specified target halfplanes. FreshC three-output reserve is independently signed. These independent CURRENT-to-target anchors exclude earlier TRUE input touches, not just entry-color conflicts.',
'All128 coupledF46/F47 roles include marker/CORE absorption. Three N losses exiting(-1,-1) remain real alternatives but cannot precede stipulated N4 y<=-2 or W5 y<=-1 targets. No beta anchor is silently used, no postforeign maturity assigned to F tags, and no through-contact persistence asserted.',
'Exact closed-segment first-positive contact geometry includes collinear onset;20 terminal aliases belong to outgoingb1D/C, not incomingF. Signedanglewindows give42 proper source heads and all actual clocks. Five lower negative-y F guards are source-letter-independent coordinate reserves, not transferred V-state assumptions.',
'Deletedg sourceD L1 physically retires the entry identity; initialD/DC residualO omit it. In the genuine selected G8 factor ending goalU BASE, g is outside goalENTRYK, so an aliveCORE shortcut cannot supply its true external input. Everynew actualfull residual producer is one of8, born atclock>=0;340 exact age0..4 HB/COUNT5 rows exclude allfunding. JO minimum4 alone is explicitly insufficient and unused.',
'W5U at0,-1 has exactly the same physicalENTRY, universalK and actualM11 as signedbeta targetC. All earlier BASE-helper arguments and actualnextM remain valid; terminalC is not parsed. This is a reader-independent ENTRY contradiction, not persistence throughU.',
'Scope is original U-entryG8/FIRSTF/immediateD orC, ordinary suffix and actualfinalM, GLOBALfirst stopping. All84proper labels close; outgoingterminal20 route separate signedsource theorem. Later ordinary sources, anotherFOREIGN, arbitrary-tail simplicity and capture remain open.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')));print(dict(cc),dict(pc),dict(uc))
