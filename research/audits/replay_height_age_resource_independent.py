from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
ROOT=Path('/workspace/shared/langton');D=ROOT/'core_periodicity_new/chronology_dcuv/delayed_height_probe';P=D/'u1_k6_petri.json';W=D/'u1_k6_age_interval8.best.txt';J=json.loads(P.read_text());S=json.loads(Path(J['source_file']).read_text());DF=json.loads(Path(J['dfa_file']).read_text());G=json.loads((ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];rules=json.loads((ROOT/'core_periodicity_new/chronology_dcuv/counted_input_age_rules_complete.json').read_text());rules={(a,x,y):r for a,x,y,r in rules};mapping=list(map(int,(D/'u1_k6_age_interval8.edge_ids').read_text().split()));low=J['low_cutoff'];phase=S['phase'];F=J['initial_bound'];states=J['positions'];poses=J['poses'];CC=0;pool=defaultdict(Counter);peak=0;count=0;constraints=0
lines=W.read_text().splitlines();pos=int(next(l for l in lines if l.startswith('start ')).split()[1]);assert pos in J['initial_controls']
def coords(v,h):
 z=complex(*v)*((-1j)**(h+phase));return round(z.real+z.imag)
def trace(a):
 p=0j;h=1j
 for c in G[a]['word']:h*=(-1j if c=='R'else 1j);p+=h
 return p,(1j,1,-1j,-1).index(h)
def packet(a,pi,do_output=True):
 global CC,peak,constraints
 h,q=poses[pi];c=G[a]['name'].count('C');need=[];out=[]
 if q is not None:
  need=[(q+coords(v,h),rules[a,*v])for v in G[a]['inputs']if q+coords(v,h)>F]
  out=[q+coords(v,h)for v in G[a]['outputs']if q+coords(v,h)>F]
 else:
  assert all(low+coords(v,h)<=F for v in G[a]['inputs']+G[a]['outputs'])
 for z,r in sorted(need,key=lambda z:-z[1]):
  eligible=[age for age,n in pool[z].items()if n and age>=r];assert eligible,(count,a,z,r,dict(pool[z]));age=min(eligible);pool[z][age]-=1;constraints+=1
 if do_output:
  for z,row in list(pool.items()):
   new=Counter()
   for age,n in row.items():new[min(4,age+c)]+=n
   pool[z]=new
  for z in out:pool[z][c]+=1
  CC+=c;peak=max(peak,max((sum(v.values())for v in pool.values()),default=0))
for line in lines:
 if not line.startswith('EDGE '):continue
 ei,p,to,a=map(int,line.split()[1:5]);e=J['transitions'][mapping[ei]];assert e[:3]==[p,to,a] and p==pos
 pi,ds=states[p];pj,dt=states[to];h,q=poses[pi];nh,nq=poses[pj];delta,dh=trace(a);dq=coords((int(delta.real),int(delta.imag)),h)
 assert nh==(h+dh)%4
 if q is not None and nq is not None:assert nq==q+dq
 elif q is not None:assert q+dq<=low
 elif nq is not None:assert nq-dq<=low
 assert DF['transitions'][ds][DF['keep'].index(a)]==dt
 packet(a,pi);pos=to;count+=1
assert any(p==pos for p,_ in J['goal_requirements']);pi,ds=states[pos];a=S['target'];assert DF['transitions'][ds][DF['keep'].index(a)]>=0
before=CC;packet(a,pi,False)
R={'status':'PASS independent exact current-age multiplicity replay and heading/height/DFA edges','strict_packets':count,'C_before_goal':before,'peak_tokens_at_one_height':peak,'high_input_allocations_including_goal':constraints,'scope':'Positive abstract resource path only. No transverse/color/producer-role ant realization; no no-hit or confinement proof. This does not sign the complete discovery model generator.','hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in(P,W,Path(__file__))}}
Path(__file__).with_suffix('.json').write_text(json.dumps(R,indent=2)+'\n');print(json.dumps(R))
