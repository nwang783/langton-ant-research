from pathlib import Path
from itertools import product
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'K1_pipeline_detours_2026-10-23'
s=(SELF.parent/'check_K1_straight_double_max_independent.py').read_text().split('rows=[];attempts=0')[0]
s=s.replace("if not lower(('A',2),('B',1),1):return None","\n for a,b in zip(order,order[1:]):\n  if not lower(a,b,1):return None\n first=[next((v,k)for k,x in enumerate(out(hs[v]))if x==di)for v,di in [('u',0),('t',1),('a',2),('Y',3)]]\n if birth not in first:return None\n for x in first:\n  if x!=birth and not lower(birth,x,1):return None")
ns={'__file__':str(SELF.parent/'check_K1_straight_double_max_independent.py')};exec(s,ns);choices=ns['choices'];solve=ns['solve'];O=ns['out'];H=lambda s:tuple('NESW'.index(c)for c in s);T=lambda h:''.join('NESW'[x]for x in h)
prior=json.loads((SELF.parent/'check_K1_bit11_outward_parent_independent.json').read_text())['necessary_rows'];uvals=[]
for mode in('strict','equal'):
 for u in choices(3,mode):
  if u.count(3)==1:uvals.append((u,mode))
assert{T(u)for u,m in uvals}=={'W','WE','WEE','WEEE','EEW','EEWE'}
baseports=[('A',3,'Z'),('Z',0,'Y'),('Y',1,'B'),('B',2,'A'),('B',0,'v'),('v',3,'a'),('a',2,'Y'),('Y',3,'u'),('u',0,'t'),('t',1,'a')]
ns['order']=[('A',1),('B',0),('A',2),('B',1),('D',0),('B',2),('D',1)]
rows=[];attempts=0
for pr in prior:
 ns['ports']=baseports+([('v',1,'D')]if pr['kind']=='S'else[('v',1,'w'),('w',2,'D'),('D',3,'B')])
 for (u,um),tm in product(uvals,('strict','equal')):
  for t in choices(0,tm):
   for born in('u','t'):
    # The signed canonical max first-L negative-corner rule, not a chosen phase.
    if born=='u'and T(u)not in('EEW','EEWE'):continue
    if born=='t'and not T(t).startswith('SSN'):continue
    attempts+=1;ns['birth']=(born,1);hs={v:H(x)for v,x in pr['headings'].items()};hs.update(u=u,t=t);sol=solve(hs)
    if sol is None:continue
    cp,de=sol
    def eq(x,y,n):assert cp[x]==cp[y]and de[x]-de[y]==n,(x,y,n)
    assert T(hs['a'])in('EWE','EWEE');eq(('v',1),('B',2),1);eq(('a',1),('B',2),2);eq(('Y',2),('B',2),3);eq(('B',3),('a',2),2)
    eq((born,1),('B',1),-3 if born=='t'else-4)
    rows.append(dict(kind=pr['kind'],lower_other='M-'+str(len(u[::2]))if um=='strict'else'M',upper_other='M-'+str(len(t[::2]))if tm=='strict'else'M',birth=born,headings={v:T(h)for v,h in hs.items()}))
ref=json.loads((D/'bit11_upper_branch_birth_ports.json').read_text());key=lambda r:(r['kind'],r['lower_other'],r['upper_other'],r['birth'],tuple(sorted(r['headings'].items())))
assert len(rows)==63 and{key(r)for r in rows}=={key(r)for r in ref['rows']}
profiles=sorted({(r['headings']['u'],r['headings']['t'],r['headings']['a'],r['lower_other'],r['upper_other'],r['birth'])for r in rows});assert len(profiles)==7
assert any(r[:3]==('EEWE','NNNS','EWEE')for r in profiles)
p=D/'K1_bit11_upper_branch_seven_birth_profiles.md';sha=hashlib.sha256(p.read_bytes()).hexdigest();assert sha=='5185ea3f901bbfebbbc0db3900c6bfe43d4ce34f92c29919db3805caea42d07f'
out=dict(status='PASS seven complete upper-branch birth profiles and exit rank3 delay',note_sha256=sha,independent_candidates=attempts,necessary_rows=rows,profiles=profiles,analytic='All complete u/t histories, matched physical edge ordinals, canonical first-boundary minimum, complete K1 order and>=4 same-cell spacing reconstruct63 rows. Birth t is exactly next main birth-3; birth u exactly next main birth-4, hence corresponding parent deadlines-8/-9. Additional complete square, not partial inventory, excludes aEEEW. B3-B2=4+(a2-a1)>=8. One-R and all-four stock escape retained.',scope='One local necessary secondary square, no exterior trace, overlapping-clock summation, strict regress, fuel charge or general K1 exclusion.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(attempts,len(rows),profiles)
