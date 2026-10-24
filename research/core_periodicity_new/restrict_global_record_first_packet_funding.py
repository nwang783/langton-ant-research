"""Exactly contract initial-core installation with a globally funded first packet.
CLI RESIDUAL_GLOBAL.json PREFIX. Initial OUT is retained without any new cut.
Every first packet input is an INITIAL residual identity, including untracked cells.
No first goal can have all inputs produced. Ordinary later packet edges are untouched.
"""
from pathlib import Path
import json,sys,hashlib
from resource_profile import load_profile
source,out=map(Path,sys.argv[1:3]);J=json.loads(source.read_text());assert J['format']=='guarded_reset_global_record_residual_v1';P,D,M=load_profile(Path(J['resource_profile_file']));G=D['geometry']['geometry'];v=json.loads(Path(J['potential_file']).read_text())['values'];ph=J['target_global_phase'];I=J['initial_token_weight'];S=J['record_threshold'];init=J['initial_control_pose'];OUT=J['out'];mask=(1<<J['n'])-1

def rot(q,h):x,y=q;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def val(q):z=rot(q,ph);return I+2*(v['ax']*z[0]+v['ay']*z[1])
T=[];packet=[];newinitial=[];records=[];rejected=[];by={}
for i,t in enumerate(J['transitions']):
 if t[0]!=init:by.setdefault(t[0],[]).append((i,t));packet.append(len(T));T.append(t)
for ii in J['initial_transition_indices']:
 z=J['transitions'][ii];fr,p,k0,v0,f0,c0,r0,g0,a0=z;assert(fr,k0,v0,f0,r0,g0,a0)==(init,0,0,0,0,0,-1)
 if p==OUT:newinitial.append(len(T));T.append(z);records.append({'edge':len(T)-1,'initial_out':True,'source_initial_edge':ii});continue
 pose=J['poses'][p];x,y,h=pose
 for ti,t in by.get(p,[]):
  _,to,k,vv,f,c,r,goal,a=t;high=[]
  for q in G[a]['inputs']:
   zq=rot(q,h);qg=(x+zq[0],y+zq[1]);av=val(qg)
   if av>=S:high.append([*qg,av])
  if high or goal:rejected.append({'initial_edge':ii,'packet_edge':ti,'high_initial_inputs':high,'goal':bool(goal)});continue
  # First map clears initial core residual bits c0. Pull guard back through it.
  if vv&k&c0:rejected.append({'initial_edge':ii,'packet_edge':ti,'guard_core_conflict':True});continue
  kk=k&~c0;nv=vv&kk;nc=c|c0;nr=(r&c)|(f&c0&~c);nf=f&~nc
  nt=[init,to,kk,nv,nf,nc,nr,0,a];newinitial.append(len(T));T.append(nt);records.append({'edge':len(T)-1,'source_initial_edge':ii,'source_packet_edge':ti,'first_pose':pose,'first_packet':a,'initial_core_clear':c0})
N={**J,'format':'guarded_reset_global_record_first_funding_v1','base_model_file':str(source.resolve()),'base_model_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'transitions':T,'packet_transition_indices':packet,'initial_transition_indices':newinitial,'first_packet_compositions':records,'first_packet_rejections':rejected,'scope':J['scope']+' Initial near packets additionally impose all full physical initial-input activation cuts, including outside patch; core clear and first packet exactly contracted. Initial OUT remains unchanged.'};out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{N['n']} {OUT+1} {len(T)} {len(N['reentry'])}\n");f.write(' '.join(map(str,N['start']))+'\n')
 for t in T:f.write(' '.join(map(str,t))+'\n')
 f.write(' '.join(map(str,N['reentry']))+'\n')
print(json.dumps({'variables':N['n'],'initial_compositions':len(records),'initial_rejections':len(rejected),'transitions':len(T)}))
