from pathlib import Path
import json
R=Path(__file__).resolve().parent;G=json.loads((R/'chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];ids=(0,1,4,5,6,7,8,9)
p=R/'chronology_dcuv/dc_spare_literal_probe.input'
with p.open('w')as f:
 f.write(f'{len(ids)}\n')
 for a in ids:
  g=G[a];f.write(' '.join(map(str,[a,g['name'].count('C'),*g['endpoint'],len(g['requirements']),len(g['raw_odd'])]))+'\n')
  for q in g['requirements']:
   x,y,v=q[:3];f.write(f'{x} {y} {int(v)}\n')
  for x,y in g['raw_odd']:f.write(f'{x} {y}\n')
print(p)
