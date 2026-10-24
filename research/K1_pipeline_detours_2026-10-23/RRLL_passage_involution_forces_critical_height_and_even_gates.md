# RRLL passage is an involution: critical height and even irreducible gates

24 October 2026. Complete WHITE cap-four translating front, actual full
P,d and positive output. Physical RRLL-strip geometry is assumed; no K1,
root-free or sign-homogeneity premise. Pending independent review.
This extends signed0cdec955 and uses the signed all-sign passage
permutation6e776346. It does not cover arbitrary axis-drift curves.

Use the signed strip coordinates and forced Z/A positive profiles:

    Z_k=(0,2k) SSNS; A_k=(1,2k) EEEW;
    B_k=(1,2k+1) SSSN(+) or SNSS(-);
    Y_k=(0,2k+1) WWEW(+) or EWWW(-).

There are4a middle vertices, actual winding+1 and d=(0,-2a). For passage
F, the input index is the middle-arrival/offside-exit read A_i and the
output is the next offside-entry/middle-departure read D_(F(i)). All
statements below use PHYSICAL lifted cells and actual event times, not
phase residues or a smaller quotient.

## 1. Literal unit faces isolate fixed points and transpositions

The complete directed boundary ports give the following actual factors.
The intermediate R0/L3 reads stay on the relevant side of gamma, so
there is no omitted middle entry before the stated endpoint.

If Y_(k-1) is positive:

    Z_k.L1 -> A_k.R0 -> B_(k-1).R0 -> Y_(k-1).R0 -> Z_k.R2.

Thus F(Z_k)=Z_k. If Y_(k-1) is negative:

    Z_k.L1 -> A_k.R0 -> B_(k-1).R0 -> Y_(k-1).L1,
    Y_(k-1).R2 -> Z_k.R2.

Therefore F(Z_k)=Y_(k-1) and F(Y_(k-1))=Z_k, an exact physical
transposition with zero net displacement.

If B_k is positive:

    A_k.L1 -> B_k.L3 -> Y_k.L3 -> Z_k.L3 -> A_k.R2,

so F(A_k)=A_k. If B_k is negative:

    A_k.L1 -> B_k.L1,
    B_k.R2 -> Y_k.L3 -> Z_k.L3 -> A_k.R2,

so F(A_k)=B_k and F(B_k)=A_k. Both possible Y modes have the required
third-port L3, and all B modes have the displayed required rank, so no
free sign is silently fixed.

These formulas hold for EVERY physical translate. Their fixed points
and two-cycles are disjoint. By bijectivity of F, the remaining set is
F invariant and consists ONLY of positive free B/Y vertices.

## 2. Positive-only residual cycles have nonpositive homology

For a remaining vertex i, positivity means A_i<D_i. Since F(i) chooses
the FIRST D event after A_i, its own D_i is an available candidate and

    D_(F(i))<=D_i,

with equality only if F(i)=i as an actual physical event. On a quotient
F cycle lifting by q full translations this monotonicity gives q<=0;
the corresponding side-cycle homology is q because gamma has winding+1.
No return span is assumed to be <P.

Every already isolated fixed point or transposition has homology zero.
The total side-cycle homology is1-w=0 by the signed physical flow split.
It follows that EVERY residual cycle has q=0. The inequalities on that
finite cycle must therefore all be equalities, forcing F(i)=i at every
remaining physical vertex.

Thus F is EXACTLY the involution consisting of the unit transpositions
from negative B/Y contacts and fixed points everywhere else. There is
no hidden essential or nonzero-winding side cycle, or drift-period
translate left in this RRLL partial repair. Zero-homology paths need
not be embedded or geometrically primitive.

## 3. Critical height and even gate count

Both physical side currents now have homology zero. With w=+1 their
signed stream jumps are c-2-c_left and c_right-c+1. Therefore EVERY RRLL
strip, even when mixed, has

    c=c_right+1.

Let n_minus count negative free B/Y classes in the actual full quotient.
There is one F transposition for each and all other points are fixed, so

    beta_gamma=4a-number_of_cycles(F)=n_minus.

The signed partial-repair parity makes n_minus EVEN. The full graph has
beta>=n_minus, but this is not an upper bound or a separate fuel payment.
The parallel unit gates are genuinely irreducible: their two Delta
values differ by4, not0, and their unit node has no other graph edge.
They are not removed by matched-port erasure.

There must also be at least two positive free B/Y contacts. If all2a
were negative, the signed whole-period identity would give P=12a,
although the4a distinct four-read gamma classes alone require16a reads.
So n_minus<2a; evenness gives n_minus<=2a-2. This is a dependent role
constraint, not an existence assertion. For a=1 the strip is necessarily
homogeneous positive.

## 4. Minimum-boundary consequence and exact live scope

Signed2b33fcce forces a G3 circle incident to ANY locally minimal L
plateau to have RRLL geometry, even with odd corners. Hence such a circle
is not only axis and positive but also has

    right C level c_right+1,
    low L level c_left-1.

At other heights, every G3 cycle has a lower neighboring L face or is
not a minimum boundary. Negative-winding circles are already known to
be genuinely mixed and cannot be RRLL. The remaining general mixed
geometry is not excluded.

RRLL negative free gates survive as exact nested unit brackets and
zero-homology partial side cycles. These closed excursions may reuse
physical cells or have different headings; no physical splice, fresh
root, original-fuel budget, generic controller or WHITE-front positive
is produced. Prepared W20 remains prepared-only. Positive output may
occur inside the remaining closed free excursions, and no upper bound
on that production is established here.
