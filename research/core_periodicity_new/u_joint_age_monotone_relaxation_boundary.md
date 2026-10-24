# Joint U ages do not strengthen their monotone upward closure

Status: independently signed LN ansatz boundary, 10:49 UTC. This concerns an
explicitly relaxed input-guard ansatz, not physical realizability or U1 closure.

Use the five U-family input labels a=(-1,1), q=(-1,2), b=(-1,4), c=(0,2),
d=(0,3). JO/KV give a,q >=3 and b,c,d >=5 for produced identities; entry
identities have formal age infinity. LN additionally requires

    Aq >= min(Aa,Ac),  Aq >= min(Aa,Ad).

For the following abstract comparison, finite integer ages suffice. Every slot
belongs to any fixed chosen resource place, for example its exact height or its
height/transverse-residue pair. Map an age assignment to per-place tail counts:
x[z,j] is the number of selected inputs at place z of age at least j. A finite
saturation K may be used, with j=0,...,K, provided K>=5; the same argument works
with all integer thresholds. Coordinatewise order is the usual older/more-token
resource domination. Let I be the tail vector of the assignment

    (Aa,Aq,Ab,Ac,Ad)=(3,3,5,5,5).

Proposition. The upward closure of all JO/KV-admissible selected-input vectors
is exactly {x:x>=I}. The upward closure is unchanged if both LN inequalities
are imposed before taking that closure.

Proof. Every admissible slot age is at least its corresponding displayed
minimum. Therefore its tail vector dominates I, for any grouping into places.
Conversely the displayed assignment is admitted by the JO/KV-only ansatz and
also by JO/KV+LN, since Aq=Aa=3. Thus I belongs to both relaxed sets. Their
upward closures are consequently the same principal upward set. The proof is
unchanged if additional unused tokens are allowed in a guard resource.

This is NOT a claim that the all-produced exact profile (3,3,5,5,5) occurs in
a physical packet execution. It is admitted by the stated JO/KV/LN premises;
stronger joint attainability information could remove it. Likewise this does
not show that LN is useless in a transition system retaining exact ages,
colors, origin types or path correlations.

Indeed the guard itself is not upward closed. In the phase-one, heading-zero
U geometry, a/c share height 2, q/d share height 3, and b has height 5. At those
places take ages (18,18), (14,14), and (6), respectively. This vector dominates
I but every assignment within either equal-age pair violates
Aq>=min(Aa,Ac). Thus replacing the joint guard by its sound monotone upward
relaxation necessarily forgets a genuine incompatibility. This example is an
abstract input inventory, not a feasible physical state or trajectory.

Consequence for the existing age-Petri approach. If its only new premise is LN
and it restores upward-closed enabling sets in the existing per-place tail
order, no stronger input requirement can result. The independently signed
saved U1 all-origin diagnostic retains incompatible simultaneous birth ages
and therefore lies outside this unchanged monotone-guard ansatz. No generic
Petri search was rerun to establish this boundary.
