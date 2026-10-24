from pathlib import Path
from itertools import product
import hashlib,json
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'K1_pipeline_detours_2026-10-23'
s=(SELF.parent/'check_K1_straight_double_max_independent.py').read_text().split('rows=[];attempts=0')[0]
s=s.replace("if not lower(('A',2),('B',1),1):return None","\n for a,b in order:\n  if not lower(a,b,1):return None")
ns={'__file__':str(SELF.parent/'check_K1_straight_double_max_independent.py')};exec(s,ns);choices=ns['choices'];solve=ns['solve'];text=lambda h:''.join('NESW'[x]for x in h);heads=lambda s:tuple('NESW'.index(c)for c in s)
ns['ports']=[('B',0,'n'),('n',1,'p'),('p',2,'C'),('C',3,'B')];ns['order']=[(('B',2),('C',1))]
branched=[]
for mn,mp in product(('strict','equal'),repeat=2):
 if mn==mp=='strict':continue
 for n,p in product(choices(0,mn),choices(1,mp)):
  hs=dict(B=heads('EEWE'),C=heads('SSNS'),n=n,p=p)
  if solve(hs)is not None:branched.append((mn,mp,text(n),text(p)))
assert set(branched)=={('equal','equal','NNSN','EWWW'),('equal','equal','SNNN','WWEW')}
ns['ports']=[('A',3,'Z'),('Z',0,'Y'),('Y',1,'B'),('B',2,'A'),('B',0,'n'),('n',1,'p'),('p',2,'C'),('C',3,'B'),('n',3,'m'),('m',2,'Y')];ns['order']=[(('A',2),('B',1)),(('B',2),('C',1))]
rows=[]
for _,_,n,p in branched:
 for mm in('WWW','WWWE','WEWW'):
  hh=dict(A='NNSN',Z='WWWE',Y='NNNS',B='EEWE',n=n,p=p,C='SSNS',m=mm);hs={k:heads(v)for k,v in hh.items()};sol=solve(hs)
  if sol is None:continue
  cp,de=sol;anchor=('B',1)
  for v,dt in{('B',2):4,('n',0):1,('p',0):2,('C',0):3,('n',1):5}.items():assert cp[v]==cp[anchor]and de[v]-de[anchor]==dt
  seq=[('n',2),('m',1),('Y',3),('B',3),('n',3),('m',2)]
  assert all(cp[v]==cp[seq[0]]and de[v]-de[seq[0]]==i for i,v in enumerate(seq))
  rows.append(hh)
assert len(rows)==2 and{r['m']for r in rows}=={'WWW','WWWE'}and all(r['n']=='NNSN'and r['p']=='EWWW'for r in rows)
p=D/'K1_locked_RIGHT_to_max_branched_RIGHT_stock_gate.md';sha=hashlib.sha256(p.read_bytes()).hexdigest();assert sha=='b9f4b64f05d7680c431086a6d0deb3cbfea3c149681c4db127f0b05d694965b0'
out=dict(status='PASS necessary locked-RIGHT to branched-RIGHT old-stock connector',note_sha256=sha,independent_branched11_profiles=branched,surviving_rows=rows,forced_clock_offsets={'nR0':1,'pR0':2,'CR0':3,'BR2':4,'nL1':5},consecutive_route=['nR2','mL1','YL3','BL3','nL3','mR2'],birth_alternative='J lower-left m R0 choosesJ, upper-right s would need two S outputs but n has exactlyone S input. Thus negative birth is n atB(G)+5 or upper-left t, with maxparentQ(-1,3) born<=B(G).',scope='Complete WHITE cap4 K1, fixed locked row4 then RIGHT bit11 with a max branch. Two necessary m variants only, not continuous exterior realization, renewable fuel or a strictly older parent in every case.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],rows)
