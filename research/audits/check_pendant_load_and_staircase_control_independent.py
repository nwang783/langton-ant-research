from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'actual_zipper_spiral_2026-10-23';p=SELF.parent/'check_serial_bridge_archive_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('# Fixed local masks')[0],ns)
ends,graph,component,wvertex=[ns[x]for x in('ends','graph','component','wvertex')]
def rank(B,k):
 g=graph(B,k);seen=set();cc=0
 for v in g:
  if v not in seen:vs,_=component(B,k,v);seen|=vs;cc+=1
 return len(B)-len(g)+cc
j=json.loads((D/'staircase_backbone_witness_q3.json').read_text());B={complex(*q)for q in j['initial_black_cells']};p=complex(*j['entry_pose'][0]);h=j['entry_pose'][1];birth={q:('initial',-1)for q in B};ticks=0;firstborn=set();removed=[];first=j['first_word'];assert len(B)==35 and len(first)==67 and Counter(first)=={'L':33,'R':34}
def step(expected,phase,forests=False):
 global p,h,ticks
 assert('L'if p in B else'R')==expected
 old=[rank(B,k)for k in(0,2)];w=wvertex(p,h);kw=int(w.real+w.imag)%4;dead=None;q=p
 if expected=='L':dead=birth.pop(p);B.remove(p)
 else:B.add(p);birth[p]=(phase,ticks)
 h=(h+(1 if expected=='R'else-1))%4;p+=1j*(-1j)**h;ticks+=1
 new=[rank(B,k)for k in(0,2)]
 if forests:assert old==new==[0,0]
 return q,dead,old,new,kw
for c in first:
 q,dead,*_=step(c,'first',True)
 if c=='R':firstborn.add(q)
 else:assert dead[0]=='initial'
assert B=={complex(*q)for q in j['first_final_black_cells']}and[p.real,p.imag]==j['first_final_pose'][0]and h==j['first_final_pose'][1]
kw=int(wvertex(p,h).real+wvertex(p,h).imag)%4;g=graph(B,kw);assert len(B)==36 and len(g)==37 and sorted(map(len,g.values())).count(1)==2 and all(len(v)<=2 for v in g.values())
assert len(component(B,kw,next(iter(g)))[1])==36 and component(B,kw,wvertex(p,h))[1]==set()
stitches={complex(*q)for q in j['charged_stitch_cells']};assert len(stitches)==2 and B-firstborn==stitches
reset=[]
for c in'RRRRL':reset.append(step(c,'reset'))
second='LRRL'*7+'L';assert len(second)==29
for c in second:
 q,dead,*_=step(c,'second',True)
 if c=='L':assert dead[0]=='first';removed.append(q)
assert len(removed)==15 and not(set(removed)&stitches)
exception=[]
for c in'RRL':exception.append(step(c,'exception'))
_,dead,old,new,kw=exception[-1];assert old[(0,2).index(kw)]>new[(0,2).index(kw)]
notes=['pendant_output_one_renewal_obstruction.md','staircase_backbone_countercontrol.md'];hs={n:hashlib.sha256((D/n).read_bytes()).hexdigest()for n in notes}
assert hs[notes[0]]=='656eda7bdc344d48a4ffc1032a52f7b2d9feb226c9b17a9b4b0b924ac3d72f24'
assert hs[notes[1]]=='0b2c1da7cf22fe6580925936e90cacb2b205da60c8bbe25c3a980e61c0c75392'
out={'status':'PASS general marked-path/pendant lemma, signed collector/pure-spiral applications, and exact q3 staircase countercontrol; mixed-rod application remains conditional on its pending construction','note_sha256':hs,'witness_sha256':hashlib.sha256((D/'staircase_backbone_witness_q3.json').read_bytes()).hexdigest(),'literal_control':{'entry_mass':35,'first_updates':67,'first_L':33,'first_R':34,'first_output_mass':36,'first_complete_w_graph':'one simple path, all34 first-R plus2 charged stitches','second_ordinary_updates':29,'first_R_lifetimes_consumed':15,'second_gain':-1,'following_RRL':'w-exceptional'},'analytic':['One actual complete R^rL block leaves at most three NEW surviving lifetimes. For r<=3 the departure L was an entry black edge; r4 returns to and deletes the first new edge. Retaining lifetimes, the next graph is contained in old G plus at most three new edges. If a physical old site is deleted and rewritten, it is a new lifetime and cannot be counted among surviving marked old edges.','The following ordinary zipper consumes a single vertex-simple path of its entry graph. Removing its at most three new-lifetime edges yields at most four vertex-simple old-G subpaths, each with marked load at most mu. Therefore at most4mu old marked lifetimes can be consumed. Additional passive components and arbitrary old deletions do not change this argument.','A tree with disjoint private pendant paths of length at most two has marked path load at most four, since a simple path can use pendants only at its two ends. This applies to the independently signed charged detoured collector and gives16. The independently signed pure spiral has disjoint1/2-edge stars, giving mu2 and bound8.','The q3 complete35-black control is a genuine positive ordinary gain with both graphs forests at every cut, yet ALL34 newborn edges lie on one complete36-edge simple path with two charged stitches. Thus a static rule placing positive-gain output necessarily off every backbone is false. The actual next ordinary epoch recycles only15 outputs and loses one mass; no positive-positive concatenation or all-q theorem is established.'],'qualification':'The frozen pendant note also mentions a mixed spiral+rod all-parameter application. Its graph-specific premise has not yet been independently audited; that application is signed only conditionally on the stated output graph. The general lemma and collector/pure applications do not depend on it.','scope':'Phase-local marked-current-lifetime load and one literal finite countercontrol. Not universal no-regeneration, all-q staircase validity, repeatable growth, global cubic sharpness or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
