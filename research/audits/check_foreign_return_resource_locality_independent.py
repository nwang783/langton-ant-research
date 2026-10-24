from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23';Q=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
author=json.loads((D/'foreign_return_resource_locality.json').read_text());J=json.loads(Q.read_text());dirs=(1j,1,-1j,-1);M='LLLLRLRRRRL'
def walk(w):
 p=0j;h=0;odd=set();requirements={};trace=[]
 for a in w:
  needed=(a=='L')^(p in odd)
  assert p not in requirements or requirements[p]==needed
  requirements[p]=needed;trace.append((p,h,a));odd.symmetric_difference_update({p});h=(h+(1 if a=='R'else-1))%4;p+=dirs[h]
 return p,h,odd,requirements,trace
def xy(q):return[int(q.real),int(q.imag)]
def points(s):return sorted(map(xy,s))
K={q for q,c in walk(M)[3].items()if c};assert K=={-1-1j,-1, -1j,0,1}
rows=[]
for name,wrow,ref in zip('DCVUFQB',J['macro_words'],author['rows']):
 w=wrow['word'];p,h,odd,_,tr=walk(w);_,_,_,ctx,ctr=walk(w+M);initial={q for q,c in ctx.items()if c};newK={p+q*(-1j)**h for q in K};final=initial^odd;I=initial-K;O=final-newK
 assert K<=initial and newK<=final
 last={q:a for q,h,a in tr};assert all(last.get(q)=='R'for q in O)
 rawset={q for q,h,a in tr};markeronly=I-rawset
 radius=lambda t:max(max(abs(q.real),abs(q.imag))for q,h,a in t)
 row=dict(name=name,endpoint=xy(p)+[h],mass_gain=w.count('R')-w.count('L'),input_slots=points(I),output_slots=points(O),recycled_slots=points(I&O),raw_read_radius=int(radius(tr)),complete_context_radius=int(radius(ctr)),marker_occurrences=[i for i in range(len(w)+1)if(w+M)[i:i+11]==M],requirements=sorted([[*xy(q),int(c)]for q,c in ctx.items()]))
 for k,v in row.items():assert ref[k]==v,(name,k)
 assert row['marker_occurrences']==[0,len(w)]and wrow['start_marker']==M+('L'if name=='D'else'R')
 if name in'FQB':assert len(markeronly)==1
 rows.append(dict(name=name,length=len(w),I=len(I),O=len(O),rawradius=row['raw_read_radius'],ctxradius=row['complete_context_radius'],marker_only=points(markeronly),mass=row['mass_gain']))
assert max(r['ctxradius']for r in rows)==6
assert [(r['I'],r['O'],r['mass'],r['rawradius'],r['ctxradius'])for r in rows[4:]]==[(14,16,2,5,6),(15,21,6,5,6),(18,24,6,5,6)]
for f,h in author['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
note=D/'foreign_return_resource_locality.md';assert hashlib.sha256(note.read_bytes()).hexdigest()=='e5a0b512e59f1a07d6f1bced8517b7d653521b99d4ea07bf1863eb087e31f089'
out=dict(status='PASS exact foreign ledgers and total finite-support spatial return operator',note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),rows=rows,analytic=['The post-A board has exactly m+delta_A blacks, so the actual intervening raw DCUV duration is bounded by the signed monotone total L(m+delta_A), not L(m).','A raw radius5 and post-A endpoint radius5 yield write ball H+5. Every candidate seven-word-plus-M11 read, including the first rejected prefix bit, is within6 of its current cut, giving query radius H+11. Complete lookahead occurs on a copy; returned state is the next foreign entry or last valid cut.','Identical mass and query-ball colors give identical literal parser evolution; separate exterior black sets remain unchanged outside the write ball. No arbitrary travel after the first language mismatch is included.','The next-foreign entry return convention differs from the post-foreign graph convention. Original 214-state successor sets remain a correspondence; missing successors do not prove capture.'],scope='Finite complete support and verified foreign source only. Total computable per-state return/EXIT, with changing mass and spatial radius; no uniform finite-state bound, contraction, global graph coverage or extension of eight-language lifetime/permanence.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(rows)
