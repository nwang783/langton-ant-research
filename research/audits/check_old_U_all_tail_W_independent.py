from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib,math,cmath
S=Path(__file__);R=S.parents[1];D=R/'old_U_all_tail_W_pair_hole_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'manifest.json';assert sha(mf)=='75c9da92fc3723864d623ca214e524f8e43839b42d4a662faa430990165fbd2f';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'W_pair_hole.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,center,xy,meet,cross=[ns[k]for k in('W','M','K','tr','rot','center','xy','meet','cross')];G={a:tr(W[a])for a in W};C={a:tr(W[a]+M)for a in W};star={0j,1j,1+0j,1+1j};left={0j,1j};d=1+1j;t=1+2j;s=1+3j;pair={d,t};g=2j
pose=lambda p,h:[*xy(p),h]
def touch(a,p,h,qs):return{q for q in qs if (q-p)/rot(h)in K or(q-p)/rot(h)in C[a]['req']}
def conflicts(a,p,h,qs):return{q for q in qs if(q-p)/rot(h)in K or C[a]['req'].get((q-p)/rot(h))is False}
def chord(a,p,h):return center(p,h),center(p+rot(h)*G[a]['p'],(h+G[a]['h'])%4)
I={a:{q for q,b in C[a]['req'].items()if b and q not in K}for a in W};RR={a:{q:v for q,v in z['last'].items()if v[0]=='R'}for a,z in G.items()}
assert sum(len(I[a])for a in'FQB')==47
# Derive every real true input, checking that marker-only true inputs become CORE.
marker=[]
for a in W:
 z=G[a];ek={z['p']+rot(z['h'])*q for q in K}
 for q in I[a]:
  if q not in z['req']:assert q in ek;marker.append((a,xy(q)))
arm=[];armcounts=Counter();ak=[]
for n in range(4):
 h=(-n)%4
 for a in'FQB':
  for q in sorted(I[a],key=lambda z:(z.real,z.imag)):
   p=t-rot(h)*q;au=next(z for z in J['all188_FOREIGN_arm_input_roles']if z['FOREIGN']==a and z['ENTRY']==pose(p,h))
   if(int(p.real+p.imag)+h)%2:why='sector'
   elif touch(a,p,h,star):why='star'
   else:
    why=f'age{n}';ak.append((n,a,p))
    if n==0:
     if a in'FQ':assert p.imag-p.real<4
     else:
      assert p==3+7j
      # N base semigroup from real U exit: x=D+V, y=D+3V+4U.
      models=[(dd,v,u)for dd in range(4)for v in range(4)for u in range(2)if dd+v==3 and dd+3*v+4*u==3];assert models==[(3,0,0)]and tr(W['D']+W['B']+M)['bad']
    elif n==1:
     assert p==2+7j and p.imag-p.real==5
     assert all((rot(3)*G[b]['p']).imag-(rot(3)*G[b]['p']).real>=2 for b in'DVU')
    else:
     qq=(s-p)/rot(h);fr=next((c,i)for i,(v,hh,c)in enumerate(C[a]['reads'])if v==qq);assert fr[0]=='R'and fr[1]<len(W[a]);assert au['genuine_preFOREIGN_bud_WHITE_contradiction']['first']==list(fr)
   armcounts[why]+=1;arm.append((n,a,pose(p,h),why))
