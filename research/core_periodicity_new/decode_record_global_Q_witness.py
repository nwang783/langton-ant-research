"""Decode a global-Q spatial witness and find exact literal illegal factors."""
from pathlib import Path
import sys,json
L=json.load(open(sys.argv[1]));C=json.load(open(L['base_model_file']));E=json.load(open(C['uncompressed_model_file']));B=json.load(open(E['base_model_file']));H=json.load(open(B['height_model_file']));O=json.load(open(B['base_model_file']));G=json.load(open(Path(O['resource_profile_file']).parent/'literal_residual_geometry.json'))['geometry'];near=len(O['poses']);qb=E['height_bits'];rows=[]
for line in open(sys.argv[2]):
 if not line.startswith('WITNESS '):continue
 p,c,a=map(int,line.split()[1:]);z,dfa=B['position_map'][L['retained_old_positions'][p]]
 if z<near:state={'pose':O['poses'][z]}
 elif z==B['geometric_initial_control']:state={'initial':True}
 else:
  k,h,q,bi=B['far_controls'][z-near];state={'far_heading':h,'height':q,'transverse_band':bi}
 rows.append(dict(state=state,packet=a,Q=E['initial_height_bound']+(c&((1<<qb)-1)),colors=c>>qb))
w=[r['packet']for r in rows]
def conflict(word):
 p=0j;h=1j;seen={};par=set();raw=0
 text=''.join(G[a]['word']for a in word)+G[0]['marker']
 for t in text:
  needed=(t=='L')^(p in par)
  if p in seen and seen[p][0]!=needed:return {'raw_step':raw,'previous_read':seen[p][1],'cell':[int(p.real),int(p.imag)],'old_initial_requirement':seen[p][0],'new_initial_requirement':needed}
  if p not in seen:seen[p]=(needed,raw)
  if p in par:par.remove(p)
  else:par.add(p)
  h*=1j if t=='L'else -1j;p+=h;raw+=1
 return None
bad=[]
for k in range(1,len(w)+1):
 for i in range(len(w)-k+1):
  c=conflict(w[i:i+k])
  if c:bad.append({'start':i,'length':k,'word':w[i:i+k],'conflict':c})
 if bad:break
out={'word':w,'states':rows,'shortest_literal_conflicts':bad,'whole_word_conflict':conflict(w)};Path(sys.argv[3]).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='states'},indent=2))
