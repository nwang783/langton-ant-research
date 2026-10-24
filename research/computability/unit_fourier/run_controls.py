import json,pathlib,itertools,time,hashlib
from fourier_transfer import *
HERE=pathlib.Path(__file__).parent

def main():
 start=time.monotonic();inventory=json.loads((HERE.parent.parent/'causal_reduction/unit_scale/probe_charge_preserving_nine.json').read_text())
 controls=[]
 # Geometric controls across all four Gaussian units. These need not be ant-legal.
 for a in range(4):
  got=[None,None]
  for k in range(3,14,2):
   for tup in itertools.product('RL',repeat=k):
    w=''.join(tup);charge=w.count('R')-w.count('L')
    if charge not in(-1,1):continue
    j=0 if charge==1 else 1
    if got[j] is not None:continue
    _,p,h=image_data(w)
    if p==rotate((charge,0),a) and h==charge%4:got[j]=w
   if all(got):break
  assert all(got)
  # Choose same length by regenerating if first hits came at unequal lengths.
  k=max(map(len,got))
  for j in range(2):
   if len(got[j])==k:continue
   sign=1 if j==0 else -1
   got[j]=next(''.join(tup) for tup in itertools.product('RL',repeat=k)
    if (lambda w: w.count('R')-w.count('L')==sign and image_data(w)[1:]==(rotate((sign,0),a),sign%4))(''.join(tup)))
  controls.append((a,tuple(got)))
 controls.append((0,('RLLLLRRRR','RRRRRLLLRLLLL')))
 checks=0;letters=0
 for a,images in controls:
  for q,u,v in ((2,1,0),(2,1,1),(3,1,2),(4,1,0),(5,2,3)):
   d,mats,z=phase_matrices(images,a,q,u,v)
   for r in range(5):
    for j,root in enumerate('RL'):
     occ,p,h=literal_occupation(images,root,r)
     expected=eval_occupation(occ,q,u,v)
     assert z[j*d:(j+1)*d]==expected,(a,images,q,u,v,r,root,z[j*d:(j+1)*d],expected)
     assert p==rotate((1 if j==0 else -1,0),a*r)
     assert h==(1 if j==0 else -1)%4
     checks+=1
     word=root
     for _ in range(r):word=''.join(images[0 if c=='R' else 1] for c in word)
     letters+=len(word)
    z=mv(mats[r%len(mats)],z)
 records=[]
 for R in inventory['R_images']:
  if not R.startswith('R'):continue
  for L in inventory['L_images']:
   result=[]
   for q,u,v in ((1,0,0),(2,1,0),(2,0,1),(2,1,1),(3,1,0),(3,0,1),(3,1,1),(3,1,2),(4,1,0),(4,0,1),(4,1,1),(4,1,2),(4,2,1)):
    ans=test_character((R,L),0,q,u,v)
    result.append(ans)
    if not ans['bounded']:break
   records.append(dict(R=R,L=L,ruled_out=any(not x['bounded'] for x in result),characters=result))
 data=json.dumps(records,sort_keys=True,separators=(',',':')).encode()+b'\n'
 (HERE/'unit9_fourier.records.json').write_bytes(data)
 out=dict(geometric_controls=controls,literal_checks=checks,literal_letters=letters,
   unit9_cases=len(records),unit9_unbounded=sum(r['ruled_out'] for r in records),
   surviving_images=[dict(R=r['R'],L=r['L']) for r in records if not r['ruled_out']],
   first_obstructions=[dict(R=r['R'],L=r['L'],modulus=r['characters'][-1]['modulus'],character=r['characters'][-1]['character'],
    recurrences=[c['polynomial'] for c in r['characters'][-1]['certificates'] if not c['bounded']]) for r in records if r['ruled_out']],
   records_sha256=hashlib.sha256(data).hexdigest(),seconds=time.monotonic()-start)
 (HERE/'unit9_fourier.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
