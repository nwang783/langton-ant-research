#!/usr/bin/env python3
"""Independent exhaustive producer/output/consumer-input alignment queries.
Uses independently reconstructed literal geometry, never author query output.
"""
from pathlib import Path
import hashlib,json
from check_dcuv_producer_model_independent import geometry,rotation,xy,walk,raws,ordinary,protected,ROOT
ids=(0,1,4,5,6,7,8,9);mp={a:i for i,a in enumerate(ids)};cc=(0,1,0,1,2,0,1,2)
F=ROOT/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813';cp=F/'01_closure.tsv'
assert hashlib.sha256(cp.read_bytes()).hexdigest()=='f68f23f8189dc750489ed3aabd48741fde629d1263503ac9cff94fb703163f58'
rawrows=[tuple(map(int,l.split())) for l in cp.read_text().splitlines()];C={r[:8]for r in rawrows}
assert len(C)==487444
oldp=ROOT/'core_periodicity_new/chronology_dcuv/recurrent8_counted/closure.tsv';old={tuple(map(int,l.split()[:8]))for l in oldp.read_text().splitlines()}
lifts={(*r[:7],k)for r in old for k in ([4,5]if r[7]==4 else[r[7]])}
missing=lifts-C
assert all(r[7]==4 and (r[4]+4)%4!=0 for r in missing)

def cone(a,p,h,count):
 rem=count-cc[mp[a]]
 if rem<0:return False
 if rem>=2:return True
 end,dh,*_=walk(raws[a]);z=-1-1j
 d=rotation(2*p+rotation(z,h)-2*end-rotation(z,dh),-dh)
 x,y=xy(d);assert d==complex(x,y)
 if x%2 or y%2:return False
 x//=2;y//=2
 if rem:
  x-=1;y-=1
  return y>=0 and x<=y and (x+y)%2==0 and (y!=0 or x%4==0)
 return x>=0 and y>=x and (x+y)%2==0 and (x!=0 or y%4==0)

out={};queries=0;allrows=[]
for b in ids:
 for z in sorted(geometry[b]['inputs'],key=xy):
  rows=[];removed={'sector':0,'ordinary':0,'protected':0}
  for a in ids:
   for q in geometry[a]['outputs']:
    for h in range(4):
     p=q-rotation(z,h);r=(a,b,*xy(p),h,*xy(q))
     if(sum(xy(p))+h)%2:removed['sector']+=1;continue
     if r[:5]in ordinary:removed['ordinary']+=1;continue
     if r in protected:removed['protected']+=1;continue
     reasons=[]
     for k in range(5):
      reason='heading'if k<cc[mp[a]]or(h+k)%4 else'cone'if not cone(a,p,h,k)else'clause'if(mp[a],mp[b],*r[2:],k)in C else'OPEN'
      reasons.append(reason);queries+=1
     rows.append({'tuple':r,'reasons_0_through_4':reasons,'overflow5_excluded':(mp[a],mp[b],*r[2:],5)in C})
  opens=[sum(r['reasons_0_through_4'][k]=='OPEN'for r in rows)for k in range(5)]
  minimum=next((k for k,v in enumerate(opens)if v),5)
  out[f'{b}:{xy(z)}']={'admitted':len(rows),'removed':removed,'unexcluded_counts_0_to_4':opens,'certified_minimum_C_age':minimum,'rows':rows}
  allrows.extend(rows)
  print(b,xy(z),len(rows),opens,'minimum',minimum)
expected={(6,q)for q in geometry[6]['inputs']}|{(b,q)for b in(7,8,9)for q in(-1+4j,2j,3j)}
assert len(expected)==11
assert all(out[f'{b}:{xy(q)}']['certified_minimum_C_age']==5 for b,q in expected)
target=(7,7,0,4,0,0,7,4)
tr=[r for r in rawrows if r[:8]==target];assert len(tr)==1 and tr[0][8]==1
assert(*target[:7],5)not in C
# Rebuild EVERY author exact-four query, including heading/sector and HB rejects.
Q=F.parent/'age_five_queries';qm=json.loads((Q/'manifest.json').read_text())
for name,digest in qm.items():assert hashlib.sha256((Q/name).read_bytes()).hexdigest()==digest
A=json.loads((Q/'queries.json').read_text());actual={}
for b,z in expected:
 for a in ids:
  for q in geometry[a]['outputs']:
   for h in range(4):
    pose=q-rotation(z,h);r=(a,b,*xy(pose),h,*xy(q));cr=(mp[a],mp[b],*r[2:],4)
    status='heading'if h else'sector'if(sum(xy(pose))+h)%2 else'HB'if r[:5]in ordinary or r in protected else'counted'
    if status=='counted':assert cr in C
    actual[r,xy(z)]=(cr,status)
observed={(tuple(r['original_tuple']),tuple(r['target_input'])):(tuple(r['counted_tuple']),r['status'])for r in A['rows']}
assert len(actual)==2992
# Author status vocabulary is checked below, without trusting membership conclusions.
from collections import Counter
print('Author statuses',Counter(v[1]for v in observed.values()))
print('Independent statuses',Counter(v[1]for v in actual.values()))
assert set(actual)==set(observed)
for key,(cr,status) in actual.items():
 acr,astatus=observed[key];assert cr==acr
 normalized=astatus.lower().replace('signed_','').replace('new_','').replace('_clause','').replace('clause','counted').replace('count5','counted')
 assert normalized==status.lower(),(astatus,status)
result={'status':'PASS all eleven formerly age-four input slots require at least five C macros','target':tr[0],'target_overflow5_excluded':False,'old_clauses':len(old),'old_lifted':len(lifts),'old_lift_absent_but_heading_impossible':len(missing),'old_lift_logical_omissions':0,'queries':queries,'slots':out,'scope':'Complete recurrent-eight protected identity intervals. Source packet C included, consumer packet C excluded. Initial residual identities are exempt. Unexcluded counts are not feasibility claims.','hashes':{str(x.relative_to(ROOT)):hashlib.sha256(x.read_bytes()).hexdigest()for x in(cp,oldp,Path(__file__))}}
(ROOT/'audits/dcuv_count5_replay/queries.json').write_text(json.dumps(result,indent=2)+'\n')
print(result['status'],len(old),len(lifts))
