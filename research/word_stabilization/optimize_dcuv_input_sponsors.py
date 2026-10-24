"""Exact finite sponsor selection for a frozen saturated packet-peak potential."""
from pathlib import Path
import json,itertools,sys,subprocess,hashlib
R=Path(__file__).resolve().parents[1];D=R/'core_periodicity_new/chronology_dcuv';src=Path(sys.argv[1]);out=Path(sys.argv[2]);J=json.loads(src.read_text());v=J['values'];G=json.loads((D/'literal_residual_geometry.json').read_text())['geometry'];inventory=json.loads((D/'transfer_inventory.json').read_text());K=J.get('kept_packet_types',list(range(10)));d=v['ax'],v['ay'];wmin=min(z for k,z in v.items()if k.startswith('w_'));low=wmin-1
obs={tuple(map(int,l.split()))for l in Path(J['observed_file']).read_text().splitlines()};rows=[e for e in inventory['protected_survivors']if e['tuple'][0]in K and e['tuple'][1]in K];ordinary=[e for e in inventory['ordinary_survivors']if e['tuple'][0]in K and e['tuple'][1]in K];proof=[]
def rot(z,h):x,y=z;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def L(z):return d[0]*z[0]+d[1]*z[1]
def a(h):return L(rot((-1,1),h))+v[f'c{h%4}']
for b in K:
 g=G[b];e=g['endpoint'];choices=[];requirements=[]
 for th in range(4):
  T=max([2*L(rot(e[:2],th))+a(th+e[2])]+[2*L(rot(q,th))+v[f'w_{b}_{i}_{th}']for i,q in enumerate(g['outputs'])]);req=[T-2*L(rot(q,th))for q in g['inputs']];requirements.append(req)
  cs=[]
  for slot in ([-1]if T<=a(th)else range(len(req))):
   bad=set();observed_bad=False
   for z,r in enumerate(rows):
    aa,bb,x,y,dh,*q=r['tuple']
    if bb!=b or r['target_input_slot']!=slot:continue
    sh=(th-dh)%4
    if req[slot]>v[f'w_{aa}_{r["source_output_slot"]}_{sh}']:bad.add(z)
   for r in ordinary:
    aa,bb,x,y,dh,*q=r['tuple']
    if tuple(r['tuple'])not in obs or bb!=b or r['target_input_slot']!=slot:continue
    if req[slot]>v[f'w_{aa}_{r["source_output_slot"]}_{(th-dh)%4}']:observed_bad=True
   if not observed_bad:cs.append((slot,bad))
  assert cs,(b,th);choices.append(cs)
 best=min(itertools.product(*choices),key=lambda cc:(len(set().union(*(c[1]for c in cc))),tuple(c[0]for c in cc)))
 for th,(slot,bad)in enumerate(best):
  for i in range(len(g['inputs'])):v[f'u_{b}_{i}_{th}']=requirements[th][i]if i==slot else low
 proof.append({'packet':b,'sponsors':[c[0]for c in best],'remaining_count':len(set().union(*(c[1]for c in best))),'available_choice_counts':list(map(len,choices))})
J['sponsor_optimization']={'source':str(src),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'low_input_weight':low,'method':'Exhaustive four-heading sponsor combinations independently per consumer packet, observed transfers hard-preserved','proof':proof,'warning':'Only minimizes these single-sponsor choices for the frozen output/core values. No global optimality or exclusion claim.'};out.write_text(json.dumps(J,indent=2)+'\n');subprocess.run(['python',str(R/'word_stabilization/check_dcuv_directional_candidate.py'),str(out)],check=True)
