from pathlib import Path
from itertools import product
import json,hashlib
S=Path(__file__);D=S.parents[1]/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'LL_root_post_X_is_forced_into_a_flat_RR_cap.md';F=D/'check_LL_post_X_RR_cap_corrected_edges.json';assert sha(P).startswith('2554859e')and sha(F).startswith('2a0ba830')and sha(D/'check_LL_post_X_RR_cap_corrected_edges.py').startswith('44641ba0');J=json.loads(F.read_text());H='NESW';V=[1j,1,-1j,-1]
def outs(w):return [H[(H.index(c)+(1 if i%2==0 else -1))%4]for i,c in enumerate(w)]
def idx(seq,c):return [i for i,x in enumerate(seq)if x==c]
# Full four-read-or-shorter E-axis domains, no first-heading omission.
domain=[''.join(w)for n in range(1,5)for w in product('EW',repeat=n)];allowed=[w for w in domain if w[0]=='E'and w.count('E')==2 and outs(w).count('N')==2 and outs(w).count('S')>=2];assert allowed==J['all_C_histories']==['EEWW','EWWE']
base=json.loads(S.with_name('check_cyclic_LL_reactivation_independent.json').read_text());assert base['status'].startswith('PASS');assert {r['histories']['(2, 0)']for r in base['necessary_inventories']}=={'NNS','NNSS'}
rows=[]
for rw,cw in product(['NNS','NNSS'],allowed):
 hs={1+0j:'EEWW',1-1j:'NNSS',2-1j:cw,2+0j:rw};succ={}
 for p,w in hs.items():
  for h,d in enumerate(V):
   if p+d not in hs:continue
   a=idx(outs(w),H[h]);b=idx(hs[p+d],H[h]);assert len(a)==len(b)
   succ.update({(p,i):(p+d,j)for i,j in zip(a,b)})
 ei=idx(cw,'E')[1];no=idx(outs(cw),'N')[1];assert ei<=no
 for u,v in [((1+0j,3),(1-1j,3)),((1-1j,3),(2-1j,ei)),((2-1j,no),(2+0j,1)),((2+0j,1),(1+0j,2))]:assert succ[u]==v
 row=next(r for r in J['rows']if r['R']==rw and r['C']==cw);assert row['second_E_arrival_rank']==ei and row['second_N_departure_rank']==no;rows.append(row)
reports=['check_cyclic_LL_reactivation_independent.json','check_mixed_flow2_flat_islands_independent.json','check_mixed_LL_gate_independent.json','check_mixed_RR_closure_independent.json'];assert all(json.loads(S.with_name(f).read_text())['status'].startswith('PASS')for f in reports)
assert sha(D/'LL_post_X_RR_gate_south_arrival_ordinal_correction.md').startswith('09e98e96')
O={'status':'PASS genuine LL-root post-X must immediately begin a flat RR cap','proof':sha(P),'mandatory_correction':sha(D/'LL_post_X_RR_gate_south_arrival_ordinal_correction.md'),'certificate':sha(F),'script':sha(S),'dependencies':{f:sha(S.with_name(f))for f in reports},'four_cores':rows,'analytic_review':['The signed six complete cyclic inventories supply R=NNS/NNSS and actual R.L1->X.R2; fixed off-cycle8a controls are not used. If the immediate nextB wereLEFT, incomingflow2 plus critical flat-island gate excludes crossingO/U afterX, leaving passiveNNSS. If nextC wereLEFT, the signed mixedLL rows with flat precedingRIGHT requireY, contrarytoX. ThusC isRIGHT incomingE.','Complete physical ports B->C have exactlytwoE arrivals, C->R exactlytwoN departures. Exhausting every complete1..4 E-axis history with actualRIGHTfirstE and nooneuse selectedoutflow yields onlyEEWW/EWWE. This is not a guessed exterior reader or assumedfirstreturn.','All four actual ordinal cores are reconstructed independently. CORRECTED X3->B3 and B3->C.Esecond give Esecond=X3+2; C.Nsecond->R1->X2 puts Nsecond=X2-2, strictlybeforeX3. Both retained complete histories requireEsecond<=Nsecond, contradiction. Full-drift aliases cannot alter physical consecutive ordinal edges or strict rank order.','Therefore actual successor ofX isRIGHT, and signed generalRR forces it flat. Root-to-firstX injection is only cyclic predecessor uniqueness; a cap can precede another root. No additional curvature deficit, owner injection, loop deletion, fuel or generalfront exclusion follows. Main criticalGLOBALM/completeWHITEcap4/nooneuse scope retained.']};S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
