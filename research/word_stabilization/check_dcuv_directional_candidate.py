"""Exact integer replay of a discovered DCUV directional potential; no SMT trust."""
from pathlib import Path
import json,sys,hashlib,collections
P=Path(__file__).resolve().parents[1]/'core_periodicity_new/chronology_dcuv'
f=Path(sys.argv[1]);m=json.loads(f.read_text());v=m['values'];G=json.loads((P/'literal_residual_geometry.json').read_text())['geometry'];K=m.get('kept_packet_types',list(range(10)));d=(v['ax'],v['ay']);assert d!=(0,0)
def r(z,h):x,y=z;return [(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def L(z):return d[0]*z[0]+d[1]*z[1]
def u(a,k,h):return v[f'u_{a}_{k}_{h%4}']
def w(a,k,h):return v[f'w_{a}_{k}_{h%4}']
n=0;policies=[];fail=[]
for a in K:
 g=G[a]
 for h in range(4):
  anchor=L(r((-1,1),h));old=[v[f'c{h}']]+[2*L(r(p,h))-anchor+u(a,k,h)for k,p in enumerate(g['inputs'])]
  end=g['endpoint'];new=[2*L(r(end[:2],h))+L(r((-1,1),h+end[2]))-anchor+v[f'c{(h+end[2])%4}']]+[2*L(r(p,h))-anchor+w(a,k,h)for k,p in enumerate(g['outputs'])]
  policies.append({'packet':a,'heading':h,'max_old_index':max(range(len(old)),key=old.__getitem__),'old':old,'new':new})
  for k,z in enumerate(new):
   n+=1
   if z>max(old):fail.append([a,h,k,z,max(old)])
inv=json.loads((P/'transfer_inventory.json').read_text());bad=[];passing=[]
for e in inv['protected_survivors']:
 if e['tuple'][0]not in K or e['tuple'][1]not in K:continue
 a,b,x,y,dh,qx,qy=e['tuple'];k=e['source_output_slot'];j=e['target_input_slot'];viol=[h for h in range(4)if u(b,j,h+dh)>w(a,k,h)]
 (bad if viol else passing).append(dict(e,violating_headings=viol))
by={tuple(e['tuple']):e for e in inv['ordinary_survivors']};obsfail=[];obsfile=Path(m['observed_file'])
for line in obsfile.read_text().splitlines():
 t=tuple(map(int,line.split()));
 if t[0]not in K or t[1]not in K:continue
 e=by[t];a,b,x,y,dh,qx,qy=t;k=e['source_output_slot'];j=e['target_input_slot'];viol=[h for h in range(4)if u(b,j,h+dh)>w(a,k,h)]
 if viol:obsfail.append([t,viol])
out={'status':'exact arithmetic PASS, conditional only'if not fail and not obsfail else'FAIL','potential_file':str(f),'potential_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'direction':d,'local_checks':n,'local_failures':fail,'observed_control_failures':obsfail,'passing_count':len(passing),'remaining_count':len(bad),'remaining_by_target':dict(collections.Counter(G[e['tuple'][1]]['name']for e in bad)),'remaining_by_source':dict(collections.Counter(G[e['tuple'][0]]['name']for e in bad)),'remaining':bad,'policies':policies}
f.with_name(f.stem+'_checked.json').write_text(json.dumps(out,indent=2)+'\n')
f.with_name(f.stem+'_remaining.tsv').write_text(''.join('\t'.join(map(str,e['tuple']))+'\n'for e in bad))
print(json.dumps({k:v for k,v in out.items()if k not in ['remaining','policies']},indent=2));assert not fail and not obsfail
