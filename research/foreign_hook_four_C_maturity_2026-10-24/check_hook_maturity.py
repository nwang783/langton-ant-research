"""Direct all-length first-four-epoch proof, not a postforeign JO age law."""
from pathlib import Path
from collections import Counter
import importlib.util,json
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('l',R/'word_stabilization/check_foreign_return_interfaces.py');l=importlib.util.module_from_spec(s);s.loader.exec_module(l);s=importlib.util.spec_from_file_location('o',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');o=importlib.util.module_from_spec(s);s.loader.exec_module(o);W=o.WORDS

def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return *q,h
# Universal first-loss input-to-RAW-exit bounds, relative a held tagg.
# This includes upper/marker-owned current-toCORE capture; it is not only
# a list of physical own-RAW L reads.
ports=[]
for atom in'DVU':
 geom=l.literal_geometry(W[atom])
 for inp in map(tuple,geom['inputs']):
  eS=after(W[atom],(*l.rot((-inp[0],-inp[1]),2),2))
  eE=after(W[atom],(*l.rot((-inp[0],-inp[1]),1),1))
  assert eS[0]<=0 and eS[1]<=0 and eE[1]<=0
  assert inp[1]>=1 and inp[0]>=-1
  ports.append(dict(atom=atom,input=inp,S_RAW_exit_relative_tag=eS,E_RAW_exit_relative_tag=eE,N_input_y_positive=inp[1]>=1,W_entry_y_at_most_tag_y_plus_one=inp[0]>=-1))
assert len(ports)==8 and l.literal_geometry(W['C'])['inputs']==[]
result=[]
Ssets={'Q':{(-3,-3),(-2,-3),(-1,-3),(-1,-2)},'B':{(-2,-4),(-1,-4),(0,-4),(0,-3)}}
for A,S in Ssets.items():
 geom=l.literal_geometry(W[A]);ep=tuple(geom['endpoint']);O={l.rot(sub(tuple(p),ep[:2]),2)for p in geom['outputs']};trA=l.trace(W[A]+l.M);assert S<=O
 rows=[]
 for atom in'DVU':
  g=l.literal_geometry(W[atom]);tr=l.trace(W[atom]+l.M)
  for h in range(4):
   for tag in sorted(S):
    for inp in map(tuple,g['inputs']):
     head=sub(tag,l.rot(inp,h));r=dict(tag=tag,atom=atom,input=inp,heading=h,head=head,actual_postforeign_C_clock=(-h)%4)
     if(sum(head)+h)%2:r['reason']='sector'
     else:
      core=[q for q in sorted(S)if l.rot(sub(q,head),-h)in l.K]
      white=[q for q in sorted(S)if(v:=l.rot(sub(q,head),-h))in tr['first']and tr['first'][v][0]=='R']
      if core:r.update(reason='held_hook_CURRENT_entry_CORE',witnesses=core)
      elif white:r.update(reason='held_hook_BLACK_first_WHITE',witnesses=white)
      elif h==0:
       assert head[1]<0;r['reason']='clock0_N_head_y_negative'
      elif h==3:
       assert head[1]<1;r['reason']='clock1_W_head_below_y1'
      else:
       witness=add(head,(-1,-3)if h==2 else(1,-1))
       assert witness in O and witness not in l.K
       orig=add(ep[:2],l.rot(witness,2));last=trA['last'][orig];assert last[0]=='R'
       loc=l.rot(sub(witness,head),-h);fr=tr['first'][loc];assert fr[0]=='R'and fr[1]<len(W[atom])
       if h==2:
        assert witness[1]<=-1 and witness[0]<head[0];assert loc==(1,3)and fr[1]==26
        why='clock2_S_left_lower_FOREIGN_output_endpoint_reserve'
       else:
        assert witness[1]<=-1 and witness[1]<head[1];assert loc==(1,1)and fr[1]==6
        why='clock3_E_lower_FOREIGN_output_endpoint_reserve'
       r.update(reason=why,actual_FOREIGN_same_id_reserve=dict(postforeign_cell=witness,A_cell=orig,last_R_tick0=last[1],last_R_read1=last[1]+1),actual_first_incompatible_R=o.describe(atom,fr[1]))
     rows.append(r)
 assert len(rows)==128
 result.append(dict(foreign=A,hook_tags=sorted(S),all128_direct_first_loss_input_alignments=rows,counts=dict(Counter(r['reason']for r in rows))))
probes=json.load(open(H/'named_two_C_controls.json'))
assert len(probes['counts'])==64 and len(probes['wordcases'])==286 and not probes['positive']
for r in probes['wordcases']:assert not r['trace']['feasible']
out=dict(status='AUTHOR_ALL_LENGTH_HOOK_FIRST_LOSS_MINIMUM4_PENDING_REVIEW',scope='Actual Q/B followed by any actual ordinary RAW suffix plus actual terminalM11. First CURRENT loss of any of four SAME hook IDs requires ordinary-base entry C clock at least4 after FOREIGN EXIT. No earlier proxy simplicity, source-age law, U ancestry or secondforeign extension.',universal8_input_to_RAW_exit_coordinate_bounds=ports,actual_C_external_input_empty=True,generic_coordinate_reserve_lemma='Starting at marked0N: an initial CURRENT tagg withgy<=-1 remains CURRENT at any S-facing entry of exact Cclock2 withheadx>gx; it remains CURRENT at any E-facing entry of exactCclock3 withheady>gy. N/W cannotconsume it; S/E RAW exit bounds and remaining Cdrifts forbid reaching that target after a first loss. These are endpoint-specific reserves, not physical WHITE permanence.',source_cases=result,all64_named_zero_or_one_N_base_two_C_count_records=probes['counts'],all286_complete_named_two_C_immutable_control_words=probes['wordcases'],no_count_cap_used_in_maturity_proof=True,no_existing_postFOREIGN_age_or_protected_ghost_source_assumed=True,no_simplicity_or_secondFOREIGN_or_capture=True)
(H/'hook_maturity.json').write_text(json.dumps(out,indent=2)+'\n');print([(r['foreign'],r['counts'])for r in result]);print('All-length hook first CURRENT-loss entry clock>=4; all256 trueinput roles and8 universal endpoint bounds checked.')
