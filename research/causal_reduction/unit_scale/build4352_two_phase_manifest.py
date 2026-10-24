"""Frozen direct affine chronology contract for the394-cell two-wave family.
The sole parameter below is M>=1; original producer N=3M+4.
"""
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent
J=json.loads((P/'prepared4352_uniform_support_manifest.json').read_text());A=json.loads((P/'prepared4352_finite_return_supply.json').read_text())
def sub(a):return[3*a[0],4*a[0]+a[1]]
seeds=[[sub(x),sub(y)]for x,y in J['seed_families']];stages=[]
for s in J['stages']:
 t=dict(s)
 for k in('count_N_constant','start_x_N_constant','start_y_N_constant','start_time_N_constant'):t[k]=sub(s[k])
 stages.append(t)
stages.append({'kind':'source-transition','word':A['transition_after_N_waves'],'count_N_constant':[0,1],'start_x_N_constant':[78,102],'start_y_N_constant':[78,107],'heading':3,'start_time_N_constant':[114456,297010]})
stages.append({'kind':'return-wave','word':A['return_word'],'count_N_constant':[1,0],'start_x_N_constant':[78,117],'start_y_N_constant':[78,111],'heading':0,'start_time_N_constant':[114456,455161]})
out={'scope':__doc__,'domain':'M>=1; all keys named N_constant mean coefficient-of-M,constant in this manifest','seed_mass':394,'seed_families':seeds,'initial_pose':{'x_N_constant':[78,217],'y_N_constant':[78,192],'heading':3},'stages':stages,'end_time_M_constant':[129780,455161],'end_pose':[[117,111],0],'end_mass_M_constant':[12660,37419],'actual_K_M_constant':[13269,86411],'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'prepared4352_two_phase_manifest.json').write_text(json.dumps(out,indent=2)+'\n');print(hashlib.sha256((P/'prepared4352_two_phase_manifest.json').read_bytes()).hexdigest())
