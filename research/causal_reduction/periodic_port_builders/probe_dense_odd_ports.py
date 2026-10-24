"""Pristine controlled half-plane probes; no horizon-based renewal claims."""
import itertools,json
from pathlib import Path
ROOT=Path(__file__).parent
D=((0,1),(1,0),(0,-1),(-1,0))
def trial(r,cap=10000,rounds=100):
 q=len(r); delta=(q+1)//2; h=2*q; S=h-1;s=[S-r[(j+delta)%q] for j in range(q)]
 B=set(); steps=0; maxx=0; words=[]
 for j in range(rounds):
  x,y,hd=0,r[j%q],1;w=[]
  for k in range(cap):
   bit=(x,y) in B;w.append('L' if bit else 'R'); B.symmetric_difference_update({(x,y)})
   hd=(hd+(3 if bit else 1))%4;dx,dy=D[hd];x+=dx;y+=dy;steps+=1;maxx=max(maxx,x)
   if x<0:
    if y!=s[j%q]:return dict(completed=j,reason='WRONG_EXIT',steps=steps,maxx=maxx,actual_exit=y,words=words+[ ''.join(w)])
    words.append(''.join(w));break
   if not 0<=y<h:return dict(completed=j,reason='VERTICAL_EXIT',steps=steps,maxx=maxx,actual_exit=y,words=words+[''.join(w)])
  else:return dict(completed=j,reason='UNKNOWN_STEP_CAP',steps=steps,maxx=maxx,words=words)
 else:return dict(completed=rounds,reason='UNKNOWN_ROUND_CAP',steps=steps,maxx=maxx,words=words)
 return None
res=[]
for q in (3,5,7,9):
 delta=(q+1)//2; vals=list(range(0,2*q,2)); counts={};best=None;tested=0
 for r0 in vals[1:]:
  rd=2*q-r0
  if rd not in vals or rd==r0:continue
  remaining=[v for v in vals if v not in (r0,rd)]
  for perm in itertools.permutations(remaining):
   r=[None]*q;r[0]=r0;r[delta]=rd;it=iter(perm)
   for j in range(q):
    if r[j] is None:r[j]=next(it)
   t=trial(r);tested+=1;counts[t['reason']]=counts.get(t['reason'],0)+1
   if best is None or (t['completed'],t['steps'])>(best['completed'],best['steps']):best=dict(r=r,**t)
 res.append(dict(q=q,height=2*q,tested=tested,counts=counts,best=best))
 print(q,tested,counts,'best',best['completed'],best['steps'],flush=True)
(ROOT/'dense_odd_port_controls.json').write_text(json.dumps(res,indent=2))
