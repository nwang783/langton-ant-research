"""Independent finite physical chronology and inherited-region reconstruction."""
from pathlib import Path
from itertools import product,combinations
from collections import defaultdict,Counter
import hashlib,json,subprocess,random
ROOT=Path(__file__).resolve().parents[1];U=ROOT/'causal_reduction/unit_scale';O=U/'nonstationary_short_slab'
s=(ROOT/'audits/check_short_refinement_cnf_independent.py').read_text();exec(compile(s.split('# White palette semantic reconstruction')[0],str(ROOT/'audits/check_short_refinement_cnf_independent.py'),'exec'))
A=json.loads((O/'architecture.json').read_text());result=json.loads((O/'result.json').read_text())
# No producer builder imported. Derive all choices directly from the independently enumerated palette.
G=defaultdict(lambda:defaultdict(list));offsets=defaultdict(set);C=[[1]]
for r in range(5):
 coarse,end,h=walk(REV,(-2*r,-2*r),3);assert (end,h)==((-2*r-2,-2*r-2),3)
 for j,(x,y,hh,c) in enumerate(coarse):
  xs=[2+10*(104*r+j)+k for k in range(10)];C.append(xs);C.extend([[-a,-b]for a,b in combinations(xs,2)])
  for k,w in enumerate(palette[c]):
   reads,e,eh=walk(w,(x,y),hh);assert (e,eh)==walk(c,(x,y),hh)[1:]
   for i,(u,v,_,turn)in enumerate(reads):
    G[u,v][r,j,i,turn].append(xs[k])
    if r==0:offsets[u-v,u%2].add(u//2)
assert set(offsets)=={(t,e)for t in range(-8,7)for e in(0,1)}
assert min(min(v)for v in offsets.values())==-2 and max(max(v)for v in offsets.values())==2
# All earlier periods -j touch exactly the upper ray L_a+1,... on each orbit.
# Verify the finite generators against the symbolic ray for a substantial arbitrary endpoint;
# the universal identity follows from j>=1 and the generator at L_a itself.
for orbit,ls in offsets.items():
 lo=min(ls)
 for k in range(lo-5,lo+31):assert any(k-l>=1 for l in ls)==(k>=lo+1)
NEread=set(g);NEblack=wake;rails=[]
for orientation,R,B in [('NE',NEread,NEblack),('SW',{(-t,e)for t,e in NEread},{(-t,e)for t,e in NEblack})]:
 for t,e in sorted({(x-u,(y-v)%2)for x,y in offsets for u,v in B if(x-u)%2==0}):
  rails.append({'orientation':orientation,'read':{(x+t,(y+e)%2)for x,y in R},'black':{(x+t,(y+e)%2)for x,y in B},'selector':5202+len(rails)})
assert len(rails)==48
for a,b in combinations(rails,2):
 if a['read']&b['read']:C.append([-a['selector'],-b['selector']])
nv=5249;gates=[];cells=[];initial_clauses=[]
for i,(p,events)in enumerate(sorted(G.items())):
 orbit=(p[0]-p[1],p[0]%2);level=p[0]//2;lo=min(offsets[orbit]);inherited=level>lo
 nv+=1;prev=nv
 cells.append({'position':list(p),'orbit':list(orbit),'level':level,'earliest_possible_previous_level':lo+1,'inherited_arbitrary':inherited,'input_variable':nv})
 if not inherited:
  sels=[r['selector']for r in rails if orbit in r['black']]
  initial_clauses.extend([[-x,prev]for x in sels]);initial_clauses.append(sels+[-prev]);C.extend([[-x,prev]for x in sels]);C.append(sels+[-prev])
 for ev,xs in sorted(events.items()):
  active,nxt=nv+1,nv+2;nv+=2;C.extend([[-x,active]for x in xs]);C.append(xs+[-active]);C.append([-active,prev if ev[3]=='L'else-prev])
  for bp,ba,bn in product((False,True),repeat=3):
   if bn!=(bp!=ba):C.append([(-lit if bit else lit)for lit,bit in zip((prev,active,nxt),(bp,ba,bn))])
  gates.append((p,ev,xs,prev,active,nxt));prev=nxt
assert cells==A['cells']
assert [{'orbit':list(k),'min':min(v),'max':max(v)}for k,v in sorted(offsets.items())]==A['orbit_offset_ranges']
assert len(cells)==214 and sum(c['inherited_arbitrary']for c in cells)==64
nv0,C0=read_cnf(O/'five_period.cnf');assert nv==nv0==44983 and len(C)==183663 and canon(C)==canon(C0)
for key,fn in [('cnf_sha256','five_period.cnf'),('rup_sha256','five_period.rup')]:assert hashlib.sha256((O/fn).read_bytes()).hexdigest()==result[key]
r=subprocess.run([str(ROOT/'causal_reduction/morphic_candidates/check_drat'),str(O/'five_period.cnf'),str(O/'five_period.rup')],text=True,capture_output=True,check=True);proof=json.loads(r.stdout);assert proof['valid']and proof['RUP']==787 and proof['RAT']==0 and proof['deletions']==0
# Test the physical event chains without the input restrictions against flat literal words.
Cf=canon(C)-canon(initial_clauses);rng=random.Random(615200);controls=[]
choices=[]
for name in ['prepared108_finite_positive','nonstationary_finite_positive']:
 meta=json.loads((O/(name+'.json')).read_text());rows=meta['images_by_period'];assert len(rows)==5
 ks=[[palette[c].index(w)for c,w in zip(REV,row)]for row in rows];choices.append((name,ks,meta))
for n in range(12):choices.append(('random'+str(n),[[rng.randrange(10)for _ in REV]for _ in range(5)],None))
for name,ks,meta in choices:
 word=''.join(palette[c][k]for row in ks for c,k in zip(REV,row));rr,end,h=walk(word,(0,0),3);assert(end,h)==((-10,-10),3)
 literal=defaultdict(list)
 for x,y,hh,c in rr:literal[x,y].append(c)
 firstL={p for p,v in literal.items()if v[0]=='L'};legal=all(all(a!=b for a,b in zip(v,v[1:]))for v in literal.values())
 val={1:True};val.update({2+10*(104*r+j)+k:(k==ks[r][j])for r in range(5)for j in range(104)for k in range(10)});val.update({r['selector']:False for r in rails});val.update({c['input_variable']:tuple(c['position'])in firstL for c in cells})
 actual=defaultdict(list)
 for p,ev,xs,prev,a,b in gates:
  val[a]=any(val[x]for x in xs);val[b]=val[prev]!=val[a]
  if val[a]:actual[p].append(ev[3])
 assert dict(actual)==dict(literal)
 sat=all(any(val[abs(x)]==(x>0)for x in cc)for cc in Cf)
 assert sat==legal
 if meta:
  assert word==meta['word']and legal
  board=set(map(tuple,meta['input_black']))
  for x,y,hh,c in rr:
   assert((x,y)in board)==(c=='L');board.symmetric_difference_update({(x,y)})
  assert sorted(map(list,board))==meta['output_black']
  assert meta['nonstationary']==(len({tuple(z)for z in ks})>1)
 controls.append({'name':name,'length':len(word),'legal':legal,'minimal_input':len(firstL),'nonstationary':len({tuple(z)for z in ks})>1})
out={'status':'PASS independent physical slab, inherited ownership, CNF and RUP reconstruction','source_sha256':hashlib.sha256((U/'synthesize_nonstationary_short_slab.py').read_bytes()).hexdigest(),'note_sha256':hashlib.sha256((U/'nonstationary_short_slab_obstruction.md').read_bytes()).hexdigest(),'architecture_sha256':hashlib.sha256((O/'architecture.json').read_bytes()).hexdigest(),'cnf_sha256':result['cnf_sha256'],'rup_sha256':result['rup_sha256'],'periods':5,'independent_image_choices':520,'physical_cells':214,'arbitrary_inherited_cells':64,'rail_prescribed_new_cells':150,'variables':nv,'clauses':len(C),'RUP_additions':787,'controls':controls,'scope':'No legal five-period slab under untouched compatible standard-bundle input and arbitrary earlier-architecture inherited colors; choices independent at every occurrence, outputs free. Does not cover additional untouched prepared defects, nonstandard writers, different palettes/scaffolds, or arbitrary earlier interventions.'}
(ROOT/'audits/check_nonstationary_short_slab_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
