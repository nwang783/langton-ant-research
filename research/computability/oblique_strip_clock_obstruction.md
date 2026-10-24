# A one-coordinate clock and bounded-write oblique-strip obstruction

Status: independently analytically audited, 2026-10-22 22:25 UTC. Exact rational controls pass. This is a refinement of the existing anisotropic clock framework, not a claimed new global escape or highway theorem.

## 1. Exact scalar-coordinate construction

Use headings N,E,S,W=0,1,2,3 and the fixed sector sign sigma, so sigma*chi(p)=(-1)^h, where chi(x,y)=(-1)^(x+y). Choose real a,b>1 satisfying (a-1)(b-1)>4. Put

    D = ab-1,
    delta = (ab-a-b-3)/D > 0,
    gamma = (3ab+a+b-1)/D > delta,
    M = 2/delta,
    (A_N,A_E,A_S,A_W) = (a+1,b+1,-b(a+1),-a(b+1))/D.

Fix any positive r. For a physical cell q=(x,y), set

    w(q)=a^x*b^y/r,
    f(q)=M*(w(q)+1/w(q))-2,
    J_h(q)=M*(A_h*w(q)+A_(h+2)/w(q)),
    Theta(B,p,h)=-sigma*sum_{q in B} chi(q)*f(q)+J_h(p).

The sum is over the complete finite black field. The head index h+2 is reduced modulo4.

Every literal ant update increases Theta by at least2.

### Eight-case proof

First take just the field weight w and head correction A_h*w. Its increment divided by w(p) is:

    N:R 0       N:L delta
    E:R delta   E:L 0
    S:R 0       S:L gamma
    W:R gamma   W:L 0.

For example, the N:R entry is -1+a*A_E-A_N=0, and N:L is 1+A_W/a-A_N=delta. The remaining identities follow by the same substitution.

The reciprocal term with head coefficient A_(h+2)/w is the 180-degree rotation of this table. It has the same four zero entries and exchanges delta with gamma in the others.

Finally replacing the summed field weight M*(w+1/w) by f=M*(w+1/w)-2 adds 2*(-1)^h*s to the update, where s=1 for R and -1 for L. This is +2 on the four zero entries and -2 on the other four. Thus the exact gains are

    2,
    M*(delta*w+gamma/w)-2,
    M*(gamma*w+delta/w)-2.

The latter two are at least M*delta*(w+1/w)-2>=2. This proves the strict clock identity uniformly in position, field, and r. No finite lookahead is needed.

The related four-component anisotropic potential and supercritical condition already occur in `../sources/kehao95-core/clock_escape/PROOF.md` and its manuscript appendix. The point here is retaining dependence on ONE oblique scalar coordinate, which is what the following strip argument needs.

## 2. Every non-axis normal is available

Let ell(q)=u*x+v*y with both u and v nonzero. A quarter rotation makes both coefficients positive. Choose lambda>0 large enough that

    a=exp(lambda*u), b=exp(lambda*v), (a-1)(b-1)>4.

Taking r=exp(lambda*c) gives w(q)=exp(lambda*(ell(q)-c)). Therefore both f and the head correction depend only on ell(q), apart from the four-valued heading.

For integer u,v>0, the entirely rational choice a=4^u,b=4^v works. If c is an integer, all weights and head coefficients on lattice cells are rational. For arbitrary real oblique normals the qualitative analytic statement still holds, without asserting a rational implementation for noncomputable coefficients.

An AXIS normal has one coefficient zero, so this construction does not apply. The distinction is substantive: fixed-port axial transport can have remote endpoint changes whose separation is unbounded.

## 3. Closed-pose complete-XOR estimate

Consider a finite actual interval with equal initial/final pose and length t. Let A be its complete board XOR, k=|A|, and suppose

    |ell(q)-c|<=W/2 for all q in A.

Then the head terms cancel, and all unchanged cells cancel. With

    F=M*(exp(lambda*W/2)+exp(-lambda*W/2))-2,

one obtains

    2t <= k*F.

