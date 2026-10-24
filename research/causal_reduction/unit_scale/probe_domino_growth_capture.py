"""Exploratory template extraction only; no all-r inference from samples."""
from pathlib import Path
import json
D=((0,1),(1,0),(0,-1),(-1,0))
WORDS=['LRRL','RLLR','LRRL','RRRLLLLRLLLLRLRRRRLR','RRRRLRRRRLLLLRLLLLRL','RLLR','LRRL']
def trajectory(r,T):
 B={(x,0) for x in range(2*r+1)}|{(-1,1)};p=(0,0);h=1;out=[];poses=[]
 for t in range(T):
  poses.append((p,h));c='L' if p in B else 'R';out.append(c);B.symmetric_difference_update({p});h=(h+(1 if c=='R' else -1))%4;p=tuple(p[i]+D[h][i] for i in (0,1))
 poses.append((p,h));return ''.join(out),poses,B

def extract(r):
 w,p,B=trajectory(r,60*r+777);at=0;res=[]
 for base in WORDS:
  for j in range(at,len(w)):
   if w.startswith(base*(r-5),j):break
  else:raise ValueError((r,base,at))
  count=0
  while w.startswith(base,j+len(base)*count):count+=1
  stop=j+len(base)*count
  res.append(dict(cap=w[at:j],word=base,count=count,count_offset=count-r,start=j,end=stop,entry=p[j],exit=p[stop]));at=stop
 return dict(r=r,segments=res,tail=w[at:],tail_start=at,final_pose=p[-1])
if __name__=='__main__':
 results=[extract(r) for r in [20,30,40,80,100,160]]
 dest=Path(__file__).with_suffix('.json');dest.write_text(json.dumps({'status':'EXPLORATORY_TEMPLATE_EXTRACTION_NOT_PROOF','cases':results},indent=2))
 for d in results:
  print(d['r'],[(x['count_offset'],len(x['cap']),x['entry'],x['exit']) for x in d['segments']],len(d['tail']),d['final_pose'])
 ref=results[0]
 print('constant_cap_and_tail_match',all([x['cap'] for x in d['segments']]==[x['cap'] for x in ref['segments']] and d['tail']==ref['tail'] for d in results))
 print('caps',[x['cap'] for x in ref['segments']]);print('tail',ref['tail'])
