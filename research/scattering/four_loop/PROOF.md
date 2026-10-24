# Exact completion of a four-scatterer circuit family

Date: 22 October 2026. This is a restricted all-parameter convergence theorem,
not the general finite-seed highway conjecture. The previous research proved
only the first mismatch of the intended circuit for all parameters, and capture
for three individual parameters. The new result completes that specific family.
No novelty or external peer-review claim is made.

## 1. Input and conclusion

Use the ordinary white/right, black/left rule, with flipping before moving,
headings N,E,S,W = 0,1,2,3, and pre-update time indices. Let R(x,y)=(y,-x).
For every integer L >= 128, define

    q0=(-127,-107),
    q1=(-151-2L,-82+2L),
    q2=(-126,-58+4L),
    q3=(-102+2L,-83+2L),
    G={(0,-1),(0,0),(1,-1),(1,0)},
    B_L = union_{j=0}^3 (qj + R^j G).

Start the ant at the origin facing north, with precisely B_L black. These are
sixteen distinct cells, four disjoint 2-by-2 blocks.

**Theorem.** Every B_L has an eternal standard northwest highway by time

    T(L)=520L+43111.

At that time the head is (-2L-40, 2L+57), facing east. The repeating word is
cyclic phase 99 of the supplied standard word W in ant_exact.py, and its drift
is (-2,2). The complete black mass at that boundary is 60L+2905.
The complete forward turn stream has exactly 19,629 forbidden ten-windows,
where forbidden means absent from the cyclic ten-factor language of W.
The stated time is a sufficient certification boundary, not an earliest onset.

## 2. Exact old-history prefix, kept intact

The earlier file
`continuation_2026-10-22/ant_continuation/wake_clock/four_scatterer_loop_proof.md`
proves the physical prefix through the first circuit mismatch. Its corresponding
affine checker is imported, with its contents hashed in completion_certificate.json.
The present checker rebuilds that full field rather than accepting an endpoint
pose or replacing it by a clean standard seed.

Write F for the fixed 7183-letter block and P for phase 61 of W. After the common
15758-update initial prelude, the exact word up to the first mismatch is

    F P^L F P^L F P^L F P^(L-65) P[0:10].

Quarter-turns change the spatial placements but do not change these LR words.
The mismatch state is at time A(L)=416L+37740, head (4,22), south. The circuit
plan requests R, but the true cell is black and produces L. It was initially
white and its unique earlier read was R at time 9500. Thus this is old memory
written by the same ant, not one of the sixteen initial scatterer cells.
Its black lifetime has age 416L+28240.

The old proof and the rebuilding checker retain every finite point and every
net flip in each of the four long sides. Remote initial blocks and every
original-core black cell remain physically present.

## 3. New complete recovery template

The file completion_template.json stores two fixed words A and C and a standard
word Q. Their lengths and exact coordinate effects are checked from the words:

1. From (4,22), south, A has length 1766 and ends at (-19,33), north.
2. Q has length 104, preserves north, and translates by (-2,2).
3. After L+2 copies of Q the head is (-2L-23,2L+37), north.
4. C has length 3397 and ends at (-2L-40,2L+57), east.
5. The phase-99 standard tail is valid forever from the complete resulting field.

The exact new suffix is therefore

    A Q^(L+2) C W99^infinity.

The discovery script compared a few complete literal executions to identify
this proposed template. Those comparisons are not its proof. The verifier
subsequently checks every color requirement uniformly for all integer L>=128,
including the final infinite suffix.

Its elapsed time is checked algebraically, not merely written into a report:

    416L+37740 +1766+104(L+2)+3397 = 520L+43111.

## 4. A second genuine history collision

The first letter of C is L, whereas uninterrupted Q transport requests R.
This collision occurs at time B(L)=520L+39714, at

    z(L)=(-2L-23,2L+37).

An independent affine incidence inventory in certify_provenance.py shows that
z(L) is initially white and has exactly one preceding visit: phase 58 of period
50 of the second old side P1, at time

    b(L)=104L+35382,

with turn R. It is therefore a black lifetime of age 416L+4332.
No first recovery read, other old side, or intervening Q period touches it.
The birth is on the northeast standard side produced after the second initial
block, not in a special manually installed return marker.

