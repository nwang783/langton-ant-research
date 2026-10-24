# Recurrent support and boundary exclusion dynamics

22 October 2026. This is an exact reformulation and a scoped necessary-condition theorem, not a highway proof. No claim of literature priority is made. The purpose is to isolate chronology not seen by static mass and clock identities.

## 1. Fixed directed lattice

Normalize the checkerboard sector so that an even cell has vertical incoming headings and horizontal outgoing headings. An odd cell has horizontal incoming headings and vertical outgoing headings. Each undirected lattice edge therefore has one globally permitted orientation. The opposite orientation is never traversed by this orbit.

At a cell, two successive visits have opposite turn letters. They consequently share either their incoming directed edge or their outgoing directed edge. They cannot use two disjoint pairs of incident edges.

## 2. Recurrent support has degree at least three

Let an edge be recurrent when it is traversed infinitely often, and let R be the set of cells visited infinitely often. At every v in R there is at least one recurrent incoming edge and at least one recurrent outgoing edge, since each of these two sets has only two edges.

If exactly one incoming edge is recurrent, then after some time every visit uses it. Alternating turn letters force both outgoing edges to recur. Dually, if exactly one outgoing edge is recurrent, then alternating turn letters force both incoming edges to recur. Thus every recurrent vertex has at least three incident recurrent edges.

In particular, the induced nearest-neighbor graph on R has minimum degree at least three. Its complement is closed under the following two-neighbor rule: a site outside the complement cannot have two nearest neighbors in the complement.

If R is nonempty and contained in a horizontal strip of finite height, its topmost recurrent row is an ENTIRE horizontal line, and the row immediately below it is also entirely recurrent. Indeed the north neighbor of each recurrent site on the top row is not recurrent; all three other neighbors must therefore be recurrent. Horizontal propagation gives the whole row and then the row below. The analogous assertion holds at the bottom. A vertical-strip statement follows by rotation.

This is a restriction on the recurrent set, not on every visited site. It does not prove that R is empty. A full two-row strip already has graph-theoretic minimum degree three, so the degree condition alone cannot settle axial recurrence.

## 3. Exact top-boundary exclusion process

For an interval during which the ant never crosses above a horizontal row, ignore a possible incomplete first or last passage. Each completed visit to that row enters from below, reads two horizontally adjacent cells, and returns below. Translate the x coordinate so the vertical-arrival sites are 2i and write

    E_i = black bit at (2i, row),
    O_i = black bit at (2i+1, row).

For an incoming north heading, a reflecting passage is precisely one of:

    E_i=0 and O_i=0:       (E_i,O_i) goes from (0,0) to (1,1),
    E_i=1 and O_(i-1)=1:  (O_(i-1),E_i) goes from (1,1) to (0,0).

If the required neighboring bit differs, the second turn exits upward and the passage is not reflecting. No condition is imposed on other cells.

Now complement the odd sites only:

    eta_(2i)=E_i,      eta_(2i+1)=1-O_i.

Every reflecting passage is exactly a nearest-neighbor exclusion move

    01 -> 10.

A particle moves one site to the left. The alternating all-white physical row becomes the alternating particle vacuum 010101..., not an empty particle configuration. Therefore finite initial black support is a finite perturbation of a vacuum with infinitely many particles and holes, not a finite fuel supply.

The signed first moment of the physical row decreases by exactly one at every completed reflecting passage:

    sum_x x (-1)^x black(x,row)  changes by -1.

This identity is finite at each time for a finite-support ant. It can decrease without bound by exporting state along the row, so it is not a global bounded resource.

## 4. Exact current constraints

Let A_i count white-type updates at vertical-arrival site 2i and D_i count black-type updates there over a complete episode. Then

    E_i(t)-E_i(s) = A_i-D_i,
    O_i(t)-O_i(s) = A_i-D_(i+1).

Both left sides lie in {-1,0,1}. Hence A_i and D_i differ by at most one, and A_i and D_(i+1) differ by at most one. Infinite activity at one such site forces infinite activity at each neighboring vertical-arrival site, and inductively everywhere along that boundary row, provided each fixed boundary site has only finitely many outward visits. This also rederives the recurrent-row conclusion with exact chronological accounting.

The bottom boundary produces the reflected, opposite-direction exclusion process. A proof excluding indefinitely coupled currents on the top and bottom would be a genuinely new route to the axial-strip problem, but no such coupling theorem has been established here.

## 5. What this does and does not add

The formulation retains the exact two-cell chronology at a boundary. It is stronger than treating arbitrary row colors as fresh or charging raw black mass. It also diagnoses why a tempting boundary-particle budget fails: its natural vacuum is infinite.

No bounded-retreat premise, eventual periodicity, standard-word classification, finite defect budget, or finite return theorem follows from these statements alone. In particular, the abstract exclusion process admits sustained currents from its alternating vacuum; ant-specific coupling to the other rows remains essential.
