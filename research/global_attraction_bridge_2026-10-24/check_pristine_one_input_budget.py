"""Complete phase-direction interior check and signed one-black decomposition arithmetic."""
import json,hashlib
from pathlib import Path
from check_fresh_record_trap_bridge import geometry
P=Path(__file__).parent;ROOT=P.parent
A=json.loads((P/'OUTWARD_RECORD_GUARDS_CHECKED.json').read_text());H=A['canonical_period'];normals=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
def rot(v,r):
 x,y=v
 for _ in range(r):x,y=y,-x
 return(x,y)
cover=[]
for h in range(4):
 for i in range(104):
  w=H[i:]+H[:i];Q,d,he=geometry((0,0),h,w);assert he==h
  for n in normals:
   f=lambda q:sum(n[j]*q[j]for j in range(2))
   record=all(f((q[0]-d[0],q[1]-d[1]))<0 for q in Q)
   if not record:continue
   assert f(d)>0
   matches=[]
   for block in A['normal_catalog']:
    for r in block['records']:
     for k in range(4):
      if rot(block['outward_normal'],k)==n and(r['normalized_heading']+k)%4==h and r['cycle_word']==w:
       matches.append((block['outward_normal'],r['phase'],k));assert r['max_old_read_time']<=270
   assert len(matches)==1,(h,i,n,matches)
   cover.append(dict(heading=h,cyclic_phase=i,normal=n,match=matches[0]))
assert len(cover)==32
fringes=[]
for length in range(1000):
 times=[t for t in range(length)if t<104 or length-t<271];assert len(times)<=min(length,375)
 if length in(0,1,103,104,270,271,374,375,500):fringes.append([length,len(times)])
audit=json.loads((ROOT/'audits/check_one_black_budget_independent.json').read_text());tab=audit['tables'];B=9977
cases=[('prefix',tab['prefixTimes']['maximum'],1),('inert',B,1),('active',B+tab['actualActiveTimes']['maximum'],1),('shallow',B+tab['actualLaneTimes']['maximum'],1),('ordinary_deep',B+tab['pristineLaneTimes']['maximum'],2),('exceptional_deep',B+tab['pristineLaneTimes']['maximum']+7994,3)]
records=[dict(case=name,arbitrary_length_bound=L,standard_piece_bound=s,pristine_bad_record_time_bound=L+375*s)for name,L,s in cases]
assert max(x['pristine_bad_record_time_bound']for x in records)==106633
result=dict(status='AUTHOR all-word pristine standard-interior lemma and one-old-input resource bound; independent audit pending',complete_previous104_phase_direction_cover=cover,largest_old_guard_first_read=270,required_future_standard_length=271,conservative_boundary_allowance_per_piece=375,finite_fringe_controls=fringes,signed_one_black_decomposition_cases=records,uniform_time_cut_bound=106633,uniform_eight_direction_marked_bound=853064,source_audit_sha256=hashlib.sha256((ROOT/'audits/check_one_black_budget_independent.json').read_bytes()).hexdigest(),source_note_sha256=hashlib.sha256((ROOT/'nonlinear_global_budget_2026-10-23/one_black_uniform_defect_budget.md').read_bytes()).hexdigest())
(P/'PRISTINE_ONE_INPUT_BUDGET_CHECKED.json').write_text(json.dumps(result,indent=2)+'\n');print(dict(phase_direction_cases=len(cover),bounds=records,uniform=106633))
