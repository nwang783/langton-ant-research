"""Find and replay literal multi-token protected transfers among explicit factors."""
from pathlib import Path
import json,subprocess
R=Path(__file__).resolve().parent;P=R.parent;G=json.loads((R/'literal_residual_geometry.json').read_text())['geometry'];obs=json.loads((R/'observed_transfers_fast_depth11.json').read_text())['witnesses'];out=R/'compound_protected_controls';out.mkdir(exist_ok=True);records=[];seen=set();D=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def walk(w,p,h,B):
 C=set()
 for c in w:assert(c=='L')==(p in B);C.add(p);B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return p,h,C
def call(cmd):subprocess.run(list(map(str,cmd)),cwd=P,capture_output=True,text=True,check=True)
for oi,c in enumerate(obs,1):
 a,b,x,y,h,*_=c['tuple'];B=set(map(tuple,c['initial_black_seed']));p=(0,0);hh=0
 for aa in c['packet_ids'][:c['source_index']]:p,hh,_=walk(G[aa]['word'],p,hh,B)
 B={rot((z[0]-p[0],z[1]-p[1]),-hh)for z in B};p=(0,0);hh=0;factor=c['packet_ids'][c['source_index']:c['target_index']+1];p,hh,_=walk(G[a]['word'],p,hh,B);startB=set(B);startp=p;starth=hh;alive=set(map(tuple,G[a]['outputs']));contexts=[];poses=[]
 for j,aa in enumerate(factor[1:]):
  poses.append((p,hh));_,_,C=walk(G[aa]['word']+G[aa]['marker'],p,hh,set(B));contexts.append(C)
  if j<len(factor)-2:alive-=C
  p,hh,_=walk(G[aa]['word'],p,hh,B)
 targetcells={(x+rot(z,h)[0],y+rot(z,h)[1])for z in G[b]['inputs']};Q=sorted(alive&targetcells)
 if len(Q)<2:continue
 key=(a,b,x,y,h,tuple(Q))
 if key in seen:continue
 seen.add(key);ci=len(records)+1;base=out/f'control{ci:02d}_base';multi=out/f'control{ci:02d}_multi';call(['python','generate_resource_transfer_patch.py',R/'profile.json',a,b,x,y,h,*Q[0],base,'source']);call(['python','add_resource_protected_cells.py',base.with_suffix('.json'),multi,';'.join(f'{qx},{qy}'for qx,qy in Q[1:])]);J=json.loads(multi.with_suffix('.json').read_text());ix={tuple(z):i for i,z in enumerate(J['poses'])};B=set(startB);p=startp;hh=starth
 def state():return sum(1<<i for i,z in enumerate(J['points'])if tuple(z)in B)
 assert state()&J['start'][1]==J['start'][2]
 for j,aa in enumerate(factor[1:]):
  goal=j==len(factor)-2;sid=ix.get((*p,hh),J['out']);s=state();edges=[e for e in J['transitions']if e[0]==sid and e[-1]==aa and bool(e[-2])==goal and s&e[2]==e[3]]if sid!=J['out']else None
  if edges is not None:assert edges,(ci,j)
  else:assert not goal
  p,hh,_=walk(G[aa]['word'],p,hh,B);dest=ix.get((*p,hh),J['out']);ss=state()
  if edges is None:assert ss==s and(dest==J['out']or dest in J['reentry'])
  else:assert any(ss==s^e[4]and dest==e[1]for e in edges)
 records.append({'control':ci,'observed_record':oi,'source':a,'target':b,'target_pose':[x,y,h],'protected_cells':Q,'status':'PRESERVED'});print(ci,key,'PASS',flush=True)
(out.with_suffix('.json')).write_text(json.dumps({'status':'ALL_COMPOUND_PHYSICAL_CONTROLS_PRESERVED','records':records},indent=2))
