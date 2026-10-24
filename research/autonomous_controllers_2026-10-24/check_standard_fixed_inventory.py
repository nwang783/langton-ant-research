#!/usr/bin/env python3
"""Exact fixed104-event inventory WHITE chronology synthesis.
An UNSAT result is only for this fixed spatial inventory, not all fronts.
Uses already installed libz3 through the retained ctypes interface.
"""
import json,sys,hashlib,time,math,re
from itertools import combinations,product
from collections import defaultdict,Counter
from pathlib import Path
from check_extremal_read_coupling import ROOT,event_word,quotient,D
sys.path.insert(0,str(ROOT/'periodic_classification_new'))
from probe_one_a_local_constraints import mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason
OUT=Path(__file__).resolve().parent
W=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];P=len(W)

def setup():
 ev,d,h=event_word(W);H=defaultdict(list)
 for e in ev:
  r,k=quotient(e['p'],d);H[r].append(dict(e,clock=e['t']-P*k))
 for es in H.values():es.sort(key=lambda e:e['clock'])
 points=sorted(H);ix={p:i for i,p in enumerate(points)};options=[];original=[]
 for p in points:
  es=H[p];n=len(es);axis=es[0]['hi']%2;counts=Counter((e['c'],e['hi'])for e in es);R=list(range(0,n,2));L=list(range(1,n,2));opts=[]
  for plusR,plusL in product(combinations(R,counts['R',axis]),combinations(L,counts['L',axis])):
   plus=set(plusR)|set(plusL);opts.append(tuple(axis if j in plus else axis+2 for j in range(n)))
  options.append(opts);original.append(opts.index(tuple(e['hi']for e in es)))
 return ev,d,H,points,ix,options,original

def smt(timeout=60000,blocked=True,pin=False):
 ev,d,H,points,ix,opts,original=setup();lines=['(set-logic QF_LIA)',f'(set-option :timeout {timeout})','(set-option :produce-models true)'];asserts=[]
 def add(x):lines.append('(assert '+x+')');asserts.append(x)
 def choose(i,indices):
  names=[f't{i}_{j}'for j in indices];s=names[-1]
  for k in range(len(names)-2,-1,-1):
   if names[k]!=s:s=f'(ite (= s{i} {k}) {names[k]} {s})'
  return s
 for i,p in enumerate(points):
  lines.append(f'(declare-fun s{i} () Int)');add(f'(and (<= 0 s{i}) (< s{i} {len(opts[i])}))')
  for j in range(len(H[p])):lines.append(f'(declare-fun t{i}_{j} () Int)')
  for j in range(1,len(H[p])):
   add(f'(>= (- t{i}_{j} t{i}_{j-1}) 4)');add(f'(= (mod (- t{i}_{j} t{i}_0) 4) 0)')
  if pin:add(f'(= s{i} {original[i]})')
 add('(= t0_0 0)')
 arcdata=[]
 for i,p in enumerate(points):
  for heading in range(4):
   source=[[j for j,hi in enumerate(hs)if (hi+(1 if j%2==0 else-1))%4==heading]for hs in opts[i]];count=len(source[0]);assert all(len(s)==count for s in source)
   if not count:continue
   q=(p[0]+D[heading][0],p[1]+D[heading][1]);r,k=quotient(q,d);ii=ix[r];target=[[j for j,hi in enumerate(hs)if hi==heading]for hs in opts[ii]];assert all(len(s)==count for s in target)
   for ordinal in range(count):
    src=choose(i,[s[ordinal]for s in source]);dst=choose(ii,[s[ordinal]for s in target]);add(f'(= (+ {src} 1) (+ {dst} {k*P}))')
   arcdata.append({'source':i,'target':ii,'heading':heading,'voltage':k,'count':count})
 if blocked:add('(or '+' '.join(f'(not (= s{i} {v}))'for i,v in enumerate(original))+')')
 return '\n'.join(lines)+'\n',{'drift':d,'points':points,'options':opts,'standard_options':original,'arc_inventory':arcdata,'raw_local_order_combinations':math.prod(map(len,opts)),'local_option_counts':list(map(len,opts)),'constraint_count':len(asserts)}

def run(label,text):
 ctx=mkcontext(mkconfig());s=mksolver(ctx);inc(ctx,s);parse(ctx,s,text.encode());t=time.time();status=solve(ctx,s);out={'status':{1:'SAT',-1:'UNSAT',0:'UNKNOWN'}[status],'seconds':time.time()-t}
 if status==1:out['model']=modelstr(ctx,getmodel(ctx,s)).decode()
 if status==0:out['reason']=reason(ctx,s).decode()
 (OUT/f'standard_fixed_inventory_{label}.smt2').write_text(text);return out

def main():
 control,meta=smt(blocked=False,pin=True);a=run('standard_control',control);assert a['status']=='SAT';print('CONTROL',a['status'],a['seconds'],flush=True)
 target,meta=smt(blocked=True,pin=False);b=run('alternative',target);print('ALTERNATIVE',b['status'],b['seconds'],flush=True)
 out={'scope':__doc__,'inventory':meta,'standard_control':a,'alternative':b,'standard_word_sha256':hashlib.sha256(W.encode()).hexdigest()}
 (OUT/'standard_fixed_inventory_result.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
