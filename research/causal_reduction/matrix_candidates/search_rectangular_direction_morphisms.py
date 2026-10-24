#!/usr/bin/env python3
"""Exact bounded-family synthesis for half-turn symmetric rectangular morphisms.
The direction substitution has independent east and north images; unlike a
relative-turn substitution it need not commute with quarter rotations.
No prefix survivor is an all-future or finite-seed certificate.
"""
import itertools,json,argparse,time,hashlib
from pathlib import Path
D=((0,1),(1,0),(0,-1),(-1,0))

def replay(dirs,h0,cap=None):
 x=y=0;h=h0;seen={};fuel=[];n=-1
 for n,d in enumerate(dirs if cap is None else itertools.islice(dirs,cap)):
  turn=(d-h)%4
  if turn not in (1,3):return dict(status='AXIS',time=n)
  c='R' if turn==1 else 'L'
  if (x,y) in seen:
   old,t=seen[x,y]
   if old==c:return dict(status='CONFLICT',time=n,previous=t,cell=[x,y],turn=c,fuel=len(fuel))
  elif c=='L':fuel.append([x,y])
  seen[x,y]=(c,n);x+=D[d][0];y+=D[d][1];h=d
 return dict(status='UNKNOWN',tested=n+1,fuel=len(fuel),fuel_cells=fuel,endpoint=[x,y,h])

def inventory(k,a):
 # Horizontal image: H,V,H,...,H and displacement(a,0).
 nh=(k+1)//2;nv=k//2
 if (nh-a)%2 or nv%2:return []
 nw=(nh-a)//2;ns=nv//2
 if not 0<=nw<=nh:return []
 out=[]
 for wi in itertools.combinations(range(nh),nw):
  W=set(wi)
  for si in itertools.combinations(range(nv),ns):
   S=set(si);ds=tuple((3 if n//2 in W else 1) if n%2==0 else (2 if n//2 in S else 0) for n in range(k))
   contexts=[h for h in [0,2] if replay(ds,h)['status']=='UNKNOWN']
   if contexts:out.append((ds,tuple(contexts)))
 return out

def main(k,a,b,cap,limit):
 st=time.monotonic();E=inventory(k,a);N0=inventory(k,b)
 # Rotation counterclockwise sends E to N: subtract one in compass encoding.
 N=[(tuple((d-1)%4 for d in w),tuple((h-1)%4 for h in hs)) for w,hs in N0]
 print(json.dumps(dict(k=k,A=[[a,0],[0,b]],east_images=len(E),north_images=len(N),candidate_pairs=len(E)*len(N))),flush=True)
 invfile=Path(__file__).with_name(f'rectangular_inventory_k{k}_{a}_{b}.json')
 invfile.write_text(json.dumps(dict(k=k,a=a,b=b,E=E,N=N),indent=2)+'\n')
 if limit==0:return
 counts={};survivors=[];latest=None;records=[];tested=0
 for ie,(u,cu) in enumerate(E):
  for jn,(v,cv) in enumerate(N):
   if limit is not None and tested>=limit:break
   tested+=1;s={1:u,3:tuple((d+2)%4 for d in u),0:v,2:tuple((d+2)%4 for d in v)}
   # Include both axis roots. Half-turn partners have identical turn data.
   for root,contexts in [(1,(0,2)),(0,(1,3))]:
    period=1 if s[root][0]==root else 2
    depth=period
    while k**depth<cap:depth+=period
    def letters(z,l):
     if l==0:yield z
     else:
      for d in s[z]:yield from letters(d,l-1)
    for h in contexts:
     r=replay(letters(root,depth),h,cap);counts[r['status']]=counts.get(r['status'],0)+1
     rec=dict(east=ie,north=jn,root=root,heading=h,period=period,**r)
     if r['status']=='UNKNOWN':survivors.append(rec)
     else:
      records.append([ie,jn,root,h,period,r['time'],r.get('previous'),r.get('cell'),r.get('turn')])
      if latest is None or r['time']>latest['time']:latest=rec
  if limit is not None and tested>=limit:break
 out=dict(k=k,A=[[a,0],[0,b]],east_images=len(E),north_images=len(N),pairs=tested,total_pairs=len(E)*len(N),all_pairs_completed=tested==len(E)*len(N),counts=counts,latest_conflict=latest,survivors=survivors,records_sha256=hashlib.sha256(json.dumps(records,separators=(',',':')).encode()).hexdigest(),seconds=time.monotonic()-st)
 target=Path(__file__).with_name(f'rectangular_k{k}_{a}_{b}.json');target.write_text(json.dumps(out,indent=2)+'\n');target.with_suffix('.records.json').write_text(json.dumps(records,separators=(',',':'))+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='survivors'},indent=2));print('survivors',len(survivors))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--k',type=int,default=17);p.add_argument('--a',type=int,default=3);p.add_argument('--b',type=int,default=5);p.add_argument('--cap',type=int,default=10000);p.add_argument('--limit',type=int);z=p.parse_args();main(z.k,z.a,z.b,z.cap,z.limit)
