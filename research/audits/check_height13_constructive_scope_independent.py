from pathlib import Path
import ast,json,hashlib
S=Path(__file__).resolve();R=S.parents[1];P=R/'autonomous_controllers_2026-10-24';F=P/'height13_constructive_search';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();wrapper=P/'search_diagonal_height13_completion.py';core=R/'periodic_classification_new/synthesize_axis_compact_clock.py';assert sha(wrapper)=='c998567d2fbfd354d231899d5fe1ba104886906b86bcf9bc2505ebe12b0f1208'and sha(core)=='6aae80f665088cfd6006b54c74c6dc99e7e79d8f762f44220a4784cd5c3031e8'
summary=json.loads((F/'SUMMARY.json').read_text());assert len(summary['completed'])==6 and sum(x['status']=='UNKNOWN'for x in summary['completed'])==4 and sum(x['status']=='UNSAT_BOUNDED_SOLVER_ONLY'for x in summary['completed'])==2
x={'__file__':str(S.parent/'check_eleven_cell_terminal_trap_independent.py')};src=(S.parent/'check_eleven_cell_terminal_trap_independent.py').read_text();exec(src[:src.index('B,p,h,reads,dead=replay(I,0j,2,C)')],x);replay=x['replay'];tail=x['tail'];xy=x['xy'];V=x['V'];D=-2+2j
can=lambda q:q+(int(q.real)//2)*D
def transformed(p,hs):
 q=-complex(*p)+11j;return xy(can(q)),tuple((h+2)%4 for h in hs)
raw=json.loads((P/'certify_diagonal_read_minimum.json').read_text());expected=[]
for z in raw['cases'][:4]:
 for a in z.get('survivors',[]):
  H=z['lower_headings']+a['A_headings'];fixed={}
  for i,hs in enumerate(H):fixed.update([transformed((i%2,i//2-1-i%2),hs)])
  expected.append(fixed)
assert len(expected)==6;statuses=[]
for i,row in enumerate(summary['completed']):
 p=F/(row['name']+'.json');a=json.loads(p.read_text());assert a['status']==row['status']
 fixed={ast.literal_eval(k):tuple(v)for k,v in a['fixed_complete_histories'].items()};assert fixed==expected[i]
 assert(a['normal_read_height'],a['multiplicity_cap'],a['period_upper_bound'],a['growth'],a['full_drift'],a['height_forced_exact'])==(13,12,312,8,[-2,2],True)
 smt=F/(row['name']+'.smt2');assert sha(smt)==a['smt2_sha256'];text=smt.read_text();assert'(assert (> (+ n0 n1) 0))'in text
 assert sum(bool(v)for q,v in fixed.items()if sum(q)==12)==1 and all(10<=sum(q)<=12 for q in fixed)
 assert all(all(h%2==1-sum(q)%2 for h in v)for q,v in fixed.items())
 statuses.append({'case':i,'status':a['status'],'smt2':sha(smt),'fixed_empty_classes_retained':[q for q,v in fixed.items()if not v]})
control=json.loads((F/'standard104_padded_control.json').read_text());c=control['word_certificate'];f=control['finite_seed_certificate'];assert control['status']=='SAT_FULL_FINITE_SUPPORT_REPLAY_PASS'and c['period']==104 and c['drift']==[-2,2]and f['seed_mass']==19
word=c['word'];x['H']=word;seed={complex(*q)for q in f['finite_seed']};p0=complex(*f['position']);h0=f['heading'];qs,d,proof=tail(seed,p0,h0);assert d==D and len(seed)==19 and word.count('R')-word.count('L')==12
B,p,h,_,_=replay(seed,p0,h0,word*4);assert(p,h)==(p0+4*D,h0)
std=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];assert word in std+std
hist={};p=p0;h=h0
for i,turn in enumerate(word):
 q=can(p);k=int((p-q).real/-2);hist.setdefault(q,[]).append((i-k*104,h,turn));h=(h+(1 if turn=='R'else-1))%4;p+=V[h]
for q,a in hist.items():
 a.sort();r=c['classes'][str(xy(q))];assert [z[0]for z in a]==r['times']and ''.join(str(z[1])for z in a)==r['kind']and all(z[2]==('R'if j%2==0 else'L')for j,z in enumerate(a))
assert len(hist)==22 and min(q.real+q.imag for q in hist)==2 and max(q.real+q.imag for q in hist)==12
out={'status':'PASS bounded search geometry/encoding scope and full finite standard positive control ONLY; no UNSAT theorem','wrapper':sha(wrapper),'unchanged_core':sha(core),'search_summary':sha(F/'SUMMARY.json'),'six_search_statuses':statuses,'standard_control':{'json':sha(F/'standard104_padded_control.json'),'period':104,'initial_mass':19,'growth':12,'actual_nonempty_normal_levels':[2,12],'padded_normal_levels':[0,12],'full_infinite_phase_tests':sum(len(z['all_change_point_tests'])for z in proof)},'analytic_review':[
'The transform(-x,11-y), heading+2 is a genuine half-turn plus odd translation, taking full drift(2,-2) to(-2,2), original sector to the compact encoder sector. It maps signed minimum rows-1,0,1 to top levels12,11,10, preserving empty classes. All six one-singleton interfaces were independently reconstructed and matched to the six saved fixed assignments.',
'The26 representative cells are exactly0<=x+y<=12, x=0,1; n_i<=12 implies the explicit derived P<=312. Fixed T occupancy gives top12; assertionn0+n1>0 gives bottom0 for the six new searches. Thus exact13 normal levels, NOT an unrestricted period/multiplicity/width theorem. The padded standard control deliberately does not force bottom0.',
'Reviewed unchanged compact encoder: n and incoming-axis bits give complete WHITE alternating histories, consecutive rank gaps>=4, exact port count equality and ordinal matching, zero exterior ports, P=sum n. A neighbor shift k*(2,-2) is -k times desired full drift, so its target representative clock uses -kP correctly. Each fully matched event cycle has positive length an integer multiple ofP; total eventsP forces a single P-event orbit and distinct phases. Real-clock relaxation is used only for discovery, with every SAT time checked integer before reconstruction.',
'Fresh standard positive replay reconstructs every actual representative history and all104 clocks, all22 nonempty classes, exact19-cell full seed and all-future phase/ray parity. It is retained standard104, growth12, not a new controller. Its active levels2..12 occupy a padded13-level strip.',
'The completed bounded run reports four UNKNOWN/timeouts and two solver-only bounded UNSAT. No opaque status is promoted to an exclusion, even within the bounded window. Any later analytic extraction requires a separate proof/certificate. This scope audit is not an independent solver exhaustion and proves no unrestricted g8 or controller classification.'
]};S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
