from pathlib import Path
import itertools,json,hashlib
P=Path(__file__).resolve().parents[1];D=[1j,1,-1j,-1];F='RRRRLR';p=1-1j;h=1j;board={}
for c in F:
 bit=c=='L';assert p not in board or board[p]==bit;assert p in board or p.imag<-1 or not bit
 board[p]=not bit;h*=1j if bit else-1j;p+=h
assert p==0j and h==1j
records=[]
for west in itertools.combinations(range(7),2):
 for south in itertools.combinations(range(6),3):
  moves=[]
  for j in range(13):moves.append((-1 if j//2 in west else 1)if j%2==0 else(-1j if j//2 in south else 1j))
  assert sum(moves)==3
  p=0j;h=1j;b=board.copy();prev={};bad=None
  for t,g in enumerate(moves):
   assert g/h in (1j,-1j);bit=g==h*1j;old=b.get(p,False if p.imag>=-1 else None)
   if old is not None and old!=bit:bad=t;break
   b[p]=not bit;h=g;p+=g
  assert bad is not None
  records.append({'west_slots':west,'south_slots':south,'first_conflict':bad})
assert len(records)==420
out={'status':'PASS all420 geometrically possible east13 blocks conflict after the forced pristine F suffix','cases':len(records),'latest_conflict':max(r['first_conflict']for r in records),'initial_output_board':sorted((int(z.real),int(z.imag),int(v))for z,v in board.items()),'records':records}
(P/'audits/k13_fresh_tail_independent.json').write_text(json.dumps(out,indent=2));print({k:v for k,v in out.items()if k!='records'})
