from pathlib import Path
import json,hashlib
P=Path(__file__).resolve();prefix=P.with_name('check_qolder_relocation_independent.py').read_text().split('roots=list')[0];exec(compile(prefix,str(P.with_name('check_qolder_relocation_independent.py')),'exec'))
B=ROOT/'core_periodicity_new/u_age4_interior_control_frozen_20261023_1238';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_u_age4_interior_control.json').read_text())
for f,hsh in J['dependencies'].items():assert hashlib.sha256((W/f).read_bytes()).hexdigest()==hsh
outrows=[]
for control in J['controls']:
 seq=control['word'];board=set(map(lambda q:complex(*q),control['initial_actual_board']));start=control['rows'][0]['head'];p=complex(*start[:2]);h=start[2];ledger={q:None for q in board-{p+rotation(z,h)for z in K}};clock=0;rawtime=0;checked=0;scores=[]
 assert len(board)==18
 for i,a in enumerate(seq):
  row=control['rows'][i];assert row['head']==[*xy(p),h]and row['C']==clock
  core={p+rotation(z,h)for z in K};assert not(core&set(ledger))and board==core|set(ledger)
  I,O,need,e,dh=G[a];assert all((p+rotation(z,h)in board)==b for z,b in need.items());inp={p+rotation(z,h):z for z in I};assert set(inp)<=set(ledger)
  ages={};births={}
  for q,z in inp.items():
   birth=ledger[q];age=None if birth is None else clock-birth[1];ages[q]=age;births[q]=birth
   if birth is not None:
    step,bc,source,sp,sh,sslot=birth;rel=rotation(p-sp,-sh);hd=(h-sh)%4
    assert(source,a,*xy(rel),hd,*xy(sslot))not in HB and(mp[source],mp[a],*xy(rel),hd,*xy(sslot),min(5,age))not in C5;checked+=1
  assert ages=={complex(*r['cell']):r['age']for r in row['inputs']}
  if i==len(seq)-1:
   assert (p,h)==(0j,0)
   assert all(ages[q]==4 and births[q][0]==1 and births[q][2]==6 for q in(-1+1j,-1+2j))
   assert all(births[q]is None for q in(-1+4j,2j,3j))
  for q in inp:del ledger[q]
  for z in O:
   q=p+rotation(z,h);assert q not in ledger;ledger[q]=(i,clock,a,p,h,z)
  entry=2*int(p.imag-p.real)+A[(h+1)%4];created=2*int(p.imag-p.real)+T[a,(h+1)%4];assert row['record']==[entry,created];scores.append((entry,created))
  bb=set(board);point=p;heading=h
  for t,turn in enumerate(raws[a]+mark):
   assert(point in bb)==(turn=='L');bb.symmetric_difference_update({point});heading=(heading+(1 if turn=='R'else-1))%4;point+=(1j,1,-1j,-1)[heading]
   if t+1==len(raws[a]):rawboard=set(bb);rawpose=(point,heading)
  assert rawpose==(p+rotation(e,h),(h+dh)%4);assert row['raw_exit']==[*xy(rawpose[0]),rawpose[1]]
  board=rawboard;p,h=rawpose;assert board==set(ledger)|{p+rotation(z,h)for z in K};clock+=cc[a];rawtime+=len(raws[a])
 assert rawtime==control['raw_length']and len(board)==control['final_mass']and checked==control['produced_HB_count_queries']==5
 assert scores[0]==(30,26)and max(max(r)for r in scores[1:-1])==26
 outrows.append({'word':seq,'seed_mass':18,'raw_length':rawtime,'final_mass':len(board),'lower_ages':[4,4],'producer_index':1,'scores':scores})
# Last UCC is not silently promoted with U/UC: direct full-word conflict.
seq=J['controls'][0]['word'][:-1]+[9];start=J['controls'][0]['rows'][0]['head'];p=complex(*start[:2]);h=start[2];last={};conflict=None
for t,c in enumerate(''.join(raws[a]for a in seq)+mark):
 if p in last and last[p][1]==c:conflict={'cell':xy(p),'previous':last[p][0],'time':t,'turn':c};break
 last[p]=(t,c);h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
assert conflict and conflict['cell']==(-3,4)
out={'status':'PASS independent continuous physical boards and ordered interior age4 controls','manifest_sha256':hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),'controls':outrows,'UCC_conflict':conflict,'scope':'Actual interior-produced age4 is possible, but these controls are funded and fail strict U1 at the earlier DC entry tie. No min5, least mass, repeated renewal or capture claim.'}
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
