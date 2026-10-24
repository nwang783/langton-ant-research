#!/usr/bin/env python3
"""Exact fixed-strip front synthesis with lazy voltage-cycle certificates.
Static local-state SAT is refined by forbidden nonpositive event cycles and
positive-voltage wrong-order segments. SAT is reconstructed and replayed;
finite UNSAT/UNKNOWN is never an unrestricted period/width exclusion.
New implementation, pending independent audit.
"""
from itertools import product
from pathlib import Path
import json,sys,time,re
from probe_one_a_local_constraints import D,mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason
from synthesize_cap_three_cylinder import check_model

def validate(ps,ss,chosen,d):
 dx,dy=d;ix={p:i for i,p in enumerate(ps)};hs=[ss[i][v][1] for i,v in enumerate(chosen)]
 def can(p):k=p[0]//dx;return(p[0]-k*dx,p[1]-k*dy),k
 ev=[(i,j) for i,h in enumerate(hs) for j in range(len(h))];succ={};pred={}
 for p,i in ix.items():
  for h,(ax,ay) in enumerate(D):
   if h%2!=sum(p)%2:continue
   q,k=can((p[0]+ax,p[1]+ay));z=ix.get(q)
   out=[j for j,(c,x) in enumerate(hs[i]) if (x+c)%4==h]
   if z is None:assert not out;continue
   ins=[j for j,(c,x) in enumerate(hs[z]) if x==h];assert len(out)==len(ins)
   for a,b in zip(out,ins):succ[i,a]=((z,b),k);pred[z,b]=(i,a)
 assert set(succ)==set(pred)==set(ev)
 cycles=[];seen=set()
 for e in ev:
  if e in seen:continue
  cyc=[];v=e;voltage=0
  while v not in seen:
   seen.add(v);cyc.append(v);v,k=succ[v];voltage+=k
  assert v==e
  cycles.append((cyc,voltage))
 assert sum(w for c,w in cycles)==1
 for cyc,w in cycles:
  if w<=0:return False,dict(kind='nonpositive_cycle',events=cyc,voltage=w,cells=sorted({i for i,j in cyc}))
 assert len(cycles)==1 and cycles[0][1]==1
 cyc=cycles[0][0];P=len(cyc);times={};wind=0
 for t,e in enumerate(cyc):times[e]=t-wind*P;wind+=succ[e][1]
 assert wind==1
 for i,h in enumerate(hs):
  for j in range(len(h)-1):
   if times[i,j]>=times[i,j+1]:
    a=(i,j);b=(i,j+1);seg=[a];v,k=succ[a];w=k
    while v!=b:
     seg.append(v);v,k=succ[v];w+=k
    seg.append(b)
    assert w>=1 and len(seg)<=P
    return False,dict(kind='positive_wrong_order',events=seg,voltage=w,cells=sorted({x for x,y in seg}),order=[a,b])
 vals={'P':P}
 for i,v in enumerate(chosen):
  vals[f's{i}']=v
  for j in range(len(hs[i])):vals[f't{i}_{j}']=times[i,j]
 cert=check_model(vals,ps,ss,d)
 # Construct a finite seed using only physical histories straddling time zero.
 seed=set()
 for i,p in enumerate(ps):
  ts=[times[i,j] for j in range(len(hs[i]))]
  if not ts:continue
  for k in range((-ts[-1])//P-2,(-ts[0])//P+3):
   shifted=[t+k*P for t in ts];past=sum(t<0 for t in shifted)
   if past%2 and past<len(ts):seed.add((p[0]+k*dx,p[1]+k*dy))
 board=set(seed);p=tuple(cert['head'][0]);h=cert['head'][1];word=cert['word']
 for t in range(100*P):
  c=-1 if p in board else 1
  assert ('R' if c==1 else 'L')==word[t%P]
  if c==1:board.add(p)
  else:board.remove(p)
  h=(h+c)%4;ax,ay=D[h];p=p[0]+ax,p[1]+ay
  if (t+1)%P==0:
   k=(t+1)//P;assert p==(cert['head'][0][0]+k*dx,cert['head'][0][1]+k*dy) and h==cert['head'][1]
 cert.update(seed=sorted(seed),replayed_periods=100)
 return True,cert

def run(cap,dx,dy,w,to,maxiter,generalize=0):
 assert cap>=1 and dx>0 and (dx+dy)%2==0
 ps=[(r,(dy*r)//dx+v) for v in range(-w,w+1) for r in range(dx)];ix={p:i for i,p in enumerate(ps)};ss=[]
 for p in ps:
  a=1-sum(p)%2;hh=[()]+[hs for n in range(1,cap+1) for hs in product((a,a+2),repeat=n)]
  ss.append([(''.join(map(str,hs)),[(1 if j%2==0 else -1,h) for j,h in enumerate(hs)]) for hs in hh])
 bits=(len(ss[0])-1).bit_length();fbits=(cap*len(ps)+1).bit_length()+1;cbits=cap.bit_length()
 def bv(n,b):return f'(_ bv{n%(1<<b)} {b})'
 def can(p):k=p[0]//dx;return(p[0]-k*dx,p[1]-k*dy),k
 decls=[f'(declare-fun s{i} () (_ BitVec {bits}))' for i in range(len(ps))]
 lines=['(set-logic QF_BV)',f'(set-option :timeout {to})','(set-option :produce-models true)']+decls
 add=lambda x:lines.append('(assert '+x+')')
 def ite(i,vals,b):
  s=bv(vals[-1],b)
  for k in range(len(vals)-2,-1,-1):s=f'(ite (= s{i} {bv(k,bits)}) {bv(vals[k],b)} {s})'
  return s
 flux=[]
 for i,p in enumerate(ps):
  add(f'(bvult s{i} {bv(len(ss[i]),bits)})')
  flux.append(ite(i,[sum((p[0]+D[(h+c)%4][0])//dx for c,h in hist) for name,hist in ss[i]],fbits))
 total=flux[0]
 for f in flux[1:]:total=f'(bvadd {total} {f})'
 add(f'(= {total} {bv(1,fbits)})')
 for p,i in ix.items():
  for h,(ax,ay) in enumerate(D):
   if h%2==sum(p)%2:
    q,k=can((p[0]+ax,p[1]+ay));z=ix.get(q)
    out=[sum((x+c)%4==h for c,x in hist) for name,hist in ss[i]]
    ins=ite(z,[sum(x==h for c,x in hist) for name,hist in ss[z]],cbits) if z is not None else bv(0,cbits)
    add(f'(= {ite(i,out,cbits)} {ins})')
   else:
    q,k=can((p[0]-ax,p[1]-ay))
    if q not in ix:add(f'(= {ite(i,[sum(x==h for c,x in hist) for name,hist in ss[i]],cbits)} {bv(0,cbits)})')
 base=Path(__file__).with_name(f'white_lazy_cap{cap}_d{dx}_{dy}_w{w}'+('_generalized' if generalize else ''))
 previous=json.loads(base.with_suffix('.json').read_text()) if base.with_suffix('.json').exists() else {}
 if previous.get('status') in ('SAT_FRONT_REPLAYED','UNSAT_FIXED_STRIP_LEARNED'):
  print(json.dumps(dict(previous_result_preserved=True,**{k:v for k,v in previous.items() if k not in ('chosen','certificate')})),flush=True);return
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,('\n'.join(lines)+'\n').encode());start=time.time();clauses=[];status=None
 if base.with_suffix('.clauses.json').exists():
  clauses=json.loads(base.with_suffix('.clauses.json').read_text())
 prior_seconds=previous.get('seconds',0)
 def clause_text(proof):
  if 'allowed_states' not in proof:
   return '(or '+' '.join(f'(not (= s{i} {bv(v,bits)}))' for i,v in proof['states'])+')'
  return '(or '+' '.join('(not (or '+' '.join(f'(= s{i} {bv(v,bits)})' for v in vs)+'))' for i,vs in proof['allowed_states'])+')'
 def generalize_proof(proof):
  events=[tuple(e) for e in proof['witness']['events']];chosen=dict(proof['states']);allowed={i:set(range(len(ss[i]))) for i in chosen}
  arcs=list(zip(events,events[1:]));obligations=[]
  if proof['witness']['kind']=='nonpositive_cycle':arcs.append((events[-1],events[0]))
  for (i,j),(k,l) in arcs:
   src=ss[i][chosen[i]][1];c,h=src[j];out=(h+c)%4;rank=sum((hh+cc)%4==out for cc,hh in src[:j])
   ax,ay=D[out];target=ps[i][0]+ax,ps[i][1]+ay;voltage=(target[0]-ps[k][0])//dx
   assert target==(ps[k][0]+voltage*dx,ps[k][1]+voltage*dy)
   obligations.append(dict(source=[i,j],target=[k,l],heading=out,ordinal=rank,seam_voltage=voltage))
   allowed[i]&={v for v,(name,hist) in enumerate(ss[i]) if len(hist)>j and (hist[j][0]+hist[j][1])%4==out and sum((hh+cc)%4==out for cc,hh in hist[:j])==rank}
   allowed[k]&={v for v,(name,hist) in enumerate(ss[k]) if len(hist)>l and hist[l][1]==out and sum(hh==out for cc,hh in hist[:l])==rank}
  assert all(chosen[i] in vs for i,vs in allowed.items())
  proof['allowed_states']=[[i,sorted(vs)] for i,vs in sorted(allowed.items())];proof['arc_obligations']=obligations
  return proof
 for proof in clauses:parse(ctx,sol,('(assert '+clause_text(proof)+')\n').encode())
 def checkpoint(status,iteration,extra=None):
  result=dict(cap=cap,drift=[dx,dy],width=w,classes=len(ps),status=status,iterations=iteration+1,clauses=len(clauses),seconds=prior_seconds+time.time()-start)
  if extra:result.update(extra)
  for suffix,data in [('.json',result),('.clauses.json',clauses)]:
   dst=base.with_suffix(suffix);temp=Path(str(dst)+'.tmp');temp.write_text(json.dumps(data,indent=2 if suffix=='.json' else None)+'\n');temp.replace(dst)
  return result
 base.with_suffix('.smt2').write_text('\n'.join(lines)+'\n')
 for iteration in range(len(clauses),maxiter):
  ans=solve(ctx,sol)
  if ans==-1:status='UNSAT_FIXED_STRIP_LEARNED';break
  if ans==0:status='UNKNOWN_SOLVER';break
  mt=modelstr(ctx,getmodel(ctx,sol)).decode();vs={int(a):int(b,2) for a,b in re.findall(r'^s(\d+) -> #b([01]+)$',mt,re.M)}
  assert len(vs)==len(ps),(len(vs),mt)
  chosen=[vs[i] for i in range(len(ps))];ok,witness=validate(ps,ss,chosen,(dx,dy))
  if ok:status='SAT_FRONT_REPLAYED';break
  cells=witness['cells'];proof=dict(states=[[i,chosen[i]] for i in cells],witness=witness)
  if generalize:proof=generalize_proof(proof)
  clauses.append(proof);parse(ctx,sol,('(assert '+clause_text(proof)+')\n').encode())
  if iteration%1000==0:
   result=checkpoint('UNKNOWN_RUNNING',iteration);print(json.dumps(result),flush=True)
 else:status='UNKNOWN_ITERATION_LIMIT'
 result=checkpoint(status,iteration,dict(chosen=chosen,certificate=witness) if status=='SAT_FRONT_REPLAYED' else None)
 print(json.dumps({k:v for k,v in result.items() if k not in ('chosen','certificate')}),flush=True)
if __name__=='__main__':run(*map(int,sys.argv[1:]))
