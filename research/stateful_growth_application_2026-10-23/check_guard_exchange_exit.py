#!/usr/bin/env python3
"""Exact retained V20 continuation: clear both local guards, retain garbage,
and exit at a different physical pose. No scan and no claimed next interface.
"""
from pathlib import Path
import sys,json,hashlib
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).parent
sys.path.insert(0,str(ROOT/'stateful_growth_quadratic_2026-10-23'))
from quadratic_lap_validator import Context,D
ctx=Context(max_operations=100000000)
source=HERE/'guard_exchange.json';j=json.loads(source.read_text());dom=j['domain']
B=ctx.set(j['complete_returned_relation']);V='LLRLRRRRLRRRRLLLLRLR'
stored=ROOT/'new_constructive_2026-10-23/two_layer_gap_frame_r10_k10.word.txt'
assert stored.read_text()[960:980]==V
change=ctx.set('[M,r]->{[x,y]:false}');pos=(0,0);h=1;reads=[]
def xor(a,b):return a.subtract(b).union(b.subtract(a)).coalesce()
def cell(q):return ctx.set('[M,r]->{[x=-2M+'+str(q[0])+',y='+str(q[1])+']:'+dom+'}')
for i,t in enumerate(V):
 q=cell(pos);current=B.intersect(q)
 assert(current.is_equal(q)if t=='L'else current.is_empty()),(i,pos,h,t,str(current))
 reads.append(dict(phase=i,relative=pos,heading=h,turn=t))
 B=xor(B,q);change=xor(change,q)
 h=(h+(1 if t=='R'else-1))%4;pos=(pos[0]+D[h][0],pos[1]+D[h][1])
assert pos==(-4,0)and h==3
cleared={(0,0),(0,1),(-1,2)};added={(-2,3),(-1,3),(-2,1),(-3,2),(-3,0)}
expected=ctx.set('[M,r]->{[x,y]:false}')
for q in cleared|added:expected=expected.union(cell(q))
assert change.is_equal(expected)
before=ctx.set(j['complete_returned_relation'])
for q in cleared:assert before.intersect(cell(q)).is_equal(cell(q))and B.intersect(cell(q)).is_empty()
for q in added:assert before.intersect(cell(q)).is_empty()and B.intersect(cell(q)).is_equal(cell(q))
assert B.intersect(cell((-1,0))).is_empty()
# The preceding unique minimum seed remains unchanged: all V first-read
# cells not seen before are white, so V adds no initial black requirement.
c=json.loads((HERE/'guard_exchange_M50_r51.json').read_text());seed={tuple(q)for q in c['seed']}
word=c['word']+V;actual=set(seed);p=(0,0);hh=1
for i,t in enumerate(word):
 assert('L'if p in actual else'R')==t,(i,p,hh,t)
 if p in actual:actual.remove(p)
 else:actual.add(p)
 hh=(hh+(1 if t=='R'else-1))%4;p=(p[0]+D[hh][0],p[1]+D[hh][1])
assert len(word)==1480 and len(seed)==107 and len(actual)==121 and p==(-104,0)and hh==3
assert not{(-101,0),(-100,0),(-100,1)}&actual
report=dict(status='EXACT NON-CLEAN TWO-GUARD EXIT, NOT A RENEWAL',domain=dom,
 word='W6^M J(r) V20',V20=V,retained_source_slice=[960,980],
 minimal_seed='same complete2r+5-cell seed as guard_exchange.json',duration='20M+8r+72',mass='2r+19',
 endpoint=[['-2M-4',0],3],complete_returned_relation=str(B),complete_V20_change_relation=str(change),
 V20_clears_relative_to_p=sorted(cleared),V20_adds_relative_to_p=sorted(added),reads=reads,
 control=dict(M=50,r=51,reads=len(word),initial_mass=len(seed),returned_mass=len(actual),head=p,heading=hh),
 source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 bindings={str(source.name):hashlib.sha256(source.read_bytes()).hexdigest(),str(stored.name):hashlib.sha256(stored.read_bytes()).hexdigest()},
 scope=__doc__)
(HERE/'guard_exchange_exit.json').write_text(json.dumps(report,indent=2)+'\n')
(HERE/'guard_exchange_exit_M50_r51.json').write_text(json.dumps(dict(word=word,seed=sorted(seed),returned=sorted(actual),head=p,heading=hh),indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items()if k not in('complete_returned_relation','complete_V20_change_relation','reads')},indent=2))
