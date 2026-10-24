from pathlib import Path
import json,itertools,sys,time,hashlib
import numpy as np
R=Path(__file__).resolve().parents[1];D=R/'core_periodicity_new/chronology_dcuv';G=json.loads((D/'literal_residual_geometry.json').read_text())['geometry'];profile=D/'profile_recurrent8.json';K=json.loads(profile.read_text())['keep'];rows=json.loads((D/'transfer_inventory.json').read_text())['protected_survivors'];base=json.loads((D/'potential_extend_dcv_policy01_saturated.json').read_text());out=D/'record_head_offset_search';out.mkdir(exist_ok=True)
def rot(z,h):x,y=z;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
results=[]
for direction in [(0,1),(1,1),(1,2),(1,3),(1,4),(2,3)]:
 def L(z):return direction[0]*z[0]+direction[1]*z[1]
 data=[]
 for e in rows:
  aa,bb,x,y,rh,*q=e['tuple']
  if aa not in K or bb not in K:continue
  for phase in range(4):
   bh=(phase+rh)%4;ae=G[aa]['endpoint'];be=G[bb]['endpoint'];sd=2*L(rot(ae[:2],phase));td=2*L(rot(be[:2],bh));th=2*L(rot((x,y),phase))+td;data.append((phase,(phase+ae[2])%4,bh,(bh+be[2])%4,sd,td,th))
 ar=np.asarray(data,dtype=np.int16).T;s,so,b,bo,sd,td,th=ar;best=None;bestA=None;tried=0;t0=time.time()
 def count(A):
  a=np.asarray(A,dtype=np.int16);return int(np.count_nonzero((td+a[bo]>a[b])&(th+a[bo]>a[s])&(th+a[bo]>sd+a[so])))
 zero=count([0,0,0,0])
 for xyz in itertools.product(range(-64,65,4),repeat=3):
  A=[0,*xyz];n=count(A);tried+=1
  if best is None or n<best:best=n;bestA=A
 coarse=bestA[:]
 for xyz in itertools.product(*(range(z-4,z+5)for z in coarse[1:])):
  A=[0,*xyz];n=count(A);tried+=1
  if n<best:best=n;bestA=A
 J=json.loads(json.dumps(base));v=J['values'];v['ax'],v['ay']=direction
 for h in range(4):v[f'c{h}']=bestA[h]-L(rot((-1,1),h))
 for aa in K:
  g=G[aa];end=g['endpoint']
  for h in range(4):
   T=2*L(rot(end[:2],h))+bestA[(h+end[2])%4]
   for i,q in enumerate(g['outputs']):v[f'w_{aa}_{i}_{h}']=T-2*L(rot(q,h))
   for i,q in enumerate(g['inputs']):v[f'u_{aa}_{i}_{h}']=T-2*L(rot(q,h))
 J['status']='RECORD-ONLY numerical candidate; no individual transfer obligations are asserted';J['record_head_offsets']={'direction':direction,'A':bestA,'events':best,'zero_offset_events':zero,'tried':tried,'seconds':time.time()-t0,'rule':'Every created peak equals new core value; saturated outputs; inputs only syntactic placeholders','not_claimed':'No optimality outside the finite grid and no physical event exclusion.'};fp=out/f'head_{direction[0]}_{direction[1]}.json';fp.write_text(json.dumps(J,indent=2)+'\n');results.append({'file':str(fp),**J['record_head_offsets']});(out/'summary.json').write_text(json.dumps(results,indent=2)+'\n');print(results[-1],flush=True)
