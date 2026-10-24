#!/usr/bin/env python3
"""Discovery-only exact endpoint-chronology relaxation of one g8 inventory."""
from probe_g8_cycle_static_flow import *
from itertools import combinations,product
from pathlib import Path

def setup():
 _,pts,O,vv=make_flow();raw=Path(__file__).with_name('probe_g8_cycle_static_flow.model').read_text();m={a:int(b)for a,b in re.findall(r'(\w+) -> (\d+)',raw)};P=m['P'];opts=[]
 for i,p in enumerate(pts):
  axis=sum(p)%2;n=sum(m[f'v{i}_{c}_{h}']for c in('R','L')for h in(axis,axis+2));os=[]
  for rr,ll in product(combinations(range(0,n,2),m[f'v{i}_R_{axis}']),combinations(range(1,n,2),m[f'v{i}_L_{axis}'])):
   plus=set(rr)|set(ll);os.append(tuple(axis if j in plus else axis+2 for j in range(n)))
  opts.append(os)
 # Pin the supplied E-cycle and the selected adjacent row, not arbitrary alternatives.
 for i,hs in {0:(3,),1:(3,),2:(2,2,0),3:(2,2,0),4:(1,1,3,3,3),5:(1,1,3,3)}.items():opts[i]=[hs]
 return P,pts,opts,O

def make(full=False):
 P,pts,opts,O=setup();d=(2,-2);ix={p:i for i,p in enumerate(pts)};lines=['(set-logic QF_LIA)','(set-option :timeout 30000)'];n=[len(os[0])for os in opts]
 def add(x):lines.append('(assert '+x+')')
 def choose(i,ks):
  terms=[f't{i}_{k}'for k in ks];s=terms[-1]
  for z in range(len(terms)-2,-1,-1):
   if terms[z]!=s:s=f'(ite (= s{i} {z}) {terms[z]} {s})'
  return s
 phasegroups={j:[]for j in range(4)}
 for i,p in enumerate(pts):
  lines.append(f'(declare-fun s{i} () Int)');add(f'(and (<= 0 s{i}) (< s{i} {len(opts[i])}))')
  for j in range(n[i]):
   lines.append(f'(declare-fun t{i}_{j} () Int)');add(f'(= (mod t{i}_{j} 4) {(2*p[0]-sum(p)%2+1)%4})');phasegroups[(2*p[0]-sum(p)%2+1)%4].append(f'(mod t{i}_{j} {P})')
   if j:add(f'(>= (- t{i}_{j} t{i}_{j-1}) 4)')
 for v in phasegroups.values():add('(distinct '+' '.join(v)+')')
 add('(= t0_0 0)')
 for i,p in enumerate(pts):
  for h in range(4):
   src=[[j for j,hi in enumerate(hs)if(hi+(1 if j%2==0 else-1))%4==h]for hs in opts[i]];m=len(src[0]);assert all(len(s)==m for s in src)
   if not m:continue
   q,k=quotient((p[0]+D[h][0],p[1]+D[h][1]),d);ii=ix[q];dst=[[j for j,hi in enumerate(hs)if hi==h]for hs in opts[ii]];assert all(len(s)==m for s in dst)
   for ordinal in range(m):
    a=choose(i,[s[ordinal]for s in src]);b=choose(ii,[s[ordinal]for s in dst]);eq=f'(= (+ {a} 1) (+ {b} {k*P}))'
    add(eq if full else f'(=> (or (= {a} t{i}_0) (= {b} t{ii}_{n[ii]-1})) {eq})')
 return '\n'.join(lines),P,pts,opts,O
if __name__=='__main__':
 full='--full'in sys.argv;text,P,pts,opts,O=make(full);ctx=mkcontext(mkconfig());s=mksolver(ctx);inc(ctx,s);parse(ctx,s,text.encode());t=time.time();ans=solve(ctx,s);print(ans,time.time()-t,flush=True)
 if ans==1:
  raw=modelstr(ctx,getmodel(ctx,s)).decode();Path(__file__).with_name('g8_extremal_inventory_endpoint.model').write_text(raw);print(raw)
