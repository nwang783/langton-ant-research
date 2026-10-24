#!/usr/bin/env python3
"""Literal standard104 family positive controls of compact clock producer."""
from pathlib import Path
from collections import defaultdict
import json,time
from synthesize_axis_compact_clock import make,values
from probe_one_a_local_constraints import D,mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr
from synthesize_cap_three_cylinder import check_model
root=Path(__file__).parent;word=(root.parent/'word_stabilization/standard_word.txt').read_text().strip();out=[]
for copies in (1,2,3):
 P=len(word)*copies;n=2*copies;hist=defaultdict(list);p=(1,0);h=2
 for t,ch in enumerate(word*copies):
  k=-(p[0]//n);q=p[0]%n,p[1]+k*n;hist[q].append((t-k*P,h,ch));h=(h+(1 if ch=='R' else -1))%4;a,b=D[h];p=p[0]+a,p[1]+b
 lo=min(y-x for x,y in hist);lo-=lo%2;hi=max(y-x for x,y in hist);H=hi-lo+1
 hs={(x,y-lo):tuple(h for t,h,ch in sorted(es)) for (x,y),es in hist.items()}
 fixed={(x,x+y):hs.get((x,x+y),()) for y in range(H) for x in range(n)};cap=max(map(len,fixed.values()))
 txt,ps=make(cap,copies,H,30000,'singleton',True,dy=n,fixed_override=fixed)
 base=root/f'compact_clock_standard{P}';base.with_suffix('.smt2').write_text(txt)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,txt.encode());st=time.time();ans=solve(ctx,sol);assert ans==1,ans
 mt=modelstr(ctx,getmodel(ctx,sol)).decode();base.with_suffix('.model').write_text(mt);v=values(mt);vv={'P':int(v['P'])};ss=[]
 for i,p in enumerate(ps):
  hs=fixed[p];ss.append([(''.join(map(str,hs)),[(1 if j%2==0 else -1,h) for j,h in enumerate(hs)])]);vv[f's{i}']=0
  for j in range(len(hs)):assert v[f't{i}_{j}'].denominator==1;vv[f't{i}_{j}']=int(v[f't{i}_{j}'])
 cert=check_model(vv,ps,ss,(-n,-n));assert cert['period']==P
 out.append(dict(period=P,drift=[-n,-n],cap=cap,height=H,seconds=time.time()-st,exact_replay='PASS'))
result=dict(status='AUTHOR_POSITIVE_CONTROLS_PASS',controls=out);(root/'check_compact_clock_positive.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
