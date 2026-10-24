"""Zero/one-C creator-history exclusion from the signed literal 69-gate list.
Four forced finite words only; no prefix search or unbounded role scan.
"""
from pathlib import Path
from collections import Counter
import hashlib,json
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
TP=R/'foreign_U_port_interfaces_2026-10-23/foreign_U_ports.json';T=json.loads(TP.read_text())
G=json.loads((R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json').read_text())['macro_words'];W={a:G[i]['word']for i,a in enumerate('DCVUFQB')};V=((0,1),(1,0),(0,-1),(-1,0));L={(0,0),(0,1),(1,0),(1,1)}
# At zero C, x=d+v and y-4=d+3v+4u, so x>=0,y-4>=x.
zero=[]
for g in T['interfaces']['star']['gates']:
 x,y,h=g['pose']
 if h!=0:continue
 passes=x>=0 and y-4>=x
 zero.append(dict(foreign=g['foreign'],pose=g['pose'],passes_head_cone=passes))
assert len(zero)==18
assert [(r['foreign'],r['pose'])for r in zero if r['passes_head_cone']]==[('B',[2,6,0])]
# At one C, y=5+d+3v+4u+e+f and
# x=d+v-e-3f-4g. All gate heights are <=6.
# For y=5 all positively counted variables vanish, so x=-4g<=0.
# For y=6, v=u=0,d+e+f=1, so x<=1.
one=[]
for g in T['interfaces']['star']['gates']:
 x,y,h=g['pose']
 if h!=3:continue
 assert y<=6
 passes=y>=5 and x<=(0 if y==5 else 1)
 one.append(dict(foreign=g['foreign'],pose=g['pose'],passes_head_cone=passes))
assert len(one)==18
assert [(r['foreign'],r['pose'])for r in one if r['passes_head_cone']]==[(a,[1,6,3])for a in'FQB']
# Exact integer solutions in the only surviving cases are respectively
# (d,v,u)=(2,0,0) and (d,v,u,e,f,g)=(1,0,0,0,0,0), as the note proves.
cases=[]
for labels in (['U','D','D','B'],['U','D','C','F'],['U','D','C','Q'],['U','D','C','B']):
 p=(0,0);h=0;par=set();req={};reads={};first={};tick=0;poses=[];fail=None
 for a in labels:
  poses.append(dict(label=a,tick=tick,pose=(*p,h)))
  for phase,ch in enumerate(W[a]):
   need=(ch=='L')^(p in par)
   if p in req and req[p]!=need:
    actual=req[p]^(p in par)
    fail=dict(label=a,phase=phase,tick=tick,cell=p,proposed_turn=ch,forced_actual_turn='L'if actual else'R',previous_reads=reads[p],first_initial_color=req[p],conflicting_initial_color=need);break
   req[p]=need;reads.setdefault(p,[]).append((tick,ch,a));first.setdefault(p,(tick,ch));par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=p[0]+V[h][0],p[1]+V[h][1];tick+=1
  if fail:break
 assert fail and fail['proposed_turn']=='L' and fail['forced_actual_turn']=='R'
 if labels[-2]=='D':
  assert fail['phase']==43 and fail['tick']==91 and fail['cell']==(0,5) and fail['previous_reads']==[(39,'L','D')]
 else:
  assert fail['phase']==16 and fail['tick']==69 and fail['cell']==(-1,4) and fail['previous_reads']==[(29,'L','D')]
 seed={q for q,b in req.items()if b};board=set(seed);q=(0,0);hh=0;word=''.join(W[a]for a in labels)
 for t,ch in enumerate(word[:tick]):
  assert(ch=='L')==(q in board);board.symmetric_difference_update({q});hh=(hh+(-1 if ch=='L'else 1))%4;q=q[0]+V[hh][0],q[1]+V[hh][1]
 assert q==p and q not in board and L<=board
 cases.append(dict(recipe=labels,poses=poses,immutable_conflict=fail,actual_consistent_prefix_seed=sorted(seed),actual_seed_mass=len(seed),actual_prefix_length=tick,old_star_still_black_at_deviation=True))
D=[TP,R/'foreign_U_port_interfaces_2026-10-23/manifest.json',R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json',R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_AUDIT',scope='First foreign after an actual uninterrupted complete-eight U-entry interval. No original U-star RAW retirement or foreign exit-core absorption is possible at C ages zero or one. No age-two or later exclusion, global reset bound or postforeign permanence.',zero_C_gate_filter=zero,one_C_gate_filter=one,forced_word_conflicts=cases,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'foreign_U_early_star_exclusion.json').write_text(json.dumps(o,indent=2)+'\n')
print('All 18 zero-C and 18 one-C heading gates filtered; four forced words fail immutably. Foreign star effect requires at least two C atoms.')
