from pathlib import Path
from collections import Counter,defaultdict
import json,hashlib,ast
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();files={'prepared_F84_F85_realize_the_one_use_LL_drop.md':'744df9cb','prepared_F84_F85_mandatory_count_and_scope_qualifier.md':'41379bcf','check_prepared_F84_F85_LL_drop.py':'61556df0','check_prepared_F84_F85_LL_drop.json':'efb23df8'}
for f,h in files.items():assert sha(D/f).startswith(h)
J=json.loads((D/'check_prepared_F84_F85_LL_drop.json').read_text());H='NESW';V=(1j,1,-1j,-1);xy=lambda p:[int(p.real),int(p.imag)];target={1+0j:'WWEW',1+1j:'SSN',2+0j:'SNNN',2+1j:'EE'};summ=[];ends=[]
for row in J['controls']:
 seed={complex(*q)for q in row['initial_black']};B=set(seed);p=complex(*row['start'][0]);h=H.index(row['start'][1]);hist=defaultdict(list);edges=[];birth={q:-i-1 for i,q in enumerate(sorted(seed,key=lambda q:(q.real,q.imag)))};owners=[];first={}
 for t,want in enumerate(row['word']):
  c='L'if p in B else'R';assert c==want;old=birth.get(p);before=sorted(map(xy,B));hist[p].append(dict(t=t,incoming=H[h],turn=c));first.setdefault(p,t)
  if c=='L':B.remove(p);birth.pop(p)
  else:B.add(p);birth[p]=t
  nh=(h+(1 if c=='R'else-1))%4;q=p+V[nh];assert row['trace'][t]==dict(t=t,cell=xy(p),incoming=H[h],turn=c,black_before=before,black_after=sorted(map(xy,B)),next_cell=xy(q),next_incoming=H[nh]);edges.append((p,q))
  if p in target and c=='L':assert old is not None and old>=0;owners.append((xy(p),old,t))
  p,h=q,nh
 assert row['end']==[xy(p),H[h]]==[[1,-1],'S']and sorted(map(xy,B))==row['final_black']and row['mass']==[len(seed),len(B)]and row['turns']==dict(Counter(row['word']));assert len(hist)==row['physical_cells_read']==58 and max(map(len,hist.values()))==row['factor_max_reads']==4 and p in B
 for q,word in target.items():
  assert q not in seed and ''.join(e['incoming']for e in hist[q])==word and ''.join(e['turn']for e in hist[q])==''.join('RL'[i%2]for i in range(len(word)));assert hist[q]==row['target_histories'][str(tuple(xy(q)))]
  if row['name']=='F85':assert first[q]>0 and edges[first[q]-1][1]==q
 assert sum(len(hist[q])for q in target)==13
 for e in row['selected_one_use_edges']:assert edges.count(tuple(complex(*q)for q in e))==1
 assert{str(tuple(xy(q))):ls for q,ls in hist.items()}==row['histories'];ends.append(B);summ.append(dict(name=row['name'],reads=len(row['word']),mass=row['mass'],cells=len(hist),target_owned_R_L=owners))
assert ends[0]==ends[1]and J['controls'][1]['word']=='L'+J['controls'][0]['word'];assert set(map(tuple,J['controls'][1]['initial_black']))==set(map(tuple,J['controls'][0]['initial_black']))|{(1,2)}
for q in target:
 a=J['controls'][0]['target_histories'][str(tuple(xy(q)))];b=J['controls'][1]['target_histories'][str(tuple(xy(q)))];assert[t['t']+1 for t in a]==[t['t']for t in b]
O=dict(status='PASS literal prepared F84/F85 LL-drop factors with mandatory count/scope qualifier, not full fronts',files={f:sha(D/f)for f in files},script=sha(S),controls=summ,analytic_review=[
'Every84/85 read is independentlyreplayed from the ENTIRE prelaid20/21-cellseed; everyfullbefore/afterboard and physicalpose matches. No discoverylazyseed snapshots are used. Exact58physicalcells, maxfactor4,50R/34or35L,final36cells andsameendpoint1,-1,S are confirmed.',
'Allfour namedtargetcells startWHITE and have exactlythe13 displayedfactorreads; each targetL has an actual earlierinternalR owner. Allthree selectedphysicaldirectededges occuronce. F85 supplieseverytargetR0 througharealpreviousedge, but its initialoutsideL is explicitlyBLACK-first.',
'F84endpointBLACK forbids its immediateR-startrepeat. SamefinalF84/F85field doesnotmean start=endfield, full-drift classcompletion, GLOBALM, essentialb-circle, fullfuture or autonomousregeneration. The mandatoryqualifier corrects62to58 and disclaims the unsupportedatomic-bud implication. This is only actualfinitepreparedrealization of the retainedlocalLLescape.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(summ);print(sha(S.with_suffix('.json')))
