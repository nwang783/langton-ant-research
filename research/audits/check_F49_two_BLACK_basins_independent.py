from pathlib import Path
from collections import defaultdict
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files={'prepared_F49_leaf_has_two_distinct_BLACK_root_basins.md':'b180a12c','check_prepared_F49_C_entry_basins.py':'56e34a1f','check_prepared_F49_C_entry_basins.json':'a8e48fb1','check_prepared_F49_portal_external_entry.json':'a8533d94'}
for f,h in files.items():assert sha(D/f).startswith(h)
assert sha(R/'audits/check_prepared_F48_F49_independent.json')=='50a7bcd50504d916bfd85fad31f7f112f9ae6712a676e30139a748dba81340ae'
J=json.loads((D/'check_prepared_F49_portal_external_entry.json').read_text());ref=json.loads((D/'check_prepared_F49_C_entry_basins.json').read_text())
H='NESW';v=[1j,1,-1j,-1];off=[-1j,-1-1j,-1,0];xy=lambda z:[int(z.real),int(z.imag)];p=complex(*J['start'][0]);h=H.index(J['start'][1]);B={complex(*q):('I',None)for q in J['initial_black']};face=p+off[h];seen={face:dict(time=-1,type='initial')};root={face:face};hist=defaultdict(list);states=[face];R0={};deaths={};entries=[]
for t,w in enumerate(J['word']):
 assert (p in B)==(w=='L');rank=len(hist[p]);hist[p].append((t,H[h],w,face));oldface=face;oldp=p
 if w=='R':
  B[p]=('R',t)
  if rank==0:R0[p]=face
 else:deaths[t]=(xy(p),B.pop(p))
 h=(h+(1 if w=='R'else-1))%4;p+=v[h];face=p+off[h]
 if w=='R':assert face==oldface
 if face not in seen:
  assert w=='L'
  if oldp in R0:assert rank==1;parent=R0[oldp];kind='WHITE';rt=root[parent]
  else:assert rank==0;parent=None;kind='BLACK';rt=face
  seen[face]=dict(time=t,cell=xy(oldp),rank=rank,type=kind,parent=xy(parent)if parent is not None else None,basin=xy(rt));root[face]=rt;entries.append((xy(face),seen[face]))
 states.append(face)
 assert xy(p)==J['trace'][t]['next_cell']and H[h]==J['trace'][t]['next_incoming']and sorted(map(xy,B))==J['trace'][t]['black_after']
F=-1j;G=1;HH=1j
assert seen[F]['time']==0 and seen[HH]['time']==21 and seen[F]['type']==seen[HH]['type']=='BLACK'
assert seen[G]['time']==26 and seen[G]['type']=='WHITE'and seen[G]['parent']==xy(F)
assert R0[1]==F and R0[1+1j]==HH and root[F]!=root[HH]
assert [t for t,f in enumerate(states)if f==G]==[27]
assert deaths[26]==([1,0],('R',2))and deaths[27]==([1,1],('R',23))
assert all(q not in hist for q in(2,2+1j))
for f,z in seen.items():assert ref['all_first_entries'][str(tuple(xy(f)))]==z
out=dict(status='PASS finite F49 internal color production with TWO distinct BLACK-root C-entry basins',files={f:sha(D/f)for f in files},dependency=sha(R/'audits/check_prepared_F48_F49_independent.json'),all_first_entries=entries,selected_lifetimes={str(t):deaths[t]for t in(26,27)},leaf_active_cut=27,final_black=sorted(map(xy,B)),review=['Fresh full-field49 replay and activeC=p+heading_offset independently reconstruct every first-entry parent and basin. G is a WHITE first-entry leaf at update26, active only at cut27. Its two L colors were born at actual internalR2 andR23, not initial BLACK.','A has SAME EE headings and parent faceF; B has OPPOSITE SN headings and its R0 faceH is a different BLACK-root basin. Their finite roots activate at actualBLACK-firstL0 andL21. No full-quotient ancestry or merger interpretation is substituted.','The result is a scope qualifier, not a one-basin counterexample or a proof of a component-payment theorem. Prepared external BLACK fuel and unknown later visits remain.'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(sha(S.with_suffix('.json')))
