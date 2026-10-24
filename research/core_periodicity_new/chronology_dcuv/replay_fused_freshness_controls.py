"""Replay explicit physical boards through fused color/origin graphs."""
from pathlib import Path
import json,subprocess,sys
R=Path(__file__).resolve().parent;P=R.parent;G=json.loads((R/'literal_residual_geometry.json').read_text())['geometry'];J=json.loads(Path(sys.argv[1]).read_text());controls=J['witnesses'];directory=R/('fused_controls_depth'+str(J.get('packet_depth',0)));directory.mkdir(exist_ok=True);records=[];D=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def walk(w,p,h,B):
 seen=set()
 for c in w:
  assert(c=='L')==(p in B);seen.add(p);B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return p,h,seen
def call(cmd):return subprocess.run(list(map(str,cmd)),cwd=P,capture_output=True,text=True,check=True).stdout
for ci,c in enumerate(controls,1):
 a,b,x,y,h,qx,qy=c['tuple'];base=directory/f'control{ci:03d}_base';fused=directory/f'control{ci:03d}_fused';call(['python','generate_resource_transfer_patch.py',R/'profile.json',a,b,x,y,h,qx,qy,base,'source']);B0=json.loads(base.with_suffix('.json').read_text());points=list(map(tuple,B0['points']));watch=sorted(points,key=lambda z:(abs(z[0]-qx)+abs(z[1]-qy),z))[:min(12,50-len(points))];call(['python','add_resource_upper_freshness_fused.py',base.with_suffix('.json'),fused,R/'hypothesis_U_upper3.tsv',';'.join(f'{xx},{yy}'for xx,yy in watch)]);model=json.loads(fused.with_suffix('.json').read_text());positions={tuple(z):i for i,z in enumerate(model['poses'])};B={tuple(z)for z in c['initial_black_seed']};p=(0,0);hh=0
 for aa in c['packet_ids'][:c['source_index']]:p,hh,_=walk(G[aa]['word'],p,hh,B)
 pp,heading=p,hh;B={rot((z[0]-pp[0],z[1]-pp[1]),-heading)for z in B};p=(0,0);hh=0;factor=c['packet_ids'][c['source_index']:c['target_index']+1];p,hh,_=walk(G[a]['word'],p,hh,B);origin={tuple(z):2 for z in G[a]['outputs']if tuple(z)in watch}
 def state():
  s=0
  for cell in model['origin_cells']:
   q=tuple(cell['cell']);black=q in B;code=origin.get(q,1 if black else 0)if cell['watched']else int(black)
   assert not(cell['watched']and code in(2,3))or black
   s|=code<<cell['offset']
  return s
 assert state()&model['start'][1]==model['start'][2]
 near=far=0
 for j,aa in enumerate(factor[1:]):
  goal=j==len(factor)-2;sid=positions.get((*p,hh),model['out']);before=state();edges=[]
  if sid!=model['out']:
   edges=[e for e in model['transitions']if e[0]==sid and e[-1]==aa and bool(e[-2])==goal and before&e[2]==e[3]];assert edges,(ci,j,'missing transition')
  else:assert not goal
  pp,heading=p,hh;_,_,context=walk(G[aa]['word']+G[aa]['marker'],p,hh,set(B));p,hh,_=walk(G[aa]['word'],p,hh,B)
  for q in list(origin):
   if q in context:origin.pop(q)
  for z in G[aa]['outputs']:
   zz=rot(z,heading);q=(pp[0]+zz[0],pp[1]+zz[1])
   if q in watch:origin[q]=3
  after=state();nextpos=positions.get((*p,hh),model['out'])
  if sid==model['out']:
   assert after==before
   if nextpos!=model['out']:assert nextpos in model['reentry']
  else:assert any(after==(((before^e[4])&~e[5])|(e[6]&e[5]))and nextpos==e[1]for e in edges),(ci,j,'wrong output')
  near+=sid!=model['out'];far+=sid==model['out']
 records.append({'control':ci,'tuple':c['tuple'],'variables':model['n'],'watch':watch,'near_steps':near,'far_steps':far,'status':'PRESERVED'});print(ci,c['tuple'],'PASS',flush=True)
(directory.with_suffix('.json')).write_text(json.dumps({'status':'ALL_PHYSICAL_CONTROLS_PRESERVED','records':records},indent=2))
