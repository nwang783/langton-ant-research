"""Independent complete literal producer-role graph and signed transfer cuts."""
from pathlib import Path
import json,hashlib
from collections import deque
from check_dcuv_producer_model_independent import ROOT,geometry,rotation,xy,protected
F=ROOT/'core_periodicity_new/genealogy_saturation_roles_frozen_20261023_0833';M=json.loads((F/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((F/f['file']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((F/'01_graph.json').read_text());ids=(0,1,4,5,6,7,8,9);mp={a:i for i,a in enumerate(ids)};Q=json.loads((ROOT/'audits/dcuv_count5_replay/queries.json').read_text());anchors={0:1j,1:1j,4:1+2j,5:1+2j,6:3j,7:3j,8:3j,9:3j};phi=(0,5,6,3)
cp=ROOT/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';oldp=ROOT/'core_periodicity_new/chronology_dcuv/recurrent8_counted/closure.tsv'
assert hashlib.sha256(cp.read_bytes()).hexdigest()=='f68f23f8189dc750489ed3aabd48741fde629d1263503ac9cff94fb703163f58'
assert hashlib.sha256(oldp.read_bytes()).hexdigest()=='e8ad57fc2f640f31e4ab0493440089418248dc03f8575dbb71b2d85bf4dcc4e4'
C={tuple(map(int,l.split()[:8]))for l in cp.read_text().splitlines()};old={tuple(map(int,l.split()[:8]))for l in oldp.read_text().splitlines()}
roles=[(a,z,h)for a in ids for z in geometry[a]['outputs']for h in range(4)];index={z:i for i,z in enumerate(roles)};assert [[a,list(xy(z)),h]for a,z,h in roles]==J['roles']
raw=set();tight=set();fundamental=set();blocked=set()
for u,(a,z,h)in enumerate(roles):
 for v,(b,o,hh)in enumerate(roles):
  q=anchors[b];age=Q['slots'][f'{b}:{xy(q)}']['certified_minimum_C_age'];rel=(hh-h)%4;p=z-rotation(q,rel)
  if(sum(xy(p))+rel)%2:continue
  transfer=(a,b,*xy(p),rel,*xy(z));counted=(mp[a],mp[b],*xy(p),rel,*xy(z))
  n0=next(n for n in range(age,age+4)if(n+rel)%4==0);dy=int(rotation(o-q,hh).imag)
  assert 3*n0-4*dy+phi[h]-phi[hh]>=0
  forbids=lambda n:transfer in protected or(*counted,min(5,n))in C
  if 3*n0-4*dy+phi[h]-phi[hh]==0:
   raw.add((u,v,n0,dy))
   if forbids(n0):blocked.add((u,v,n0,dy,transfer,(*counted,min(5,n0)),'HB'if transfer in protected else'counted'))
   else:tight.add((u,v,n0,dy))
  possible=[n for n in range(age,age+8)if(n+rel)%4==0 and not forbids(n)]
  if possible:fundamental.add((u,v,min(possible),dy))
assert raw==set(map(tuple,J['raw_tight_edges'])) and tight==set(map(tuple,J['tight_edges_after_signed_exclusions'])) and fundamental==set(map(tuple,J['all_fundamental_edges']))
assert blocked=={(e['source_role'],e['target_role'],e['C_gap'],e['dy'],tuple(e['transfer_original']),tuple(e['counted_tuple']),e['reason'])for e in J['blocked_tight_edges']}
# Kahn deletion and reverse longest path, independent of the author's DFS SCC.
adj=[set()for _ in roles];indegree=[0]*len(roles)
for u,v,n,dy in tight:adj[u].add(v)
for neighbors in adj:
 for v in neighbors:indegree[v]+=1
ready=deque(i for i,d in enumerate(indegree)if d==0);order=[]
while ready:
 u=ready.popleft();order.append(u)
 for v in adj[u]:
  indegree[v]-=1
  if not indegree[v]:ready.append(v)
assert len(order)==len(roles)
longest=[0]*len(roles)
for u in reversed(order):longest[u]=max([0]+[1+longest[v]for v in adj[u]])
assert longest==J['topological_rank'] and max(longest)==2
cuts=json.loads((F/'03_eight_cycle_cut_queries.json').read_text());expected=set()
for a in(6,7,8,9):
 for z in(0j,2+0j):
  assert z in geometry[a]['outputs'];p=z-rotation(1j,1);row=(mp[a],mp[1],*xy(p),1,*xy(z),3);assert row in C and row in old;expected.add(row)
assert expected=={tuple(r['counted_tuple'])for r in cuts['rows']}
# A role's physical color is encoded by its literal output coordinate, not an
# unknown producer flag. Every actual protected genealogy edge maps to a listed
# fundamental edge plus a nonnegative multiple of four in C gap.
result={'status':'PASS complete role graph; no KY zero-margin directed cycle','roles':len(roles),'raw_tight_edges':len(raw),'remaining_tight_edges':len(tight),'blocked_tight_edges':len(blocked),'fundamental_edges':len(fundamental),'longest_tight_path':max(longest),'eight_old_and_new_cycle_cuts_verified':len(expected),'manifest_sha256':hashlib.sha256((F/'manifest.json').read_bytes()).hexdigest(),'scope':'Produced-parent ancestry saturation only. Fundamental edges overapproximate arbitrarily long intervening actual packet words; no physical realization, ancestry-length bound or capture is inferred.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
