from pathlib import Path
import json,hashlib
ROOT=Path('/workspace/shared/langton');P=ROOT/'global_attraction_bridge_2026-10-24';OUT=ROOT/'audits'
helper=OUT/'check_return_permanent_debt_independent.py'
exec(compile(helper.read_text().split('results=[check_case')[0],str(helper),'exec'))
M=json.loads((P/'TWENTY_RELEVANT_STOCK_MANIFEST.json').read_text())
for group in ('files','retained_dependencies'):
 for f,v in M[group].items():assert sha(P/f)==v
E=json.loads((P/'TWENTY_RELEVANT_STOCK_CHECKED.json').read_text())
closures={}
for r in J['controls'][:2]:
 name=r['name'];N=r['physical_updates'];B={complex(*z['cell']):z['lifetime'] for z in r['terminal_black']};p=complex(*r['terminal_pose'][0]);h=r['terminal_pose'][1]
 word,drift,tail,tests=verify_future(B,p,h);C0={q for q,i in B.items() if i in tail};initial=dict(B);deaths={};events=[]
 for s in range(104):
  old=B.pop(p,None);events.append(old)
  if old is None:B[p]=N+s;h=(h+1)%4
  else:deaths[old]=s;h=(h-1)%4
  p+=vec[h]
 w1,d1,t1,tests1=verify_future(B,p,h)
 assert word==w1 and drift==d1
 deaths.update({i:104+s for i,s in t1.items()})
 C1={q for q,i in B.items() if i in t1};assert C1=={q+drift for q in C0}
 assert C0=={q for q,i in initial.items() if i in deaths}
 L=len(C0);prof=[L]
 for s,old in enumerate(events):L+=int(N+s in deaths) if old is None else -1;prof.append(L)
 assert max(prof)<=r['relevant_mass_max']
 got=dict(pruned_state=sorted(map(pair,C0)),translated_pruned_state=sorted(map(pair,C1)),drift=pair(drift),relevant_profile=prof,all_future_relevant_max=r['relevant_mass_max'],parity_tests=tests+tests1)
 assert got==E['all_future_reference_closures'][name]
 closures[name]=got
# Recovery confinement and full standalone first stage read/birth identities.
B=set(recovery);p=0j;h=1
for t in range(983+104):
 assert p.real>=-16 and -16<=p.real+p.imag<=10
 black=p in B
 if black:B.remove(p)
 else:B.add(p)
 h=(h+(-1 if black else 1))%4;p+=vec[h]
assert pair(drift)==[2,-2]  # Remaining rays preserve x+y and increase x.
B={q:-i-1 for i,q in enumerate(sorted(G,key=zkey))};p=0j;h=1;word='';reads=[];snapshot=None;first={}
for t in range(390):
 reads.append(p)
 if t==61:snapshot=dict(B)
 old=B.pop(p,None)
 if old is None:B[p]=t;h=(h+1)%4;word+='R'
 else:first[old]=t;h=(h-1)%4;word+='L'
 p+=vec[h]
_,_,tail,_=verify_future(B,p,h);first.update({i:390+t for i,t in tail.items()})
row=[dict(cell=pair(q),lifetime=i,death=first.get(i)) for q,i in sorted(snapshot.items(),key=lambda z:zkey(z[0]))]
assert row==E['reference_cut61_current']
assert all(first[-i-1] in (1,22,32,58) for i in range(4))
A,U=word[:182],word[182:286]
bal=lambda w:w.count('R')-w.count('L')
bals={'A':bal(A),'U':bal(U),'U14':bal(U[:14]),'U61':bal(U[:61]),'U71':bal(U[:71])};assert bals==E['source_word_balances']
internal=[r for r in row if r['death'] is not None];rescued=[r for r in row if r['death'] is None]
assert len(internal)==11 and max(r['death'] for r in internal)==157 and len(rescued)==4
assert internal==E['reference_cut61_later_internal']
recovery_fates={tuple(z['cell']):z['death'] for z in J['controls'][1]['initial_read_fates']}
rescue=[]
for r in rescued:
 x,y=r['cell'];rescue.append(dict(cell=r['cell'],birth=r['lifetime'],recovery_death=recovery_fates[x,y-2]))
assert rescue==E['reference_cut61_restored_by_actual_recovery']
assert sum(v is not None for v in recovery_fates.values())==61
# Exact affine stage periods in k, not sample fitting.
R=[(1,-4),(2,-5),(4,-6),(2,-7),(3,-4)];assert tuple(map(sum,zip(*R)))==(12,-26)
coeff=6*bals['U'];const=20+5*bals['A']-26*bals['U']+2*bals['U61']+2*bals['U71']+bals['U14']
assert (coeff,const,const-61)==(72,-88,-149)
assert E['entire_relevant_stock_bound']==20+22+90==132
# Controls are checked as controls, never as the universal argument.
for r,n in zip(J['controls'][5:],(20,80,400)):
 a=r['selected_returns'][0];assert a['birth']==60 and a['death']==624*n-1516 and a['permanent_births']==72*n-149 and a['radius']>=5*n-5
 assert r['selected_mass_relevance']['61']=={'full':31,'relevant':31,'permanent':0}
report=dict(status='PASS all-even-n>=20 full relevant-stock cap132 and exact marked-return permanent-output72n-149',manifest_sha256=sha(P/'TWENTY_RELEVANT_STOCK_MANIFEST.json'),note_sha256=sha(P/'TWENTY_CELL_RELEVANT_STOCK_AND_OUTPUT.md'),checker_sha256=sha(Path(__file__)),new_finite_annotations=dict(pruned_period_closures=closures,balances=bals,source61_rescues=rescue,endpoint_mass=[coeff,const],marked_permanent_births=[coeff,const-61]),analytic_dependency_scope='All-parameter stage read-set disjointness and protected C90 restriction/future confinement are retained signed exact geometry, bound by manifest and prior independent3e9990a9. Before e partition initial<=20, same-stage eventual inputs<=22, surviving post-e R identities<=90; afterward exact relevant maximum77. No template-permanent outputs are silently treated as permanent in circuit.',not_claimed=['uniform all-n relevant maximum77','one seed with unbounded waits','failure of eventual translation under bounded relevant cardinality','global capture or finite fuel'])
(OUT/'twenty_relevant_stock_independent.json').write_text(json.dumps(report,indent=2)+'\n');print('PASS',sha(OUT/'twenty_relevant_stock_independent.json'))
