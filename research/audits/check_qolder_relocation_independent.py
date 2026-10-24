from pathlib import Path
from collections import Counter
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
B=ROOT/'core_periodicity_new/qolder_low_record_relocation_frozen_20261023_1219';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_qolder_low_record_relocation.json').read_text());W=ROOT/'core_periodicity_new'
for p,h in J['dependencies'].items():assert hashlib.sha256((W/p).read_bytes()).hexdigest()==h
K={z for z,b in walk(mark)[2].items()if b};ids=(0,1,4,5,6,7,8,9);cc=dict(zip(ids,(0,1,0,1,2,0,1,2)));mp={a:i for i,a in enumerate(ids)};G={}
for a in ids:
 e,dh,_,flip=walk(raws[a]);need=walk(raws[a]+mark)[2];black={z for z,b in need.items()if b};I=black-K;O=(black^flip)-{e+rotation(z,dh)for z in K};G[a]=(I,O,need,e,dh)
meta=json.loads((W/'chronology_dcuv/delayed_height_probe/u1_residue_cegar/root_out.json').read_text());pp=Path(meta['potential_file']);assert hashlib.sha256(pp.read_bytes()).hexdigest()==meta['potential_sha256'];v=json.loads(pp.read_text())['values']
A=[int(rotation(-1+1j,h).real+rotation(-1+1j,h).imag)+v[f'c{h}']for h in range(4)];T={}
for a in ids:
 I,O,need,e,dh=G[a]
 for h in range(4):
  HH=lambda z:int(rotation(z,h).real+rotation(z,h).imag)
  T[a,h]=max(2*HH(e)+A[(h+dh)%4],*(2*HH(o)+v[f'w_{a}_{j}_{h}']for j,o in enumerate(sorted(O,key=xy))))
HB={tuple(map(int,l.split()[:7]))for l in(W/'chronology_dcuv/protected_patch2.tsv').read_text().splitlines()};C5={tuple(map(int,l.split()[:8]))for l in(W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv').read_text().splitlines()}
roots=list(map(lambda p:complex(*p),J['initial_residual_roots']));assert len(roots)==len(set(roots));ledger={p:None for p in roots};schedule=J['schedule'];h=schedule[0]['head'][2];clock=0;oldend=None;broken=0;peak=-10**9;produced=0;rawreads=0;counts=Counter()
assert max(int(p.imag-p.real)for p in roots)==-17 and all(48+2*int(p.imag-p.real)<30 for p in roots)
for i,row in enumerate(schedule):
 a=row['packet'];p=complex(*row['head'][:2]);assert row['head'][2]==h and row['C']==clock and (int(p.real+p.imag)+h)%2==0
 core={p+rotation(z,h)for z in K};assert not(core&set(ledger));board=set(ledger)|core
 if i==0:assert sorted(map(xy,board))==list(map(tuple,J['initial_actual_board'])) and len(board)==646
 if oldend is not None:broken+=oldend!=(p,h)
 I,O,need,e,dh=G[a];assert all((p+rotation(z,h)in board)==b for z,b in need.items())
 inp={p+rotation(z,h):z for z in I};assert set(inp)<=set(ledger);births={z:ledger[z]for z in inp};ownrows={}
 for z,slot in inp.items():
  birth=ledger[z];age=None if birth is None else clock-birth[1]
  if birth is not None:
   step,bclock,source,sp,sh,sslot=birth
   minimum=3 if a in(0,1)or slot in(-1+1j,-1+2j)else 5 if a in(6,7,8,9)else 2 if slot==3j else 3
   assert age>=minimum
   rel=rotation(p-sp,-sh);hd=(h-sh)%4
   assert(source,a,*xy(rel),hd,*xy(sslot))not in HB
   assert(mp[source],mp[a],*xy(rel),hd,*xy(sslot),min(5,age))not in C5;produced+=1
  ownrows[z]=(age,birth)
 assert {complex(*x['cell']):x['age']for x in row['inputs']}=={z:a for z,(a,b)in ownrows.items()}
 if i==len(schedule)-1:goal=ownrows.copy()
 for z in inp:del ledger[z]
 for slot in O:
  z=p+rotation(slot,h);assert z not in ledger;ledger[z]=(i,clock,a,p,h,slot)
 # Replay every local raw+true marker, retaining exact raw exit board.
 point=p;head=h;rawboard=None
 for t,turn in enumerate(raws[a]+mark):
  assert(point in board)==(turn=='L');board.symmetric_difference_update({point});head=(head+(1 if turn=='R'else-1))%4;point+=(1j,1,-1j,-1)[head]
  if t+1==len(raws[a]):rawboard=set(board);rawpose=(point,head)
 assert rawpose==(p+rotation(e,h),(h+dh)%4)
 ec={rawpose[0]+rotation(z,rawpose[1])for z in K};assert not(ec&set(ledger))and rawboard==set(ledger)|ec
 entry=2*int(p.imag-p.real)+A[(h+1)%4];created=2*int(p.imag-p.real)+T[a,(h+1)%4];assert row['record']==[entry,created]
 if i<len(schedule)-1:assert max(entry,created)<30;peak=max(peak,entry,created)
 else:assert (entry,created)==(22,30)
 assert row['raw_exit']==[*xy(rawpose[0]),rawpose[1]]
 oldend=rawpose;h=rawpose[1];clock+=cc[a];counts[a]+=1;rawreads+=len(raws[a])
assert counts==Counter({0:158,1:638,7:1})and len(schedule)==797 and broken==796 and peak==26 and produced==160 and rawreads==17558 and len(rawboard)==2564
ages=[goal[z][0]for z in(-1+1j,-1+2j,-1+4j,2j,3j)];assert ages==[6,479,598,282,598]and all(goal[z][1]is not None for z in goal)
a,q,b,c,d=[goal[z]for z in(-1+1j,-1+2j,-1+4j,2j,3j)]
assert q[1][0]<=max(a[1][0],c[1][0])and q[1][0]<=max(a[1][0],d[1][0])and q[0]>=min(a[0],c[0])and q[0]>=min(a[0],d[0])
out={'status':'PASS independent LOCAL relocation board/identity/age/record replay only','manifest_sha256':hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),'packets':797,'broken_position_junctions':796,'initial_mass':646,'initial_max_residual_height':-17,'initial_weight':48,'prior_record_max':26,'goal_record':[22,30],'goal_ages':ages,'produced_identity_checks':160,'final_mass':2564,'scope':'Every positional junction is deliberately nonphysical. This only refutes a local-record deduction omitting live-core transport and full chronology; not an actual word, U1 counterexample, renewal, capture/noncapture or global factor-language witness.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
