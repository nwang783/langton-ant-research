"""Challenge standard attraction by exact front synthesis after backbone edits."""
import sys,json,time,itertools,math
from collections import defaultdict,Counter
from loop_decoration_solver import *
from enumerate_pose_loops import loops
from standard_loop_skeleton import skeleton
N=int(sys.argv[1]) if len(sys.argv)>1 else 12
K=int(sys.argv[2]) if len(sys.argv)>2 else 2
base,old,standard=skeleton();small=loops(N);libraries={i:list(dict.fromkeys(small+[v])) for i,v in old.items()};counts=Counter();records=[];new=[];begin=time.time()
for change in itertools.chain([()],itertools.combinations(range(len(base)),K)):
 core=''.join(('L' if c=='R' else 'R') if i in change else c for i,c in enumerate(base));ev,end=walk(core)
 if end[:2]==(0,0):counts['zero_drift_skipped']+=1;continue
 opts,eq,guards,d=build(core,library=libraries,onehot=False);groups=defaultdict(list)
 for q,o in enumerate(opts):groups[o['phase']].append(q)
 groups={i:[None]+qs for i,qs in sorted(groups.items())}
 sig={q:sum(((m>>q)&1)<<j for j,(m,b) in enumerate(eq)) for q in range(len(opts))};sig[None]=0;rhs=sum(b<<j for j,(m,b) in enumerate(eq));basis={}
 for x in sig.values():add_row(basis,x,0)
 counts['translating_cores']+=1
 if reduce_row(rhs,0,basis)[0]:counts['linear_inconsistent']+=1;continue
 left=list(groups.values())[:3];right=list(groups.values())[3:];L=defaultdict(list)
 for combo in itertools.product(*left):
  z=0
  for q in combo:z^=sig[q]
  L[z].append(combo)
 hits=valid=0
 for combo in itertools.product(*right):
  z=rhs
  for q in combo:z^=sig[q]
  for pre in L.get(z,[]):
   chosen=[q for q in pre+combo if q is not None];mask=sum(1<<q for q in chosen);hits+=1
   if any((m&mask).bit_count()%2!=b for q in chosen for m,b in guards[q]):continue
   valid+=1;ans=[int(q in chosen) for q in range(len(opts))];word=assemble(core,opts,ans);cert=verify(word)
   if standard_trace_word(word,standard):counts['standard_solutions']+=1
   else:
    rec=dict(changed_phases=change,core=core,word=word,verified=cert,choices=[opts[q] for q in chosen]);new.append(rec);print('NONSTANDARD SAT',json.dumps(rec),flush=True)
 counts['original_read_compatible']+=hits;counts['valid_fronts']+=valid
 rec=dict(changed_phases=change,drift=d,unconditional_matches=hits,valid_fronts=valid);records.append(rec)
 if counts['translating_cores']%20==0:print('PROGRESS',dict(counts),'seconds',time.time()-begin,flush=True)
result=dict(loop_max=N,changed_turn_count=K,backbone=base,counts=dict(counts),seconds=time.time()-begin,nonlinear_cases=records,nonstandard=new)
print('COMPLETE',json.dumps(result),flush=True);(HERE/f'core_{K}flip{N}_result.json').write_text(json.dumps(result,indent=2))
