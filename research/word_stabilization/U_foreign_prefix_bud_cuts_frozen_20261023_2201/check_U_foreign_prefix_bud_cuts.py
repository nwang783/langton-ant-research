"""Finite dependency-bound U-source first-foreign-prefix contact cuts.
No continuation/prefix search. All ages refer to actual full producers.
"""
from pathlib import Path
from collections import Counter
import json, hashlib, importlib.util

ROOT=Path('/workspace/shared/langton'); HERE=Path(__file__).resolve().parent
W=ROOT/'core_periodicity_new'
GP=W/'chronology_dcuv/literal_residual_geometry.json'
CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv'
WP=HERE/'shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
IP=ROOT/'seven_word_spatial_return_2026-10-23/foreign_first_contact_interface.json'
G=json.loads(GP.read_text())['geometry']; keep=[0,1,4,5,6,7,8,9]; compact={a:i for i,a in enumerate(keep)}
COUNT={tuple(map(int,l.split()[:8])) for l in CP.read_text().splitlines()}
WORDS=[a['word'] for a in json.loads(WP.read_text())['macro_words']]
K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}
sp=importlib.util.spec_from_file_location('literal_foreign',HERE/'check_foreign_return_interfaces.py')
lit=importlib.util.module_from_spec(sp);sp.loader.exec_module(lit)
rot=lit.rot

def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def guard_rows(sources,output,ages):
    rows=[]
    for s in sources:
      assert list(output) in G[s]['outputs']
      for n in ages:
        h=(-n)%4
        for a in keep:
          for z in G[a]['inputs']:
            p=sub(output,rot(z,h))
            key=(compact[s],compact[a],*p,h,*output,n)
            why='sector' if (sum(p)+h)%2 else 'signed_count5' if key in COUNT else 'UNEXCLUDED'
            assert why!='UNEXCLUDED',(s,output,n,a,z,p)
            rows.append(dict(source=G[s]['name'],source_id=s,output=output,age=n,
                             consumer=G[a]['name'],consumer_id=a,input=z,pose=(*p,h),
                             key=key,reason=why))
    return rows

# A U-base exit bud has the SAME C birth clock as its actual full producer.
# All C tails preserve this physical fresh output.
bud=(1,3)
bud_rows=guard_rows((7,8,9),bud,(3,4))
assert len(bud_rows)==138
assert Counter(r['reason'] for r in bud_rows)=={'sector':69,'signed_count5':69}
assert G[7]['endpoint']==[0,4,0]

interface=json.loads(IP.read_text())
ports=[]
for f,rr in interface['U_source_star_filters'].items():
  for r in rr:
    if r['reason']=='unexcluded_necessary_interface':
      ports.append((f,tuple(r['foreign_pose']),tuple(r['permitted_C_ages'])))
assert sorted(ports)==sorted([
 ('F',(-2,3,3),(1,5)),('F',(1,3,0),(4,8)),('F',(2,4,0),(4,8)),
 ('F',(3,3,0),(4,8)),('Q',(1,3,0),(4,8)),('Q',(2,4,0),(4,8)),
 ('B',(1,3,0),(4,8))])

age4=[]
for f,p,ages in ports:
  if ages!=(4,8):continue
  a={'F':4,'Q':5,'B':6}[f]
  local=rot(sub(bud,p[:2]),-p[2]);t=lit.trace(WORDS[a]+lit.M)
  assert t['feasible']
  read=t['first'][local]
  reason='entry_core' if local in K else 'before_white' if read[0]=='R' else 'WRONG'
  assert reason!='WRONG'
  age4.append(dict(foreign=f,pose=p,source_bud_global=bud,source_bud_local=local,
                   reason=reason,first_read_turn=read[0],first_read_phase=read[1]))
assert len(age4)==6
assert Counter(r['reason'] for r in age4)=={'entry_core':5,'before_white':1}

# At age one the exact atomic overapproximation is N zero-run, C_N, W zero-run.
# Every zero-run y increment is nonnegative and C_N contributes +1, so y>=5.
oneC=dict(source_U_base_exit=(0,4,0),N_zero_steps=[rot(z,0) for z in ((1,1),(1,3),(0,4))],
          C_N=rot((0,1),0),W_zero_steps=[rot(z,3) for z in ((1,1),(1,3),(0,4))],
          goal=(-2,3,3))
assert min(z[1] for z in oneC['N_zero_steps'])>=0
assert min(z[1] for z in oneC['W_zero_steps'])>=0
assert oneC['source_U_base_exit'][1]+oneC['C_N'][1]>oneC['goal'][1]

