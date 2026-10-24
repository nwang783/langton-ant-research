"""Independent complex-heading replay of the finite ingredients, no stored footprints."""
import itertools,json,hashlib
from pathlib import Path
R=Path('/workspace/shared/langton')
P=R/'continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json'
D={a:x['word'] for a,x in json.loads(P.read_text()).items()}
assert all(set(D[a])<={'L','R'} for a in 'UVQB')
def walk(w,p=0j,h=1j):
 t=[]
 for a in w:
  for c in D[a]:
   t.append((p,c));h*=(-1j if c=='R' else 1j);p+=h
 return t,p,h
for a in 'UVQB':
 t,p,h=walk(a)
 if a in 'UV':
  assert h==1j and p==({'U':4j,'V':1+3j}[a])
  assert min(q.imag for q,c in t)==-1 and max(q.imag for q,c in t)==p.imag
 else:
  assert h==-1j and min(q.imag for q,c in t)>=-5
  assert p+(1-1j)==({'Q':-3-5j,'B':-2-6j}[a])
def window(w,south):
 h=-1j if south else 1j;center=(-1+1j)if south else 0j
 _,d,_=walk(w[:2],h=h);start=center-d
 t,end,hh=walk(w,start,h);assert hh==h
 assert walk(w[:2],start,h)[1]==center
 return t,start.imag,end.imag
rows=[]
for c in 'UV':
 d='V' if c=='U' else 'U'
 for abc in itertools.product('UV',repeat=3):
  a=abc[0]+c+c+abc[1]+abc[2];ta,sa,ea=window(a,False)
  for xyz in itertools.product('UV',repeat=3):
   b=xyz[0]+d+d+xyz[1]+xyz[2];tb,sb,eb=window(b,True)
   last={p:(i,l)for i,(p,l)in enumerate(ta)};first={}
   for i,(p,l) in enumerate(tb):first.setdefault(p,(i,l))
   witnesses=[p for p in last.keys()&first.keys() if last[p][1]==first[p][1] and sa<p.imag<ea-1 and eb+1<p.imag<sb and p.imag<ea-5]
   assert witnesses,(a,b)
   q=min(witnesses,key=lambda p:(p.imag,p.real))
   rows.append({'north':a,'south':b,'witness':[int(q.real),int(q.imag)],'north_last':last[q],'south_first':first[q]})
assert len(rows)==128
out={'status':'PASS','independent_implementation':'complex headings, literal words, no stored footprints','source_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'cases':rows}
(R/'audits/uv_crossing_independent.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS 128 independent crossing witnesses; exact center and shielding geometry')
