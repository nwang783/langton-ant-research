import sys,json,time
from loop_decoration_solver import *
standard=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];out=[]
for k in range(1,int(sys.argv[1])+1):
 w=standard*k;o,eq,g,d=build(w,True);r,ans=solve(eq,g,True,timeout=30);r.update(backbone_periods=k,drift=d)
 if ans is not None:r['word']=assemble(w,o,ans);r['verified']=verify(r['word']);r['standard']=standard_trace_word(r['word'],standard)
 out.append(r);print(json.dumps(r),flush=True);(HERE/'period_multiplied_decorations.json').write_text(json.dumps(out,indent=2))
