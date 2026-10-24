"""A distinct finite-fuel local alphabet: the actual52-step blank excursion returning to its
white origin and original heading, not a longer exhaustive turn-image inventory. Tests only
identity or that one anchored excursion at each standard104 coarse read.
"""
from pathlib import Path
import json,collections,hashlib
import synthesize_reverse_wake_short_refinement as S
from probe_perpendicular_highway_wake import step
P=Path(__file__).resolve().parent
B=set();p=(0,0);h=0;loop=''
for _ in range(52):p,h,c=step(B,p,h);loop+=c
assert(p,h,len(B))==((0,0),0,12)
images={'R':['R',loop+'R'],'L':['L','L'+loop]}
for c,dom in images.items():
 target=(1,0,1)if c=='R'else(-1,0,3)
 assert S.legal_image(dom[1],target)
 r,e,g=S.trace(dom[1],(0,0),0);first={};last={}
 for q,hh,t in r:
  if q not in first:first[q]=t
  if q in last:assert last[q]!=t
  last[q]=t
 assert {q for q,t in first.items()if t=='L'}==(set()if c=='R'else{(0,0)})
S.rev=S.H;S.wake=set();S.dom=images
text,coarse,events=S.build((1,0),'all');base=P/'blank_return_refinement';base.with_suffix('.smt2').write_text(text)
ctx=S.mkcontext(S.mkconfig());s=S.mksolver(ctx);S.inc(ctx,s);S.parse(ctx,s,text.encode());ans=S.solve(ctx,s)
out=dict(scope=__doc__,blank_loop=loop,blank_loop_length=52,blank_loop_output_mass=12,images=images,result={1:'SAT_BULK_ONLY',-1:'UNSAT_ARCHITECTURE',0:'UNKNOWN'}[ans],orbit_classes=len(events),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
if ans==1:
 mt=S.modelstr(ctx,S.getmodel(ctx,s)).decode();base.with_suffix('.model').write_text(mt);v=S.values(mt);choices=[next(w for k,w in enumerate(images[c])if v[f'x{j}_{k}'])for j,(_,_,c)in enumerate(coarse)];w=''.join(choices);r,end,head=S.trace(w,(0,0),3);assert(end,head)==((-2,-2),3)
 pr=collections.defaultdict(list)
 for j,(q,hh,c)in enumerate(r):pr[S.key(q)].append((j+len(w)*(q[0]//2),c))
 for l in pr.values():l.sort();assert l[0][1]=='R';assert all(a[1]!=b[1]for a,b in zip(l,l[1:]))
 out.update(word=w,length=len(w),images_chosen=choices,output_black_classes=sorted(a for a,l in pr.items()if len(l)%2))
if ans==0:out['reason']=S.reason(ctx,s).decode()
base.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
