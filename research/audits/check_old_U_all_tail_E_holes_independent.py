from pathlib import Path
from fractions import Fraction
from itertools import product
from collections import Counter
import json,hashlib,math
S=Path(__file__).resolve();R=S.parents[1];D=R/'old_U_all_tail_E_hole_guard_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(D/'manifest.json')=='e366b17f4b003eed6aac7bdc5ad4cf3a8a1b841ead4f3d5649ce59246f83829d';m=json.loads((D/'manifest.json').read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
q=R/'audits/check_old_V_second_age1_independent.py';ns={'__file__':str(q)};exec(q.read_text().split('# Universal')[0],ns);W,M,K,tr,rot,center,xy,meet=[ns[k]for k in('W','M','K','tr','rot','center','xy','meet')]
J=json.loads((D/'E_holes.json').read_text());G={a:tr(W[a])for a in'DCVUFQB'};angles=json.loads((R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json').read_text())['all44_exact_source_target_C_window_rows']
for a in'DCVU':
 ar=next(z for z in angles if z['source_class']=='preFOREIGN_ordinary'and z['source_atom']=='U'and z['contact_atom']==a);assert[k for k in ar['allowed_C_counts_before_contact_ENTRY']if(2-k)%4==1]==[1]
# Every source-deletion, physical finalR and actual CORE rewrite is rebuilt.
RR={a:[(p,t,p in{z['p']+k*rot(z['h'])for k in K})for p,(c,t)in z['last'].items()if c=='R']for a,z in G.items()}
for a,rows in RR.items():
 assert{(tuple(xy(p)),t,core)for p,t,core in rows}=={(tuple(z['slot']),z['actual_RAW_last_R_tick0'],z['in_RAW_EXIT_CORE'])for z in J['all_physical_RAW_final_R_slots_including_EXIT_CORE'][a]}
left={0j,1j};source=(center(0j,0),center(G['U']['p'],G['U']['h']));geom=[];surv=[]
for a in'DCVU':
 z=tr(W[a]+M);end=center(G[a]['p']*rot(1),(G[a]['h']+1)%4);start=center(0j,1);corners=[(s-t)/2 for s in source for t in(start,end)]
 for x in range(math.floor(min(p.real for p in corners)),math.ceil(max(p.real for p in corners))+1):
  for y in range(math.floor(min(p.imag for p in corners)),math.ceil(max(p.imag for p in corners))+1):
   if(x+y+1)%2:continue
   head=complex(x,y);hit=meet(*source,start+2*head,end+2*head)
   if hit is None or not(0<=hit[0]<1 and 0<hit[1]<=1):continue
   bad={p for p in left if(p-head)/rot(1)in K or z['req'].get((p-head)/rot(1))is False}
   au=next(v for v in J['all18_exact_outgoing_owned_E_geometries']if v['actor']==a and v['ENTRY']==[x,y,1]);assert set(map(tuple,[xy(p)for p in bad]))=={tuple(v['SAME_LEFT'])for v in au['SAME_LEFT_contradictions']};assert[str(hit[0]),str(hit[1])]==[au['old_U_parameter'],au['new_positive_parameter']]
   geom.append((a,x,y,str(hit[0]),str(hit[1]),len(bad)))
   if not bad:surv.append((a,head))
assert len(geom)==18 and len(surv)==4
holes={('D',-1+0j):-1+1j,('V',-3+0j):-1-1j,('U',-4-1j):-1-1j,('U',-2-1j):-1j};assert set(surv)==set(holes)
for (a,head),g in holes.items():
 z=tr(W[a]);slot=(g-head)/rot(1);tick=next(t for t,(p,h,c)in enumerate(z['reads'])if p==slot);assert z['reads'][tick][2]=='L'and G['U']['last'][g][0]=='L'
 au=next(v for v in J['all4_SAME_LEFT_compatible_targets_and_source_deleted_holes']if v['geometry']['actor']==a and v['geometry']['ENTRY']==[*xy(head),1]);assert au['actual_source_last_L_tick0']==G['U']['last'][g][1]and au['actual_target_first_BLACK']==['L',tick]
for a in'DCVU':assert min(p.imag for p,t,c in RR[a])>=0 and min(p.real for p,t,c in RR[a])>=-1
for a in'FQB':assert min(p.real for p,t,c in RR[a])>=-5
# Exact endpoint Diophantine classification, different elimination than author's.
N=[];WW=[]
for a in'FQB':
 for p,t,core in RR[a]:
  for g in sorted(set(holes.values()),key=lambda p:(p.real,p.imag)):
   X=int((g-p).real);Y=int((g-p).imag)-4;nn=[]
   if X>=0:
    for v in range(X+1):
     d=X-v;r=Y-X-2*v
     if r>=0 and r%4==0:nn.append((d,v,r//4))
   au=next(z for z in J['all_FOREIGN_n0_physical_R_funding_roles']if z['foreign']==a and z['hole']==xy(g)and z['physical_final_R']['slot']==xy(p));assert nn==[(z['N_D_count'],z['N_V_count'],z['N_U_count'])for z in au['all_nonnegative_integer_count_models']]
   for counts in nn:
    d,v,u=counts;assert a=='B'and g==-1+1j and counts in[(1,0,0),(2,0,0)]and tr(W['D']+W['B'])['bad'];N.append((a,xy(g),xy(p),counts))
   ss=int(g.imag-p.real)-5;tt=int(-g.real-p.imag);ww=[]
   if ss>=1:
    for v in range(ss+1):
     d=ss-v;r=tt-ss-2*v
     if r>=0 and r%4==0:ww.append((d,v,r//4))
   au=next(z for z in J['all_FOREIGN_n1_UC_physical_R_funding_roles']if z['foreign']==a and z['hole']==xy(g)and z['physical_final_R']['slot']==xy(p));assert ww==[(z['W_D_count'],z['W_V_count'],z['W_U_count'])for z in au['all_integer_count_models_with_d_plus_v_ge1']]
   for counts in ww:
    word='UCV'+a if counts==(0,1,0)else'UCDUQ';assert counts==(0,1,0)or(a=='Q'and counts==(1,0,1));b=tr(''.join(W[c]for c in word)+M)['bad'];assert b is not None;WW.append((a,xy(g),xy(p),counts,word,[b[0],b[1],xy(b[2]),b[3]]))
assert len(N)==2 and len(WW)==4 and tr(W['C']+W['U'])['bad']
# No depth cap: E displacement (d+3v+4u,-d-v).
def ecounts(ep,target):
 dx=int((target-ep).real);drop=int((ep-target).imag)
 if dx<0 or drop<0:return[]
 ans=[]
 for u in range(dx//4+1):
  r=dx-drop-4*u
  if r<0 or r%2:continue
  v=r//2;d=drop-v
  if d>=0:ans.append(dict(D=d,V=v,U=u))
 return sorted(ans,key=lambda z:(z['V'],z['U']))
post=[];repairs=[]
for(a,head),g in holes.items():
 for writer in'DVU':
  z=G[writer]
  for p,t,core in RR[writer]:
   ep=g+(z['p']-p)*rot(1);models=ecounts(ep,head);assert not models
   s=g+(z['p']-p)*rot(2);assert s.imag<=g.imag
   if head.imag>=g.imag:route='below_after_C'
   elif s.imag<g.imag:route='D_below_after_C'
   elif s.real==g.real+1:assert s==1j and head==-1;route='D_right_after_C'
   else:assert s==-1+1j and center(s,2)==-1+3j;route='earlier_midpoint_EXIT'
   au=next(v for v in J['all_postFOREIGN_E_physical_R_endpoint_obligations']if v['target']['actor']==a and v['target']['ENTRY']==[*xy(head),1]and v['writer_RAW']==writer and v['physical_final_R']['slot']==xy(p));assert au['writer_RAW_EXIT']==[*xy(ep),1]and not au['all_zeroC_E_endpoint_count_models']
   au=next(v for v in J['all_postFOREIGN_S_physical_R_endpoint_obligations']if v['target']['actor']==a and v['target']['ENTRY']==[*xy(head),1]and v['writer_RAW']==writer and v['physical_final_R']['slot']==xy(p));assert au['writer_RAW_EXIT']==[*xy(s),2]
   post.append((a,xy(head),writer,xy(p),t,core,xy(ep),xy(s),route))
 for p,t,core in RR['C']:
  ep=g+(G['C']['p']-p)*rot(2);models=ecounts(ep,head);au=next(v for v in J['all_postFOREIGN_C_physical_R_endpoint_obligations']if v['target']['actor']==a and v['target']['ENTRY']==[*xy(head),1]and v['physical_C_final_R']['slot']==xy(p));assert au['writer_RAW_EXIT']==[*xy(ep),1]and au['all_E_continuation_count_models']==models
  if models:
   assert a=='D'and head==-1 and p==0 and t==4 and core and models==[dict(D=0,V=0,U=0)];cp=g-p*rot(2);assert cp==-1+1j and center(cp,2)==-1+3j and(1j-cp)/rot(2)in K;repairs.append((a,xy(head),xy(cp),t))
assert len(post)==112 and len(repairs)==1
# Literal CORE-positive regression, complete board and exact birth/death.
w=W['C']+W['D']+M;z=tr(w);assert z['bad']is None;B={p:('I',i)for i,p in enumerate(sorted((p for p,b in z['req'].items()if b),key=lambda p:(p.real,p.imag)))};initial=set(B);p=0j;h=0;cut=None;death=None
for t,c in enumerate(w):
 assert(p in B)==(c=='L')
 if c=='L':
  old=B.pop(p)
  if old==('R',4):death=t
 else:B[p]=('R',t)
 h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
 if t+1==len(W['C']):assert B[0j]==('R',4)and(0j-p)/rot(h)in K;cut=[xy(p),h]
assert len(initial)==6 and death==16 and sorted(map(xy,initial))==J['real_prepared_C_R4_alive_CORE_repair_regression']['complete_finite_black_seed']
regs=[]
for v in J['all6_structurally_matched_rail_negative_regressions']:
 b=tr(''.join(W[a]for a in v['word'])+M)['bad'];assert b and b[1]==14 and b[2]==-1+1j;regs.append([v['word'],b[0],b[1],xy(b[2]),b[3]])
review=['Signed one-foreign angle window and actual heading congruence force TOTAL K1, with true preFORE n0/1 only. Genuine completed UCC cannot fit; n0 source plainU, n1 plainU orUC. PreFORE all-star/currentness plus complete firstFORE MISS and global-first stopping invoke the conditional LEFT guardian exactly at candidateENTRY, not through contact.',
'All18 rational outgoing-U-owned E heads and actual before-context LEFT tests are rebuilt. Four survivors need three genuinely source-L-deleted physical holes; each target first sees its selected hole at an own RAW L. LastR funding is therefore exhaustive over every physical prior RAW finalR, including activeCORE writes, not just residualO or net packet output.',
'After sourceU RAW, later N heads have y>=4 and W heads y>=5; every physical ordinary finalR has localy>=0,x>=-1. Thus no preFORE restoration. In the n1 plainU case its firstC belongs to a later full producer, hence W starty>=6; real CU and C-toFORE exclusions force a nonempty W firstD/V, henceFORE entryy>=7. FOREIGN finalR localx>=-5 then writesy>=2. The UC case startsW0,5 and is handled separately by exact endpoint equations.',
'The complete FOREIGN origin arithmetic gives only two n0 models, both actual D-toB adjacency contradictions, and four UC/n1 models, all immutable wholeword conflicts. These endpoint-derived finite solutions are not a depth search. Unknown prepared initial bits cannot restore an actually source-erased hole without a laterR.',
'PostFORE phases are S then oneC then E for n0, or E alone for n1. Fresh full physical-R support plus exact unlimited E semigroup cuts all E writers and all but the recorded C CORE repair. S endpoints either become too low afterC, start E right oftarget, or equal the strict old-U midpoint. The actual C-R4 repair is legal but its ENTRY is that same earlier old-U midpoint, contradicting GLOBAL-first before the target. Legitimate source adjacency is not excluded: midpoint is strict interior of the old source chord.',
'The six-cell CD+M board freshly replays a real C R4 birth aliveCORE at its RAWexit and death at actual nextD tick1/read2. This protects CORE completeness, not an old-U ancestry or first-contact control. Six negative rail words are regressions only.',
'Conclusion is solely no E-facing ordinary GLOBAL-first contact with this genuine preFORE old-U source after FIRSTFORE and arbitrary ordinary-only suffix. No right-pair/q persistence, postFORE maturation, secondFOREIGN, other-heading/source closure or arbitrary-tail simplicity is inferred.']
out=dict(status='PASS all-length old-U E-facing first-contact hole restoration guard',manifest=sha(D/'manifest.json'),dependencies=m['dependencies'],all18_geometries=geom,physical_R_counts={a:len(v)for a,v in RR.items()},n0_foreign_models=N,n1_UC_foreign_models=WW,all112_E_and_S_writer_roles=post,sole_real_C_CORE_repair=repairs,prepared_CORE_control=dict(seed=sorted(map(xy,initial)),exit=cut,death=death,final=sorted(map(xy,B))),negative_rail_controls=regs,analytic_review=review,scope=m['scope'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(sha(S.with_suffix('.json')))
