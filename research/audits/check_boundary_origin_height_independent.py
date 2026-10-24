from pathlib import Path
import json,hashlib
P=Path(__file__).resolve();S=P.with_name('check_U1_young3_shadow_independent.py');exec(compile(S.read_text().split('rows=[];cases=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/boundary_origin_height_guard_frozen_20261023_1258';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:
 name=f.get('frozen',f.get('file'));assert hashlib.sha256((B/name).read_bytes()).hexdigest()==f['sha256']
HH=lambda z:int(z.imag-z.real);rows=[];k=[]
for h in range(4):
 for a in ids:
  I=[HH(rotation(z,h))for z in G[a][3]];O=[HH(rotation(z,h))for z in G[a][4]];d=max(O)-max(I);assert d<=4;rows.append((a,h,max(I),max(O),d))
 origin=rotation(-1,h);sh=(h+3)%4;values={max(HH(origin+rotation(z,sh))for z in G[a][3])for a in(4,5,6)};assert len(values)==1;k.append(values.pop())
assert k==[4,4,-4,-2];F=(30-48-1)//2;assert F==-10 and[F-v for v in k]==[-14,-14,-6,-8]
for S in range(-20,21):
 for B0 in range(-20,21):
  I=S-2*B0;assert(S-I-1)//2<B0
out=dict(status='PASS independent first-output envelope and directional first-source guard',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),rows=rows,kappa=k,U1_I48_F=F,U1_lower3_head_caps=[F-v for v in k],scope='Only consumed entry residual heights bounded; unused initial black cells unrestricted. Produced lower3 U event requires first V-family source and H(head)<=F-kappa. Entry identities exempt; near-domain I increase is finite, far exceptions retained. No record closure.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({x:y for x,y in out.items()if x!='rows'})
