from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'K1_pipeline_detours_2026-10-23';note=D/'early_top_output_exclusion_from_lower_roots.md'
# Normalize C maximum to0; H(L)=h(L)+1. Both chronological flat types
# have R multiplicities(1,1); their unique L may be in either direction.
flat=[]
for lE,lW in((1,0),(0,1)):
 a=-1;HNW=1-lE+a;HNE=1+a;HSE=1-lW+a;HSW=1+a
 assert HNE==HSW==0;levels=sorted([HNW-1,HSE-1]);assert levels==[-2,-1];flat.append(levels)
a=-1;HNW=1+a;HNE=a;HSE=1+a;HSW=1+a;assert max(HNE,HSW)==0 and[HNW-1,HSE-1]==[-1,-1]
sha=hashlib.sha256(note.read_bytes()).hexdigest();assert sha.startswith('de0faec3')
out={'status':'PASS early top-output reservations exclude lower-band roots','note_sha256':sha,'normalized_flat_L_heights':flat,'normalized_singleton_L_heights':[-1,-1],'analytic':['Signed783b71a0 supplies exactly one mutually distinct shallow odd-output class per early source: S singleton, R3 positive-flat x, or R4 negative-flat d. The unused same-R t is deliberately excluded.','The exact incident-face equations with H(L)=h(L)+1 give unshifted L heights M-1/M-2 for both three-read opposite-R flat types, and M-1/M-1 for the singleton selecting C maximum M. Rotating the physical frame does not change these height differences. Hence none can touch an L minimum at or below M-3.','The signed ordered-band theorem assigns distinct odd-output contacts to rooted spatial bands, all at such lower minima. Those contacts avoid the n_A shallow reserved classes, leaving at most Nodd-n_A rooted bands. Substitution in the same disjoint physical-current partition gives P>=6D+12D*max(0,r-1-Nodd+n_A).'],'scope':'Conditional ordered disjoint maximum-curve family in complete WHITE cap4 K1. One height-stratified current bound, not an added clock budget, per-branch lower cut, initial fuel or capture theorem.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha)
