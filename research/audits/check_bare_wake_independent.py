"""Independent literal replay and phase-threshold all-time oracle on T xor E.
Unlike the source, every phase's earlier-write thresholds are checked directly.
"""
from pathlib import Path
from collections import Counter,defaultdict
import hashlib,json,time
B=Path('/workspace/shared/langton');src=B/'core_periodicity_new/periodic_wake_fronts.json';f=B/'computability/singleton_first_block_input.json'
assert hashlib.sha256(f.read_bytes()).hexdigest()=='c67ebdaa29c14c814e8aeb7d42273310f116860fe9f8ff1c7279212a9648f142'
W=json.loads(f.read_text())['word'];cycles={(W+W)[i:i+104] for i in range(104)}
DIR=((0,1),(1,0),(0,-1),(-1,0))
def trace(w,p,h):
 out=[]
 for c in w:
  out.append(p);h=(h+(1 if c=='R' else -1))%4;dx,dy=DIR[h];p=p[0]+dx,p[1]+dy
 return out,p,h
reads,end,h=trace(W,(0,0),3);assert(end,h)==((-2,-2),3)
cnt=Counter((x-y,x%2) for x,y in reads);T={k for k,v in cnt.items() if v%2};assert len(T)==12

def multiple(q,d):
 x,y=q;dx,dy=d
 if dx:
  if x%dx:return None
  k=x//dx
  return k if y==k*dy else None
 if y%dy:return None
 k=y//dy
 return k if x==0 else None

def canonical(q,d):
 k=q[0]//d[0] if d[0] else q[1]//d[1]
 return(q[0]-k*d[0],q[1]-k*d[1]),k

def exact(w,p,h,E):
 qs,end,eh=trace(w,p,h);P=len(w);d=end[0]-p[0],end[1]-p[1]
 if eh!=h or d==(0,0):return False
 er=defaultdict(set)
 for e in E:
  c,k=canonical(e,d);er[c].add(k)
 for i,q in enumerate(qs):
  thresholds=[];cuts={0};c,ki=canonical(q,d)
  for j,r in enumerate(qs):
   shift=multiple((q[0]-r[0],q[1]-r[1]),d)
   if shift is not None and P*shift+j<i:
    assert shift<=0
    thresholds.append(-shift);cuts.add(-shift)
  for ke in er.get(c,()):
   n=ke-ki
   if n>=0:cuts.update((n,n+1))
  dz=d[0]-d[1]
  if dz:
   for z,a in T:
    diff=z-q[0]+q[1]
    if diff%dz==0:
     n=diff//dz
     if n>=0:cuts.update((n,n+1))
  cuts=sorted(cuts)
  for j,a in enumerate(cuts):
   end=cuts[j+1] if j+1<len(cuts) else None
   for n in (a,a+1):
    if end is not None and n>=end:continue
    v=q[0]+n*d[0],q[1]+n*d[1]
    color=((v[0]-v[1],v[0]%2) in T) ^ (v in E) ^ (sum(t<=n for t in thresholds)%2)
    if color!=(w[i]=='L'):return False
 return True

start=time.time();data=json.loads(src.read_text());rows=data['rows']
assert len(rows)==1508
expected={(a,a-t,h) for t in range(-188,189) for a in (0,1) for h in range(4) if(h-t)%2==1}
assert {(r['start_position'][0],r['start_position'][1],r['start_heading']) for r in rows}==expected
moves=0;drifts=Counter();negative=set()
for z,row in enumerate(rows):
 x,y=row['start_position'];h=row['start_heading'];E=set()
 for _ in range(row['capture']):
  q=x,y;color=((x-y,x%2) in T) ^ (q in E)
  if q in E:E.remove(q)
  else:E.add(q)
  h=(h+(-1 if color else 1))%4;dx,dy=DIR[h];x+=dx;y+=dy
 assert [x,y]==row['position'] and h==row['heading'] and len(E)==row['errors']
 w=row['certificate']['word'];assert w in cycles
 qs,end,eh=trace(w,(x,y),h);d=end[0]-x,end[1]-y
 assert list(d)==row['certificate']['drift'] and eh==h
 assert exact(w,(x,y),h,E),(z,row)
 if d not in negative:
  far=(x+10**60*d[0],y+10**60*d[1]);bad=E^{far}
  assert not exact(w,(x,y),h,bad);negative.add(d)
 moves+=row['capture'];drifts[d]+=1
 if z%100==0:print('checked',z+1,'moves',moves,flush=True)
out={'status':'independent complete literal and all-time phase-threshold audit passed','poses':len(rows),'literal_moves':moves,'max_capture':max(r['capture'] for r in rows),'drifts':{str(k):v for k,v in sorted(drifts.items())},'far_negative_controls':len(negative),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'seconds':time.time()-start,'scope':'Exactly the1508 undecorated same-sector bilateral-wake poses; all far poses require the separate715-cell transfer and geometric reduction.'}
(B/'audits/check_bare_wake_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
