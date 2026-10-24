from pathlib import Path
import json,hashlib
S=Path(__file__);D=S.parents[1]/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'T_PORT8_ABSORBER_MANIFEST.json';assert sha(MF)=='0851a2f132d07836fbcbf983e7953bcb418d8bec20c3e6915086193c3f6fbc51';mf=json.loads(MF.read_text())
for kind in ('files','dependencies'):
 for f,h in mf[kind].items():assert sha(D/f)==h
J=json.loads((D/'T_PORT8_ABSORBER_CHECKED.json').read_text());MJ=json.loads((D/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());TJ=json.loads((D/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());ns={'__file__':str(S.with_name('check_phase13_double_scatter_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Canonical source')[0],ns);K,xy,geometry,sim,cert,key=[ns[k]for k in('K','xy','geometry','sim','cert','key')];enc=lambda q:sorted(map(xy,q));dec=lambda q:{complex(*p)for p in q};d=2+2j;W=sim(K,104)['word'];Q,H,_,_=geometry(0j,1,W)
B=set()
for i,p in enumerate(Q):
 a=p-Q[13]
 for k in range(-((int(a.imag)+20)//2),1 if i<13 else 0):B.symmetric_difference_update({a+k*d})
packet={a*d for a in(0,1,3,5,6,8)};assert not B&packet;kernel=B|packet;assert len(kernel)==148 and enc(kernel)==J['kernel']and enc(packet)==J['packet'];word=(D/'T_PORT8_RECOVERY_WORD.txt').read_text().strip();assert word==J['word']and len(word)==23296 and word[:6188]==TJ['T_recovery'][:6188]and(word[6188],TJ['T_recovery'][6188])==('L','R')
z=cert(sim(kernel,len(word),0j,0,word),J['tail_word']);assert z['tail']==W[14:]+W[:14]and(z['p'],z['h'],z['d'])==(-30+26j,0,-2+2j)and enc(z['B'])==J['output_full_black']and len(z['B'])==1204 and z['tests']==J['infinite_parity_tests'];tq,_,_,_=geometry(z['p'],z['h'],z['tail']);assert min(p.imag for p in z['pts']+tq)==-20
C={q for i,q in enumerate(sorted(kernel,key=key))if-i-1 in z['dead']};assert len(C)==124 and enc(C)==J['whole_comparison_pruning']and max(max(abs(q.real),abs(q.imag))for q in C)==22==J['local_radius'];assert max(z['dead'][-i-1]for i,q in enumerate(sorted(kernel,key=key))if q in C)==22254
assert [dict(cell=xy(q),time=z['first'].get(q))for q in sorted(kernel,key=key)]==J['initial_first_reads']and [dict(cell=xy(q),time=z['dead'].get(-i-1))for i,q in enumerate(sorted(kernel,key=key))]==J['initial_consumption_fates']
for row in J['interfaces']:
 lab=row['previous'];m=MJ['modes'][lab];old=dec(m['complete_output_black']);v=complex(*m['output_pose'][0]);ph=m['output_phase'];actual=max(q.imag for q in old);synthetic=v.imag+max(Q[i].imag-Q[ph].imag+(0 if i<ph else -2)for i in range(104));step=206 if lab=='S' else 228;guard=step-20
 assert actual==row['previous_full_output_max_y']and synthetic==row['omitted_synthetic_max_y']and guard==row['new_southern_boundary']and guard-max(actual,synthetic)==row['strict_slack']and row['strict_slack']==(175 if lab=='S' else 177)
assert max(max(q.imag for q in K),max(q.imag for q in Q)-2)==6<201-20
# Solve every infinite ray intersection, rather than assume bounded footprint.
first={}
for i,q in enumerate(z['pts']):
 if q.real==q.imag and q.real>=0 and q.real%2==0:first.setdefault(int(q.real)//2,i)
tests=[]
for i,q in enumerate(tq):
 sol=[];num=q.imag-q.real;den=z['d'].real-z['d'].imag
 if num%den==0:
  k=int(num//den);p=q+k*z['d']
  if k>=0 and p.real>=0 and p.real%2==0:sol.append([int(p.real)//2,k]);first[int(p.real)//2]=min(first.get(int(p.real)//2,10**99),len(word)+104*k+i)
 tests.append({'phase':i,'point':xy(q),'solutions':sol})
assert sorted([[a,t]for a,t in first.items()])==J['entire_ray_first_reads']and set(first)==set(range(11))and(first[9],first[10])==(6232,7816)
# Data may call the exact same independent systems by a different field title.
assert [{'phase':r['phase'],'point':r['point'],'hit':r['solutions'][0]if r['solutions']else None}for r in tests]==J['tail_ray_intersection_tests']
controls=[];reads=0
for row in J['controls']:
 labs=list(row['prefix'])+['T8'];seed=set(K);seq='';p=0j;phase=0;pk=[]
 for lab,n in zip(labs,row['gaps']):
  assert n>=100;q=p+(n+int(13<phase))*d+Q[13]-Q[phase];tail=W[phase:]+W[:phase];seq+=tail*n+tail[:(13-phase)%104];inds=[0,1,3,5,6,8]if lab=='T8'else MJ['modes'][lab]['packet_black_indices'];bits={q+a*d for a in inds};assert not bits&seed;seed|=bits;pk.append(dict(mode=lab,origin=xy(q),time=len(seq),indices=inds))
  if lab=='T8':break
  mm=MJ['modes'][lab];seq+=mm['recovery_word'];p=q+complex(*mm['output_pose'][0]);phase=mm['output_phase']
 assert pk==row['packets']and enc(seed)==row['seed'];entry=len(seq);seq+=word;assert entry==row['entry']and hashlib.sha256(seq.encode()).hexdigest()==row['complete_word_sha256'];zz=cert(sim(seed,len(seq),expected=seq,cuts={entry}),z['tail']);field,p,h=zz['snap'][entry];assert(p,h)==(q,0)and{u-q for u in field if u.imag>=q.imag-20}==kernel
 assert sorted([[xy(u),i]for u,i in field.items()])==row['entry_full_black'];actual={u for u,i in field.items()if i in zz['dead']};assert actual=={q+u for u in C}and enc(actual)==row['entry_entire_pruning']
 for pkt in pk:
  oq=complex(*pkt['origin']);assert all(zz['first'][oq+a*d]>=pkt['time']for a in pkt['indices'])
  if pkt['mode']=='M':assert all(not(pkt['time']<=i<pkt['time']+10712)for u,i in field.items()if i in zz['dead'])
 assert zz['first'][q+8*d]==entry+6188 and enc(zz['B'])==row['terminal_full_black']and[xy(zz['p']),zz['h']]==row['terminal_pose']and zz['tests']==row['parity_tests'];reads+=len(seq);controls.append(dict(prefix=row['prefix'],seed=len(seed),reads=len(seq),relevant=len(actual)))
old=dec(TJ['exact_entry_pruning']['local']);assert old<=C and len(C-old)==25 and 8*d in C-old and len((C-old)-{8*d})==24
O={'status':'PASS all-prefix WHITE7 BLACK8 southern absorber and complete ray footprint','manifest':sha(MF),'script':sha(S),'kernel':148,'pruning':124,'radius':22,'canonical_phase':14,'last_initial_death':22254,'controls':controls,'full_reads':reads,'analytic_review':['Independently reconstructed the whole mature phase13 upper field y>=-20, disjoint paid packet,23296 reads,1204 output cells, explicit canonicalW phase14 and all infinite parity boundaries. Entire future remains in the upper halfplane; exact124 current input lifetimes all die by22254, radius22.','All-prefix transfer retains complete old output and omitted synthetic-past maxima11/31, versus next guard186/208, yielding175/177 slacks. Earlier paid packets lie below; phase13 chronology proves genuine unreadness. This proves every finite protectedS/M prefix and all gaps>=100, not only five named controls. Arbitrary unrelated initial western archive remains excluded.','Every finite read and104 infinite integer ray equations give exactlyindices0..10, with next9/10 at6232/7816. Arbitrary finite extras>=11 are separately missed by whole-future first-difference coupling; they do not preserve bare upper-halfplane equality.','Five complete full-board futures333485 reads reconstruct every entry/terminal field and original first-read owner. No input born in a previousM is consumed. Counterfactual T versusT8 adds24localwake inputs andoneoriginal bit while avoiding786remote dependencies only across different seeds; no in-orbit relevance jump, general register bound or arbitrary-pattern coverage.']};assert reads==333485;S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
