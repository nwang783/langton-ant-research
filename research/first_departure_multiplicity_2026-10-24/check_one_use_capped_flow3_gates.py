"""Exact source1->3/sink3->1 RR versus RLR gates.
The GLOBAL-M all-length template reduction is a signed dependency, not a scan.
Uncapped reader controls are necessary local interfaces, not physical factors.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
b=Path(__file__).parent;L={'__file__':str(b/'check_even_reader_rail_and_merge_reset.py')};exec((b/'check_even_reader_rail_and_merge_reset.py').read_text().split('rows=[]')[0],L)
out,graph,check=L['out'],L['graph'],L['check'];X={};exec((b/'check_even_portal_entry_incidence.py').read_text().split('words=')[0],X);exact=X['exact']
rr=[]
for z,y in [('NNS','EEW'),('NNSN','EEWE')]:
 hs={(0,0):z,(1,0):'EWWW',(1,-1):'SSNS',(0,-1):y};assert check(hs)=='open'
 su,cs,order,tt=graph(hs);path=[((0,0),0),((1,0),0),((1,-1),0),((0,-1),2),((0,0),1)]
 assert all(su[e]==f for e,f in zip(path,path[1:]));assert tt[path[-1]]==tt[path[0]]+4
 if len(z)==4:assert su[((0,-1),3)]==((0,0),3)
 rr.append(dict(histories={str(p):h for p,h in hs.items()},actual_RRRR=path,components=cs,component_order=order,distinct_mod4_calendar={str(e):t for e,t in tt.items()},events=len(tt),odd_classes=sum(len(h)%2 for h in hs.values())))
# RLR core: B source, Y LEFT-three, Z sink and their reader D.
base={(1,1):'SNNN',(0,1):'EWWW',(0,0):'SSNS'};domain=[];ct=Counter();op=[]
for n in range(1,13):
 for a in product('EW',repeat=n):
  if a.count('E')!=3 or sum(out(a,r)=='N'for r in range(n))!=3:continue
  d=''.join(a);RE=sum(a[r]=='E'for r in range(0,n,2));RW=sum(a[r]=='W'for r in range(0,n,2));eps=n%2
  assert RE==RW and n==4*RE-eps and RE<=3
  hs=base|{(1,0):d};ans,cert=exact(hs);ct[ans]+=1
  row=dict(D=d,length=n,result=ans,certificate=cert);domain.append(row)
  if ans=='open':op.append(d)
  if n<=4:
   assert d in ['EEWE','WEEE'] and ans=='rank'
   path=[((0,0),3),((1,0),3),((1,1),3),((0,1),3),((0,0),3)]
   assert cert['path']==path
assert len(domain)==84 and ct=={'rank':78,'open':6}
assert op==['EWWWWEE','WWEWWEE','WWWWEEE','EWWWWEEW','WWEWWEEW','WWWWEEEW']
# Retain full six-cell chronology, not only the four-cell port shield.
full=[]
for q,C in [('EEW','SSN'),('EEWE','SSNS')]:
 for d in op:
  hs=base|{(1,2):q,(0,2):C,(1,0):d};ans=check(hs)
  row=dict(q=q,C=C,D=d,result=ans)
  if ans=='open':
   su,cs,order,tt=graph(hs);row|=dict(histories={str(p):h for p,h in hs.items()},components=cs,component_order=order,distinct_mod4_calendar={str(e):t for e,t in tt.items()},events=len(tt),odd_classes=sum(len(h)%2 for h in hs.values()))
  full.append(row)
assert Counter(r['result']for r in full)=={'open':4,'clock_cycle':8}
assert sum(r['result']=='open'and r['odd_classes']==0 for r in full)==1
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,RR_two_complete_controls=rr,RLR_uncapped_reader_count_derived_domain=domain,RLR_summary=dict(ct),RLR_open_reader_words=op,full_six_cell_reader_controls=full,warning='RR controls and higher-reader calendars have open exterior channels, no physical connectors/full quotient/periodic board; no front or renewal is certified.'),indent=2)+'\n')
print('PASS two RR complete calendars; RLR cap4 same-L3 event cycle;84 uncapped readers->6 core shields->4 complete local calendars')
