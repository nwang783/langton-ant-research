from pathlib import Path
from itertools import product
import hashlib,json
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'K1_pipeline_detours_2026-10-23'
s=(SELF.parent/'check_K1_straight_double_max_independent.py').read_text().split('rows=[];attempts=0')[0]
s=s.replace("if not lower(('A',2),('B',1),1):return None","\n for a,b in zip(order,order[1:]):\n  if not lower(a,b,1):return None")
ns={'__file__':str(SELF.parent/'check_K1_straight_double_max_independent.py')};exec(s,ns);choices=ns['choices'];solve=ns['solve'];O=ns['out'];H=lambda s:tuple('NESW'.index(c)for c in s);T=lambda h:''.join('NESW'[x]for x in h)
baseports=[('A',3,'Z'),('Z',0,'Y'),('Y',1,'B'),('B',2,'A'),('B',0,'v'),('v',3,'a'),('a',2,'Y')]
ns['order']=[('A',1),('B',0),('A',2),('B',1),('D',0),('B',2),('D',1)]
rows=[];attempts=0
for kind in('S','R'):
 ns['ports']=baseports+([('v',0,'D')]if kind=='S'else[('v',1,'w'),('w',2,'D'),('D',3,'B')])
 # For S physical v->D is N, since entry B and exit D are both E at this rotation?
 if kind=='S':ns['ports']=baseports+[('v',1,'D')]
 for mk in('strict','equal'):
  if kind=='S'and mk=='equal':continue # signed bit1 straight has strict first other.
  modes=('strict','equal')if kind=='R'else('none',)
  for mw in modes:
   vs=choices(0,mk);aa=choices(1,mk);ws=choices(1,mw)if kind=='R'else[None]
   ds=('SSN','SSNS','SSNN')if kind=='R'else('EEW','EEWE','EEWW')
   for v,a,w,dd in product(vs,aa,ws,ds):
    attempts+=1;hs=dict(A=H('NNSN'),Z=H('WWEW'),Y=H('NSSS'),B=H('EEWE'),v=v,a=a,D=H(dd))
    if w is not None:hs['w']=w
    sol=solve(hs)
    if sol is None:continue
    cp,de=sol
    assert mk=='strict'and T(v)in('NNN','NNNS')and T(a)in('EWE','EWEE','EEEW')
    assert cp['a',0]==cp['B',1]and de['a',0]-de['B',1]==-2
    assert cp['Y',1]==cp['B',1]and de['Y',1]-de['B',1]==-1
    rows.append(dict(kind=kind,first_other=mk,headings={k:T(v)for k,v in hs.items()}))
ref=json.loads((D/'bit11_max_RIGHT_outward_parent_ports.json').read_text());key=lambda r:(r['kind'],r['first_other'],tuple(sorted(r['headings'].items())))
assert len(rows)==21 and{key(r)for r in rows}=={key(r)for r in ref['rows']},(len(rows),{key(r)for r in rows}-{key(r)for r in ref['rows']})
# Explicit equal-first-other cycle follows ordinal physical edge matching.
cycles=[]
for v,a in product(('NNSN','SNNN'),('WWEW','EWWW')):
 hs=dict(Y=H('NSSS'),B=H('EEWE'),v=H(v),a=H(a));es=[]
 for u,di,w in[('Y',1,'B'),('B',0,'v'),('v',3,'a'),('a',2,'Y')]:
  sr=[i for i,x in enumerate(O(hs[u]))if x==di];ta=[i for i,x in enumerate(hs[w])if x==di];assert len(sr)==len(ta)
  es.extend([((u,i),(w,j))for i,j in zip(sr,ta)])
 assert all(x in es for x in[(('Y',3),('B',3)),(('B',3),('v',3)),(('v',3),('a',3)),(('a',3),('Y',3))]);cycles.append([v,a])
p=D/'K1_bit11_max_RIGHT_branch_outward_parent.md';sha=hashlib.sha256(p.read_bytes()).hexdigest();assert sha=='b360bbb8469978f784e9c5bab516e7dc237b1662dfad7ae3a871aa3b5e88039a'
out=dict(status='PASS bit11 max-RIGHT upper branch further-LEFT parent',note_sha256=sha,raw_complete_candidate_count=attempts,necessary_rows=rows,equal_first_other_impossible_cycles=cycles,common_clocks={'aR0':'B(next main)-2','YL1':'B(next main)-1'},analytic='Every S/R successor retains all output states and both second other heights. A maximum first other creates an actual L3 four-cycle. In every strict survivor a=EWE/EWEE/EEEW chooses I at R0, while Y.L1 uses I before first R2 outgoing boundary. Both right I corners nonnegative, so parent is(-2,0) or(-2,2), birth at most B(next main)-8. EEEW late L3 is retained for S.',scope='One real supplier obligation. No off-cycle, iteration, component/root injection, fuel or universal K1 exclusion.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(attempts,len(rows))
