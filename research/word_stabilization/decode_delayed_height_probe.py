from pathlib import Path
import sys,json
src,txt,out=map(Path,sys.argv[1:4]);J=json.loads(src.read_text());B=json.loads(Path(J['base_spatial_file']).read_text());O=json.loads(Path(B['base_model_file']).read_text());G=json.loads((Path(O['resource_profile_file']).parent/'literal_residual_geometry.json').read_text())['geometry'];near=len(O['poses']);raw=txt.read_text().splitlines();assert raw[0].startswith('status WITNESS');word=list(map(int,raw[1].split()[1:]));rs=[list(map(int,l.split()))for l in raw[2:]if not l.startswith('goal_edge')];ge=int(raw[-1].split()[1]);steps=[]
for i,r in enumerate(rs):
 p,col,ine,*Q=r;ei=rs[i+1][2]if i+1<len(rs)else ge;e=J['transition_details'][ei];assert e[0]==p and e[8]==word[i];z,dfa=B['position_map'][p]
 if z<near:state={'pose':O['poses'][z]}
 elif z==B['geometric_initial_control']:state={'initial':True}
 else:
  k,h,q,band=B['far_controls'][z-near];state={'far_heading':h,'height':q,'transverse_band':band}
 steps.append({'position':p,'colors':col,'incoming_edge':ine,'edge':ei,'packet':e[8],'Q':Q,'state':state})
def rot(z,h):x,y=z;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
known={};where={};conf=[]
for i,s in enumerate(steps):
 if 'pose'not in s['state']:known={};where={};continue
 x,y,h=s['state']['pose'];a=s['packet']
 def at(z):u,v=rot(z,h);return x+u,y+v
 for r in G[a]['requirements']:
  q=at(r[:2]);b=r[2]
  if q in known and known[q]!=b:conf.append({'packet_index':i,'earlier_packet':where[q],'cell':q,'expected':b,'known':known[q],'retained':list(q)in O['points']})
  known[q]=b;where[q]=i
 for q in map(at,G[a]['raw_odd']):known[q]^=1

def literal(w):
 p=0j;h=1j;seen={};par=set()
 for ti,t in enumerate(''.join(G[a]['word']for a in w)+G[0]['marker']):
  b=(t=='L')^(p in par)
  if p in seen and seen[p][0]!=b:return {'raw_step':ti,'previous_read':seen[p][1],'cell':[int(p.real),int(p.imag)]}
  if p not in seen:seen[p]=(b,ti)
  par.symmetric_difference_update([p]);h*=1j if t=='L'else -1j;p+=h
bad=[]
for k in range(1,len(word)+1):
 for i in range(len(word)-k+1):
  c=literal(word[i:i+k])
  if c:bad.append({'start':i,'word':word[i:i+k],'length':k,'conflict':c})
 if bad:break
N={'model':str(src),'word':word,'states':steps,'near_block_conflicts':conf,'shortest_literal_conflicts':bad,'points':O['points']};out.write_text(json.dumps(N,indent=2)+'\n');print(json.dumps({k:N[k]for k in ['word','near_block_conflicts','shortest_literal_conflicts']},indent=2))
