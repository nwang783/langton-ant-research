from pathlib import Path
from collections import defaultdict
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
P=D/'STANDARD_TWO_MODULE_ALL_LENGTH_CLASSIFICATION.md';JF=D/'standard_two_module_language_certificate.json'
assert sha(P).startswith('bd5c4792') and sha(JF).startswith('31769a5d') and sha(D/'certify_standard_two_module_language.py').startswith('45ab87be')
J=json.loads(JF.read_text())
for f,h in J['dependencies'].items():assert sha(Path(f))==h
assert sha(S.with_name('check_C_cycle_excursion_independent.json')).startswith('99d6b773')
ns={'__file__':str(S.with_name('check_phase13_double_scatter_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Canonical source')[0],ns);sim,future=ns['sim'],ns['future']
V=[1j,1,-1j,-1];xy=lambda z:[int(z.real),int(z.imag)];delta=-1+1j

def geo(w,h=3,p=0j):
 E=[]
 for t,c in enumerate(w):
  hi=h;h=(h+(1 if c=='R' else -1))%4;E.append(dict(t=t,p=xy(p),hi=hi,ho=h,c=c));p+=V[h]
 return E,p,h
A,B=J['module_words']['A'],J['module_words']['B'];source={};allrows=defaultdict(lambda:{'A_sources':[],'B_sources':[]})
for name,w in [('A',A),('B',B)]:
 E,d,h=geo(w);assert d==delta and h==3 and E==J['all104_local_events'][name]
 for e in E:
  x,y=e['p'];q=(0,x+y);z=dict(relative_module_index=x,local_phase=e['t'],turn=e['c'],heading=e['hi'],local_position=e['p']);allrows[q][name+'_sources'].append(z)
for q,z in allrows.items():
 for v in z.values():v.sort(key=lambda a:(a['relative_module_index'],a['local_phase']))
assert [dict(representative=list(q),**v) for q,v in sorted(allrows.items())]==J['complete_cell_source_tables']
for kind,q in [('AA_guard',(0,-1)),('BB_guard',(0,-3))]:
 for a in 'AB':
  ls=[[z['relative_module_index'],z['local_phase'],z['turn']] for z in allrows[q][a+'_sources']];assert ls==J[kind][a+'_complete_sources']
fa=J['AA_guard']['A_complete_sources'];fb=J['AA_guard']['B_complete_sources'];assert fa==[[0,5,'L']] and [z for z in fb if z[0]<0]==[[-1,7,'R']]
E,_,_=geo(B*2);q=-2-1j;reads=[e for e in E if complex(*e['p'])==q];assert [r['t'] for r in reads[:2]]==[17,109] and [r['c'] for r in reads[:2]]==['R','R'] and reads[:2]==J['BB_guard']['consecutive_same_physical_R_reads']
# Full AA prepared factor, from first-color constraints, not merely expected word replay.
E,p,h=geo(A*2);seen={};seed=set()
for e in E:
 q=complex(*e['p'])
 if q not in seen:
  if e['c']=='L':seed.add(q)
 else:assert seen[q]!=e['c']
 seen[q]=e['c']
z=sim(seed,20,h=3,expected=A*2);aa=J['genuine_prepared_AA_full_factor']
assert seed=={-1, -1j,1-1j} and sorted(map(xy,seed))==aa['initial_black'] and sorted(map(xy,z['B']))==aa['final_black'] and xy(z['p'])==aa['head'] and z['h']==aa['heading'] and E==aa['all_events']
W=json.loads((D/'active_C_entry_exit_forests_certificate.json').read_text())['base_controls']['S104']['word'];assert A+B==W[45:]+W[:45]
st=J['genuine_standard_AB_full_field'];field={complex(*q):i for i,q in enumerate(st['full_black_field'])};fw,d,dead,tests=future(field,complex(*st['head']),st['heading']);assert len(field)==758 and fw==A+B and d==-2-2j
powrows=[]
for n in [1,2,3,5]:
 E,d,h=geo((A+B)*n);N=104*n;assert d==2*n*delta and h==3;hist=defaultdict(list)
 for e in E:
  p=complex(*e['p']);k=-(int(p.real)//(2*n));q=p-k*d;hist[q].append((e['t']-k*N,e['c']))
 for ls in hist.values():
  ls.sort();assert ls[0][1]=='R' and all(a[1]!=b[1] for a,b in zip(ls,ls[1:]))
 powrows.append(dict(module_count=2*n,period=N,full_drift=xy(d),complete_read_classes=len(hist)))
assert powrows==J['standard_full_drift_power_controls']
O=dict(status='PASS all-length exact fixed A10/B94 language classification only',proof=sha(P),certificate=sha(JF),script=sha(S),all_module_events=104,complete_source_classes=len(allrows),AA_full_factor_reads=20,AA_seed=sorted(map(xy,seed)),AB_full_field_mass=758,AB_infinite_parity_tests=tests,full_drift_controls=powrows,analytic_review=[
'Both literal modules preserve incoming W and displace by delta=(-1,1). Every local event is explicitly integrated. The delta bookkeeping representative is (0,x+y) and its relative module index is x; thus the finite source tables enumerate every possible read of each physical cell for ANY module sequence. This does not collapse the n residues of an actual full drift n*delta.',
'For AA at successive indices j-1,j, q_j=(0,-1)+j*delta is first read by A_j.L5. The only possible earlier table entry is B_(j-1).R7, absent because that module is A. All other B entries lie in module j or later. In a complete WHITE bi-infinite history this is impossible. In a one-sided actual tail, every internal AA pair instead consumes a distinct BLACK bit present at the whole tail-entry cut, since no earlier tail read can touch q_j and delta is nonzero. No newly written bit or restarted cohort is charged.',
'For BB, the same physical cell at(-2,-1) relative to the first module has consecutive R updates17 and109, with no intervening read in either module. Initial color, older archive and later modules cannot repair consecutive identical turns. This excludes BB on any board.',
'Consequently complete WHITE bi-infinite module histories alternate. Complete WHITE periodic histories are standard104 phases/powers. An actual infinite finite-field module tail has finitely many AA by the injective entry-bit charge and no BB, hence eventually alternates. The condition of entering and staying in this exact module alphabet is not supplied by this theorem.',
'The actual prepared AA three-cell seed and complete20-read output are retained; AA is not an arbitrary-board contradiction. The AB control retains its whole758-cell blank-origin state and exact infinite standard tail. Full-drift power controls verify physical classes without a period bound. No claim covers extra routers, orientation resets, different modules, arbitrary controllers, WHITE S=1, or universal capture.'
]);S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
