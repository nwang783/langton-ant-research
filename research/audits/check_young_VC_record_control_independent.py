from pathlib import Path
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
B=ROOT/'core_periodicity_new/young_U_VC_control_frozen_20261023_1132';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_young_U_VC_literal_control.json').read_text());model=json.loads((B/'04_root_out.json').read_text());pot=Path(model['potential_file']);assert hashlib.sha256(pot.read_bytes()).hexdigest()==model['potential_sha256'];w=json.loads(pot.read_text())['values']
core={z for z,c in walk(mark)[2].items()if c};ids=(0,1,4,5,6,7,8,9);cc=dict(zip(ids,(0,1,0,1,2,0,1,2)));G={};H=lambda z:int(z.real+z.imag)
A=[H(rotation(-1+1j,h))+w[f'c{h}']for h in range(4)];assert A==model['core_offsets'];T={}
for a in ids:
 e,h,_,flip=walk(raws[a]);need=walk(raws[a]+mark)[2];black={z for z,b in need.items()if b};I=sorted(black-core,key=xy);O=sorted((black^flip)-{e+rotation(z,h)for z in core},key=xy);G[a]=(I,O,need,e,h)
 for hh in range(4):T[a,hh]=max(2*H(rotation(e,hh))+A[(hh+h)%4],*(2*H(rotation(o,hh))+w[f'w_{a}_{i}_{hh}']for i,o in enumerate(O)))
seq=J['word'];word=''.join(raws[a]for a in seq)+mark;req=walk(word)[2];seed={z for z,b in req.items()if b};assert sorted(map(xy,seed))==list(map(tuple,J['seed']))and len(seed)==16
board=set(seed);ledger={z:('entry',None)for z in seed-core};p=0j;h=0;clock=0;t=0;watched=set(map(lambda z:complex(*z),J['protected_points']));held=None;records=[]
for j,a in enumerate(seq):
 I,O,need,e,dh=G[a];cphys={p+rotation(z,h)for z in core};assert board==cphys|set(ledger)and not(cphys&set(ledger))
 assert all((p+rotation(z,h)in board)==b for z,b in need.items())
 inputs=[p+rotation(z,h)for z in I];birth=[ledger[z]for z in inputs];ages=[None if b[1]is None else clock-b[1]for b in birth]
 entry=2*H(p)+A[h];peak=2*H(p)+T[a,h];r=J['rows'][j]
 assert r['pose']==[*xy(p),h]and r['C_clock']==clock and r['raw_time']==t
 assert list(map(tuple,r['input_cells']))==list(map(xy,inputs))and list(map(tuple,r['input_births']))==birth and r['input_ages']==ages
 assert (r['entering_core_value'],r['created_peak'])==(entry,peak)
 if j:
  assert all(ledger[z]==held[z]for z in watched)
  if j<len(seq)-1:assert not(watched&{p+rotation(z,h)for z in need})
 if j<len(seq)-1:assert max(entry,peak)<28
 else:assert (p,h)==(-1j,1)and peak==28 and birth==[(0,0),(0,0),('entry',None),('entry',None),('entry',None)]and ages==[3,3,None,None,None]
 for z in inputs:del ledger[z]
 for z in O:
  q=p+rotation(z,h);assert q not in ledger;ledger[q]=(j,clock)
 for c in raws[a]:
  assert (p in board)==(c=='L');board.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h];t+=1
 clock+=cc[a]
 if j==0:held={z:ledger[z]for z in watched}
 records.append((entry,peak))
assert t==155 and clock==3
for c in mark:
 assert (p in board)==(c=='L');board.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h];t+=1
assert t==166
activations=[]
for z in sorted(map(lambda q:complex(*q),J['older_upper_points']),key=xy):
 val=28+2*H(z);assert val>=28;activations.append(val)
assert activations==[30,32,36]
out={'status':'PASS','manifest_sha256':hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),'seed_mass':16,'word':seq,'raw_plus_marker':166,'earlier_core_and_creation_pairs':records[:-1],'target_pair':records[-1],'upper_initial_activations':activations,'scope':'Actual lower-pair age3 VC control retaining all five target identities and strict full record cuts. Upper entry identities fund it; not an unfunded U1 record, recurrence or capture counterexample.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
