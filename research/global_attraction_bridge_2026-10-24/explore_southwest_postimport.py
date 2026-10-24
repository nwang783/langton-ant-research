from pathlib import Path
import json
from check_return_permanent_output_debt import DXY,future
P=Path(__file__).parent;j=json.loads((P/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());w=json.loads((P/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text())['W'];phases={w[i:]+w[:i]for i in range(104)};out=[]
for control in j['controls']:
 n=control['n'];B={tuple(q):i for i,q in enumerate(control['whole_post_event_black'])};p,h=control['post_event_pose'];p=tuple(p);words=[];result=None
 for t in range(200000):
  old=B.pop(p,None)
  if old is None:B[p]=100000+t;h=(h+1)%4;c='R'
  else:h=(h-1)%4;c='L'
  words.append(c);p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
  if(t+1)%104==0 and t>=311:
   a=''.join(words[-104:])
   if a in phases and ''.join(words[-312:])==a*3:
    try:fw,dr,dead,tests=future(B,p,h)
    except AssertionError:continue
    if fw not in phases:continue
    result=dict(n=n,reads=t+1,pose=[p,h],relative_pose=[p[0]-206,p[1]-229,h],complete_tail_black=sorted(B),tail_word=fw,drift=dr,parity_tests=tests,word=''.join(words));break
 print('n',n,'tail',None if result is None else{k:v for k,v in result.items()if k not in['complete_tail_black','tail_word','word']},flush=True)
 out.append(result or dict(n=n,status='UNKNOWN bounded200000postimport reads'))
(P/'SOUTHWEST_POSTIMPORT_EXPLORATORY.json').write_text(json.dumps(dict(status='UNSIGNED named future probes only',controls=out),indent=2)+'\n')
