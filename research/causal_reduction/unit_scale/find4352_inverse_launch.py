"""Targeted4352 inverse causal-launch connector, fixed preexisting32/150000
connector limits. No image palette, word-period or cap-radius escalation.
Only cells outside the ENTIRE4352 future READ set may be assigned initially;
exact inverse104 tail completion may use other such still-unread cells.
"""
from pathlib import Path
from collections import deque,Counter
import json,time
import inverse4352_tail_completion as T
P=Path(__file__).resolve().parent
p=T.POSE[0]-T.V[T.HEAD][0],T.POSE[1]-T.V[T.HEAD][1];h=(T.HEAD+2)%4
queue=deque([(p,h,frozenset(),frozenset(),frozenset(),'')]);count=0;depths=Counter();found=None;start=time.time();visited_states=set()
while queue and count<150000:
 p,h,edits,flips,seen,w=queue.popleft();count+=1;depths[len(w)]+=1
 goals=T.completion(p,h,edits,flips,seen)
 if goals:
  g=goals[0];extra=set(map(tuple,g['extra_initial_XOR']));finaled=set(edits)^extra
  assert all(not T.future_read(z)for z in finaled)
  found={'inverse_prefix':w,'prefix_pose':[p,h],'inverse_tail_word':g['word'],'original_H_phase':g['phase'],'initial_wave_XOR_edits':sorted(finaled),'tail_completion_extra_edits':sorted(extra),'prefix_flip_mask':sorted(flips),'prefix_reads':sorted(seen)};break
 if len(w)>=32:continue
 now=T.bulk(p)^(p in T.BASE)^(p in edits)^(p in flips)
 choices=[now]if p in seen or T.future_read(p)else[now,not now]
 for b in choices:
  ee=set(edits)
  if b!=now:ee.symmetric_difference_update({p})
  ff=set(flips);ff.symmetric_difference_update({p});hh=(h+(-1 if b else 1))%4;v=T.V[hh];q=p[0]+v[0],p[1]+v[1]
  # No independent spatial cutoff: depth32 itself bounds every coordinate.
  state=(q,hh,frozenset(ee),frozenset(ff),seen|{p})
  if state in visited_states:continue
  visited_states.add(state);queue.append((*state,w+('L'if b else'R')))
 if count%10000==0:print('nodes',count,'depth',len(w),'queued',len(queue),'seconds',time.time()-start,flush=True)
out={'scope':__doc__,'found':found,'nodes':count,'queue_remaining':len(queue),'depth_counts':dict(depths),'bounds':{'max_total_depth':32,'max_nodes':150000},'seconds':time.time()-start}
(P/'4352_inverse_launch_search.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
