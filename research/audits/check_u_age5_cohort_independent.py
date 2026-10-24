"""Literal geometry plus exhaustive selected-birth histories at one C clock.
No author geometry or producer/checker code is imported. Unobserved packets
are conservatively represented by independently enumerated zero-C counts.
"""
from pathlib import Path
from itertools import combinations
from collections import deque
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
B=ROOT/'core_periodicity_new/u_age_five_cohort_frozen_20261023_1110';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_u_age_five_latest_cohort.json').read_text())
for p,h in J['dependencies'].items():assert hashlib.sha256((ROOT/'core_periodicity_new'/p).read_bytes()).hexdigest()==h
ids=(0,1,4,5,6,7,8,9);cc={0:0,1:1,4:0,5:1,6:2,7:0,8:1,9:2}
K={z for z,b in walk(mark)[2].items()if b};G={};cells=(-1+1j,-1+2j,-1+4j,2j,3j)
for b in ids:
 e,h,_,flip=walk(raws[b]);req=walk(raws[b]+mark)[2];black={z for z,c in req.items()if c}
 G[b]=(set((black^flip)-{e+rotation(z,h)for z in K}),set(req),e,h)
placements=[];sets=[]
for b in ids:
 O,context,e,h=G[b]
 heads={z-rotation(o,1)for z in cells for o in O}
 for p in sorted(heads,key=xy):
  if (sum(xy(p))+1)%2:continue
  out={p+rotation(o,1)for o in O};ctx={p+rotation(z,1)for z in context}
  outids=frozenset(i for i,z in enumerate(cells)if z in out);hits=frozenset(i for i,z in enumerate(cells)if z in ctx)
  placements.append(dict(packet=b,head=[*xy(p),1],exit=[*xy(p+rotation(e,1)),(h+1)%4],output_mask=sum(1<<i for i in outids),context_mask=sum(1<<i for i in hits),C=cc[b]))
  sets.append((outids,hits))
assert placements==J['placements'] and len(placements)==103
# Explicit nonnegative D/V counts. The residual x distance determines U.
pairs=set()
for i,p in enumerate(placements):
 for j,t in enumerate(placements):
  dx=t['head'][0]-p['exit'][0];drop=p['exit'][1]-t['head'][1]
  if dx<0 or drop<0:continue
  if any(d+v==drop and dx-d-3*v>=0 and (dx-d-3*v)%4==0 for d in range(dx+1)for v in range(dx//3+1)):
   pairs.add((i,j))
assert sorted(pairs)==[tuple(z)for z in J['exact_zero_C_endpoint_pairs']]
full=frozenset(range(5));totals=[0,0];complete=[]
for author in J['birth_subset_DAGs']:
 old=author['older_input_mask'];initial=frozenset(i for i in full if old>>i&1);start=(initial,-1,0)
 states={start};todo=deque([start]);edges=set()
 while todo:
  alive,last,depth=todo.popleft()
  if alive==full:continue
  for j,p in enumerate(placements):
   output,context=sets[j]
   if alive&context or last>=0 and(last,j)not in pairs:continue
   fresh=sorted(output-alive)
   for n in range(1,len(fresh)+1):
    for chosen in combinations(fresh,n):
     nxt=alive|set(chosen)
     if nxt!=full and p['C']!=0:continue
     child=(frozenset(nxt),j,depth+1)
     edges.add(((alive,last,depth),child,j,frozenset(chosen)))
     if child not in states:states.add(child);todo.append(child)
 def mask(s):return sum(1<<i for i in s)
 astates={(frozenset(i for i in full if b>>i&1),p,d)for b,p,d in author['states']}
 assert states==astates
 ae=set()
 for si,ti,p,sub in author['arcs']:
  def convert(k):
   b,p,d=author['states'][k];return(frozenset(i for i in full if b>>i&1),p,d)
  ae.add((convert(si),convert(ti),p,frozenset(i for i in full if sub>>i&1)))
 assert edges==ae
 for alive,j,depth in states:
  if alive==full:
   assert depth==1;complete.append((old,j))
 totals[0]+=len(states);totals[1]+=len(edges)
expected={(r['old_mask'],placements.index(r['source']))for r in J['completed_cohorts']}
assert set(complete)==expected and len(complete)==8
model=json.loads((ROOT/'core_periodicity_new/chronology_dcuv/delayed_height_probe/u1_residue_cegar/root_out.json').read_text())
potential=Path(model['potential_file']);assert hashlib.sha256(potential.read_bytes()).hexdigest()==model['potential_sha256']
weights=json.loads(potential.read_text())['values']
A=(0,22,20,10);height=lambda z:int(z.imag-z.real);scores=[]
for old,j in sorted(complete):
 p=placements[j];b=p['packet'];head=complex(*p['head'][:2]);O,_,e,h=G[b]
 peak=max(2*height(head+rotation(e,1))+A[(h+2)%4],*(2*height(head+rotation(o,1))+weights[f'w_{b}_{i}_2']for i,o in enumerate(sorted(O,key=xy))))
 expected=next(r['U1_created_peak']for r in J['completed_cohorts']if r['old_mask']==old and r['source']==p)
 assert peak==expected and peak<30,(p,peak,expected);scores.append(dict(older_mask=old,source=p,created_peak=peak))
out=dict(status='PASS independent literal contexts, exact zero-C endpoint counts and full birth-subset DAG closure',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),placements=len(placements),cases=len(J['birth_subset_DAGs']),states=totals[0],arcs=totals[1],completed_single_source_cohorts=scores,multistage_completions=0,scope='Necessary same-minimum-clock cohort theorem, not actual attainment or U1 closure. Numeric age5 requires lower-a>=5; heading-phase generalization is separately analytic.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
