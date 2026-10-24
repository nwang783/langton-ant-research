"""Nontrivial chronology-encoding positive control and a concrete white variant.
The control uses a changed prepared profile, NOT the standard wake.
"""
from pathlib import Path
import collections,json,hashlib
import synthesize_reverse_wake_short_refinement as S
P=Path(__file__).resolve().parent
w=S.rev[:31]+'LRRRR'+S.rev[32:];rr,ep,eh=S.trace(w,(0,6),3);prof=collections.defaultdict(list)
for j,(q,h,c)in enumerate(rr):prof[S.key(q)].append((j+len(w)*(q[0]//2),c))
for z in prof.values():z.sort();assert all(a[1]!=b[1]for a,b in zip(z,z[1:]))
input_black={q for q,z in prof.items()if z[0][1]=='L'};output_black=input_black^{q for q,z in prof.items()if len(z)%2}
old=S.wake;S.wake=input_black
text,coarse,events=S.build((1,6),'all')
# Fix the exact nonidentity control, so the event ordering is exercised.
for j,c in enumerate(S.rev):
 word='LRRRR'if j==31 else c;k=S.dom[c].index(word);text+=f'(assert x{j}_{k})\n'
ctx=S.mkcontext(S.mkconfig());sol=S.mksolver(ctx);S.inc(ctx,sol);S.parse(ctx,sol,text.encode());ans=S.solve(ctx,sol);assert ans==1
(P/'reverse108_prepared_control.smt2').write_text(text)
out=dict(scope=__doc__,word=w,phase31_replacement='LRRRR',start=[0,6,3],drift=[-2,-2],period=108,charge=-8,input_black_classes=sorted(input_black),output_black_classes=sorted(output_black),read_classes=len(prof),encoding_result='SAT_EXACT_FIXED_NONIDENTITY',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'reverse108_prepared_control.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
# Forward standard word on white in the same physical sector. The same return
# coordinate convention applies because incoming W makes H drift(-2,-2).
S.rev=S.H;S.wake=set()
for kind in['identity','all']:
 text,coarse,events=S.build((1,0),kind);ctx=S.mkcontext(S.mkconfig());sol=S.mksolver(ctx);S.inc(ctx,sol);S.parse(ctx,sol,text.encode());ans=S.solve(ctx,sol)
 base=P/f'white_standard_refine_{kind}';base.with_suffix('.smt2').write_text(text)
 z=dict(scope='All104 independent legal pose-preserving length1/5/9 replacements of H, with first-read WHITE in every complete spatial orbit; no fixed image sharing.',kind=kind,result={1:'SAT_BULK_ONLY',-1:'UNSAT_FAMILY',0:'UNKNOWN'}[ans],orbit_classes=len(events),source_sha256=out['source_sha256'])
 if ans==1:
  mt=S.modelstr(ctx,S.getmodel(ctx,sol)).decode();base.with_suffix('.model').write_text(mt);v=S.values(mt);choices=[]
  for j,(p,h,c)in enumerate(coarse):
   dom=S.dom[c]if kind=='all'else[c];a=[w for k,w in enumerate(dom)if v[f'x{j}_{k}']];assert len(a)==1;choices+=a
  W=''.join(choices);r,end,h=S.trace(W,(0,0),3);pr=collections.defaultdict(list)
  for j,(q,h,c)in enumerate(r):pr[S.key(q)].append((j+len(W)*(q[0]//2),c))
  for a,l in pr.items():l.sort();assert l[0][1]=='R';assert all(x[1]!=y[1]for x,y in zip(l,l[1:]))
  z.update(word=W,images=choices,period=len(W),charge=W.count('R')-W.count('L'),endpoint=end,output_black_classes=sorted(a for a,l in pr.items()if len(l)%2))
 if ans==0:z['reason']=S.reason(ctx,sol).decode()
 base.with_suffix('.json').write_text(json.dumps(z,indent=2)+'\n');print(z)
