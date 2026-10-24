"""Meet-in-the-middle exact search over independent pose-loop replacements."""
import itertools,sys,json,time
from collections import defaultdict,Counter
from loop_decoration_solver import *
from enumerate_pose_loops import loops
from standard_loop_skeleton import skeleton

N=int(sys.argv[1]) if len(sys.argv)>1 else 12
base,old,standard=skeleton();small=loops(N);libraries={i:list(dict.fromkeys(small+[v])) for i,v in old.items()}
opts,eq,guards,d=build(base,library=libraries,onehot=False);groups=defaultdict(list)
for q,o in enumerate(opts):groups[o['phase']].append(q)
groups={i:[None]+qs for i,qs in sorted(groups.items())}
sig={q:sum(((m>>q)&1)<<j for j,(m,b) in enumerate(eq)) for q in range(len(opts))};sig[None]=0
rhs=sum(b<<j for j,(m,b) in enumerate(eq));left=list(groups.values())[:3];right=list(groups.values())[3:]
print('SETUP',len(base),len(opts),'groups',[len(x) for x in groups.values()],'left',__import__('math').prod(map(len,left)),'right',__import__('math').prod(map(len,right)),flush=True)
L=defaultdict(list)
for combo in itertools.product(*left):
 z=0
 for q in combo:z^=sig[q]
 L[z].append(combo)
print('LEFT signatures',len(L),'maximum bucket',max(map(len,L.values())),flush=True)
counts=Counter();found=[];begin=time.time()
for combo in itertools.product(*right):
 z=rhs
 for q in combo:z^=sig[q]
 counts['right_combinations']+=1
 for pre in L.get(z,[]):
  chosen=[q for q in pre+combo if q is not None];mask=sum(1<<q for q in chosen);counts['unconditional_matches']+=1
  if any((m&mask).bit_count()%2!=b for q in chosen for m,b in guards[q]):continue
  counts['all_guard_matches']+=1;ans=[int(q in chosen) for q in range(len(opts))];word=assemble(base,opts,ans);v=verify(word)
  isstandard=standard_trace_word(word,standard)
  if not isstandard:
   rec=dict(word=word,verified=v,choices=[opts[q] for q in chosen]);found.append(rec);print('NONSTANDARD SAT',json.dumps(rec),flush=True)
  else:counts['standard_solutions']+=1
 if counts['right_combinations']%50000==0:print('PROGRESS',dict(counts),'seconds',time.time()-begin,flush=True)
result=dict(loop_library_max=N,backbone=base,original_loops=old,variables=len(opts),group_sizes=[len(x) for x in groups.values()],left_signatures=len(L),counts=dict(counts),seconds=time.time()-begin,nonstandard=found)
print('COMPLETE',json.dumps(result),flush=True);(HERE/f'skeleton_mitm{N}_result.json').write_text(json.dumps(result,indent=2))
