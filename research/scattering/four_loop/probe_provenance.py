"""Literal provenance probes; affine proof supplied separately."""
import sys,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
SRC=Path('/workspace/shared/langton/continuation_2026-10-22/ant_continuation/wake_clock')
sys.path[:0]=[str(SRC),str(SRC.parent)]
from four_scatterer_loop import build
from ant_exact import step,LEGAL10
T=json.loads((HERE/'completion_template.json').read_text())
P=T['period_word'];S=T['suffix_word']
r=next(i for i,c in enumerate(S) if c!=P[i%104])
print('second divergence offset in suffix',r)
rows=[]
for L in [128,129,192,256]:
 B,*_=build(L);p=(0,0);h=0;lastread={};word='';events=0;hits=[]
 t1=416*L+37740;t2=520*L+39714+r;capture=520*L+43111
 for t in range(capture):
  if t in [t1,t2]:
   old=lastread.get(p)
   hits.append(dict(t=t,p=p,h=h,color=p in B,lastread=old,age=None if old is None else t-old[0],expected='R' if t==t1 else P[r%104]))
  lastread[p]=(t,'L' if p in B else 'R')
  p,h,c=step(B,p,h);word=(word+c)[-10:]
  events+=len(word)==10 and word not in LEGAL10
 rows.append(dict(L=L,hits=hits,J10_windows=events))
print(json.dumps(rows,indent=2))
(HERE/'provenance_probes.json').write_text(json.dumps(rows,indent=2)+'\n')
