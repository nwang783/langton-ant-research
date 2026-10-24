# A nonnegative completed-cap change when A is initially white

Working proof, 21 October 2026. This is an exact consequence of the fresh-cap
scattering decomposition. Two other analysis independently reviewed the run
classification, the history charge, and the final accounting within this
session and found no gap. This is internal review, not external peer review
or proof-assistant verification. It does not yet prove eventual highway capture.

## 1. Statement and conventions

Use the notation

    T_r=(r,-r), A_r=(r,-1-r), B_r=(r,-2-r), C_r=(r,-3-r).

Take a finite actual ant segment that starts and ends at x+y<=-4, stays at
x+y<=0, and has the heading sector in which T is approached with heading E.
The whole row A is initially white. The initial colors on all other rows are
arbitrary. Initial black support need not be finite. Only visited cells enter
the sums below.

Let M be the number of T events. Let Delta_A, Delta_B, Delta_C be net changes
in black count on their rows. Let L_C count black C events arriving N and
departing W (lower corners). Then

    7 Delta_A - 4 Delta_B + Delta_C <= 8M - L_C.

In particular,

    7 Delta_A - 4 Delta_B + Delta_C <= 8M.

With the earlier notation D=D_0 and Z=Z_0 (there are no A bridges), this is
equivalent to

    N_A - N_C - 8D - 4Z <= -L_C <= 0.

The proof retains the initially old colors on B and C. Freshness of A is
essential; it is used in the history charge in Section 5.

## 2. Upper excursions and upper runs

Every C upper excursion goes from one C cell to the next C event, with no C
event in its interior. The fresh-A scattering decomposition gives two forms:

* A short excursion goes from C_r to C_(r+1) through a white lower B corner,
  and has length two.
* A nontrivial excursion goes from C_r to C_(r-k), for k>=0. It contains
  k+1 black lower A events, k extra white B upper corners, and j top diamonds,
  where j is 0, 1, or 2. There is at most one top diamond at each endpoint.

Call a nontrivial excursion with k=0 a zero excursion, and one with k>0 a long
excursion. The word `zero` refers only to its displacement on C. Every zero
excursion is a literal first return to its initial C cell.

A C upper run starts at a white C event arriving N from below, follows one or
more upper excursions, and ends at a white C event arriving S from above.
Its internal C events are black upper corners. All other C events in the
whole segment are black lower corners. Runs are complete because the whole
segment starts and ends below C.

For one run let P count its short excursions, R its long excursions, D the
sum of the k values of its long excursions, and M its top visits. These local
symbols sum to the corresponding whole-segment counts. A run with n upper
excursions has two white C events and n-1 black C events, hence contributes
3-n to Delta_C.

A short excursion contributes Delta_B=1. A nontrivial excursion with
parameters k,j contributes

    Delta_A = 2j-(k+1),
    Delta_B = k-2+j.

Thus its contribution to 7Delta_A-4Delta_B-8M is 1+2j-11k. After including
the C events, the exact contribution of a whole upper run to

    S := 7Delta_A-4Delta_B+Delta_C-8M

is

    S_run = 3+2M-5P-11D.                         (1)

Consequently S=sum_runs S_run-L_C.

## 3. Zero excursions can occur only at the ends of a run

A zero excursion reverses the color of its C endpoint between its two
visits. If it starts at an internal C event, that event is black. Its return
is therefore white and ends the run. If it starts at the first C event, its
return is black, and the run must continue. A zero excursion can therefore
occur only first or last. There are at most two.

For a zero excursion based at C_(s-1), let z_ab record its two optional roofs:

* a=1 means a right diamond at B_s through T_(s+1);
* b=1 means a left diamond at B_(s-1) through T_s.

Its selected black A event is at A_s. At the end of the excursion the three
cell colors are

    B_s has color a, A_s has color b, B_(s-1) is white,

where 1 means black. If this zero excursion is first in a run, its C return
is black and the next departure is E.

* If a=0, the next excursion is a short through white B_s.
* If a=1,b=0, the next path reaches T_(s+1) for a second time and leaves the
  cap. This is impossible in the completed capped segment.
* If a=b=1, the next path goes through black B_s, black A_s, and white
  B_(s-1). The last corner is extra because its top diamond was already used.
  Thus the next excursion is long, and it has no right diamond.

In particular two zero excursions cannot be consecutive, and each run has
P+D>=1.

There is a complementary restriction at the other end. If a terminal zero
excursion follows a short, its left B cell has just been read white by that
short and is now black. It cannot have a left diamond, so b=0. If a terminal
zero excursion has two diamonds, its predecessor must be long and that long
excursion cannot have a left diamond: both left diamonds would use the same
top cell.

