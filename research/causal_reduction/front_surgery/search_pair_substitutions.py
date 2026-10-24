"""Exact single/pair loop substitutions, joined by original-read parity signatures."""
import sys,time,json,itertools
from collections import defaultdict,Counter
from loop_decoration_solver import walk,cl_rank,verify,HERE,standard_trace_word
from enumerate_pose_loops import loops
from standard_loop_skeleton import skeleton
N=int(sys.argv[1]) if len(sys.argv)>1 else 24
base,old,standard=skeleton();events,end=walk(base);d=end[:2];origin=[(cl_rank(p,d),i) for i,(p,h,c) in enumerate(events)]
library=loops(N);last={v:next(c for p,h,c in reversed(walk(v)[0]) if p==(0,0)) for v in library};choices={};signatures={};counts=Counter();nonstandard=[];start=time.time()
for phase,was in old.items():
 p,h,c=events[phase];cache={}
 def cellmask(q):
  if q not in cache:
   cl,a=cl_rank(q,d);cache[q]=sum((1<<j) for (cl2,a2),j in origin if cl==cl2 and (a>a2 or a==a2 and phase<=j))
  return cache[q]
 def sig(v):
  m=0
  for q,hh,cc in walk(v,(p[0],p[1],h))[0]:m^=cellmask(q)
  return m
 original=sig(was);at=defaultdict(list)
 for v in list(dict.fromkeys(['']+[v for v in library if last[v]!=c]+[was])):
  if v!=was:at[sig(v)^original].append(v)
 choices[phase]=at;signatures[phase]=dict(candidates=sum(map(len,at.values())),signatures=len(at))

def test(changes):
 counts['original_read_compatible']+=1;ll=dict(old);ll.update(changes);w=''.join(ll.get(i,'')+c for i,c in enumerate(base));ev,en=walk(w);classes=defaultdict(list)
 for t,(p,h,c) in enumerate(ev):
  cl,a=cl_rank(p,d);classes[cl].append((-a,t,c))
 for ee in classes.values():
  ee.sort()
  if any(c!=('R' if j%2==0 else 'L') for j,(_,t,c) in enumerate(ee)):return
 counts['valid_fronts']+=1
 if standard_trace_word(w,standard):counts['standard_fronts']+=1;return
 rec=dict(changes=changes,word=w,verified=verify(w));nonstandard.append(rec);print('NONSTANDARD SAT',json.dumps(rec),flush=True)
for i,at in choices.items():
 for v in at.get(0,[]):counts['single_compatible']+=1;test({i:v})
for i,j in itertools.combinations(choices,2):
 a,b=choices[i],choices[j];before=counts['original_read_compatible']
 for mask in a.keys()&b.keys():
  for v,w in itertools.product(a[mask],b[mask]):test({i:v,j:w})
 print('PAIR',i,j,'candidates',counts['original_read_compatible']-before,'seconds',time.time()-start,flush=True)
out=dict(library_max=N,library_size=len(library),backbone=base,options=signatures,counts=dict(counts),seconds=time.time()-start,nonstandard=nonstandard)
print('COMPLETE',json.dumps(out),flush=True);(HERE/f'pair_substitutions{N}_result.json').write_text(json.dumps(out,indent=2))
