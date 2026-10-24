from pathlib import Path
import json
from check_return_permanent_output_debt import DXY,rot,future
P=Path(__file__).parent;G={(0,-1),(1,1),(1,3),(2,2)};B={q:-i-1 for i,q in enumerate(sorted(G))};p=(0,0);h=1;Q=[];A='';U='';first={};B182=None
for t in range(286):
 if t==182:B182=dict(B);p182=p;h182=h
 if t>=182:Q.append(p)
 if t<182 and p not in first:first[p]=dict(cell=p,black=p in B,first=t)
 old=B.pop(p,None)
 if old is None:B[p]=t;h=(h+1)%4
 else:h=(h-1)%4
 if t<182:A+='R' if old is None else 'L'
 else:U+='R' if old is None else 'L'
 p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
w,dr,tail,tests=future(B182,p182,h182);assert w==U and dr==(2,2)
C={q for q,i in B182.items() if i in tail};W=[]
for i,q in enumerate(Q):
 if U[i]=='L':continue
 times=[]
 for j,r in enumerate(Q):
  dx,dy=q[0]-r[0],q[1]-r[1]
  if dx==dy and dx%2==0 and dx>=0 and 104*(dx//2)+j>i:times.append(104*(dx//2)+j)
 if not times:W.append(dict(cell=q,phase=i))
assert len(W)==12
onfull=lambda q:any(q[0]-z['cell'][0]==q[1]-z['cell'][1] and (q[0]-z['cell'][0])%2==0 for z in W)
def onpast(q):
 return q in C or any(q[0]-z['cell'][0]==q[1]-z['cell'][1] and (q[0]-z['cell'][0])%2==0 and q[0]<z['cell'][0] for z in W)
g0=(0,-1);bulk=[]
for r in range(4):
 for z in W:
  off=rot(g0,r);o=(z['cell'][0]-off[0],z['cell'][1]-off[1])
  failures=[]
  for f in sorted(first.values(),key=lambda z:z['first']):
   d=rot(f['cell'],r);q=(o[0]+d[0],o[1]+d[1])
   if onfull(q)!=f['black']:failures.append(dict(first_read=f['first'],cell=q,wanted_black=f['black'],actual_black=onfull(q)))
  blackhits=sum(onfull((o[0]+rot(g,r)[0],o[1]+rot(g,r)[1])) for g in G)
  bulk.append(dict(rotation=r,origin=o,blackhits=blackhits,first_failure=failures[0],failures=len(failures)))
mins=min(sum(q) for q in list(C)+Q+[z['cell'] for z in W]);maxoffset=max(sum(rot((f['cell'][0]-g0[0],f['cell'][1]-g0[1]),r)) for f in first.values() for r in range(4))
L=1
while max(sum(z['cell']) for z in W)-4*L+maxoffset>=mins:L+=1
assert L==6 and mins==6 and maxoffset==13
assert len(C)==13 and len(first)==58
launch_permanent=set(B182)-C;assert len(launch_permanent)==23
assert max(map(sum,launch_permanent))==max(sum(z['cell'])-4 for z in W)==11
changes=set();cases=[];matches=[]
for phase in range(104):
 on=lambda q:onpast(q)^(q in changes)
 anchors=set(C)|set(Q[:phase])|{(z['cell'][0]+2*j,z['cell'][1]+2*j) for z in W for j in range(-L+1,0)}
 for r in range(4):
  shift=rot(g0,r)
  for z in sorted(anchors):
   if not on(z):continue
   o=(z[0]-shift[0],z[1]-shift[1]);fail=None
   for f in sorted(first.values(),key=lambda z:z['first']):
    d=rot(f['cell'],r);q=(o[0]+d[0],o[1]+d[1])
    if on(q)!=f['black']:fail=dict(first_read=f['first'],cell=q,wanted_black=f['black'],actual_black=on(q));break
   row=dict(phase=phase,rotation=r,origin=o,first_failure=fail)
   cases.append(row)
   if fail is None:matches.append(row)
 q=Q[phase];assert on(q)==(U[phase]=='L')
 if q in changes:changes.remove(q)
 else:changes.add(q)
assert len(cases)==33568 and not matches
assert max(z['first_failure']['first_read'] for z in cases+bulk)<=32
# Exact one-period finite closure, sufficient for every completed standard period.
Fset=C^changes
assert Fset=={(x+2,y+2) for x,y in C}|{z['cell'] for z in W}
assert not ({(x+2,y+2) for x,y in C}&{z['cell'] for z in W})
# All copies of permanent periodic outputs are physically distinct.
for i,z in enumerate(W):
 for j,v in enumerate(W):
  a,b=z['cell'];c,d=v['cell']
  assert not (a-c==b-d and (a-c)%2==0 and (i!=j or a!=c))
# Every launch-permanent bit misses the entire standard future.
for q in launch_permanent:
 for r in Q:
  dx,dy=q[0]-r[0],q[1]-r[1]
  assert not(dx==dy and dx%2==0 and dx>=0)
# Finite complete fields, not cropped comparisons, illustrate the exact transfer.
controls=[]
for K in (0,1,7,31):
 BB=dict(B182);pp=p182;hh=h182
 for t in range(104*K+104):
  if t>=104*K:
   phi=t-104*K;fringe=set(C)
   for q in Q[:phi]:
    if q in fringe:fringe.remove(q)
    else:fringe.add(q)
   predicted=launch_permanent|{(z['cell'][0]+2*j,z['cell'][1]+2*j) for z in W for j in range(K)}|{(x+2*K,y+2*K)for x,y in fringe}
   assert set(BB)==predicted
  old=BB.pop(pp,None)
  if old is None:BB[pp]=182+t;hh=(hh+1)%4
  else:hh=(hh-1)%4
  assert (old is None)==(U[t%104]=='R')
  pp=(pp[0]+DXY[hh][0],pp[1]+DXY[hh][1])
 controls.append(dict(K=K,checked_phases=104,full_terminal_mass=len(BB),terminal_pose=[pp,hh]))
out=dict(status='AUTHOR exact written-wake launch obstruction; independent audit requested',G=sorted(G),A=A,U=U,Q=Q,source182_black=sorted(B182),source182_pose=[p182,h182],source_all_future_ray_tests=tests,W=W,C=sorted(C),launch_permanent=sorted(launch_permanent),first=list(first.values()),bulk=bulk,cutoff_L=L,cutoff_inequality=dict(max_W_sum=max(sum(z['cell']) for z in W),max_constraint_offset=maxoffset,cutoff_upper=max(sum(z['cell']) for z in W)-4*L+maxoffset,minimum_fringe_sum=mins),finite_cases=cases,matches=matches,maximum_first_discrepancy=32,whole_field_transfer_boundary=11,controls=controls,scope='No quarter-rotated G launch prefix33 on the exact settled semi-infinite standard field at any phase/pose. Actual finite G history inherits this outside the fixed initial cap x+y<=11. Other wakes, overlapping archives, modified histories and port-writing turns are not covered.')
(P/'WRITTEN_WAKE_PORT_OBSTRUCTION_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['finite_cases','bulk','Q','source182_black','W','C','launch_permanent','first','A','U']},indent=2))
