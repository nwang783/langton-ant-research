"""Joint first-S4-loss wrapper. No fixed rail counts or foreign iteration."""
from pathlib import Path
from collections import Counter
import json,hashlib,importlib.util
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def sub(p,q):return p[0]-q[0],p[1]-q[1]
def local(g,p):return l.rot(sub(g,p[:2]),(-p[2])%4)
F15={(-1,-1),(-1,0),(-1,1),(0,0),(0,1),(1,0),(1,1),(1,2),(2,0),(2,1),(-4,1),(-4,2),(-3,2),(-2,1),(-2,-1)}
old13=F15-{(2,0),(2,1)};HK={(-1,-1),(-2,-1),(-3,-1),(-3,-2)}
a=(-3,3);r=(-4,3)
fields={'F_unspent':F15,'F_paired':old13,'QB_unspent':F15|HK,'QB_paired':old13|HK}
B=json.loads((R/'C4_foreign_original_hook_loss_2026-10-24/C4_original_hook_loss.json').read_text())
F=json.loads((R/'foreign_C5_left_hole_frontier_2026-10-24/C5_left_hole.json').read_text())
# Bind the source-only C5 proof interface, not its target-specific final E step.
assert F['always_CURRENT_through_C3_old13']==[list(z)for z in sorted(old13)]
assert F['proof_steps'][2].startswith('At W3 cuts r may genuinely be alive CORE:')
assert F['proof_steps'][4].startswith('At an S4 physical last-R producer')
S=F['all216_CORE_inclusive_last_RAW_R_roles']
assert[(z['producer'],z['ENTRY'])for z in S if z['hole']==list(r)and z['epoch_heading']==2 and z['route']=='possible_funder']==[('U',[-4,4,2])]
assert not[z for z in S if z['hole']==list(a)and z['epoch_heading']==2 and z['route']=='possible_funder']
records=[]
for name,field in fields.items():
 rows=[]
 for tag in sorted(field):
  for atom in'DVU':
   ct=l.trace(W[atom]+l.M)
   for slot in map(tuple,l.literal_geometry(W[atom])['inputs']):
    p=(*sub(tag,l.rot(slot,2)),2)
    row=dict(original=tag,consumer=atom,ENTRY=p,true_input=slot,actual_L=o.describe(atom,ct['first'][slot][1]))
    if(sum(p[:2])+2)%2:route='sector'
    else:
     bad=[]
     for g in sorted(field):
      q=local(g,p);f=ct['first'].get(q)
      if q in l.K or f and f[0]=='R':bad.append(dict(SAME_original=g,local=q,first=f,reason='ENTRY_CORE'if q in l.K else'first_WHITE'))
     row['current_field_conflicts']=bad
     if bad:route='held_field'
     else:
      assert atom=='U'and p in[(-5,3,2),(-4,4,2)]
      hole,tick=(r,1)if p==(-5,3,2)else(a,14)
      assert ct['first'][local(hole,p)]==('L',tick)
      row['WHITE_hole']=hole;row['own_BLACK_request']=o.describe(atom,tick)
      row['hole_scope']='r WHITE at every completed S4 cut'if hole==r else'a WHITE specifically at U(-4,4,S) by x-frontier'
      route='source_only_f01_WHITE_hole'
    row['route']=route;rows.append(row)
 counts=dict(Counter(z['route']for z in rows))
 assert counts['source_only_f01_WHITE_hole']==5
 assert len(rows)==8*len(field)
 records.append(dict(field_name=name,SAME_current_at_S4_start=sorted(field),counts=counts,all_first_CURRENT_loss_rows=rows))
assert sum(len(z['all_first_CURRENT_loss_rows'])for z in records)==480
bindings=[]
for A in'FQB':
 for branch in['unspent','paired']:
  k=('F_'if A=='F'else'QB_')+branch;field=fields[k]
  row=next(z for z in B['theorem_B_all_C4_original_hook_loss']['source_branch_cases']if z['source']==A and z['C3_state_branch']==('N2_paired'if branch=='paired'else branch))
  assert field<=set(map(tuple,row['all_current_at_S4_start']))
  hook={(-1,-1),(-2,-1)}if A=='F'else HK
  assert hook<=field
  bindings.append(dict(source=A,C3_branch=branch,joint_field=k,all_retained_originals_CURRENT_through_ordinary_S4=True,protected_hook=sorted(hook)))
# C external input I=0 and actual EXIT CORE capture cannot lose an external tag.
assert l.literal_geometry(W['C'])['inputs']==[]
C=l.trace(W['C']+l.M)
assert all(q in l.K for q,(turn,t)in C['first'].items()if turn=='L')
D=['C4_foreign_original_hook_loss_2026-10-24/manifest.json','audits/check_C4_original_hook_loss_independent.json','foreign_C5_left_hole_frontier_2026-10-24/manifest.json','audits/check_FOREIGN_C5_left_hole_independent.json','word_stabilization/check_foreign_return_interfaces.py','literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Any actual F/Q/B source ENTRY0N followed only ordinary RAWs through EXACT C4/S4, with the actual complete contexts supplied by a subsequent complete nextFOREIGN+M. All thirteen guaranteed original source outputs, and all four sourceQ/B hook originals, stay SAME CURRENT at every completed marked cut through the ordinary S4 section. The unspent branch retains all15. This is not a claim about the paired nine new outputs.',all480_joint_first_S4_CURRENT_loss_rows=records,all6_source_branch_bindings=bindings,source_only_f01_hole_premise_lift='The N/W/S portion of f01 is independent of its final nextFOREIGN target: it proves rWHITE at S4 start and all later S4 marked cuts; aWHITE at the sole high U(-4,4,S) funder. Its use of old13 at high funder ENTRY is proved from eight loss-exit inequalities and does NOT assume global S4 old13 persistence. Thus this joint first-loss argument is noncircular.',unconditional_one_next_FOREIGN_C4_corollary='For sourceQ/B and exactly4 ordinary Cs, all4 SAME hook originals are CURRENT at nextFOREIGN ENTRY by this joint table. Signed b961 excludes their physical first deletion in that next FOREIGN RAW or its real M, and independently checks all15 actual exitCORE capture roles. Hence all4 are SAME CURRENT at nextFOREIGN RAW EXIT and physically SAME BLACK through its supplied actual M. The earlier conditional b961 corollary is invoked once, never iterated.',limits=['An attempted impossible U gate may physically consume earlier inputs before its failing BLACK request; no fine-cut or failed-attempt permanence is asserted.','No paired-new9 permanence or equality of the whole postFOREIGN field.','No currentness through ordinary E5, all-C5 classification, arbitrary-tail seal or third-FOREIGN transfer.','Do not call r WHITE at every W3 cut; real transient CORE repairs remain in signed f01 regression.','No U ancestry, proxy simplicity, global-first-contact, rail-length or ant-language coverage premise/conclusion.'],dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest()for p in D})
(H/'C4_joint_hook.json').write_text(json.dumps(out,indent=2)+'\n')
print('480 joint S4 first-loss rows;6 source/branch bindings; two source-only WHITE-hole gates; one-nextFOREIGN C4 corollary.')
