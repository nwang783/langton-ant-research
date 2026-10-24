"""Independent partial-controller cube coverage and finite refined-word conflicts."""
from pathlib import Path
from itertools import product
from collections import defaultdict
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];F=ROOT/'causal_reduction/unit_scale';heads=(1j,1,-1j,-1)
def trace(w,h=1j):
 p=0j;last={}
 for c in w:
  if last.get(p)==c:return None
  last[p]=c;h*=(-1j if c=='R'else 1j);p+=h
 return p,h
pal=[['R'],['L']]
for tup in product('LR',repeat=9):
 w=''.join(tup);e=w.count('R')-w.count('L')
 if e in(-1,1)and trace(w)==(complex(e),complex(e)):pal[e==-1].append(w)
assert all(len(p)==7 for p in pal)
def children(state,word):
 h=heads[state//2];out=[]
 for c in word:out.append(2*heads.index(h)+(c=='L'));h*=(-1j if c=='R'else 1j)
 assert h==heads[state//2]*(-1j if state%2==0 else 1j)
 return out

def replay(row):
 ass=row['assignment'];root=row['root'];assert all(w is None or w in pal[i%2]for i,w in enumerate(ass))
 # Every image length is >=1. Eight refinements of a growing root contain
 # >=65 symbols. Unknown images may not be guessed when checking a cube.
 pending=[(root,8)];p=0j;h=1j;last={};t=0
 while pending:
  s,depth=pending.pop()
  if depth:
   assert ass[s]is not None,('certificate depends on an unspecified image',row,t,s)
   pending.extend((a,depth-1)for a in reversed(children(s,ass[s])));continue
  assert heads[s//2]==h
  c='RL'[s%2]
  if last.get(p)==c:
   assert row['kind']=='color'and t==row['read']and list((int(p.real),int(p.imag)))==row['cell']and c==row['turn'];return t
  last[p]=c;h*=(-1j if c=='R'else 1j);p+=h;t+=1
 raise AssertionError('No conflict in the complete depth-eight prefix')
results=[]
for stem in ['search_heading_transport','search_heading_transport_cycles']:
 J=json.loads((F/(stem+'.json')).read_text());rows=json.loads((F/(stem+'.records.json')).read_text());assert all(set(J['domains'][i])==set(pal[i])for i in range(2));groups=defaultdict(list)
 for r in rows:
  replay(r)
  if stem.endswith('cycles'):key=(r['root'],r['assignment'][0],r['assignment'][1])
  else:key=(r['root'],)
  groups[key].append(r)
 totals=0
 for key,rr in groups.items():
  root=key[0];expected=7**6 if len(key)==3 else 4*7**7
  if len(key)==3:assert key[1][0]=='L'and key[2][0]=='R'
  weight=0
  for i,r in enumerate(rr):
   ass=r['assignment'];free=ass.count(None);assert r['unassigned']==free and r['completion_weight']==7**free
   if len(key)==1:assert ass[root][0]=='RL'[root]and len(ass[root])==9
   weight+=7**free
   for other in rr[:i]:assert any(a is not None and b is not None and a!=b for a,b in zip(ass,other['assignment']))
  assert weight==expected;totals+=weight
 expectedkeys={(r,)for r in(0,1)}if not stem.endswith('cycles')else{(r,u,v)for r in(0,1)for u in pal[0]if u[0]=='L'for v in pal[1]if v[0]=='R'}
 assert set(groups)==expectedkeys
 results.append(dict(family=stem,root_cases=len(groups),disjoint_conflict_cubes=len(rows),rooted_controller_completions=totals,latest_first_conflict=max(r['read']for r in rows),records_sha256=hashlib.sha256((F/(stem+'.records.json')).read_bytes()).hexdigest()))
out=dict(status='PASS every growing rooted cycle in the eight independent identity/nine heading-turn architecture',domains=list(map(len,pal)),method='Independent inventories, literal depth-eight refinement, pairwise-disjoint cube proof and exact product-volume coverage',results=results,scope='Arbitrary initial coloring, identity or one of six charge-preserving unit9 images per actual heading/turn state. No general variable-length or hidden-context exclusion.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
