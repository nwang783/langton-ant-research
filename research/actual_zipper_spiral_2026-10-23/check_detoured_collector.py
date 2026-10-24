"""Adversarial no-w-cycle collector variant, charged at full finite-board cost."""
import check_collector as cc
from check_spiral import *

def detoured(q,scale=8):
 at=(0,0);ends=[at]
 for j in range(1,q+1):
  dx,dy=D[(j-1)%4];at=(at[0]+scale*((j+1)//2)*dx,at[1]+scale*((j+1)//2)*dy);ends.append(at)
 d0=D[0];points=[(0,-1)]
 for j in range(1,q):
  x,y=ends[j];dx,dy=D[(j-1)%4];ex,ey=D[j%4]
  points += [(x-ex,y-ey),(x+2*dx-ex,y+2*dy-ey),(x+2*dx+ex,y+2*dy+ey),(x+dx+ex,y+dy+ey)]
 dx,dy=D[(q-1)%4];x,y=ends[-1];points.append((x+dy,y-dx))
 out=[points[0]]
 for c,d in points[1:]:
  while out[-1]!=(c,d):
   a,b=out[-1];assert a==c or b==d
   out.append((a+(c>a)-(c<a),b+(d>b)-(d<b)))
 assert len(set(out))==len(out)
 return out

if __name__=='__main__':
 cc.collector_vertices=lambda q:detoured(q,8)
 cc.setup=lambda q,scale:setup(q,8)
 out=[cc.run(q,j)for q in(1,2,3,4,8,16,32)for j in(False,True)]
 for d in out:d['scale']=8;d['collector_style']='detoured to avoid every second corner-arm tip'
 Path(__file__).with_name('detoured_collector_controls.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps([{k:v for k,v in d.items()if k!='events'}for d in out],indent=2))
