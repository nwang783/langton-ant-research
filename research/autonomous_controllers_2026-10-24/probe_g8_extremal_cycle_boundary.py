#!/usr/bin/env python3
"""Discovery only: exact one-row completion of the g8 E-cycle4 boundary."""
import sys,json,re,time
from itertools import product
from check_extremal_read_coupling import ROOT,D,quotient
sys.path.insert(0,str(ROOT/'periodic_classification_new'))
from probe_one_a_local_constraints import mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr

def options():
 out=[]
 for n in (4,5,8,9):
  for hs in product((1,3),repeat=n):
   if sum(h==1 for h in hs)!=2:continue
   if sum((h+(1 if j%2==0 else-1))%4==2 for j,h in enumerate(hs))!=2:continue
   out.append(hs)
 return out

def make():
 d=(2,-2);pts=[(0,-1),(1,-2),(0,0),(1,-1),(0,1),(1,0)];opts=[[(3,)],[(3,)],[(2,2,0)],[(2,2,0)],options(),options()];ix={p:i for i,p in enumerate(pts)}
 lines=['(set-logic QF_LIA)','(set-option :timeout 30000)','(declare-fun P () Int)','(assert (>= P 28))','(assert (= (mod P 4) 0))']
 for i,os in enumerate(opts):
  lines.extend([f'(declare-fun s{i} () Int)',f'(assert (and (<= 0 s{i}) (< s{i} {len(os)})))'])
  for j in range(max(map(len,os))):lines.append(f'(declare-fun t{i}_{j} () Int)')
  for a,hs in enumerate(os):
   for j in range(1,len(hs)):lines.append(f'(assert (=> (= s{i} {a}) (>= (- t{i}_{j} t{i}_{j-1}) 4)))')
 lines.append('(assert (= t0_0 0))')
 def disj(v):return '(or '+' '.join(v)+')'
 for p,i in ix.items():
  for h in range(4):
   q,k=quotient((p[0]+D[h][0],p[1]+D[h][1]),d)
   if q not in ix:continue
   ii=ix[q];pairs=[]
   for a,hs in enumerate(opts[i]):
    src=[j for j,h0 in enumerate(hs)if(h0+(1 if j%2==0 else-1))%4==h]
    for b,hs2 in enumerate(opts[ii]):
     dst=[j for j,h0 in enumerate(hs2)if h0==h]
     if len(src)!=len(dst):continue
     eq=[f'(= s{i} {a})',f'(= s{ii} {b})']+[f'(= (+ t{i}_{u} 1) (+ t{ii}_{v} (* {k} P)))'for u,v in zip(src,dst)]
     pairs.append('(and '+' '.join(eq)+')')
   lines.append('(assert '+disj(pairs)+')')
 return '\n'.join(lines),pts,opts
if __name__=='__main__':
 text,pts,opts=make();ctx=mkcontext(mkconfig());s=mksolver(ctx);inc(ctx,s);parse(ctx,s,text.encode());t=time.time();ans=solve(ctx,s);result={'options':list(map(len,opts)),'status':ans,'seconds':time.time()-t}
 if ans==1:result['model']=modelstr(ctx,getmodel(ctx,s)).decode()
 print(json.dumps(result,indent=2));open(__file__.replace('.py','.json'),'w').write(json.dumps(result,indent=2)+'\n')
