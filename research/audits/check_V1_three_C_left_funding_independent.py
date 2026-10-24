from pathlib import Path
import json,hashlib
P=Path(__file__).resolve();S=P.with_name('check_U1_young3_shadow_independent.py');exec(compile(S.read_text().split('rows=[];cases=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/V1_three_C_left_return_frozen_20261023_1305';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_V1_three_C_left_return_funding.json').read_text());C5={tuple(map(int,l.split()[:8]))for l in(B/'06_01_closure.tsv').read_text().splitlines()};mp={a:i for i,a in enumerate(ids)};goal=-1+0j;gh=1;r=1-1j
assert goal+rotation(1+2j,gh)==r
O=sorted(G[4][4],key=xy);exit=goal+rotation(G[4][0],gh);eh=(gh+G[4][1])%4;score=max(2*H(exit)+A[eh],*(2*H(goal+rotation(o,gh))+w[f'w_4_{i}_{gh}']for i,o in enumerate(O)));assert score==24
rows=[];first=[]
for a in ids:
 c=counts[a];h=(-G[a][1])%4;p=-rotation(G[a][0],h);slot=[o for o in G[a][4]if p+rotation(o,h)==r];assert len(slot)==1;slot=slot[0];rel=rotation(goal-p,-h);dh=(gh-h)%4;key=(mp[a],mp[4],*xy(rel),dh,*xy(slot),3+c)
 if c==2:assert 2*H(p)+A[h]==28>score;reason='earlier entry core funds'
 elif c==1:assert key in C5;reason='exact age4 selected clause'
 elif a in(4,7):assert key in C5;reason='exact age3 V/U clause'
 else:
  assert a==0 and key not in C5 and(rel,dh)==(1j,1)
  # Universal3C marker near-return would forbid a noninitial D predecessor.
  inp=p+rotation(next(iter(G[a][3])),h);assert inp==-1 and 28+2*H(inp)==26>score;reason='D factor-first then initial input funds'
 rows.append(dict(predecessor=a,pose=[*xy(p),h],bud_output=list(xy(slot)),bud_age=3+c,relative_target=[*xy(rel),dh],counted_query=list(key),counted_excluded=key in C5,reason=reason))
 assert 2+0j in G[a][4]
 activation=28+2*max(map(H,G[a][3]));assert activation>=30>score;first.append([a,activation])
AA={q['predecessor']:q for q in J['predecessor_cases']}
for row in rows:
 for k in('pose','bud_output','bud_age','relative_target','counted_query','counted_excluded'):assert row[k]==AA[row['predecessor']][k]
assert sum(r['counted_excluded']for r in rows)==5
result=dict(status='PASS independent all-source three-C left-step V1 funding',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),goal_score=score,predecessors=rows,first_source_activations=first,scope='Any marked A0N then V at(-1,0,E), exact3C, complete recurrent8 full record/I>=28. Universal bud origin plus five signed counted clauses and one recursive noninitial-marker cut force funding. No A-output survival premise, no wholeV1/12th record/capture.')
P.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items()if k!='predecessors'})
