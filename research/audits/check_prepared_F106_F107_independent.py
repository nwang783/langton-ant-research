from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib,ast
S=Path(__file__).resolve();R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
f={'prepared_F106_F107_realize_an_odd_root_mixed_portal_patch.md':'877ee07b8355c896303ad4f53a86a0e89992163195c3a44c2223bf9e64c712f9','check_prepared_F106_F107_odd_portal.py':'55dce079a91b1cf4925c2acd293f5f1c02bc0a42ff346ee7f86b63034c27831d','check_prepared_F106_F107_odd_portal.json':'c9b39d4d0f828b0bdf35fe23efaf84ed64e8b2a468b899d8c7a03c0bf44e58b4'}
f['prepared_F106_F107_mandatory_visited_cell_qualifier.md']='e89591de1ec474763abf0c5fb4092da29590c241f59279ab28e3dbecb92007b2'
for p,h in f.items():assert sha(D/p)==h
J=json.loads((D/'check_prepared_F106_F107_odd_portal.json').read_text());V=(1j,1,-1j,-1);HN='NESW';xy=lambda p:[int(p.real),int(p.imag)];sort=lambda z:sorted(map(xy,z));controls=[]
for n,z in enumerate(J['controls']):
 seed={complex(*q)for q in z['initial_black']};B={q:('initial',xy(q))for q in seed};p=complex(*z['start'][0]);h=HN.index(z['start'][1]);hist=defaultdict(list);edges=Counter();ev=[]
 for t,c in enumerate(z['word']):
  ar=z['trace'][t];assert ar['cell']==xy(p)and ar['incoming']==HN[h]and ar['turn']==c and ar['black_before']==sort(B);assert(p in B)==(c=='L');old=B.get(p)
  if c=='L':del B[p]
  else:B[p]=('R',t)
  ho=(h+(1 if c=='R'else-1))%4;q=p+V[ho];assert ar['black_after']==sort(B)and ar['next_cell']==xy(q)and ar['next_incoming']==HN[ho]
  ev.append((p,h,c,q,old));hist[p].append(t);edges[p,q]+=1;p,h=q,ho
 assert p==3 and h==1 and p not in B and len(B)==34 and len(hist)==63 and max(map(len,hist.values()))==4 and sort(B)==z['final_black']
 assert z['physical_cells']==len(hist)+2==65 and z['factor_max_reads']==4 and z['R']==60 and z['L']==46+n and len(seed)==20+n and len(ev)==106+n
 for qq,rr in z['all_cell_histories'].items():
  q=complex(*ast.literal_eval(qq));ts=hist.get(q,[]);assert ts==rr['times']and ''.join(HN[ev[t][1]]for t in ts)==rr['history']and ''.join(ev[t][2]for t in ts)==rr['turns']and(q in seed)==rr['initial_BLACK']
 for qq,rr in z['targets'].items():
  q=complex(*ast.literal_eval(qq));ts=hist.get(q,[]);assert q not in seed and rr['times']==ts and rr['history']==''.join(HN[ev[t][1]]for t in ts)and rr['final_BLACK']==(q in B)
  assert ''.join(ev[t][2]for t in ts)==('RL'*3)[:len(ts)]
  if ts and(n or ts[0]):assert ts[0]>0 and ev[ts[0]-1][3]==q
 assert sum(bool(rr['history'])for rr in z['targets'].values())==14 and sum(not rr['history']for rr in z['targets'].values())==2
 path=list(map(lambda q:complex(*q),z['selected_physical_path']));assert[edges[a,b]for a,b in zip(path,path[1:])]==z['selected_edge_uses']==[1,1,1,2,2,2,1]
 assert hist[1+1j]==[79+n,87+n,91+n,95+n]and hist[2]==[89+n,97+n,105+n]and hist[1]==[90+n]
 assert hist[2-1j]==[16+n,104+n]and[ev[t][2]for t in hist[2-1j]]==['L','R']and ev[104+n][3]==2 and ev[90+n][3]==1+1j
 controls.append(dict(name=z['name'],mass=[len(seed),len(B)],counts=[len(ev),len(hist),max(map(len,hist.values()))],whole_seed=sort(seed),whole_final=sort(B),guide=[(t,ev[t][2],ev[t][4])for t in hist[2-1j]],q_times=hist[1+1j],X_times=hist[2],end=[xy(p),HN[h]]))
a,b=J['controls'];assert b['word']=='L'+a['word']and set(map(tuple,b['initial_black']))==set(map(tuple,a['initial_black']))|{(3,3)}and a['final_black']==b['final_black']
report=dict(status='PASS prepared F106/F107 finite factors WITH mandatory visited-cell qualifier e89591de',bindings=f,metadata_discrepancy='Frozen physical_cells=65 counts two inserted empty histories; actual visited physical cells=63. Mandatory e89591de qualifier bound; original artifacts unchanged.',controls=controls,analytic_review=[
'Both full prelaid seeds, every actual board before/after each read, every heading/cell/ordinal, all63 visited cells and every target/guide history reconstruct. No lazy-seed interim state is imported.20/21BLACK inputs yield identical34BLACK output;106/107reads, maximum4.',
'Fourteen named visited targets startWHITE with exactly the supplied histories, including ODD rootSNN; two additional named cells remain unreadWHITE. F107 prepends one genuine preparedBLACK L at(3,3), supplying every target first read without changing the final field. Its old three-visit guide becomes four-read, not a new64th visited cell.',
'The complete selected path has edge-use counts1,1,1,2,2,2,1. q at79/87/91/95 and X at89/97/105 preserve the older/future ordinals. v first observedR90 supplies q.R2, not q.R0. Southern guide beginsBLACK L16, laterR104 supplies X.R2; no whole-history firstR ownership is inferred from that factor-observed birth.',
'Endpoint(3,0),E isWHITE but starting headingW differs, so no restored-pose translation period is supplied. This is a genuine connected prepared finite factor, not completeWHITE full histories, GLOBAL-M field, essential b-circle, recurrent connector, guide funding, full future or autonomous controller. Even-root exclusion is not challenged by this odd-root control.'
])
S.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print(report['status']);print(sha(S.with_suffix('.json')))
