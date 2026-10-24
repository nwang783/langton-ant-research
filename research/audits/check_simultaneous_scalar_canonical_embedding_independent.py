from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23';p=SELF.with_name('check_canonical_barriers_stock_hole_roots_independent.py');ns={'__file__':str(SELF)};exec(p.read_text().split('files=')[0],ns);rows=ns['rows'];outrows=[]
for z in rows:
 h,j,C,L=z['word'],z['j'],z['C'],z['L'];a=(sum(C.values())+sum(L.values())-(len(h)%2))//4
 assert 4*a==sum(C.values())+sum(L.values())-(len(h)%2)
 assert min(C.values())>=a>=max(L.values());typ='R'if j>a else'L'
 assert all(t==typ for i,k,t in z['pairs']);outrows.append({'word':h,'j':j,'C':C,'L':L,'a':a,'turns':[t for i,k,t in z['pairs']]})
assert len(outrows)==78 and sum(len(z['turns'])for z in outrows)==98
# Fresh chronological port matching for every exchange, not inferred from local same tangents.
v={'E':1+0j,'W':-1+0j,'N':1j,'S':-1j};names={z:k for k,z in v.items()};ex=[]
for n in[3,4]:
 for seq in product('EW',repeat=n):
  h=''.join(seq);rr=Counter(h[::2]);a=-max(rr.values());C={'E':a+rr['E'],'W':a+rr['W'],'N':a+rr['W'],'S':a+rr['E']};inc=Counter();outs=Counter();events=[]
  for i,x in enumerate(h):
   y=names[v[x]*(-1j if i%2==0 else 1j)];inc[x]+=1;outs[y]+=1;events.append((x,y,inc[x],outs[y],C[x]-inc[x]+1,C[y]-outs[y]+1))
  e,f=events[1],events[2];samein=e[0]==f[0];sameout=e[1]==f[1];assert samein!=sameout
  ords=(e[2],f[2])if samein else(e[3],f[3]);levels=(e[4],f[4])if samein else(e[5],f[5]);assert ords[1]==ords[0]+1 and levels==(a+1,a)
  ex.append({'word':h,'shared_port':'input'if samein else'output','ordinals':ords,'labels':levels,'center':a})
assert len(ex)==24
au=json.loads((D/'canonical_simultaneous_scalar_interpolation.json').read_text());assert au['local_sheets']==78 and au['canonical_arcs']==98
for x,y in zip(outrows,au['rows']):assert(x['word'],x['a'],x['turns'])==(y['headings'],y['center'],y['canonical_turns'])
files=['canonical_simultaneous_scalar_interpolation.md','canonical_simultaneous_scalar_interpolation.py','canonical_simultaneous_scalar_interpolation.json','positive_output_scope_addendum_stages15_through20.md'];hs={f:hashlib.sha256((D/f).read_bytes()).hexdigest()for f in files}
out={'status':'PASS simultaneous all-sheet scalar embedding and equal-sign essential exchange rule','source_hashes':hs,'all78_center_height_checks':outrows,'all24_shared_consecutive_exchange_ports':ex,'analytic':['At every primal vertex the exact completeWHITE face equations give integer a=(sumC+sumL-delta)/4, withC>=a>=L anddelta=nmod2. This formula is coordinate-independent under the actual rotated checker sector. Inactive vertices have equal adjacent heights. The full-drift invariant assigned values agree globally.','Dual squares around primal vertices tile the plane; subdividing each into4triangles gives a single globally compatible triangulation. Face-center and central values agree on shared dual edges, so linear interpolation is continuous. Half-integer levels avoid every integer-valued triangulation vertex and cannot contain a flat triangle/edge. Every component is therefore a regular disjoint polygonal contour; crossings of a dualC/L edge occur exactly for L<j<=C.','Fresh78-sheet98-arc reconstruction proves canonicalturnR iffj>a andL iffj<=a, including both four-port choices. These precisely match local half-level interpolation around the low/high center. Thus the scalar contours are simultaneously isotopic to ALL canonical occurrence circles, not merely individually embedded. Their physicalport ordering agrees with chronological ordinalr labelC-r+1.','At all24 L1/R2 exchanges the two ranks share exactly one actual input or output port; its ordinals are consecutive and the crossing labels area+1,a. Their open connector lies on one dualedge withF strictly between the two halflevels. It therefore avoids both entire endpoint circles and any other canonical level, not just the local displayed arcs.','If the endpoint circles are both essential in the actual full-drift cylinder, they are disjoint embedded circles with winding±1. A connector incident to both without crossing either must lie in their unique intermediate annulus, rather than either exterior end component. BecauseF is higher onRIGHT, this annulus isLEFT ofupper andRIGHT oflower. Its oriented boundary isupper minuslower, homologyzero, hence their winding signs agree. No reduction of the actual drift to its primitive direction is made.'],'scope':'All-output completeWHITE cap4 front. This adds a genuine simultaneous cross-sheet embedding not assumed in the older within-sheet audit. Opposite essential signs may still connect via contractible nodes or longer graph paths. No resource/genus bound, realization, or capture follows. Mandatory positive-output scope addendum9402be38 is bound; no Nodd0 premise is used.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
