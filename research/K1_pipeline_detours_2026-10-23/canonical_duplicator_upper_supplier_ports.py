"""Actual upper maximum supplier at the unique rank3 duplicator.
No K1 interleaving, successor geometry or repeated package is imposed.
"""
from pathlib import Path
from itertools import product
import ast,json
source=Path(__file__).with_name('canonical_max_face_child_ports.py').read_text();tree=ast.parse(source)
H='NESW'
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef)and x.name in ['out','histories']],type_ignores=[]),'helpers','exec'))
base=dict(A='NNSN',Z='WWEW',Y='NSSS',B='EEWE')
def feasible(h,birth):
 ns=[(v,r)for v in h for r in range(len(h[v]))];es=[]
 for v in h:
  for r in range(len(h[v])-1):es.append(((v,r),(v,r+1),4))
 oh={v:out(s)for v,s in h.items()}
 ports=[('A','W','Z','W'),('Z','N','Y','N'),('Y','E','B','E'),('B','S','A','S'),('Y','W','u','W'),('u','N','t','N'),('t','E','a','E'),('a','S','Y','S'),('B','N','v','N'),('v','W','a','W')]
 for x,o,y,i in ports:
  aa=[(x,r)for r,z in enumerate(oh[x])if z==o];bb=[(y,r)for r,z in enumerate(h[y])if z==i]
  if len(aa)!=len(bb):return
  for x1,y1 in zip(aa,bb):es.extend([(x1,y1,1),(y1,x1,-1)])
 for boundary,b in [([('A','W'),('Z','N'),('Y','E'),('B','S')],('A',1)),([('u','N'),('t','E'),('a','S'),('Y','W')],(birth,1))]:
  ff=[next(((v,r)for r,z in enumerate(oh[v])if z==o),None)for v,o in boundary]
  if None in ff or b not in ff:return
  for x in ff:
   if x!=b:es.append((b,x,1))
 # B.L1 is an actual canonical child birth, earlier than other known G boundary ports.
 vv=next(((('v',r))for r,z in enumerate(oh['v'])if z=='E'),None)
 if vv is None:return
 es.append((('B',1),vv,1))
 d={x:0 for x in ns}
 for _ in ns:
  change=False
  for x,y,k in es:
   if d[y]<d[x]+k:d[y]=d[x]+k;change=True
  if not change:break
 else:return
 off=d['A',1];return{v:[d[v,r]-off for r in range(len(h[v]))]for v in h}
rows=[];candidates=0
for (uh,uo),(th,to),(ah,ao),(vh,vo),birth in product(histories('W'),histories('N'),histories('E'),histories('N'),['u','t','a']):
 if ao!=vo:continue
 if birth=='u'and not uh.startswith('EEW'):continue
 if birth=='t'and not th.startswith('SSN'):continue
 if birth=='a'and not ah.startswith('WWE'):continue
 h=dict(base,u=uh,t=th,a=ah,v=vh);candidates+=1
 if any(out(h[x]).count(o)!=h[y].count(i)for x,o,y,i in [('Y','W','u','W'),('u','N','t','N'),('t','E','a','E'),('a','S','Y','S'),('B','N','v','N'),('v','W','a','W')]):continue
 ts=feasible(h,birth)
 if ts is not None:rows.append(dict(headings=h,birth=birth,u_other=uo,t_other=to,a_other=ao,minimum_clocks=ts))
r=dict(scope=__doc__,candidates=candidates,count=len(rows),rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n')
profiles=sorted(set((x['headings']['u'],x['headings']['t'],x['headings']['a'],x['headings']['v'],x['birth'],x['u_other'],x['t_other'],x['a_other'])for x in rows))
print(json.dumps({k:v for k,v in r.items()if k!='rows'}|dict(profiles=profiles),indent=2))
