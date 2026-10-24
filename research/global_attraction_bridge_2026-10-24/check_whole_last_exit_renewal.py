"""Whole historical last-exit tree, exact edge exchanges, and a finite drought countercontrol."""
from pathlib import Path
from collections import Counter
import hashlib,json
from check_return_permanent_output_debt import DXY,future
from certified_comparison_perturbation import geometry
P=Path(__file__).parent
J=json.loads((P/'JOINT_RECORD_DROUGHT_CHECKED.json').read_text());F=json.loads((P/'RADIAL_SQUARE_EXTERIOR_FACTOR_CHECKED.json').read_text())

def run(name,seed,N,intervals):
 B={q:-i-1 for i,q in enumerate(sorted(seed))};p=(0,0);h=1 if name!='factor11'else 0
 par={};ind=Counter({p:0});V={p};leaves=1;last={};death={};events=[];snap={};records=[];vals=lambda q:(q[1],q[0],-q[1],-q[0]);ext=[max(vals(q)[a]for q in seed|{p})for a in range(4)]
 checkpoints={s for s,t in intervals}|{t for s,t in intervals};Acum=Bcum=0;rewrite=[]
 for t in range(N):
  if t in checkpoints:
   assert len(par)==len(V)-1 and sum(ind[q]==0 for q in V)==leaves and leaves==1+sum(ind[q]==2 for q in V)
   for q,r in par.items():assert r==p or last[r][0]>last[q][0]
   snap[t]=dict(B=dict(B),pose=[p,h],tree=dict(par),V=set(V),leaves=leaves,branches=sum(ind[q]==2 for q in V),A=Acum,Bcharge=Bcum)
  q0=p;old=B.pop(p,None);c='R'if old is None else'L'
  if old is None:B[p]=t;h=(h+1)%4
  else:death[old]=t;h=(h-1)%4
  q=(p[0]+DXY[h][0],p[1]+DXY[h][1]);a=b=0;rr=None;arrival_black=q in B
  if q in V:
   rr=par.pop(q);a=int(ind[rr]==1);b=int(ind[q]==0);leaves+=a-b;ind[rr]-=1;ind[q]+=1
  else:V.add(q);ind[q]=1
  par[p]=q;last[p]=(t,q,c);Acum+=a;Bcum+=b
  events.append(dict(time=t,cell=p,turn=c,consumed=old,next=q,arrival_was_old=rr is not None,arrival_BLACK=arrival_black,removed_destination=rr,A=a,B=b,leaf_change=a-b))
  if a or b:rewrite.append((t,c,arrival_black,a,b))
  p=q
  vv=vals(p)
  for normal in range(4):
   if vv[normal]>ext[normal]:assert vv[normal]==ext[normal]+1;ext[normal]=vv[normal];records.append((t+1,normal))
 if N in checkpoints:raise AssertionError('choose future endpoint strictly beyond checkpoints')
 w,dr,tail,tests=future(B,p,h);death.update({i:N+tt for i,tt in tail.items()});Q,_,_,_=geometry(p,h,w)
 def ray_hit(q):
  ts=[]
  for i,r in enumerate(Q):
   dx=q[0]-r[0];dy=q[1]-r[1]
   if dx%dr[0]==0:
    k=dx//dr[0]
    if k>=0 and dy==k*dr[1]:ts.append(N+104*k+i)
  return min(ts)if ts else None
 outs=[]
 for s,t in intervals:
  S=snap[s];T=snap[t];seen={tuple(e['cell'])for e in events[s:t]};inputs={q:i for q,i in S['B'].items()if s<=death.get(i,10**30)<t};outputs={q:i for q,i in T['B'].items()if s<=i<t};permanent={q:i for q,i in outputs.items()if i not in death};outF={q:i for q,i in outputs.items()if i in death}
  relS={q:i for q,i in S['B'].items()if i in death};relT={q:i for q,i in T['B'].items()if i in death}
  assert set(outputs)==set(T['B'])&seen
  assert len(T['B'])-len(S['B'])==len(permanent)+len(outF)-len(inputs)
  assert len(relT)-len(relS)==len(outF)-len(inputs)
  aa=T['A']-S['A'];bb=T['Bcharge']-S['Bcharge'];assert T['leaves']-S['leaves']==aa-bb
  abandoned={q for q in seen if last[q][0]<t and ray_hit(q)is None}
  frozen_R=abandoned&set(outputs);assert frozen_R==set(permanent)
  tree_info=[]
  for z in[S,T]:
   tree_info.append(dict(pose=z['pose'],vertices=len(z['V']),edges=len(z['tree']),root_count=1,leaves=z['leaves'],branches=z['branches'],tree_sha256=hashlib.sha256(json.dumps(sorted(z['tree'].items())).encode()).hexdigest(),full_black=[[q,i]for q,i in sorted(z['B'].items())],entire_relevant=[[q,i,death[i]]for q,i in sorted(z['B'].items())if i in death]))
  out=dict(start=s,end=t,duration=t-s,whole_tree_cuts=tree_info,A=aa,B=bb,leaf_change=aa-bb,old_cut_inputs=len(inputs),last_R_outputs=len(outputs),permanent_R_outputs=len(permanent),future_consumed_outputs=len(outF),permanently_abandoned_read_cells=len(abandoned),abandoned_WHITE_cells=len(abandoned-set(outputs)),full_mass_change=len(T['B'])-len(S['B']),whole_relevant_change=len(relT)-len(relS),endpoint_is_fresh_in_whole_history=tuple(T['pose'][0])not in{tuple(e['cell'])for e in events[:t]},actual_interval_records=[r for r in records if s<=r[0]<=t])
  if name=='empty'and(s,t)==(11,20):
   assert out['actual_interval_records']==[(11,0),(20,3)]and out['leaf_change']==1 and len(relS)==7 and len(relT)==6 and len(inputs)==3 and len(outF)==2 and not abandoned and not permanent
   future_visits=[]
   for q in sorted(T['V']):
    tt=next(u for u in range(t,125)if tuple(events[u]['cell'])==q);future_visits.append((q,tt))
   out.update(full_tree_before=sorted(S['tree'].items()),full_tree_after=sorted(T['tree'].items()),whole_visited_after=sorted(T['V']),every_historical_vertex_next_read=future_visits,events=events[s:t],inputs=[[q,i,death[i]]for q,i in sorted(inputs.items())],outputs=[[q,i,death[i]]for q,i in sorted(outputs.items())])
  outs.append(out)
 print(name,N,[(z['start'],z['end'],z['leaf_change'],z['permanent_R_outputs'],z['whole_relevant_change'],z['permanently_abandoned_read_cells'])for z in outs],flush=True)
 types={}
 for e in events:
  if e['leaf_change']==1:types.setdefault(str((e['turn'],e['arrival_BLACK'])),e)
 return dict(first_leaf_creating_exchange_types=types,name=name,seed=sorted(seed),physical_reads=N,full_turn_word=''.join(e['turn']for e in events),intervals=outs,terminal_full_field=[[q,i]for q,i in sorted(B.items())],terminal_pose=[p,h],tail_word=w,tail_drift=dr,tail_parity_tests=tests,tree_rewrite_sha256=hashlib.sha256(json.dumps(rewrite).encode()).hexdigest())

