from pathlib import Path
import json,hashlib,collections
R=Path('/workspace/shared/langton');P=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
base=R/'audits/check_minimal_cohort_restart_independent.py';ns={'__file__':str(base)};exec(base.read_text().split('report=')[0],ns)
seed,states,poses,head,dead,relevant,events,reads,cp,xy,multiple,v=[ns[k]for k in['seed','states','poses','head','dead','relevant','J','reads','cp','xy','multiple','v']]
for stem,mhash in [('FRESH_HULL_RELEVANT_PRODUCTION','ac2a5cd95dda2e6b70c01c8043074268efeff124c3cdc144bdec4b3cb9d3e373'),('PAIRED_WAKE_RETURN_CREDIT','1d3b853107c359c8951ef603839051d4c3b77140aff7bcdbcef4350304f84c20')]:
 m=P/(stem+'_MANIFEST.json');assert sha(m)==mhash;mf=json.loads(m.read_text())
 for f,h in mf['files'].items():assert sha(P/f)==h
 for f,h in mf['independent_dependency'].items():assert sha(R/'audits'/f)==h
S=json.loads((P/'FRESH_HULL_RELEVANT_PRODUCTION_CHECKED.json').read_text());norm=lambda p:int(p.real-p.imag);tan=lambda p:int(p.real+p.imag)
assert max(map(norm,seed))==-1 and poses[0]==0 and poses[104]==2-2j and head[0]==head[104]==1
fr={q:l for q,l in relevant[104].items()if norm(q)>=0};cnt=collections.Counter(norm(q)for q in fr);assert cnt=={0:5,1:4,2:4,3:4}and len(fr)==17
assert {(tuple(xy(q)),l,dead[l])for q,l in fr.items()}=={(tuple(r['cell']),tuple(r['lifetime']),r['death'])for r in S['fresh_side_lifetimes']}
assert all(q not in seed and l[0]=='R'and 0<=l[1]<104 and dead[l]>=104 for q,l in fr.items())
next3=sorted((dead[l],q,l)for q,l in relevant[104].items())[:3];assert [[xy(q),list(l),t]for t,q,l in next3]==[[r['cell'],r['lifetime'],r['death']]for r in S['next_three_inputs']];assert all(q in fr for t,q,l in next3)
old=set(relevant[0]);new={q-(2-2j)for q in relevant[104]};assert sorted(map(xy,new-old))==S['normalized_added']and sorted(map(xy,old-new))==S['normalized_missing']and(len(new-old),len(old-new))==(11,2)
for zz,k in [(old,'entry_normalized_support'),(new,'exit_normalized_support')]:assert S[k]==dict(normal_min=min(map(norm,zz)),normal_max=max(map(norm,zz)),tangent_min=min(map(tan,zz)),tangent_max=max(map(tan,zz)))
J=json.loads((P/'PAIRED_WAKE_RETURN_CREDIT_CHECKED.json').read_text());seedB=set(map(cp,J['baseline_seed']));assert seedB==seed|{-3-2j};word=J['baseline_word'];assert len(word)==104 and word[:71]==''.join(reads[:71])and word[71]!=reads[71]
BB={q:('I',i)for i,q in enumerate(sorted(seedB,key=lambda z:(z.real,z.imag)))};db={};p=0j;h=1;Q=[];birthpos={}
for t,ch in enumerate(word):
 Q.append(p);oldid=BB.pop(p,None);assert ch==('L'if oldid is not None else'R')
 if oldid is None:BB[p]=('R',t);birthpos[t]=p
 else:db[oldid]=t
 row=J['baseline_events'][t];assert row['time']==t and row['cell']==xy(p)and row['turn']==ch
 h=(h+(1 if ch=='R'else-1))%4;p+=v[h]
