from pathlib import Path
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'HISTORICAL_CONNECTOR_SCOPE_MANIFEST.json'
assert sha(MF).startswith('ef3e97bd')
for f,h in json.loads(MF.read_text())['files'].items():assert sha(D/f)==h
ref=json.loads((D/'HISTORICAL_CONNECTOR_SCOPE_CHECKED.json').read_text())
for f,h in ref['dependencies'].items():assert sha(D/f)==h
lib=S.with_name('check_phase13_double_scatter_independent.py');ns={'__file__':str(lib)};exec(lib.read_text().split('# Canonical source')[0],ns)
sim,geometry,K,xy,future,phases=[ns[k]for k in('sim','geometry','K','xy','future','phases')]
P=json.loads((D/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());A=json.loads((D/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());J=json.loads((D/'CHRONOLOGICAL_SPINE_ORIENTATION_CHECKED.json').read_text());W=sim(K,104)['word'];assert W==P['W'];v=157+164j;w=158+164j
pre=W*100+W[:13]+P['modes']['M']['recovery_word'];Q,H,p,h=geometry(0j,1,pre);assert len(pre)==21125 and(p,h)==(228+229j,0)
assert[(i,pre[i])for i,q in enumerate(Q)if q==v]==[(8183,'R')]and Q[8184]==w
assert[(i,pre[i])for i,q in enumerate(Q)if q==w]==[(8184,'R'),(8292,'L'),(8304,'R'),(8308,'L')]
q,_,e,hh=geometry(p,h,W[41:]+W[:41]);assert min(z.real for z in q)==225 and e-p==2+2j
q,_,e,hh=geometry(0j,0,A['T_recovery']);assert min(z.real for z in q)==-38 and(e,hh)==(-36-10j,0)
q,_,e,hh=geometry(0j,0,A['T_tail_word']);assert min(z.real for z in q)==-4 and min(z.real for z in q[:100])==-4 and e==-2-2j
post=A['postcollision_word'];q,_,e,hh=geometry(207+229j,1,post);assert v not in q and[(i,post[i])for i,z in enumerate(q)if z==w]==[(47390,'R')];assert(e,hh)==(155+215j,1)
NW=A['controls'][0]['complete_future_certificate']['tail_word'];q,_,e,hh=geometry(e,hh,NW);assert min(z.imag for z in q)==213 and(e,hh)==(153+217j,1)and NW in phases
controls=[];reads=0
for c in J['MT_controls']:
 n=c['n'];N=c['end'];seed={complex(*q)for q in c['seed']};z=sim(seed,N);reads+=N
 assert z['word']==c['complete_prefix_word'];last={q:i for i,q in enumerate(z['pts'])};par={q:(z['pts']+[z['p']])[i+1]for q,i in last.items()};assert par[v]==w and last[v]==8183 and last[w]==79196+208*n
 assert z['B'][v]==8183 and z['B'][w]==last[w]and v not in {complex(*q)for q,p in c['full_interval_tree']}
 tw,d,dead,tests=future(z['B'],z['p'],z['h']);assert tw in phases and 8183 not in dead and last[w]not in dead
 controls.append(dict(n=n,reads=N,edge=[xy(v),xy(w)],labels=[last[v],last[w]],jump=last[w]-last[v],both_permanent=True,parity_tests=tests))
out=dict(status='PASS all-n historical connector and reset-tree scope contrast',manifest=sha(MF),dependencies={**ref['dependencies'],'../audits/check_primitive_spine_clock_independent.json':sha(S.with_name('check_primitive_spine_clock_independent.json'))},full_reads=reads,controls=controls,analytic=[
'Actual common source/M prefix reads v once at R8183 and immediately reaches w; w has four source reads ending L8308. Every later pre-collision stage misses both: NE minx225, T minx2n+192, full SW minimum206 and final partial minimum204. These are complete stage ranges from the already signed all-n MT source, not arbitrary synthetic fields.',
'Actual postcollision recovery begins31806+208n, misses v, and reads w exactly once at relative R47390. The entire NW tail has y>=213 and positive y drift, so both identities are permanent. Consequently the historical parent edge v->w has labels8183 and79196+208n, with jump71013+208n for every integer n>=100.',
'All three complete original-seed histories and infinite parity fields replay independently. The old v is absent from the drought readset, so this edge does not contradict its bounded29865 reset-tree clock. It is a selected unbounded historical lower witness, not a whole-history maximum or consumed-lifetime edge.',
'No single-orbit recurrence, universal connector law, chronological Euler identity or gross leaf budget is inferred.'
])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
