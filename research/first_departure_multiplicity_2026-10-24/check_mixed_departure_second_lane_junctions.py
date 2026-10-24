"""Exact actual second-lane scattering of mixed2/3/4 first-R b macros.
No period, drift, width or support scan. Open exit ports remain physical ports.
"""
from pathlib import Path
from itertools import product
import json
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
def rot(h,ci):return''.join(H[(H.index(x)+H.index(ci)-1)%4]for x in h)
def rr(h,dr,kin):return[i for i in range(len(h))if(h[i]if kin=='in'else out(h,i))==dr]
def build(tw,bits,start='EWE',end='EEE'):
 rj=[i for i,x in enumerate(tw)if x=='R'and i not in[0,len(tw)-1]]
 p=(0,1);ci='E';nodes=[]
 for i,turn in enumerate(tw):
  h=rot(start if i==0 else end if i==len(tw)-1 else bits[rj.index(i)]if turn=='R'else'WEEE',ci)
  co=H[(H.index(ci)+(1 if turn=='R'else-1))%4]
  nodes.append(dict(cell=p,turn=turn,history=h,cycle_incoming=ci,cycle_outgoing=co))
  p=p[0]+V[co][0],p[1]+V[co][1];ci=co
 return nodes
def scatter(nodes):
 r=rr(nodes[0]['history'],nodes[0]['cycle_incoming'],'in')[1];route=[]
 for i,n in enumerate(nodes):
  h=n['history'];route.append(dict(vertex=i,cell=n['cell'],rank=r,incoming=h[r],outgoing=out(h,r)))
  co=n['cycle_outgoing']
  if out(h,r)!=co:
   return dict(kind='EXIT',side='RIGHT'if n['turn']=='L'else'LEFT',at_vertex=i,at_rank=r,physical_target=(n['cell'][0]+V[out(h,r)][0],n['cell'][1]+V[out(h,r)][1]),heading=out(h,r),route=route)
  j=rr(h,co,'out').index(r)
  if i==len(nodes)-1:
   assert j==1
   return dict(kind='THROUGH',output_ordinal=2,route=route)
  nxt=nodes[i+1];tr=rr(nxt['history'],co,'in');assert len(rr(h,co,'out'))==len(tr)
  r=tr[j]
 raise AssertionError
macros=[]
for tw in ['RR','RLR','RLRR','RRLR','RRLRR']:
 nn=sum(x=='R'for x in tw)-2
 for bits in product(['EEEW','EWEE'],repeat=nn):
  nodes=build(tw,bits);s=scatter(nodes)
  assert(s['kind']=='THROUGH')==(tw in['RR','RLR'])
  macros.append(dict(flow3_turn_word=tw,internal_RIGHT_histories=bits,complete_nodes=nodes,second_lane=s))
assert len(macros)==10
f4=build('RR',(),start='EWEW',end='EEEE');fs=scatter(f4);assert fs['kind']=='THROUGH'and all(r['rank']==2 for r in fs['route'])
locals=[]
for turn,h,ci,co in [('L','WWEE','E','N'),('L','WEE','E','N'),('L','WEEW','E','N'),('R','EEWW','E','S'),('R','EWWE','E','S')]:
 n=dict(cell=(0,1),turn=turn,history=h,cycle_incoming=ci,cycle_outgoing=co);s=scatter([n]);assert(s['kind']=='THROUGH')==(h=='WWEE')
 locals.append(dict(turn=turn,history=h,second_lane=s))
obj=dict(scope=__doc__,flow3_macros=macros,flow4_macro=dict(nodes=f4,second_lane=fs),flow2_internal_contacts=locals,global_conditional_obstruction='If every maximal3 macro is RR/RLR, every4 block is its isolated pair, and every remaining2 contact is LEFT V, the actual selected lane follows the entire negative b circle once. Physical clocks would give -P=ell>0. Thus some recorded EXIT junction is compulsory. No open exterior port is declared impossible or freshly fueled.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS10 three-macros + one four-block +5 two-contacts; exact through/exit scattering')
