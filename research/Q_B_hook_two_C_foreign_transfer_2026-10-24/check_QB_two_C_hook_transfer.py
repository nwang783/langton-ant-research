"""Any genuine sourceQ/B hook survives the NEXT complete foreign after
EXACTLY2 ordinaryCs. Source-entry frame, no U/history/simple premise.
Uses actual current-tag projection and first-ordinary deletedCORE holes.
"""
from pathlib import Path
from collections import Counter
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h

def normal(p):return p[1]-p[0]
NE={(-1,-1),(-1,0),(-1,1),(0,0),(0,1),(1,0),(1,1),(1,2),(2,0),(2,1)};HOOK={(-1,-1),(-2,-1),(-3,-1),(-3,-2)};field=NE|HOOK;assert len(field)==13
# Bind the SOURCE-ENTRY physical hook coordinates to signed postEXIT hooks,
# including actual distinct sourceR events of Q andB.
sources=[]
post={'Q':{(-3,-3),(-2,-3),(-1,-3),(-1,-2)},'B':{(-2,-4),(-1,-4),(0,-4),(0,-3)}}
for A in'QB':
 ep=after(W[A]);tr=l.trace(W[A]);O=set(map(tuple,l.literal_geometry(W[A])['outputs']));assert{add(ep[:2],l.rot(q,ep[2]))for q in post[A]}==HOOK and HOOK<=O
 sources.append(dict(source_foreign=A,ENTRY=(0,0,0),actual_EXIT=ep,all4_actual_hook_R_births=[dict(cell=q,own_R_tick0=tr['last'][q][1])for q in sorted(HOOK)],source_NE_hook_overlap_SAME_R46=(-1,-1)))
# Every possible first hook loss by the nextforeign is a TRUE input,
# including marker-owned capture. EntryCORE overlap is already a conflict
# with hookCURRENT at preceding ordinary cut; firstR is a BLACK conflict.
goals={}
for A2 in'FQB':
 tr=l.trace(W[A2]+l.M)
 for g in sorted(HOOK):
  for slot in map(tuple,l.literal_geometry(W[A2])['inputs']):
   p=(*sub(g,slot),0)
   if(sum(p[:2]))%2:continue
   goals.setdefault((A2,p),[]).append(dict(hook_cell=g,input_slot=slot,physical_first_L=o.describe(A2,tr['first'][slot][1])))
assert len(goals)==60
branchA=[];branchB=[];keep=[]
for(A2,p),witness in sorted(goals.items()):
 tr=l.trace(W[A2]+l.M);bad=[]
 for g in sorted(field):
  loc=sub(g,p[:2]);f=tr['first'].get(loc)
  if loc in l.K or f and f[0]=='R':bad.append(dict(SAME_CURRENT=g,local=loc,role='ENTRY_CORE'if loc in l.K else'initial_WHITE',actual_first=f))
 row=dict(next_foreign=A2,entry=p,hook_input_witnesses=witness)
 if bad:row.update(classification='all_NE_unspent_FIELD_CORE_WHITE',conflicts=bad)
 else:row['classification']='three_deleted_CORE_hole_route';keep.append(row)
 branchA.append(row)
 # If the paired loss U3,-1 has actually completed, remaining N heads
 # satisfy X>=3,Y>=3,H>=0 from actual RAW exit3,3.
 assert p[0]<3 or p[1]<3 or normal(p[:2])<0
 branchB.append(dict(next_foreign=A2,entry=p,route='post_NE_pair_breaker_N_cone_impossible',violations=dict(X_below3=p[0]<3,Y_below3=p[1]<3,H_below0=normal(p[:2])<0)))
assert Counter(q['classification']for q in branchA)=={'all_NE_unspent_FIELD_CORE_WHITE':48,'three_deleted_CORE_hole_route':12}
positions={(-2,-4),(0,-4),(1,-5),(2,-4)};assert{(q['next_foreign'],tuple(q['entry'][:2]))for q in keep}=={(A,p)for A in'FQB'for p in positions}
# Shared firstordinary ENTRY-CORE holes are actual LASTL1/L2/L3 in all4
# RAWs. This is a fresh ordered read fact, not an age law or preparedoldID.
coreholes=[(-1,0),(-1,-1),(0,-1)];firstword=[];allR=[];negxR=[];normalR=[]
for a in'DCVU':
 tr=l.trace(W[a]);assert[tr['last'][q]for q in coreholes]==[('L',1),('L',2),('L',3)];firstword.append(dict(atom=a,all3_real_last_L=[dict(local_cell=q,own_tick0=t)for q,t in zip(coreholes,[1,2,3])]))
 p=(0,0,0);rr=[]
 for t,c in enumerate(W[a]):
  if c=='R':
   q=p[:2];assert q[0]>=-1 and q[1]>=0 and q!=(-1,0);rr.append(dict(own_tick0=t,local_cell=q))
   if q[0]==-1:negxR.append(dict(atom=a,own_tick0=t,local_cell=q));assert a=='U'
   if a!='C':
    ep=after(W[a]);nh=normal(ep[:2])-normal(q);assert nh>=0;normalR.append(dict(producer=a,R_own_tick0=t,R_local_cell=q,N_RAW_EXIT_H_minus_written_cell_H=nh))
  p=after(c,p)
 allR.append(dict(atom=a,all_physical_R_events=rr))
assert negxR and all(q['atom']=='U'for q in negxR)
cu=l.trace(W['C']+W['U']);assert not cu['feasible']and(cu['conflict_read'],cu['previous_read'],cu['turn'])==(29,1,'L')
assert after(W['C'],(0,0,2))==(0,-1,1)
for a in'DVU':
 s=after(W[a],(0,0,2));e=after(W[a],(0,0,1));n=after(W[a]);assert s[1]<0 and e[1]<=0 and normal(n[:2])>=0
