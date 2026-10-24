from pathlib import Path
from collections import deque,Counter
import json,hashlib
from check_dcuv_patch_model_independent import walk,rotation,xy
R=Path(__file__).resolve().parents[1];B=R/'word_stabilization/foreign_return_interfaces_frozen_20261023_2110'
m=json.loads((B/'manifest.json').read_text())
for f,h in m['files'].items():assert hashlib.sha256((B/f).read_bytes()).hexdigest()==h
for f,h in m['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
ref=json.loads((B/'check_foreign_return_interfaces.json').read_text());q=json.loads((R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json').read_text());E=q['quotient_edges'];W=[r['word']for r in q['macro_words']];M='LLLLRLRRRRL';K={z for z,b in walk(M)[2].items()if b}
foreign=[i for i,e in enumerate(E)if e[1]>=4];ordinary=[i for i,e in enumerate(E)if e[1]<4];P={E[i][2]for i in foreign};Q={E[i][0]for i in foreign}
assert len(P)==35 and len(Q)==53 and not P&Q and Counter(E[i][1]for i in foreign)=={4:37,5:76,6:27}
records=set();pairs=set();distances={}
for p in P:
 dist={p:0};todo=deque([p])
 while todo:
  a=todo.popleft()
  for i in ordinary:
   aa,t,b=E[i]
   if aa==a and b not in dist:dist[b]=dist[a]+1;todo.append(b)
 for b in Q&dist.keys():pairs.add((p,b));distances[p,b]=dist[b]
 for i in foreign:
  if E[i][0]in dist:records.add((p,i))
arcs={(p,E[i][1],E[i][2])for p,i in records}
assert(len(pairs),len(records),len(arcs),max(distances.values()))==(1721,4667,1578,8)
assert E==ref['original_edges'] and ordinary==ref['dcuv_edge_ids'] and foreign==ref['foreign_edge_ids']
assert records==set(map(tuple,ref['return_records_from_postport_and_actual_foreign_edge_id']))and arcs==set(map(tuple,ref['deduplicated_return_edges']))
assert {(p,b)for p,b,ww in ref['dcuv_reachability_witnesses']}==pairs
for p,b,ww in ref['dcuv_reachability_witnesses']:
 a=p
 for i in ww:assert i in ordinary and E[i][0]==a;a=E[i][2]
 assert a==b and len(ww)==distances[p,b]
for pp in ref['postforeign_ports']:
 p=pp['state'];out=[i for i,e in enumerate(E)if e[0]==p]
 assert out==pp['all_next_edge_ids'] and {i for i in foreign if E[i][2]==p}==set(pp['actual_foreign_in_edge_ids'])
 bits={'L'if E[i][1]==0 else'R'for i in out};assert bits=={pp['required_actual_twelfth_marker_turn']}
 assert all((W[E[i][1]]+M)[11]in bits for i in out)
# Own literal first/last inventory, including complete marker-only obligations.
def trace(w):
 p=0j;d=1j;first={};last={}
 for i,a in enumerate(w):
  if p in last and last[p][0]==a:return None
  first.setdefault(p,(a,i));last[p]=(a,i);d*=(-1j if a=='R'else 1j);p+=d
 return p,(1j,1,-1j,-1).index(d),first,last
outputs={};geometry=[]
for i,w in enumerate(W):
 ep,h,fr,la=trace(w);_,_,fc,lc=trace(w+M);seed={p for p,(a,t)in fc.items()if a=='L'};after=set(seed)
 for p,(a,t)in la.items():
  if a=='R':after.add(p)
  else:after.discard(p)
 core={ep+rotation(p,h)for p in K};assert core<=after;I=seed-K;O=after-core;outputs[i]=O
 assert all(p in la and la[p][0]=='R'for p in O)
 g=ref['literal_geometry'][i]
 assert sorted(map(xy,I))==list(map(tuple,g['inputs']))and sorted(map(xy,O))==list(map(tuple,g['outputs']))
 assert sorted(map(xy,I&O))==list(map(tuple,g['recycled']))
 assert [[*xy(p),a=='L',t]for p,(a,t)in sorted(fc.items(),key=lambda z:xy(z[0]))]==g['requirements']
 only=I-fr.keys();assert sorted(map(xy,only))==list(map(tuple,g['marker_only_inputs']))
 geometry.append((len(I),len(O),sorted((xy(p),fc[p][1])for p in only)))
assert geometry[4:]==[(14,16,[((-3,-2),57)]),(15,21,[((-3,-4),65)]),(18,24,[((-2,-5),75)])]
paircontrols={}
for i in (4,5,6):
 for j in (4,5,6):
  z=trace(W[i]+W[j]+M)
  assert bool(z)==ref['all_nine_fixed_foreign_pairs'][f'{i}_{j}']['feasible']
  if z:
   seed={p for p,(a,t)in z[2].items()if a=='L'};paircontrols[f'{i}_{j}']=len(seed)
   assert sorted(map(xy,seed))==list(map(tuple,ref['all_nine_fixed_foreign_pairs'][f'{i}_{j}']['seed']))
assert paircontrols=={'5_4':34,'6_4':37}
uc=[]
for i in (4,5,6):
 full=W[3]+W[i]+M;ep,h,_,_=trace(W[3]);ctx={ep+rotation(z,h)for z in trace(W[i]+M)[2]};assert not outputs[3]&ctx
 z=trace(full);seed={p for p,(a,t)in z[2].items()if a=='L'};black=set(seed);p=0j;d=1j
 for a in full:
  assert(p in black)==(a=='L');black.symmetric_difference_update({p});d*=(-1j if a=='R'else 1j);p+=d
 assert outputs[3]<=black
 assert sorted(map(xy,seed))==list(map(tuple,ref['immediate_U_foreign_controls'][str(i)]['seed']))
 uc.append(len(seed))
assert uc==[24,25,28]
out=dict(status='PASS conditional35-port graph-return interface and complete literal foreign ledgers',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),counts={'ports':35,'preports':53,'reachability_pairs':1721,'records':4667,'arcs':1578},foreign_geometry=geometry[4:],physical_pairs_outside_graph=paircontrols,U_foreign_seed_masses=uc,analytic='Full original DCUV connector graph, not one shortest witness, defines each return language. Marker-only residual inputs retire in the ordered core exchange but are not falsely called owned raw reads. Untouched U identities survive the three supplied controls, while clean-eight unconsumability authority cannot be carried across arbitrary foreign readers.',scope='Conditional on inherited214-state quotient only. Actual QF/BF controls prove it is not a presentation of every physical seven-word factor. No graph-only finiteness, global coverage, permanent-star extension or return-budget theorem.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(out['counts'])
