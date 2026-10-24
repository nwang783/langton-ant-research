from pathlib import Path
from collections import defaultdict
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'OPEN79_PAID_CHAIN201_AND_UNPAID67_CONTRAST.md';C=D/'open79_paid_chain201_certificate.json';assert sha(P)=='7261971a3699e8346be7025b296ae366148f0e463a9c7637784ac8c2a2dc9d9e';assert sha(C)=='52c221ca53e6f8ec4ec25538c326cf887605a17fdca8a72ad82d6ec9a3535d0d';J=json.loads(C.read_text())
for f,h in J['dependency_hashes'].items():assert sha(D/f)==h
ns={'__file__':str(S.with_name('check_physical_return_debt_independent.py'))};exec(Path(ns['__file__']).read_text().split('out=dict(')[0],ns);chains,H=ns['chains'],ns['H'];chain=next(ch for ch in chains if ch[0]==((12,11),0));assert len(chain)==35
v=(1j,1,-1j,-1);xy=lambda q:[int(q.real),int(q.imag)];B={complex(*q):'initial BLACK'for q in J['complete_initial_black']};p=2+1j;h=2;events=[];owners=[];reads=defaultdict(list)
for t in range(201):
 c='L'if p in B else'R';e=dict(time=t,position=xy(p),normal_level=int(3*p.imag-p.real+11),incoming_heading=h,turn=c);events.append(e);reads[p].append((t,h,c))
 if c=='L':owners.append(dict(time=t,position=xy(p),owner_R_time=B.pop(p)));h=(h-1)%4
 else:B[p]=t;h=(h+1)%4
 p+=v[h]
assert ''.join(e['turn']for e in events)==J['word']and events==J['events']and owners==J['all_L_lifetime_owners'];assert sorted(map(xy,B))==J['complete_final_black']and(p,h)==(1+1j,3);assert len(B)==41 and len(J['complete_initial_black'])==28 and sum(z['owner_R_time']=='initial BLACK'for z in owners)==28;assert 'initial BLACK'not in B.values()
anchors={0:(12,0),2:(10,2),3:(11,8),6:(12,8),20:(12,1),21:(11,1),158:(12,9),159:(11,9),162:(12,10)};named=[]
for k,((t,r),lift)in enumerate(chain):
 e=events[166+k];assert e['position']==xy(11-t+lift*(3+1j))and e['incoming_heading']==H[t][r]and e['turn']=='RL'[r%2];anchors[166+k]=(t,r);named.append(dict(time=166+k,**{'class':t},rank=r,full_lift=lift,position=e['position']))
assert named==J['full35_named_chain'];assert {str(t):list(a)for t,a in anchors.items()}==J['all_named_read_anchors'];assert set(anchors)=={e['time']for e in events if e['normal_level']<=12}and len(anchors)==44
physical=defaultdict(list)
for t,(lev,r)in anchors.items():
 e=events[t];assert e['normal_level']==lev and e['incoming_heading']==H[lev][r]and e['turn']=='RL'[r%2];physical[tuple(e['position'])].append((t,r))
for q,seq in physical.items():
 seq.sort();assert all(b[1]==a[1]+1 for a,b in zip(seq,seq[1:]))
assert max(e['normal_level']for e in events)==32
# Known-color-only obstruction after the earlier literal factor, no exterior whites assumed.
J67=json.loads((D/'open79_joint_repair67_certificate.json').read_text());known={complex(*e['position']):e['turn']=='R'for e in J67['events']};p=complex(*J67['final_position']);h=J67['final_heading'];forced=[]
for t in range(67,70):
 assert p in known and known[p]is False;forced.append([t,xy(p),h,'R']);known[p]=True;h=(h+1)%4;p+=v[h]
assert(p,h)==(-1+0j,2);assert forced==J['earlier67_unread_extension_obstruction']['forced_known_R_reads'];assert [(e['time'],e['incoming_heading'],e['turn'])for e in J67['events']if e['position']==[2,1]]==[(0,2,'R')]
assert all(11-t+lift*(3+1j)!=2+1j for(t,r),lift in chain[:26]);(t,r),lift=chain[26];assert(t,r,lift)==(12,2,1)and H[t][r]==0 and H[12][1]==2
out=dict(status='PASS genuine prepared201 chain payment and exact67 unread-extension obstruction',proof=sha(P),certificate=sha(C),script=sha(S),physical_reads=201,initial_mass=28,final_mass=41,all_initial_lifetimes_consumed=True,complete_named_anchors=44,max_actual_read_normal=32,known67_forced_reads=forced,analytic_scope=['The deterministic201 replay independently uses the complete28-black input and records every read, every L previous-R/initial owner and entire41-black output. All28 initial lifetimes are consumed, not hidden unread support.','The independent79-event ordinal graph supplies all35 lifted physical chain events166..200. All44 named low-level anchors and every same-physical-cell consecutive rank fragment match, including X0/20/192/200 and guide restorations. This is more than a turn-only factor but not the missing earlier/later79 chronology or complete higher drift classes.','For the exact67 factor, three further R reads are forced by cells already read in that factor, regardless of every unread initial color. They reach C rank11 at70; the mandatory named chain reaches X N/rank2 at96 before any intervening X read, while its owned next read is S/rank1. Earlier chain failure also prevents completion. Thus that precise67 prefix has no extension satisfying the complete supplied histories, not a default-WHITE-only diagnostic.','The different201 factor pays X rank1 and realizes this finite mechanism. Positive mass13 is not regeneration; there is no full growth-eight odd inventory, global phase/period, whole-state repeat or autonomous controller claim.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