# Age-five west port: q is in the foreign entry core, hence retired strictly
# earlier. Signed1954/2027 give V/VC at(-1,5,S), start age two (UC impossible).
Fpose=(-2,3,3); q=(-1,2); cleanup=(-1,5,2)
assert rot(sub(q,Fpose[:2]),-Fpose[2])==(-1,-1)
assert rot(sub(Fpose[:2],cleanup[:2]),-cleanup[2])==(1,2)
assert (Fpose[2]-cleanup[2])%4==1
common=(2,0)
common_rows=guard_rows((4,5),common,range(3))
assert len(common_rows)==138
assert Counter(r['reason'] for r in common_rows)=={'sector':80,'signed_count5':58}
ends=[]
for a in (0,4,7):
  for z in G[a]['inputs']:
    p=sub(common,rot(z,1)); ep=add(p,rot(G[a]['endpoint'][:2],1))
    assert ep[0]>=2
    ends.append(dict(consumer=G[a]['name'],input=z,pose=(*p,1),base_exit=ep,
                     sector_compatible=(sum(p)+1)%2==0))
assert len(ends)==8
assert all(rot(z,1)[0]>=0 for z in ((1,1),(1,3),(0,4)))
common_global=add(cleanup[:2],rot(common,cleanup[2]))
foreign_local=rot(sub(common_global,Fpose[:2]),-Fpose[2])
assert common_global==(-3,5) and foreign_local==(2,1)
assert lit.trace(WORDS[4]+lit.M)['first'][foreign_local]==('R',7)

dependencies=[GP,CP,WP,IP,
 ROOT/'seven_word_spatial_return_2026-10-23/foreign_first_contact_manifest.json',
 W/'atomic_exit_bud_frozen_20261023_1325/manifest.json',
 W/'U_recycled_q_consumer_frozen_20261023_1954/manifest.json',
 W/'U_q_source_history_frozen_20261023_2027/manifest.json',
 HERE/'check_foreign_return_interfaces.py']
PP=ROOT/'seven_word_spatial_return_2026-10-23/foreign_U_predecessor_ports_manifest.json'
assert hashlib.sha256(PP.read_bytes()).hexdigest()=='53a51ea0fe95433edb7448ba1990170b2673bfd7fd20cd716c0f80ef9d05cf28'
dependencies.append(PP)
combined=[dict(foreign=f,pose=p,age=8,preceding_C=True) for f,p,ages in ports
          if ages==(4,8) and p!=(1,3,0)]
assert [(r['foreign'],r['pose']) for r in combined]==[
 ('F',(2,4,0)),('F',(3,3,0)),('Q',(2,4,0))]
out=dict(status='AUTHOR_EXACT_FIXED_U_SOURCE_FOREIGN_PREFIX_CUTS_PENDING_INDEPENDENT_REPLAY',
 scope='Actual U-family creating producer, complete-eight interval until the FIRST foreign. Only source-U/common-F-prefix first-contact interfaces. No tail-contact closure, full proxy simplicity, physical attainment or global seven-word cover.',
 source_exit_bud_age3_4_queries=bud_rows,source_exit_bud_maturity='Atomic1325 covers ages0,1,2; these rows cover3,4; full C tails preserve bud.',
 age4_port_cuts=age4,west_age1_endpoint_cone=oneC,
 west_age5=dict(foreign_pose=Fpose,q_entry_core_local=(-1,-1),forced_cleanup=cleanup,
   cleanup_source_age=2,UC_source='q permanent: impossible',
   common_output_age0_1_2_queries=common_rows,age3_zero_C_consumer_endpoints=ends,
   remaining_Cs=3,positive_C_tail='Cannot finish strictly before the full foreign entry at the same clock.',
   foreign_normalized_to_cleanup=(1,2,1),common_output_global=common_global,
   common_output_foreign_local=foreign_local,foreign_first_read=['R',7]),
 independent_remaining_prefix_ports=[dict(foreign=f,pose=p,age=8,preceding_C=True)
   for f,p,ages in ports if ages==(4,8)],
 combined_with_signed_predecessor_ports=combined,
 dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in dependencies})
HERE.joinpath('U_foreign_prefix_bud_cuts.json').write_text(json.dumps(out,indent=2)+'\n')
print('138 U-bud age3/4 queries69sector+69count; six age4 ports cut.')
print('138 cleanup-common age0/1/2 queries80sector+58count; eight E endpoints x>=2; west ages1/5 cut.')
