"""Two necessary D-source resets force genuine old buds into changed F cores.
No returned simplicity, postforeign age law, or generic prefix enumeration.
"""
from pathlib import Path
from collections import Counter
from itertools import permutations
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';QP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json';CP=R/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact.json';XP=R/'returned_D_entry_controls_2026-10-24/D_entry_controls.json'
G=json.loads(GP.read_text())['geometry'];W=json.loads(QP.read_text())['macro_words'];C=json.loads(CP.read_text());X=json.loads(XP.read_text());M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};VEL=((0,1),(1,0),(0,-1),(-1,0));mp={a:i for i,a in enumerate('DCVUFQB')};b=(2,0);bp=(3,1);g=(0,0);g1=(0,1);gm=(-1,-1);young_deleted=(0,-1);previous_bud=(1,-1)
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def at(q,p,h):return add(p,rot(q,h))
def center(p,h):return add((2*p[0],2*p[1]),rot((-1,-1),h))
def derive(w,stop=False):
 p=(0,0);h=0;par=set();rq={};rd={};first={}
 for t,ch in enumerate(w):
  initial=(ch=='L')^(p in par)
  if p in rq and rq[p]!=initial:
   if stop:return dict(tick=t,cell=p,first=first[p],required_initial=initial)
   raise AssertionError((t,p))
  if p not in rq:rq[p]=initial;first[p]=[t,ch]
  rd.setdefault(p,[]).append([t,ch]);par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEL[h])
 return rq,par,p,h,rd
AT=[]
for i in range(4):
 rq,par,ep,dh,rd=derive(W[i]['word']);ctx,_,_,_,_=derive(W[i]['word']+M);outs={q for q in rq if rq[q]^(q in par)}-{at(z,ep,dh)for z in K};assert all(q[1]>=0 and sum(q)>=0 for q in outs);AT.append(dict(name='DCVU'[i],endpoint=ep,turn=dh,outputs=outs,context=ctx))
def endpoints(identity,target,foreign,case):
 out=[]
 for gi in(0,4,7):
  for slot in map(tuple,G[gi]['inputs']):
   p=sub(identity,rot(slot,1));ep=at(tuple(G[gi]['endpoint'][:2]),p,1);dx=target[0]-ep[0];down=ep[1]-target[1];sol=[];allowed=('V','U')if foreign in('F','Q')else('U',)
   for v in range(max(down+1,0)):
    d=down-v;rem=dx-d-3*v
    if rem<0 or rem%4:continue
    u=rem//4;last=[a for a,c in(('D',d),('V',v),('U',u))if c and a in allowed];sol.append(dict(d=d,v=v,u=u,allowed_last=last))
   assert ep!=target and all(not z['allowed_last']for z in sol),(identity,target,gi,slot,sol)
   out.append(dict(case=case,identity=identity,clearer=G[gi]['name'],input_slot=slot,entry=[*p,1],endpoint=ep,foreign_entry=target,all_E_run_counts=sol))
 return out

rows=[];erows=[]
for ix in (15,30):
 r=C['old_source_contact_cases'][ix];p=tuple(r['foreign_pose'][:2]);h=r['foreign_pose'][2];n=mp[r['returned_atom']]
 fr,fp,fe,fh,fd=derive(W[4]['word']);combined=derive(W[4]['word']+W[n]['word']+M)
 rq,par,ep,dh,reads=combined;exitK={at(q,fe,fh) for q in K}
 # beta is a genuinely previous actual exit-bud under U-entry, not an entry root.
 erows.extend(endpoints(previous_bud,p,'F',ix))
 # D30 also physically retires source b. Same target-specific held-b argument.
 if ix==30:erows.extend(endpoints(b,p,'F',ix))
 inputport=(-4,-1);globalraw=at(inputport,p,h)
 assert globalraw==(previous_bud if ix==15 else b)
 assert fd[inputport]==[[51,'L'],[55,'R']] and reads[inputport]==[[51,'L'],[55,'R'],[59,'L']]
 assert inputport not in K and inputport in exitK
 assert rq[inputport] is True
 # Actual physical read of the changed BLACK core, not residual reproduction.
 marker=(-3,-2);globalmarker=at(marker,p,h)
 assert marker not in fr and marker in exitK and reads[marker][0]==[57,'L']
 assert rq[marker] is True
 if ix==30:assert globalmarker==previous_bud
 rows.append(dict(catalogue_id=ix,foreign_pose=r['foreign_pose'],returned_atom=r['returned_atom'],returned_pose=r['returned_pose'],old_source_C_clock=3,genuine_old_raw_input=globalraw,foreign_local_raw_input=inputport,original_residual_retirement=dict(owner='F RAW',owner_tick0=51,owner_read_number1=52),core_black_rewrite=dict(owner='F RAW',owner_tick0=55,owner_read_number1=56,is_F_exit_core=True,is_fresh_F_residual_output=False),replacement_core_deletion=dict(owner='immediately following actual '+r['returned_atom']+' RAW',owner_tick0=3,owner_read_number1=4,combined_tick0=59),marker_input=dict(foreign_local_cell=marker,global_cell=globalmarker,RAW_read=False,F_exit_core=True,actual_owner='immediately following actual '+r['returned_atom']+' RAW',owner_tick0=1,owner_read_number1=2,combined_tick0=57,is_genuine_previous_exit_bud=(ix==30))))
assert len(erows)==24
D=[GP,QP,CP,R/'returned_D_source_join_2026-10-24/manifest.json',R/'returned_D_clock3_controls_2026-10-24/manifest.json',R/'core_periodicity_new/atomic_exit_bud_frozen_20261023_1325/manifest.json',R/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='Conditional exact core-port history in the TWO necessary U-entry D-source return geometries, not their attainment or exclusion. Original beta is genuinely born at the actual pre-D atomic exit; original b is genuinely D-born. Both are current before F where used. The subsequent R is a BLACK EXIT-CORE write, not a fresh residual output. Independent signed prepared D-entry controls demonstrate the physical reset but have no U-entry fixed-word lift.',two_forced_core_reset_interfaces=rows,all24_target_specific_E3_older_bud_endpoint_obligations=erows,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in D})
(H/'D_forced_core_ports.json').write_text(json.dumps(o,indent=2)+'\n');print('Two forced original-bud to F-core reset interfaces,24 exact older-bud endpoint obligations.')
