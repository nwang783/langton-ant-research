"""Existing signed transports only: one interior recursive decoration.
A negative output is a literal same-cell repeated-turn conflict, not a bound.
"""
import json
from pathlib import Path
D=[(0,1),(1,0),(0,-1),(-1,0)]
WORDS=[('R21','LRLLLLRRRRLRRLRRLRRLL','R'),('R29','RRLLRLRRRRLRRRRLLLLRLRLLRLLRL','R'),('L29','RLLRLRRRRLRRRRLLLLRLRLLRLLRLL','L')]
def trace(w):
 x=y=h=0; out=[]
 for c in w:
  out.append((x,y,h,c));h=(h+(1 if c=='R' else -1))%4;dx,dy=D[h];x+=dx;y+=dy
 return out,(x,y,h)
def conflict(w):
 last={}; tr,end=trace(w)
 for n,(x,y,h,c) in enumerate(tr):
  if (x,y) in last and last[x,y][1]==c:
   return {'read':n,'previous':last[x,y][0],'cell':[x,y],'turn':c}
  last[x,y]=(n,c)
 return None
records=[]
for name,w,parent in WORDS:
 tr,end=trace(w)
 assert conflict(w) is None
 for j,(x,y,h,c) in enumerate(tr):
  if (h,c)!=(0,parent) or (x,y)==(0,0):continue
  U,V=w[:j],w[j+1:]
  rec={'source':name,'word':w,'recursive_read':j,'drift':[x,y],'U':U,'parent':parent,'V':V}
  for r in range(2,101):
   bad=conflict(U*r+parent+V*r)
   if bad:
    rec.update({'first_failing_depth':r,'conflict':bad});break
  else:rec['status']='literal_survivor_through_100_NOT_CERTIFIED'
  records.append(rec)
out={'scope':'only the three previously signed21/29 transports; all eligible nonzero-offset same-parent decorations','cases':len(records),'survivors':sum('status' in x for x in records),'records':records}
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
