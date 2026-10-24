"""The two remaining U-source F-prefix ports: exact old-arm retirement.
Only552 literal input alignments and one unbounded one-C endpoint cone.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json,hashlib,importlib.util
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent;W=ROOT/'core_periodicity_new'
sp=importlib.util.spec_from_file_location('literal',HERE/'check_foreign_return_interfaces.py')
lit=importlib.util.module_from_spec(sp);sp.loader.exec_module(lit)
GP=W/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry']
CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv'
CT={tuple(map(int,z.split()[:8])) for z in CP.read_text().splitlines()}
keep=[0,1,4,5,6,7,8,9];compact={a:i for i,a in enumerate(keep)}
L={(0,0),(0,1),(1,0),(1,1)};t=(1,2)
ST={0:(2,2),1:(2,2),4:(2,6),5:(2,6),6:(2,6),7:(0,8),8:(0,8),9:(0,8)}
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def chord(p,h,a):
 c=add((2*p[0],2*p[1]),lit.rot((-1,-1),h));return c,add(c,lit.rot(ST[a],h))
def contact(a,b,c,d):
 u,v,z=sub(b,a),sub(d,c),sub(c,a);de=cross(u,v)
 if de:
  s,q=Q(cross(z,v),de),Q(cross(z,u),de)
  return dict(s=str(s),t=str(q),point=[str(a[k]+s*u[k]) for k in (0,1)]) if 0<=s<=1 and 0<=q<=1 else None
 if cross(z,u):return None
 k=0 if u[0] else 1
 x,y=Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k]);lo=max(Q(0),min(x,y));hi=min(Q(1),max(x,y))
 return dict(s_interval=[str(lo),str(hi)],point=[str(a[k]+lo*u[k]) for k in (0,1)]) if lo<=hi else None

goal=(2,4,0);lastC=(1,4,1);C=G[1]['word'][len(G[0]['word']):]
local=lit.rot(sub(t,lastC[:2]),-lastC[2]);assert local==(2,0)
assert lit.trace(C)['first'][local]==('R',8)
ce=lit.trace(C)['pose'];assert add(lastC[:2],lit.rot(ce[:2],lastC[2]))==goal[:2]
assert (lastC[2]+ce[2])%4==goal[2]
source_chord=chord((0,0),0,7);rows=[];survivors=[]
for si in (7,8,9):
 assert list(t) in G[si]['outputs']
 for n in range(8):
  h=(-n)%4
  for a in keep:
   for z in G[a]['inputs']:
    p=sub(t,lit.rot(z,h));key=(compact[si],compact[a],*p,h,*t,min(n,5))
    req=lit.trace(G[a]['word']+lit.M);assert req['feasible']
    ctx={add(p,lit.rot(q,h)) for q in req['first']}
    hit=contact(*source_chord,*chord(p,h,a));c=G[a]['name'].count('C')
    if (sum(p)+h)%2:why='sector'
    elif key in CT:why='signed_count5'
    elif ctx&L:why='permanent_left_star_complete_context'
    # The retiring full packet may CONTAIN the final C at clock7. It need
    # only finish by foreign entry8; do NOT demand completion by clock7.
    elif n+c>8:why='full_tail_after_foreign'
    elif hit is not None:
      why='earlier_closed_source_U_chord_contact'
      # No immediately adjacent atomic-source-end exception is suppressed.
      assert n>G[si]['name'].count('C')
      assert p!=(0,4) or h!=0
    else:
      why='endpoint_obligation'
      d=lit.rot(G[a]['endpoint'][:2],h);ep=(*add(p,d),(h+G[a]['endpoint'][2])%4)
      assert (n,a,p,ep,c) in [(6,0,(1,3),(0,2,2),0),(6,4,(1,5),(0,2,2),0),(6,7,(0,6),(0,2,2),0)]
      survivors.append(dict(source=G[si]['name'],consumer=G[a]['name'],entry_clock=n,pose=(*p,h),full_exit=ep,remaining_Cs_to_last_C_entry=1))
    rows.append(dict(source=G[si]['name'],source_id=si,age=n,consumer=G[a]['name'],consumer_id=a,input=z,
      pose=(*p,h),count_key=key,reason=why,permanent_star_context_hits=sorted(ctx&L),base_contact=hit))
co=Counter(r['reason'] for r in rows)
assert len(rows)==552
assert co=={'sector':276,'signed_count5':189,'permanent_left_star_complete_context':69,
 'earlier_closed_source_U_chord_contact':9,'endpoint_obligation':9}
assert len(survivors)==9
# Exact one-C atomic factorization: S zero-run, C_S, E zero-run.
zs=[lit.rot(z,2) for z in ((1,1),(1,3),(0,4))]
ze=[lit.rot(z,1) for z in ((1,1),(1,3),(0,4))]
cs=lit.rot(ce[:2],2);assert cs==(0,-1)
assert all(z[1]<=0 for z in zs+ze)
assert 2+cs[1]==1<lastC[1]
deps=[GP,CP,HERE/'check_foreign_return_interfaces.py',
 HERE/'U_foreign_prefix_renewal_return_frozen_20261023_2204/manifest.json',
 W/'U_left_star_permanence_frozen_20261023_1918/manifest.json',
 W/'U_entry_simplicity_frozen_20261023_1616/manifest.json',
 ROOT/'seven_word_spatial_return_2026-10-23/foreign_U_predecessor_ports_manifest.json']
out=dict(status='AUTHOR_EXACT_FINITE_RETIREMENT_AND_UNBOUNDED_CONE_PENDING_INDEPENDENT_REPLAY',
 scope='Only genuine U-source/common-F-prefix chronological first contact after uninterrupted complete-eight interval. Not later Q/B tails or D/C/V earlier sources; no generic prefix search.',
 goal_pose=goal,foreign_types=['F','Q'],foreign_entry_clock=8,last_C_pose=lastC,last_C_entry_clock=7,
 mandatory_retired_original_arm=t,last_C_arm_local=local,last_C_first_read=['R',8],
 query_counts=dict(co),queries=rows,remaining_clearer_obligations=survivors,
 one_C_cone=dict(from_pose=(0,2,2),from_clock=6,target=lastC,target_clock=7,
  S_zero_steps=zs,C_S=cs,E_zero_steps=ze,maximum_possible_final_y=1,required_final_y=4),
 full_tail_interface='A retiring full consumer may include the final C; no completion before last-C entry is assumed. The surviving nine consumers are all plain zero-C bases.',
 conclusion='The final two F/Q(2,4,N) age8/precedingC U-source prefix interfaces are excluded. Hence no creating U-base chord can be the earlier source of the first common-F-prefix contact in this exact scope.',
 dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in deps})
(HERE/'U_foreign_prefix_arm_guard.json').write_text(json.dumps(out,indent=2)+'\n')
print('552 rows:',dict(co));print('all nine obligations exit(0,2,S)at6; one-C y<=1 cannot reach C(1,4,E)at7')
