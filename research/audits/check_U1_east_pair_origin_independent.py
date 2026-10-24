from pathlib import Path
from collections import Counter
import hashlib,json
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
B=ROOT/'core_periodicity_new/U1_east_pair_origin_frozen_20261023_1852';m=json.loads((B/'manifest.json').read_text())
for f in m['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
M=json.loads((ROOT/'core_periodicity_new/atomic_core_record_interface_frozen_20261023_1359/04_root_out.json').read_text());pf=Path(M['potential_file']);assert hashlib.sha256(pf.read_bytes()).hexdigest()==M['potential_sha256'];w=json.loads(pf.read_text())['values'];H=lambda q:int(q.real+q.imag)
A=[H(rotation(-1+1j,h))+w[f'c{h}']for h in range(4)];assert A==[0,22,20,10]
K={q for q,b in walk(mark)[2].items()if b};G={}
for s in(7,8,9):
 e,dh,_,f=walk(raws[s]);black={q for q,b in walk(raws[s]+mark)[2].items()if b};G[s]=(black-K,(black^f)-{e+rotation(q,dh)for q in K},e,dh);assert{2+0j,2+1j}<=G[s][1]
I=sorted(G[7][0],key=xy);O=sorted(G[7][1],key=xy);e=rotation(G[7][2],1);peak=max(2*H(e)+A[1],*(2*H(rotation(o,1))+w[f'w_7_{j}_1']for j,o in enumerate(O)));assert peak==M['record_threshold']==30
rows=[]
for s in(7,8,9):
 for o in(2+0j,2+1j):
  for i in I:
   for h in range(4):
    p=i-rotation(o,h)
    if(sum(xy(p))+h)%2:r='sector';score=None
    elif(p,h)!=(-3+1j,0)or i!={2+0j:-1+1j,2+1j:-1+2j}[o]:r='rigid_pair_geometry';score=None
    else:
     score=2*H(rotation(p,1))+A[1];assert score==peak;r='original_entry_tie'
    rows.append(dict(source=s,output=xy(o),goal_input=xy(i),source_pose=(*xy(p),h),reason=r,earlier_entry_score=score))
assert Counter(r['reason']for r in rows)==dict(sector=60,rigid_pair_geometry=54,original_entry_tie=6)
out=dict(status='PASS original strict U1 all-age east-pair provenance exclusion',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),literal_core_offsets=A,goal_global_phase=1,goal_creation_peak=peak,counts=dict(Counter(r['reason']for r in rows)),rows=rows,scope='Original earlier full ENTERING-core observation suffices, even factor-first creator. No enlarged atomic history or C-age premise; genuine earlier producer within same factor only. Original11/13 funding ledger unchanged.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
