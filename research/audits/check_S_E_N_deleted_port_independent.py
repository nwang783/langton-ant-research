from pathlib import Path
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];D=R/'S_E_N_deleted_core_port_guard_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='cb606e5e073a200f748125f61d05ae4cf0a87e55667e122c2609df500fa14de9'
mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'deleted_S_core_ports.json').read_text());lib=S.with_name('check_old_V_second_age1_independent.py');ns={'__file__':str(lib)};exec(lib.read_text().split('# Universal')[0],ns)
W,M,K,tr,rot,xy,V=[ns[k]for k in('W','M','K','tr','rot','xy','V')];raw={a:tr(W[a])for a in'DCVU'};ctx={a:tr(W[a]+M)for a in'DCVU'}
I={a:{q for q,b in ctx[a]['req'].items()if b and q not in K}for a in raw};O={a:{q for q,(c,t)in raw[a]['last'].items()if c=='R'and q not in {raw[a]['p']+rot(raw[a]['h'])*k for k in K}}for a in raw}
first=lambda z,q:next((j,c)for j,(p,h,c)in enumerate(z['reads'])if p==q)
roles=[];deletions=[];ledger=[]
for a,z in raw.items():
 for j,(q,h,c)in enumerate(z['reads']):
  if c=='R':
   assert q.imag>=0 and q.real>=-1 and(a!='C'or q.real>=0);roles.append((a,j,tuple(xy(q))))
 if a=='C':continue
 assert z['p'].imag>=1 and z['h']==0
 for q,j in [(-1,1),(-1-1j,2),(-1j,3)]:assert first(z,q)==(j,'L')and z['last'][q]==('L',j);deletions.append((a,tuple(xy(q)),j))
 ins=[];outs=[];cores=[]
 for q in I[a]:assert q.imag>=1;ins.append((xy(q),first(ctx[a],q)[0],q not in z['req']))
 for q in O[a]:assert q.imag<=z['p'].imag and z['last'][q][0]=='R';outs.append((xy(q),z['last'][q][1]))
 ek={z['p']+rot(z['h'])*k for k in K}
 for q in K:
  assert q in z['last'];assert q in ek or z['last'][q][0]=='L'or q in O[a];cores.append((xy(q),z['last'][q],q in ek))
 rr=next(r for r in J['all3_N_RAW_external_export_ledgers']if r['atom']==a)
 assert {tuple(xy(q))for q in I[a]}=={tuple(r['local'])for r in rr['all_true_external_inputs']}
 assert {tuple(xy(q))for q in O[a]}=={tuple(r['local'])for r in rr['all_external_O_final_R_births']}
 for r in rr['all_true_external_inputs']:assert first(ctx[a],complex(*r['local']))[0]==r['actual_first_L']['context_tick0']
 ledger.append(dict(atom=a,inputs=ins,outputs=outs,CORE=cores))
assert len(roles)==41 and set(roles)=={(r['atom'],r['own_tick0'],tuple(r['local_R']))for r in J['all41_CORE_inclusive_physical_R_supports']}
assert len(deletions)==9 and sum(len(I[a])for a in'DVU')==8 and sum(len(O[a])for a in'DVU')==16
# Signed geometric inequalities, including arbitrary lengths and both actual Cs.
assert raw['C']['p']==1j and raw['C']['h']==3
for a in'DVU':assert (rot(2)*raw[a]['p']).imag<=-1 and(rot(1)*raw[a]['p']).imag<=0 and raw[a]['p'].imag>=1
# Complete literal source/reader control from the entire prelaid seed.
r=J['selected_reachable_source_and_failed_reader_control'];labels=r['actual_prefix_labels'];word=''.join(W[a]for a in labels)+W['U'][:13];z=tr(word);seed={q for q,b in z['req'].items()if b};assert not z['bad'] and len(seed)==35 and set(map(tuple,r['complete_seed']))=={tuple(xy(q))for q in seed}and len(word)==221
assert W['U'][:11]==M and len(''.join(W[a]for a in labels))==208
B=set(seed);ids={q:['initial_BLACK',xy(q)]for q in B};p=0j;h=0;fields={};cuts={r['actual_read_count']:r for r in r['all_completed_RAW_and_partial_cuts']}
for t,c in enumerate(word):
 rr=J['selected_reachable_source_and_failed_reader_control']['all221_actual_reads'][t];assert rr['tick0']==t and rr['cell']==xy(p)and rr['turn']==c and rr['prior_identity']==ids.get(p)
 assert(p in B)==(c=='L')
 if c=='L':B.remove(p);del ids[p]
 else:B.add(p);ids[p]=['new_R',t]
 h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 if t+1 in cuts:
  row=cuts[t+1];assert row['pose']==xy(p)+[h]and {tuple(q)for q in row['complete_BLACK']}=={tuple(xy(q))for q in B}and row['hole_BLACK']==(-7-4j in B)and row['hole_identity']==ids.get(-7-4j);fields[t+1]=len(B)
assert(p,h)==(-7-4j,3)and p not in B
zz=tr(''.join(W[a]for a in r['candidate_labels'])+M);assert zz['bad']==(221,133,-7-4j,'L')
assert tr(''.join(W[a]for a in labels))['p']==-6-6j and z['reads'][132][:2]==(-8-4j,2)
out=dict(status='PASS S/E/N deleted-core external-input obstruction and entire221-read control',manifest=sha(MF),dependencies=mf['dependencies'],physical_R_supports=len(roles),actual_deletions=deletions,external_N_ledgers=ledger,complete_control=dict(seed_size=len(seed),reads=len(word),cut_masses=fields,final_pose=xy(p)+[h],actual_next='R',desired_L_conflict=[221,133,[-7,-4]]),analytic=[
'Source S D/V/U deletes its three named K cells finally at L1/L2/L3; their y is Y orY+1, while source EXIT y<=Y-1. Every remaining S R lies at/below its decreasing head. C1 moves down one more, so E entry y<=Y-2. Every E RAW R lies at most one above that head, and C2 R lies at/below it. All41 physical R reads, including CORE writes, satisfy these inequalities. Thus the holes are physically WHITE when the N epoch begins.',
'For every N D/V/U, all8 true external input slots are strictly above entry y, including marker-only inputs whose first read occurs in the actual supplied M. All16 genuine O outputs are final RAW R births at/below EXIT y. Every one of15 incoming K sites is read, so a previously CORE identity cannot emerge as unexplained external BLACK.',
'If a hole later becomes external BLACK, some actual completed N RAW first exports it; even a carried CORE identity requires a final-R O export because every incoming K cell is read. Its fixed y<=producer EXIT y<=all subsequent N entry y prevents any later external input, which requires a strictly higher cell. No assumption that the hole remains physically WHITE during N, or that N CORE births are forbidden, is used.',
'The exact35-cell prelaid seed replays all221 reads and every complete field/identity cut. Source S-V L1 at133 deletes the prospective N-U external q; its requested L13 at221 repeats L133 at the same cell, so actual next turn is R. Last completed V really has M11 from the actual first11 U reads, plus two more executed reads. Reader U is not complete; no physical ant termination is claimed.',
'Scope is only the named S rail/C/E rail/C/N rail with no extra C or FOREIGN and actual contexts. No U ancestry, simplicity, age, rail bound, N CORE-input ban, all-Q-C3 restoration classification or capture theorem follows.'
])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
