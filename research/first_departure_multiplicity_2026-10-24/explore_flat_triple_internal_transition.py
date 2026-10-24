"""Exact internal three-flat junction alphabet for all-length composition.
No high endpoint substitution, imposed period, or strip-length scan.
Every local reader retains complete 0..4 WHITE history. OPEN means necessary
local constraint only, not an actual board factor or simultaneous exterior.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json,time
base=Path(__file__).parent
L={'__file__':str(base/'explore_two_flat_pair_reader_closure.py')};exec((base/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],L)
H,V,rot,dom,plainprop,check=[L[k]for k in ['H','V','rot','dom','propagate','check']]
raw=(base/'flat_flow2_symbolic_row_with_odd_left.py').read_text().split('rows=[];n=0')[0].split(' d={a:0 for a in ns}')[0]+" return'open'\n";Q={};exec(raw,Q);rankcheck=Q['check']
FW={'X':'NNSS','Y':'NSSN'};LW={'O':'WEE','U':'WEEW','V':'WWEE'}
def prop(ds):
 z=plainprop(ds)
 if z is None:return None
 hs={p:a[0]for p,a in z.items()if len(a)==1}
 return z if rankcheck(hs)=='open'else None

def build(gs,fs,ls):
 spec=[]
 for i,f in enumerate(fs):
  spec.append(('R',FW[f],'flat'))
  if i<2:spec.extend(('L',LW[k],'middle')for k in ls[i])
 p=(0,0);ci='N';nodes=[]
 for j,(t,h,role)in enumerate(spec):
  h=rot(h,ci,'N'if role=='flat'else'E');co=H[(H.index(ci)+(1 if t=='R'else-1))%4]
  nodes.append(dict(cell=p,turn=t,history=h,role=role,ci=ci,co=co));p=p[0]+V[co][0],p[1]+V[co][1];ci=co
 return nodes
rows=[];stats=Counter();tm=time.time()
for gs in product(range(3),repeat=2):
 if gs==(0,0):continue
 for fs in product('XY',repeat=3):
  for ww in product('OUV',repeat=sum(gs)):
   ls=[];j=0
   for g in gs:ls.append(tuple(ww[j:j+g]));j+=g
   valid=True
   for i,g in enumerate(gs):
    if g==2 and (ls[i][1]!='V'or fs[i]!='Y'or fs[i+1]!=('Y'if ls[i][0]=='V'else'X')):valid=False
    if g==0:
     if i>0 and ls[i-1][-1]!='V':valid=False
     if i+1<len(gs)and ls[i+1][0]!='V':valid=False
   if not valid:continue
   nodes=build(gs,fs,ls);fixed={tuple(n['cell']):n['history']for n in nodes};ct=Counter();sample=[]
   if len(fixed)!=len(nodes):ct['primary_geometry']+=1
   else:
    pts=set(fixed)
    while True:
     ca={(p[0]+v[0],p[1]+v[1])for p in pts for v in V.values()}-pts
     ad={q for q in ca if sum((q[0]+v[0],q[1]+v[1])in pts for v in V.values())>=2}
     if not ad:break
     pts|=ad
    ds=prop({p:([fixed[p]]if p in fixed else dom(p))for p in sorted(pts)})
    def rec(ds):
     if all(len(v)==1 for v in ds.values()):
      hs={p:v[0]for p,v in ds.items()};a=check(hs);ct[a]+=1
      if a=='open'and not sample:sample.append({str(p):h for p,h in hs.items()})
      return
     p=min((p for p in ds if len(ds[p])>1),key=lambda p:len(ds[p]))
     for h in ds[p]:
      z=prop(ds|{p:[h]})
      if z is not None:rec(z)
    if ds is not None:rec(ds)
    else:ct['primary_pruned']+=1
   rows.append(dict(gaps=gs,flats=fs,lefts=ls,counts=dict(ct),nodes=nodes,open_sample=sample));stats.update(ct)
 print('DONE',gs,'n',len(rows),'openprim',sum(bool(r['counts'].get('open'))for r in rows),'elapsed',round(time.time()-tm,2),flush=True)
obj=dict(scope=__doc__,summary=dict(stats),primary_count=len(rows),open_primaries=sum(bool(r['counts'].get('open'))for r in rows),rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('TOTAL',dict(stats),time.time()-tm,flush=True)
