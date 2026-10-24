from pathlib import Path
from itertools import product
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23'
s=(SELF.parent/'check_K1_straight_double_max_independent.py').read_text().split('rows=[];attempts=0')[0]
extra="""
 for a,b in zip(order,order[1:]):
  if not lower(a,b,1):return None
 first=[next((v,k)for k,x in enumerate(out(hs[v]))if x==di)for v,di in [('u',0),('t',1),('a',2),('Y',3)]]
 if birth not in first:return None
 for x in first:
  if x!=birth and not lower(birth,x,1):return None
 if mode=='old':
  if not lower(('r',1),('Z',1),1):return None
 else:
  for v,di in [('r',0),('e',1),('q',3)]:
   ix=next(k for k,x in enumerate(out(hs[v]))if x==di)
   if not lower(('Z',1),(v,ix),1):return None
"""
s=s.replace("if not lower(('A',2),('B',1),1):return None",extra)
ns={'__file__':str(SELF.parent/'check_K1_straight_double_max_independent.py')};exec(s,ns)
choices=ns['choices'];O=ns['out'];solve=ns['solve'];H=lambda s:tuple('NESW'.index(c)for c in s);T=lambda h:''.join('NESW'[x]for x in h)
prior=json.loads((SELF.parent/'check_K1_upper_branch_birth_profiles_independent.json').read_text())['necessary_rows']
baseports=[('A',3,'Z'),('Z',0,'Y'),('Y',1,'B'),('B',2,'A'),('B',0,'v'),('v',3,'a'),('a',2,'Y'),('Y',3,'u'),('u',0,'t'),('t',1,'a'),('Z',2,'q'),('q',1,'h'),('h',0,'A'),('q',3,'r'),('r',0,'e'),('e',1,'Z'),('u',2,'e')]
ns['order']=[('A',1),('B',0),('A',2),('B',1),('D',0),('B',2),('D',1)]
results={}
for mode in ('old','new'):
 ns['mode']=mode;rows=[];attempts=0
 rv=[(H(x),'old')for x in ('EEW','EEWE','EEWW')]if mode=='old'else [(h,m)for m in ('strict','equal')for h in choices(3,m)]
 ev=[(h,m)for m in ('strict','equal')for h in choices(0,m)]
 for pr in prior:
  ns['ports']=baseports+([('v',1,'D')]if pr['kind']=='S'else[('v',1,'w'),('w',2,'D'),('D',3,'B')]);ns['birth']=(pr['birth'],1)
  for qh,(rh,rm),(eh,em)in product((H('SSS'),H('SSSN')),rv,ev):
   if pr['lower_other']=='M'and em!='equal':continue
   if pr['lower_other']=='M-1'and(em!='strict'or len(eh[::2])!=1):continue
   hs={v:H(x)for v,x in pr['headings'].items()};hs.update(q=qh,r=rh,e=eh,h=H('WWWE'));attempts+=1
   sol=solve(hs)
   if sol is None:continue
   cp,de=sol
   def eq(a,b,k):assert cp[a]==cp[b]and de[a]-de[b]==k,(mode,a,b,k)
   anchor=('A',1)
   for a,k in [(('Z',0),1),(('Y',0),2),(('B',0),3),(('A',2),4),(('Z',1),5),(('q',0),6)]:eq(a,anchor,k)
   ri=next(k for k,x in enumerate(rh)if x==3);eq(('r',ri),anchor,7)
   eq(('q',2),('Z',2),5)
   if mode=='old':
    assert(T(qh),T(rh),T(eh),pr['birth'])==('SSS','EEWW','SNN','u')
    for a,k in [(('e',2),8),(('Z',2),9),(('q',1),10),(('h',3),11),(('A',3),12),(('Z',3),13),(('q',2),14),(('r',3),15)]:eq(a,anchor,k)
   else:
    assert rh[0]==3
    eq(('e',next(k for k,x in enumerate(eh)if x==0)),anchor,8)
    eout=[k for k,x in enumerate(O(eh))if x==1];assert len(eout)==1 and eout[0]in(0,2)
    if eout[0]==0:
     eq(('Z',2),anchor,9)
     rsecond=[k for k,x in enumerate(rh)if x==3][1]
     # If R2 were this second W, the exact physical return spacings exclude it.
     assert rsecond%2==1
     eq(('r',rsecond),anchor,15)
    else:assert pr['birth']=='u'and T(hs['u'])in('EEW','EEWE')
   row=dict(kind=pr['kind'],birth=pr['birth'],headings={v:T(h)for v,h in hs.items()})
   if mode=='new':row['r_other']=rm
   rows.append(row)
 ref=json.loads((D/f'bit11_{mode}_first_branch_full_ports.json').read_text())
 key=lambda r:(r['kind'],r['birth'],r.get('r_other'),tuple(sorted(r['headings'].items())))
 assert {key(r)for r in rows}=={key(r)for r in ref['rows']}
 assert len(rows)==(27 if mode=='old' else 324)
 results[mode]=dict(candidates=attempts,survivors=len(rows),profiles=sorted({(r['headings']['q'],r['headings']['r'],r['headings']['e'],r['headings']['u'],r['birth'])for r in rows}))
# Direct physical literal paths, independent of the ordinal solver.
vec=(1j,1,-1j,-1)
def walk(p,h,w):
 out=[]
 for c in w:
  out.append((int(p.real),int(p.imag),h,c));h=(h+(1 if c=='R'else-1))%4;p+=vec[h]
 return p,h,out
assert walk(1,0,'LRRRRLR')[:2]==(-1-1j,3)
assert walk(0,1,'RLLLLR')[:2]==(-1-1j,3)
def minimum(d,last,forced=None):
 for n in range(1,14):
  for w in product('LR',repeat=n):
   if forced and w[0]!=forced:continue
   p,h,_=walk(0,3,w)
   if p==d and h==last:return n
 raise AssertionError
mins=[minimum(2j,1),minimum(3j,2),minimum(2j,1,'L'),minimum(3j,2,'L')]
assert mins==[4,9,8,13]
notes={'K1_bit11_branch_literal_birth_waits.md':'97d6470669cacc80db8a23f5b55c029a5a3de56984113ce051444789b20e373b','K1_bit11_two_branch_old_stock_wait.md':'d050e640edecee6ff383bf1adb486585eee5e4637304c1b56e7cb8f0351daecc','K1_bit11_branch_early_parent_or_long_wait.md':'39b74908b281f7f62c777c7844ee4003291be6f5176c73c793dc330b4c20b63b'}
for f,h in notes.items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
out=dict(status='PASS independent complete old/new two-branch ports, literal suffixes, and analytic main-birth waits',notes=notes,results=results,literal_transport_minima=mins,analytic='Canonical first-boundary birth at J is Z or negative r; e cannot supply two S entries. Old r birth is <=alpha-5, with real old Q<=alpha-10. Old and new eR0 modes reach r with actual L atalpha+15; exclusion of occupied birth ticks and literal transport give27/31. New eR2 mode has earlier S supplier uR0<=alpha-5 and actual P0 birth<=alpha-6, parent<=alpha-11. Only consecutive main-birth intervals telescope; no overlapping stock span is added.',scope='Necessary local complete-WHITE cap4 K1 bit11 max-branch conditions; no exterior realization, distinct-root charge, iteration or general K1 exclusion.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print({m:(x['candidates'],x['survivors'])for m,x in results.items()},mins)
