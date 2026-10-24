from pathlib import Path
from itertools import product
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23';p=SELF.parent/'check_K1_early_L3_cleanup_independent.py';env={'__file__':str(p)};exec(p.read_text().split('results={}')[0],env)
ns=env['ns'];base=env['base'];H=env['H'];T=env['T'];choices=env['choices'];baseports=env['baseports']+[('g',3,'j'),('j',0,'k'),('k',1,'f')]
extra="""
 if not lower(('B',3),('D',1),1):return None
 firstQ=[next((v,k)for k,x in enumerate(out(hs[v]))if x==di)for v,di in [('j',0),('k',1),('f',2),('g',3)]]
 qb=(Qbirth,1)
 if qb not in firstQ:return None
 for x in firstQ:
  if x!=qb and not lower(qb,x,1):return None
"""
base=base.replace('nc=len(set(comp.values()));dist=[0]*nc',extra+'\n nc=len(set(comp.values()));dist=[0]*nc');exec(base,ns)
prior=json.loads((D/'bit11_early_L3_cleanup_next_gate_ports.json').read_text())['rows'];assert len(prior)==36
ns['mode']='new';ns['parent_birth']='g';ns['birth']=('u',1);ns['order']=[('A',1),('B',0),('A',2),('B',1),('D',0),('B',2),('D',1)]
rows=[];attempts=0
for pr in prior:
 ns['ports']=baseports+([('v',1,'D')]if pr['kind']=='S'else[('v',1,'w'),('w',2,'D'),('D',3,'B')])
 for jm,km,qb in product(('strict','equal'),('strict','equal'),('j','k')):
  for j,k in product(choices(3,jm),choices(0,km)):
   if qb=='j'and not T(j).startswith('EEW'):continue
   if qb=='k'and not T(k).startswith('SSN'):continue
   attempts+=1;ns['Qbirth']=qb;hs={v:H(h)for v,h in pr['headings'].items()};hs.update(j=j,k=k);sol=ns['solve'](hs)
   if sol is None:continue
   cp,de=sol
   def eq(a,b,n):assert cp[a]==cp[b]and de[a]-de[b]==n,(a,b,n)
   eq(('k',3),('e',0),-4)
   if qb=='j':assert(T(j),T(k),jm,km)==('EEWE','NNNS','equal','strict');eq(('j',1),('g',0),-3);eq(('k',1),('g',0),2)
   else:assert(T(j),T(k),jm,km)==('W','SSNS','strict','equal');eq(('k',1),('g',0),-2);eq(('k',2),('g',0),2)
   def height(h,m):return'M'if m=='equal'else'M-'+str(len(h[::2]))
   rows.append(dict(kind=pr['kind'],headings={v:T(h)for v,h in hs.items()},Qbirth=qb,jother=height(j,jm),kother=height(k,km)))
ref=json.loads((D/'bit11_surviving_cleanup_Q1_parent_ports.json').read_text());key=lambda r:(r['kind'],r['Qbirth'],tuple('equal' if r[k] in ('M','equal') else 'strict' for k in ('jother','kother')),tuple(sorted(r['headings'].items())))
assert attempts==4536 and len(rows)==72 and{key(r)for r in rows}=={key(r)for r in ref['rows']}
profiles=sorted({(r['headings']['j'],r['headings']['k'],r['Qbirth'],r['jother'],r['kother'])for r in rows})
note=D/'K1_surviving_cleanup_Q1_two_ancestor_profiles.md';assert hashlib.sha256(note.read_bytes()).hexdigest()=='a7f57d46c2dc591af2eb6f40eeb21e58e4b659a9e250c822d281f2c5b2102054'
out=dict(status='PASS complete Q1 ancestor square with strict RIGHT/STRAIGHT and older birth clocks',note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),candidates=attempts,survivors=len(rows),profiles=profiles,analytic='R mode: kL1=gamma+2, kL3=delta-4 implies delta>=gamma+14; Q1 birth gamma-3<=alpha-21 and parent<=alpha-26. S mode: kR2=gamma+2, kL3=delta-4 implies delta>=gamma+10; Q1 birth gamma-2<=alpha-16 and parent<=alpha-21. All R0/L1/R2/L3 ports and canonical boundary minima are retained; no extra off-Gamma K1 ordering is added.',scope='Finite genuine ancestor classification, not a repeated branch mechanism, distinct resource or additional main-P interval charge.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(attempts,len(rows),profiles)
