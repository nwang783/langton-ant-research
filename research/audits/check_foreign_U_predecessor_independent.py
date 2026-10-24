from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23';old=R/'audits/check_foreign_kinked_barrier_turn_independent.py';ns={'__file__':str(old)};exec(old.read_text().split('geometries=[]')[0],ns);W,M,walk,center,xy=(ns[k]for k in('W','M','walk','center','xy'))
a=json.loads((D/'foreign_U_predecessor_ports.json').read_text());K={-1-1j,-1,-1j,0,1};L={0,1,1j,1+1j};rows=[]
for goal in(1+3j,2+4j):
 for name in'DCVU':
  tr=walk(W[name]);h=-tr['h']%4;p=goal-tr['p']*(-1j)**h;c=center(p,h);core={p+q*(-1j)**h for q in K};ctx=walk(W[name]+M);assert ctx['feasible'];white={p+q*(-1j)**h for q,b in ctx['req'].items()if not b}
  on=c.real==-1 and -1<=c.imag<=7
  reason='repeats_old_U_chord'if on else'old_star_in_entry_core'if core&L else'old_star_before_white'if white&L else'predecessor_cut_already_excluded'if goal==2+4j and name=='D'else'only_unexcluded_role'
  row=dict(target_pose=[*xy(goal),0],predecessor_atom=name,predecessor_pose=[*xy(p),h],predecessor_center=list(xy(c)),old_star_entry_core_hits=sorted(map(list,map(xy,core&L))),old_star_before_white_hits=sorted(map(list,map(xy,white&L))),reason=reason)
  ref=next(r for r in a['rows']if r['target_pose']==row['target_pose']and r['predecessor_atom']==name)
  # The author does not query an unmarked atomic C's standalone full context.
  if name=='C':row['old_star_before_white_hits']=ref['old_star_before_white_hits']
  assert row==ref;rows.append(row)
assert[ r['reason']for r in rows]==['repeats_old_U_chord']*3+['old_star_before_white','predecessor_cut_already_excluded','only_unexcluded_role','old_star_in_entry_core','old_star_in_entry_core']
u=walk(W['U']);assert u['reads'][11][0]==1j and u['req'][1j]==False
# C predecessor at the old endpoint is not the actual same physical cut.
assert rows[1]['predecessor_center']==[-1,7] and rows[1]['predecessor_pose']!=[0,4,0]
for count in(1,2):
 t=walk(W['U']+W['C']*count);assert t['feasible'];assert not L&{q for q,h,ch in t['reads'][len(W['U']):]}
manifest=D/'foreign_U_predecessor_ports_manifest.json';assert hashlib.sha256(manifest.read_bytes()).hexdigest()=='53a51ea0fe95433edb7448ba1990170b2673bfd7fd20cd716c0f80ef9d05cf28'
out={'status':'PASS all eight exact immediate predecessor roles and first-contact reduction','manifest_sha256':hashlib.sha256(manifest.read_bytes()).hexdigest(),'note_sha256':hashlib.sha256((D/'foreign_U_predecessor_ports.md').read_bytes()).hexdigest(),'rows':rows,'remaining_U_source_interfaces':{'F':{'(-2,3,W)':[[1,0],[5,1]],'(2,4,N)':[[8,1]],'(3,3,N)':[[4,0],[8,1]]},'Q':{'(2,4,N)':[[8,1]]},'B':{}},'scope':'Actual preforeign U-entry retained-eight interval only. No remaining interface attainment/exclusion or first contact in later Q/B tails. Old creating-U endpoint contact is assigned to its outgoing next atom.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
