import json
from pathlib import Path
D=json.load(open('/workspace/shared/langton/continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json'))
def rot(p,h):
 x,y=p;return ((x,y),(y,-x),(-x,-y),(-y,x))[h]
def extend(last,p,h,word):
 new=last.copy()
 for z in word:
  dx,dy=rot(z['p'],h);q=p[0]+dx,p[1]+dy
  if new.get(q)==z['c']:return None
  new[q]=z['c']
 return new
states=[('',{},(0,0),0)]
for n in range(13):
 newstates=[]
 for w,last,p,h in states:
  m=extend(last,p,h,D['C']['trace'][:12]);
  if m is not None:
   for q in [(0,2),(1,2)]:
    dx,dy=rot(q,h);v=last.get((p[0]+dx,p[1]+dy))
    if v=='R':
     print('knownblacknose',q,w,'successors',[k for k,r in D.items() if extend(last,p,h,r['trace']) is not None]);Path(__file__).with_name('nose_counterexample.json').write_text(json.dumps({'w':w,'q':q}));raise SystemExit
  for k,r in D.items():
   ll=extend(last,p,h,r['trace'])
   if ll is not None:
    dx,dy=rot(r['end_pose'][:2],h);newstates.append((w+k,ll,(p[0]+dx,p[1]+dy),(h+r['end_pose'][2])%4))
 states=newstates
 print(n+1,len(states),flush=True)
