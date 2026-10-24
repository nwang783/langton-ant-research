# Eventual affine ninefold position inflation

Status: independently analytically approved on 22 October 2026, 21:48 UTC.
Both the computability analysis and independent auditor checked the affine phase,
rotated first-record, and finite-block cancellation arguments. The two finite
local certificates were previously independently audited in
position_only_k9_record_exclusion.md. No new search is used here.

## Independently audited theorem

Let p(t) be the physical position of a standard ant started with finitely many
black cells. There do not exist integers c,N, an integer vector b, and

    a in {3, -3, 3i, -3i}

such that

    p(9n+c) = a p(n) + b                                  (1)

for every integer n >= N (with 9n+c >= 0).

The initial pose is arbitrary. There is no heading-preservation assumption,
no substitution or finite-controller assumption, and no requirement that the
identity start at time zero. This excludes an eventual affine self-similarity
class, not all aperiodic paths and not the highway conjecture.

## Two imported finite facts

Write a=3u, where u is a quarter-turn rotation. Normalize a coarse record
heading to north and rotate the fine coordinate frame by u relative to the
coarse frame. Every nine-step image then has displacement three times its
coarse unit step.

1. A feasible nine-step image has maximum northward read offset at most4.
   If its endpoint displacement is not north, the maximum is at most2.
   A north-displacement image followed by an east-displacement image, with
   the first image starting at(0,-3) and all first reads in y>=0 white, has
   exactly six possible literal pairs. Every pair has NO first-image read in
   y>=0, reaches the junction with heading north, and its second word is

       A = RRLRRRRLR.

2. There is no physically alternating nine-image refinement of the coarse
   word A whose first image is A and whose coarse/fine entry headings are
   both north. The complete search has635 nodes and8,877 conflicts, with no
   extension beyond six completed images. All initial colors below the
   relevant fresh-record constraint remain unrestricted in this second test.

These facts were regenerated with independent complex-coordinate geometry in
computability/check_position_k9_record_independent.py/json and analytically
reviewed by the auditor. The local inventory allows opposite fine/coarse
boundary headings; only the heading axes have to agree in the normalized
frames.

## Why an affine time phase adds no heading-axis case

In nine steps, an entry heading on the vertical axis produces five horizontal
moves and four vertical moves. Thus its net horizontal displacement is odd and
its net vertical displacement is even. An entry heading on the horizontal axis
has the opposite displacement parities. Therefore an image with displacement
three times a coarse unit step has entry heading on the same axis as the
coarse pre-turn heading, after applying the spatial rotation u.

This conclusion follows from the endpoint identity alone. Since heading axis
alternates at every update, (1) also forces c congruent to the quarter-turn
index of u modulo2. Inconsistent phases are impossible already geometrically;
consistent phases are exactly those covered by the imported local inventory.

## Fresh-record proof

Choose an unbounded coordinate direction of the physical trajectory. Finite
support implies the usual finite-domain escape theorem, so at least one such
direction exists. Rotate its coarse frame to north. Choose a record level Y
so large that:

- the coarse first hit t of level Y occurs after N+1;
- both the coarse level Y and its image fine level 3Y+beta are beyond all
  initial black cells in their respective outward directions;
- the finite uncontrolled fine prefix before 9N+c stays strictly below the
  image fine level; and
- the next image record is also beyond those finite exceptional sets.

Here beta is the north component of b in the fine frame. Only finitely many
bounds are imposed, and arbitrarily large coordinate records exist.

Before the coarse record predecessor n=t-1, every earlier coarse center at
height Y-1 has a non-north endpoint displacement, so its fine read heights are
at most

    3(Y-1)+beta+2 < 3Y+beta.

All lower centers have fine heights at most

    3(Y-2)+beta+4 < 3Y+beta.

Together with the bounded uncontrolled prefix, this makes the entire fine
half-plane y>=3Y+beta pristine immediately before the record predecessor.
At coarse time t the turn is R, because the coarse record cell is fresh and
not initially black. The imported six-pair certificate therefore implies that

    s = 9t+c

is the FIRST fine visit to level 3Y+beta, with outward heading, and the next
nine turn letters are A. In particular this is another genuine global
coordinate record, now in the direction rotated by u.

Apply the same reasoning to this record at time s. Its corresponding first
fine record is at time 9s+c, with heading rotated by u again, and its next
nine letters are also A.

Finally, for every j=0,...,9, subtract two instances of(1):

    p(9s+c+9j)-p(9s+c) = a [p(s+j)-p(s)].

In the successive coarse/fine frames this is exactly the relation defining
an A-root nine-image refinement of A, with both normalized entry headings
north. The 81 fine turns starting at9s+c are physically feasible because they
are part of the actual trajectory. This contradicts imported fact2.

No shifted whole trajectory is asserted to satisfy a pure inflation law.
Only two applications at genuine records and the displayed finite-block
identity are used. Translation b cancels in that identity, and the time
phase c is retained throughout. QED.
