"""Exact backward-conjugate evolution of the canonical original13-cell source.
A supplied finite board only; affine other-cap ownership is a separate check.
"""
from pathlib import Path
import sys,json,hashlib
from check_prepared1564_router_geometry import H,infer,trace
from check1564_noncrossing_producer import V
P=Path(__file__).resolve().parent;sys.path.insert(0,str(P.parents[1]/'computability'))
from periodic_tail_checker import State,first_mismatch
B=set(infer(H*30,(0,0),3)['input']);seed=set(B);p=(1,0);h=1;recent='';word=[];events=[];rot={H[i:]+H[:i]for i in range(104)}
def step():
 global p,h,recent
 c='L'if p in B else'R';B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1]);word.append(c);recent=(recent+c)[-208:];return c
while True:
 if len(recent)==208 and recent[:104]==recent[104:]and recent[104:]in rot:
  w=recent[104:];bad=first_mismatch(State(frozenset(B),p,h),w);e={'time':len(word),'pose':[p,h],'word':w,'mass':len(B),'next_mismatch':bad};events.append(e)
  print('candidate',{k:v for k,v in e.items()if k!='word'},flush=True)
  if bad is None:break
  for i in range(bad):assert step()==w[i%104]
  step();recent='';continue
 step()
 if len(word)%100000==0:print('steps',len(word),p,h,len(B),flush=True)
rows=list(trace(w,p,h));d=[rows[-1][1][i]-p[i]for i in range(2)]
out={'scope':__doc__,'source_seed':sorted(seed),'initial_reverse_pose':[[1,0],1],'word':''.join(word),'events':events,'capture_time':len(word),'capture_pose':[p,h],'capture_mass':len(B),'capture_word':w,'capture_drift':d,'final_field':sorted(B),'final_field_sha256':hashlib.sha256(json.dumps(sorted(B),separators=(',',':')).encode()).hexdigest()}
(P/'prepared1564_reverse_source.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(word),p,h,d,flush=True)
