from pathlib import Path
from itertools import product
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];p=SELF.with_name('check_K1_straight_double_max_independent.py');n={'__file__':str(SELF)};exec(compile(p.read_text().split('rows=[];attempts=0')[0],str(p),'exec'),n)
n['ports']=[('A',3,'w'),('w',0,'y'),('y',1,'B'),('B',2,'A'),('e',1,'z'),('w',2,'e'),('z',0,'A'),('U',3,'z'),('z',2,'q'),('q',3,'u'),('u',0,'e')]
solve=n['solve'];out=n['out'];prior=json.loads(SELF.with_name('check_K1_straight_double_max_independent.json').read_text())['necessary_rows'];rows=[]
us=[h for k in(3,4)for h in product((1,3),repeat=k)if h.count(3)>=3]
assert set(us)=={(3,3,3),(3,3,3,1),(3,1,3,3),(3,3,1,3),(1,3,3,3),(3,3,3,3)}
for r in prior:
 for U,q,u in product([(0,0,2),(0,0,2,2)],[(2,0,2),(2,0,2,0)],us):
  hs={k:tuple('NESW'.index(x)for x in s)for k,s in r.items()};hs.update(U=U,q=q,u=u);ans=solve(hs)
  if ans is None:continue
  cp,de=ans;assert u==(1,3,3,3)and q==(2,0,2)and hs['e']==(0,2,2)
  # Chronological port equalities, not chosen minimum-clock values.
  links=[(('u',2),('e',0)),(('e',0),('z',2)),(('z',2),('q',2)),(('q',2),('u',3))]
  for a,b in links:assert cp[a]==cp[b]and de[b]-de[a]==1
  for a,b,d in[(('z',1),('q',0),1),(('z',1),('u',1),2),(('z',2),('q',1),-3),(('z',2),('u',2),-2)]:assert cp[a]==cp[b]and de[b]-de[a]==d
  assert [out(hs[v])[k]for v,k in[('u',2),('e',0),('z',2),('q',2)]]==[0,1,2,3]
  rows.append({v:''.join('NESW'[x]for x in h)for v,h in hs.items()})
assert len(rows)==10
# One-occurrence birth exclusions: at a flat negative corner, L1/R2 must
# depart through the same face-output port, requiring at least two occurrences.
assert rows and all(r['u'].count('E')==1 for r in rows)
# Same-R q=N-normalized SNS fixes one oriented straight face; selected
# contacts have opposite R headings, so q cannot be any selected rise cell.
assert all(r['q'][0]==r['q'][2]for r in rows)
p=ROOT/'K1_pipeline_detours_2026-10-23/K1_strict_fall_branch_stock_loops.md';assert hashlib.sha256(p.read_bytes()).hexdigest()=='730d9bb19a41dfbdd490b835f3c67679c5d54bc842739c7b62ca9eb2522a6536'
o=dict(status='PASS independent strict-fall supplier closure and exact stock loops',note_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),all_W_supplier_histories=us,necessary_rows=rows,clock_bound='u.L1=beta+2;u.R2=gamma-2; actual same-cell spacing>=4 implies gamma-beta>=8.',birth_results=['J unique negative corner z, so parent(J)=F and B(J)=beta.','u.R0 chooses lowerQ; B(Q)<=beta-3. Q top-right R0 and top-left one-occurrence port cannot birth; bottom parent has B<=beta-8.','When w=EWW only, H upper-left one-occurrence port cannot birth, forcing lower-left parent.'],output_reservation='Each strict-fall branch owns distinct odd same-R q class; disjoint from all opposite-R selected rise entries. Nodd>=n_up+n_f, only OUTPUT, not original fuel.',scope='Exact local branchful complete-WHITE cap4 K1 necessary history, not exterior realization, iterative regress, additive stock budget or exclusion.')
SELF.with_suffix('.json').write_text(json.dumps(o,indent=2)+'\n');print(o['status'],len(rows))
