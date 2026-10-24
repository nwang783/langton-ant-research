"""Literal replay of finite controls; no search absence is used as a theorem."""
from pathlib import Path
import json,re
P=Path(__file__).resolve().parent;words={'D':'LLLLRLRRRR','C':'LLLLRLRRRRLRRRR','V':'LLLLRLRRRRLRRLRRRR'};marker='LLLLRLRRRRL';dirs=[(0,1),(1,0),(0,-1),(-1,0)];R=json.loads((P/'dcv_residual_core_resources.json').read_text())['geometry'];obs={tuple(map(int,l.split()))for l in(P/'dcv_companion_observed19.tsv').read_text().splitlines()}
def rot(p,h):
 x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def trace(word):
 p=(0,0);h=0;first={};last={};reads=[];poses=[(p,h)]
 for c in word:
  bit=int(c=='L');assert last.get(p)!=bit;first.setdefault(p,bit);last[p]=bit;reads.append(p);h=(h+(1 if c=='R'else-1))%4;d=dirs[h];p=(p[0]+d[0],p[1]+d[1]);poses.append((p,h))
 return first,reads,poses
out=[]
for line in(P/'dcv_packet_witnesses_fuel20.log').read_text().splitlines():
 if not line.startswith('WITNESS '):continue
 z=line.split();a,qx,qy,b,ix,iy,hr=map(int,z[1:8]);path=z[8];u,v,last=map(int,z[9:]);raw=''.join(words[c]for c in path);first,reads,poses=trace(raw+marker);turns=[0]
 for c in path:turns.append(turns[-1]+len(words[c]))
 pa,ha=poses[turns[u]];pb,hb=poses[turns[v]];relative=rot((pb[0]-pa[0],pb[1]-pa[1]),-ha);row=(a,b,*relative,hr,qx,qy)
 if row not in obs:continue
 assert (hb-ha)%4==hr;qp=rot((qx,qy),ha);q=(pa[0]+qp[0],pa[1]+qp[1]);qi=rot((ix,iy),hb);assert q==(pb[0]+qi[0],pb[1]+qi[1]);assert [qx,qy]in R[a]['outputs'] and[ix,iy]in R[b]['inputs']
 packets=[]
 for match in re.finditer('[DV]C*',path):
  s,e=match.span();name=match.group();typ=(0 if name[0]=='D' else 4)+len(name)-1;packets.append({'type':typ,'name':name,'macro_start':s,'macro_end':e,'turn_start':turns[s],'turn_end':turns[e]})
 si=next(i for i,p in enumerate(packets)if p['macro_start']==u);ti=next(i for i,p in enumerate(packets)if p['macro_start']==v);assert packets[si]['type']==a and packets[ti]['type']==b;assert packets[ti]['macro_end']==last+1;assert ti<len(packets)-1
 assert all(p['type']in[0,1,4,5,6]for p in packets[si:ti+1])
 for p in packets[si+1:ti]:assert q not in reads[p['turn_start']:p['turn_end']+len(marker)]
 black={p for p,b in first.items()if b};source_black=None;after_source=None
 for t,c in enumerate(raw+marker):
  p,h=poses[t]
  if t==turns[u]:source_black=sorted(rot((x-pa[0],y-pa[1]),-ha)for x,y in black)
  assert(p in black)==(c=='L')
  if p in black:black.remove(p)
  else:black.add(p)
  if t+1==packets[si]['turn_end']:after_source=q in black
 assert after_source
 out.append({'tuple':row,'whole_macro_word':path,'source_macro_index':u,'target_macro_index':v,'target_macro_last':last,'source_packet_index':si,'target_packet_index':ti,'factor_packet_types':[p['type']for p in packets[si:]],'factor_macro_word':path[u:],'initial_seed_normalized_at_source':source_black,'initial_mass_at_source':len(source_black),'target_pose':[*relative,hr],'protected_contexts_verified':ti-si-1,'literal_turns_checked':len(raw+marker)})
covered={tuple(r['tuple'])for r in out};result={'status':'LITERAL_FINITE_CONTROLS','covered':len(covered),'expected':len(obs),'missing':[r for r in sorted(obs-covered)],'controls':out};(P/'dcv_observed19_witnesses.json').write_text(json.dumps(result,indent=2));print({k:v for k,v in result.items()if k!='controls'});assert covered==obs
