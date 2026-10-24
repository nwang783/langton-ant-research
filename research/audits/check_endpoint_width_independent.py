from pathlib import Path
PP=Path(__file__).resolve();SS=PP.with_name('check_exceptional_return_map_independent.py');exec(compile(SS.read_text().split('# A separate full-field')[0],str(SS),'exec'))
t=lambda z:int(z.real-z.imag);seed=base|{head+11*d};assert len(seed)==14 and head+11*d==-39-20j
assert p==-15+10j and h==3 and r==-49j and rh==1
assert A.index(head+11*d)==1216
assert(min(map(t,seed)),max(map(t,seed)))==(-27,-19)
assert(min(map(t,S)),max(map(t,S)))==(-28,-18)
assert(min(map(t,stable)),max(map(t,stable)))==(-82,56)
assert(min(map(t,Q)),max(map(t,Q)))==(42,52)
ends=sorted(map(xy,(z for z in stable if t(z)in(-82,56))));assert ends==[(-72,10),(-71,11),(-70,12),(2,-54),(3,-53),(4,-52)]
assert all(not 42<=x-y<=52 for x,y in ends)
halo=max(0,-28-min(map(t,A+Q)))+max(0,max(map(t,A+Q))+18);assert halo==128
J=json.loads((R/'phase72_width_countercontrol.json').read_text());assert sorted(map(tuple,J['initial_black']))==sorted(map(xy,seed)) and J['first_obstacle_read']==1216 and J['output_black_mass']==2216
out=dict(status='PASS independent actual persistent endpoint widening and analytic read-hull ledger',note_sha256=hashlib.sha256((R/'endpoint_width_countercontrol_and_hull_ledger.md').read_bytes()).hexdigest(),seed=sorted(map(xy,seed)),first_obstacle_read=1216,certified_terminal_time=52262,terminal_mass=len(stable),initial_black_hull=[-27,-19],incoming_read_hull=[-28,-18],terminal_black_hull=[-82,56],outgoing_read_hull=[42,52],permanent_extreme_black_cells=ends,outboard_read_halo=halo,scope='One actual backscatter violates a pointwise12-per-leg or24-per-pair width increment, not an amortized alpha*J+C bound, repeatability or capture. General support ledger keeps the entire changed board and actual reaction reads plus outgoing period; cumulative halo<12 per leg would suffice only with separately established common untouched bulk packing hypotheses.')
PP.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
