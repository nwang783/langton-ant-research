"""Separate literal movement inventory for the F-to-east13 obstruction."""
import itertools,collections,json,hashlib,pathlib
D=[1j,1,-1j,-1];board={};z=1-1j;h=0
for c in 'RRRRLR':
 bit=int(c=='L');old=board.get(z,0 if z.imag>=-1 else None)
 assert old is None or old==bit
 board[z]=1-bit;h=(h+(1 if bit==0 else -1))%4;z+=D[h]
assert z==0 and h==0
records=[];hist=collections.Counter();legal=[]
for west in itertools.combinations(range(7),2):
 for south in itertools.combinations(range(6),3):
  ds=[]
  for i in range(7):
   ds.append(3 if i in west else 1)
   if i<6:ds.append(2 if i in south else 0)
  assert sum(D[d] for d in ds)==3
  b=board.copy();z=0j;h=0;word='';last={}
  for t,d in enumerate(ds):
   assert (d-h)%4 in (1,3)
   bit=int((d-h)%4==3);old=b.get(z,0 if z.imag>=-1 else None)
   if old is not None and old!=bit:
    hist[t]+=1
    records.append(dict(west=west,south=south,read=t,cell=[int(z.real),int(z.imag)],required='RL'[bit],available='RL'[old],word_prefix=word))
    break
   b[z]=1-bit;word+='RL'[bit];h=d;z+=D[d]
  else:legal.append(dict(west=west,south=south,word=word,heading=h))
assert len(records)+len(legal)==420
p=pathlib.Path(__file__);raw=json.dumps(records,sort_keys=True,separators=(',',':')).encode()
p.with_suffix('.records.json').write_bytes(raw+b'\n')
out=dict(status='ALL420 CONFLICT' if not legal else 'LOCAL SURVIVOR',candidates=420,conflict_histogram=dict(hist),latest_conflict=max(hist),survivors=legal,records_sha256=hashlib.sha256(raw+b'\n').hexdigest())
p.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
