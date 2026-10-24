#!/usr/bin/env python3
"""Separate literal enumeration of the position-only inflation owner guards.
Imports none of the causal worker's simulation or ownership implementation.
"""
from itertools import product
from pathlib import Path
import json
D=[(0,1),(1,0),(0,-1),(-1,0)]
def rotation(q,h):
 x,y=q
 if h%4==0:return x,y
 if h%4==1:return y,-x
 if h%4==2:return -x,-y
 return -y,x

def times(a,p):return a[0]*p[0]-a[1]*p[1],a[1]*p[0]+a[0]*p[1]
def path(word,h):
 p=(0,0);last={};first={};reads=[]
 for letter in word:
  if p in last and last[p]==letter:return None
  first.setdefault(p,letter);last[p]=letter;reads.append(p)
  h=(h+(1 if letter=='R'else-1))%4;v=D[h];p=p[0]+v[0],p[1]+v[1]
 return p,first,reads

def check(k,a,theta):
 records=[]
 for cs in product('RL',repeat=k):
  w=''.join(cs)
  for Hf in range(4):
   trace=path(w,Hf)
   if trace is None:continue
   endpoint,first,reads=trace
   for Hc in range(4):
    if Hf%2!=((k%2)*Hc+theta)%2:continue
    for c in 'RL':
     if endpoint==times(a,D[(Hc+(1 if c=='R'else-1))%4]):
      records.append((Hc,Hf,c,w,first,reads))
 out=[];norm=a[0]*a[0]+a[1]*a[1]
 for Hc,Hf,c,w,first,reads in records:
  if Hc or c!='R':continue
  witnesses=[]
  for z,letter in first.items():
   if letter!='L':continue
   owners=set()
   for hc,hf,cc,ww,ff,rr in records:
    for p in rr:
     dx,dy=z[0]-p[0],z[1]-p[1];nx=dx*a[0]+dy*a[1];ny=dy*a[0]-dx*a[1]
     if nx%norm or ny%norm:continue
     q=nx//norm,ny//norm
     if (sum(q)+hc)%2==0:owners.add(q)
   witnesses.append(dict(cell=list(z),owners=[list(q)for q in sorted(owners)],private=owners=={(0,0)},forward=all(q[1]>=0 for q in owners)))
  out.append(dict(word=w,fine_heading=Hf,witnesses=witnesses,protected=any(z['forward']for z in witnesses)))
 return dict(k=k,scale=list(a),theta=theta,records=len(records),target_images=out,all_protected=bool(out)and all(z['protected']for z in out))

def canonical(x):
 x=dict(x);imgs=[]
 for z in x['target_images']:
  z=dict(z);z['witnesses']=sorted(z['witnesses'],key=lambda q:q['cell']);imgs.append(z)
 x['target_images']=sorted(imgs,key=lambda q:(q['word'],q['fine_heading']))
 return x
if __name__=='__main__':
 root=Path(__file__).resolve().parents[1];reported=json.load(open(root/'causal_reduction/morphic_candidates/position_only_ownership_2_5.json'))
 checked=[]
 for row in reported:
  actual=check(row['k'],tuple(row['scale']),row['theta']);assert canonical(actual)==canonical(row)
  checked.append(dict(k=row['k'],scale=row['scale'],theta=row['theta'],records=actual['records'],images=len(actual['target_images']),all_protected=actual['all_protected']))
 out=dict(status='PASS exact independent ownership replay; complete prefix exhaustion is a separate dependency',cases=checked,total_inventory_records=sum(z['records']for z in checked),total_target_images=sum(z['images']for z in checked))
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
