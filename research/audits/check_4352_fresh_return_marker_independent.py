"""Exact all-parameter prior READ and seed ownership for one proposed marker.
Reconstructs literal affine positions; imports no author code.
"""
from pathlib import Path
from collections import defaultdict
import hashlib,json
R=Path('/workspace/shared/langton');P=R/'causal_reduction/unit_scale';SELF=Path(__file__).resolve()
p=P/'prepared4352_two_phase_manifest.json';assert hashlib.sha256(p.read_bytes()).hexdigest()=='ffd8a1393f96ad81b6d8515912b00304e5c4527b1a7b949644686e5c05d56715';J=json.loads(p.read_text());V=((0,1),(1,0),(0,-1),(-1,0));families=defaultdict(set)
for s in J['stages']:
 ax,bx=s['start_x_N_constant'];ay,by=s['start_y_N_constant'];assert ax==ay
 pos=(bx,by);h=s['heading'];reads=[]
 for c in s['word']:
  reads.append(pos);h=(h+(1 if c=='R'else-1))%4;pos=tuple(pos[i]+V[h][i]for i in (0,1))
 drift=tuple(pos[i]-(bx,by)[i]for i in (0,1));cnt=tuple(s['count_N_constant'])
 if cnt==(0,1):drift=(0,0)
 else:assert h==s['heading']and drift[0]==drift[1]and drift[0]and ax%drift[0]==0
 for q in reads:families[q[0]-q[1]].add((ax,q[0],q[1],drift[0],*cnt))
def interval(q,f):
 a,x,y,d,ca,cb=f
 if q[0]-q[1]!=x-y:return None
 z=q[0]-x
 if not d:
  if not a:return (1,None)if z==0 else None
  if z%a:return None
  m=z//a;return (m,m)if m>=1 else None
 if z%d:return None
 # k=(z-a*M)/d and 0<=k<=ca*M+cb-1.
 assert a%d==0
 A=-a//d;B=z//d;lo=1;hi=None
 for u,v in ((A,B),(ca-A,cb-1-B)):
  if u==0:
   if v<0:return None
  elif u>0:lo=max(lo,-(v//u))
  else:
   n=v//(-u);hi=n if hi is None else min(hi,n)
 return None if hi is not None and hi<lo else (lo,hi)
def hits(q):return [v for f in families[q[0]-q[1]]if (v:=interval(q,f))is not None]
def fullcover(ranges):
 through=0
 for lo,hi in sorted(ranges,key=lambda x:x[0]):
  if lo>through+1:return False
  if hi is None:return True
  through=max(through,hi)
 return False
q=(117,111);h=0;word=J['stages'][-1]['word'];seen=set();rows=[];early=[]
for i,c in enumerate(word[:90]):
 r=hits(q)
 if c=='R'and q not in seen:
  if i<89:assert fullcover(r);early.append(dict(offset=i,cell=q,cover=r))
  else:assert i==89 and q==(108,105)and h==1 and not r
 rows.append((q,h,c));seen.add(q);h=(h+(1 if c=='R'else-1))%4;q=tuple(q[j]+V[h][j]for j in (0,1))
marker=(108,105);assert rows[89]==(marker,1,'R')and marker not in {r[0]for r in rows[:89]}
for x,y in J['seed_families']:
 assert x[0]==y[0]
 assert interval(marker,(x[0],x[1],y[1],0,0,1))is None
A=json.loads((P/'prepared4352_fresh_return_marker.json').read_text());assert A['marker']==list(marker)and A['offset_after_checkpoint']==89 and A['read_time_M_constant']==[129780,455250]
out=dict(status='PASS independent all-M complete prior READ and original-seed exclusion, with earliest fresh-R property',manifest_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),marker=marker,heading=1,offset=89,time_affine_M=(129780,455250),distinct_prior_families=sum(map(len,families.values())),marker_normal_families=len(families[3]),original_seed_families=394,earlier_first_seen_R_count=len(early),earlier_R_coverage=early,read_prefix=word[:89],scope='Adding this one original black preserves the signed entire unmodified prefix through just before this read, for ALL M>=1. The modified read turns L. No later modified trajectory or capture conclusion.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='earlier_R_coverage'})
