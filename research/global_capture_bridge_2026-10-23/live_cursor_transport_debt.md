# Transport debt cannot be absorbed into positive face height

23 October 2026. This is a new application of the retained axial charge and
sharp midpoint bounds, not a new conserved quantity. Both charge and companion-output applications have independent analytic
approval. They do not bound residual highway defects.

## 1. Charge-compatible comparison states need not be reachable

Let X_0=(B_0,p_0,h_0) be an actual finite ant state, with invariant sector
sigma, and let X_t=(B_t,p_t,h_t) be its actual forward orbit. Use

    epsilon(x,y)=-sigma*(-1)^(x+y),
    rho(B)=epsilon*1_B,
    mu(p,h)=p-d_h/2.

At each t choose ANY finite binary comparison board A_t satisfying

    rho(A_t)=rho(B_0)+Delta H_t,                         (1)

for some finite integer plaquette field H_t. No sign, monotonicity, rate,
locality, chronology or reachability hypothesis on H_t is needed.
Only binary validity of A_t and equation (1) matter. Define the discrepancy
E_t=B_t symmetric_difference A_t.

**Transport-debt lemma.** For every t,

    |E_t| >= 2 ||mu(p_t,h_t)-mu(p_0,h_0)||_infinity.     (2)

Moreover every horizontal or vertical lattice line strictly separating the
two head cells contains at least two discrepancy cells. More precise
heading-corrected per-line bounds are given below.

This applies in particular to the preceding unit-height schedule, with
B_0 empty and its four-corner ideal checkpoints. It also applies to arbitrary
unions, multiplicities and arbitrarily large height supports whenever (1)
is binary. There is no bound assumed on actual or comparison black mass.

## 2. Complete proof

Every mixed difference has zero signed sum on every individual row and
column. Since epsilon differs from the usual alternating row weight by a
row-constant sign, and from the column weight by a column-constant sign,
A_t and B_0 have exactly the same alternating row and column sums.

Use G_r(p,h), F_c(p,h) from the retained axial invariant:

    S_r(B_t)-G_r(p_t,h_t)=S_r(B_0)-G_r(p_0,h_0) mod4,
    T_c(B_t)-F_c(p_t,h_t)=T_c(B_0)-F_c(p_0,h_0) mod4.

Consequently

    S_r(B_t)-S_r(A_t)=G_r(p_t,h_t)-G_r(p_0,h_0) mod4,
    T_c(B_t)-T_c(A_t)=F_c(p_t,h_t)-F_c(p_0,h_0) mod4.     (3)

Each discrepancy cell contributes +1 or -1 to its line's signed difference.
With delta4(v)=min(v mod4,4-(v mod4)), this gives

    |E_t intersect row r| >= delta4(G_r(t)-G_r(0)),
    |E_t intersect col c| >= delta4(F_c(t)-F_c(0)).      (4)

In particular a strict separating line has correction difference2 and hence
at least two discrepancy cells.

The exact sum identities in the retained sharp midpoint proof depend only
on the endpoint poses in one sector, not on either board being a reachable
state. The row sum of the lower bounds in (4) is

    |2(p_t.y-p_0.y)+d_h0.y-d_ht.y|, if p_t.y!=p_0.y,
    circular_heading_distance(h_0,h_t), otherwise.

The column expression exchanges x and y. Each is at least twice its
corresponding incoming-midpoint displacement. Taking their maximum proves
(2). This is the entire proof; no physical interval from A_t to B_t was
assumed or needed.

## 3. Spatially distributed and conditionally persistent debt

For one fixed axial line strictly on the far side of p_0, if the live head
stays strictly across that line throughout a later interval, (3) keeps its
signed discrepancy equal to2 modulo4 throughout that interval. At every
checkpoint in that interval at least two discrepancy cells remain on the
line, regardless of how many ideal face loops are inserted or how much
positive height is added. The cells carrying the discrepancy may change.

The debt can lose this forced residue only if the live head touches/crosses
the line again. Thus the charge is a precise conditional return-order
constraint, not an unconditional monotone quantity. Without a retreat bound,
indefinitely repeated crossings are not excluded.

