from pathlib import Path
import json,hashlib
P=Path(__file__).resolve();S=P.with_name('check_U1_young3_shadow_independent.py');exec(compile(S.read_text().split('rows=[];cases=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/atomic_bud_sharp_control_frozen_20261023_1331';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_atomic_bud_three_C_sharp_control.json').read_text());D=ROOT/'core_periodicity_new'
for f,hsh in J['dependencies'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==hsh
C5={tuple(map(int,l.split()[:8]))for l in(D/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv').read_text().splitlines()};HB={tuple(map(int,l.split()[:7]))for l in(D/'chronology_dcuv/protected_patch2.tsv').read_text().splitlines()};mp={a:i for i,a in enumerate(ids)}
seq=[0,0,0,1,5,5,0,4];assert seq==J['word'];word=''.join(raws[a]for a in seq);need=walk(word+mark)[2];board={z for z,b in need.items()if b};assert board=={complex(*q)for q in J['initial_actual_board']}and len(board)==14
p=0j;h=0;clock=0;ledger={z:None for z in board-K};records=[];queries=[]
for i,a in enumerate(seq):
 e,dh,need,I,O=G[a];core={p+rotation(z,h)for z in K};assert board==core|set(ledger)and not core&set(ledger)
 ins={p+rotation(z,h):z for z in I};assert set(ins)<=set(ledger);inputs=[]
 for q,z in ins.items():
  origin=ledger[q];age=None if origin is None else clock-origin[1]
  if origin is not None:
   ix,bc,src,sp,sh,slot=origin;rel=rotation(p-sp,-sh);hh=(h-sh)%4;hk=(src,a,*xy(rel),hh,*xy(slot));ck=(mp[src],mp[a],*xy(rel),hh,*xy(slot),min(5,age));assert hk not in HB and ck not in C5;queries.append((hk,ck))
  inputs.append((xy(q),age,origin[0]if origin is not None else None))
 if i==7:assert(p,h)==(1j,1)and set(inputs)=={((2,0),3,0),((3,1),3,1)}
 for q in ins:del ledger[q]
 for z in O:
  q=p+rotation(z,h);assert q not in ledger;ledger[q]=(i,clock,a,p,h,z)
 bb=set(board);q=p;hh=h
 for t,c in enumerate(raws[a]+mark):
  assert(q in bb)==(c=='L');bb.symmetric_difference_update({q});hh=(hh+(1 if c=='R'else-1))%4;q+=(1j,1,-1j,-1)[hh]
  if t+1==len(raws[a]):rawboard=set(bb);rawpose=(q,hh)
 assert rawpose==(p+rotation(e,h),(h+dh)%4)
 records.append((a,(*xy(p),h),clock,inputs,(*xy(rawpose[0]),rawpose[1])))
 board=rawboard;p,h=rawpose;clock+=counts[a];assert board==set(ledger)|{p+rotation(z,h)for z in K}
assert len(word)==149 and len(board)==35 and clock==3 and len(queries)==J['produced_HB_count_queries']==2
out=dict(status='PASS independent actual sharp atomic-bud consumption control',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),initial_mass=14,final_mass=35,raw_length=len(word),C=clock,rows=records,produced_queries=queries,scope='Continuous actual D,D,D,DC,VC,VC,D,V plus genuine following marker. First and SECOND/interior D buds survive until finalV entry then are consumed at exact postexitC3. Uniform atomic maturity cannot rise to4. No factor renewal, unfunded record, mass minimality or infinite word.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='rows'})