Each long excursion has at most two diamonds. An endpoint zero excursion
with at most one diamond adds at most one. An endpoint zero with two diamonds
forces the adjacent long excursion to lack its corresponding endpoint
diamond. When the same long excursion meets both endpoint zeros, the two
missing diamonds are its two different endpoint diamonds. Therefore

    M <= 2R+2 <= 2D+2.                           (2)

If D=0, all the moving excursions are short. The initial zero, if present,
has a=0, and the terminal zero, if present, has b=0. Hence M<=2.

## 4. The only runs with positive S_run

If D>=1, equations (1) and (2) give

    S_run+2P <= 7-7D-3P <= 0.                    (3)

If D=0 and P>=2, then M<=2 and S_run<=7-5P<0.

If D=0 and P=1, equation (1) reads S_run=2M-2. Thus the only positive case is

    D=0, P=1, M=2, S_run=2.                      (4)

Call this a positive run. For a unique index s, it consists of

    zero z_01 at C_(s-1),
    short through B_s from C_(s-1) to C_s,
    zero z_10 at C_s.

Its two top visits are T_s and T_(s+2). At its start A_s is black. At the
start of its last zero excursion A_(s+1) is white. No part of the run before
that last zero touches A_(s+1), so this cell is white at the run's start too.

## 5. Every positive run forces an earlier short

Fix a positive run at index s. All A cells were initially white. Before the
run, T_s and T_(s+2) have not been visited, because the run visits them and
top visits are unique.

The only earlier white event possible at A_s is its departure to T_(s+1).
Since A_s is black at the positive run's start, that departure must have
occurred, and there was no subsequent black A_s event. Thus T_(s+1) was
previously visited, and A_s stayed black from its one earlier white event
until the positive run starts.

The middle top visit arrived at A_(s+1) on white and left it black. Before the
positive run starts, A_(s+1) must be white again. Its other white port, the
departure to T_(s+2), has not yet occurred. Consequently it had exactly one
intervening black event, arriving N and departing W to B_s.

At that black erasure of A_(s+1), B_s must be black. If B_s were white, the
ant would turn N to A_s and erase its black state, which cannot be restored
before T_s is visited in the positive run. A black B_s event instead turns
S and leaves B_s white.

At the positive run's start, its first zero enters B_s on black. There must
therefore be a B_s visit between the above erasure and the positive run.
Take the first such visit. It is white. It cannot arrive W and turn N, since
that would again erase A_s. Hence it arrives E and turns S: it is a short
C upper excursion through B_s.

Assign this earlier short to the positive run. Different positive runs have
different indices s, since otherwise they would repeat the top visits T_s
and T_(s+2). Their assigned shorts occur at different B cells and are
therefore distinct. Every positive run has one assigned short, and every
short receives at most one assignment.

## 6. The earlier shorts supply enough negative contribution

For each upper run let c be the number of its shorts assigned to later
positive runs. Clearly c<=P. By (3), any run with D>=1 satisfies

    S_run+2c <= 0.

Consider a run with D=0. If its first short is preceded by an initial zero
with one top diamond, that zero is z_01. If the short is at B_s, the zero
visits T_s. This short cannot be assigned to a later positive run at index s,
since that later run would have to visit T_s again. Likewise, if its last
short is followed by a terminal zero with one diamond, that zero is z_10
and visits T_(s+2), so that short cannot be assigned to a later positive run
at index s.

If P>=2, the first and last shorts are different. Every one of the M<=2 top
diamonds rules out a different endpoint short. Thus c<=P-M, and

    S_run+2c <= 3+2M-5P+2(P-M) = 3-3P <= 0.

For P=1 and M=0, S_run=-2 and c<=1, so the same bound holds. For P=1 and M=1,
S_run=0 and the endpoint diamond forces c=0. For a positive run (P=1,M=2),
the unique short cannot be assigned, c=0, and S_run+2c=2.

Let B be the number of positive runs. The injective assignment in Section 5
gives sum_runs c=B. Summing the preceding inequalities gives

    sum_runs S_run <= 2B-2 sum_runs c = 0.

Since S=sum_runs S_run-L_C, the theorem follows.

## 7. Scope

The proof uses no simulation bound or period assumption. It is an inequality
for finite completed excursions under a fixed cap with A initially white.
It is not yet a bound for an unfinished record prefix. It also cannot be
applied to arbitrary old A merely by checking H=0: the earlier history
charge requires that the black state at A_s came from a prior top visit.

The coefficient combination is relevant to shifts of a cap by two diagonals,
but a global proof still must account for the incomplete tail and for how
the row roles change. No global telescoping claim is made here.
