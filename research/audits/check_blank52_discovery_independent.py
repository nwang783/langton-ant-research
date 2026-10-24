from pathlib import Path
from collections import defaultdict
import json,hashlib
S=Path(__file__);D=S.parents[1]/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
P=D/'BLANK52_DISCOVERY_EXCURSION_NOT_A_CONTROLLER.md';F=D/'blank52_discovery_excursion_certificate.json'
assert sha(P).startswith('7fa9a412')and sha(F).startswith('ef0d32a3')and sha(D/'certify_blank52_discovery_excursion.py').startswith('2da782fe')
J=json.loads(F.read_text());V=[1j,1,-1j,-1];off=[-1j,-1-1j,-1,0j];xy=lambda p:[int(p.real),int(p.imag)]
B={};p=0j;h=0;ev=[];states={};fc={}
for t in range(60):
 if str(t)in J['full_states']:
  states[str(t)]={'black':sorted(map(xy,B)),'head':xy(p),'heading':h};assert states[str(t)]==J['full_states'][str(t)]
 fc.setdefault(p+off[h],t);c='L'if p in B else'R';e=dict(time=t,position=xy(p),heading=h,turn=c,active_C=xy(p+off[h]))
 if c=='L':e['R_owner']=B.pop(p)
 else:B[p]=t
 ev.append(e);assert e==J['all60_blank_events'][t];h=(h+(1 if c=='R'else-1))%4;p+=V[h]
w=''.join(e['turn']for e in ev[:54]);assert w==J['whole_module_word']and w[1:53]==J['closed_excursion_word']
assert[(e['time'],e['turn'],e['heading'])for e in ev[:54]if e['position']==[1,0]]==[(1,'R',1),(53,'L',1)]
assert ev[53]['R_owner']==1 and fc[1+0j]==54
assert[e for e in ev[1:53]if e['turn']=='L'and e['R_owner']<1]==[ev[4]]and ev[4]['R_owner']==0
assert states['54']['head']==[1,1]and states['54']['heading']==0 and len(states['54']['black'])==12
H=defaultdict(list)
for e in ev[:54]:
 p=complex(*e['position']);k=int(p.real);q=p-k*(1+1j);H[tuple(xy(q))].append((e['time']-54*k,e['time'],e['turn'],k))
for q in H:H[q].sort()
for r in J['full_drift_stable_histories']:
 assert H[tuple(r['class'])]==[(e['canonical_time'],e['t'],e['c'],e['period_lift'])for e in r['reads']]
assert len(H)==len(J['full_drift_stable_histories'])and H[(0,-4)]==[(-12,42,'R',1),(36,36,'R',0)]
assert next(t for t,e in enumerate(ev)if e['turn']!=w[t%54])==59
O=dict(status='PASS literal blank R E52 L and supplied repetition rejection only',proof=sha(P),certificate=sha(F),script=sha(S),full54_state=states['54'],actual_root_reads=[1,53],first_new_C=54,external_excursion_owner=[0,4],complete_full_drift_class_count=len(H),same_cell_RR_witness=H[(0,-4)],first_blank_repeat_mismatch=59,scope='The52-read excursion is a genuine finite closed head-pose factor funded by connectorR0; the54-read R E52 L module is no-input and drifts(1,1), but cannot repeat on any board. No controller, extremal/unread-row or WHITE S1 claim.')
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(sha(S.with_suffix('.json')))
