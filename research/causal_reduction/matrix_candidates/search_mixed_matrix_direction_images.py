"""First genuinely coordinate-mixing expansive matrix synthesis control.
Finite-prefix survivors require the separate all-time matrix verifier.
"""
import itertools,json,hashlib,time,pathlib
D=((0,1),(1,0),(0,-1),(-1,0));K=9;A=((3,2),(2,5));CAP=10000

def replay(ds,h,cap=CAP):
 x=y=0;last={};fuel=[]
 for t,d in enumerate(itertools.islice(ds,cap)):
  c=(d-h)%4
  if c not in (1,3):return dict(status='AXIS',read=t)
  if (x,y) in last and last[x,y][0]==c:
   return dict(status='CONFLICT',read=t,previous=last[x,y][1],cell=[x,y],turn=c)
  if (x,y) not in last and c==3:fuel.append([x,y])
  last[x,y]=(c,t);h=d;x+=D[d][0];y+=D[d][1]
 return dict(status='PREFIX SURVIVOR',reads=t+1,fuel=fuel,pose=[x,y,h])

def inventory(z):
 tx=A[0][0]*D[z][0]+A[0][1]*D[z][1];ty=A[1][0]*D[z][0]+A[1][1]*D[z][1]
 raw=[];out=[]
 for bits in itertools.product((0,1),repeat=K):
  w=tuple(((z%2 if i%2==0 else 1-z%2)+2*b) for i,b in enumerate(bits))
  if sum(D[d][0] for d in w)!=tx or sum(D[d][1] for d in w)!=ty:continue
  raw.append(w);hs=[h for h in range(4) if h%2!=z%2 and replay(w,h)['status']=='PREFIX SURVIVOR']
  if hs:out.append((w,hs))
 return raw,out

def main():
 st=time.monotonic();inv=[inventory(z) for z in range(4)];dom=[[p[0] for p in x[1]] for x in inv]
 records=[];survivors=[];controllers=0;hist={}
 for ix in itertools.product(*(range(len(v)) for v in dom)):
  s=[dom[z][ix[z]] for z in range(4)];controllers+=1
  for root in range(4):
   period=1 if s[root][0]==root else 2 if s[s[root][0]][0]==root else None
   if period is None:continue
   depth=period
   while K**depth<CAP:depth+=period
   def letters(z,l):
    if l==0:yield z
    else:
     for d in s[z]:yield from letters(d,l-1)
   for h in range(4):
    if h%2==root%2:continue
    r=replay(letters(root,depth),h);r.update(indices=ix,root=root,heading=h,period=period)
    hist[r['status']]=hist.get(r['status'],0)+1
    if r['status']=='PREFIX SURVIVOR':r['images']=[''.join(map(str,w)) for w in s];survivors.append(r)
    else:records.append(r)
 p=pathlib.Path(__file__);raw=json.dumps(records,sort_keys=True,separators=(',',':')).encode()+b'\n';p.with_suffix('.records.json').write_bytes(raw)
 out=dict(k=K,matrix=A,raw_domains=[len(x[0]) for x in inv],domains=[len(x) for x in dom],inventory=dom,controllers=controllers,horizon=CAP,counts=hist,latest_conflict=max([r['read'] for r in records],default=None),survivors=survivors,records_sha256=hashlib.sha256(raw).hexdigest(),seconds=time.monotonic()-st)
 p.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('inventory','survivors')}));print('survivors',len(survivors))
if __name__=='__main__':main()
