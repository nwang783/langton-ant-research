"""Whole maximal3 source/sink paths after the structural five-edge theorem.
Only19 exact geometric/profile templates; not a bounded period or support scan.
All unspecified exterior histories remain open.
"""
from pathlib import Path
from itertools import product
from collections import Counter
base=Path(__file__).parent
ss=(base/'flat_flow2_symbolic_row_with_odd_left.py').read_text().split('rows=[];n=0')[0]
ss=ss.replace("val={(0,-1):0};q=deque([(0,-1)])","val={(-1,0):0};q=deque([(-1,0)])")
ns={};exec(ss,ns);check=ns['check']
H='NESW';V=ns['V'];out=ns['out']
def rot(h,ci):return''.join(H[(H.index(x)+H.index(ci)-1)%4]for x in h)
templates=['RR']+['R'*a+'L'*l+'R'*b for l in[1,2]for a in[1,2]for b in[1,2]]
rows=[];counts=Counter()
for tw in templates:
 ri=[i for i,x in enumerate(tw)if x=='R'and i not in[0,len(tw)-1]]
 for bits in product(['EEEW','EWEE'],repeat=len(ri)):
  pos=(0,1);ci='E';hs={};reads=[];collision=False
  for i,turn in enumerate(tw):
   hh='EWE'if i==0 else'EEE'if i==len(tw)-1 else bits[ri.index(i)]if turn=='R'else'WEEE'
   h=rot(hh,ci)
   if pos in hs:collision=True;break
   hs[pos]=h;reads.append(dict(cell=pos,turn=turn,cycle_incoming=ci,history=h))
   co=H[(H.index(ci)+(1 if turn=='R'else-1))%4];pos=(pos[0]+V[co][0],pos[1]+V[co][1]);ci=co
  ans='physical collision'if collision else check(hs);counts[ans]+=1
  rows.append(dict(turn_word=tw,internal_RIGHT_bits=bits,result=ans,named_histories=reads))
print('19 complete maximal3 templates',dict(counts))
for r in rows:
 if r['result']=='open':print(r['turn_word'],r['internal_RIGHT_bits'])
