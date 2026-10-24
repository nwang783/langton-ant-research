#!/usr/bin/env python3
import sys,time,json
sys.setrecursionlimit(30000)
D=((0,1),(1,0),(0,-1),(-1,0))
def test(mass,nodecap=2000000,depthcap=2000):
 reads={}; word=[]; nodes=0; longest=''; status=None; leaves=0
 def go(x,y,h,fuel):
  nonlocal nodes,longest,status,leaves
  nodes+=1
  if len(word)>len(longest):longest=''.join(word)
  if nodes>=nodecap:status='NODE_CAP_UNKNOWN';return
  if len(word)>=depthcap:status='DEPTH_CAP_UNKNOWN';return
  v=reads.get((x,y))
  if v and v[0]>=3:leaves+=1;return
  opts=(-v[1],) if v else ((1,-1) if fuel else (1,))
  for c in opts:
   reads[x,y]=(v[0]+1,c) if v else (1,c)
   word.append('R' if c==1 else 'L');hh=(h+c)%4;dx,dy=D[hh]
   go(x+dx,y+dy,hh,fuel-int(v is None and c==-1))
   word.pop()
   if v:reads[x,y]=v
   else:del reads[x,y]
   if status:return
 go(0,0,0,mass)
 return dict(mass=mass,status=status or'EXHAUSTED',nodes=nodes,leaves=leaves,max_reads=len(longest),longest=longest)
if __name__=='__main__':
 out=[]
 for m in range(9):
  r=test(m);out.append(r);print(json.dumps({k:v for k,v in r.items() if k!='longest'}),flush=True)
  open(__file__.replace('.py','.json'),'w').write(json.dumps(out,indent=2)+'\n')
  if r['status']!='EXHAUSTED':break