Equivalently, no interpolation that keeps a uniform finite number e of
unrecorded connector bits can transport the live incoming midpoint farther
than e/2 from its starting midpoint while preserving an exact zero-margin
height model. Every remote connector must leave a distributed error trail
through all strict separating axial cuts. Face-loop height has zero line
margins, so it cannot absorb that transport charge.

## 4. Consequences and exact stopping point

- If an actual finite-seed trajectory is compared at every time with any
  family satisfying (1), a uniform Hamming-error bound would confine the
  live head. The known ant unboundedness theorem therefore forces unbounded
  comparison error along some subsequence. If the live head itself tends
  to infinity, the comparison error tends to infinity as well.
- The unit-height construction cannot be repaired merely by a bounded
  number of extra connector defects. This remains true even though its
  four-corner ideal patterns grow and its full height support is unbounded.
- A standard highway also creates a growing transport trail. Nothing here
  makes discrepancy cells forbidden ten-turn windows, six-label residual
  defects, black lifetimes, or fresh initial information. No such conversion
  is asserted.
- A successful global invariant must retain both the positive height and
  the uncancelled moving transport component. Bounding either in isolation
  would discard the exact mechanism carrying the head across axial cuts.

The presently missing bridge is an ordering/resource theorem that allows
standard transport but rules out indefinitely renewed nonstandard transport.
Equations (2)--(4) supply a compulsory spatial ledger, not that distinction.

## Dependencies

The correction tables and exact midpoint sum are in
`../continuation_2026-10-22/ant_continuation2/chronology/axial_separator_proof.md`,
Sections2--4. The comparison-board extension simply notices that their proof
uses charge compatibility, not an actual interval between the two boards.
The pose-injectivity special case e=0 is already recorded in
`../core_periodicity_new/cut_charge_pose_reconstruction.md`.

## 5. A returned cursor needs spatially separated companion output

This separate elementary application uses the retained closed-pose hull
identity, not a new clock. Suppose a nonempty actual interval begins at
X=(B,p,h) and ends at X'=(B',p,h), with exactly the same head pose. Let P be
one unit plaquette whose closed square does not contain p. Assume its
four-corner flip is locally legal on B, and call the resulting comparison
board A=B symmetric_difference corners(P). Put E=B' symmetric_difference A.

Then:

    |E| >= 4,
    p belongs to conv(corners(P) union E).              (5)

In particular E cannot be confined with P to any half-plane excluding p.
The repair to a remote face operation must have companion output extending
back across every line separating p from P. A bounded window near the face
cannot suffice, regardless of how many bits that window is allowed.

Proof. The locally legal complete face loop preserves every exact alternating
row and column sum, so A and B have equal margins. The actual same-pose
interval preserves those margins modulo four. Consequently the signed
B'-versus-A differences sum to zero modulo four on every individual row
and column. If 0<|E|<4, each occupied row and column must contain at least two
cells of E: one cell contributes +1 or -1, never zero modulo four. But a
nonempty simple bipartite incidence graph of cells, with every occupied row
and column of degree at least two, has at least four edges. This is a
contradiction. Hence the Hamming size is either zero or at least four.

The complete changed mask of the actual interval is

    B symmetric_difference B'=corners(P) symmetric_difference E.

The retained closed-pose hull theorem places p in the convex hull of this
complete mask. Its support is contained in corners(P) union E, proving the
second assertion. E=empty would put p inside P, contrary to the premise,
so the first assertion follows as well.

The complete-mask hull condition is the retained geometric dependency in
`../computability/one_sided_cpu_hull_obstruction.md`. Equation(5)
does not bound the number of returned excursions: four or more companion
cells can be arbitrarily far apart, and changing companions can surround
the head. It is a transport/return dichotomy, not a global irreversibility
or capture theorem. Both the quantitative charge application in Sections1--4 and this
additional hull application have independent analytic approval. Neither
supplies persistence of particular companion cells or an additive fuel
cost across repeated operations.


## Finite literal controls

`check_live_cursor_transport_debt.py/json` checks 2,180 comparison cases
against literal trajectories from four finite seeds, including exact
per-line charge residues and the midpoint bound, plus 300 returned-pose
companion cases. These support the algebraic proof; no finite horizon is
used to assert an infinite ant behavior.
