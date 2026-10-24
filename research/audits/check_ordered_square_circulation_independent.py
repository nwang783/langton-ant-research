from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'ORDERED_SQUARE_CIRCULATION_MANIFEST.json';assert sha(mf)=='bf5e48255a91a5df4eef7d1a5da406cfb1e2d1b6b1a45fa002f04dd25260062f';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(D/f)==h
J=json.loads((D/'ORDERED_SQUARE_CIRCULATION_CHECKED.json').read_text());ns={'__file__':str(S.with_name('check_phase13_double_scatter_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Canonical source')[0],ns);sim,future,xy,V=[ns[k]for k in('sim','future','xy','V')]
z=sim(set(),10081,0j,1,expected=J['prefix_word']+J['tail_word'],cuts={5710,5712,6036,6042,9977});B,p,h=z['snap'][9977];w,d,deaths,n=future(B,p,h);assert w==J['tail_word']and xy(d)==J['tail_drift']and n==J['tail_parity_tests']and len(B)==715;z['dead'].update({i:9977+t for i,t in deaths.items()})
for row in J['whole_cuts']+[J['tail_state']]:
 B,p,h=z['snap'][row['cut']];assert row['pose']==[xy(p),h]and row['full_mass']==len(B)and row['full_black']==[[xy(q),i]for q,i in sorted(B.items(),key=lambda kv:(kv[0].real,kv[0].imag))]
 assert row['entire_future_relevant']==[[xy(q),i,z['dead'][i]]for q,i in sorted(B.items(),key=lambda kv:(kv[0].real,kv[0].imag))if i in z['dead']]
Q={9+4j,10+4j,10+5j,9+5j};ts=[t for t in range(5710,6042)if z['pts'][t]in Q];assert ts==[5710,5711,6036,6037,6038,6039,6040,6041]
def event(t):return dict(time=t,cell=xy(z['pts'][t]),heading=z['heads'][t],turn=z['word'][t],old_lifetime=z['events'][t])
assert[event(t)for t in ts]==J['patch_events']and[event(z['first'][complex(*q)] )for q in J['patch']]==J['patch_first_reads'];assert all(z['word'][z['first'][q]]=='R'for q in Q)
assert all(sum(z['pts'][t]==q and z['word'][t]==c for t in ts)==1 for q in Q for c in'RL')
assert set(z['snap'][5710][0])&Q==set(z['snap'][6042][0])&Q=={10+5j}
last={q:max(t for t in ts if z['pts'][t]==q)for q in Q};arrows=[]
for q in map(lambda q:complex(*q),J['patch']):
 t=last[q];c=z['word'][t];v=z['pts'][t+1];assert v not in Q or last[v]>t;arrows.append(dict(cell=xy(q),last_read=t,turn=c,next=xy(v),exits=v not in Q))
assert arrows==J['last_exit_forest'];assert z['events'][6037]==5693 and z['dead'][5693]==6037 and z['dead'][6041]==6313
assert all(z['pts'][t+1]in Q for t in ts if z['word'][t]=='L')and len({q for q in Q if z['snap'][5710][0].get(q)is not None})==1
assert z['word'][5712:6036]==J['outside_word']and Counter(J['outside_word'])==dict(R=172,L=152)
assert sorted(map(xy,set(z['snap'][5710][0])^set(z['snap'][6042][0])))==J['full_field_xor']and len(J['full_field_xor'])==92
C=[0j,1+0j,1+1j,1j];maxlen=0
for row in J['patch_automaton']:
 mask=row['before'];p=C[row['entry']];h=[0,3,2,1][row['entry']];ls=[];seen=set()
 while p in C:
  state=(mask,p,h);assert state not in seen;seen.add(state);i=C.index(p);c='L'if mask&(1<<i)else'R';ls.append([i,c]);mask^=1<<i;h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 assert ls==row['reads']and mask==row['after']and[xy(p),h]==row['exit_pose'];maxlen=max(maxlen,len(ls))
assert len(J['patch_automaton'])==64 and maxlen==6
O=dict(status='PASS exact finite last-exit BLACK-root condition and sharp literal EMPTY-seed square component only',manifest=sha(mf),script=sha(S),full_reads=10081,tail_parity_tests=n,patch_times=ts,old_input=J['old_input'],replacement=J['replacement'],whole_masses=[len(z['snap'][t][0])for t in(5710,6042)],whole_relevance=[len(r['entire_future_relevant'])for r in J['whole_cuts']],automaton_states=64,analytic_review=[
'For a finite actual interval ending outsideQ, the last outgoing arrow from each visited Q cell, if internal, reaches a cell whose last read is strictly later. The internal arrows are therefore a forest with exiting roots. Restored endpoint colors give positive even visit counts and lastL for initiallyWHITE, lastR for initiallyBLACK.',
'For an actual square sector whose L route is internal, with no external-cornerL, each exiting root mustR and hence initiallyBLACK. Roots are distinct per last-exit component. This charges CURRENT bits at the packet initialcut, not originalseed cells or freshfuel.',
'Fresh blank replay reconstructs all10081 reads, full fourpacketfields and715cell capturefield, everylifetime fate including exact infinite rays, all64 local color/entry states and actual outside324reads. The oneQinputR5693 dies6037; replacementR6041 dies6313. Bothfullfields, entireC*296to310 and cursor changes remain; no local reset is treated as globalstate recurrence.',
'This is only a finite component of the scaled radial flow, not its full15/3/9/9 inventory. Remaining externalL routes could provide last exits and evade this particular allWHITE obstruction. No ant realization of the summable stationary witness, boundedseed allscale family, autonomous packet repetition or noncapture follows.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
