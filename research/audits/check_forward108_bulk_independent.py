from pathlib import Path
from collections import Counter
from itertools import combinations
import json,hashlib,subprocess
P=Path(__file__).resolve();src=P.with_name('check_generic_bulk_criterion_independent.py');exec(compile(src.read_text().split('records=[];profile_classes=0')[0],str(src),'exec'))
J=json.loads((G/'forward108_bulk_author.json').read_text());Q=''.join('R'if c=='L'else'L'for c in P108[::-1]);assert Q==J['word']and hashlib.sha256(Q.encode()).hexdigest()==J['word_sha256']
original=profile(Q,1,2);assert trace(Q,1)[1:]==((2,2),1)
origblack={z for z,v in original.items()if v[0][1]=='L'};assert origblack=={(-8,1),(-7,0),(-6,0)}
assert all(all(a[1]!=b[1]for a,b in zip(v,v[1:]))for v in original.values())
assert sum(v[-1][1]=='R'for v in original.values())==11 and len(original)==23
p=profile(Q,3,2);reads=set(p);black={z for z,v in p.items()if v[0][1]=='L'};white=reads-black;assert black=={(6,0),(7,0),(8,1)}
assert sorted(map(list,reads))==J['read_classes'];own=[];bindex={z:i for i,z in enumerate(sorted(black))}
for orient in('NE','SW'):
 rr,bb=writer[orient];lo=min(t for t,e in rr);hi=max(t for t,e in rr)
 shifts={(t-u,(e-v)%2)for t,e in black for u,v in bb if(t-u)%2==0}
 for t,e in sorted(shifts):
  painted={z for z in reads if(z[0]-t,(z[1]-e)%2)in bb};covered=painted&black;polluted=painted&white;assert covered and polluted
  own.append(dict(orientation=orient,normal=t,x_parity=e,band=[lo+t,hi+t],covered_black=sorted(map(list,covered)),polluted_white=sorted(map(list,polluted)),cover_mask=sum(1<<bindex[z]for z in covered)))
assert own==J['candidates']and len(own)==21
C=[[-i-1]for i in range(len(own))]
C += [[i+1 for i,r in enumerate(own)if z in set(map(tuple,r['covered_black']))]for z in sorted(black)]
C += [[-i-1,-j-1]for i,j in combinations(range(len(own)),2)if max(own[i]['band'][0],own[j]['band'][0])<=min(own[i]['band'][1],own[j]['band'][1])]
cnf=G/'forward108_bulk.cnf';cc=[list(map(int,l.split()))[:-1]for l in cnf.read_text().splitlines()if l and l[0]not in'pc']
assert Counter(map(tuple,C))==Counter(map(tuple,cc))and len(C)==234
proof=json.loads(subprocess.run([str(ROOT/'causal_reduction/morphic_candidates/check_drat'),str(cnf),str(G/'forward108_bulk.rup')],check=True,capture_output=True,text=True).stdout);assert proof['valid']and proof['RUP']==1 and proof['RAT']==0
levels=[x//2 for x,y,c in trace(Q,3)[0]];assert max(levels)-min(levels)==2;assert J['constants']['parallel_flight_loss']==6 and J['constants']['nonparallel_flight_loss']==22*2*(8-(-3)+21)==1408
out=dict(status='PASS independent FORWARD108 original/rotated bulk profiles and every standard rail anchor',word_sha256=hashlib.sha256(Q.encode()).hexdigest(),original_black=sorted(origblack),read_classes=23,output_black_classes=11,rails=21,all_contributing_rails_individually_pollute=True,clauses=len(C),proof=proof,scope='Fresh origin/E forward108 instance, distinct from opposite-drift reverse108. No finite parallel mature standard bundle supplies its exact bulk input. Signed preparation lift constants2/6/1408 apply; no unproved factor3 strengthening needed.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
