"""Supplied affine continuation candidate after the signed two-phase family.
This builds a contract, not a proof; complete literal and all-parameter checks
are kept separately. M>=1 remains the only parameter.
"""
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent;J=json.loads((P/'prepared4352_two_phase_manifest.json').read_text());A=json.loads((P/'prepared4352_return_endpoint_capture.json').read_text());L=json.loads((P/'prepared4352_return_end_limit.json').read_text())
stages=list(J['stages']);fixed=L['word'];assert len(fixed)==38503;tail=A['events'][1]['word'];response=A['continuation_word'][48430:];assert len(response)==1777
# Trace all starts rather than transcribing intermediate offsets.
from check_prepared1564_router_geometry import trace
p=(-5,-66);h=3;rr=list(trace(tail[:32],p,h));d=(rr[-1][1][0]-p[0],rr[-1][1][1]-p[1]);hh=rr[-1][2]
stages.append({'kind':'launch-end-response','word':fixed,'count_N_constant':[0,1],'start_x_N_constant':[0,117],'start_y_N_constant':[0,111],'heading':0,'start_time_N_constant':[129780,455161]})
stages.append({'kind':'SW-standard','word':tail,'count_N_constant':[78,184],'start_x_N_constant':[0,-5],'start_y_N_constant':[0,-66],'heading':3,'start_time_N_constant':[129780,493664]})
stages.append({'kind':'SW-partial','word':tail[:32],'count_N_constant':[0,1],'start_x_N_constant':[-156,-373],'start_y_N_constant':[-156,-434],'heading':3,'start_time_N_constant':[137892,512800]})
stages.append({'kind':'router-contact-response','word':response,'count_N_constant':[0,1],'start_x_N_constant':[-156,-373+d[0]],'start_y_N_constant':[-156,-434+d[1]],'heading':hh,'start_time_N_constant':[137892,512832]})
out={k:v for k,v in J.items()if k not in('scope','stages','source_sha256')};out.update({'scope':__doc__,'stages':stages,'end_time_M_constant':[137892,514609],'end_pose_x_M_constant':[-156,-399],'end_pose_y_M_constant':[-156,-429],'end_heading':0,'end_mass_M_constant':[13596,41167],'actual_K_M_constant':[13269,104594],'tail_word':A['capture_word'],'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()});out.pop('end_pose',None)
(P/'prepared4352_capture_manifest.json').write_text(json.dumps(out,indent=2)+'\n');print(hashlib.sha256((P/'prepared4352_capture_manifest.json').read_bytes()).hexdigest())
