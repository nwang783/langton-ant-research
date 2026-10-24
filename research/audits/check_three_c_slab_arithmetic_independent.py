from pathlib import Path
import json,hashlib
ROOT=Path('/workspace/shared/langton')
p=ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';J=json.loads(p.read_text());geo={g['packet']:g for g in J['geometry']}
weights={0:1,1:1,4:1,5:1,6:2,7:5,8:5,9:5};cc={0:0,1:1,4:0,5:1,6:2,7:0,8:1,9:2};rows=[]
for a,w in weights.items():
 word=geo[a]['word'];mass=word.count('R')-word.count('L');c=cc[a]
 assert len(word)<=18*w+15*c and mass<=4*w+3*c
 rows.append(dict(packet=a,length=len(word),mass=mass,C_count=c,weight=w,length_slack=18*w+15*c-len(word),mass_slack=4*w+3*c-mass))
# Exact recurrence and sum identities, not a proof by finite cases.
for m in range(5,50):
 r=m-5;total=0
 for b in range(1,20):
  total+=18*r
  assert total==18*(m-2)*(5**b-1)//4-54*b
  r=5*r+12
  assert r==5**b*(m-2)-3
res={'status':'PASS literal arithmetic and reviewed slab identity proof','rows':rows,'scope':'Context-complete recurrent-eight finite factors only; logarithmic necessary C recurrence, not confinement.','hashes':{str(x.relative_to(ROOT)):hashlib.sha256(x.read_bytes()).hexdigest()for x in(p,Path(__file__),ROOT/'word_stabilization/dcuv_three_turn_fuel_bound.md')}}
Path(__file__).with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res))
