from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'RADIAL_SQUARE_EXTERIOR_FACTOR_MANIFEST.json';assert sha(mf)=='e17c0b92a87181855d32bcd03022d55b7e381c2a3362c76fa538363377c12456';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(D/f)==h
J=json.loads((D/'RADIAL_SQUARE_EXTERIOR_FACTOR_CHECKED.json').read_text());seed={complex(*q)for q in J['seed']};Q=[0j,1+0j,1+1j,1j];assert len(seed)==11 and not seed&set(Q);xy=lambda p:[int(p.real),int(p.imag)];key=lambda p:(p.real,p.imag);B={q:-i-1 for i,q in enumerate(sorted(seed,key=key))};p=0j;h=0;V=[1j,1,-1j,-1];first={};dead={};events=[];snap={}
for t in range(186):
 if str(t)in J['full_snapshots']:
  row=dict(pose=[xy(p),h],full_field=[[xy(q),i]for q,i in sorted(B.items(),key=lambda z:key(z[0]))],patch={str(Q.index(q)):i for q,i in B.items()if q in Q});assert row==J['full_snapshots'][str(t)];snap[t]=(dict(B),p,h)
 if t==185:break
 old=B.pop(p,None);c='R'if old is None else'L';first.setdefault(p,t);row=dict(time=t,cell=xy(p),heading=h,turn=c,consumed_lifetime=old);assert row==J['events'][t];events.append(row)
 if old is None:B[p]=t
 else:dead[old]=t
 h=(h+(1 if c=='R'else-1))%4;p+=V[h]
assert len(events)==185 and(p,h)==(1+0j,3)and B[p]==65
for row in J['patch_episodes']:
 s,t=row['start'],row['end'];assert Q[row['entry']]==snap[s][1]and ''.join(e['turn']for e in events[s:t])==row['word'];assert all(complex(*e['cell'])in Q for e in events[s:t])and snap[t][1]not in Q
for row in J['connectors']:
 s,t=row['start'],row['end'];assert t-s==row['length']and row['word']==''.join(e['turn']for e in events[s:t])and row['read_cells']==[e['cell']for e in events[s:t]]and all(complex(*e['cell'])not in Q for e in events[s:t])
assert all(complex(*e['cell'])not in Q for e in events[66:185])
for r in J['all_initial_first_reads']:
 q=complex(*r['cell']);assert r['first_read']==first[q]==dead[r['initial_identity']]and r['turn']==events[first[q]]['turn']=='L'
assert max(dead[i]for i in range(-11,0))==52 and dead[1]==25 and snap[5][0][1+0j]==1 and snap[66][0][1+0j]==65
B5=snap[5][0];B66=snap[66][0];assert len(B5)==14 and len(B66)==25 and sorted(map(xy,set(B5)^set(B66)))==J['inner_cycle']['full_field_xor']and len(set(B5)^set(B66))==29
assert{q:B66[q]for q in seed&B66.keys()}=={-2+0j:56,2j:28,2+1j:39}
ct=Counter();outside=[]
for row in J['patch_episodes'][2:]:
 for k,e in enumerate(events[row['start']:row['end']]):
  typ=('inner_L'if k else'outer_L')if e['turn']=='L'else('entry_R'if not k else'exit_R');ct[tuple(e['cell']),typ]+=1
assert all([ct[tuple(xy(q)),typ]for typ in['inner_L','outer_L','entry_R','exit_R']]==[2,0,1,1]for q in Q)
outside=[e for e in events[5:66]if complex(*e['cell'])not in Q];assert len(outside)==45 and Counter(e['turn']for e in outside)==dict(R=28,L=17)
proto=json.loads((D/'RADIAL_SQUARE_ORDERED_PORTS_CHECKED.json').read_text());assert [r['entry']for r in J['patch_episodes']]==proto['entry_ports'][:6]==[0,0,3,2,1,0]and proto['entry_ports'][6]==3
O=dict(status='PASS literal eleven-cell full-field finite185-update exterior-routing factor ONLY',manifest=sha(mf),script=sha(S),seed=J['seed'],patch_entries=[0,0,3,2,1,0],factor_updates=66,verified_updates=185,original_inputs_consumed_by=52,inner_root=dict(birth=1,death=25,replacement=65),full_field_xor=29,next_actual_entry=dict(t=185,vertex=1,heading=3,color='BLACK',required_protocol_vertex=3),analytic_review=[
'Every one of185 physical updates and all completeBLACK snapshots are independently replayed from the full11-cell exteriorseed, with all other cellsWHITE. Each initial guide firstL is its actual lifetime death, and all11 retire by52. The five entire exterior connectors and119-read later interval avoid the protectedpatch as claimed.',
'Actual firstsix protocolentries implement preparation and one uniform innercirculation. Q rootR1 dies25 and newR65 replacesit; wholemass14to25, XOR29,45outside reads and every guide-coordinate fate remain. This is not a reset ofcursor, outsidefield, identities or fuel.',
'The unchanged continuation next enters vertex1 BLACK at185 rather than prescribedvertex3. Only this185-update finite certificate is bound; no wholefuture relevance, tailcapture, full96protocol, repair impossibility, boundedseed iteration or autonomouscontroller follows.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
