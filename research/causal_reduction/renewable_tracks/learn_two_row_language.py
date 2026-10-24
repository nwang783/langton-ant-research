"""Finite residual-language discovery only; no extrapolation to all widths."""
from two_row_right_cap import *
from array import array
N=int(sys.argv[1]) if len(sys.argv)>1 else 10;t0=time.time();codes={'S_ESCAPE':0,'W20_ESCAPE':1,'HEIGHT_EXIT':2,'UNKNOWN':3};counts=Counter();outputs=bytearray(1<<(2*N));unknown=[]
cached=HERE/f'two_row_outcomes_width{N}.bin'
if cached.exists():
 outputs=bytearray(cached.read_bytes());counts=Counter({st:outputs.count(v) for st,v in codes.items()})
else:
 for p in range(len(outputs)):
  st,w,ret,en=run_two(p,N);outputs[p]=codes[st];counts[st]+=1
  if st=='UNKNOWN':unknown.append(p)
  if p and p%65536==0:print('INPUTS',p,'seconds',time.time()-t0,flush=True)
 (HERE/f'two_row_outcomes_width{N}.bin').write_bytes(outputs)
# S_d(p) captures the outcomes under every suffix of length <=d.
# Here p ranges over prefixes of varying fixed lengths; trailing zeros implicit.
prev=[array('I',list(outputs[:1<<(2*l)])) for l in range(N+1)];rows=[]
for d in range(1,N+1):
 ids={};nexts=[];bylen=[]
 for l in range(N-d+1):
  arr=array('I');step=1<<(2*l)
  for p in range(step):
   sig=(outputs[p],*(prev[l+1][p+a*step] for a in range(4)))
   if sig not in ids:ids[sig]=len(ids)
   arr.append(ids[sig])
  nexts.append(arr);bylen.append(len(set(arr)))
 rows.append(dict(suffix_depth=d,distinct_residuals=len(ids),counts_by_prefix_length=bylen))
 print('RESIDUAL',rows[-1],flush=True);prev=nexts
out=dict(width=N,counts=dict(counts),unknown=unknown,residuals=rows,seconds=time.time()-t0)
(HERE/f'two_row_language_width{N}.json').write_text(json.dumps(out,indent=2));print('DONE',out['counts'],time.time()-t0,flush=True)
