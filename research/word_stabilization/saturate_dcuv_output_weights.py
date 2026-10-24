from pathlib import Path
import json,sys,hashlib,subprocess
R=Path(__file__).resolve().parents[1];D=R/'core_periodicity_new/chronology_dcuv';G=json.loads((D/'literal_residual_geometry.json').read_text())['geometry'];src=Path(sys.argv[1]);out=Path(sys.argv[2]);J=json.loads(src.read_text());v=J['values'];old=dict(v);d=v['ax'],v['ay'];K=J.get('kept_packet_types',list(range(10)));peaks=[]
def rot(z,h):x,y=z;return [(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def L(z):return d[0]*z[0]+d[1]*z[1]
def a(h):return L(rot((-1,1),h))+v[f'c{h%4}']
for i in K:
 g=G[i];e=g['endpoint']
 for h in range(4):
  T=max([2*L(rot(e[:2],h))+a(h+e[2])]+[2*L(rot(q,h))+old[f'w_{i}_{j}_{h}'] for j,q in enumerate(g['outputs'])]);peaks.append([i,h,T])
  for j,q in enumerate(g['outputs']):
   key=f'w_{i}_{j}_{h}';v[key]=T-2*L(rot(q,h));assert v[key]>=old[key]
J['saturation']={'source':str(src),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'rule':'Raise each output token to its producing packet maximum T; exact local peak unchanged','peaks':peaks,'raised_count':sum(v[k]>old[k]for k in v),'new_max_output_weight':max(x for k,x in v.items()if k.startswith('w_')),'warning':'Conditional potential only; no transfer exclusion inferred.'};out.write_text(json.dumps(J,indent=2)+'\n');subprocess.run(['python',str(R/'word_stabilization/check_dcuv_directional_candidate.py'),str(out)],check=True)
