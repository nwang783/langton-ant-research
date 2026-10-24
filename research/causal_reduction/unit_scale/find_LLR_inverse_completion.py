"""Supplied LLR kernel repair followed by the old bounded connector domain.
Only the goal is strengthened: unused, future-free inverse-tail fringe cells
may be set in the initial field. No increase in depth, radius or node budget.
"""
from pathlib import Path
from collections import deque,Counter
import json,time,hashlib
import inverse_wave_tail_completion as T
P=Path(__file__).resolve().parent
rows,p,h=T.trace('LLR',(-6,-7),2);prefix_flips=frozenset(q for _,q,_,_ in rows)
queue=deque([(p,h,frozenset({(-6,-7)}),prefix_flips,prefix_flips,'LLR')]);count=0;depths=Counter();found=None;start=time.time()
while queue and count<150000:
 p,h,edits,flips,seen,w=queue.popleft();count+=1;depths[len(w)]+=1
 goals=T.completion(p,h,edits,flips,seen)
 if goals:
  g=goals[0];extra=set(map(tuple,g['extra_initial_XOR']));finaled=set(edits)^extra
  assert all(not T.future_read(z)for z in finaled)
  found={'inverse_prefix':w,'prefix_pose':[p,h],'inverse_tail_word':g['word'],'original_H_phase':g['phase'],
   'initial_wave_XOR_edits':sorted(finaled),'tail_completion_extra_edits':sorted(extra),
   'prefix_flip_mask':sorted(flips),'prefix_reads':sorted(seen)};break
 if len(w)>=32:continue
 now=T.bulk(p)^(p in T.BASE)^(p in edits)^(p in flips)
 choices=[now]if p in seen or T.future_read(p)else[now,not now]
 for b in choices:
  ee=set(edits)
  if b!=now:ee.symmetric_difference_update({p})
  ff=set(flips);ff.symmetric_difference_update({p});hh=(h+(-1 if b else 1))%4;v=T.V[hh];q=p[0]+v[0],p[1]+v[1]
  if not(-60<=sum(q)<=30 and -12<=q[0]-q[1]<=20):continue
  queue.append((q,hh,frozenset(ee),frozenset(ff),seen|{p},w+('L'if b else'R')))
out={'scope':__doc__,'found':found,'nodes':count,'queue_remaining':len(queue),'depth_counts':dict(depths),'bounds':{'max_total_depth':32,'max_nodes':150000,'u':[-60,30],'t':[-12,20]},'seconds':time.time()-start}
(P/'LLR_inverse_completion_search.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2),flush=True)
