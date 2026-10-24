from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib,math,cmath
S=Path(__file__);R=S.parents[1];D=R/'U_cycle_one_FOREIGN_clock2_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'manifest.json';assert sha(mf)=='90e9ff1ea47ace8ab2d6eba94b78d8274098ec0a96b066aa5cc9fa1c9f47b192';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'cycle_FOREIGN.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,center,xy,meet=[ns[k]for k in('W','M','K','tr','rot','center','xy','meet')];G={a:tr(W[a])for a in W};C={a:tr(W[a]+M)for a in W}
Z={1+0j,1+1j,2+0j,2+1j};STAR={0j,1j,1+0j,1+1j};LEFT={0j,1j};arm=1+2j;bud=1+3j;hole=-1j
pose=lambda p,h:[*xy(p),h]
def touch(a,p,h,qs):return{q for q in qs if(q-p)/rot(h)in K or(q-p)/rot(h)in C[a]['req']}
def conflicts(a,p,h,qs):return{q for q in qs if(q-p)/rot(h)in K or C[a]['req'].get((q-p)/rot(h))is False}
def chord(a,p,h):return center(p,h),center(p+rot(h)*G[a]['p'],(h+G[a]['h'])%4)
I={a:{q for q,b in C[a]['req'].items()if b and q not in K}for a in W};RR={a:{q:z for q,z in g['last'].items()if z[0]=='R'}for a,g in G.items()}
assert sum(len(I[a])for a in'FQB')==47 and sum(len(I[a])for a in'DVU')==8 and not I['C']
# Every possible external-to-CORE capture is a context read; marker-only
# BLACK inputs are indeed in the actual RAW EXIT CORE, not already read.
marker=[];captures=[]
for a in W:
 ek={G[a]['p']+rot(G[a]['h'])*q for q in K}
 for q in ek-K:
  assert q in C[a]['req'];captures.append((a,xy(q),C[a]['req'][q]))
 for q in I[a]:
  if q not in G[a]['req']:assert q in ek;marker.append((a,xy(q)))
for seq in['U','UC','UCC']:
 z=tr(''.join(W[a]for a in seq));ek={z['p']+rot(z['h'])*q for q in K};assert all(z['last'][q]==G['U']['last'][q]and q not in ek for q in Z|STAR|{arm,bud});assert z['last'][hole]==('L',3)
# Earliest RAW-end physical BLACK restoration of the genuinely deleted hole.
hc=Counter();hs=[]
for n in range(3):
 h=(-n)%4
 for a in'DCVU':
  for q,(c,t)in RR[a].items():
   p=hole-rot(h)*q;ep=p+rot(h)*G[a]['p'];eh=(h+G[a]['h'])%4;au=next(v for v in J['all108_pre_FOREIGN_physical_CORE_inclusive_first_BLACK_cut_origins']if v['actual_source_C_clock']==n and v['earlier_RAW']==a and v['ENTRY']==pose(p,h));assert au['RAW_EXIT']==pose(ep,eh)and au['physical_last_R']['last_R_tick0']==t
   if(int(p.real+p.imag)+h)%2:why='sector'
   elif G[a]['req'][q]:why='needs_earlier_BLACK_cut'
   elif touch(a,p,h,STAR|{arm}):why='independently_CURRENT_anchor'
   else:
    why=f'endpoint_{n}';hs.append((n,a,pose(p,h)))
    assert(n==0 and p.imag<4)or(n==1 and p.imag<5)
   hc[why]+=1
assert sum(hc.values())==108
# Complete FOREIGN cycle touch: CURRENT excludes CORE/firstR, leaving
# exactly the complete set of RAW-or-marker firstL external inputs.
fc=Counter();fg=[]
for n in range(3):
 h=(-n)%4
 for tag in [2+0j,2+1j]:
  for a in'FQB':
   for q in I[a]:
    p=tag-rot(h)*q;au=next(v for v in J['all282_early_FOREIGN_cycle_Einput_roles']if v['true_preFOREIGN_SOURCE_ENTRY_C_age']==n and v['original_east_cycle_tag']==xy(tag)and v['FOREIGN']==a and v['ENTRY']==pose(p,h))
    if(int(p.real+p.imag)+h)%2:why='sector'
    elif touch(a,p,h,STAR|{arm}):why='complete_STAR_arm_MISS'
    elif conflicts(a,p,h,Z|{bud}):why='CURRENT_Z_or_preFORE_bud'
    else:
     why=f'gate_{n}';fg.append((n,a,pose(p,h),xy(tag)))
     if n==0:assert p==7-1j and p.imag<4
     elif n==1:assert p in{4+1j,5+4j}and p.imag-p.real<5
     else:
      assert a=='B'and p==-2j;qq=(hole-p)/rot(h);assert qq in K and qq==-1j and C[a]['reads'][3][0]==qq and C[a]['reads'][3][2]=='L'
    fc[why]+=1
