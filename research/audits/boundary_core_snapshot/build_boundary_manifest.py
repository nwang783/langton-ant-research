import json,hashlib,pathlib
b=pathlib.Path(__file__).resolve().parent;out={}
for m in range(11,15):
 d=json.load(open(b/f'boundary_m{m}_certificate.json'));assert d['capture_time_in_u_v']==[0,416,416*200+312*m+197704]
 assert d['domain']==f'integer n>=200, fixed m={m}'
 for stage in ('two_bit','three_bit'):
  for name in ('archive','finite_reads'):
   x=d['interfaces'][stage][name]
   assert x['u_lower_m_coefficient']==-4 and x['u_lower_constant']==-130
   assert x['z_upper']==(71 if stage=='two_bit' else 75)
   if stage=='two_bit':assert x['u_upper']==98
 g=json.load(open(b/f'boundary_m{m}_geometry.json'));assert g['common_diagonal_cross_half_width']==82
 out[str(m)]={'time':d['capture_time_in_u_v'],'sha256':hashlib.sha256((b/f'boundary_m{m}_certificate.json').read_bytes()).hexdigest()}
manifest={'status':'all fixed boundary instances passed; independent audit pending','domain':'m in{11,12,13,14}, n>=200','instances':out}
(b/'boundary_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');print(json.dumps(manifest,indent=2))
