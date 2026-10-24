#!/usr/bin/env python3
"""Discovery only, derived local size bounds and full phase travel constraints."""
from probe_g8_cycle_three_modes import *
def produce():
 txt,pts,caps=make();P=124;lines=[txt,'(assert (= P 124))'];events=[(i,j)for i in range(8)for j in range(caps[i])]
 def add(x):lines.append('(assert '+x+')')
 def absx(x):return f'(ite (>= {x} 0) {x} (- {x}))'
 def vec(i,j,out=False):
  h=f'h{i}_{j}';h=f'(mod (+ {h} {1 if j%2==0 else 3}) 4)'if out else h
  return f'(ite (= {h} 1) 1 (ite (= {h} 3) (- 1) 0))',f'(ite (= {h} 0) 1 (ite (= {h} 2) (- 1) 0))'
 for i,j in events:
  for nm in ('q','x','y'):lines.append(f'(declare-fun {nm}{i}_{j} () Int)')
  add(f'(= q{i}_{j} (mod t{i}_{j} {P}))')
  add(f'(= x{i}_{j} (- {pts[i][0]} (* 2 (div t{i}_{j} {P}))))')
  add(f'(= y{i}_{j} (+ {pts[i][1]} (* 2 (div t{i}_{j} {P}))))')
 for z,(i,j)in enumerate(events):
  for ii,jj in events[z+1:]:
   ac=f'(and (< {j} n{i}) (< {jj} n{ii}))';add(f'(=> {ac} (not (= q{i}_{j} q{ii}_{jj})))')
 for i,j in events:
  vx,vy=vec(i,j,True)
  for ii,jj in events:
   if(i,j)==(ii,jj):continue
   ux,uy=vec(ii,jj);ac=f'(and (< {j} n{i}) (< {jj} n{ii}))';wrap=f'(ite (< q{i}_{j} q{ii}_{jj}) 0 1)';dt=f'(+ (- q{ii}_{jj} q{i}_{j}) (* {P} {wrap}))'
   dx=f'(- (+ x{ii}_{jj} (* 2 {wrap})) x{i}_{j})';dy=f'(- (- y{ii}_{jj} (* 2 {wrap})) y{i}_{j})'
   direct=f'(and (= {dx} {vx}) (= {dy} {vy}) (= h{ii}_{jj} (mod (+ h{i}_{j} {1 if j%2==0 else 3}) 4)))'
   bx=f'(- {dx} {ux} {vx})';by=f'(- {dy} {uy} {vy})';bound=f'(<= (+ {absx(bx)} {absx(by)}) (- {dt} 2))'
   add(f'(=> {ac} (ite (= {dt} 1) {direct} {bound}))')
 return '\n'.join(lines)
if __name__=='__main__':
 text=produce();Path(__file__).with_suffix('.smt2').write_text(text);ctx=mkcontext(mkconfig());s=mksolver(ctx);inc(ctx,s);parse(ctx,s,text.encode());t=time.time();ans=solve(ctx,s);print(ans,time.time()-t,flush=True)
 if ans==1:Path(__file__).with_suffix('.model').write_text(modelstr(ctx,getmodel(ctx,s)).decode())
