from pathlib import Path
import json,hashlib
R=Path('/workspace/shared/langton');P=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();m=P/'MINIMAL_COHORT_RESTART_MANIFEST.json';assert sha(m)=='6ae662ff2b7a3095d0d7e47c327af920a77783af5bb98c8f2302512b775408ae';mf=json.loads(m.read_text())
for f,h in mf['files'].items():assert sha(P/f)==h
for f,h in mf['independent_dependencies'].items():assert sha(R/'audits'/f)==h
J=json.loads((P/'MINIMAL_COHORT_RESTART_CHECKED.json').read_text());v=[1j,1,-1j,-1];xy=lambda p:[int(p.real),int(p.imag)];cp=lambda a:complex(*a);dot=lambda n,p:int(n.real*p.real+n.imag*p.imag);norms=[1,-1,1j,-1j,1+1j,-1-1j,1-1j,-1+1j];seed=set(map(cp,J['initial_seed']));assert len(seed)==14
B=set(map(cp,J['genuine_preparation']['initial_seed']));p=-1+1j;h=1;past=[]
for ch in'RL':
 past.append(p);assert(p in B)==(ch=='L');B.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=v[h]
assert B==seed and(p,h)==(0,1)
B={q:('C0',i)for i,q in enumerate(sorted(seed,key=lambda z:(z.real,z.imag)))};dead={};states=[];poses=[];head=[];maxima=[];reads=[];records=[];maxi={n:max(dot(n,p)for p in past)for n in norms}
for t in range(309):
 states.append(B.copy());poses.append(p);head.append(h);maxima.append(maxi.copy());ns=[n for n in norms if dot(n,p)>maxi[n]and all(dot(n,q)<dot(n,p)for q in B)]
 if ns:records.append((t,ns))
 for n in norms:maxi[n]=max(maxi[n],dot(n,p))
 if t==308:break
 old=B.pop(p,None);ch='L'if old is not None else'R'
 if old is None:B[p]=('R',t)
 else:dead[old]=t
 e=J['events'][t];assert e==dict(time=t,cell=xy(p),heading=h,turn=ch,consumed=list(old)if old else None)
 reads.append(ch);h=(h+(1 if ch=='R'else-1))%4;p+=v[h]
assert(p,h,len(B))==(4-4j,1,54)and len(records)==27
word=J['terminal_word'];Q=[];pp=p;hh=h
for ch in word:Q.append(pp);hh=(hh+(1 if ch=='R'else-1))%4;pp+=v[hh]
d=pp-p;assert d==2-2j and hh==h and len(word)==104

def multiple(z):
 k=int(z.real)//2
 return k if z==k*d else None
checks=0
for i,q in enumerate(Q):
 hits=[k for z in B if(k:=multiple(z-q))is not None and k>=0];th=[k for j,z in enumerate(Q)if(k:=multiple(z-q))is not None and(k>0 or k==0 and j<i)];cuts={0,*th,*hits,*[k+1 for k in hits]}
 tests=[]
 for k in sorted(cuts):
  bit=(sum(a==k for a in hits)+sum(a<=k for a in th))%2;assert bit==(word[i]=='L');tests.append([k,bit]);checks+=1
 a=J['terminal_ray_parity'][i];assert a['phase']==i and a['point']==xy(q)and sorted(a['initial_black_ray_hits'])==sorted(hits)and sorted(a['earlier_read_thresholds'])==sorted(th)and a['tests']==tests
terminal=[]
for q,l in B.items():
 times=[308+104*k+i for i,z in enumerate(Q)if(k:=multiple(q-z))is not None and k>=0];first=min(times)if times else None
 if first is not None:dead[l]=first
 row=next(a for a in J['terminal_cohort_first_reads']if a['cell']==xy(q));assert row['lifetime']==list(l)and row['first_future_read']==first;terminal.append((xy(q),first))
assert checks==154
relevant=[{q:l for q,l in s.items()if l in dead and dead[l]>=t}for t,s in enumerate(states)];assert [len(relevant[t])for t in[0,71,104,169,225,308]]==[14,16,23,25,18,15]and max(dead[l]for l in states[0].values())==70
cat=json.loads((P/'OUTWARD_RECORD_GUARDS_CHECKED.json').read_text());guards=[]
for c in cat['normal_catalog']:
 for r in c['records']:
  for k in range(4):
   z=(-1j)**k;guards.append((r['phase'],k,(r['normalized_heading']+k)%4,cp(c['outward_normal'])*z,{cp(q)*z for q in r['required_black']},{cp(q)*z for q in r['required_white']}))
assert len(guards)==32

