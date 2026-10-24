from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23';note=D/'K1_surviving_L3_cleanup_two_outward_parents.md'
assert hashlib.sha256(note.read_bytes()).hexdigest()=='74d7dfec6ad1399805696b84f9130e9bb190e59015d059fe96720565550e5428'
q=SELF.parent/'check_K1_early_L3_cleanup_independent.py';env={'__file__':str(q)};exec(q.read_text().split('results={}')[0],env)
ns=env['ns'];base=env['base'];H=env['H'];prior=env['prior'];baseports=env['baseports'];exec(base,ns)
for pr in prior:
 ns['ports']=baseports+([('v',1,'D')]if pr['kind']=='S'else[('v',1,'w'),('w',2,'D'),('D',3,'B')])
 hs={v:H(h)for v,h in pr['headings'].items()};hs['f']=H('EEEW');cp,de=ns['solve'](hs)
 assert cp['f',0]==cp['g',0]and de['f',0]-de['g',0]==-1
 assert cp['g',1]==cp['e',0]and de['g',1]-de['e',0]==-2
# The incoming/departing edges of both actual R0s belong to Q1.
Q={(-3,1),(-2,1),(-2,2),(-3,2)}
for before,at,after in[((-2,2),(-2,1),(-3,1)),((-3,2),(-2,2),(-2,1))]:assert before in Q and at in Q and after in Q
# Parent directions on the actual canonical p-chain, without identifying lifts.
parent_choices=[(-4,0),(-4,2)];center=(-3,1);child=(-2,0)
turns=[]
for p in parent_choices:
 a=(center[0]-p[0],center[1]-p[1]);b=(child[0]-center[0],child[1]-center[1]);det=a[0]*b[1]-a[1]*b[0];turns.append('RIGHT'if det<0 else'STRAIGHT')
assert turns==['RIGHT','STRAIGHT']
out=dict(status='PASS surviving cleanup earlier Q1 boundary and both outward parent alternatives',note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),rows=len(prior),parent_choices=parent_choices,chain_turns=turns,analytic='The actual complete R0s at g(S) and f(E) both traverse a Q1 input edge before its output, excluding both right birth corners. Port equality fR0=gR0-1 means the Q1 input edge is traversed at gamma-2. gR0<=gL1-4=delta-6 and delta<=alpha-4 give B(Q1)<=alpha-12; canonical parent gap5 gives B(p(Q1))<=alpha-17. Only one of the two left faces must be the max parent.',scope='Finite same-component canonical supplier chain in physical lifts. Either parent may alias an earlier quotient class; no distinct resource, iterative pattern, extra overlapping clock or global K1 exclusion.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
