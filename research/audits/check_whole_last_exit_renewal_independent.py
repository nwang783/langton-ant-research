from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'WHOLE_LAST_EXIT_RENEWAL_MANIFEST.json';ad=D/'WHOLE_LAST_EXIT_ENDPOINT_ADDENDUM.json';assert sha(mf)=='2689a2a619f607b42011bce454b6da60746747a314822027103fe89d90e22bd4'and sha(ad).startswith('15a2411b')
for man in[mf,ad]:
 m=json.loads(man.read_text())
 for f,h in m['files'].items():assert sha(D/f)==h
 for f,h in m.get('dependencies',{}).items():assert sha(D/f)==h
J=json.loads((D/'WHOLE_LAST_EXIT_RENEWAL_CHECKED.json').read_text());ns={'__file__':str(S.with_name('check_phase13_double_scatter_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Canonical source')[0],ns);sim,future,xy,V=[ns[k]for k in('sim','future','xy','V')];summary=[];total=0
for case in J['cases']:
 name=case['name'];seed={complex(*p)for p in case['seed']};N=case['physical_reads'];cuts={r[k]for r in case['intervals']for k in('start','end')};z=sim(seed,N,0j,0 if name=='factor11' else 1,expected=case['full_turn_word'],cuts=cuts);total+=N;w,dr,dead,tests=future(z['B'],z['p'],z['h']);assert w==case['tail_word']and xy(dr)==case['tail_drift']and tests==case['tail_parity_tests'];z['dead'].update({i:N+t for i,t in dead.items()});assert case['terminal_pose']==[xy(z['p']),z['h']]and case['terminal_full_field']==[[xy(q),i]for q,i in sorted(z['B'].items(),key=lambda kv:(kv[0].real,kv[0].imag))]
 roots={0j};edge={};deg=Counter({0j:0});last={};snap={};cumA=cumB=0;rew=[];types={};records=[];ext=[max((p.imag,p.real,-p.imag,-p.real)[a]for p in seed|{0j})for a in range(4)]
 def ordered_edges(ed):return[[xy(p),xy(q)]for p,q in sorted(ed.items(),key=lambda kv:(kv[0].real,kv[0].imag))]
 for t in range(N):
  p=z['pts'][t]
  if t in cuts:
   assert p not in edge and set(edge)==roots-{p}and all(v in roots for v in edge.values());actual=Counter(edge.values());assert all(actual[q]==deg[q]and deg[q]<=2 for q in roots);leaves=sum(deg[q]==0 for q in roots);branches=sum(deg[q]==2 for q in roots);assert leaves==branches+1
   for q,r in edge.items():assert r==p or last[r][0]>last[q][0]
   snap[t]=dict(edge=dict(edge),V=set(roots),leaves=leaves,branches=branches,A=cumA,B=cumB)
  q=z['pts'][t+1]if t+1<N else z['p'];c=z['word'][t];a=b=0;old=edge.pop(q,None);arrival_black=(q in z['snap'][t][0])if t in z['snap']else None
  if q in roots:
   assert old is not None;a=int(deg[old]==1);b=int(deg[q]==0);deg[old]-=1;deg[q]+=1
  else:assert old is None;roots.add(q);deg[q]=1
  edge[p]=q;last[p]=(t,q,c);cumA+=a;cumB+=b
  # Arrival color follows its most recent physical read, or the complete input seed.
  if q in last:arrival_black=last[q][2]=='R'
  else:arrival_black=q in seed
  if a or b:rew.append((t,c,arrival_black,a,b))
  if a-b==1:
   key=str((c,arrival_black));types.setdefault(key,dict(time=t,cell=xy(p),turn=c,consumed=z['events'][t],next=xy(q),arrival_was_old=old is not None,arrival_BLACK=arrival_black,removed_destination=xy(old)if old is not None else None,A=a,B=b,leaf_change=a-b))
  v=(q.imag,q.real,-q.imag,-q.real)
  for normal in range(4):
   if v[normal]>ext[normal]:assert v[normal]==ext[normal]+1;ext[normal]=v[normal];records.append([t+1,normal])
 assert types==case['first_leaf_creating_exchange_types']and hashlib.sha256(json.dumps(rew).encode()).hexdigest()==case['tree_rewrite_sha256']
 # Future read rays from the complete certified terminal field.
 pp=z['p'];hh=z['h'];Q=[]
 for c in w:Q.append(pp);hh=(hh+(1 if c=='R'else-1))%4;pp+=V[hh]
 def hit(q):
  for r in Q:
   a=(q-r)/dr
   if abs(a.imag)<1e-12 and a.real>=0 and abs(a.real-round(a.real))<1e-12:return True
  return False
 for row in case['intervals']:
  s,t=row['start'],row['end'];ss=snap[s];tt=snap[t];SB,sp,sh=z['snap'][s];TB,tp,th=z['snap'][t];seen=set(z['pts'][s:t]);ins={q:i for q,i in SB.items()if s<=z['dead'].get(i,10**30)<t};outs={q:i for q,i in TB.items()if s<=i<t};perm={q:i for q,i in outs.items()if i not in z['dead']};ff={q:i for q,i in outs.items()if i in z['dead']};rs={q:i for q,i in SB.items()if i in z['dead']};rt={q:i for q,i in TB.items()if i in z['dead']};abandon={q for q in seen if last[q][0]<t and not hit(q)}
  assert set(outs)==set(TB)&seen and set(perm)==abandon&set(outs);assert len(TB)-len(SB)==len(outs)-len(ins)and len(rt)-len(rs)==len(ff)-len(ins)
  assert (tt['leaves']-ss['leaves'],tt['A']-ss['A'],tt['B']-ss['B'],len(ins),len(outs),len(perm),len(ff),len(abandon),len(abandon-set(outs)),len(TB)-len(SB),len(rt)-len(rs))==(row['leaf_change'],row['A'],row['B'],row['old_cut_inputs'],row['last_R_outputs'],row['permanent_R_outputs'],row['future_consumed_outputs'],row['permanently_abandoned_read_cells'],row['abandoned_WHITE_cells'],row['full_mass_change'],row['whole_relevant_change']);assert row['leaf_change']==row['A']-row['B'];assert row['actual_interval_records']==[r for r in records if s<=r[0]<=t];assert row['endpoint_is_fresh_in_whole_history']==(tp not in set(z['pts'][:t]))
  for cut,trr in zip([s,t],row['whole_tree_cuts']):
   st=snap[cut];B,p,h=z['snap'][cut];assert(trr['vertices'],trr['edges'],trr['root_count'],trr['leaves'],trr['branches'])==(len(st['V']),len(st['edge']),1,st['leaves'],st['branches']);assert trr['pose']==[xy(p),h]and trr['tree_sha256']==hashlib.sha256(json.dumps(ordered_edges(st['edge'])).encode()).hexdigest();assert trr['full_black']==[[xy(q),i]for q,i in sorted(B.items(),key=lambda kv:(kv[0].real,kv[0].imag))];assert trr['entire_relevant']==[[xy(q),i,z['dead'][i]]for q,i in sorted(B.items(),key=lambda kv:(kv[0].real,kv[0].imag))if i in z['dead']]
  if(name,s,t)==('empty',11,20):
   assert ordered_edges(ss['edge'])==row['full_tree_before']and ordered_edges(tt['edge'])==row['full_tree_after'];vis=[]
   for q in sorted(tt['V'],key=lambda q:(q.real,q.imag)):vis.append([xy(q),next(i for i in range(20,125)if z['pts'][i]==q)])
   assert vis==row['every_historical_vertex_next_read'];assert len(tt['V'])==11 and z['pts'][20]not in set(z['pts'][:20]);assert z['word'][11:20]=='RRRLLLLRL'and(ss['leaves'],tt['leaves'],len(rs),len(rt))==(2,3,7,6);assert len(ins)==3 and len(ff)==2 and not perm and not abandon
  summary.append(dict(name=name,start=s,end=t,leaf_delta=row['leaf_change'],C=len(ins),O=len(outs),P=len(perm),F=len(ff),relevant_delta=len(rt)-len(rs)))
print('full reads',total);assert total==J['physical_reads']==256217
O=dict(status='PASS exact whole-history last-exit exchange and narrow net-renewal falsifier, with mandatory fresh-root qualification',manifest=sha(mf),endpoint_addendum=sha(ad),script=sha(S),physical_reads=total,intervals=summary,analytic_review=[
'The entire historical last-exit graph deletes the currenthead oldsuccessor and has exactlyone root. Along any nonrootedge lastdeparturetimes strictlyincrease, excludingcycles. Fixedsector permits indegree0/1/2, giving leaves=branches+1. Newarrival preservesleaves; oldarrival removesitsactualoldsuccessor edge and addsoldhead->arrival, yielding precisely thetwo degreeindicators. All chronological exchanges and snapshot edge/time order checked.',
'C counts consumed distinct BLACK-at-start identities, O intervalborn lastR outputs; permanentP and actualfutureF splitO. Fullmasschange=P+F-C and entire relevantchange=F-C are bookkeeping, not a charging theorem. Unread oldBLACK remains in every fullboard and may lie outside the headhistorygraph.',
'EmptyseedE pristinecuts11/20 are consecutive; wholehistoricalleaves2->3,branches1->2 while C*7->6, C3,F2,P0. Allten earlierreadvertices are rereadby124 and thefresh eleventhroot is FIRSTreadat20, as mandatoryaddendum clarifies. Thus positivebranch/leafrenewal neednotpay permanentabandonment or netrelevantgrowth; actualselfwritten inputreplacements are retained.',
'Fresh256217 updates acrossfour original completefields, seven intervals, allterminalfields, infinitecanonicalparity and allpast/futureidentity fates reconstruct. The11cell exteriorfactor is independently captured at sufficientcut20000, not claimedearliest; its earlier finiteportfailure remainsunchanged.',
'The proposed interval-reset leaf<=C+O+1 bound staysUNPROVED. Gross output/lifetime charging, a different amortizedpotential and repeated-drought exclusions are not falsified by this narrowcountercontrol. No universal occurrence or capture follows.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(summary);print(sha(S.with_suffix('.json')))
