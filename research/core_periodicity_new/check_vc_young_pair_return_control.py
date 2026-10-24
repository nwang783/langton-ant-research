"""One direct fifteen-cell VC-young-pair control, not an all-r family claim."""
from pathlib import Path
import hashlib,json
W=Path(__file__).resolve().parent
GP=W/'chronology_dcuv/literal_residual_geometry.json'
RP=W/'chronology_dcuv/delayed_height_probe/u1_residue_cegar/root_out.json'
J=json.loads(GP.read_text());G=J['geometry'];K=set(map(tuple,J['core']))
R=json.loads(RP.read_text());A=R['core_offsets'];T={(a,h):v for a,h,v in R['created_peaks']}
seed={(-5,-1),(-5,0),(-4,-2),(-4,0),(-3,-2),(-3,1),(-2,-1),
      (-1,-1),(-1,0),(-1,1),(-1,4),(0,-1),(0,0),(0,2),(0,3)}
def rot(p,h):
 x,y=p
 return ((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def cells_at(P,p,h):
 return {(p[0]+rot(z,h)[0],p[1]+rot(z,h)[1])for z in P}
controls=[]
for goal in (7,8,9):
 word=[5,1,0,1,0,0,0,goal]
 B=set(seed);p=(-1,0);h=3;current={z:dict(entry=True)for z in B-cells_at(K,p,h)}
 C=0;time=0;rows=[];protected=set(map(tuple,G[7]['inputs']))
 for step,b in enumerate(word):
  k=cells_at(K,p,h);assert k<=B and not k&set(current) and B==k|set(current)
  ins=cells_at(G[b]['inputs'],p,h);outs=cells_at(G[b]['outputs'],p,h)
  ctx=cells_at([z[:2]for z in G[b]['requirements']],p,h)
  for x,y,black,*_ in G[b]['requirements']:
   dx,dy=rot((x,y),h);assert ((p[0]+dx,p[1]+dy)in B)==bool(black)
  assert ins<=set(current)
  if 0<step<7:assert not ctx&protected
  row=dict(step=step,packet=b,pose=[*p,h],C_before=C,raw_time=time,
           consumed=[dict(cell=z,origin=current[z],age=None if current[z].get('entry')else C-current[z]['C'])for z in sorted(ins)],
           entry_core=2*(p[1]-p[0])+A[(h+1)%4],created_peak=2*(p[1]-p[0])+T[b,(h+1)%4])
  if step==7:
   by={tuple(r['cell']):r for r in row['consumed']}
   for z in [(-1,1),(-1,2)]:assert by[z]['origin']['step']==0 and by[z]['age']==3
   for z in [(-1,4),(0,2),(0,3)]:assert by[z]['origin']['entry']
   assert p==(0,0)and h==0
  for z in ins:del current[z]
  for z in outs:
   assert z not in current
   current[z]=dict(step=step,packet=b,C=C)
  start=p;start_h=h
  for ch in G[b]['word']:
   black=p in B;assert ch==('L'if black else'R')
   if black:B.remove(p)
   else:B.add(p)
   h=(h+(-1 if black else 1))%4;dx,dy=rot((0,1),h);p=(p[0]+dx,p[1]+dy);time+=1
  dx,dy,dh=G[b]['endpoint'];assert p==(start[0]+rot((dx,dy),start_h)[0],start[1]+rot((dx,dy),start_h)[1])and h==(start_h+dh)%4
  assert B==cells_at(K,p,h)|set(current) and not cells_at(K,p,h)&set(current)
  row['exit']=[*p,h];rows.append(row);C+=G[b]['name'].count('C')
 rawlen=time
 for ch in G[0]['marker']:
  black=p in B;assert ch==('L'if black else'R')
  if black:B.remove(p)
  else:B.add(p)
  h=(h+(-1 if black else 1))%4;dx,dy=rot((0,1),h);p=(p[0]+dx,p[1]+dy)
 assert rows[1]['pose']==[-5,1,2]and rows[1]['created_peak']==30
 controls.append(dict(word=word,initial_black_cells=sorted(seed),initial_pose=[-1,0,3],raw_length=rawlen,
                      checked_reads=rawlen+len(G[0]['marker']),rows=rows))
O=dict(status='AUTHOR_DIRECT_VC_AGE3_PAIR_FIFTEEN_CELL_CONTROLS_PASS',
       scope='Three actual context-complete finite words; lower pair source VC age3, old upper3. Earlier DC already reaches U1 core/creation value30. Not an unfunded record, renewal, minimum-mass or all-r result.',
       controls=controls,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()
                                    for p in [GP,RP,Path(__file__).resolve()]})
P=W/'chronology_dcuv/vc_young_pair_return_control.json';P.write_text(json.dumps(O,indent=2)+'\n')
print({'seed_mass':15,'tails':[r['word'][-1]for r in controls],'raw_lengths':[r['raw_length']for r in controls],'first_strict_DC_score':30})
