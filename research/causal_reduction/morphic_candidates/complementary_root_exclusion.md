# Complementary roots in geometric turn substitutions

Status: independently audited complete enumeration and analytic certificates,
22 October 2026; see audits/check_complementary_roots_independent.py and JSON. This complements, and does not change the scope
of, the earlier audited R-prolongable search in `computability/`.

## Statement and scope

Let phi(R)=u, phi(L)=v have a common odd length k in {3,5,...,17}. From a
north-facing origin, u must end east with Gaussian displacement a, and v west
with displacement -a, where |a|>1. Consider either:

1. v begins L, and the infinite fixed point phi^infinity(L); or
2. u begins L, v begins R, and a fixed point of phi squared.

None is a finite-black-seed Langton-ant trajectory. In case2 both initial
phases are excluded, not only the R-root phase actually enumerated.

Together with the prior R-prolongable theorem, these cover every first-letter
cycle for two-letter uniform geometric turn substitutions through length17.
They do NOT cover length19, arbitrary multi-symbol substitutions, all automatic
walks, all aperiodic ants, or the full highway conjecture.

## Complete finite parameterization

Enumerate all binary words of each stated length. Compute their exact turtle
geometry and discard any word with two equal consecutive reads at one physical
cell. Such a word cannot occur inside ANY ant trajectory, regardless of seed.
Group the remaining images by final heading and displacement, then pair all
u with v having the required opposite displacement/quarter-turn endpoint.

Every expanding image contains both letters: a monochromatic odd turn word
has displacement of magnitude1. Thus the substitution incidence matrix is
strictly positive. Both images necessarily occur in either infinite phase,
so the internal-word rejection is sound and completeness loses no candidate.

For case1 enumerate all pairs with v beginning L, including pairs whose u
also begins R. Those were different ROOTED trajectories from the previous
R-root theorem. For case2 enumerate all pairs with u beginning L and v R.
The R-root of phi squared suffices for finite alternating-read failures:
every finite prefix of that fixed point occurs, up to translation and
rotation, in the L-root fixed point, because phi squared is primitive. A
same-cell consecutive-equal-turn contradiction inside the factor survives.
The analytic filters below also exclude both phases when used in case2.

## Root-sensitive analytic filters

Put q=e(u), r=e(v), alpha=(q+r)/2, lambda=(q-r)/2, where e=#R-#L.
For a root with initial signed charge z=+1 or -1, the length-k^n prefix has

 E_n = c*k^n + (z-c)*lambda^n,  c=alpha/(k-lambda), |lambda|<k.

The geometric prefix radius is O(|a|^n). Therefore:

- alpha<0 forces unbounded negative black-mass increments for either root.
- alpha nonzero and k>|a|^2 makes signed excess exceed the number of visited
  cells, impossible even on an arbitrary coloring.
- For an L-prolongable root with alpha=0, E_n=-q^n. If |q|>1, some subsequence
  tends to minus infinity; otherwise mass stays bounded at expanding endpoints.
  All symmetric-charge L-root cases are therefore excluded.
- For a first-letter2-cycle, the nested prefixes use EVEN powers. When alpha=0,
  their R-root excess is q^(2n). The midpoint inequality excludes q^2<=|a|^2;
  the visited-area inequality excludes |q|>|a|^2. The L-root has excess
  -q^(2n) and is already impossible by negative mass or bounded mass.

In particular, one must NOT reuse the negative-q obstruction for an unsquared
R-prolongable substitution at a first-letter2-cycle. Negative q becomes
positive after squaring. The new checker implements the squared condition.

The midpoint and visited-area ingredients were independently audited in
`computability/selfsimilar_visit_certificates.md`; these are their explicit
root/phase specializations.

## Exhaustive outcomes

`search_complementary_roots.py` gives exactly1,241,057 rooted cases:

-1,000,661 analytic exclusions;
-240,394 finite consecutive-equal-turn conflicts, latest at time3466;
-2 prefixes surviving100,000 reads, both at image length17.

Every conflict stores its two read times, cell, and turn. These are exact finite
countercertificates to the prescribed path, not time-horizon assumptions.
Full records and per-length digests are saved; the independent reviewer may
regenerate them without trusting the stored counts.

The two remaining image pairs are:

 u=LRLRLRRLRLRLRLRRL, v=RLRRLRRLRLRLRLRLR, a=3+6i;
 u=LRLRLRLRLRLRRLRRL, v=RLRRLRLRLRLRRLRLR, a=-3+6i.

They are NOT accepted candidates. Their100,000-step prefixes already require
about40,862 initial black cells. The next exact argument excludes finite
support without extrapolating that observed growth.

## Exact exclusion of both remaining pairs

Let psi=phi squared. Its image length is289 and scale A=a^2, respectively
-27+36i and -27-36i. Both images begin with their own root letter. Literal
integer checks of all288 internal phase offsets in EACH image find none in
the Gaussian ideal A Z[i]. Divisibility of x+iy by A=X+iY is checked by

 X*x+Y*y =0 mod(X^2+Y^2),
 X*y-Y*x =0 mod(X^2+Y^2).

Thus the full infinite path reads the sublattice A Z[i] exactly at macro
boundaries289*n. Since p(289*n)=A*p(n), a visit is first at n exactly when
its scaled visit is first at289*n, and its turn is preserved.

The R-root word begins RL. Time1 is therefore a first-L read at the nonzero
cell1. It follows inductively that EVERY time289^j is a first-L read at A^j.
These cells are distinct because |A|=45>1. Infinitely many initial black
cells are necessary. This is an explicit infinite first-L family, so no
blank-orbit assumption or expensive general automaton is needed.

The L-root phase begins LRL. Its time2 read is therefore a first-L event at
-1+i, also nonzero. The same ideal isolation gives first-L events at every
time2*289^j and cell A^j*(-1+i). This explicitly excludes the other phase as
well. No inference from a finite factor's local freshness to global freshness,
and no complementation of the infinite background, is used.

Files: `complementary_roots_l17.json`, its full `_records.json`,
`check_two_cycle_survivors.py`, `two_cycle_survivor_sublattice.json`.
