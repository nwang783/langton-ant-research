"""Actual older Q1 left square, with no K1 pipeline imported off Gamma.
Necessary full physical ports and canonical minima only.
"""
from pathlib import Path
from itertools import product
import ast,json
s=Path(__file__).with_name('bit11_early_L3_cleanup_next_gate_ports.py').read_text();prefix=s.split('\nrows=[];candidates=0\n')[0]
exec(prefix)
# The inherited rs()/ts() exhaust strict/equal maximizing-R histories.
ss=ss.replace("def feasible(h,kind,birth,parent_birth):", "def feasible(h,kind,birth,parent_birth,Qbirth):")
ss=ss.replace("('f','S','g','S')]", "('f','S','g','S'),('g','W','j','W'),('j','N','k','N'),('k','E','f','E')]")
ss=ss.replace('d={x:0 for x in ns}', "qq=[next((vv,rr)for rr,z in enumerate(oh[vv])if z==oo)for vv,oo in [('j','N'),('k','E'),('f','S'),('g','W')]]\n qb=(Qbirth,1)\n if qb not in qq:return\n for z in qq:\n  if z!=qb:es.append((qb,z,1))\n d={x:0 for x in ns}")
exec(ss)
rows=[];candidates=0
source=json.loads(Path(__file__).with_name('bit11_early_L3_cleanup_next_gate_ports.json').read_text())
for prior in source['rows']:
 for (jh,jother),(kh,kother),qb in product(rs(),ts(),['j','k']):
  if qb=='j'and not jh.startswith('EEW'):continue
  if qb=='k'and not kh.startswith('SSN'):continue
  hs=dict(prior['headings'],j=jh,k=kh);candidates+=1
  t=feasible(hs,prior['kind'],'u','g',qb)
  if t is not None:rows.append(dict(kind=prior['kind'],headings=hs,Qbirth=qb,jother=jother,kother=kother,minimum_clocks=t))
r=dict(scope='Actual Q1 older parent square without off-Gamma K1 assumptions',candidates=candidates,count=len(rows),rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(dict(scope=r['scope'],candidates=candidates,count=len(rows),profiles=sorted(set((x['headings']['j'],x['headings']['k'],x['Qbirth'],x['jother'],x['kother'])for x in rows))),indent=2))
