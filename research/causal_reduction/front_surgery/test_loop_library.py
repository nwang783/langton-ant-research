import sys,json
from loop_decoration_solver import *
from enumerate_pose_loops import loops
N=int(sys.argv[1]) if len(sys.argv)>1 else 12
library=loops(N);w=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
st=[]
for c in w:
 if st and st[-1][0]==c:
  a,n=st.pop();n+=1
  if n<4:st.append((a,n))
 else:st.append((c,1))
r=''.join(a*n for a,n in st)
T=json.loads((ROOT/'continuation_2026-10-22/ant_continuation/factor_language/no_pair_graph_result.json').read_text())
t=next(c['word'] for c in T['cyclic'] if c['size']==24)
out=[]
for name,base,nonzero in [('reduced_standard',r,False),('T24',t,False),('standard',w,True)]:
 o,eq,g,d=build(base,library=library);z,ans=solve(eq,g,nonzero,timeout=120)
 z.update(name=name,backbone=base,loop_max_length=N,library_size=len(library),nonzero=nonzero)
 if ans is not None:z['word']=assemble(base,o,ans);z['verified']=verify(z['word']);z['choices']=[o[i] for i,v in enumerate(ans) if v]
 out.append(z);print(json.dumps(z),flush=True);(HERE/f'loop_library{N}_results.json').write_text(json.dumps(out,indent=2))
