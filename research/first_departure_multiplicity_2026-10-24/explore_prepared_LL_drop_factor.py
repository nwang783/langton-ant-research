"""Constructive literal guide for the four-cell LL bit-drop interface.
Prepared finite factor only; no translating board, complete front or renewal.
"""
from pathlib import Path
from collections import defaultdict,Counter
import json
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
segments=[
 ('B first R unit loop','RRRR',((1,1),'S')),
 ('first core strand','LRRRRL',((2,2),'N')),
 ('east guide','RRLRRLRR',((2,0),'N')),
 ('X and A first L','LL',((1,-1),'S')),
 ('second X strand','LLRRL',((4,-1),'E')),
 ('southern guide',''.join(['R','R','L','R','L','R','L','R','R','L','R','L','R','R','L','R','L','R']),((1,0),'E')),
 ('A second R and west exit','RRRLR',((-1,1),'N')),
 ('north east guide',''.join(['L','R','R','L','R','L','R','L','R','L','R','R','L','R','L','R','L','R','R']),((5,2),'W')),
 ('third X strand',''.join(['L','R','L','L','L','L','R','R','R','R','L','R','L','R','R','L','L']),((1,-1),'S'))]
p=(1,1);head='S';black=set();initial=set();seen=set();trace=[];word='';hist=defaultdict(list)
core={(1,0),(1,1),(2,0),(2,1)}
for name,ws,end in segments:
 for tr in ws:
  if p not in seen:
   if p in core:assert tr=='R',(len(word),p,head,tr,'core must start WHITE')
   if tr=='L':initial.add(p);black.add(p)
   seen.add(p)
  actual='L'if p in black else'R';assert actual==tr,(len(word),name,p,head,'wanted',tr,'actual',actual)
  hist[p].append(dict(t=len(word),incoming=head,turn=tr));before=sorted(black)
  black.symmetric_difference_update({p});nh=H[(H.index(head)+(1 if tr=='R'else-1))%4];v=V[nh];q=p[0]+v[0],p[1]+v[1]
  trace.append(dict(t=len(word),cell=p,incoming=head,turn=tr,black_before=before,black_after=sorted(black),next_cell=q,next_incoming=nh));word+=tr;p=q;head=nh
 assert (p,head)==end,(name,len(word),(p,head),'expected',end)
print('LENGTH',len(word),'turns',Counter(word),'seed',len(initial),'final',len(black),'end',p,head,'max',max(map(len,hist.values())))
for q in sorted(core):print(q,''.join(z['incoming']for z in hist[q]),''.join(z['turn']for z in hist[q]),[z['t']for z in hist[q]])
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,word=word,initial_black=sorted(initial),start=[[1,1],'S'],end=[p,head],final_black=sorted(black),trace=trace,histories={str(q):z for q,z in hist.items()},factor_max_reads=max(map(len,hist.values())),segments=[dict(name=n,word=w,end=e)for n,w,e in segments],warning='Fresh guide turns determine the explicit finite prepared seed. No repeated-word legality or full board translation is claimed.'),indent=2)+'\n')
