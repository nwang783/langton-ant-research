"""Prepared BLACK singleton at the strict off-plateau helper of a late D4 route.
Every known maximum-plateau corner remains WHITE four-read. Only f is
BLACK at first read; no complete front or exterior realization is asserted.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import ast,json
root=Path(__file__).parent;base=json.loads((root/'canonical_max_face_child_ports.json').read_text())['rows'];H='NESW';V=dict(N=(0,1),E=(1,0),S=(0,-1),W=(-1,0));cp=dict(A=(1,0),Z=(0,0),Y=(0,1),B=(1,1));op=dict(A=(1,-1),Z=(-1,-1),Y=(-1,1),B=(1,1))
s=(root/'canonical_three_child_square_closure.py').read_text();tree=ast.parse(s)
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef)and x.name in['rot','pose','outs']],type_ignores=[]),'poses','exec'))
fn=next(x for x in tree.body if isinstance(x,ast.FunctionDef)and x.name=='check');ss=ast.get_source_segment(s,fn)
ss=ss.replace('def check(packages):','def check(packages):')
ss=ss.replace('ns=[(p,r)for p,h in hh.items()for r in range(len(h))];es=[]',"hh[(-2,2)]='W'\n ns=[(p,r)for p,h in hh.items()for r in range(len(h))];es=[]")
ss=ss.replace('oo={p:outs(h)for p,h in hh.items()}',"oo={p:(['S'] if p==(-2,2) else outs(h))for p,h in hh.items()}")
exec(ss)
def find(h):return next(r for r in base if r['headings']==h)
F=find(dict(A='NNSN',Z='WWEW',Y='NSSS',B='EEWE'));I=find(dict(A='NNSN',Z='WWWE',Y='NSNN',B='WEEE'))
parents=[r for r in base if r['headings']['A']=='NNSN'and r['headings']['B']=='EEWE'and all(len(x)==4 for x in r['headings'].values())]
Gs=[r for r in base if r['headings']['A']=='NNSN'and r['headings']['Z']=='WWWE'and all(len(x)==4 for x in r['headings'].values())]
rows=[];attempts=0
for j,p,g in product(parents,parents,Gs):
 if p['other']['Y']!='M-2':continue
 attempts+=1;q=check([(F,(0,0),0),(j,(-1,-1),1),(p,(-2,0),0),(I,(-1,1),3),(g,(1,1),3)])
 if q is None:continue
 hs={ast.literal_eval(k):v for k,v in q['headings'].items()};hc={ast.literal_eval(k):v for k,v in q['heights'].items()};local=[]
 for v,h in hs.items():
  black=v==(-2,2);rchars=h[1::2]if black else h[::2];lchars=h[::2]if black else h[1::2];rs=Counter(rchars);ls=Counter(lchars);x,y=v
  if h[0]in'EW':Cspec={'NE':((x,y),rs['W']),'SW':((x-1,y-1),rs['E'])};Lcount={'NW':ls['E'],'SE':ls['W']}
  else:Cspec={'NW':((x-1,y),rs['S']),'SE':((x,y-1),rs['N'])};Lcount={'NE':ls['S'],'SW':ls['N']}
  aa={hc[z]-n for z,n in Cspec.values()if z in hc};assert len(aa)==1,(v,h,Cspec,hc);a=next(iter(aa));Cs={k:a+n for k,(z,n)in Cspec.items()};Ls={k:a-n for k,n in Lcount.items()}
  assert max(Cs.values())<=0
  local.append(dict(cell=v,headings=h,initial='BLACK'if black else'WHITE',C=Cs,L=Ls))
 if min(v for z in local for v in z['L'].values()) < -3:continue
 # Exact real consecutive route u.R2 -> t.L1 -> f.singletonL -> g.L3 -> u.L3.
 assert hs[(-2,1)]=='NNNS'
 tt={ast.literal_eval(k):v for k,v in q['minimum_clocks'].items()};route=[((-1,1),2),((-1,2),1),((-2,2),0),((-2,1),3),((-1,1),3)]
 ts=[tt[v][rank]for v,rank in route];assert ts==list(range(ts[0],ts[0]+5)),ts
 rows.append(dict(J=j['headings'],P0=p['headings'],G=g['headings'],f_initial='BLACK',f_headings='W',local_levels=local,exact_route=route,route_times=ts,**q))
assert rows and all(r['P0']['Y']=='NNNS'and r['P0']['Z']=='WWWE'for r in rows)
out=dict(scope=__doc__,attempts=attempts,count=len(rows),profiles=sorted(set(tuple(r['P0'].values())for r in rows)),rows=rows)
p=root/'reverse_late_D4_black_singleton_helper.json';p.write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(rows),'strict BLACK-singleton necessary profiles; exact RLLLL route and opposite-height floor retained')