assert sum(fc.values())==282 and len(fg)==20
# Rebuild ALL ordinary first-current-loss inputs, independent of full packets.
pc=Counter();pg=[];src=chord('U',0j,0)
for tag in Z:
 for h in range(4):
  for a in'DVU':
   for q in I[a]:
    p=tag-rot(h)*q;ep=p+rot(h)*G[a]['p'];eh=(h+G[a]['h'])%4;au=next(v for v in J['all128_plain_ordinary_cycle_first_CURRENT_loss_roles']if v['first_lost_original_Z_tag']==xy(tag)and v['earlier_ordinary_RAW']==a and v['ENTRY']==pose(p,h));assert au['RAW_EXIT']==pose(ep,eh)
    if(int(p.real+p.imag)+h)%2:why='sector'
    elif conflicts(a,p,h,Z):why='CURRENT_Z_CORE_or_WHITE'
    elif meet(*src,*chord(a,p,h))is not None:why='earlier_source_contact'
    elif touch(a,p,h,LEFT):why='independent_LEFT_at_strictly_earlier_cut'
    else:
     why='right_U_simultaneous';assert a=='U'and p==3-1j and h==0 and q in{-1+1j,-1+2j};assert {2+0j,2+1j}<={p+rot(h)*v for v in I[a]};pg.append((xy(tag),pose(p,h),pose(ep,eh)))
    pc[why]+=1
assert pc==dict(sector=64,CURRENT_Z_CORE_or_WHITE=56,earlier_source_contact=4,independent_LEFT_at_strictly_earlier_cut=2,right_U_simultaneous=2)
# Independently reconstruct protected-edge geometry, not an old clock table.
P=-1+7j;E=5+1j;B=5-3j;bridge=[E,3+3j,1+1j,-1+3j,P];edges=list(zip(bridge,bridge[1:]));assert src==(-1-1j,P)and chord('U',3-1j,0)==(B,5+5j)
for q,(a,b)in zip([2+1j,1+1j,1j],edges):
 v=1+1j if int(q.real+q.imag)%2==0 else 1-1j;assert {a,b}=={2*q-v,2*q+v}
for i,(a,b)in enumerate(edges):
 assert meet(a,b,B,E)==((F(0),F(1))if i==0 else None)
 for j in range(i+1,len(edges)):assert meet(a,b,*edges[j])==((F(1),F(0))if j==i+1 else None)
assert edges[-1][0].real==src[0].real and src[0].imag<edges[-1][0].imag<P.imag
ct=[];p=4j;h=0
for idx in range(2):
 cc=chord('C',p,h);hits=[meet(a,b,*cc)for a,b in edges];assert hits==([None,None,None,(F(1),F(0))]if idx==0 else[None]*4);ct.append([pose(p,h),list(map(xy,cc))]);p+=rot(h)*G['C']['p'];h=(h+G['C']['h'])%4
vec=[8j]+[b-a for a,b in edges];joins=[cmath.phase(b/a)for a,b in zip(vec,vec[1:])];assert all(abs(x-y)<1e-12 for x,y in zip(joins,[math.pi/4,math.pi/2,-math.pi/2,-math.pi/4]))and abs(sum(joins))<1e-12
# Actual principal tangent increments for arbitrary ordinary rails with ONE
# complete FOREIGN; only C->FORE wraps, and actual G8/FIRSTFORE disallows it.
raws={a:W[a]for a in'DCVUF'}|{'TQ':W['Q'][56:],'TB':W['B'][56:]};gg={a:tr(w)for a,w in raws.items()};alpha={a:cmath.phase(center(g['p'],g['h'])-center(0j,0))for a,g in gg.items()};alpha['F']+=2*math.pi;omega={a:(math.pi/2 if a=='C'else math.pi if a=='F'else 0)for a in raws};pairs=[]
for a in raws:
 for b in raws:
  if (a in'DCVU'and b in'DCVU')or(a in'VU'and b=='F')or(a=='F'and b in'DCVU')or(a=='F'and b in['TQ','TB'])or(a in['TQ','TB']and b in'DCVU'):
   va=center(gg[a]['p'],gg[a]['h'])-center(0j,0);vb=(center(gg[b]['p'],gg[b]['h'])-center(0j,0))*rot(gg[a]['h']);actual=cmath.phase(vb/va);claim=omega[a]+alpha[b]-alpha[a];assert abs(actual-claim)<1e-12;pairs.append((a,b,actual/math.pi))