def matches(field,p,h):
 ans=[]
 for phase,k,hh,n,bb,ww in guards:
  if h==hh and{p+q for q in bb}<=set(field)and not{p+q for q in ww}&set(field)and all(dot(n,q)<dot(n,p)for q in field):ans.append([phase,k,xy(n)])
 return ans
for (t,ns),row in zip(records,J['all_pristine_records']):
 assert row['time']==t and row['normals']==list(map(xy,ns))and row['pose']==xy(poses[t])and row['mass']==len(states[t])
 for label,field in [('full_guard_matches',states[t]),('minimal_guard_matches',relevant[t])]:
  got=matches(field,poses[t],head[t]);assert got==row[label]and bool(got)==(t==308)
summary=[]
for row in J['greedy_renewals']:
 t=row['start'];co=set(states[t].values());rel=set(relevant[t].values());deaths=sorted((a,l)for l,a in dead.items()if l in co and a>=t);third=deaths[2][0];u=next(z for z,ns in records if z>third);assert(third,u)==(row['third_consumption'],row['next_record'])
 oldlive=set(states[u].values())&co;oldrel=set(relevant[u].values())&rel;newrel=set(relevant[u].values())-rel
 assert (len(co),len(states[u]),len(rel),len(relevant[u]),len(rel-oldrel),len(newrel))==(row['full_start'],row['full_end'],row['relevant_start'],row['relevant_end'],row['relevant_retired'],row['relevant_new_live'])
 removed=set(states[t])-set(relevant[t]);assert all(all(q in states[z]for z in range(t,309))for q in removed)
 candidate=next((z,[n for n in norms if dot(n,poses[z])>maxima[z][n]and all(dot(n,q)<dot(n,poses[z])for q in set(states[z])-removed)])for z in range(third+1,309)if any(dot(n,poses[z])>maxima[z][n]and all(dot(n,q)<dot(n,poses[z])for q in set(states[z])-removed)for n in norms))
 assert candidate[0]==u and [candidate[0],list(map(xy,candidate[1]))]==row['first_record_after_pruning_entry_irrelevant']
 # Physically replay from the minimal entry board as an additional control.
 BB=set(relevant[t]);pp=poses[t];hh=head[t]
 for z in range(t,308):
  ch='L'if pp in BB else'R';assert ch==reads[z];BB.symmetric_difference_update({pp});hh=(hh+(1 if ch=='R'else-1))%4;pp+=v[hh]
 assert BB==set(states[308])-removed and pp==poses[308]and hh==head[308]
 summary.append((t,third,u,len(rel),len(relevant[u])))
assert summary[:3]==[(0,31,71,14,16),(71,93,104,16,23),(104,135,169,23,25)]
assert next(t for t,ns in records if t>31 and 1-1j in ns)==104
for row in J['selected_complete_states']:
 t=row['time'];assert row['pose']==xy(poses[t])and row['heading']==head[t]
 for e in row['black']:
  q=cp(e['cell']);l=states[t][q];assert e['lifetime']==list(l)and e['death']==dead.get(l)and e['relevant']==(q in relevant[t])
 assert len(row['black'])==len(states[t])
report={'status':'PASS literal failure of strict or nonincreasing oracle-minimal relevant-cohort mass across greedy third-input pristine-record restarts','manifest_sha256':sha(m),'script_sha256':sha(Path(__file__)),'fine_prefix_reads':308,'actual_pristine_record_cuts':27,'rotated_guards_per_cut':32,'infinite_tail_parity_tests':checks,'terminal_relevant_unread':[15,39],'greedy_renewals':summary,'fixed_normal_subcontrol':[0,104,14,23],'analytic_review':['Minimal relevant subboard means deletion-only preservation of the whole future word. Deleting never-read black lifetimes changes no read; deleting an eventually-read one changes its earliest differing read. This is an exact hindsight notion, not an effective general algorithm.','Complete finite replay retains all fields, genuine R birth IDs and two-read preparation. Every record is strict against all actual earlier heads and the entire current forward half-plane is white.','Exact phase-ray change thresholds certify the entire standard tail, not finite replay. Every terminal current lifetime has its first future read solved over all104 infinite rays or proved absent; this determines complete relevance at every earlier cut.','All32 guards tested on full and minimal fields at all27 record cuts. Full pruning is also physically replayed from every greedy entry, and ALL subsequent cuts rechecked for possibly earlier newly-pristine records. Greedy cuts stay71/104/169; first three relevant sizes rise14/16/23/25.','This refutes only strict-drop or nonincrease of minimal relevant cohort mass at that restart, including fixed-normal0-to104 increase14-to23. The example captures by308 and does not refute spatial/amortized budgets, all finite-seed capture or the signed fixed-cohort272754 theorem.']}
p=R/'audits/minimal_cohort_restart_independent.json';p.write_text(json.dumps(report,indent=2)+'\n');print(sha(p));print(report['status'])
