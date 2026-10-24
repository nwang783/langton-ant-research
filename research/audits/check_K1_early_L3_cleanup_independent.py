from pathlib import Path
from itertools import product
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23'
q=SELF.parent/'check_K1_early_parent_square_independent.py';env={'__file__':str(q)};exec(q.read_text().split('rows=[];attempts=0')[0],env)
ns=env['ns'];base=env['base'];H=env['H'];T=env['T'];choices=env['choices'];O=ns['out'];baseports=env['baseports']+[('t',3,'f'),('f',2,'g')]
ns['mode']='new';ns['parent_birth']='g';ns['birth']=('u',1);ns['order']=[('A',1),('B',0),('A',2),('B',1),('D',0),('B',2),('D',1)]
prior=[p for p in json.loads((D/'bit11_early_parent_left_square_ports.json').read_text())['rows']if p['headings']['g']=='SSNS'];assert len(prior)==54
route=[('B',2),('v',1),('a',1),('Y',2),('u',2),('t',1),('f',3),('g',3),('u',3),('t',2),('a',2),('Y',3),('B',3)]
pos={'B':1+1j,'v':1+2j,'a':2j,'Y':1j,'u':-1+1j,'t':-1+2j,'f':-2+2j,'g':-2+1j};dirs=(1j,1,-1j,-1)
results={}
for deadline in (False,True):
 code=base.replace('return comp,delta','return comp,delta,edges')
 if deadline:code=code.replace('nc=len(set(comp.values()));dist=[0]*nc',"if not lower(('B',3),('D',1),1):return None\n nc=len(set(comp.values()));dist=[0]*nc")
 exec(code,ns);rows=[];tried=0;mins={}
 for pr in prior:
  ns['ports']=baseports+([('v',1,'D')]if pr['kind']=='S'else[('v',1,'w'),('w',2,'D'),('D',3,'B')])
  for fh in choices(1,'strict'):
   tried+=1;hs={v:H(h)for v,h in pr['headings'].items()};hs['f']=fh;sol=ns['solve'](hs)
   if sol is None:continue
   cp,de,edges=sol;assert T(fh)=='EEEW';assert cp['f',2]==cp['g',1]and de['f',2]==de['g',1]-1
   for k,a in enumerate(route):assert cp[a]==cp[route[0]]and de[a]-de[route[0]]==k
   for a,b in zip(route,route[1:]):
    v,k=a;u,l=b;oh=O(hs[v])[k];assert pos[v]+dirs[oh]==pos[u]and hs[u][l]==oh
   assert [k%2 for v,k in route[5:9]]==[1]*4
   # The next physical contact is absent from every occupied route location.
   dpos=2+2j if pr['kind']=='S'else 2+1j;assert dpos not in set(pos.values())
   if deadline:
    start=('B',1);goal=('D',1);nc=len(set(cp.values()));dist=[-10**9]*nc;dist[cp[start]]=0
    for _ in range(nc-1):
     for a,b,g in edges:
      if dist[a]>-10**8:dist[b]=max(dist[b],dist[a]+g)
    lo=dist[cp[goal]]+de[goal]-de[start]
    prof=(pr['kind'],T(hs['v']),T(hs.get('w',())),T(hs['D']));mins[prof]=min(mins.get(prof,10**9),lo)
   rows.append(dict(kind=pr['kind'],headings={v:T(h)for v,h in hs.items()}))
 results[str(deadline)]=dict(candidates=tried,rows=len(rows),profiles=sorted(mins.items()))
 if deadline:
  ref=json.loads((D/'bit11_early_L3_cleanup_next_gate_ports.json').read_text())['rows'];key=lambda r:(r['kind'],tuple(sorted(r['headings'].items())))
  assert {key(r)for r in rows}=={key(r)for r in ref}and len(rows)==36
  assert all(lo>= (18 if prof[0]=='S'else 27 if prof[2]=='EEWW'else 23)for prof,lo in mins.items())
  assert {p[1:3]for p in mins if p[0]=='R'}=={('NNNS','EEEW'),('NNNS','EEE'),('NNN','EEWW')}
 else:assert len(rows)==54
notes={'K1_early_LEFT_parent_L3_exact_cleanup.md':'484944913183bda20019b92bdeff6552bc5edabb5cd92571e8c20edfcd97af0f','K1_early_L3_cleanup_forces_next_gate.md':'e385bb1fc18780e71f14936d58bf77361cb93e569105fba75b286700f4c8e212'}
for f,h in notes.items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
out=dict(status='PASS exact twelve-edge physical old-stock route and disjoint next-main-gate waits',notes=notes,results=results,route=route,analytic='Complete t-to-f and f-to-g ordinal matching forces f EEEW; its earlier R2 funds g L1. The 12-edge actual route omits next physical D. K1 puts D L1 after B R2, hence strictly after B L3. Full next profiles leave strict S or locked row4 and both retained falls. The exact next-main intervals, distinct from the branched predecessor intervals, contribute 13/18/22 over baseline5. No later B R2 minimal time is claimed.',scope='Necessary old-stock interfaces and main-clock refinement only, not exterior realization, extra overlapping-span charge, original fuel or K1 exclusion.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(results)