This is independent of the normal position c of the strip, the longitudinal separation of changed cells, all unchanged background, and the initial black mass. As usual every changed cell q was visited, so 2||q-p||_1<=t.

These conclusions hold on arbitrary initial backgrounds, finite or infinite: copy the entry colors on the finite interval's read set into an otherwise white finite board. The copied interval has the same path, endpoint poses, and complete XOR, so the finite-field proof transfers verbatim.

## 4. Fixed finite controller and any fixed oblique strip

Suppose one actual uninterrupted infinite trajectory has strictly increasing checkpoints, with all checkpoint poses in a fixed finite set P. Let C be a fixed finite controller cell set. Assume each complete checkpoint XOR outside C has at most k cells, all contained in one fixed strip

    c-W/2 <= ell(q) <= c+W/2,

where ell has both coefficients nonzero. Then such an infinite checkpoint sequence is impossible, on any initial background.

Indeed, fix the clock from Section2 once. The remote field difference is bounded by kF, the controller contribution by sum_{q in C}|f(q)|, and the head difference by the finite range of J_h(p) on P. Hence every physical checkpoint interval has a common finite duration bound. Since each interval begins at a position from P, all later reads are confined to a fixed finite neighborhood. Only finitely many full checkpoint states can then occur, because their exterior is unchanged. An exact full-state recurrence contradicts the strict clock (or its finite-interval copying consequence).

No bound on the longitudinal distance between writes or on their movement from one checkpoint to the next is required. No finite-state assumption on the internal choice of intervals is needed. Temporary work may be anywhere, provided the COMPLETE endpoint XOR satisfies the stated bound.

Thus the previously audited NE/SW and NW/SE bounded-write corridor obstruction extends to EVERY fixed non-axis strip. A translating strip, an axis-parallel strip, unbounded write count, moving physical CPU, or spatially two-dimensional writes remain outside this theorem.

## 5. Two compact changed patches cannot separate in a uniformly oblique direction

Fix a patch radius R and eta>0. Consider equal-pose intervals whose complete XOR is contained in the union of two sup-norm-R boxes centered at q1,q2. Suppose their separation d=q2-q1 satisfies

    min(|d_x|,|d_y|) >= eta*max(|d_x|,|d_y|).

Their durations and distances of any actually changed cells from the common pose are uniformly bounded in R and eta.

For d!=0, choose a unit normal perpendicular to d. Its two absolute components are bounded away from zero by a constant depending only on eta. Rotate its quadrant, and choose one sufficiently large lambda that is supercritical for every such normal. The parameters delta,M,A_h then vary over a compact set and are uniformly bounded, with delta uniformly positive. Both boxes fit in a strip of uniformly bounded normal width. Section3 yields a common time bound because the changed-cell count is at most2(2R+1)^2. The round-trip inequality bounds changed-cell distances. The case d=0 is the already audited compact-mask case.

Consequently a family of increasingly long closed-pose intervals with complete XOR in two uniformly bounded patches can separate those patches only in directions approaching the coordinate axes. This is a necessary geometric restriction, not an exclusion of axial shuttles or distributed-write computation.

## Existing-clock alternative

The core analysis identified a shorter inherited route using `../sources/kehao95-core/wake_synthesis/PROOF.md`, Section9: its one-sided anisotropic clock has increment at least kappa*w, where kappa=1-2/(a+1)-2/(b+1)>0. The complete path-hull theorem confines a closed-pose excursion to the strip containing its complete XOR, so w has both positive lower and finite upper bounds along that path. This gives the same strip-duration consequence. For open controller intervals include the finite endpoint poses and controller cells in the hull. The explicit uniform-gain clock above avoids invoking the hull theorem and was independently checked as a scoped anisotropic refinement. Neither route is claimed as a new general theory of clocks.

## Exact controls

`check_oblique_one_coordinate_clock.py/json` independently implements the literal local rule, not any existing clock or ant module. It checks all8 heading/turn cases on361 positions for each of four rational parameter pairs, including an asymmetric near-critical pair. These finite controls supplement, rather than replace, the displayed universal algebra.
