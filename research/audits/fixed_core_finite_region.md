# A finite necessary region for retained mass-five cores

The four independently signed asymptotic exclusions apply in the same normalized blank-pose coordinates, with u=x-y and z=x+y. They exclude u<=-461, u>=502 and z>=76. The now-complete initial-SW and return-NE classifications also exclude every retained fixed core with z<=-431.

For the last assertion, the exact negative-z read map says that at z<=-94 only two bands can be read persistently by the pristine exceptional chain: initial SW u in[-28,-18] and return NE u in[42,52]. Outside them the established fixed-site recurrence coupling excludes the core. Each band is the disjoint union of 22 fresh rays with drift(-2,-2). Their phase-zero bases have z ranges[-15,-8] and[-34,-27]. Every ray has now been excluded at every fixed age m>=100. A site at age at most99 therefore has z>=-411 in the first band or z>=-430 in the second. Negative ages do not produce a lower z. Hence z<=-431 is excluded uniformly over the fixed retained site. The earlier -434 was conservative.

Consequently every hypothetical recurrent mass-five subsequence has its persistent one-black core in

    -460 <= u <= 501,
    -430 <= z <= 75,
    min(|u|,|z|) <= 82,
    u == z (mod 2).

The last restriction is the previously audited D82 core restriction; parity identifies actual integer lattice sites. The exact negative-z map sharpens this to the following explicit finite superset:

* For -93<=z<=75, keep all sites satisfying the displayed u range and D82 restriction. There are 76,905.
* For z<=-94, keep only the 44 fresh rays at ages m<100. There are 1,741 initial-SW and 1,840 return-NE sites.

The union has exactly 80,486 cells. Its physical bounding box is -271<=x<=288, -291<=y<=267. This is a convenient necessary superset, not a claim that every retained cell in it remains possible; other signed local exclusions may remove more.

`check_fixed_core_finite_region.py` independently reconstructs all fresh bases from literal W, binds them to the audited read map, proves their residue uniqueness, checks both cutoffs, and enumerates the finite superset. The output supplies a hash of the sorted physical cell list.

## What remains

This is not an eventual-mass-six theorem. For every remaining fixed core the four remote checkpoint cells can still have unbounded distances and exposed gaps. Capturing the singleton seed at that core, or testing a finite collection of five-cell seeds, does not settle those all-parameter interactions. To infer eventual mass at least six one must exclude every remaining retained-core recurrence case uniformly in those remote variables, or supply a separate global argument.

## Signed dependencies

* `global_constraints.md`, retained one-black local core and D82 restriction.
* `scattering/return_nw_frontier/PROOF.md`, combined u<=-461 exclusion.
* `scattering/far_se_core/PROOF.md`, u>=502 exclusion.
* `scattering/far_se_core/UPPER_Z_PROOF.md`, z>=76 exclusion.
* `scattering/far_sw_core/pristine_sw_bands.json`, exact fixed-site negative-z support.
* The independently signed complete initial-SW 22-class packages, including `return28_complete`, `return61_complete`, `return75_complete`, `return56_nested`, `initial_sw_exclusion`, `independent_reverse_ages` and the opposite-cycle packages.
* `scattering/return_ne_frontier/PROOF.md`, its `opposite/PROOF.md`, and `audits/return_ne_adjacent_coupling.md`, all22 return-NE classes at age>=100.
