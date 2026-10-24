"""Forget selected height places as unlimited resources. Exact projection only."""
from pathlib import Path
import json,sys,hashlib
src,out=map(Path,sys.argv[1:3]);keep=list(map(int,sys.argv[3].split(',')));J=json.loads(src.read_text());ix=[J['places'].index(h)for h in keep];project=lambda r:[r[i]for i in ix]
N={k:v for k,v in J.items()if k not in ['transitions','goal_requirements']};N.update(format='record_height_petri_projection_v1',base_file=str(src.resolve()),base_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),places=keep,goal_requirements=[[p,project(r)]for p,r in J['goal_requirements']],transitions=[[p,q,a,project(i),project(o)]for p,q,a,i,o in J['transitions']],scope='Forgetting every unretained height count permits unlimited tokens there; this is an overapproximation of the full height Petri model.')
out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f'{len(keep)} {len(N["positions"])} {len(N["transitions"])} {len(N["initial_controls"])} {len(N["goal_requirements"])}\n');f.write(' '.join(map(str,N['initial_controls']))+'\n')
 for p,r in N['goal_requirements']:f.write(' '.join(map(str,[p]+r))+'\n')
 for p,q,a,i,o in N['transitions']:f.write(' '.join(map(str,[p,q,a]+i+o))+'\n')
print({'places':keep})