Thus the intended four-corner circuit does not simply fail once and abandon all
its past. It first hits the original core, then its new northwest route crosses
its own old northeast highway. The second complete recovery passes through that
old side and emerges northwest, rather than regenerating the old circuit.

## 5. Why the affine finite and infinite checks prove the theorem

At any prescribed boundary, the field is represented as an XOR of:

- finitely many points whose coordinates are affine integer functions of L;
- finitely many segments b(L)+k*d, 0<=k<N(L), where d is a fixed diagonal drift
  and N is an affine integer function.

This represents the complete finite physical field for each finite L. It is
not a truncated local window. All overlaps are XORed, including intersections
of distinct older corridors.

For a fixed word, visits to a cell determine the required color at the word's
start. Repeated visits must alternate; that condition is checked explicitly.
For a repeated period, each distinct local read cell becomes a ray indexed by
its epoch k. Each old point or segment contributes either no epochs, one epoch,
or a closed interval of epochs. Nonparallel intersections are solved with exact
integer determinants. Parallel intersections become intervals with affine endpoints.
Previous copies of the current period contribute half-lines starting at positive
integer overlap thresholds. Intra-period parity is already included in the
initial-color requirement.

Clipping to the allowed epoch range and XORing interval endpoints gives the
color mismatch function. Its boundary set must be empty, which proves no mismatch
at any epoch. Each inequality used in clipping is proved over the whole domain:
an affine aL+b is nonnegative for all L>=128 when a>=0 and 128a+b>=0. An unresolved
change of order, isolated equality, or parameter residue raises an error instead
of being silently dropped.

For the final infinite word, clip only to k>=0. A half-line [u,infinity) has the
single boundary u. Finite intervals retain two boundaries. Empty XOR boundary
sets imply zero mismatch on every nonnegative epoch, including the last infinite
interval. Induction on update time then proves the prescribed eternal word.
The output heading is checked to repeat and its displacement to be (-2,2).

The run checks 5920 fixed read-color constraints and 234 finite-period read-ray
constraints, including the old prefix; the final tail adds 44 distinct read rays
and 782 nonempty parity contributions. The exact counts are diagnostics, not
substitutes for the coverage argument above.

## 6. Event count and mass

All five variable powers have at least one complete standard period at L>=128.
Adding a copy strictly inside an existing standard run leaves both possibly bad
exterior joins unchanged and inserts only standard ten-windows. Consequently the
ordered sequence of forbidden ten-windows is independent of L. The literal
word assembled at L=128 has exactly 19629, and the certified infinite suffix
adds none. The ordered sequence's hash is retained in provenance_certificate.json.

Each additional L adds five standard periods, each with twelve more R than L
turns. Since R raises black mass by one and L lowers it by one, the capture mass
increases by 60. Its directly counted value at L=128 is 10585, giving 60L+2905.
This is a turn-count identity, not a proposed monotone disorder potential.

## 7. What is reusable, and what is still absent

A reusable interface is a **complete crossing field**, not merely an incoming
heading and an outgoing highway direction. The affine XOR representation makes
the history contributed by transverse old rails explicit. It allows a fixed
recovery certificate to compose with arbitrarily long intervening corridors if
all their read-incidence conditions are proved, including the final future guard.

This example does not show that every crossing passes through, consumes a fixed
resource, or creates no future scatterers. It proves those exact read colors only
for this whole family. Its second recovery still creates additional black debris.
That debris is harmless here because the exact final future-ray test excludes
all later influence, not because its amount decreases.

A general finite-scatterer proof would need: complete interface closure after
EVERY allowed interaction; a proof that newly written debris cannot create
unaccounted later interactions; and a well-founded rank or permanent geometric
separation for the resulting interaction graph. Neither a finite table of clean
collisions nor this family supplies those global premises. The next mechanistic
question is clean transverse highway/wake scattering and which historical
separation conditions survive its output.

## Reproduction

Run without Python -O:

    python scattering/four_loop/certify_completion.py
    python scattering/four_loop/certify_provenance.py

Discovery-only controls are extract_completion.py and probe_provenance.py.
No timeout or observation of a few repeated periods is accepted as a proof.
