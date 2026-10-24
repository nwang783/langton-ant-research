#!/usr/bin/env python3
"""Small opposite-axis-start half-turn direction family. No fuel extrapolation."""
from pathlib import Path
import argparse,hashlib,itertools,json,time
D=((0,1),(1,0),(0,-1),(-1,0))
def replay(ds,h,cap=None):
 x=y=0;last={};fuel=[]
 for t,d in enumerate(ds if cap is None else itertools.islice(ds,cap)):
  turn=(d-h)%4
  assert turn in (1,3)
  if (x,y) in last and last[x,y][0]==turn:
   return dict(status='CONFLICT',time=t,previous=last[x,y][1],cell=[x,y],turn=turn)
  if (x,y) not in last and turn==3:fuel.append([x,y])
  last[x,y]=turn,t;x+=D[d][0];y+=D[d][1];h=d
 return dict(status='UNKNOWN',reads=t+1,first_L=len(fuel),first_L_cells=fuel)
def inventory(k,a):
 # East image V,H,...,H,V, with vertical net0 and horizontal net a.
 nv=(k+1)//2;nh=k//2
 if nv%2 or (nh-a)%2 or not 0<=a<=nh:return [],0
 out=[];raw=0
 for west in itertools.combinations(range(nh),(nh-a)//2):
  for south in itertools.combinations(range(nv),nv//2):
   raw+=1;w=tuple((2 if t//2 in south else 0) if t%2==0 else (3 if t//2 in west else 1) for t in range(k))
   if any(replay(w,h)['status']=='UNKNOWN' for h in [1,3]):out.append(w)
 return out,raw
def main(k,a,b,cap):
 start=time.monotonic();E,re=inventory(k,a);horizontal_b,rn=inventory(k,b)
 N=[tuple((d-1)%4 for d in w) for w in horizontal_b]
 cases=[];survivors=[];latest=None
 for ie,u in enumerate(E):
  for jn,v in enumerate(N):
   im={1:u,0:v,3:tuple((d+2)%4 for d in u),2:tuple((d+2)%4 for d in v)}
   def letters(d,depth):
    if not depth:yield d
    else:
     for q in im[d]:yield from letters(q,depth-1)
   for root in [1,0]:
    f=im[root][0];period=1
    while f!=root:f=im[f][0];period+=1;assert period<=4
    assert period in [2,4]
    depth=period
    while k**depth<cap:depth+=period
    for heading in [(root+3)%4,(root+1)%4]:
     r=replay(letters(root,depth),heading,cap)
     rec=dict(east=ie,north=jn,root=root,heading=heading,period=period,**r)
     cases.append(rec)
     if r['status']=='UNKNOWN':survivors.append(rec)
     elif latest is None or r['time']>latest['time']:latest=rec
 out=dict(status='COMPLETE FINITE FAMILY PREFIX TEST',k=k,A=[[a,0],[0,b]],raw_images=[re,rn],legal_images=[len(E),len(N)],pairs=len(E)*len(N),cases=len(cases),cap=cap,survivors=survivors,latest_conflict=latest,inventory=dict(E=E,N=N),records_sha256=hashlib.sha256(json.dumps(cases,sort_keys=True,separators=(',',':')).encode()).hexdigest(),seconds=time.monotonic()-start)
 path=Path(__file__).with_name(f'axis_swapping_k{k}_{a}_{b}.json');path.write_text(json.dumps(out,indent=2)+'\n');path.with_suffix('.records.json').write_text(json.dumps(cases,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ['inventory','survivors']}));print('survivors',len(survivors))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--k',type=int,default=11);p.add_argument('--a',type=int,default=3);p.add_argument('--b',type=int,default=5);p.add_argument('--cap',type=int,default=10000);z=p.parse_args();main(z.k,z.a,z.b,z.cap)
