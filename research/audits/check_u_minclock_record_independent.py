"""Independent four-heading full-record birth graph reconstruction.
Uses literal raw words/marker, exact integer endpoint counts, and independently
rebuilds every reachable selected-birth state and edge, not just completions.
"""
from pathlib import Path
from itertools import combinations
from collections import deque
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
B=ROOT/'core_periodicity_new/u1_minclock_cohort_frozen_20261023_1118';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f.get('frozen',f.get('file'))).read_bytes()).hexdigest()==f['sha256']
J=json.loads(next(B.glob('02*json')).read_text())
for p,h in J['dependencies'].items():assert hashlib.sha256((ROOT/'core_periodicity_new'/p).read_bytes()).hexdigest()==h
model=json.loads((ROOT/'core_periodicity_new/chronology_dcuv/delayed_height_probe/u1_residue_cegar/root_out.json').read_text());potential=Path(model['potential_file']);assert hashlib.sha256(potential.read_bytes()).hexdigest()==model['potential_sha256']
w=json.loads(potential.read_text())['values'];ids=(0,1,4,5,6,7,8,9);cc=dict(zip(ids,(0,1,0,1,2,0,1,2)));core={z for z,b in walk(mark)[2].items()if b};G={}
for a in ids:
 e,h,_,flip=walk(raws[a]);req=walk(raws[a]+mark)[2];black={z for z,b in req.items()if b}
 G[a]=(sorted((black^flip)-{e+rotation(z,h)for z in core},key=xy),set(req),e,h)
L=lambda z:int(z.real+z.imag);H=lambda z:int(z.imag-z.real)
A=[L(rotation(-1+1j,h))+w[f'c{h}']for h in range(4)];assert A==model['core_offsets']
T={}
for a in ids:
 O,_,e,eh=G[a]
 for h in range(4):T[a,h]=max(2*L(rotation(e,h))+A[(h+eh)%4],*(2*L(rotation(o,h))+w[f'w_{a}_{i}_{h}']for i,o in enumerate(O)))
assert [[a,h,T[a,h]]for a in ids for h in range(4)]==model['created_peaks']
cells=(-1+1j,-1+2j,-1+4j,2j,3j);full=frozenset(range(5));summaries=[]
for strict,key in ((False,'phases'),(True,'U1_strict_record_phases')):
 for author in J[key]:
  h=author['heading'];placements=[];sets=[]
  for a in ids:
   O,ctx,e,eh=G[a]
   for p in sorted({z-rotation(o,h)for z in cells for o in O},key=xy):
    if (sum(xy(p))+h)%2:continue
    output={p+rotation(o,h)for o in O};context={p+rotation(z,h)for z in ctx}
    outids=frozenset(i for i,z in enumerate(cells)if z in output);hits=frozenset(i for i,z in enumerate(cells)if z in context)
    entry=2*H(p)+A[(h+1)%4];created=2*H(p)+T[a,(h+1)%4]
    placements.append(dict(packet=a,head=[*xy(p),h],exit=[*xy(p+rotation(e,h)),(h+eh)%4],output_mask=sum(1<<i for i in outids),context_mask=sum(1<<i for i in hits),C=cc[a],U1_entry_core=entry,U1_created_peak=created,U1_strict_record_permitted=max(entry,created)<30));sets.append((outids,hits))
  assert placements==author['placements'];pairs=set()
  for i,p in enumerate(placements):
   for j,t in enumerate(placements):
    dz=rotation(complex(*t['head'][:2])-complex(*p['exit'][:2]),-h);dx,dy=xy(dz)
    if dx<0 or dy<0:continue
    if any(d+v==dx and dy-d-3*v>=0 and (dy-d-3*v)%4==0 for d in range(dx+1)for v in range(min(dx,dy//3)+1)):pairs.add((i,j))
  assert sorted(pairs)==list(map(tuple,author['exact_zero_C_endpoint_pairs']))
  counts=[0,0];completed=[]
  for case in author['birth_subset_DAGs']:
   old=case['older_input_mask'];initial=frozenset(i for i in full if old>>i&1);start=(initial,-1,0);states={start};todo=deque([start]);edges=set()
   while todo:
    alive,last,depth=todo.popleft()
    if alive==full:continue
    for j,p in enumerate(placements):
     if strict and not p['U1_strict_record_permitted']:continue
     output,context=sets[j]
     if alive&context or last>=0 and(last,j)not in pairs:continue
     fresh=sorted(output-alive)
     for n in range(1,len(fresh)+1):
      for chosen in combinations(fresh,n):
       nxt=alive|set(chosen)
       if nxt!=full and p['C']:continue
       child=(frozenset(nxt),j,depth+1);edges.add(((alive,last,depth),child,j,frozenset(chosen)))
       if child not in states:states.add(child);todo.append(child)
   def convert(i):
    b,j,d=case['states'][i];return(frozenset(k for k in full if b>>k&1),j,d)
   assert states=={convert(i)for i in range(len(case['states']))}
   expected={(convert(si),convert(ti),p,frozenset(i for i in full if sub>>i&1))for si,ti,p,sub in case['arcs']};assert edges==expected
   for alive,last,depth in states:
    if alive==full:completed.append((old,last,depth))
   counts[0]+=len(states);counts[1]+=len(edges)
  expected={(r['older_input_mask'],placements.index(r['last_producer']),r['birth_packets'])for r in author['completed_abstract_states']};assert set(completed)==expected
  if strict:assert all(d==1 for old,last,d in completed)
  summaries.append(dict(heading=h,strict_record=strict,placements=len(placements),states=counts[0],arcs=counts[1],completed=len(completed),max_relevant_birth_packets=max((d for old,last,d in completed),default=0)))
out=dict(status='PASS independent full four-phase birth-graph and entry-plus-created-record reconstruction',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),summaries=summaries,scope='Produced q is a youngest-clock U input. Necessary sixteen one-source templates under strict U1, not attainment, q-not-youngest coverage, record descent or closure.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
