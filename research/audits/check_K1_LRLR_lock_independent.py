from pathlib import Path
from itertools import product
from collections import Counter
import hashlib,json
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'K1_pipeline_detours_2026-10-23'
src=(SELF.parent/'check_K1_straight_double_max_independent.py').read_text().split('rows=[];attempts=0')[0]
src=src.replace("if not lower(('A',2),('B',1),1):return None","\n for x,y in zip(order,order[1:]):\n  if not lower(x,y,1):return None\n for k,h in enumerate(out(hs['Z'])):\n  if h==0 and not lower(('A',1),('Z',k),0):return None")
ns={'__file__':str(SELF.parent/'check_K1_straight_double_max_independent.py')};exec(src,ns)
ns['ports']=[('q',1,'C'),('C',0,'A'),('A',3,'Z'),('Z',0,'Y'),('Y',1,'B'),('B',2,'A'),('Z',2,'q')]
ns['order']=[('C',1),('A',0),('C',2),('A',1),('B',0),('A',2),('B',1)]
choices=ns['choices'];solve=ns['solve'];rows=[];attempts=0
selectedE=[(1,1,3),(1,1,3,1),(1,1,3,3)];selectedN=[(0,0,2),(0,0,2,0),(0,0,2,2)]
for mz,my in product(('strict','equal'),repeat=2):
 for c,a,b,z,y,q in product(selectedE,selectedN,selectedE,choices(3,mz),choices(0,my),choices(0,mz)):
  if mz=='strict'and len(z[::2])!=len(q[::2]):continue
  attempts+=1;hs=dict(C=c,A=a,B=b,Z=z,Y=y,q=q)
  if solve(hs)is None:continue
  rows.append(dict(Z_other=mz,Y_other=my,headings={k:''.join('NESW'[h]for h in v)for k,v in hs.items()}))
assert len(rows)==23,(len(rows),attempts)
ref=json.loads((D/'LR_pair_all_states_complete_ports.json').read_text());key=lambda r:(r['Z_other'],r['Y_other'],tuple(sorted(r['headings'].items())))
assert{key(r)for r in rows}=={key(r)for r in ref['rows']}
ones=[r for r in rows if r['headings']['A']=='NNSN'];assert len(ones)==3
assert{(r['headings']['Z'],r['headings']['Y'],r['headings']['q'],r['Y_other'])for r in ones}=={('WWW','NNSS','NNNS','equal'),('WWWE','NNN','NNNS','strict'),('WWWE','NNNS','NNNS','strict')}
assert all(r['headings']['q'][0]=='N'for r in rows)
# Exact shared-cell overlap of two consecutive actual LR windows.
locks=[]
for r,s in product(rows,repeat=2):
 if r['headings']['B']!=s['headings']['C']or r['headings']['Y']!=s['headings']['q']:continue
 locks.append((r,s));assert r['Z_other']==r['Y_other']=='strict';assert{v:r['headings'][v]for v in('A','Z','Y','B')}==dict(A='NNSN',Z='WWWE',Y='NNNS',B='EEWE')
assert locks
p=D/'K1_LRLR_forces_locked_row4_and_straight.md';sha=hashlib.sha256(p.read_bytes()).hexdigest();assert sha=='4f9db2ac3df183a0d8fb549fa2efce0ac27f6a0ee94dc2dccd605ff523aee165'
out=dict(status='PASS branchful LRLR locks strict row4; leftmost K1 needs straight and LEFT max branch',note_sha256=sha,complete_candidate_count=attempts,necessary_row_count=len(rows),rows=rows,input1_rows=ones,compatible_overlap_pairs=len(locks),analytic='Complete independent 1..4-read histories, physical port ordinal equality, per-cell spacing4, full K1 order and canonical boundary minimum regenerate23 rows without author right-turn inventories. Equal-G state1 cases fail early suppliers or an actual L3 clock cycle. Signed strict cleanup removes residual NSN/NSNN/NSSN through rank spacing. Every lowerq starts R0N; shared Y=q prime locks first RIGHT to WWWE/NNNS strict11. All-bend essential curve plus signed noLL/zero turn alternates, so every RIGHT is locked and no LEFT max branch exists. Signed leftmost branch-free exclusion then forces at least one straight face; independent signed branch necessity still holds.',scope='Complete WHITE cap4 K1 canonical max curve. Both straight and LEFT branch are necessary at leftmost component, not necessarily same face; no arbitrary K1 exclusion, fuel or capture theorem.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print('candidates',attempts,'rows',len(rows),'overlaps',len(locks))
