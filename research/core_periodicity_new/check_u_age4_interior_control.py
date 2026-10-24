"""Direct literal age-four interior controls. No search or minimality claim."""
from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';J=json.loads(GP.read_text());G=J['geometry'];K=set(map(tuple,J['core']));RP=W/'chronology_dcuv/delayed_height_probe/u1_residue_cegar/root_out.json';M=json.loads(RP.read_text());A=M['core_offsets'];T={(a,h):v for a,h,v in M['created_peaks']};HP=W/'chronology_dcuv/protected_patch2.tsv';CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';HB={tuple(map(int,l.split()[:7]))for l in HP.read_text().splitlines()};COUNT={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()};keep=[0,1,4,5,6,7,8,9];ki={a:i for i,a in enumerate(keep)}
def rot(z,h):x,y=z;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def cells(Z,p,h):return{add(p,rot(z,h))for z in Z}
def solve(word):
 x=y=h=0;poses=[]
 for a in reversed(word[:-1]):
  h=(h+G[a]['name'].count('C'))%4;u,v=rot(G[a]['endpoint'][:2],h);x-=u;y-=v;poses.append((x,y,h))
 poses=list(reversed(poses))+[(0,0,0)];need={};par=set()
 for i,(a,(x,y,h))in enumerate(zip(word,poses)):
  for u,v,bit,*_ in G[a]['requirements']:
   z=add((x,y),rot((u,v),h));r=bool(bit)^(z in par)
   if z in need and need[z]!=r:return None,dict(packet_index=i,packet=a,cell=z,first_initial_bit=need[z],second_initial_bit=r)
   need[z]=r
  par^=cells(G[a]['raw_odd'],(x,y),h)
 return (poses,{z for z,v in need.items()if v}),None
controls=[]
for tail in[7,8]:
 word=[1,6,4,5,5,4,4,tail];ans,conflict=solve(word);assert ans is not None;poses,B=ans;initial=set(B);assert len(B)==18
 R={z:dict(initial=True)for z in B-cells(K,poses[0][:2],poses[0][2])};C=0;rows=[];raw_length=0;produced_queries=0
 for i,(a,(x,y,h))in enumerate(zip(word,poses)):
  p=(x,y);assert B==set(R)|cells(K,p,h);assert not set(R)&cells(K,p,h);assert(sum(p)+h)%2==0
  ins=cells(G[a]['inputs'],p,h);assert ins<=set(R);inrows=[]
  for z in sorted(ins):
   origin=R[z];age=None if origin.get('initial')else C-origin['C'];inrows.append(dict(cell=z,age=age,origin=origin))
   if age is not None:
    dh=(h-origin['heading'])%4;rel=rot(sub(p,origin['head']),-origin['heading']);key=(origin['packet'],a,*rel,dh,*origin['slot']);ck=(ki[origin['packet']],ki[a],*rel,dh,*origin['slot'],min(5,age));assert key not in HB and ck not in COUNT;(produced_queries:=produced_queries+1)
  for z in ins:del R[z]
  for slot in G[a]['outputs']:
   z=add(p,rot(slot,h));assert z not in R;R[z]=dict(packet=a,step=i,C=C,head=p,heading=h,slot=slot)
  # Execute RAW and its genuine post-RAW marker without relocating the head.
  bcopy=set(B);xx,yy,hh=x,y,h;raw_exit=None
  for k,ch in enumerate(G[a]['word']+G[a]['marker']):
   z=xx,yy;black=z in bcopy;assert ch==('L'if black else'R'),(tail,i,k,z)
   if black:bcopy.remove(z)
   else:bcopy.add(z)
   hh=(hh+(-1 if black else 1))%4;u,v=rot((0,1),hh);xx+=u;yy+=v
   if k+1==len(G[a]['word']):raw_exit=(xx,yy,hh,set(bcopy))
  xx,yy,hh,B=raw_exit;assert B==set(R)|cells(K,(xx,yy),hh);assert not set(R)&cells(K,(xx,yy),hh)
  if i+1<len(word):assert(xx,yy,hh)==poses[i+1]
  record=[2*(y-x)+A[(h+1)%4],2*(y-x)+T[a,(h+1)%4]];rows.append(dict(packet=a,head=[x,y,h],C=C,inputs=inrows,record=record,raw_exit=[xx,yy,hh]));raw_length+=len(G[a]['word']);C+=G[a]['name'].count('C')
 goal={tuple(z['cell']):z for z in rows[-1]['inputs']};assert goal[(-1,1)]['age']==goal[(-1,2)]['age']==4
 assert goal[(-1,1)]['origin']['step']==goal[(-1,2)]['origin']['step']==1
 assert all(goal[z]['origin'].get('initial')for z in[(-1,4),(0,2),(0,3)])
 assert rows[0]['record']==[30,26] and max(max(z['record'])for z in rows[1:-1])==26
 # Initial activations fund both controls, independently of the earlier DC core tie.
 activations=[48+2*(y-x)for z in rows for r in z['inputs']if r['origin'].get('initial')for x,y in[tuple(r['cell'])]]
 assert max(activations)>=58
 controls.append(dict(word=word,initial_actual_board=sorted(initial),initial_mass=18,final_mass=len(B),raw_length=raw_length,produced_HB_count_queries=produced_queries,goal_lower_ages=[4,4],source_index=1,source_packet=6,earlier_DC_record=rows[0]['record'],subsequent_strict_core_creation_max=26,goal_record=rows[-1]['record'],max_I48_initial_activation=max(activations),rows=rows))
# Same proposed prefix with UCC is not a physical literal word.
_,conflict=solve([1,6,4,5,5,4,4,9]);assert conflict is not None and conflict['packet_index']==7
O=dict(status='AUTHOR_ACTUAL_INTERIOR_AGE4_CONTROLS_PASS',scope='Two actual finite eighteen-cell complete recurrent-eight factors. Produced lower age4 has a genuinely interior source. Both are funded and NOT unfunded U1 controls. No least-mass claim, repeated renewal or capture consequence.',controls=controls,UCC_conflict=conflict,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,RP,HP,CP,Path(__file__).resolve()]})
(W/'chronology_dcuv/u_age4_interior_control.json').write_text(json.dumps(O,indent=2)+'\n');print(json.dumps([{k:v for k,v in z.items()if k not in['rows','initial_actual_board']}for z in controls],indent=2));print('UCC conflict',conflict)
