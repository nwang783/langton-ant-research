# Independent analytic audit: positive clocks and finite-order uniform refinements

2026-10-23 05:12 UTC. PASS, with the scope below. This does not settle universal finite-seed capture.

## The scalar clock is a genuine noncancellation argument

Write headings N,E,S,W as 0,1,2,3 and turns R,L as +1,-1. For positive X,Y let w(x,y)=X^x Y^y and use gamma=(2/(Y+1),2/(X+1),-2Y/(Y+1),-2X/(X+1)). For the physical one-step state s=(u,v), set d_s=(-1)^u turn(u,v), H_s=gamma_v w(v)-gamma_u and g_s=H_s-d_s. Direct symbolic substitution gives g_s=kappa except for (S,E) and (W,N), where it is kappa+4; kappa=1-2/(X+1)-2/(Y+1). Thus g is strictly positive on a nonempty open region of the positive quadrant.

In a unit-spatial exact typed refinement, the Laurent incidence matrix M counts all read positions. At every depth, the weighted sum of H telescopes to the actual endpoint correction. If its boundary headings are fixed or eventually periodic, their depth generating function has no pole at any real t strictly between zero and one. Therefore the identity M^r g=H(r)-M^r d excludes signed cancellation at a positive Perron pole; this is stronger than simply asserting positive incidence.

## Finite-valued coefficients give one fixed denominator

If every refined block is internally ant-legal, turns at each physical cell alternate. All incoming heading axes at that cell are equal, so each coefficient of M^r d lies in {-1,0,1}, even if the block's initial axis changes with depth. Offsets are sums of r elements of one finite set, hence are O(r). A linear spatial shear makes the joint depth/spatial rational series a formal power series with denominator constant term one.

The previously signed finite-valued rational-array theorem applies to this complete array, not merely one specialization. Each coefficient-value set is semilinear. A finite disjoint simple-linear decomposition gives a fixed Laurent denominator P(t,X,Y) which is a product of factors 1-t^a X^b Y^c. Every nonzero period has a>0: a zero-time period would create infinitely many points at one fixed depth, impossible for a finite word. Consequently P(t,1,1) has no real zero in (0,1).

## Perron continuation

For an irreducible M, its positive Perron eigenvalue lambda(X,Y) is simple and real analytic on the entire connected positive quadrant. The matrix selecting each row's first child has unit row sums, since every first child has offset zero; it is dominated by M. If the component has any extra child and is irreducible, strict Perron comparison gives lambda>1 everywhere. This argument also follows by dominating a zero-offset first-child cycle.

On the open clock region, positive left/right Perron vectors and g>0 give a nonzero simple pole of [(I-tM)^(-1)g]_s at t=1/lambda. The boundary correction is analytic there. Hence P(1/lambda(X,Y),X,Y)=0 throughout that open region. This is one real-analytic function on the connected positive quadrant, so it vanishes identically. At X=Y=1 this contradicts P(t,1,1) being nonzero for t in (0,1), since lambda(1,1)>1. No eigenvalue choice is switched between regions.

## Exact adjacent-pair lift removes heading preservation

For a fixed uniform absolute-direction substitution with finite-order matrix, take a power whose actual rooted limit P is fixed and whose spatial matrix is I. Let psi have uniform length K>1 and net psi(v)=v. Its occurring adjacent pairs (u,v) form a finite alphabet S. For psi(v)=w_0...w_(K-1), define chi(u,v)=(G(u),w_0),(w_0,w_1),...,(w_(K-2),w_(K-1)), with G the last-letter map. All these pairs really occur in psi(P)=P and are perpendicular.

Induction gives chi^r(u,v) as precisely the physical read states of psi^r(v) after psi^r(u). Their boundary headings are G^r(u),G^r(v), their displacement remains v, and their child offsets add without spatial rescaling. Thus M^r is the actual weighted incidence, not an assumed heading-compatible approximation. G is a finite map, so the boundary correction is eventually periodic. Every block is an actual factor of P and is internally legal if P is.

A terminal strongly connected component of S is closed and has row sums K. Its Perron value at (1,1) is K>1. Restriction preserves all geometry and legality premises, so the preceding contradiction applies. This proves: no growing rooted power-limit of a fixed uniform absolute-direction substitution with finite-order integer spatial matrix is an ant path on ANY coloring. No half-turn symmetry, heading preservation, finite support, period bound or image-length bound is required.

For the earlier half-turn uniform finite-seed dichotomy, only the expansive branch remains: every eigenvalue has modulus greater than one and rho(A)<k<=|det A|. Arbitrary directive schedules and reducible nonuniform refinements remain outside this conclusion.

## Independent implementation controls

`check_perron_pair_clock_independent.py` independently generates 24 geometric four-direction substitutions of lengths 5,9,13. It checks literal adjacent-pair iteration, exact Laurent checker coefficients and endpoint headings through depth three, and positive-clock telescoping at two rational characters. These are deliberately geometric controls, not accepted ant models, and are not the premise for the all-length proof.

Reviewed sources: `causal_reduction/unit_scale/primitive_perron_clock_obstruction.md` and `finite_order_uniform_obstruction.md`. Dependencies are the signed finite-valued rational coefficient theorem and the retained literal exponential-clock identities.