assert(p,h,len(BB))==(2-2j,1,27);d=p;tests=0
for i,q in enumerate(Q):
 hits=[k for z in seedB if(k:=multiple(z-q))is not None and k>=0];th=[k for j,z in enumerate(Q)if(k:=multiple(z-q))is not None and(k>0 or k==0 and j<i)];cuts=sorted({0,*hits,*[k+1 for k in hits],*th});row=J['baseline_ray_parity'][i]
 assert sorted(row['initial_hits'])==sorted(hits)and sorted(row['earlier_thresholds'])==sorted(th)and row['tested_periods']==cuts
 for k in cuts:assert (sum(a==k for a in hits)+sum(a<=k for a in th))%2==(word[i]=='L');tests+=1
assert tests==154
for q,l in BB.items():
 times=[104*k+i for i,z in enumerate(Q)if(k:=multiple(q-z))is not None and k>=0 and 104*k+i>=104];tt=min(times)if times else None
 if tt is not None:db[l]=tt
 row=next(r for r in J['baseline_full_state104']if r['cell']==xy(q));assert row['lifetime']==list(l)and row['death']==tt
assert len(J['baseline_full_state104'])==len(BB)
perm=[{'birth':b,'cell':xy(q)}for b,q in birthpos.items()if('R',b)not in db];assert perm==J['baseline_permanent_births']and len(perm)==12
Dp=[{'birth':t,'cell':events['events'][t]['cell']}for t in range(104)if reads[t]=='R'and('R',t)not in dead];assert Dp==J['defect_permanent_births']and len(Dp)==3
assert word.count('R')==reads[:104].count('R')==58 and word.count('L')==reads[:104].count('L')==46
for row in J['common_prefix_births_with_different_fates']:
 b=row['birth'];q=cp(row['cell']);assert b<71 and birthpos[b]==q and events['events'][b]['cell']==xy(q)and('R',b)not in db and dead['R',b]==row['defect_death']
assert [(r['birth'],r['defect_death'])for r in J['common_prefix_births_with_different_fates']]==[(44,168),(46,166),(52,200),(58,210)]
assert sum(l in db for l in BB.values())==15 and all(('I',i)in db for i in range(15));assert len(relevant[104])-len(relevant[0])==58-3-46==9
report={'status':'PASS finite fresh-layer production and paired complete-future wake-return controls','proof_sha256':{f:sha(P/f)for f in['FRESH_HULL_RELEVANT_PRODUCTION.md','PAIRED_WAKE_RETURN_CREDIT.md']},'script_sha256':sha(Path(__file__)),'fresh_relevant_layer_counts':dict(cnt),'normalized_added_missing':[11,2],'next3_input_birth_deaths':[[l[1],t]for t,q,l in next3],'baseline_all_period_parity_tests':tests,'both_104_RL_counts':[58,46],'permanent_R_outputs_baseline_defect':[12,3],'relevant_gains_baseline_defect':[0,9],'analytic_checks':['Signed full defect replay rebuilt, including exact all-future lifetime relevance.17 relevant R lifetimes lie in original-white layers0..3 and exceed14 retired entrylifetimes. This defeats only a unit injective retirement charge.','Same-sector displacement normalization is actual2,-2; relevant14->23 corresponds11 added2 missing, scalar change9-4alpha. No bounded-below or total-credit argument follows.','Independent full15-black baseline replay and exact104 infinite phase-ray parity certify its whole future. All27 terminal lifetimes receive exact first futurehit or none, not a finite replay guess.','General identity C*(u)-C*(t)=R-P-L is exact lifetime accounting with P retrospectively forever-unread interval births. Permanent current lifetimes cannot later be consumed in the SAME orbit.','Four identical commonprefixRbirths have different futures on two distinct initialboards. No actually forever-unread lifetime revives; nine permanent-output deficit is NET, not a claimed nine-birth bijection.'],'not_claimed':['global resource or P(m) impossibility','repeatable growth','noncapture','failure of fixed-cohort272754','all spatial/amortized potentials ruled out']}
p=R/'audits/relevant_spatial_pair_independent.json';p.write_text(json.dumps(report,indent=2)+'\n');print(sha(p));print(report['status'])
