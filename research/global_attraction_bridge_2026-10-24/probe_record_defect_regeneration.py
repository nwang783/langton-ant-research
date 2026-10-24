import json
from pathlib import Path
P=Path(__file__).parent
A=json.loads((P/'OUTWARD_RECORD_GUARDS_CHECKED.json').read_text());R=A['normal_catalog'][2]['records'];D=((0,1),(1,0),(0,-1),(-1,0));r=R[0];J=set(map(tuple,r['required_black']));free=[tuple(x['flip_cell'])for x in r['fresh_first_return_comparison']['one_bit_controls']]
allout=[]
for x in free:
 B=J^{x};born={q:('initial',q)for q in B};p=(0,0);h=1;mx=-1;retired=set();records=[]
 for t in range(4000):
  if p[0]-p[1]>mx:
   mx=p[0]-p[1];gs=[]
   for a in R:
    if a['normalized_heading']!=h:continue
    G=set(map(tuple,a['old_guard']));want=set(map(tuple,a['required_black']));cur={q for q in G if (p[0]+q[0],p[1]+q[1])in B};bad=cur^want
    if len(bad)<=2:
     gs.append(dict(phase=a['phase'],bad=[dict(offset=q,current_black=q in cur,birth=born.get((p[0]+q[0],p[1]+q[1])))for q in sorted(bad)]))
   records.append(dict(t=t,p=p,h=h,level=mx,near=gs,retired=len(retired)))
  if p in B:
   if born[p][0]=='initial':retired.add(born[p][1])
   B.remove(p);born.pop(p);h=(h-1)%4
  else:B.add(p);born[p]=('R',t);h=(h+1)%4
  p=(p[0]+D[h][0],p[1]+D[h][1])
 near=[r for r in records if r['near']]
 reps=[]
 for r1,r2 in zip(near,near[1:]):
  for a in r1['near']:
   for b in r2['near']:
    if a['phase']==b['phase']and [c['offset']for c in a['bad']]==[c['offset']for c in b['bad']] and a['bad'] and r1['retired']==r2['retired']:
     reps.append([r1,r2])
 print('flip',x,'records',len(records),'near',[(r['t'],r['level'],[(a['phase'],[b['offset']for b in a['bad']])for a in r['near']])for r in near[:15]],'reps',len(reps),flush=True)
 allout.append(dict(flip=x,records=records,repeated_defect_no_initial_retirement=reps))
(P/'RECORD_DEFECT_REGENERATION_PROBE.json').write_text(json.dumps(allout,indent=2)+'\n')
