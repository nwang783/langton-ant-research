from pathlib import Path
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
B=ROOT/'core_periodicity_new/U1_young3_shadow_frozen_20261023_1220'
M=json.loads((B/'manifest.json').read_text())
for f in M['files']: assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_U1_young3_predecessor_shadow.json').read_text())
model=json.loads((B/'05_root_out.json').read_text());pf=Path(model['potential_file']);assert hashlib.sha256(pf.read_bytes()).hexdigest()==model['potential_sha256'];w=json.loads(pf.read_text())['values']
K={z for z,b in walk(mark)[2].items()if b};ids=(0,1,4,5,6,7,8,9);counts=dict(zip(ids,(0,1,0,1,2,0,1,2)));base={a:(0 if a<4 else 4 if a<7 else 7)for a in ids}
H=lambda z:int(z.real+z.imag)
A=[H(rotation(-1+1j,h))+w[f'c{h}']for h in range(4)];assert A==[0,22,20,10]
G={}
for a in ids:
 e,dh,_,flips=walk(raws[a]);need=walk(raws[a]+mark)[2];bs={z for z,b in need.items()if b};I=bs-K;O=(bs^flips)-{e+rotation(z,dh)for z in K};G[a]=(e,dh,need,I,O)
 assert dh==(-counts[a])%4
 assert G[a][3]==G[base[a]][3]
 assert raws[a]==raws[base[a]]+(raws[1][len(raws[0]):])*counts[a]
C=raws[1][len(raws[0]):];assert walk(C)[:2]==(1j,3)
# Whole-word cones, from literal zero-C endpoints and one standalone C.
cones={h:[rotation(G[a][0],h)for a in(0,4,7)]for h in range(4)}
assert all(z.imag>=0 for h in(0,3)for z in cones[h]) and rotation(1j,0).imag==1
assert all(z.imag<=0 for h in(1,2)for z in cones[h]) and rotation(1j,2).imag==-1
assert all(z.real>=0 and z.imag<=0 for z in cones[1])
assert all(z.real<=0 for z in cones[3])
oldages={(a,complex(x,y)):r for a,x,y,r in json.loads((B/'04_counted_input_age_rules_complete.json').read_text())}
assert set(oldages)=={(a,z)for a in ids for z in G[a][3]} and min(oldages.values())==2
assert {(a,xy(z))for (a,z),n in oldages.items()if n==2}=={(4,(0,3)),(5,(0,3))}
gp=-1j;gh=1;needgoal={gp+rotation(z,gh):b for z,b in G[7][2].items()};eg=gp+rotation(G[7][0],gh);hg=(gh+G[7][1])%4
# Exact target creation score from all literal outputs and potential table.
O=sorted(G[7][4],key=xy)
target=max(2*H(eg)+A[hg],*(2*H(gp+rotation(o,gh))+w[f'w_7_{i}_{gh}']for i,o in enumerate(O)));assert target==28
rows=[];cases=[]
for p in ids:
 c=counts[p];h=(-G[p][1])%4;start=-rotation(G[p][0],h);assert start+rotation(G[p][0],h)==0 and h==c
 if c==2:
  val=2*H(start)+A[h];assert val==target;rows.append({'p':p,'pose':[*xy(start),h],'core':val});continue
 outs={start+rotation(o,h):o for o in G[p][4]}
 shadows=set(outs)&{1-1j,-3j};assert shadows;q=(-3j if p in(4,7) else 1-1j);assert q in shadows;assert needgoal[q] is False and q not in K
 for s in(4,5):
  assert q not in G[s][3]|G[s][4] and G[s][2].get(q,True) is True
  # Every eligible possible first retirement, including positive-C consumer tails.
  for a in ids:
   for z in G[a][3]:
    for n in range(c+counts[s],c+4):
     if n<oldages[a,z] or counts[a]>c+3-n:continue
     ch=(h-n)%4;pos=q-rotation(z,ch);end=pos+rotation(G[base[a]][0],ch);remain=c+3-n
     if ch==1:
      assert remain==0 and counts[a]==0
      assert end.real>gp.real or end.imag<gp.imag
      why='final east cone cannot undo endpoint overshoot'
     elif ch==2:
      assert remain==1 and end.imag-1<gp.imag
      why='remaining south-to-east one-C cone strictly lowers y'
     elif ch==3:
      assert c==1 and n==2 and base[a]==4 and z==3j and pos==4-1j
      se,sh=G[s][:2]
      if s==4:
       assert sh==0 and n-c-counts[s]==1 and pos.imag<se.imag+1
       why='preceding north-to-west one-C cone cannot reach low y'
      else:
       assert sh==3 and n-c-counts[s]==0 and pos.real>se.real
       why='preceding west zero-C cone cannot increase x'
     else:raise AssertionError((p,s,a,z,n))
     cases.append({'predecessor':p,'source':s,'consumer':a,'input':list(xy(z)),'age':n,'consumer_pose':[*xy(pos),ch],'remaining_C':remain,'base_endpoint':list(xy(end)),'shadow':list(xy(q)),'reason':why})
 rows.append({'p':p,'pose':[*xy(start),h],'shadow':list(xy(q)),'slot':list(xy(outs[q]))})
key=lambda r:(r['predecessor'],r['source'],r['consumer'],tuple(r['input']),r['age'])
author={key(r):r for r in J['retirement_cases']};own={key(r):r for r in cases};assert author.keys()==own.keys() and len(own)==162
for k,r in own.items():
 for field in ('consumer_pose','remaining_C','base_endpoint','shadow'):assert r[field]==author[k][field],(k,field)
for s in(4,5):
 for z in G[s][3]:assert z not in K and 28+2*H(z)==34>target
out={'status':'PASS independent literal predecessor, full retirement and unbounded cone reconstruction','manifest_sha256':hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),'predecessors':rows,'retirement_cases':cases,'target_score':target,'source_first_activations':[34,34],'scope':'Exact q-age3 excluded only at outer unfunded U1 with full strict record and I>=28. Depends on signed LN same-cohort/source reduction, HB identity retirement and JO produced minima. Not a global U age4 rule, not U1 closure, not capture.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='retirement_cases'})
