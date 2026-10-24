"""Literal W wake and exhaustive unions; imports no research geometry."""
from pathlib import Path
from collections import Counter,defaultdict
import hashlib,json
B=Path('/workspace/shared/langton');p=B/'computability/singleton_first_block_input.json'
assert hashlib.sha256(p.read_bytes()).hexdigest()=='c67ebdaa29c14c814e8aeb7d42273310f116860fe9f8ff1c7279212a9648f142'
W=json.loads(p.read_text())['word'];D='LLLLRLRRRR'
def path(s,p,v):
 out=[]
 for i,c in enumerate(s):
  out.append((p,i,c));x,y=v;v=(y,-x) if c=='R' else (-y,x);p=(p[0]+v[0],p[1]+v[1])
 return out,p,v
r,p,v=path(W,(0,0),(-1,0));assert (p,v)==((-2,-2),(-1,0))
co=Counter((q[0]-q[1],q[0]%2) for q,i,c in r);T={k for k,n in co.items() if n%2};assert len(T)==12
r,p,v=path(D,(0,0),(0,1));assert(p,v)==((1,1),(0,1))
groups=defaultdict(list)
for q,i,c in r:groups[q[0]-q[1]].append((-q[0],i,c))
profiles={k:''.join(c for a,i,c in sorted(s)) for k,s in groups.items()}
assert profiles=={-1:'L',0:'RLRL',1:'RLRL',2:'R'}
assert all(sum(t==a for t,b in T)<=1 for a in {t for t,p in T if not t%2})
r,p,v=path(D*2,(0,-1),(0,1));assert(p,v)==((2,1),(0,1));groups=defaultdict(list)
for q,i,c in r:groups[(q[0]-q[1],q[0]%2)].append((-q[0],i,c,q))
guard={}; witnesses=[]
for k,s in groups.items():
 s=sorted(s);assert all(a[2]!=b[2] for a,b in zip(s,s[1:]));guard[k]=s[0][2]=='L';witnesses.append(s[0][3])
keys=sorted(guard);black=sum(1<<i for i,k in enumerate(keys) if guard[k]);allmask=(1<<len(keys))-1
assert [k for k in keys if guard[k]]==[(0,0),(0,1)]
assert [k for k in keys if not guard[k]]==[(t,p) for t in [1,2,3] for p in [0,1]]
profiles=[]
for sign in [-1,1]:
 for offset in {-sign*t for t,p in T if t%2==0}:
  for parity in [0,1]:
   rail={(sign*t+offset,(p+parity)%2) for t,p in T}
   mask=sum(1<<i for i,k in enumerate(keys) if k in rail)
   if mask&black:profiles.append(mask)
assert len(profiles)==16
unions={0}
for profile in profiles:unions|={x|profile for x in unions}
minimum=min(((u^black)&allmask).bit_count() for u in unions);assert minimum==2
width=[max(q[i] for q in witnesses)-min(q[i] for q in witnesses) for i in [0,1]];assert max(width)<=9
source=json.loads((B/'core_periodicity_new/check_ten_turn_wake_consumer.json').read_text())
assert source['minimum_union_guard_error']==minimum and source['witness_coordinate_widths']==width
assert sorted(map(tuple,source['first_read_witnesses']))==sorted(witnesses)
out={'status':'independently verified','single_period_ordered_profiles':'L / RLRL / RLRL / R, t=-1..2','wake_classes':sorted(T),'helpful_profiles':16,'distinct_unions':len(unions),'minimum_guard_error':minimum,'witness_coordinate_widths':width,'scope':'D^N after r standard blocks and a other updates: N<=m+a+174r+1, conditional on the independently audited complete-history rail decomposition.'}
(B/'audits/check_ten_turn_consumer_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
