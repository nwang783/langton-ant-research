"""Exact two-module specialization on the two retained named return legs."""
from pathlib import Path
from collections import defaultdict
import json,sys,hashlib
ROOT=Path('/workspace/shared/langton');OUT=Path(__file__).parent
sys.path.insert(0,str(ROOT/'reframe_finite_seed_2026-10-24'))
from active_flight import cursor,ends,sector,step
SOURCE=OUT/'helper_return_connector_or_growth_certificate.json'
class Graph:
 def __init__(self,B,k):
  self.k=k;self.g=defaultdict(dict)
  for q in B:self.update(q,True)
 def update(self,q,on):
  a,b=ends(q,self.k)
  if on:self.g[a][b]=q;self.g[b][a]=q
  else:del self.g[a][b];del self.g[b][a]
 def component(self,v):
  seen={v};todo=[v];E=set()
  for u in todo:
   for v,q in self.g[u].items():
    E.add(q)
    if v not in seen:seen.add(v);todo.append(v)
  return E
ans=[]
for a in json.loads(SOURCE.read_text())['controls']:
 B=set(map(tuple,a['departure_full_black']));p,h=a['departure_pose'];p=tuple(p);k=sector(p,h);G=Graph(B,k)
 f=tuple(a['helper']);e=tuple(a['parent']);F=G.component(ends(f,k)[0]);E=G.component(ends(e,k)[0]);U=F|E
 assert not F&E and f not in G.component(cursor(p,h))and e not in G.component(cursor(p,h))
 M=a['M'];assert len(F)<=M-1 and len(E)<=M-1
 before=set(B);first=None;old=set(B);retired=[]
 for t in range(a['departure'],a['helper_consumption']+1):
  C=G.component(cursor(p,h));assert len(C)<=M
  if f in C and first is None:
   assert last_turn=='R'and F<=C and F<=B and last_cell in C-F
   first=dict(cut=t,previous_R_cell=last_cell,active_mass=len(C),complete_active=sorted(C))
  if first is None:assert F<=B
  if t==a['helper_consumption']:assert p==f and p in B;break
  q=p;on=q not in B
  if not on and q in old:old.remove(q);retired.append(q)
  G.update(q,on);p,h=step(B,p,h);last_turn='R'if on else'L';last_cell=q
 assert first is not None and B==set(map(tuple,a['helper_pre_read_full_black']))
 K=a['old_consumption_count'];assert len(retired)==K
 outside=[q for q in retired if q not in U];H=len(outside)
 assert len(retired)-H<=len(U)-2
 exact_rhs=2*a['distance']+2-2*len(U);coarse_rhs=2*a['distance']-4*M+6
 lhs=a['global_mass_change']+2*H
 assert lhs>=exact_rhs>=coarse_rhs
 assert a['passive_mass_change']+2*H>=exact_rhs-M
 ans.append(dict(name=a['name'],helper_module=sorted(F),parent_module=sorted(E),union_size=len(U),
  helper_first_R_import=first,K=K,inside_two_module_retirements=K-H,H=H,additional_old_lifetime_cells=outside,
  global_mass_change=a['global_mass_change'],passive_mass_change=a['passive_mass_change'],
  exact_connector_or_growth_rhs=exact_rhs,cap_only_rhs=coarse_rhs,lhs=lhs,
  scope='Two fixed actual modules at departure; cut-d identities stay fixed through mergers/rebirths. No material-neutral long fresh return is constructed.'))
out=dict(status='AUTHOR exact two-module connector-or-growth specialization',source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),controls=ans)
(OUT/'two_module_connector_or_growth_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps([{k:a[k]for k in['name','union_size','K','H','global_mass_change','exact_connector_or_growth_rhs','cap_only_rhs','lhs']}for a in ans],indent=2))
