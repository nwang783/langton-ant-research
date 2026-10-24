"""Discovery: exact joining of two high macros across ONE or TWO flow2 V contacts.
Macrolibrary is RR3, RLR3, isolated RR4. Fixed whole junctions, no length,
period, radius or full-front scan. Complete missing corner histories <=4.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json,time
base=Path(__file__).parent;lib={'__file__':str(base/'explore_two_flat_pair_reader_closure.py')};exec((base/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],lib)
H=lib['H'];V=lib['V'];out=lib['out'];rot=lib['rot'];dom=lib['dom'];prop=lib['propagate']
src=(base/'flat_flow2_symbolic_row_with_odd_left.py').read_text().split('rows=[];n=0')[0];src=src.split(' adj=defaultdict(list)')[0]+' return\'open\'\n';ck={};exec(src,ck);check=ck['check']
macros={'RR3': [('R','EWE'),('R','EEE')], 'RLR3':[('R','EWE'),('L','WEEE'),('R','EEE')], 'RR4':[('R','EWEW'),('R','EEEE')]}
def build(a,b,s):
 specs=macros[a]+[('L','WWEE')]*s+macros[b];p=(0,1);ci='E';nodes=[]
 for t,h in specs:
  h=rot(h,ci);co=H[(H.index(ci)+(1 if t=='R'else-1))%4]
  nodes.append(dict(cell=p,turn=t,history=h,ci=ci,co=co));p=p[0]+V[co][0],p[1]+V[co][1];ci=co
 return nodes
stats=Counter();rows=[];t=time.time()
for a,b,s in product(macros,macros,[1,2]):
 nodes=build(a,b,s);fixed={tuple(n['cell']):n['history']for n in nodes};pts=set(fixed)
 if len(fixed)<len(nodes):
  print('COINCIDENT',a,b,s,nodes,flush=True);continue
 while True:
  cand={(p[0]+v[0],p[1]+v[1])for p in pts for v in V.values()}-pts
  add={q for q in cand if sum((q[0]+v[0],q[1]+v[1])in pts for v in V.values())>=2}
  if not add:break
  pts|=add
 ds=prop({p:([fixed[p]]if p in fixed else dom(p))for p in sorted(pts)})
 counts=Counter();good=[]
 def rec(ds):
  if all(len(v)==1 for v in ds.values()):
   hs={p:v[0]for p,v in ds.items()};verdict=check(hs);counts[verdict]+=1
   if verdict=='open':good.append({str(p):h for p,h in hs.items()})
   return
  p=min((p for p in ds if len(ds[p])>1),key=lambda p:len(ds[p]))
  for h in ds[p]:
   nd=prop(ds|{p:[h]})
   if nd is not None:rec(nd)
 if ds is None:counts['PORT_AT_START']+=1
 else:rec(ds)
 rows.append(dict(A=a,B=b,separator=s,nodes=nodes,corner_closure=sorted(pts),counts=dict(counts),open=good));stats.update(counts);print(a,b,s,'cells',len(pts),dict(counts),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,summary=dict(stats),rows=rows),indent=2)+'\n');print('DONE',dict(stats),time.time()-t)
