from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'seven_word_spatial_return_2026-10-23';p=SELF.parent/'check_ordered_W_archive_transport_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('ports=dict')[0],ns);raw,O,walk,W,M=[ns[x]for x in('raw','O','walk','W','M')]
# Exact affine coefficient vectors in(A,B,constant), not parameter samples.
for source,weight,x,y in [('V',1,(-1,0,-4),(0,1,1)),('U',2,(-1,0,-5),(0,1,0))]:
 step=raw['V']['p']*(-1j);exitx=(x[0],x[1],x[2]+int(step.real));exity=(y[0],y[1],y[2]+int(step.imag));normal=tuple(exitx[i]+exity[i]for i in range(3));assert normal==(-1,1,1-2*weight)
 assert exitx[2]-1<=-2
for n,w in [('D',0),('V',1),('U',2)]:
 delta=raw[n]['p']*(-1j);assert delta.real+delta.imag==2*w
foreign=[]
for f,p,c,minremaining in [('F',2-5j,2,1),('Q',4-5j,1,1),('B',5-4j,0,2)]:
 assert p.real+p.imag==1-2*c
 # foreign normal=1-2T+2(T_E-J), hence J+T=T_E+c.
 assert c+minremaining=={'F':3,'Q':2,'B':2}[f];foreign.append((f,c,c+minremaining))
mp=D/'W_portal_complementary_indices_manifest.json';mh=hashlib.sha256(mp.read_bytes()).hexdigest();assert mh=='ef6f916a8899ee57b064578da6a940b9ba48f661d85b9e14497cbf1c5a8f2ffd'
mf=json.loads(mp.read_text())
for f,h in mf['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
for f,h in mf['dependencies'].items():assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h
out={'status':'PASS weighted-index annotation of actual W portal submatching','manifest_sha256':mh,'foreign_constant_and_source_minimum':foreign,'analytic':['For actual W base displacements, A-B increases by2 for V and4 for U, zero for D. Thus prior weight is(A-B)/2, and source-inclusive T adds1 or2. Genuine portal identity and actual V input fix consumer RAW-exit normal exactly1-2T. Source C tails preserve the portal; no fictitious internal producer or omitted S run is introduced.','Every subsequent E base changes x+y by twice its D/V/U weight. Comparing the actual foreign normals -3,-1,1 gives J+T=T_E+2,+1,+0. This is an annotation of actual matched identities and endpoints, not a new monotone time clock.','The consuming V cannot be the last E packet by its exit x<=-2 versus foreign entry2/4/5. The remaining word therefore has an actual last V/U for F/Q or U for B, giving remaining weight at least1/1/2 and source T>=3/2/2. Its delayed marker-only L belongs to the next E RAW phase2 before foreign.'],'scope':'Signed23f62a2c actual once-spent portals only, one foreign/returnedC residue. Arbitrary S stage and unbounded D gaps remain; no spending count, contraction, periodicity or capture conclusion.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
