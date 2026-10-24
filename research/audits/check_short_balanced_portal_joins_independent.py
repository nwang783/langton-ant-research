from pathlib import Path
from itertools import product
from collections import Counter,defaultdict,deque
import json,hashlib,ast
S=Path(__file__);D=S.parents[1]/'first_departure_multiplicity_2026-10-24'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
files={'shortest_balanced_one_use_portal_joins_are_chiral.md':'2cfd811d','check_shortest_balanced_one_use_portal_joins.py':'b1c599a1','check_shortest_balanced_one_use_portal_joins.json':'5898c499'}
for f,h in files.items():assert sha(D/f).startswith(h)
J=json.loads((D/'check_shortest_balanced_one_use_portal_joins.json').read_text());H='NESW';V=[(0,1),(1,0),(0,-1),(-1,0)]
def outgoing(w,r):return (H.index(w[r])+(1 if r%2==0 else-1))%4
def words(ax):return[''.join(x)for n in range(1,5)for x in product(ax,repeat=n)]
def domain(first,inc,out):
 ax='NS'if first in'NS'else'EW'
 return[w for w in words(ax)if w[0]==first and w.count(inc)==1 and sum(outgoing(w,r)==H.index(out)for r in range(len(w)))==1]
assert domain('S','S','W')==['S'] and domain('E','E','S')==['E']
assert set(domain('E','W','S'))=={'EEW','EEWE'}and set(domain('N','S','E'))=={'NNS','NNSN'}
def match(hs):
 g={};bad=[]
 for p,w in hs.items():
  for d,(x,y) in enumerate(V):
   q=p[0]+x,p[1]+y
   if q not in hs:continue
   sr=[r for r in range(len(w))if outgoing(w,r)==d];tr=[r for r,c in enumerate(hs[q])if H.index(c)==d]
   if len(sr)!=len(tr):bad.append((p,q,d,sr,tr))
   else:g.update({(p,r):(q,s)for r,s in zip(sr,tr)})
 return g,bad
def faces(p,d):
 x,y=p
 # Left/right geometric faces of the actual oriented unit grid edge.
 return [((x-1,y),(x,y)),((x,y),(x,y-1)),((x,y-1),(x-1,y-1)),((x-1,y-1),(x-1,y))][d]
def heights(hs):
 eq={}
 for p,w in hs.items():
  ia=[0,2]if sum(p)%2==0 else[1,3]
  for d in [z for z in range(4)if z not in ia]:eq[p,d]=sum(outgoing(w,r)==d for r in range(len(w)))
  for d in ia:
   v=V[d];q=p[0]-v[0],p[1]-v[1];n=w.count(H[d]);assert (q,d)not in eq or eq[q,d]==n;eq[q,d]=n
 adj=defaultdict(list)
 for(p,d),n in eq.items():
  l,r=faces(p,d);adj[l].append((r,n));adj[r].append((l,-n))
 values={(0,-1):0};todo=[(0,-1)]
 for u in todo:
  for v,k in adj[u]:
   if v in values:assert values[v]==values[u]+k
   else:values[v]=values[u]+k;todo.append(v)
 assert set(values)==set(adj)
 assert all(h<=0 for p,h in values.items()if sum(p)%2)
 return {str(p):h for p,h in sorted(values.items())}
def serial(path):return[[list(p),r]for p,r in path]
results=[];counts=Counter()
for kind,upper,lower,extra in product(['RL','LR'],['EWW','EWWE'],['EWW','EWWE'],[False,True]):
 b=(0,-2)if kind=='RL'else(2,-2);x,y=b
 hs={(1,1):'SN',(0,1):upper,(0,0):'NNSS',(1,0):'EE',b:'SN',(x-1,y):lower,(x-1,y-1):'NNSS',(x,y-1):'EE'}
 if kind=='RL':hs|={(1,-1):'S',(0,-1):'EEWE'if extra else'EEW'}
 else:hs|={(1,-1):'NNSN'if extra else'NNS',(2,-1):'E'}
 au=next(z for z in J['rows']if(z['join'],z['upper_root'],z['lower_root'],z['LEFTfour'])==(kind,upper,lower,extra));assert{ast.literal_eval(p):w for p,w in au['histories'].items()}==hs
 g,bad=match(hs);row=dict(kind=kind,upper=upper,lower=lower,extra_L=extra)
 if bad:
  counts['port']+=1;assert au['result']=='port';row.update(result='port',witnesses=bad)
 elif kind=='LR':
  assert lower=='EWWE'and not extra
  path=[((1,-1),0),((2,-1),0),((2,-2),0),((1,-2),1),((1,-3),3),((2,-3),1),((2,-2),1),((1,-2),2),((1,-1),0)]
  assert all(g[u]==v for u,v in zip(path,path[1:]));assert serial(path)==au['certificate']['actual8_event_cycle'];counts['skipped_rank']+=1;row.update(result='same_physical_event_cycle',path=serial(path))
 else:
  assert not extra and au['result']=='open';counts['open']+=1
  ev={(p,r)for p,w in hs.items()for r in range(len(w))};pr={v:u for u,v in g.items()};assert len(pr)==len(g)
  cs=[];used=set()
  for start in sorted(ev-pr.keys()):
   chain=[start]
   while chain[-1]in g:chain.append(g[chain[-1]])
   assert not used.intersection(chain);used.update(chain);cs.append(chain)
  assert used==ev
  acs=au['certificate']['components'];assert{tuple(c)for c in cs}=={tuple((tuple(p),r)for p,r in c)for c in acs}
  times={ast.literal_eval(e):t for e,t in au['certificate']['injective_mod4_calendar'].items()}
  assert set(times)==ev and len(set(times.values()))==len(ev)
  for e,f in g.items():assert times[f]==times[e]+1
  phase=lambda p:2*(p[0]%2)if sum(p)%2==0 else 3-2*(p[0]%2)
  for p,w in hs.items():
   for r in range(len(w)):
    assert times[p,r]%4==phase(p)
    if r:assert times[p,r]-times[p,r-1]>=4
  intervals=sorted((times[c[0]],times[c[-1]])for c in cs);assert all(a[1]<b[0]for a,b in zip(intervals,intervals[1:]))
  row.update(result='OPEN_local_only',events=len(ev),components=len(cs),heights=heights(hs))
 results.append(row)
assert counts==J['summary']==dict(port=10,skipped_rank=2,open=4)
# Actual b-path geometry of one RL join, not a complete quotient identification.
p=(1,1);inc=2;turns='RLLRRL'
for c in turns:
 inc=(inc+(1 if c=='R'else-1))%4;v=V[inc];p=p[0]+v[0],p[1]+v[1]
assert p==(0,-2)and inc==2
out=dict(status='PASS two specified balanced one-use joins, scoped necessary local cover',files={f:sha(D/f)for f in files},script=sha(S),counts=counts,rows=results,complete_flow_one_domain_derivation='Every1..4 complete WHITE same-axis word independently generated with actual first heading, one selected incoming and one selected outgoing port. RIGHT singleton and LEFT3/4 domains follow without dropped alternatives.',scope='Only the displayed RL/LR two-internal-vertex joins. All physical zero ports, full literal LR8-event cycles, exposed stream heights, and four injective event-disjoint whole-component calendars independently checked. RL carries two odd classes in this stipulated local geometry; no charge for arbitrary longer joins, no actual factor, complete full-drift aliasing or periodic front is supplied.',geometry=dict(b_turns=turns,displacement=[-1,-3],not_a_repeatable_tile=True))
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(sha(S.with_suffix('.json')))
