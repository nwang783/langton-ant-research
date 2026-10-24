#!/usr/bin/env python3
"""Bounded constructive completion. UNKNOWN/UNSAT is not a classification."""
import sys,json,time,hashlib
from pathlib import Path
from collections import defaultdict
ROOT=Path(__file__).resolve().parents[1];OUT=Path(__file__).with_name('height13_constructive_search');OUT.mkdir(exist_ok=True)
sys.path.insert(0,str(ROOT/'periodic_classification_new'))
from synthesize_axis_compact_clock import make,values
from probe_one_a_local_constraints import mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason
from synthesize_cap_three_cylinder import check_model
sys.path.insert(0,str(ROOT/'computability'))
from check_rigid_reachability import State,forward
from periodic_tail_checker import first_mismatch
from check_extremal_read_coupling import quotient,event_word
CAP=12;H=13;D=(-2,2)

def transform(p,hs):
 q=(-p[0],11-p[1]);r,k=quotient(q,D)
 return r,tuple((h+2)%4 for h in hs)

def finite_cert(c):
 p0,h0=c['head'];p0=tuple(p0);ev,d,hend=event_word(c['word'],h0,p0);P=len(ev);assert d==D and hend==h0
 groups=defaultdict(list)
 for e in ev:
  r,k=quotient(e['p'],D);groups[r].append((e['t']-P*k,k,e['c']))
 seed=set()
 for r,g in groups.items():
  g.sort();assert g[0][2]=='R'and all(a[2]!=b[2]for a,b in zip(g,g[1:]))
  for n in range(min(k for _,k,_ in g),max(k for _,k,_ in g)):
   turn=next(c for _,k,c in g if k<=n)
   if turn=='L':seed.add(tuple(r[z]+n*D[z]for z in(0,1)))
 state=State(frozenset(seed),p0,h0);bad=first_mismatch(state,c['word']);assert bad is None,bad
 s=state
 for t in range(P*4):
  assert ('L'if s.p in s.black else'R')==c['word'][t%P];s=forward(s)
 primitive=next(k for k in range(1,P+1)if P%k==0 and c['word']==c['word'][:k]*(P//k))
 return {'finite_seed':sorted(seed),'seed_mass':len(seed),'position':p0,'heading':h0,'full_infinite_periodic_tail_mismatch':None,'literal_extra_periods':4,'turn_word_primitive_length':primitive,'growth':c['word'].count('R')-c['word'].count('L')}

def run(name,fixed,timeout,growth=None,force_height=False):
 txt,ps=make(CAP,1,H,timeout,'singleton',True,dy=-2,fixed_override=fixed)
 extra=[]
 if growth is not None:extra.append('(assert (= (+ '+' '.join(f'(mod n{i} 2)'for i in range(len(ps)))+f') {growth}))')
 if force_height:extra.append('(assert (> (+ n0 n1) 0))')
 # Redundant necessary signed residues are NOT added; use unchanged core.
 txt+='\n'.join(extra)+'\n';base=OUT/name;base.with_suffix('.smt2').write_text(txt)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,txt.encode());start=time.time();ans=solve(ctx,sol)
 result={'name':name,'full_drift':D,'normal_read_height':H,'height_forced_exact':force_height,'multiplicity_cap':CAP,'period_upper_bound':len(ps)*CAP,'growth':growth,'fixed_complete_histories':{str(k):v for k,v in fixed.items()},'timeout_ms':timeout,'status':{1:'SAT_PENDING_REPLAY',-1:'UNSAT_BOUNDED_SOLVER_ONLY',0:'UNKNOWN'}[ans],'seconds':time.time()-start,'smt2_sha256':hashlib.sha256(txt.encode()).hexdigest()}
 if ans==1:
  mt=modelstr(ctx,getmodel(ctx,sol)).decode();base.with_suffix('.model').write_text(mt);v=values(mt);vv={'P':int(v['P'])};ss=[]
  for i,p in enumerate(ps):
   n=int(v[f'n{i}']);axis=1-sum(p)%2;hs=[axis+2*int(v[f'b{i}_{j}'])for j in range(n)];ss.append([(''.join(map(str,hs)),[(1 if j%2==0 else-1,h)for j,h in enumerate(hs)])]);vv[f's{i}']=0
   for j in range(n):assert v[f't{i}_{j}'].denominator==1;vv[f't{i}_{j}']=int(v[f't{i}_{j}'])
  cert=check_model(vv,ps,ss,D);result['word_certificate']=cert;result['finite_seed_certificate']=finite_cert(cert);result['status']='SAT_FULL_FINITE_SUPPORT_REPLAY_PASS'
  if growth is not None:assert result['finite_seed_certificate']['growth']==growth
 if ans==0:result['reason']=reason(ctx,sol).decode()
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k not in('fixed_complete_histories','word_certificate','finite_seed_certificate')}) ,flush=True)
 return result

def main():
 std=json.loads(Path(__file__).with_name('check_single_used_first_circle.json').read_text());fixed={(x,-x+t):()for t in range(H)for x in(0,1)}
 for z in std['all_standard_stable_histories']:
  p,hs=transform(z['point'],tuple('NESW'.index(h)for h in z['headings']));assert p in fixed;fixed[p]=hs
 control=run('standard104_padded_control',fixed,15000,growth=12)
 assert control['status']=='SAT_FULL_FINITE_SUPPORT_REPLAY_PASS' and control['word_certificate']['period']==104
 cert=json.loads(Path(__file__).with_name('certify_diagonal_read_minimum.json').read_text());tasks=[]
 for c in cert['cases'][:4]:
  for z in c.get('survivors',[]):
   histories=c['lower_headings']+z['A_headings'];f={}
   for i,hs in enumerate(histories):
    t=i//2-1;r=i%2;p,h=transform((r,t-r),hs);f[p]=h
   tasks.append((c['case'],z['A_indices'],f))
 assert len(tasks)==6
 results=[]
 for i,(case,indices,f)in enumerate(tasks):
  name=f'g8_one_singleton_case{i}_lower{case}_a{indices[0]}_{indices[1]}'
  results.append(run(name,f,30000,growth=8,force_height=True))
  if results[-1]['status']=='SAT_FULL_FINITE_SUPPORT_REPLAY_PASS':break
 (OUT/'SUMMARY.json').write_text(json.dumps({'scope':__doc__,'encoding_source_sha256':hashlib.sha256((ROOT/'periodic_classification_new/synthesize_axis_compact_clock.py').read_bytes()).hexdigest(),'positive_control':control['status'],'requested_cases':6,'completed':[{'name':r['name'],'status':r['status'],'seconds':r['seconds']}for r in results]},indent=2)+'\n')
if __name__=='__main__':main()
