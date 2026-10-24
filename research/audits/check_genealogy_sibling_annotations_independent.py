"""Independent full literal source-sibling intersections on reconstructed LA edges."""
from pathlib import Path
import sys,json,hashlib
sys.path.insert(0,str(Path(__file__).resolve().parent))
import check_genealogy_saturation_roles_independent as G
from check_dcuv_patch_model_independent import walk,raws,mark
R=G.ROOT;F=R/'core_periodicity_new/genealogy_sibling_clearance_frozen_20261023_0926';M=json.loads((F/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((F/f['file']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((F/'02_genealogy_sibling_clearance.json').read_text());K={z for z,b in walk(mark)[2].items()if b};req={a:walk(raws[a]+mark)[2]for a in G.ids}
E=list(map(tuple,G.J['all_fundamental_edges']));assert set(E)==G.fundamental
records={};strict=[];by=[]
def pairset(rows):return{(complex(*a),complex(*b))for a,b in rows}
for ei,(u,v,n,dy)in enumerate(E):
 a,s,h=G.roles[u];b,r,hh=G.roles[v];key=(u,b,hh)
 if key not in records:
  dh=(hh-h)%4;p=s-G.rotation(G.anchors[b],dh);parts={k:set()for k in ['core','white','other_inputs','untouched']}
  for t in G.geometry[a]['outputs']:
   if t==s:continue
   z=G.rotation(t-p,-dh)
   category='core'if z in K else'white'if z in req[b]and not req[b][z]else'other_inputs'if z in G.geometry[b]['inputs']else'untouched'
   parts[category].add((t,z))
  old=J['transfers'][J['edge_transfer_index'][ei]]
  assert (old['source_role'],old['target_packet'],old['target_heading'])==key
  assert old['source_normalized_target_pose']==[*G.xy(p),dh]
  assert all(pairset(old[k])==q for k,q in parts.items())
  records[key]=parts
 z=records[key]
 if not z['core']and not z['white']:
  strict.append((u,v,n,dy,ei))
  if not z['other_inputs']:by.append((u,v,n,dy,ei))
 old=J['transfers'][J['edge_transfer_index'][ei]]
 assert(old['source_role'],old['target_packet'],old['target_heading'])==key
 assert all(pairset(old[k])==q for k,q in records[key].items())
assert len(records)==4224 and strict==list(map(tuple,J['strict_clearance_free_edges']))and by==list(map(tuple,J['by_target_clearance_free_edges']))
positive={1,5,6,8,9};ps=[e for e in strict if G.roles[e[0]][0]in positive and G.roles[e[1]][0]in positive];pb=[e for e in by if G.roles[e[0]][0]in positive and G.roles[e[1]][0]in positive]
assert ps==list(map(tuple,J['positive_C_strict_free_edges']))and pb==list(map(tuple,J['positive_C_by_target_free_edges']))
def components(edges):
 adj=[set()for _ in G.roles]
 for u,v,*_ in edges:adj[u].add(v)
 reach=[]
 for u in range(len(adj)):
  seen=set();todo=list(adj[u])
  while todo:
   v=todo.pop()
   if v in seen:continue
   seen.add(v);todo.extend(adj[v]-seen)
  reach.append(seen)
 pending=set(range(len(adj)));cs=[]
 while pending:
  u=min(pending);c={v for v in reach[u]if u in reach[v]};pending-=c or{u}
  if c:cs.append(sorted(c))
 return sorted(cs)
pcs=components(pb);assert pcs==J['positive_C_by_target_free_cyclic_SCCs']
assert len(pcs)==1 and set(pcs[0])=={G.index[1,2+0j,h]for h in range(4)}
ce=[e for e in pb if e[0]in pcs[0]and e[1]in pcs[0]];assert len(ce)==4 and all(e[2]==7 and(G.roles[e[1]][2]-G.roles[e[0]][2])%4==1 for e in ce)
assert {G.roles[e[0]][0]for e in pb}=={1,5,8}
acs=components(by);assert list(map(len,acs))==J['summary']['all_by_target_free_cyclic_SCC_sizes']
out=dict(status='PASS independent literal sibling annotations and cyclic components',roles=len(G.roles),fundamental_edges=len(E),transfer_classes=len(records),strict_before_free=len(strict),by_target_free=len(by),positive_C_strict_before_free=len(ps),positive_C_by_target_free=len(pb),positive_C_cyclic_components=pcs,all_by_target_cyclic_component_sizes=list(map(len,acs)),manifest_sha256=hashlib.sha256((F/'manifest.json').read_bytes()).hexdigest(),scope='Necessary identity retirements only. Packet types with zero C cannot be discarded from actual ancestry. Counted retirements may occur on path consumers; no fresh-root or global fuel bound.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
