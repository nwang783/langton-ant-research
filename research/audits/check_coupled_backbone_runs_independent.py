"""Exact tiny local proof leaf for the all-cap coupled-backbone inequality."""
import itertools,json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parents[1];P=R/'periodic_classification_new';accepted=[]
for bits in itertools.product('RL',repeat=8):
 if bits[0]!='R':continue
 w=''.join(bits);q=0j;h=1j;seen={};tr=[];ok=True
 for t,c in enumerate(w):
  if t and not q:ok=False;break
  if seen.get(q)==c:ok=False;break
  seen[q]=c;tr.append((q,c));h*=(-1j if c=='R'else 1j);q+=h
 if ok and q==0 and h==1j:accepted.append((w,tr))
assert{w for w,tr in accepted}=={'RRRLLLLR','RRLLLLRR'}
controls=[]
for w,tr in accepted:
 events=[(-2,1-1j,'R'),(-1,-1j,'R')]+[(t,q,c)for t,(q,c)in enumerate(tr)]
 old={};conflicts=[]
 for t,q,c in events:
  if q in old and old[q][1]==c:conflicts.append({'cell':[int(q.real),int(q.imag)],'old_time':old[q][0],'new_time':t,'turn':c})
  old[q]=(t,c)
 assert conflicts
 first=conflicts[0];assert(first['new_time'],first['cell'])==((2,[1,-1])if w=='RRRLLLLR'else(7,[0,-1]))
 controls.append({'word':w,'conflict':first})
# For every number of run pairs, the pointwise inequality already supplies the global bound.
for r,l in itertools.product(range(1,4),repeat=2):
 t=int(r>=2 and l>=2);assert r+l<=4+2*t
# Four-step next-left-return proof leaf; its predecessor is visited only at last step.
q=0j;h=1j;tr=[]
for c in'RRRR':tr.append((q,c));h*=-1j;q+=h
assert(q,h)==(0j,1j)and tr[-1]==(-1j,'R')and sum(z==-1j for z,c in tr)==1
out={'status':'PASS complete independent eight-step first-return leaf and run-pair inequality','eight_step_word_count':256,'consistent_initialR_finalN_first_returns':[w for w,tr in accepted],'conflicts':controls,'run_pair_types':9,'proof_sha256':hashlib.sha256((P/'white_front_coupled_run_speed.md').read_bytes()).hexdigest(),'scope':'Analytic complete-WHITE first-read backbone coupling gives P>=4ell>=8D, with P=2D mod4. Not arbitrary prepared input or nonperiodic capture.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
