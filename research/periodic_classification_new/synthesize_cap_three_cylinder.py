#!/usr/bin/env python3
"""Exact fixed-drift finite-strip cap-three front synthesis, all periods.
Only the strip is bounded. P is derived from multiplicities, not enumerated.
A model has one event cycle by the positive-voltage component argument.
"""
import sys,json,time,re
from pathlib import Path
from probe_one_a_local_constraints import D,states,conj,disj,mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason

def make(w,timeout,dx=-2,dy=-2):
 assert dx==dy and dx<0
 n=-dx
 ps=[(r,r+v) for v in range(-w,w+1) for r in range(n)];ix={p:i for i,p in enumerate(ps)};ss=[states(p) for p in ps]
 def canonical(q):
  x,y=q;r=x%n;k=(x-r)//dx;return (r,r+y-x),k
 lines=['(set-logic QF_LIA)',f'(set-option :timeout {timeout})','(set-option :produce-models true)','(declare-fun P () Int)']
 add=lambda x:lines.append('(assert '+x+')')
 mult=[];odd=[]
 for i,p in enumerate(ps):
  lines.append(f'(declare-fun s{i} () Int)');add(f'(and (<= 0 s{i}) (< s{i} 11))')
  for j in range(3):lines.append(f'(declare-fun t{i}_{j} () Int)')
  add(f'(< t{i}_0 t{i}_1)');add(f'(< t{i}_1 t{i}_2)')
  mult.append('(+ '+' '.join(f'(ite (= s{i} {a}) {len(h)} 0)' for a,(_,h) in enumerate(ss[i]) if h)+')')
  odd.append('(+ '+' '.join(f'(ite (= s{i} {a}) 1 0)' for a,(_,h) in enumerate(ss[i]) if len(h)%2)+')')
 add('(= P (+ '+' '.join(mult)+'))');add('(> P 0)');add('(>= (+ '+' '.join(odd)+') 8)')
 for p,i in ix.items():
  for out_h in range(4):
   if out_h%2!=sum(p)%2:continue
   ax,ay=D[out_h];q,k=canonical((p[0]+ax,p[1]+ay))
   po=[[j for j,(c,h) in enumerate(hist) if (h+c)%4==out_h] for _,hist in ss[i]]
   if q not in ix:
    add(disj([f'(= s{i} {a})' for a,oi in enumerate(po) if not oi]));continue
   z=ix[q];qi=[[j for j,(c,h) in enumerate(hist) if h==out_h] for _,hist in ss[z]];opts=[]
   for a,oi in enumerate(po):
    for b,ij in enumerate(qi):
     if len(oi)!=len(ij):continue
     opts.append(conj([f'(= s{i} {a})',f'(= s{z} {b})']+[f'(= (+ t{z}_{y} (* {k} P)) (+ t{i}_{x} 1))' for x,y in zip(oi,ij)]))
   add(disj(opts))
 # Incoming edges from outside must be absent as well.
 for p,i in ix.items():
  for h in range(4):
   if h%2==sum(p)%2:continue
   ax,ay=D[h];q,k=canonical((p[0]-ax,p[1]-ay))
   if q in ix:continue
   add(disj([f'(= s{i} {a})' for a,(_,hist) in enumerate(ss[i]) if not any(hh==h for c,hh in hist)]))
 return '\n'.join(lines)+'\n',ps,ss

def getints(txt):
 out={}
 for line in txt.splitlines():
  k,v=line.split(' -> ');out[k]= -int(v[3:-1]) if v.startswith('(- ') else int(v)
 return out

def check_model(val,ps,ss,d):
 P=val['P'];ev={};hist={}
 for i,p in enumerate(ps):
  name,h=ss[i][val['s'+str(i)]];ts=[val[f't{i}_{j}'] for j in range(len(h))];assert all(a<b for a,b in zip(ts,ts[1:]));hist[p]=dict(kind=name,times=ts)
  for j,((c,hd),t) in enumerate(zip(h,ts)):
   k=t//P;r=t%P;pos=(p[0]-k*d[0],p[1]-k*d[1]);assert r not in ev;ev[r]=(pos,hd,c)
 assert len(ev)==P and set(ev)==set(range(P))
 for r in range(P):
  p,h,c=ev[r];hh=(h+c)%4;ax,ay=D[hh];q=(p[0]+ax,p[1]+ay)
  np,nh,nc=ev[(r+1)%P]
  if r==P-1:np=(np[0]+d[0],np[1]+d[1])
  assert (q,hh)==(np,nh)
 return dict(period=P,drift=d,word=''.join('R' if ev[r][2]==1 else'L' for r in range(P)),head=ev[0][:2],classes={str(p):a for p,a in hist.items() if a['times']})

if __name__=='__main__':
 w=int(sys.argv[1]);timeout=int(sys.argv[2]) if len(sys.argv)>2 else 30000;n=int(sys.argv[3]) if len(sys.argv)>3 else 2
 d=(-n,-n);txt,ps,ss=make(w,timeout,*d);base=Path(__file__).with_name(f'cap3_cylinder_d{n}_w{w}');base.with_suffix('.smt2').write_text(txt)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,txt.encode());st=time.time();ans=solve(ctx,sol)
 result=dict(width=w,drift=d,classes=len(ps),timeout_ms=timeout,status={1:'SAT',-1:'UNSAT_FIXED_STRIP',0:'UNKNOWN'}[ans],seconds=time.time()-st)
 if ans==1:
  mt=modelstr(ctx,getmodel(ctx,sol)).decode();base.with_suffix('.model').write_text(mt);result['certificate']=check_model(getints(mt),ps,ss,d)
 if ans==0:result['reason']=reason(ctx,sol).decode()
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
