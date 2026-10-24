from pathlib import Path
from collections import defaultdict
import json,random
ROOT=Path(__file__).resolve().parents[1];S=ROOT/'audits/check_short_refinement_cnf_independent.py';exec(compile(S.read_text().split('# White palette semantic reconstruction')[0],str(S),'exec'))
Q=json.loads((U/'forward108_prepared_control.json').read_text())['word'];matches=[]
for j,c in enumerate(H):
 for k,w in enumerate(palette[c]):
  if H[:j]+w+H[j+1:]==Q:matches.append((j,k))
assert matches
j,k=matches[0];selQ=[k if i==j else 0 for i in range(104)]
rng=random.Random(202610231323);controls=[([0]*104,'identity'),(selQ,'forward108')]
for a in range(24):
 sel=[0]*104
 for p in rng.sample(range(104),rng.randint(1,5)):sel[p]=rng.randrange(1,10)
 controls.append((sel,'sparse'))
results=[]
for sel,label in controls:
 word=''.join(palette[c][k]for c,k in zip(H,sel));hist=fullhist(word,(0,0),3);inp={q for q,v in hist.items()if v[0][1]=='L'};legal=all(all(a[1]!=b[1]for a,b in zip(v,v[1:]))for v in hist.values())
 nv,clauses,groups,gates=build(H,(0,0),inp,False);v={1:True}
 for j,k in enumerate(sel):
  for l in range(10):v[2+10*j+l]=k==l
 def lit(x):return v[abs(x)]if x>0 else not v[abs(x)]
 active=defaultdict(list)
 for key,ev,xs,prev,a,n in gates:
  v[a]=any(lit(x)for x in xs);v[n]=lit(prev)!=v[a]
  if v[a]:active[key].append(ev[3])
 assert dict(active)=={key:[c for t,c in hist0]for key,hist0 in hist.items()}
 assert all(any(lit(x)for x in cl)for cl in clauses)==legal
 results.append(dict(label=label,length=len(word),input_classes=len(inp),legal=legal))
assert results[0]['legal']and results[0]['input_classes']==0 and results[1]['legal']and results[1]['input_classes']==3
out=dict(status='PASS independent forward free-input circuit positives and sparse controls',forward108_single_image=matches[0],controls=results,scope='Prepared forward108 and unchanged white H are legal. They do not assert a compatible mature rail input for nonidentity or any nonstationary result.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
