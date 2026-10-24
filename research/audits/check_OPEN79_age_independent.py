from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();F=D/'RETURN_DEBT_OPEN79_CANONICAL_AGE_ADDENDUM.md';assert sha(F)=='b2370fb31a65275cf2d330d218531a5fe6fa5c8b7424747e23b1b18b22b5c6f4'
ns={'__file__':str(S.with_name('check_physical_return_debt_independent.py'))};exec(Path(ns['__file__']).read_text().split('out=dict(')[0],ns)
chains,H,outs=ns['chains'],ns['H'],ns['outs'];ch=max(chains,key=len);assert len(ch)==35 and ch[0]==((12,11),0)and ch[-1]==((12,3),1)
assert min(v for _,v in ch)==-3 and max(v for _,v in ch)==1
assert H[12][11]==2 and [i for i,h in enumerate(H[12])if h==2].index(11)==7
assert outs[12,3]==3 and [i for i in range(len(H[12]))if outs[12,i]==3].index(3)==1
obj=dict(status='PASS exact OPEN79 canonical-age identity only',proof=sha(F),independent_parent_report=sha(S.with_name('check_physical_return_debt_independent.json')),named_chain_start=ch[0],named_chain_end=ch[-1],named_events=35,outside_distance=36,internal_lift_range=[-3,1],outside_source='T15 S departure ordinal7',outside_target='T13 W arrival ordinal1',outside_net_voltage=0,canonical_age='t12,11-t12,3=P-34',analytic_review='35 consecutive named events give34 actual steps from rank11/lift0 to rank3/lift1, so the displayed canonical-clock identity is exact. Eight intervening same-cell gaps implyP>=66, weaker than79 named-event phase count. This is a necessary OPEN graph identity, not physical or phase-complete realization, bounded-age disproof, monotone debt or new period theorem.');S.with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print(obj['status']);print(sha(S.with_suffix('.json')))
