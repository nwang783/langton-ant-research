"""One actual parent square of a surviving strict-RIGHT ancestor.
Complete local WHITE cap4 histories and canonical birth minima only.
No off-Gamma K1 interleaving or repeated package is imposed.
"""
from pathlib import Path
from itertools import product
import json
src=Path(__file__).with_name('bit11_surviving_cleanup_Q1_parent_ports.py').read_text()
exec(src.split('\nrows=[];candidates=0\n')[0])
ss=ss.replace('def feasible(h,kind,birth,parent_birth,Qbirth):','def feasible(h,kind,birth,parent_birth,Qbirth,Rbirth):')
ss=ss.replace("('k','E','f','E')]", "('k','E','f','E'),('j','S','d0','S'),('d0','W','c0','W'),('c0','N','l0','N'),('l0','E','j','E'),('d0','E','x','E')]")
ss=ss.replace('d={x:0 for x in ns}',"pp=[next((vv,rr)for rr,z in enumerate(oh[vv])if z==oo)for vv,oo in [('c0','N'),('l0','E'),('j','S'),('d0','W')]]\n rb=(Rbirth,1)\n if rb not in pp:return\n for z in pp:\n  if z!=rb:es.append((rb,z,1))\n d={x:0 for x in ns}")
exec(ss)
def ds():
 for h,mode in ts():yield h.translate(str.maketrans('NS','SN')),mode
source=json.loads(Path(__file__).with_name('bit11_surviving_cleanup_Q1_parent_ports.json').read_text())
rows=[];candidates=0;port_compatible=0
for prior in source['rows']:
 if prior['Qbirth']!='j':continue
 for (dh,do),(ch,co),(lh,lo),pb in product(ds(),rs(),ts(),['d0','c0','l0']):
  if pb=='d0'and not dh.startswith('NNS'):continue
  if pb=='c0'and not ch.startswith('EEW'):continue
  if pb=='l0'and not lh.startswith('SSN'):continue
  hs=dict(prior['headings'],d0=dh,c0=ch,l0=lh);candidates+=1
  oh={v:out(hs[v])for v in ['j','d0','c0','l0']}
  if any(oh[v].count(o)!=hs[w].count(i)for v,o,w,i in [('j','S','d0','S'),('d0','W','c0','W'),('c0','N','l0','N'),('l0','E','j','E'),('d0','E','x','E')]):continue
  port_compatible+=1
  t=feasible(hs,prior['kind'],'u','g','j',pb)
  if t is not None:rows.append(dict(kind=prior['kind'],headings=hs,Rbirth=pb,d_other=do,c_other=co,l_other=lo,minimum_clocks=t))
r=dict(scope="Actual strict-R ancestor parent closure, including the real d0-to-x cross edge; no off-Gamma K1 ordering",candidates=candidates,port_compatible=port_compatible,count=len(rows),rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({k:v for k,v in r.items()if k!='rows'}|dict(profiles=sorted(set((r['headings']['d0'],r['headings']['c0'],r['headings']['l0'],r['Rbirth'],r['d_other'],r['c_other'],r['l_other'])for r in rows))),indent=2))
