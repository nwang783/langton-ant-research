from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];D=R/'core_periodicity_new/chronology_dcuv';O=D/'record_head_offset_search';source=O/'head_1_1.json';J=json.loads(source.read_text());G=json.loads((D/'literal_residual_geometry.json').read_text());K=J['kept_packet_types'];v=J['values'];A=[0,22,20,18]
def rot(q,h):x,y=q;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def L(q):return q[0]+q[1]
def T(a,h):e=G['geometry'][a]['endpoint'];return 2*L(rot(e[:2],h))+A[(h+e[2])%4]
for h in range(4):v[f'c{h}']=A[h]-L(rot((-1,1),h))
for a in K:
 g=G['geometry'][a]
 for h in range(4):
  for i,q in enumerate(g['outputs']):v[f'w_{a}_{i}_{h}']=T(a,h)-2*L(rot(q,h))
  for i,q in enumerate(g['inputs']):v[f'u_{a}_{i}_{h}']=T(a,h)-2*L(rot(q,h))
I=max(T(a,h)-2*L(rot(q,h))for a in K for h in range(4)for q in G['geometry'][a]['inputs']);activation=max(0,max(I+2*L(rot(q,h))-A[h]for a in K for h in range(4)for q in G['geometry'][a]['inputs']));events=[{'packet':a,'name':G['geometry'][a]['name'],'phase':h,'old_core':A[h],'peak':T(a,h)}for a in K for h in range(4)if T(a,h)>A[h]]
J.update({'status':'RECORD-ONLY alternate; zero event certificates transferred from original potential','parent':str(source.resolve()),'parent_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'direction':[1,1],'record_head_offsets':{'direction':[1,1],'A':A,'rule':'All created peaks equal new core; exact saturated output values'},'alternate_arithmetic':{'initial_activation_weight':I,'activation_increase_bound':activation,'record_events':events}})
(O/'head_1_1_A3_18.json').write_text(json.dumps(J,indent=2)+'\n');print(json.dumps(J['alternate_arithmetic'],indent=2))