# Route the12 remaining nextletter/pose labels separately for BOTH source
# foreigners. Each selected physical WHITE hole has strictly larger H
# than target, so no completedN R-producer can fund it before that entry.
selection={'Q':{(-2,-4):0,(0,-4):1,(1,-5):2,(2,-4):1},'B':{(-2,-4):2,(0,-4):0,(1,-5):1,(2,-4):0}}
holeroutes=[]
for A in'QB':
 ep=after(W[A]);holes=[add(ep[:2],l.rot(q,2))for q in coreholes]
 for row in keep:
  A2=row['next_foreign'];p=tuple(row['entry']);i=selection[A][p[:2]];hole=holes[i];loc=sub(hole,p[:2]);tr=l.trace(W[A2]+l.M);f=tr['first'][loc];assert f[0]=='L'and f[1]<len(W[A2])and normal(hole)>normal(p[:2])
  holeroutes.append(dict(source_foreign=A,next_foreign=A2,target_entry=p,first_ordinary_deleted_core_index0=i,first_ordinary_delete_own_tick0=i+1,physical_hole=hole,hole_H=normal(hole),target_H=normal(p[:2]),target_local_cell=loc,actual_target_first_BLACK=o.describe(A2,f[1]),route='S_E_WHITE_then_N_completed_R_normal_cone'))
assert len(holeroutes)==24
# Both named-foreign old source hooks are CURRENT before nextentry because
# ordinary lifetime>=4, while only2 actual Cs have occurred. This is not
# claimed to hold after an arbitraryFOREIGN reader without the NEW proof.
D=[R/'foreign_two_C_pair_hole_transfer_2026-10-24/manifest.json',R/'audits/check_foreign_two_C_pair_hole_independent.json',R/'foreign_hook_four_C_maturity_2026-10-24/manifest.json',R/'audits/check_hook_four_C_maturity_independent.json',R/'word_stabilization/check_foreign_return_interfaces.py',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='ANY actual sourceQ/B, onlyordinaryRAW connector with EXACTLY2 actualCs, then NEXT completeF/Q/B plus actualM11. No U/prehistory/globalSIMPLE/firstforeign premise. All4 SAME sourcehook IDs remainCURRENT at nextFOREIGN RAW EXIT as well as through the ordinary connector. No claim after any furtherforeign.',all2_actual_source_hook_frames=sources,all60_next_foreign_hook_input_geometries_unspent_NE_branch=branchA,all60_spent_NE_branch_N_cone_routes=branchB,all24_source_target_deleted_hole_routes=holeroutes,all4_first_ordinary_shared_last_L_hole_interfaces=firstword,all4_plain_physical_R_supports=allR,all_negative_x_R_events_only_U=negxR,actual_CU_prohibition=cu,all_physical_DVU_R_to_N_RAW_EXIT_normal_bounds=normalR,three_hole_WHITE_proof='Firstordinary at sourceFOREIGN S exitp deletes h1=p+(1,0),h2=p+(1,1),h3=p+(0,1) by lastL1/L2/L3. S physicalR_y<=headY<=pY excludes h2/h3; for h1 equality needs R(-1,0), absent, and laterS heads dropY. In E1 headY<=pY-1; allR_y_offset<=1 excludes h2/h3. A repair of h1 requires headY=pY-1 and localRx=-1, possibleonly U; this height forces no priorS base and no priorE D/V, so firstE base would immediatelyfollowC asU, contradicting literalCU29/1. A secondC has no negative-xR. Thus all3 holesWHITE beforeN2. Every completedN R-producer exits with H=y-x at least the written cellsH, and subsequentN motion neverdecreasesH. At selected targetH<holeH no Rfunding is possible, including RAW COREwrites or previously recycled identities.',coupled_entry_logic='Signed4C hookmaturity gives all4 originals CURRENT through ordinaryC2. Signedpaired-NE dichotomy says either all10NE areunspentCURRENT at nextENTRY, or firstlossactualU3,-1 has completed and Nhead comesfrom3,3 withX,Y>=3,H>=0. All60 truehook inputposes violate that postbreakercone. In unspent branch,48 exact initialCORE/WHITE fieldcuts and12 poses remain. Each of24 typedsource/remainingpose labels has the listed fresh WHITEhole contradiction at actualownRAW firstL. EntryCORE hook overlaps are already impossible and no initial-before-WHITE hook pose can beactual.',CURRENT_completion_qualification='Every actual first CURRENTloss byFOREIGN, including unread exitCORE absorption, has a complete-context trueI firstL slot unless oldtaginENTRYCORE, alreadyimpossible at precedingordinaryCURRENT cut. Since all possible trueI lossposes are excluded, each original staysBLACK SAMEidentity outside nextFOREIGN EXITCORE. No futureforeword is silently executed.',no_single_normal_potential_claim='H is used only for lastR funding of these freshly deleted physical holes, not as a global resource/turnclock. Dormant old outputs and unmatchedports remain in fullfield.',not_claimed=['No zero/oneC or3+Cs genericFOREIGN-toFOREIGN hook theorem here.','No automatic preservation through a thirdforeign or a decreasingforeign budget.','No overalltwoforeign/arbitrarytail simplicity, trajectorylanguage coverage or capture.','No first U-star is transported across sourceFOREIGN.'],dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'QB_two_C_hook_transfer.json').write_text(json.dumps(out,indent=2)+'\n');print('ANY sourceQ/B hook across NEXTFOREIGN C2: spentNE60cone; unspentNE60=48field+12poses;24sourceposes all fresh3holeWHITE/lastR normal obstructions. No U/simple/railbound premise.')
