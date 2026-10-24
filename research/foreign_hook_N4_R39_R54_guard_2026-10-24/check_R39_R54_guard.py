"""All ordinary preparations: genuine foreign R39/R54 repair obstruction."""
from pathlib import Path
from collections import Counter
import importlib.util,json
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('l',R/'word_stabilization/check_foreign_return_interfaces.py');l=importlib.util.module_from_spec(s);s.loader.exec_module(l);s=importlib.util.spec_from_file_location('o',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');o=importlib.util.module_from_spec(s);s.loader.exec_module(o);W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return *q,h
ports=[]
for a in'DVU':
 for inp in map(tuple,l.literal_geometry(W[a])['inputs']):
  ee=after(W[a],(*l.rot((-inp[0],-inp[1]),1),1));nn=after(W[a],(-inp[0],-inp[1],0))
  assert ee[0]+ee[1]>=-1 and nn[0]>=0 and inp[0]>=-1 and inp[1]>=1
  ports.append(dict(atom=a,input=inp,E_RAW_exit_relative_tag=ee,E_exit_H_lower_bound=-1,N_RAW_exit_relative_tag=nn,N_exit_x_lower_bound=0,N_input_y_minimum=inp[1],W_input_x_minimum=inp[0]))
assert len(ports)==8 and l.literal_geometry(W['C'])['inputs']==[]
CU=l.trace(W['C']+W['U']+l.M);assert not CU['feasible']and(CU['conflict_read'],CU['previous_read'])==(29,1)
allcases=[]
for A,offset in[('Q',(0,0)),('B',(1,-1))]:
 geom=l.literal_geometry(W[A]);ep=tuple(geom['endpoint']);trA=l.trace(W[A]+l.M)
 SQ={(-3,-3),(-2,-3),(-1,-3),(-1,-2)};S={add(p,offset)for p in SQ};g=add((0,-5),offset);r=add((1,-3),offset)
 births=[]
 for name,p,cell,tick in[('g_R39',g,(-4,1),39),('r_R54',r,(-5,-1),54)]:
  original=add(ep[:2],l.rot(p,2));assert original==cell and trA['last'][original]==('R',tick)and list(original)in geom['outputs']and p not in l.K
  assert p[1]<=-1
  births.append(dict(name=name,postforeign_cell=p,actual_A_cell=original,actual_last_R_tick0=tick,actual_last_R_read1=tick+1,external_CURRENT_at_A_exit=True))
 # All first losses at clocks0/1 are impossible from the negative-y cones.
 # At clock2 directly enumerate each tag's complete eight S-input roles.
 tables={}
 for name,tag in[('r_R54',r),('g_R39',g)]:
  rows=[]
  for a in'DVU':
   tr=l.trace(W[a]+l.M)
   for inp in map(tuple,l.literal_geometry(W[a])['inputs']):
    head=add(tag,inp);rec=dict(atom=a,input=inp,S_head=(*head,2))
    if(sum(head)+2)%2:rec['reason']='sector'
    else:
     core=[q for q in sorted(S)if l.rot(sub(q,head),2)in l.K]
     white=[q for q in sorted(S)if(v:=l.rot(sub(q,head),2))in tr['first']and tr['first'][v][0]=='R']
     if core or white:rec.update(reason='young_hook_CURRENT_core_or_first_WHITE',hook_CORE=core,hook_WHITE=white)
     else:
      assert name=='g_R39'and a=='D'and inp==(0,1)and head==add(g,(0,1))
      local=l.rot(sub(r,head),2);assert local==(-1,-1)and local in l.K
      rec.update(reason='same_r_R54_CURRENT_in_D_entry_CORE',r_local=local)
    rows.append(rec)
  tables[name]=rows
 assert Counter(q['reason']for q in tables['r_R54'])=={'sector':6,'young_hook_CURRENT_core_or_first_WHITE':2}
 assert Counter(q['reason']for q in tables['g_R39'])=={'sector':2,'young_hook_CURRENT_core_or_first_WHITE':5,'same_r_R54_CURRENT_in_D_entry_CORE':1}
 # r first: the hook is signed current throughclock3; no g premise is used.
 # g second: r has now been proved current at every markedclock<=2.
 targets=[]
 for i,base in enumerate([(-1,-5),(0,-4)]):
  target=add(base,offset);needed=g if i==0 else r;N_weight_H_min=2;E_terminal_H_max=sum(target)-N_weight_H_min-1;E_g_loss_H_min=sum(needed)-1
  assert E_g_loss_H_min>E_terminal_H_max and needed[0]>target[0]
  local=sub(needed,target);fr=l.trace(W['U']+l.M)['first'].get(local)
  if i==0:assert local==(1,0)and local in l.K;cut='same_g_R39_CURRENT_in_U_entry_CORE'
  else:assert local==(1,1)and fr==('R',6);cut='same_r_R54_BLACK_at_actual_U_R6'
  targets.append(dict(target_U_N=target,postforeign_C_entry_clock=4,needed_same_foreign_tag='g_R39'if i==0 else'r_R54',target_H=sum(target),nonempty_final_N_H_minimum=2,E_terminal_H_max=E_terminal_H_max,minimum_E_tag_loss_RAW_exit_H=E_g_loss_H_min,minimum_N_tag_loss_RAW_exit_x=needed[0],target_x=target[0],literal_target_local=local,exact_target_cut=cut,actual_R_owner=o.describe('U',6)if i else None))
 allcases.append(dict(foreign=A,translation=offset,actual_FOREIGN_R39_R54_births=births,all16_clock2_tag_input_alignments=tables,two_N4_target_obligations=targets))
out=dict(status='AUTHOR_ALL_PREPARATIONS_TWO_FOREIGN_TAG_N4_GUARD_PENDING_REVIEW',scope='After actual Q/B, no arbitrary ordinary RAW suffix with actual finalM11 reaches either of its two N4 hook-loss U gates. No U ancestry, global simplicity, firstpost-letter or ordinary rail-length bound. W5 and hook-missing contacts remain open.',all8_true_input_RAW_exit_coordinate_inequalities=ports,actual_C_external_input_empty=True,actual_RAW_C_U_noncontinuation=CU,source_cases=allcases,chronological_dependency_order='Signed four-hook CURRENT throughC3 -> initial r_R54 CURRENT throughC2 by six sectors/two hook cuts -> initial g_R39 CURRENT throughC2 by sectors/fivehookcuts/one rCORE -> exact E/N endpoint reserves at selectedN4 targets -> gCORE or r firstWHITE contradiction. No circular reserve assumption.',unbounded_endpoint_argument='N0 andW1 cannot consume initial negative-y tags. E3 lossRAWexitH>=tagH-1, while C4+nonemptyNrail forces lastE H<=targetH-3; these bounds contradict. N4 lossRAWexitx>=tagx>targetx cannot return under monotoneN x. C hasI0. Nrail empty is actualCU RAW contradiction.',no_postFOREIGN_JO_age_import_or_unread_CORE_omission=True,no_W5_hook_miss_secondFOREIGN_or_simplicity_or_capture_claim=True)
(H/'R39_R54_guard.json').write_text(json.dumps(out,indent=2)+'\n');print('Both N4 U gates for Q/B excluded under arbitrary ordinary preparations: 8 endpoint roles,32 actual tag/input cases and4 exact target obligations; no firstpost-letter or simplicity premise.')
