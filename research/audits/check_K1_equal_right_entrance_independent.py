from pathlib import Path
from itertools import product
from collections import Counter
import hashlib,json
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];P=ROOT/'K1_pipeline_detours_2026-10-23'
p=SELF.with_name('check_K1_straight_double_max_independent.py');s=p.read_text().split('rows=[];attempts=0')[0]
s=s.replace("if not lower(('A',2),('B',1),1):return None","\n for aa,bb in [(('V',2),('U',1)),(('U',2),('A',1)),(('A',2),('B',1))]:\n  if not lower(aa,bb,1):return None")
n={'__file__':str(SELF)};exec(compile(s,str(p),'exec'),n)
n['ports']=[('V',2,'a'),('a',3,'r'),('r',0,'U'),('U',1,'V'),('U',3,'z'),('z',2,'q'),('q',1,'r'),('A',3,'w'),('w',0,'y'),('y',1,'B'),('B',2,'A'),('e',1,'z'),('w',2,'e'),('z',0,'A'),('q',3,'u'),('u',0,'e')]
solve=n['solve'];choices=n['choices'];out=n['out']
pred=json.loads(SELF.with_name('check_K1_straight_branch_predecessor_independent.json').read_text())['rows'];future=json.loads(SELF.with_name('check_K1_straight_double_max_independent.json').read_text())['necessary_rows'];rows=[]
for prior,fut,u in product(pred,future,choices(3,'strict')+choices(3,'equal')):
 if prior['r_other']!='equal':continue
 hh=dict(prior['h'])
 if any(k in hh and hh[k]!=v for k,v in fut.items()):continue
 hh.update(fut);hs={k:tuple('NESW'.index(c)for c in v)for k,v in hh.items()};hs['u']=u
 ans=solve(hs)
 if ans is None:continue
 cp,de=ans
 assert hs['q']==(0,0,2,2) and u in[(1,3,3),(1,3,3,1)]
 assert hs['e']==((0,2,2)if len(u)==3 else(0,2,2,0))
 for aa,bb,dd in[(('U',1),('q',0),-2),(('U',1),('A',0),2),(('U',2),('q',2),2),(('z',1),('z',2),4)]:assert cp[aa]==cp[bb]and de[bb]-de[aa]==dd
 rows.append(dict(a_other=prior['a_other'],h={k:''.join('NESW'[x]for x in v)for k,v in hs.items()}))
assert len(rows)==80
ref=json.loads((P/'straight_branch_equal_right_entry_closure.json').read_text())
key=lambda r:(r['a_other'],tuple(sorted(r['h'].items())))
assert{key(r)for r in rows}=={key(dict(a_other=r['a_other'],h=r['headings']))for r in ref['rows']}
# Physical face choices at the four J corners; R chooses a quadrant by heading.
corner={'q':(0,-1),'u':(-1,-1),'e':(-1,0),'z':(0,0)};offset=((0,-1),(-1,-1),(-1,0),(0,0));J=(-1,-1)
for row in rows:
 for v,p in corner.items():
  h=row['h'][v];r0='NESW'.index(h[0]);d=offset[r0];face=(p[0]+d[0],p[1]+d[1])
  if v=='e':assert face==J and h[1]!=h[0]
  else:assert face!=J
  assert not(face==J and h[1]==h[0])
# q.L1 bounds follow from SAME-CELL spacing and exact links, not minimum clocks.
# q0=delta-2, q2=U2+2 -> delta+2<=q1<=U2-2.
report=dict(status='PASS independent equal-max RIGHT entrance obstruction',note_sha256=hashlib.sha256((P/'K1_straight_branch_equal_right_entrance_obstruction.md').read_bytes()).hexdigest(),necessary_rows=rows,corner_counts={str(k):v for k,v in Counter((r['h']['q'],r['h']['u'],r['h']['e'])for r in rows).items()},analytic_side='No J corner can be selected OUTGOING from J, so J is off the birth cycle. Incoming selected contacts enter J and are also off cycle. The whole closed J square lies LEFT. q.L1 lies strictly between A.R0 and U.R2, the actual RIGHT excursion, contradiction.',scope='Complete WHITE cap4 K1, branchful physical lift, no leftmost or globally absent branch premise. Every straight max branch therefore has strict-fall entrance; reservation is final odd BLACK OUTPUT only.')
assert report['note_sha256']=='c945fd545aa4bc3cfcd0617842f162f145e602b7eb7dc8c7b8736363d4400dbd'
SELF.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print(report['status']);print(report['corner_counts'])