cases=[run('empty',set(),9977,[(11,20),(5710,6042)])]
for n in[100,137]:
 c=next(c for c in J['controls']if c['name']==f'MT_{n}');seed=set(map(tuple,c['seed']));end=88368+208*n
 cases.append(run(f'MT_{n}',seed,end+104,[(29671+104*n,end),(32433+104*n,80270+208*n)]))
cases.append(run('factor11',set(map(tuple,F['seed'])),20000,[(5,66)]))
fs=['JOINT_RECORD_DROUGHT_MANIFEST.json','../audits/check_joint_record_drought_independent.json','DROUGHT_BOUNDARY_PINNING_MANIFEST.json','DROUGHT_BOUNDARY_ORIENTATION_ADDENDUM.json','../audits/check_drought_boundary_pinning_independent.json','ORDERED_SQUARE_CIRCULATION_MANIFEST.json','../audits/check_ordered_square_circulation_independent.json','RADIAL_SQUARE_EXTERIOR_FACTOR_MANIFEST.json','../audits/check_radial_square_exterior_factor_independent.json']
for f in fs:assert(P/f).exists(),f
out=dict(status='AUTHOR exact whole-history last-exit rewrite and countercontrol; independent audit pending',cases=cases,physical_reads=sum(c['physical_reads']for c in cases),dependencies={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in fs},scope='One-root arborescence and exact leaf/mass/relevance ledgers. Completed empty-seed drought11..20 refutes payment of leaf increase by permanent abandonment plus net relevant growth. No universal leaf inequality or global occurrence claim.')
(P/'WHOLE_LAST_EXIT_RENEWAL_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
