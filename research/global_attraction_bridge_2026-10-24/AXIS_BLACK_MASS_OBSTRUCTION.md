# Two genuine collision controls exclude one fixed-axis black-mass potential class

Status: author checked; submitted for independent audit.

Fix the absolute axis normal n=(0,1). Consider a proposed potential

    Phi(B,p,h) = sum over (x,y) in B of f(y) + C_h(p_y),

where f(-1)+f(1)>0 (in particular f is everywhere positive) and C_h is arbitrary. The correction is invariant under translations tangent to the layers. There is no such potential that is nonincreasing on every genuine nonabsorbed blank-collision macro. This excludes positive fixed absolute horizontal-layer black mass plus a heading/height credit as a universal macro fuel. Proper rotations give the corresponding other coordinate-axis normals.

Here are the entire two controls, in the usual N,E,S,W heading convention:

1. Head (0,0), E, black board {(-1,0)}. The physical word is RRRL; the only old input is consumed on read 3. The final head is (-2,0), W, and the complete final board is {(0,0),(0,-1),(-1,-1)}. The potential change is 2f(-1)+C_W(0)-C_E(0).
2. Head (0,0), W, black board {(1,0)}. The physical word is RRRL, again consuming its old input on read 3. The final head is (2,0), E, and the complete final board is {(0,0),(0,1),(1,1)}. The change is 2f(1)+C_E(0)-C_W(0).

Both initial and both final full states fail the exact all-future standard104 predicate, so an absorber exception does not remove these examples. If both changes were nonpositive, their sum 2(f(-1)+f(1)) would be nonpositive, a contradiction.

These are two separate actual histories. They are NOT a composable two-cycle, a renewable controller, or a counterexample to attraction. They do not claim that any given history must increase the potential indefinitely.

## Scope boundaries

- The layer coordinate is the fixed absolute y coordinate, and the displacement of each macro is tangent to these layers. This is why the two heading credits cancel.
- For a diagonal head-relative weighting, moving the head changes the layer offset of every retained black cell. The displayed changes are then not valid. No diagonal or recentered no-go theorem is asserted.
- The result is about positive BLACK-MASS weights, not unsigned finite guard-defect counts. The two are different state functionals, and no no-go statement for one is inferred for the other.
- Nonlinear, cohort-dependent, archive-position-dependent, or record-to-record potentials remain outside this theorem. In particular, this does not refute a pristine-record budget.

Run `python check_axis_black_mass_obstruction.py` for the complete physical read logs, boards, exact macro comparisons and standard-absorber controls. The manifest binds the frozen files. No numerical search or assumed word-language cover enters the two inequalities.
