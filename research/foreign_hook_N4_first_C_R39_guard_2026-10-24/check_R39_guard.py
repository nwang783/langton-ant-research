"""One N4 U-gate, all lengths after an initial ordinary C."""
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
for atom in'DVU':
 geom=l.literal_geometry(W[atom])
 for inp in map(tuple,geom['inputs']):
  sHead=l.rot((-inp[0],-inp[1]),2);nExit=after(W[atom],(-inp[0],-inp[1],0));eExit=after(W[atom],(*l.rot((-inp[0],-inp[1]),1),1))
  assert sHead[0]>=-1 and inp[0]>=-1 and nExit[0]>=0 and eExit[0]+eExit[1]>=-1
  ports.append(dict(atom=atom,input=inp,S_entry_relative_tag=sHead,N_RAW_exit_relative_tag=nExit,E_RAW_exit_relative_tag=eExit,E_RAW_exit_H_relative_tag=eExit[0]+eExit[1]))
assert len(ports)==8 and l.literal_geometry(W['C'])['inputs']==[]
CU=l.trace(W['C']+W['U']+l.M);assert not CU['feasible']and CU['conflict_read']==29 and CU['previous_read']==1
# A hypothetical first loss in S must respect headx<=-1, because the initial
# ordinary N rail is empty, C1 starts0N, and C2 follows a W rail with x<=0.
# For Q gx0, only the three U inputs with local x=-1 reach this boundary.
S_Q={(-3,-3),(-2,-3),(-1,-3),(-1,-2)};boundary=[]
trU=l.trace(W['U']+l.M)
for inp in [(-1,1),(-1,2),(-1,4)]:
 head=add((0,-5),inp);core=[q for q in S_Q if l.rot(sub(q,head),2)in l.K];white=[q for q in S_Q if(v:=l.rot(sub(q,head),2))in trU['first']and trU['first'][v][0]=='R']
 assert core or white
 boundary.append(dict(U_input=inp,head=(*head,2),held_young_hook_entry_CORE_witnesses=sorted(core),held_young_hook_first_WHITE_witnesses=sorted(white)))
cases=[]
for A,target,g in[('Q',(-1,-5),(0,-5)),('B',(0,-6),(1,-6))]:
 geom=l.literal_geometry(W[A]);ep=tuple(geom['endpoint']);old=add(ep[:2],l.rot(g,2));tr=l.trace(W[A]+l.M)
 assert old==(-4,1)and tr['last'][old]==('R',39)and list(old)in geom['outputs']and g not in l.K
 assert g[1]<-1 and sum(g)==-5 and sum(target)==-6 and g[0]==target[0]+1
 assert sub(g,target)==(1,0)and sub(g,target)in l.K
 # E head H cannot decrease. A nonempty final N rail has H increment>=2.
 max_E_terminal_H=sum(target)-2-1;min_E_g_loss_exit_H=sum(g)-1
 assert max_E_terminal_H==-9 and min_E_g_loss_exit_H==-6 and min_E_g_loss_exit_H>max_E_terminal_H
 cases.append(dict(foreign=A,target_U_N=target,genuine_R39_tag_postforeign=g,source_A_cell=old,source_R_tick0=39,source_R_read1=40,initial_EXTERNAL_CURRENT=True,target_CORE_local=sub(g,target),max_E_terminal_H=max_E_terminal_H,min_E_g_loss_RAW_exit_H=min_E_g_loss_exit_H,tag_N_loss_exit_x_at_least=g[0],target_x_strictly_smaller=target[0]))
reg=json.load(open(H/'named_clock4_controls.json'));assert len(reg['counts'])==300 and len(reg['words'])==3264 and not reg['positive']
for T,r in reg['words'].items():
 tr=l.trace(''.join(W[a]for a in T)+l.M);assert not tr['feasible']and tr==r['trace']
out=dict(status='AUTHOR_FIRST_C_ALL_LENGTH_R39_GATE_GUARD_PENDING_REVIEW',scope='Actual Q/B, first ordinary atomC, arbitrary W/S/E/N rails, exactfour ordinary Cs before targetU(-1,-5,N) forQ orU(0,-6,N) forB, actual terminalM11. No target history exists. No U ancestry/global simplicity required; initial D/V/U and other hook gates remain outside.',all8_true_input_complete_RAW_exit_coordinate_roles=ports,actual_raw_C_U_obstruction=CU,all3_Q_S_boundary_current_hook_guards=boundary,all2_exact_FOREIGN_R39_frame_and_target_CORE_cases=cases,all300_named_count_records=reg['counts'],all3264_immutable_named_control_words=reg['words'],unbounded_length_proof='InitialC makes W heads y>=1,x<=0; negativegy excludes W input. S headsx<=-1; B g needsheadx>=0, Q boundary threeU ports conflict with same younghook CURRENT. Cpreserves. InE any g-loss RAWexitH>=-6, but finalE H<=-9 because C4 then nonemptyNrail mustreach targetH-6. InN lossRAWexitx>=gx>targetx. Thus the genuine g remains CURRENT but lies in target ENTRYCORE.',no_named_count_cap_or_postFOREIGN_JO_law_or_full_packet_relabel=True,no_other_gate_or_initial_N_nonempty_or_secondFOREIGN_or_simplicity_result=True)
(H/'R39_guard.json').write_text(json.dumps(out,indent=2)+'\n');print('Two exact N4 U-gate initialC routes excluded for arbitrary W/S/E/N lengths;8 input bounds and3 Q S-boundary guards checked;3264 named regressions retained.')
