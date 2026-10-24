"""Finite ingredients for the all-length opposed-run interior crossing lemma."""
import itertools,json,hashlib
from pathlib import Path
ROOT=Path(__file__).parent
SOURCE=ROOT.parent/'continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json'
D=json.loads(SOURCE.read_text());VEC=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):
 x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h]
def literal(w,p,h):
 first={};last={};trace=[]
 for a in w:
  for phase,c in enumerate(D[a]['word']):
   row=(len(trace),a,phase,c,p);first.setdefault(p,row);last[p]=row;trace.append(row)
   h=(h+(1 if c=='R' else -1))%4;d=VEC[h];p=p[0]+d[0],p[1]+d[1]
 return first,last,p,h,trace
for a in 'UVQB':
 f,l,p,h,tr=literal(a,(0,0),0)
 assert tuple(D[a]['end_pose'])==(*p,h)
 assert [(t[4],t[3])for t in tr]==[(tuple(t['p']),t['c'])for t in D[a]['trace']]
 if a in'UV':
  assert h==0 and min(t[4][1]for t in tr)==-1 and max(t[4][1]for t in tr)==p[1]
 else:assert min(t[4][1]for t in tr)>=-5

def window(w,h):
 disp=tuple(sum(D[a]['end_pose'][j]for a in w[:2])for j in range(2));d=rot(disp,h)
 centerhead=(0,0)if h==0 else(-1,1);start=centerhead[0]-d[0],centerhead[1]-d[1]
 f,l,end,hh,tr=literal(w,start,h);assert hh==h
 return f,l,start,end
rows=[]
for a,b in [('U','V'),('V','U')]:
 aw=[''.join(w)for w in itertools.product('UV',repeat=5)if w[1]==w[2]==a]
 bw=[''.join(w)for w in itertools.product('UV',repeat=5)if w[1]==w[2]==b]
 assert len(aw)==len(bw)==8
 for x in aw:
  af,al,astart,aend=window(x,0)
  for y in bw:
   bf,bl,bstart,bend=window(y,2)
   choices=[]
   for q in al.keys()&bf.keys():
    if al[q][3]!=bf[q][3]:continue
    if not astart[1]<q[1]<aend[1]-1:continue
    if not bend[1]+1<q[1]<bstart[1]:continue
    if not q[1]<aend[1]-5:continue
    choices.append(q)
   assert choices,(x,y)
   q=min(choices,key=lambda p:(p[1],p[0]));rows.append(dict(north=x,south=y,cell=q,letter=al[q][3],north_last=al[q],south_first=bf[q],north_window_start=astart,north_window_end=aend,south_window_start=bstart,south_window_end=bend))
assert len(rows)==128
out={'status':'PASS','statement':'interior straight U / straight V opposed-run crossing obstruction','source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'cases':rows}
(ROOT/'uv_interior_crossing_certificate.json').write_text(json.dumps(out,indent=2))
print('PASS: 128 exact local cases, literal word binding, run shielding, fold shielding')
