# Asymptotic far-northwest read bands of the pristine rectangle chain

Status: exact geometry, first-frontier lattice coverage, and fixed-site
quantifiers independently audited.
The underlying trajectory's full color verification is an audited dependency.

Fix a lattice site s, write u=x-y,z=x+y, and let n tend to infinity in
the original exceptional rectangle family. For every fixed s with u(s)<=-71,
that complete trajectory reads s for all sufficiently large n if and only if

    z(s) in [7,17] union [-63,-53] union [55,65].

In the three respective bands the first possible long passage is segment5
(NW), segment7 (returning SE), or segment11 (NW across the center).
Each band has both x-parity classes at every integer z. The bands are
disjoint. This is a statement about each FIXED site as n grows; it does
not assert one common n threshold for all sites and does not discard
possible isolated finite-n incidences.

The geometry-only checker is classify_pristine_nw_bands.py, with result
pristine_nw_bands.json. It reconstructs every read from the same exact
word template used by the existing full-field rectangle proof.

For a finite word, each read has the form a*n+b. If a is nonzero, it can
equal a fixed s for at most one n. If a=0, its u coordinate is one of a
finite list. The cutoff is chosen strictly below every relevant static
read coordinate, so none of these stationary reads can equal s.

For a periodic segment, a read is a*n+b+j*d with

    0<=j<c_a*n+c_b.

If a is not parallel to d, its transverse equation can hold at at most
one n. Otherwise write a=ell*d. For any fixed on-line s, the required
index is j=-ell*n+beta(s). If -ell lies strictly between0 and c_a, the
read occurs for every sufficiently large n. If -ell is outside that
closed interval it eventually does not. At the lower endpoint0 or
upper endpoint c_a, the cutoff compares s to the stationary start or
end of the corridor. Taking the minimum of all required finite endpoint
bounds gives the certified safe cutoff-71.

This calculation leaves exactly the three passages listed above:

    segment5: start slope0, driftNW, count n+5;
    segment7: start slopeNW, driftSE, count n+7;
    segment11: start slopeSE, driftNW, count2n+15.

The final NW tail starts at a position with slopeNW in n and continues
NW. For every fixed s it eventually starts beyond s, so it adds no
asymptotic fixed-site band. Segment13 has only13 periods, is also already
at a position with slopeNW, and has the same absence property.

All phase reads are checked, not only displayed corridor center lines.
The checker verifies that the exact (z,x mod2) classes in each surviving
passage comprise the stated11 consecutive z levels with both parities.
That is why the result is an exact lattice-site classification rather
than only containment in broader strips.

## Sparse-recurrence consequence and next targets

The same argument applies to the intermediate q_n and q_n+a_n parents:
for fixed u<=-71, their asymptotic fixed-site bands are, respectively,
[7,17] and [7,17] union[-63,-53]. Their separate infinite continuations
add no further far-NW sites: q's NW continuation is the already listed
first band, while q+a's permanent SE tail starts at bounded u and moves
toward increasing u.

Thus a fixed retained core outside all three bands stays unread by the
entire audited exceptional-parent chain for all sufficiently large n.
The global four-strand/cycle argument then captures exactly as in the
existing D82 restriction proof: ordinary corner hits avoid the fixed core
by the diverging half-plane gap, and exceptional hits force the old
rectangle coordinates. This excludes such a retained core.

The22 q-parent fresh classes are exactly all (z,x mod2) classes with
7<=z<=17. Their bases have minimum u=-54, so every site in that band
with u<=-454 has core index m>=100. The independently audited completed frontier classification excludes
this whole first band below that cutoff.

Consequently the only remaining retained-core locations in the far-NW
region u<=-454 are the two11-level bands

    -63<=z<=-53, or55<=z<=65.

These are new target families, not established captures. In the first
band the core is first read on the SE return after the exceptional a-hit.
In the second it is first read during the later long NW passage after c.
Their local source ages and complete old histories differ from the first
frontier; the previous22-rule theorem must not be reused without proving
those new couplings.
