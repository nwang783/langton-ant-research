from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parent
source=ROOT.parents[1]/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
J=json.loads(source.read_text());G=next(g for g in J['geometry']if g['name']=='DC')
K={tuple(z)for z in J['core']};I={tuple(z)for z in G['inputs']};O={tuple(z)for z in G['outputs']}
F={tuple(z[:2])for z in G['requirements']};B={tuple(z[:2])for z in G['requirements']if z[2]}
assert I=={(0,1)} and B==K|I
labels={(2,0):'A',(2,3):'B',(3,1):'C',(3,2):'D'}
def rot(q,h):
 x,y=q
 for _ in range(h):x,y=y,-x
 return x,y
def transformed(S,p,h):return {(p[0]+rot(q,h)[0],p[1]+rot(q,h)[1])for q in S}
records=[]
for q in sorted(O):
 for h in range(4):
  u=rot((0,1),h);p=(q[0]-u[0],q[1]-u[1])
  sector=(-1 if sum(p)%2 else 1)*(1 if h%2==0 else-1)
  if sector!=1:continue
  k=transformed(K,p,h);f=transformed(F,p,h);b=transformed(B,p,h);ii=transformed(I,p,h)
  siblings=O-{q};core=siblings&k;white=siblings&(f-b);coinput=siblings&ii;outside=siblings-f
  assert siblings==core|white|coinput|outside
  assert not(core&white or core&outside or white&outside or coinput)
  records.append({'source_output':labels[q],'source_cell':q,'target_heading':h,'target_head':p,'core_retire':sorted(core),'white_retire':sorted(white),'coinputs':sorted(coinput),'outside_context':sorted(outside),'must_retire':sorted(core|white)})
assert len(records)==8
zeros=[x for x in records if not x['must_retire']]
assert len(zeros)==1 and zeros[0]['source_output']=='A'and zeros[0]['target_heading']==1
out={'status':'PASS exact geometric necessary conditions only','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'labels':{v:list(k)for k,v in labels.items()},'records':records,'scope':'No row is declared physically feasible; required retirement concerns ordered residual identities, not necessarily black erasure.'}
(ROOT/'dc_sibling_clearance.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