assert all(gg[a]['h']==0 for a in['D','V','U','TQ','TB'])and gg['C']['h']==3 and gg['F']['h']==2
# The path starts at a source U terminal tangent and ends on a consumer U
# half chord, so endpoint alphas cancel. The one F prefix contributes pi.
assert [k for k in range(10)if k+2 in[-4,4]]==[2]
# Critical pair actor needs still-original eastbottom in entryCORE; breaker
# EXIT(3,3,N) cannot reach(2,0,N) at the same remaining C clock.
assert(2-(2+0j))in K and pg[0][2]==[3,3,0]
for a in'DVU':assert G[a]['p'].imag>0 and G[a]['p'].real>=0 and G[a]['h']==0
# Complete prelaid seed, every actual fine read, original identity, all fields.
reg=J['actual37_cell_genuine_U_entry_cycle_survival_regression'];seq='UCCVDUUFD';raw=''.join(W[a]for a in seq);z=tr(raw+M);assert z['bad']is None and len(z['reads'])==219;seed={complex(*q)for q in reg['complete_black_seed']};assert seed=={q for q,b in z['req'].items()if b}and len(seed)==37;board=set(seed);ids={q:('initial',q)for q in seed};snap=[]
for i,(p,h,c)in enumerate(z['reads']):
 au=reg['all219_actual_RAW_plus_M11_fine_reads'][i];assert au['cell']==xy(p)and au['turn']==c and au['tick0']==i;assert(p in board)==(c=='L')
 if c=='L':board.remove(p);ids.pop(p)
 else:board.add(p);ids[p]=('R',i)
 snap.append(sorted(map(xy,board)))
 if i+1==len(raw):assert ids[2+0j]==('R',8)and ids[2+1j]==('R',7);ep=p+ns['V'][(h+(1 if c=='R'else-1))%4];assert ep==2-4j and all((q-ep)not in K for q in[2+0j,2+1j])
bad=tr(raw+W['U']+M)['bad'];assert bad==(232,8,2+0j,'R')
O=dict(status='PASS scoped one-FIRST-FOREIGN intact U-cycle and conditional TOTAL-C2 first-break interface',manifest=sha(mf),script=sha(S),hole108_counts=hc,hole_endpoint_survivors=hs,FORE282_counts=fc,FORE20_gates=fg,plain128_counts=pc,two_simultaneous_right_U_inputs=pg,source_C_tail_chords=ct,bridge_doubled=list(map(xy,bridge)),actual_principal_closing_turns_over_pi=[v/math.pi for v in joins],all_principal_tangent_interfaces=pairs,actual_marker_inputs_in_RAW_EXIT_CORE=marker,complete_capture_cover=captures,finite_control=dict(word=seq,initial_black=sorted(map(xy,seed)),all219_postread_fields=snap,final_black=sorted(map(xy,board)),immutable_attempt_failure=[bad[0],bad[1],xy(bad[2]),bad[3]]),analytic_review=[
'The signed old-four-C cycle theorem is used strictly before FIRSTFORE at true age<=2. Source U/UC/UCC real tails preserve all named original cycle/star/arm/bud identities. The early star and arm COMPLETE-MISS premises plus literal 282-role cover protect the whole cycle across completeFORE RAW+actualM, not merely its external outputs.',
'The source L3 hole is physically WHITE, including CORE. Earliest BLACK RAW-end restoration is covered by every physical finalR, not just residual outputs. FirstL needs a preceding BLACK cut. Independent STAR/arm CURRENT at every earlier cut excludes true marker captures as CURRENT loss at RAWexit; it is not mislabeled an intrinsic first-color conflict. Unbounded N/W endpoint cones close all108 origins.',
'All128 postFORE ordinary current-loss roles are freshly derived from actual RAW+M inputs and ENTRY/EXIT CORE completeness. Two remaining rows are simultaneous east-pair inputs of one genuine rightU(3,-1,N). Independent LEFT is invoked strictly before the chosen global-first contact, never to exclude a legitimate target input merely by entry color.',
'The closing bridge is a simple actual current-edge chain at old(2,1),(1,1),(0,1), followed by a genuine clipped past source-U chord. These IDs are used only after actual source birth. GLOBAL-first stopping supplies simple future curve and no earlier contact with the actual source chord; signed ordinary and repairedFORE barriers protect the other bridge edges. Source ownC interfaces and the final consuming U half are independently checked, so retirement inside that final base does not invalidate the closure.',
'Actual principal tangent interfaces telescope to TOTAL K*pi/2+pi from source-U terminal tangent to consumer-U half. The single FORE contributes its genuine F prefix; Q/B tails are retained. C-to-FIRSTFORE wrap is excluded by actual G8 adjacency, not by geometry alone. Closing turns pi/4,pi/2,-pi/2,-pi/4 cancel, and the genuine Jordan equation forces K=2. No old upper-input age, root funding or U-count theorem is transported.',
'The proposed critical U(2,0,N) atTOTAL2 has original eastbottom in ENTRYCORE. Its required earlier cycle retirement must be the rightU at2; actual rightU RAWexit(3,3,N) cannot reach(2,0,N) along arbitrary zeroC ordinary N rails, and a real C already exceeds the targetclock. No unexecuted full-family tail is inserted.',
'The literal37-cell whole-board219-read control preserves original east R7/R8 through the actual next-U entry. Attempted U firstfails ownR24/global232 at still-black originalR8. It is not a new contact/loop control or unconditional postFORE persistence theorem.',
'Only n<=2 completeFOREMISS and the stated GLOBAL-first/simple-prefix conditional firstbreak law are signed. No permanent cycle, secondFORE, arbitrary-tail simplicity, old-age lift, fuel budget or universal capture follows.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(hc,fc,pc);print(sha(S.with_suffix('.json')))