assert len(arm)==188 and len(ak)==13 and armcounts['sector']==94 and armcounts['star']==81
# Fresh exact outgoing-owned contact geometry.
angles=json.loads((R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json').read_text())['all44_exact_source_target_C_window_rows'];src=chord('U',0j,0);geom=[];lk=[]
for a in'DCVU':
 ar=next(z for z in angles if z['source_class']=='preFOREIGN_ordinary'and z['source_atom']=='U'and z['contact_atom']==a);assert[k for k in ar['allowed_C_counts_before_contact_ENTRY']if(2-k)%4==3]==[3]
 c,e=chord(a,0j,3);corners=[(ss-tt)/2 for ss in src for tt in(c,e)]
 for x in range(math.floor(min(p.real for p in corners)),math.ceil(max(p.real for p in corners))+1):
  for y in range(math.floor(min(p.imag for p in corners)),math.ceil(max(p.imag for p in corners))+1):
   if(x+y+3)%2:continue
   p=complex(x,y);hit=meet(*src,c+2*p,e+2*p)
   if hit is None or not(0<=hit[0]<1 and 0<hit[1]<=1):continue
   au=next(z for z in J['all18_exact_outgoing_owned_W_geometries']if z['actor']==a and z['ENTRY']==pose(p,3));bad=conflicts(a,p,3,left);assert[str(hit[0]),str(hit[1])]==[au['old_source_parameter'],au['new_positive_parameter']];assert{tuple(xy(q))for q in bad}=={tuple(z['SAME_CURRENT_BLACK'])for z in au['SAME_LEFT_contradictions']};geom.append((a,pose(p,3),str(hit[0]),str(hit[1]),len(bad)))
   if not bad:lk.append((a,p))
assert len(geom)==18 and len(lk)==6 and max(p.imag for a,p in lk)==3
# Pair loss retains genuine simultaneous true inputs; other member only ENTRY-held.
loss=[];pending=[];losscount=Counter()
for tag in sorted(pair,key=lambda z:(z.real,z.imag)):
 other=(pair-{tag}).pop()
 for h in range(4):
  for a in'DVU':
   for q in sorted(I[a],key=lambda z:(z.real,z.imag)):
    p=tag-rot(h)*q;ep=p+rot(h)*G[a]['p'];eh=(h+G[a]['h'])%4;au=next(z for z in J['all64_earlier_first_PAIR_CURRENT_loss_roles']if z['SAME_first_lost_pair_tag']==xy(tag)and z['consumer']==a and z['ENTRY']==pose(p,h));assert au['RAW_EXIT']==pose(ep,eh)
    if(int(p.real+p.imag)+h)%2:why='sector'
    elif meet(*src,*chord(a,p,h))is not None:why='earlier_contact'
    elif touch(a,p,h,left):why='independent_LEFT'
    elif conflicts(a,p,h,{other}):why='held_other'
    else:
     why='N_simultaneous'if h==0 else'S_Jordan';pending.append((tag,a,p,h,ep))
     if h==0:assert a=='U'and p==2 and ep==2+4j and pair<={p+rot(h)*qq for qq in I[a]}
     else:assert h==2 and tag==t and ep==2j
    loss.append((xy(tag),a,pose(p,h),why));losscount[why]+=1
assert len(loss)==64 and len(pending)==5
# Rebuild actual bridge geometry and principal turn signs from vectors.
bridge=[1+5j,3+3j,1+1j,-1+3j];sourcepart=(-1+3j,src[1]);vec=[bridge[i+1]-bridge[i]for i in range(3)];jordan=[]
for i in range(3):assert meet(bridge[i],bridge[i+1],*sourcepart)==((F(1),F(0))if i==2 else None)
assert all(meet(bridge[i],bridge[i+1],bridge[j],bridge[j+1])is None for i,j in[(0,2)])
for tag,a,p,h,ep in pending:
 if h==0:continue
 cc=chord(a,p,h);qq=(t-p)/rot(h);fr=next((c,i)for i,(q,hh,c)in enumerate(C[a]['reads'])if q==qq);assert fr==('L',len(W[a])+1)and qq not in G[a]['req'];assert(t-ep)/rot(h)in K
 for i in range(3):assert meet(bridge[i],bridge[i+1],*cc)==((F(0),F(1))if i==0 else None)
 v=cc[1]-cc[0];alpha={'D':math.pi/4,'V':math.atan(3),'U':math.pi/2}[a];joins=[cmath.phase(vec[0]/v),cmath.phase(vec[1]/vec[0]),cmath.phase(vec[2]/vec[1]),cmath.phase((src[1]-src[0])/vec[2])];assert all(abs(x-y)<1e-12 for x,y in zip(joins,[3*math.pi/4-alpha,-math.pi/2,-math.pi/2,-math.pi/4]));assert abs(sum(joins)+alpha+math.pi/2)<1e-12;jordan.append(dict(actor=a,ENTRY=pose(p,h),actual_marker_first=list(fr),exitCORE=xy(qq),principal_join_angles_over_pi=[v/math.pi for v in joins],total_turn=0))
assert len(jordan)==3
live=[]
for a,p in lk:
 if not conflicts(a,p,3,pair):live.append((a,p))
assert live==[('U',2+3j)]and G['U']['last'][g]==('L',20)and C['U']['req'][(g-(2+3j))/rot(3)]
# Every physical RAW-final R, CORE included; no residual-only producer omission.
rcount=Counter();rk={h:[]for h in range(4)};marker_anchor=0
for h in range(4):
 for a in'DCVU':
  for q,(c,tm)in RR[a].items():
   p=g-rot(h)*q;ep=p+rot(h)*G[a]['p'];eh=(h+G[a]['h'])%4;au=next(z for z in J['all144_CORE_inclusive_ordinary_first_BLACK_cut_hole_origins']if z['earlier_writer']==a and z['ENTRY']==pose(p,h));assert au['RAW_EXIT']==pose(ep,eh)and au['physical_final_R']['last_R_tick0']==tm
   if(int(p.real+p.imag)+h)%2:why='sector'
   elif G[a]['req'][q]:why='prior_BLACK'
   elif touch(a,p,h,left|pair):
    why='independent_anchor'
    for tag in touch(a,p,h,left|pair):
     qq=(tag-p)/rot(h)
     if qq not in G[a]['req']and C[a]['req'].get(qq)is True:assert qq in{G[a]['p']+rot(G[a]['h'])*k for k in K};marker_anchor+=1
   else:why='open_origin';rk[h].append((a,p,ep,eh))
   rcount[why]+=1
assert sum(rcount.values())==144 and[list(map(len,[rk[h]for h in range(4)]))]==[[4,3,0,0]]
assert{(a,p)for a,p,*_ in rk[0]}=={(a,-2+2j)for a in'DCVU'}
assert{(a,p)for a,p,*_ in rk[1]}=={('C',-1+4j),('C',-2+3j),('U',-1+4j)}
for a,p,ep,eh in rk[0]:assert(a=='C'and ep==-2+3j and eh==3)or(a!='C'and ep.imag>=3 and eh==0)
for a,p,ep,eh in rk[1]:
 if a=='C':assert eh==0 and ep.imag>=3
 else:
  assert a=='U';qq=(s-p)/rot(1);assert G[a]['reads'][17][0]==qq and G[a]['reads'][17][2]=='R'
  ns={p+rot(1)*v for v in star};tar=2+3j;hits={q for q in ns if(q-tar)/rot(3)in I['U']};assert hits=={3j,-1+3j};assert all((q-tar)/rot(3)in G['U']['req']and G['U']['req'][(q-tar)/rot(3)]for q in hits)
# All foreign physical final-R alignments. Bud TRUE inputs intentionally survive.
fcount=Counter();fk=[]
for n in range(4):
 h=(-n)%4
 for a in'FQB':
  for q,(c,tm)in RR[a].items():
   p=g-rot(h)*q;ep=p+rot(h)*G[a]['p'];eh=(h+G[a]['h'])%4;au=next(z for z in J['all292_CORE_inclusive_FOREIGN_hole_R_origins']if z['FOREIGN']==a and z['ENTRY']==pose(p,h));assert au['RAW_EXIT']==pose(ep,eh)and au['physical_final_R']['last_R_tick0']==tm
   if(int(p.real+p.imag)+h)%2:why='sector'
   elif G[a]['req'][q]:why='prior_BLACK'
   elif touch(a,p,h,star|{t}):why='star_arm_MISS'
   elif conflicts(a,p,h,{s}):why='bud_WHITE_CORE'
   else:
    why=f'age{n}';fk.append((n,a,pose(p,h),pose(ep,eh)))
    if n==0:assert p==-2+2j
    else:assert n==3 and p==-2+3j and eh==3 and ep.real<2 and ep.imag>3
   fcount[why]+=1
assert sum(fcount.values())==292 and len(fk)==6
# Source own C tails retain exact genuine IDs and leave hole WHITE.
for seq in['U','UC','UCC']:
 z=tr(''.join(W[a]for a in seq));assert all(z['last'][q]==G['U']['last'][q]for q in star|{t,s})and z['last'][g][0]=='L'
O=dict(status='PASS old-U arbitrary ordinary-tail W-facing GLOBAL-first-contact exclusion, TOTAL C3 only',manifest=sha(mf),script=sha(S),all188_arm_roles=arm,arm_counts=armcounts,all18_exact_geometry=geom,all64_pair_loss_roles=loss,pair_loss_counts=losscount,three_genuine_current_bridge_interfaces=jordan,all144_ordinary_origin_counts=rcount,ordinary_survivors={h:[[a,pose(p,h),pose(ep,eh)]for a,p,ep,eh in v]for h,v in rk.items()},marker_anchor_inputs_independently_in_exitCORE=marker_anchor,all292_foreign_origin_counts=fcount,six_foreign_survivors=fk,analytic_review=[
'Signed angle gives TOTAL ordinaryC3 and true preFORE n<=3. Independent LEFT remains CURRENT at every strictly earlier simple cut and targetENTRY, not through target. Complete firstFORE starMISS and new188-input arm cover give actual completeFORE RAW+M armMISS; no old-age or bud survival is transferred beyondFORE.',
'At n0, F/Q violate sourceN y-x>=4 and B forces preciselyDDD, forbiddenD-toB. At n1 a real nonemptyWbase is required beforeFORE; Wstart y-x>=5 and everybase increases it>=2. At n2/3 the real preFORE bud supplies the exact firstR contradictions. Source ownC tails preserve the actual IDs.',
'The earliest earlier pair CURRENT loss is counted with other member held only toENTRY, retaining simultaneousU2,0 N inputs. Its exitN y4 and mandatoryC cannot reach listedW heads y<=3. LEFT true inputs in strictly earlier writers are CURRENT-loss contradictions atRAWexit, including real marker CORE capture, not alleged intrinsic color failures.',
'For the three S arm gates, TOTALC0 follows because S after exactlyoneFORE has clock0 mod4 and targetclock3. Bridge t/d/w edges are real SAME current edges only AFTER sourceU RAW. The clipped source chord and finalconsumer chord are directly checked, each touching the simplebridge only at its correct endpoint. Earlier source-to-loss curve is simple by GLOBAL-first stopping, including the repaired actualFORE fine kink. Signed ordinary/current-survivorFORE barriers apply to the intervening pieces, not source prebirth history. d cannot lose inS by the exact independently heldLEFT cover; w is independently held. Actual principal bridge joins cancel the open alpha+pi/2 turn to zero, contradicting a genuine Jordan polygon.',
'Five remainingW targets have entryCORE/firstWHITE pair contradictions. U2,3W truly consumes arm and is retained until the separate sourceL20-hole guard. No pair survival through that contact is assumed.',
'Earliest RAW-END BLACK restoration ofg includesCORE, so every candidate has a physical finalR and firstR. Unread orfirstL requires an earlierBLACKcut. All144ordinary and292FORE origins are rebuilt, retaining actual marker ownership and budTRUEinputs. Their pre/postFORE endpoint cones use arbitrary zeroC rail lengths, not fixedworddepth.',
'The sole postFORE EU(-1,4) donor is real, not cut by the oldbud. Its genuinely NEW star(0,3),(-1,3) lies in targetU ownRAW trueinputs. The independently signed strong freshU ordinary-RAW star theorem applies from this actual donor with no laterFORE, through any terminalC/DCC cuts and attempted targetcompletion. Thus target consumption contradicts NEW current identity permanence; no oldcohort maturity is reused.',
'Only old outgoing-U W-facing GLOBAL-first contacts after FIRSTFORE and arbitrary ordinary suffix close. Other source/headings, secondFORE, unbounded-tail simplicity and global attraction remain separate.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(armcounts,losscount,rcount,fcount);print(sha(S.with_suffix('.json')))
