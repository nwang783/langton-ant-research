# Internal coarse-lattice overlap is necessary for rectangular direction models

2026-10-23 00:07 UTC. Status: independently analytically reviewed on 2026-10-23 at 00:12 UTC.
This is an all-length finite-support obstruction, not a bounded substitution scan.
It applies even when the four direction images are chosen independently.

## Hypotheses

Let phi be an odd-length k>1 substitution on absolute movement directions
E,N,W,S, prolongable on E, with:

- Every image starts with its own letter: F(d)=d.
- Every image alternates move axes and starts on the axis of d.
- The total displacement of phi(d) is A d, where A=diag(a,b), a,b>1 integers.
- Every internal prefix displacement of every image avoids A Z^2.

The images need NOT obey phi(-d)=-phi(d). No assumption is made that the last-letter
map is a permutation. The integrated fixed-point path has p(0)=0 and first move E.
Either perpendicular initial heading N or S is allowed.

THEOREM: this path cannot be realized by a classical ant from finite black support.
Therefore a finite-support example in this class must have an internal macro read
on the coarse lattice A Z^2. Independent direction images and last-letter collapse
alone cannot evade the obstruction without such overlap.

## 1. Exact first-visit inheritance

The affine geometry gives p(kn)=A p(n). Coarse-lattice avoidance gives

    p(t) in A Z^2 iff k divides t,
    n is a first visit iff kn is a first visit.

These are the same exact arguments as in `matrix_coarse_vertex_obstruction.md`.
Let L(d) be the final movement direction of phi(d). Since k is odd, L preserves
the two axes, but may collapse both opposite directions to one.

For n>0 the incoming/outgoing pair (e,d) at read n becomes (L(e),d) at read kn:
the outgoing direction is unchanged because F is identity. All scaled reads of
any nonzero first-visit cell occur at distinct first-visit cells A^r p(n).

Two consequences under finite support are crucial:

(A) If a nonzero first read is R with incoming direction e, then L(e)=e.
    Indeed if L(e)=-e, its iterates on the two-element axis either alternate
    e,-e forever or remain forever at -e. The fixed outgoing direction d=J e
    then makes infinitely many scaled first reads L, a contradiction.

(B) If L(e)=e, no nonzero first read with incoming e can be L.
    Such a first L would remain L under every scale and require infinite support.

Here J is the clockwise quarter turn. These deductions retain the complete
chronology of first visits; they do not infer an initial color from a finite
sample of an arbitrary path.

## 2. What unbounded coordinate records force

For any finite-support ant, a sufficiently high north-coordinate record enters
an initially white, never-read cell with incoming N. Its R turn moves east to a
second never-read cell on that same new row, whose incoming heading is E.
Thus unbounded north records force L(N)=N and L(E)=E by (A).
Rotate this exact two-fresh-cell argument:

    unbounded east:  E,S are fixed by L;
    unbounded south: S,W are fixed by L;
    unbounded west:  W,N are fixed by L.

The first record cells and their neighbors can be chosen nonzero and beyond
all initial black support. Opposite unbounded coordinate directions therefore
force L to be the identity on all four headings.

## 3. Bidirectional coordinates are impossible

Because a,b>1 and p(k^r n)=A^r p(n), any positive (negative) coordinate value in
one finite prefix makes that coordinate unbounded positively (negatively).
If x takes both signs, or y takes both signs, Section2 fixes all four directions.
By (B) the only possible initially black visited cell is the origin.

From the empty seed or the singleton-origin seed, the first four movement steps
form a unit square and return to the origin. The respective relative turn words
are RRRR or LRRR. This remains true for any initial heading. Hence p(4)=0 belongs
to A Z^2, but coarse-lattice separation requires k|4. Odd k>1 cannot divide4.
This contradiction does not require an asymptotic highway theorem.

## 4. The remaining two quadrants also fail

The first position is (1,0), so positive x occurs. With bidirectional coordinates
excluded, x>=0 throughout. Some y coordinate is nonzero because axes alternate.
Thus the path must lie either in the NE quadrant x,y>=0 or in the SE quadrant
x>=0,y<=0. By positive diagonal scaling, both outward coordinate directions are
unbounded, even if only one finite witness position is initially known.

NE case: north and east records force L(N),L(E),L(S) fixed. At time1 the head is
at the nonzero fresh cell (1,0) incoming E. Staying in y>=0 requires its first
turn to be L, because R would move south to (1,-1). This contradicts (B) for E.

SE case: east and south records force E,S,W fixed by L. By (B), the nonzero fresh
cells (1,0), (1,-1), (0,-1) must each turn R, with incoming headings E,S,W.
They are precisely the next three cells following the first E move. Thus time4
returns to the origin, again contradicting coarse separation and k∤4.
The initial origin may turn either R or L; the first movement was prescribed E,
and the subsequent three-read argument is unchanged.

All cases are impossible, proving the theorem.

## Boundaries

The theorem does not cover first-letter maps other than identity, nonpositive or
nondiagonal A, even k, phase-coupled fixed points, or any internal A-lattice read.
It does not prove that every finite-seed ant has all four fresh incoming headings
infinitely often. Only the stated coordinate-record implications are used.
It does not claim that overlap candidates actually work.
