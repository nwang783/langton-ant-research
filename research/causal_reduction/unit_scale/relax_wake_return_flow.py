"""Cap-free finite-cylinder incidence relaxation for prepared104 wake return.
No chronological alternation order or connected physical cycle is assumed.
A feasible output is only a necessary aggregate control, never an ant path.
"""
from pathlib import Path
import sys,json,time
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'periodic_classification_new'))
from probe_one_a_local_constraints import mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason,D
from synthesize_axis_compact_clock import values
W=set(map(tuple,json.loads((P/'shifted_reverse104_bulk.json').read_text())['wake_black_classes']))
def run(height=13,offset=-4,sector=1,massdelta=0,timeout=20000,pmax=None):
 ps=[(x,x+y+offset)for y in range(height)for x in range(2)];ix={p:i for i,p in enumerate(ps)}
 axis=lambda p:(sector-sum(p))%2
 counts={(i,h,s):f'c{i}_{h}_{"R"if s==1 else"L"}'for i,p in enumerate(ps)for h in range(4)if h%2==axis(p)for s in(1,-1)}
 lines=['(set-logic QF_LIA)',f'(set-option :timeout {timeout})','(set-option :produce-models true)','(declare-fun P () Int)']
 add=lambda x:lines.append('(assert '+x+')')
 summ=lambda z:'(+ '+' '.join(z)+')'if z else'0'
 for v in counts.values():lines.append(f'(declare-fun {v} () Int)');add(f'(>= {v} 0)')
 for i,p in enumerate(ps):
  lines.append(f'(declare-fun o{i} () Int)');add(f'(and (<= 0 o{i})(<= o{i} 1))')
  init=int((p[0]-p[1],p[0]%2)in W)
  signed=[v if s==1 else f'(- {v})'for (ii,h,s),v in counts.items()if ii==i]
  add(f'(= {summ(signed)} (- o{i} {init}))')
  for h in range(4):
   if h%2!=axis(p):continue
   # Incoming h comes from the predecessor physical cell p-D[h].
   vx,vy=D[h];a=(p[0]-vx,p[1]-vy);k=a[0]//2;q=(a[0]%2,a[1]-2*k);j=ix.get(q)
   incoming=[v for(ii,hh,s),v in counts.items()if ii==i and hh==h]
   outgoing=[v for(ii,hh,s),v in counts.items()if ii==j and(hh+s)%4==h]
   add(f'(= {summ(incoming)} {summ(outgoing)})')
  # Absence of destinations outside the strip.
  for h in range(4):
   if h%2==axis(p):continue
   vx,vy=D[h];a=(p[0]+vx,p[1]+vy);k=a[0]//2;q=(a[0]%2,a[1]-2*k)
   if q not in ix:add(f'(= {summ([v for(ii,hh,s),v in counts.items()if ii==i and(hh+s)%4==h])} 0)')
 add(f'(= P {summ(list(counts.values()))})');add('(> P 0)')
 for ax in range(2):
  vals=[]
  for(i,h,s),v in counts.items():
   coeff=D[(h+s)%4][ax]
   if coeff:vals.append(v if coeff==1 else f'(- {v})')
  add(f'(= {summ(vals)} -2)')
 add(f'(<= (- {summ([f"o{i}"for i in range(len(ps))])} {len(W)}) {massdelta})')
 if pmax is not None:add(f'(<= P {pmax})')
 txt='\n'.join(lines)+'\n';tag=f'wake_return_flow_h{height}_s{sector}_mass{massdelta}'+(f'_p{pmax}'if pmax is not None else'')
 (P/(tag+'.smt2')).write_text(txt)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,txt.encode());st=time.monotonic();ans=solve(ctx,sol)
 out=dict(scope=__doc__,height=height,offset=offset,sector=sector,mass_delta_at_most=massdelta,period_bound=pmax,status={1:'SAT_RELAXATION_ONLY',-1:'UNSAT_RELAXATION',0:'UNKNOWN'}[ans],seconds=time.monotonic()-st)
 if ans==1:
  mt=modelstr(ctx,getmodel(ctx,sol)).decode();(P/(tag+'.model')).write_text(mt);v=values(mt)
  out['period']=int(v['P']);out['cells']=[dict(p=p,input=int((p[0]-p[1],p[0]%2)in W),output=int(v[f'o{i}']),counts={f'{h}{"R"if s==1 else"L"}':int(v[c])for(ii,h,s),c in counts.items()if ii==i},n=sum(int(v[c])for(ii,h,s),c in counts.items()if ii==i))for i,p in enumerate(ps)]
 if ans==0:out['reason']=reason(ctx,sol).decode()
 (P/(tag+'.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True);return out
if __name__=='__main__':run()
