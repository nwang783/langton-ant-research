import itertools,pathlib,json,time,hashlib
from bounded_charge_state_transfer import *
p=pathlib.Path(__file__).parent

def main():
 start=time.monotonic();records=[];controllers=0;formula_checks=0;literal_checks=0;letters=0;seen_roots=0
 for m in (1,2):
  for Rs in itertools.combinations(range(0,8,2),m):
   for Ls in itertools.combinations(range(1,8,2),m):
    active=Rs+Ls
    for bits in itertools.product(range(2),repeat=2*m):
     images=['R','L']*4
     for s,b in zip(active,bits):images[s]=(('RLLLL','LLLLR') if s%2==0 else ('LRRRR','RRRRL'))[b]
     controllers+=1
     # The incidence formula is checked directly, not inferred from charge certificates.
     M=[[0]*8 for _ in range(8)]
     for s,w in enumerate(images):
      for _,hj,j in image_data(w)[0]:M[s][2*((s//2+hj)%4)+j]+=1
     E=[1,-1]*4
     for r in range(9):
      expected=[Q(1 if s%2==0 else -1)+Q(4,m)*((1-m)**r-1)*(int(s in Rs)-int(s in Ls)) for s in range(8)]
      assert E==expected;formula_checks+=8;E=mv(M,E)
     for root in active:
      try:info=validate_state_images(images,0,root)
      except AssertionError:continue
      seen_roots+=1
      # Different powers of one root cycle define different root words, retain all.
      charge=checkpoint_charge_certificate(images,0,root);assert charge['bounded']
      d, mats, init = None,None,None
      # Direct geometric checks at all levels, not only true root-limit phases.
      _,d,mats,z=cyclotomic_matrices(images,0,3,1,2,root)
      for r in range(4):
       occ,pose,h,n=literal_state_occupation(images,root,r)
       assert z[root*d:(root+1)*d]==eval_occupation(occ,3,1,2)
       literal_checks+=1;letters+=n;z=mv(mats[r%len(mats)],z)
      tests=[]
      for q,u,v in ((2,1,0),(2,0,1),(2,1,1),(3,1,0),(3,0,1),(3,1,1),(3,1,2),(4,1,0),(4,0,1),(4,1,1),(4,1,2),(4,2,1)):
       t=character_test(images,0,q,u,v,root);tests.append(t)
       if not t['bounded']:break
      records.append(dict(m=m,images=images,root=root,root_period=info['root_period'],charge=charge,
        excluded=any(not t['bounded'] for t in tests),tests=tests))
 raw=json.dumps(records,sort_keys=True,separators=(',',':')).encode()+b'\n';(p/'five_charge_controllers.records.json').write_bytes(raw)
 out=dict(controllers=controllers,root_cases=seen_roots,formula_checks=formula_checks,literal_checks=literal_checks,literal_letters=letters,
  fourier_excluded=sum(r['excluded'] for r in records),
  survivors=[{k:r[k] for k in ('m','images','root','root_period')} for r in records if not r['excluded']],
  records_sha256=hashlib.sha256(raw).hexdigest(),seconds=time.monotonic()-start)
 (p/'five_charge_controllers.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
