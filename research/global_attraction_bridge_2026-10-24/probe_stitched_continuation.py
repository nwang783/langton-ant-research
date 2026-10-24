from pathlib import Path
import sys,json,hashlib
ROOT=Path('/workspace/shared/langton'); OUT=Path(__file__).parent
sys.path.insert(0,str(ROOT/'actual_zipper_spiral_2026-10-23'));sys.path.insert(0,str(ROOT/'computability'))
from return_guide_geometry import setup_guide,step,wwhich,cursors,xy
from check_chronological_stitched_return import ordered_path,path_word
from periodic_tail_checker import first_mismatch,State
H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
PHASE={H[i:]+H[:i]:i for i in range(104)}

def final(q):
 B,p,h,w1,P,C,G,K,U=setup_guide(q);B0=set(B);p0=p;h0=h;R1=set();labels={x:'old' for x in B}
 for ch in w1:
  assert ch==('L'if p in B else'R')
  if ch=='R':R1.add(p);labels[p]='first'
  else:labels.pop(p)
  p,h=step(B,p,h)
 vs=ordered_path(R1|C,wwhich(p,h),xy((1,-1)))
 w2='RL'+path_word(K,0)+'RRRRL'
 w3=path_word([((X+Y-2)//4,(X-Y)//4)for X,Y in vs],2)+'RLL'
 for label,w in [('transport',w2),('second',w3)]:
  for ch in w:
   assert ch==('L'if p in B else'R'),(q,label,p)
   if ch=='R':labels[p]=label
   else:labels.pop(p)
   p,h=step(B,p,h)
 return B,p,h,dict(q=q,entry=[p0,h0],final_pose=[p,h],prefix=len(w1+w2+w3),initial=sorted(B0),final=sorted(B),labels=[[x,labels[x]]for x in sorted(B)],words=[w1,w2,w3])

def probe(q,N=200000):
 B,p,h,data=final(q);seq='';first104=None;tests=0
 for t in range(N+1):
  if len(seq)>=208 and seq[-104:]==seq[-208:-104] and seq[-104:]in PHASE:
   phase=PHASE[seq[-104:]];w=H[phase:]+H[:phase];tests+=1
   bad=first_mismatch(State(frozenset(B),p,h),w)
   if bad is None:
    data.update(capture_after_final=t,capture_pose=[p,h],capture_phase=phase,tail_word=w,tail_field=sorted(B),future_word=seq,first_candidate=first104,tail_tests=tests)
    print(dict(q=q,prefix=data['prefix'],final_pose=data['final_pose'],capture=t,pose=[p,h],phase=phase,mass=len(B),tests=tests),flush=True)
    return data
   if first104 is None:first104=[t,bad]
  c='L'if p in B else'R';seq+=c;p,h=step(B,p,h)
 data.update(status='BOUND_EXHAUSTED_NOT_A_COUNTEREXAMPLE',elapsed=N,pose=[p,h],mass=len(B),first_candidate=first104,tail_tests=tests,future_word=seq)
 print({k:data[k]for k in['q','status','elapsed','pose','mass','first_candidate','tail_tests']},flush=True)
 return data
if __name__=='__main__':
 out=[probe(q)for q in(3,5,7,9,11,13)]
 (OUT/'stitched_continuation_probe.json').write_text(json.dumps(out,indent=2)+'\n')
