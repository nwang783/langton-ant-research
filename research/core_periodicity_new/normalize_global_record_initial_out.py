"""Finite-I normalization to an all-white retained residual patch, initial OUT only.
CLI RESIDUAL_GLOBAL.json PREFIX. I is raised enough that every residual input
of every near packet, and every retained cell, is high. Any first near packet
would consume initial high fuel. Thus a genuinely unfunded prefix starts OUT.
Ordinary packet and OUT/reentry transitions remain byte-for-byte unchanged.
"""
from pathlib import Path
import sys,json,hashlib
from resource_profile import load_profile
source,out=map(Path,sys.argv[1:3]);J=json.loads(source.read_text());assert J['format']=='guarded_reset_global_record_residual_v1';P,D,M=load_profile(Path(J['resource_profile_file']));G=D['geometry']['geometry'];v=json.loads(Path(J['potential_file']).read_text())['values'];phase=J['target_global_phase'];S=J['record_threshold'];init=J['initial_control_pose'];points=set(map(tuple,J['points']));allq=set(points)
def rot(q,h):x,y=q;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def twice(q):z=rot(q,phase);return 2*(v['ax']*z[0]+v['ay']*z[1])
for x,y,h in J['poses']:
 for a in J['keep']:
  assert G[a]['inputs']
  for q in G[a]['inputs']:
   z=rot(q,h);allq.add((x+z[0],y+z[1]))
minimum=min(map(twice,allq));I=max(J['initial_token_weight'],S-minimum);T=[t for t in J['transitions']if t[0]!=init];start=[J['out'],(1<<J['n'])-1,0]
N={**J,'format':'guarded_reset_global_record_initial_out_v1','base_model_file':str(source.resolve()),'base_model_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'initial_token_weight':I,'initial_out_normalization':{'old_weight':J['initial_token_weight'],'new_weight':I,'minimum_twice_linear_value':minimum,'all_near_input_and_patch_cells':sorted(allq),'justification':'Every recurrent packet has an input; every first near input is initial and has activation >=S. All near entries impossible in an unfunded prefix. Initial OUT has no retained core; high initial residuals whitened.'},'start':start,'transitions':T,'initial_transition_indices':[],'packet_transition_indices':list(range(len(T))),'high_initial_white_cells':sorted(points),'scope':J['scope']+' Raised finite I removes all first-near entries; normalized initial state is OUT with every retained residual white. No restriction on later hidden OUT behavior.'};out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{N['n']} {N['out']+1} {len(T)} {len(N['reentry'])}\n");f.write(' '.join(map(str,start))+'\n')
 for t in T:f.write(' '.join(map(str,t))+'\n')
 f.write(' '.join(map(str,N['reentry']))+'\n')
print(json.dumps({'variables':N['n'],'I':I,'start':'OUT allwhite','transitions':len(T)}))
