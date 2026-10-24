from pathlib import Path
from itertools import product
import json,hashlib
P=Path(__file__);R=P.parent.parent;S=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();bind={'flow2_flat_departure_segment_has_forbidden_five_corner_word.md':'90b57415b706c255d35db0270f148419bf99bc0a421e3fa72f0fb1813594aafc','check_flow2_staircase_flat_segment_obstruction.py':'e9c5e1577e694b2a8ad8f6e703c02e6ec125caaeaf49ba298cf992f365ca0d23','check_flow2_staircase_flat_segment_obstruction.json':'d98e803ca60b15cd732559f6c67dbf90d0541eec3a74fd6613056a7fc90bc788'}
for n,h in bind.items():assert sha(S/n)==h
ref=json.loads((S/'check_flow2_staircase_flat_segment_obstruction.json').read_text());hs='NESW';v=[1j,1,-1j,-1];out=lambda w,j:hs[(hs.index(w[j])+(1 if j%2==0 else-1))%4];xy=lambda z:[int(z.real),int(z.imag)]
base={-1j:'WWEE',0j:'NSSN',1+0j:'WWEE',1+1j:'NSSN',2+1j:'WWEE'}
assert [{'cell':xy(p),'headings':w}for p,w in base.items()]==ref['given_complete_histories']
candidates=[]
for n in range(1,5):
 for z in product('NS',repeat=n):
  w=''.join(z);ss=[j for j,h in enumerate(w)if h=='S'];ww=[j for j in range(n)if out(w,j)=='W']
  if len(ss)==len(ww)==2:candidates.append(dict(headings=w,first_W_rank=ww[0],second_S_rank=ss[1],can_return_in_four=ss[1]==ww[0]+1))
assert candidates==ref['D_candidates']and[r['headings']for r in candidates if r['can_return_in_four']]==['SSNN']
full=base|{1-1j:'SSNN',2+0j:'SSNN'};edges={};op=[];ip=[]
for p,w in full.items():
 for h in hs:
  sr=[j for j in range(len(w))if out(w,j)==h];q=p+v[hs.index(h)]
  if q in full:
   tr=[j for j,x in enumerate(full[q])if x==h];assert len(sr)==len(tr)
   for a,b in zip(sr,tr):edges[p,a]=(q,b)
  else:
   for k,a in enumerate(sr):op.append(dict(source=xy(p),rank=a,heading=h,target=xy(q),outgoing_ordinal=k+1))
 for j,h in enumerate(w):
  q=p-v[hs.index(h)]
  if q not in full:ip.append(dict(target=xy(p),rank=j,heading=h,source=xy(q),incoming_ordinal=[a for a,x in enumerate(w)if x==h].index(j)+1))
canon=lambda xs:{json.dumps(x,sort_keys=True)for x in xs}
assert canon(op)==canon(ref['all_named_outgoing_open_ports'])and canon(ip)==canon(ref['all_named_incoming_open_ports'])
assert canon([dict(source=xy(p),source_rank=j,target=xy(q),target_rank=k)for(p,j),(q,k)in edges.items()])==canon(ref['all_named_internal_edges'])
chains=[]
for row in ref['forced_return_chains']:
 seq=row['path'];a=complex(*seq[0]['cell']);b=complex(*seq[-1]['cell']);assert a==b and all(complex(*z['cell'])!=a for z in seq[1:-1])
 if row['steps']==4:
  assert len(seq)==5 and seq[0]['rank']==0 and seq[-1]['rank']==1
  for x,y in zip(seq,seq[1:]):assert edges[complex(*x['cell']),x['rank']]==(complex(*y['cell']),y['rank'])
 else:
  assert row['steps']==8 and len(seq)==9 and a==2-1j
  assert seq[1]=={'cell':[2,0],'rank':3}and full[2j-2j+2][3]=='N'
  nr=[j for j,h in enumerate(full[2])if h=='N'];assert nr==[2,3] # rank3 is SECOND incoming N, not third.
  for x,y in zip(seq[1:-2],seq[2:-1]):assert edges[complex(*x['cell']),x['rank']]==(complex(*y['cell']),y['rank'])
  assert seq[-2]=={'cell':[1,-1],'rank':1};assert [j for j in range(4)if out(full[1-1j],j)=='E']==[1,2]
 chains.append(row)
# Check all four actual first-R displayed departure edges and exact total flow2.
for p,q in [(-1j,0j),(0j,1+0j),(1+0j,1+1j),(1+1j,2+1j)]:
 h=out(base[p],0);assert p+v[hs.index(h)]==q and sum(out(base[p],j)==h for j in range(4))==2
outj=dict(status='PASS fixed five-corner flow2 staircase word impossible under WHITE cap4 outside histories; general one-use remains open',bindings=bind,D_candidates=candidates,three_literal_paths=chains,internal_edges=len(edges),outgoing_open_ports=len(op),incoming_open_ports=len(ip),analytic_review=['Actual physical cells used without quotienting, so all possible full-drift aliases can only add constraints. Exact complete ports force D S-count2/W-count2 and four WHITE cap4 candidates; first-W to second-S is a first return in4 moves, retaining only consecutive ranks0/1 SSNN.','Unknown E has exactly2 incoming E and2 outgoing N by the forced neighboring complete histories, but otherwise unbounded multiplicity and either first color. Its second N departs before its FIRST incoming E, hence is R(W); next read L(E) would be a third N departure.','Eight-step E return is literal, every intermediate ordinal matched and no intermediate E read. The contradiction is adjacency of complete read ranks/alternation, not a short-time heuristic.','No other flow2 profile, variable-turn segment, complete front, period or drift classification is inferred.','Minor nonmathematical author-code comment says third N arrival at D1 rank3; physical list is second N arrival (ranks2/3). Note and JSON give correct L3 and all equations are correct.'])
P.with_suffix('.json').write_text(json.dumps(outj,indent=2)+'\n');print(outj['status'])
